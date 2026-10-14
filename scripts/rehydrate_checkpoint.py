"""Rebase operational job/request paths to this clone without rewriting QA history."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "outputs/2026-10-14-upgrade/run"
FILES = [RUN / "imagegen-jobs.json", RUN / "pet_request.json"]
SUFFIX = "/outputs/2026-10-14-upgrade/run"
RELATIVE_PREFIXES = ("references\\", "decoded\\", "qa\\", "prompts\\", "final\\", "source\\")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    manifest = json.loads(FILES[0].read_text(encoding="utf-8"))
    old_run = str(manifest.get("run_dir", "")).replace("\\", "/")
    if not old_run.casefold().endswith(SUFFIX):
        raise SystemExit("Unrecognized job run_dir; inspect it before rebasing.")
    old_root = old_run[:-len(SUFFIX)]
    changed = 0

    def rebase(value):
        nonlocal changed
        if isinstance(value, dict):
            return {key: rebase(item) for key, item in value.items()}
        if isinstance(value, list):
            return [rebase(item) for item in value]
        if isinstance(value, str):
            normalized = value.replace("\\", "/")
            if normalized.casefold().startswith(old_root.casefold() + "/"):
                relative = normalized[len(old_root) + 1:]
                result = (ROOT / relative).as_posix()
            elif value.startswith(RELATIVE_PREFIXES):
                result = normalized
            else:
                return value
            changed += result != value
            return result
        return value

    for path in FILES:
        value = rebase(json.loads(path.read_text(encoding="utf-8")))
        if not args.dry_run:
            temporary = path.with_suffix(path.suffix + ".tmp")
            temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            temporary.replace(path)
    print(json.dumps({"ok": True, "dry_run": args.dry_run,
                      "operational_files": [path.relative_to(ROOT).as_posix() for path in FILES],
                      "rebased_values": changed, "run_dir": RUN.as_posix(),
                      "qa_history_rewritten": False}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
