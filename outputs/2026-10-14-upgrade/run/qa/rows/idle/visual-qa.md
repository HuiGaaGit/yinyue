# Idle visual worker QA

- Selected source: `decoded/idle.png`, 2172 × 724 transparent PNG generated with the built-in image generator.
- Actual selected prompt: `prompts/rows/idle-retry-02-actual.md`.
- References attached: `references/canonical-base.png` (primary visual), `references/reference-01.webp` (old identity), and `references/layout-guides/idle.png` (spacing only).
- Frame count: exactly 6 complete poses in one row. Bundled extraction used connected components, producing 6 files at 192 × 208 in `qa/rows/idle/frames/idle/`.
- Structural check: `inspect_frames.py --require-components` returned `ok: true`, no errors and no warnings. All frames have 0 edge pixels and 0 chroma-adjacent pixels. Each bottom bound is y = 203; occupied heights are 198 pixels.
- Visual inspection: full source strip and extracted frames 00, 02, 05 viewed. Identity matches the approved polished anime chibi base: layered silver hair, fox ears, amber eyes, fine gray clothing trim, red obi and ribbons, decorated white calf boots. No palette or style regression to the old raster atlas.
- Action: front-facing calm pose, hands down and feet planted. Frame 01 has lowered eyelids and frame 02 shows a complete closed-eye blink; subsequent frames reopen the eyes and settle. Hair and ear micro-variation remains restrained. First and last poses are very close. No other state, props, detached decorative effects or shadows.
- Visual conclusion: selected source and extracted native-size poses pass this row's initial visual review. Final motion and cross-row registration still belong to parent assembly QA.

## Rejected first attempt

The first output crowded neighboring hair silhouettes together and clipped hair at the outside canvas edges. The automatic extractor produced four empty frames; `inspect_frames.py` correctly returned `ok: false`. This was a source spacing/clipping problem, not a registration issue. It was fixed by regenerating the whole strip with smaller figures and explicit broad transparent gaps. The rejected source and actual failed report are preserved as `source-rejected-01.png` and `review-rejected-01.json` here; no fixed-slot slicing was used.
