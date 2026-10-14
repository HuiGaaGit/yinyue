param(
    [string[]]$States = @('idle','running-right','running-left','waving','jumping','failed','waiting','running','review')
)

# Correct cross-row scale after the bundled connected-component extraction.
# The jump's larger source viewport includes 44 px of visible lift. Its settled
# body is 169 px tall; the other rows were independently fit to ~198 px. Apply
# one fixed transform to every frame of each non-jump row so their body scale
# matches the jump while preserving all generated pose differences.
# This performs layout/resampling only, not drawing or sprite composition.
# Final composition and all acceptance gates remain the bundled pet scripts.
$ErrorActionPreference = 'Stop'
$petRun = $PSScriptRoot
$petFrameCounts = @{idle=6; 'running-right'=8; 'running-left'=8; waving=4; jumping=5; failed=8; waiting=6; running=6; review=6}
$petRegisteredRoot = Join-Path $petRun 'qa/registered-frames'
New-Item -ItemType Directory -Force -Path $petRegisteredRoot | Out-Null
foreach ($petState in $States) {
    if (-not $petFrameCounts.ContainsKey($petState)) { throw "Unknown state: $petState" }
    $petSource = Join-Path $petRun "qa/rows/$petState/frames/$petState"
    $petDestination = Join-Path $petRegisteredRoot $petState
    $petSourceFiles = @(Get-ChildItem -LiteralPath $petSource -Filter '*.png' -File)
    if ($petSourceFiles.Count -ne $petFrameCounts[$petState]) { throw "Incorrect source frame count: $petState" }
    New-Item -ItemType Directory -Force -Path $petDestination | Out-Null
    if ($petState -eq 'jumping') {
        foreach ($petSourceFile in $petSourceFiles) {
            Copy-Item -LiteralPath $petSourceFile.FullName -Destination (Join-Path $petDestination $petSourceFile.Name)
        }
    } else {
        $petInputPattern = Join-Path $petSource '%02d.png'
        $petOutputPattern = Join-Path $petDestination '%02d.png'
        & ffmpeg -hide_banner -loglevel error -nostdin -y -start_number 0 -i $petInputPattern -vf 'scale=166:180:flags=lanczos,format=rgba,pad=192:208:13:28:color=black@0' -frames:v $petFrameCounts[$petState] -start_number 0 $petOutputPattern
        if ($LASTEXITCODE -ne 0) { throw "Frame registration failed: $petState" }
    }
    [pscustomobject]@{State=$petState; Frames=$petFrameCounts[$petState]; Destination=$petDestination}
}
