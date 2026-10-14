# running (working / thinking) row review

Selected source: `decoded/running.png` (2172 × 724), created with built-in `image_gen__imagegen` and transparent alpha. Canonical base, original identity sheet and six-slot guide were attached. Exact prompts are `prompts/rows/running.actual.md` and `prompts/rows/running.retry-01.md`.

## Repair history

The first strip had correct thinking semantics but the first two hair silhouettes touched. The actual bundled extraction grouped both characters into frame 00 and assigned a tiny four-pixel component to frame 04; `inspect_frames.py` returned `ok: false`. The original source, report and frames are preserved under `revision-01/`.

The selected second strip is one coherent generation that repairs spacing and figure scale while preserving the thinking poses. No frames from different sources were spliced. The six complete silhouettes are now separated by clear transparent gutters.

## Structural QA

Ran bundled `extract_strip_frames.py --method auto` followed by `inspect_frames.py --require-components`. Current `review.json` reports `ok: true`, 6 expected / 6 actual frames, extraction method `components`, no errors and no warnings. Every frame is 192 × 208 with zero edge pixels and zero chroma-adjacent pixels.

All six visible baselines are y=203. Bounding widths are 114–115 pixels. Top extents are y=5–8, supporting tiny head movement with constant apparent size and planted feet.

## Visual QA

Inspected the full source strip and all six extracted native-size frames.

- The state is recognizably mental work: one hand remains at the chin/jaw and the other supports the raised elbow. Both hands are attached naturally through the sleeves.
- Frame 00 is focused and open-eyed; 01 narrows and shifts the gaze slightly sideways; 02 lowers the gaze/head a little; 03 clearly closes both eyelids; 04 reopens with a concentrated expression; 05 returns toward the opening pose. This provides visible micro-animation distinct from plain idle.
- Both boots remain planted without raised knees, steps, hopping, arm pumping or lateral travel. There is no literal running.
- Silver hair, fox ears, amber eyes, white/gray embroidered sleeves, detailed boots and front red waist bow remain in the same design and placement. The supporting arm partly overlaps the waist area naturally; the bow never migrates to another location.
- All six figures are complete and separated. No guide marks, labels, props, paper, book, lightbulb, symbols, shadows, motion effects or detached fragments are visible at native size.

Disposition: passes initial row structural and visual QA. Parent still owns final atlas assembly, playback continuity, cross-row scale and overall acceptance. No global manifest or unrelated resource was changed.
