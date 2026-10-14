# review row visual QA

Selected source: `decoded/review.png` (2172 × 724), generated as one coherent transparent six-frame strip with built-in `image_gen__imagegen`. Reference inputs were the canonical base, original identity sheet, six-slot guide, and approved `running.png` used only for separation/scale. Exact prompt: `prompts/rows/review.actual.md`.

## Structural evidence

Ran bundled `extract_strip_frames.py --method auto` and `inspect_frames.py --require-components`. The actual `review.json` reports `ok: true`, 6 expected / 6 actual frames, `components` extraction, no errors and no warnings.

All frames are 192 × 208. All six occupied baselines are y=203, and all frames have zero edge pixels and zero chroma-adjacent pixels. Top bounds are y=5–10, matching a small inspection lean/nod. Widths are 119–122 pixels, with safe side padding.

## Visual evidence

Inspected the full strip and all six extracted native frames.

- Each frame contains one complete separate figure. Hair, ears, sleeves, ribbons and both boots remain complete. Transparent gutters separate every source figure without the bridges seen in the earlier working-strip failure.
- Both hands are gathered together in front below the waist bow, with wrists naturally meeting the two sleeve cuffs. There are no extra hanging hands, third hand, detached fingers or residual base-pose hands. The lightly overlapping hands do not add a limb.
- Frame 00 is upright and attentive. Frames 01–02 pitch the head and upper body down to inspect. Frame 03 clearly tilts the head while continuing the downward glance. Frame 04 gives a closed-eye satisfied nod with a small smile. Frame 05 returns upright and open-eyed toward the opening pose.
- This differs visibly from working: no hand is at the chin, and the animation is inspection lean / checking / confirmation rather than sustained thought. Both boots remain planted, with no walking or raised knees.
- The front red bow stays at the abdomen. Silver hair, fox ears, amber eyes, embroidered white/red costume and detailed boots retain the canonical identity. No rear bow, new accessory, paper, book, magnifying glass, symbol, label, guide mark, shadow or loose effect is present in the extracted native frames.
- The source figures are larger than the prompt's 45–50% height target, but the purpose of that instruction is met: all six figures have uninterrupted transparent separation and safe full-body padding. No structural defect results.

Disposition: first attempt passes initial structural and visual QA; no failure revision was needed. Parent owns final cross-row scale, playback-loop review and final atlas acceptance. No global manifest or unrelated file was changed.
