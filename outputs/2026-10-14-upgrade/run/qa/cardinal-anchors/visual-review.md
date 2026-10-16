# 四方位候选复核（2026-10-15）

- 原始提取失败报告保留为 `structure-before-alpha-clean.json`。
- 独立复核确认四个方向可读，耳尖和鞋底完整；四个源slot边缘134/109/183/161像素均为alpha=1，边缘没有alpha>=2像素，非实际裁切。
- 仅用FFmpeg将alpha<=1的背景噪声清零，不重画人物。原源文件保留，清理结果在 `source-alpha-clean.png`。
- 原官方提取脚本重跑 `structure.json` 返回 `ok: true`；192×208原生复核000上仰、090屏右、180低头、270屏左，脸部可见、躯干锚定。批准锚点合成为 `references/approved-cardinals.png`。
- 该批准仅覆盖四锚点，不替代后续十六方向与最终图集验收。
