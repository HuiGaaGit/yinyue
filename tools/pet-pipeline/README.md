# 保存的宠物技能流水线

`scripts/` 内18个Python脚本原字节复制自本机安装的 OpenAI `work-pets` 插件0.1.6、`skills/create-pet/scripts/`，用于本次跨电脑续做；未修改脚本实现。

对应规则快照保存于 `docs/pet-workflow/`。复制后的技能文档中相对链接保留原始形式；本仓库的实际路径以 `docs/RESUME.md` 为准。

脚本依赖Python3.11以上和Pillow；预览MP4及现有PowerShell对齐脚本还使用FFmpeg。图像生成、Pets预检与宠物更新需要新的Codex会话内置工具，不依赖这些本地脚本提供API密钥。

如果当前宠物技能要求bundled runtime，调用Codex的 `load_workspace_dependencies` 获取新电脑的准确Python路径；原机器路径仅保留在历史证据中。
