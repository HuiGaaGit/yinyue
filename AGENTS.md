# 银月桌宠工作约定

- 本仓库对应工作区项目 `06银月桌宠`。先读 `docs/project-index.md`、`README.md`、`docs/RESUME.md`，再读最新 `docs/sessions/*.md`。
- 2026-10-14 升级为未完成的检查点。根目录 `pet.json`、`spritesheet.webp` 是旧版正式资源；候选图位于 `outputs/2026-10-14-upgrade/`。
- 手工编辑用 `apply_patch`，每次不超过8k字符。Windows文本优先 `Get-Content`，搜索用 `rg`。shell工具明确设置workdir，不再套一层shell。
- 所有新角色像素用内置imagegen生成。`tools/pet-pipeline/scripts` 是已保存的官方技能流水线；用于提取、合成、对齐、去底、质量检查与预览，不用替代图像生成。
- 使用环境当前适用的宠物技能。若技能要求bundled Python，先调用 `load_workspace_dependencies` 获取本机路径；不得照抄旧机器的绝对路径。
- `imagegen-jobs.json` 的旧生成完成状态不能替代视觉验收。左右移动的步态仍需修复；接触表和GIF为候选预览。
- 先修右行并验收，然后重新生成或逐帧镜像左行。优先检查已找回的四方位候选，避免重复生成已存在的素材。行9通过后再生成行10。
- 保留失败稿与真实检查报告，不伪造质量通过结果。最终上传前必须通过结构、动作、方向、连续性、Pets预检，并展示最终文件导出的动画。
- 更新已有银月稳定ID `pet_6acc45e9b9748191844cb9cf900e35f2`，不创建重复宠物。更新前重新读取当前激活项并保持用户选择。
- 当前没有需要打包的应用或exe；`spriteVersionNumber: 2` 是图集协议版本。
