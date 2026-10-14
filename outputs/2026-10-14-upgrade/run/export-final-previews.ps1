param(
    [Parameter(Mandatory=$true)][string]$Atlas,
    [string]$SkillScripts = (Join-Path $PSScriptRoot '../../../tools/pet-pipeline/scripts')
)

# Crop only the exact final encoded atlas. Artwork is neither drawn nor changed.
$ErrorActionPreference = 'Stop'
$petFinalAtlas = (Resolve-Path -LiteralPath $Atlas).Path
$petPreviewRoot = Join-Path $PSScriptRoot 'previews'
$petEncodedFrames = Join-Path $PSScriptRoot 'qa/final-frames'
$petSpecs = @(
    @('idle',0,6), @('running-right',1,8), @('running-left',2,8),
    @('waving',3,4), @('jumping',4,5), @('failed',5,8),
    @('waiting',6,6), @('running',7,6), @('review',8,6),
    @('look-a',9,8), @('look-b',10,8)
)
New-Item -ItemType Directory -Force -Path $petPreviewRoot | Out-Null
foreach ($petSpec in $petSpecs) {
    $petFrameDirectory = Join-Path $petEncodedFrames $petSpec[0]
    New-Item -ItemType Directory -Force -Path $petFrameDirectory | Out-Null
    for ($petColumn=0; $petColumn -lt $petSpec[2]; $petColumn++) {
        $petX = 192 * $petColumn
        $petY = 208 * $petSpec[1]
        $petFramePath = Join-Path $petFrameDirectory ('{0:00}.png' -f $petColumn)
        & ffmpeg -hide_banner -loglevel error -nostdin -y -i $petFinalAtlas -vf "crop=192:208:${petX}:${petY},format=rgba" -frames:v 1 -update 1 $petFramePath
        if ($LASTEXITCODE -ne 0) { throw "Final frame export failed: $petFramePath" }
    }
}
& python (Join-Path $SkillScripts 'render_animation_previews.py') --frames-root $petEncodedFrames --output-dir $petPreviewRoot
if ($LASTEXITCODE -ne 0) { throw 'Bundled state-preview export failed' }

# Reuse the bundled preview encoder and its authoritative frame durations.
$petPreviewCode = @'
import json,sys,hashlib
from pathlib import Path
sys.path.insert(0,sys.argv[1])
from render_animation_previews import load_frames,save_preview,ROW_DURATIONS
root,out,atlas = map(Path,sys.argv[2:5])
all_frames=[]
all_times=[]
for state,times in ROW_DURATIONS.items():
    all_frames.extend(load_frames(root,state,len(times)))
    all_times.extend(times)
look=load_frames(root,'look-a',8)+load_frames(root,'look-b',8)
save_preview(look,[180]*16,out/'look-loop.gif')
save_preview(all_frames+look,all_times+[180]*16,out/'all-states.gif')
idle=load_frames(root,'idle',6)
jump=load_frames(root,'jumping',5)
save_preview(idle+jump+idle,ROW_DURATIONS['idle']+ROW_DURATIONS['jumping']+ROW_DURATIONS['idle'],out/'idle-jump-idle.gif')
record={'atlas':str(atlas),'sha256':hashlib.sha256(atlas.read_bytes()).hexdigest(),'source':'decoded final encoded atlas, fixed 192x208 cell crops','standard_frames':57,'look_frames':16,'previews':sorted(p.name for p in out.glob('*.gif'))}
(out/'preview-provenance.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
'@
& python -c $petPreviewCode $SkillScripts $petEncodedFrames $petPreviewRoot $petFinalAtlas
if ($LASTEXITCODE -ne 0) { throw 'Combined preview export failed' }
& ffmpeg -hide_banner -loglevel error -nostdin -y -i (Join-Path $petPreviewRoot 'all-states.gif') -vf 'format=yuv420p' -movflags +faststart (Join-Path $petPreviewRoot 'all-states.mp4')
if ($LASTEXITCODE -ne 0) { throw 'MP4 export failed' }

$petStills = Join-Path $petPreviewRoot 'stills'
New-Item -ItemType Directory -Force -Path $petStills | Out-Null
Copy-Item -LiteralPath (Join-Path $petEncodedFrames 'idle/00.png') -Destination (Join-Path $petStills '01-idle.png')
Copy-Item -LiteralPath (Join-Path $petEncodedFrames 'waving/02.png') -Destination (Join-Path $petStills '02-waving.png')
Copy-Item -LiteralPath (Join-Path $petEncodedFrames 'jumping/02.png') -Destination (Join-Path $petStills '03-jumping.png')
Copy-Item -LiteralPath (Join-Path $petEncodedFrames 'running/02.png') -Destination (Join-Path $petStills '04-thinking.png')
Write-Output $petPreviewRoot
