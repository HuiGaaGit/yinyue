"""Write or verify a byte-exact, repository-relative continuation snapshot."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/checkpoint-manifest.json"
SCOPES = ["outputs/2026-10-14-upgrade", "tools/pet-pipeline", "docs", "scripts",
          "README.md", "AGENTS.md", "requirements.txt", "pet.json", "spritesheet.webp",
          ".gitignore", ".gitattributes"]


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def snapshot_files() -> list[Path]:
    files: set[Path] = set()
    for scope in SCOPES:
        target = ROOT / scope
        if not target.exists():
            raise FileNotFoundError(f"Snapshot scope is missing: {scope}")
        candidates = [target] if target.is_file() else target.rglob("*")
        for path in candidates:
            if not path.is_file() or path == MANIFEST:
                continue
            if "__pycache__" in path.parts or path.suffix in {".pyc", ".tmp"}:
                continue
            files.add(path)
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("snapshot", "verify"))
    args = parser.parse_args()
    if args.action == "snapshot":
        records = [{"path": path.relative_to(ROOT).as_posix(),
                    "bytes": path.stat().st_size, "sha256": digest(path)}
                   for path in snapshot_files()]
        payload = {"schema_version": 1, "checkpoint": "2026-10-14-upgrade",
                   "purpose": "File integrity for cross-computer continuation; not final artwork approval.",
                   "files": records}
        MANIFEST.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"ok": True, "files": len(records),
                          "bytes": sum(row["bytes"] for row in records)}, ensure_ascii=False))
        return
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors = []
    for row in payload["files"]:
        path = (ROOT / row["path"]).resolve()
        if not path.is_relative_to(ROOT):
            errors.append(f"Path escapes repository: {row['path']}")
        elif not path.is_file():
            errors.append(f"Missing: {row['path']}")
        elif path.stat().st_size != row["bytes"] or digest(path) != row["sha256"]:
            errors.append(f"Changed: {row['path']}")
    print(json.dumps({"ok": not errors, "files": len(payload["files"]),
                      "errors": errors, "scope": "checkpoint integrity"}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
