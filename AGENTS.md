# 银月桌宠工作约定

- 本仓库对应工作区项目 `06银月桌宠`。先读 `docs/project-index.md`、`README.md`、`docs/RESUME.md`，再读最新 `docs/sessions/*.md`。
- 最新保存点为2026-10-16最终候选；先读 `docs/sessions/2026-10-16_06-25.md`。根目录 `pet.json`、`spritesheet.webp` 是旧版正式资源；候选图位于 `outputs/2026-10-14-upgrade/run/final/spritesheet-v2-20261016-r2.webp`。
- 手工编辑用 `apply_patch`，每次不超过8k字符。Windows文本优先 `Get-Content`，搜索用 `rg`。shell工具明确设置workdir，不再套一层shell。
- 所有新角色像素用内置imagegen生成。`tools/pet-pipeline/scripts` 是已保存的官方技能流水线；用于提取、合成、对齐、去底、质量检查与预览，不用替代图像生成。
- 使用环境当前适用的宠物技能。若技能要求bundled Python，先调用 `load_workspace_dependencies` 获取本机路径；不得照抄旧机器的绝对路径。
- `imagegen-jobs.json` 的生成完成状态不能替代视觉验收。当前交替步态已修复，四方位与16方向已生成；复用已通过素材，不要按旧会话记录重复生图。
- 此保存点的结构和方向连续性通过，三份盲测84项判断无错向。仍须完成综合质量门禁、动画复核和Pets预检后更新。原机器另一个聊天也在做最终验收，恢复时先核验云端及远程最新状态，避免重复上传或覆盖更新成果。
- 保留失败稿与真实检查报告，不伪造质量通过结果。最终上传前必须通过结构、动作、方向、连续性、Pets预检，并展示最终文件导出的动画。
- 更新已有银月稳定ID `pet_6acc45e9b9748191844cb9cf900e35f2`，不创建重复宠物。更新前重新读取当前激活项并保持用户选择。
- 当前没有需要打包的应用或exe；`spriteVersionNumber: 2` 是图集协议版本。
