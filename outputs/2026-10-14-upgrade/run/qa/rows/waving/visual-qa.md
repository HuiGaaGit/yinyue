# Waving strip visual QA

- Selected source: `decoded/waving.png` (2172 x 724, built-in image_gen, transparent background).
- Actual generation prompt: `prompts/rows/waving-actual.md`.
- All three references were viewed and supplied: canonical base, old identity atlas, and four-slot waving layout guide.
- Bundled extraction: `extract_strip_frames.py --states waving --method auto` succeeded with connected-component extraction.
- Bundled inspection: `inspect_frames.py --states waving --require-components` returned `ok: true`, 4/4 frames, no errors or warnings. Exact report: `qa/rows/waving/review.json`.
- Viewed the generated strip and all four extracted 192 x 208 frames. Identity is consistent: silver hair, fox ears, amber eyes, ivory/red shrine-maiden outfit, sleeve embroidery, red bow/ribbons and white detailed boots.
- Action order is readable: low hand; raised palm by cheek; outward wave with happy closed-eye smile; hand returned low. Sleeves follow the waving arm and the other hand remains low. No visible extra limbs, detached hand, floating effects or copied guides.
- Native frames preserve full body and a stable baseline. All four bounding boxes have top 5 and bottom 203, with zero edge pixels. No pose overlaps, missing boots or clipped ears observed in the extracted frames.
- Source-level caveat: enlarged source shows small bright color flecks around some alpha edges inherited from the refined reference. They are not visibly disruptive at the inspected native pet size; parent must still perform its normal final edge cleanup and exact-atlas visual/structural checks. This is row-level acceptance, not final atlas acceptance.
