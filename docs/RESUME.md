# 在另一台电脑继续银月升级

最新检查点日期：2026-10-16。仓库：`HuiGaaGit/yinyue`。分支：`checkpoint/2026-10-16-final-candidate`。

**先阅读 [最新会话记录](sessions/2026-10-16_06-25.md)。下面“现在已有的成果”之后保留的是10月14日历史细节，不能作为当前待办。** 当前已完成9类57帧动作、4方位锚点及16个视线方向；不要再次修复已经通过的步态或重画方向。最新候选为 `run/final/spritesheet-v2-20261016-r2.webp`，SHA256为 `f3b2687fa42bf82f5aa9135e3a774a383373b85303c6810d4829f1cb515d425d`。先核验综合质量/Pets预检及正式更新状态。

这是未完成的进度备份。根目录的 `pet.json`、`spritesheet.webp` 仍是旧版正式资源；本次新素材均在 `outputs/2026-10-14-upgrade/`。

## 回家恢复

1. 用有GitHub访问权限的账户克隆这个分支：

```powershell
git clone --branch checkpoint/2026-10-16-final-candidate https://github.com/HuiGaaGit/yinyue.git "06银月桌宠"
```

2. 在另一台电脑的Codex中打开克隆后的 `06银月桌宠` 文件夹，发送：

> 请先读 AGENTS.md 和 docs/RESUME.md，校验检查点，再恢复 docs/sessions/2026-10-16_06-25.md。复用已经完成的73帧图集，先核实云端是否已被原机器更新，然后完成仍缺少的最终门禁、预览确认和原PET更新，不要重复生图。

3. 新会话先调用 `load_workspace_dependencies` 获取本机bundled Python路径，把下面的 `$petPy` 设为工具实际返回的Python路径。在克隆仓库根目录执行：

```powershell
& $petPy scripts/checkpoint.py verify
& $petPy scripts/rehydrate_checkpoint.py
```

先校验，再重写工作路径/恢复会话标记。`verify`只验证本检查点文件完整性，不能替代动画和方向质量验收。`rehydrate_checkpoint.py`只重定位两份操作清单，不改原始检查报告。

4. Python需3.11以上和Pillow，FFmpeg需在PATH中；脚本需要PowerShell。优先使用Codex自带runtime。缺Pillow且当前技能允许安装时用该runtime执行 `-m pip install -r requirements.txt`；FFmpeg未安装时可通过系统软件包管理器安装。图像生成和Pets工具在新会话中使用登录后的内置能力，仓库不包含API密钥或上传令牌。

当前本地会话已成功获取bundled runtime。历史恢复记录中“委托线程缺少依赖工具”的限制仅描述当时那个线程；新电脑必须重新检查自己的工具能力。

## 10月14日历史检查点细节

以下内容保留用于追溯；当前状态和下一步以最新会话记录为准。

### 当时已有的成果

| 内容 | 路径 | 状态 |
| --- | --- | --- |
| 用户截图、旧正式图和云端旧图 | `outputs/2026-10-14-upgrade/source/` | 已备份；云端旧PNG被保存为`.webp`文件名，实际格式见原验证报告 |
| 精细化角色基准 | `run/decoded/base.png`、`run/references/canonical-base.png` | 已选中；银发、狐耳、琥珀眼、红白服饰、细致发丝/绣纹/靴饰 |
| 九类动作源条带 | `run/decoded/<state>.png` | 57帧候选齐全；左右移动仍有步态问题 |
| 每行提取帧和真实QA | `run/qa/rows/<state>/` | 包括成功/失败稿和修订，不能将结构通过等同于视觉通过 |
| 对齐后的标准帧 | `run/qa/registered-frames/` | 已处理跨行动作大小；待步态修复后更新对应两行 |
| 标准九行图、接触表和GIF | `run/final/spritesheet-standard.png`、`run/qa/contact-sheet.png`、`run/qa/standard-previews/` | 候选预览；不是可上传的最终v2图集 |
| 四主方向找回的生成图 | `run/qa/recovery/look-cardinals-interrupted-source.png` | 已找回完整PNG，尚未提取/原生尺寸语义验收，无需直接重新生成 |
| 全部实际提示词 | `run/prompts/` | 包括各次失败和修复；模板绿底与实际透明背景不同，后续遵循actual提示词 |
| 图集流水线 | `tools/pet-pipeline/scripts/` | 18个原技能脚本已复制，脱离旧电脑插件目录也可使用 |

表中的`run/`均指 `outputs/2026-10-14-upgrade/run/`。

## 尚未完成与下一步

1. 修复 `running-right`。独立复核发现一条腿持续前伸/落地，另一条腿持续后折，没有前后交换；镜像 `running-left` 继承同样问题。换用明确的交替小步走姿，避免继续微调同一失败跑姿。先保存当前修订，基于新基准和正确步态参考生成完整右条带，真实检查后再重建左条带。
2. 每个新行仍用 `extract_strip_frames.py --method auto` 和 `inspect_frames.py --require-components`，检查完整人物、帧数、手脚和服饰；允许镜像时只逐帧镜像并保持时间顺序。保存的左行生成脚本读取 `imagegen-jobs.json`，旧左行存在时需要归档并使用其`--force`参数。
3. 用 `extract_cardinal_anchors.py` 提取已找回候选，检查192×208的上/右/下/左含义，再用 `compose_cardinal_anchor_strip.py` 生成批准锚点。该候选原字节SHA256为 `8f9acb75bf889553f5293c6e16df5aa8c8475b16d0cb5053570d6e6f88a0fa1b`。
4. 按 `run/qa/look-mechanics.md` 生成连贯行9，先注册/检查，再生成行10。行9顺序：000、022.5、045、067.5、090、112.5、135、157.5；行10：180、202.5、225、247.5、270、292.5、315、337.5。000是向上。
5. 用已保存的官方流水线合成1536×2288透明v2图集；执行一次边缘去色、结构验证、方向语义与盲审、连续性及 `validate_pet_quality.py`，保存真实报告。不要拼贴不同来源的单个方向帧。
6. 从实际最终编码文件导出全部预览，可运行 `run/export-final-previews.ps1 -Atlas <最终文件>`；它现在默认使用本仓库的流水线目录。展示动作和方向预览后，对同一文件运行Pets `validate_pet_spritesheet`。
7. 全部门禁通过后 `prepare_pet_upload` → `update_pet`，保持原稳定ID `pet_6acc45e9b9748191844cb9cf900e35f2`，只传upload session，名称和描述沿用。更新前重新读取当前激活项并保持选择；历史上后来激活过“南宫婉”，不要强行切换回银月。
8. 最后同步根目录正式文件和新电脑 `%USERPROFILE%\.codex\pets\yinyue\`，比对哈希，更新说明、计划和GitHub进度。

本次已检查到旧正式图idle行的未使用列6有额外图像，新图集必须清空该格和其他全部未使用格。`spriteVersionNumber: 2`是协议版本。

## 可用命令与路径

在仓库根目录设置 `$petScripts = 'tools/pet-pipeline/scripts'`、`$petRun = 'outputs/2026-10-14-upgrade/run'`；以下参数均为仓库相对路径，可按修复状态调整。

```powershell
& $petPy "$petScripts/inspect_frames.py" --frames-root "$petRun/qa/registered-frames" --json-out "$petRun/qa/review.json" --require-components
& $petPy "$petScripts/compose_atlas.py" --frames-root "$petRun/qa/registered-frames" --output "$petRun/final/spritesheet-standard.png"
& $petPy "$petScripts/validate_atlas.py" <最终图集> --require-v2 --chroma-key '#00FF00' --json-out <验证报告>
```

`run/register-standard-frames.ps1`将非跳跃行统一缩放到166×180并放入192×208的(13,28)，跳跃保持44px升高和203落地基线。以后若重新生成的姿态/比例改变，先复核跨行尺度再复用，不能把当前数值当永久设定。

历史QA内的旧绝对路径保留作为当时记录。后续操作一律用当前仓库根目录和重定位后的操作清单；不得读取旧机器临时目录，也不要重跑 `prepare_pet_run.py --force`覆盖已有成果。
