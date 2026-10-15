"""Layout reference from existing generated pixels; never a final pose source."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "outputs/2026-10-14-upgrade/run"
with Image.open(RUN / "references/canonical-base.png") as opened:
    base = opened.convert("RGBA")
    # Ignore alpha=1 background specks when locating the actual character.
    bounds = base.getchannel("A").point(lambda a: 255 if a > 16 else 0).getbbox()
    figure = base.crop(bounds)
figure.thumbnail((240, 320), Image.Resampling.LANCZOS)
guide = Image.new("RGBA", (3072, 1024), (0, 0, 0, 0))
for index in range(8):
    guide.alpha_composite(figure, (index * 384 + (384 - figure.width) // 2,
                                  (1024 - figure.height) // 2))
path = RUN / "references/look-spacing-guide.png"
guide.save(path)
print(path)
