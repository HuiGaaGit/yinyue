"""Abstract pose guide only: right foot steps out, left foot follows."""
from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
output = root / 'outputs/2026-10-14-upgrade/run/references/shuffle-pose-guide.png'
guide = Image.new('RGB', (2304, 768), 'white')
pen = ImageDraw.Draw(guide)
# Every tuple is (knee x, knee y, ankle x, ankle y); hips stay spatially separate.
left = [(122,540,112,620), (122,540,112,620), (137,530,143,580),
        (134,550,145,620), (122,540,112,620), (122,540,112,620),
        (137,530,143,580), (131,548,135,620)]
right = [(179,525,195,580), (181,550,203,620), (181,550,203,620),
         (165,550,173,620), (178,530,190,588), (181,550,203,620),
         (181,550,203,620), (165,550,170,620)]
for index in range(8):
    x = index * 288
    pen.ellipse((x+104,250,x+176,322), outline='#777777', width=4)
    pen.line((x+176,278,x+192,286,x+176,293), fill='#777777', width=4)
    pen.rectangle((x+126,324,x+162,432), outline='#777777', width=4)
    for hip, pose, color in ((128,left[index],'#175bb8'),(160,right[index],'#db7519')):
        kx,ky,ax,ay = pose
        pen.line([(x+hip,432),(x+kx,ky),(x+ax,ay)], fill=color, width=6)
        pen.line((x+ax-4,ay,x+ax+14,ay), fill=color, width=6)
    pen.text((x+12,25),f'{index+1}: BLUE=left hip, ORANGE=right hip',fill='#555555')
output.parent.mkdir(parents=True,exist_ok=True)
guide.save(output)
print(output)
