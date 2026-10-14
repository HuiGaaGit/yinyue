# Waiting visual worker QA

- Selected strip: `decoded/waiting.png`, 2172 × 724 PNG with transparent alpha, produced by built-in image generation.
- Selected actual prompt: `prompts/rows/waiting-respace-04-actual.md`.
- Selected generation attached the original waiting strip as the edit target, the approved canonical base, the old identity atlas, and the waiting layout guide. Canonical identity and polished rendering remain preserved.
- Exactly 6 complete waiting poses extracted by bundled `extract_strip_frames.py --method auto`; recorded method is `components`, not fixed-slot slicing.
- Bundled `inspect_frames.py --require-components`: `ok: true`, no errors and no warnings. All six frames are 192 × 208, foot bottom y = 203, 0 edge pixels, 0 chroma-adjacent pixels. Recorded occupied heights vary with the intended gentle head motion (190–198 pixels).
- Visual review performed on full source plus native-size frames 00, 02, 03, 05. All six preserve silver layered hair, fox ears, amber eyes, white embroidered clothing, red obi/ribbons and detailed white-silver boots.
- Waiting semantics read clearly: both hands meet at upper chest, softly expectant eyes and a small head tilt, blink then return. Feet remain grounded and torso stays centered. This is visibly different from idle's lowered hands. No hand-to-chin, wave, walk, deep bow, props or loose decorative effects.
- Anatomy: each selected pose shows two hands clasped at chest and no duplicate hands at lower sleeve corners. Lower sleeves are cloth only. First and last frames are close in pose and expression.
- Selected strip passes initial visual and structural review; final motion playback, row registration and full-atlas quality gates remain with parent assembly.

## Revisions and real failures

1. First source had correct waiting anatomy but neighboring hair silhouettes touched. Component extraction yielded one sparse frame and the real report failed. Saved as `source-rejected-01.png` and `review-rejected-01.json`.
2. Second source fixed spacing and passed structural checks, but visual inspection found duplicate lower hands in addition to clasped hands. It was rejected despite structural success. Preserved as `source-rejected-02-duplicate-hands.png` and `review-structural-only-02.json`.
3. A targeted duplicate-hand removal retained those extra hands, confirmed with a larger first-pose crop. Rejected and preserved as `source-rejected-03-duplicate-hands.png` and `review-structural-only-03.json`.
4. Strategy changed to the anatomically correct first source as the exact edit target, reducing source figure size and adding clean spacing. This selected fourth source has both correct anatomy and successful component extraction. No manual pet drawing or pixel invention was used.
