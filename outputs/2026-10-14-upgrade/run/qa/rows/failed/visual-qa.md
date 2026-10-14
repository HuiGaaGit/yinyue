# Failed strip visual QA

- Selected source: `decoded/failed.png` (2172 x 724, built-in image_gen, transparent background).
- Actual prompt: `prompts/rows/failed-actual.md`. Canonical base, old identity atlas and eight-slot guide were viewed and supplied to both attempts.
- First tool attempt returned `image generation failed: network error: error sending request` with no image. Retrying the same saved prompt and references succeeded. No visual content was fabricated to work around the network error.
- Bundled extraction with `--states failed --method auto` succeeded using connected components. Bundled `inspect_frames.py --states failed --require-components` returned `ok: true`, 8/8 frames, no errors or warnings; report `qa/rows/failed/review.json`.
- Viewed the complete strip and all eight native 192 x 208 frames. Sequence reads as mildly disappointed, ears flatten/downcast eyes, closed eyes with head lowered, hands together near chest, tiny-mouth sigh, eyes reopen/head lifts, ears/arms recover, relaxed return.
- All frames remain standing with two planted boots. Baseline bottom is 203 in every frame. Ear/head top bounds are 5, 11, 11, 11, 11, 9, 5, 5, consistent with ear droop rather than whole-character resizing. All native frames have zero edge pixels.
- Silver hair, fox ears, amber eyes, face, white/red outfit, embroidered sleeves, bow, red ribbons and detailed boots remain consistent. No extra arms, detached hands, changed clothing, sleep/collapse poses, tears, stars, X, text or motion effects observed in native frames.
- The image generator made the row taller than the requested 40–45% source occupancy and left low-opacity colored/white fringe material between apparent silhouettes in the large preview. Nevertheless, the authoritative component extractor recovered exactly eight separate full figures without fixed-slot slicing; inspected native frames show clean separation and complete long hair. No geometry repair was required.
- This is row-level acceptance; parent must perform final shared-scale, edge, contact-sheet, motion and exact-atlas checks.
