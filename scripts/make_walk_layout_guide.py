"""Create a pose/layout guide only; no character pixels or final artwork."""
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/2026-10-14-upgrade/run/references/walk-pose-guide.png"

# Coordinates describe one anatomical near leg (blue) and far leg (orange).
# The second half reverses their contact/passing roles. Imagegen draws the pet.
near = [
    ((118, 342), (137, 380)), ((105, 346), (112, 380)),
    ((94, 344), (91, 380)), ((82, 339), (70, 375)),
    ((75, 341), (61, 380)), ((78, 338), (73, 365)),
    ((109, 332), (120, 355)), ((125, 345), (142, 380)),
]
far = [near[index] for index in (4, 5, 6, 7, 0, 1, 2, 3)]
guide = Image.new("RGB", (1536, 512), "white")
draw = ImageDraw.Draw(guide)
for index in range(8):
    offset = index * 192
    draw.rectangle((offset + 4, 8, offset + 188, 504), outline="#cccccc", width=1)
    draw.ellipse((offset + 69, 198, offset + 123, 252), outline="#777777", width=3)
    draw.line((offset + 96, 252, offset + 96, 310), fill="#777777", width=5)
    for color, poses in (("#db7519", far), ("#175bb8", near)):
        knee, foot = poses[index]
        draw.line([(offset + 96, 310), (offset + knee[0], knee[1]),
                   (offset + foot[0], foot[1])], fill=color, width=5)
        draw.line((offset + foot[0] - 3, foot[1], offset + foot[0] + 12, foot[1]),
                  fill=color, width=5)
    draw.text((offset + 7, 20), f"{index + 1}: near=BLUE far=ORANGE", fill="#444444")
    draw.line((offset + 45, 384, offset + 157, 384), fill="#bbbbbb", width=1)
OUT.parent.mkdir(parents=True, exist_ok=True)
guide.save(OUT)
print(OUT)

# A second strategy makes the two hip-to-knee chains spatially distinct.
# This is an abstract guide, not a drawn or warped version of the pet.
march = Image.new("RGB", (1536, 512), "white")
pen = ImageDraw.Draw(march)
left = [((85, 330), (99, 347)), ((84, 340), (96, 365)),
        ((82, 351), (80, 380)), ((82, 351), (80, 380)),
        ((82, 351), (80, 380)), ((82, 351), (80, 380)),
        ((82, 351), (80, 380)), ((84, 338), (96, 363))]
right = [((111, 350), (116, 380)), ((111, 350), (116, 380)),
         ((111, 350), (116, 380)), ((110, 338), (125, 363)),
         ((110, 330), (126, 347)), ((110, 340), (124, 365)),
         ((111, 350), (116, 380)), ((111, 350), (116, 380))]
for index in range(8):
    offset = index * 192
    pen.rectangle((offset + 4, 8, offset + 188, 504), outline="#cccccc")
    pen.ellipse((offset + 69, 198, offset + 123, 252), outline="#777777", width=3)
    pen.line((offset + 122, 223, offset + 134, 226, offset + 122, 230),
             fill="#777777", width=3)
    pen.polygon([(offset + 83, 254), (offset + 108, 254),
                 (offset + 111, 310), (offset + 80, 310)], outline="#777777", width=3)
    for color, poses, hip in (("#175bb8", left, (85, 310)),
                              ("#db7519", right, (108, 310))):
        knee, foot = poses[index]
        pen.line([(offset + hip[0], hip[1]), (offset + knee[0], knee[1]),
                  (offset + foot[0], foot[1])], fill=color, width=5)
        pen.line((offset + foot[0] - 3, foot[1], offset + foot[0] + 12, foot[1]),
                 fill=color, width=5)
    pen.text((offset + 7, 20), f"{index + 1}: left=BLUE right=ORANGE", fill="#444444")
    pen.line((offset + 45, 384, offset + 157, 384), fill="#bbbbbb")
march_path = OUT.with_name("march-pose-guide.png")
march.save(march_path)
print(march_path)
