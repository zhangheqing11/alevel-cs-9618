# CIE 9618 Computer Science 学习系统 · 协作规则

本仓库为一名学生建设 CIE AS & A Level Computer Science 9618（P1–P4，2027 年 5–6 月考）的学习系统，模式迁移自 `~/Desktop/a2 physics`（9702 P4）：真题语料 → 题型化手册 → 教学 skill → 掌握记录。完整方案见 `docs/PLAN.md`。

本文件是所有 agent（Claude Code、Codex）的**唯一规则源**。任务细节在 `tasks/Txx-*.md`，任务状态在 `tasks/BOARD.md`。

## 1. 开工前必读

1. 本文件。
2. 你的任务卡 `tasks/Txx-*.md`（目标、输入、产出、允许写的路径、完成标准）。
3. 你的进度日志 `tasks/progress/Txx.md`（若存在：从上次停下的地方继续）。
4. 任务卡点名的 schema（`schemas/`）与格式规范（`schemas/*.md`）。

## 2. 角色

| 角色 | 担任者 | 职责 |
|:--|:--|:--|
| 总控 | 最初的 Claude Code 会话（Opus） | 架构、schema、本文件、下载与配对、合并、质检、派活 |
| 设计工位 | Claude Code 会话（Opus） | 需要判断与设计的工作：题型体系、题型卡、教学 skill、课程设计、疑难裁决、抽查 codex 产出 |
| 执行工位 | Codex 会话 | 按规格执行：抽取、拆分、打标签、生成练习与测试、构建脚本、审计设计工位的产出 |

## 3. Git 工作流

- 每个任务一个分支 `task/Txx-<slug>`，在独立 worktree 里工作（任务卡给出命令）。**不要在主 checkout `~/Desktop/alevel cs` 里切分支或改文件**——那里是总控和学习会话的工作区。
- 只写任务卡「允许写的路径」（机器可读版：`tasks/scope.json`）。提交前运行 `make check-scope TASK=Txx`。
- 小步提交，信息用英文祈使句，前缀任务号：`T12: split P1 rows for 2024`。
- 交付前：`git fetch origin && git rebase origin/main` → `make check` 全绿 → `make check-scope TASK=Txx` 全绿 → `git push -u origin HEAD` → `gh pr create --base main`。
- PR 描述写：做了什么、校验结果、已知问题、**「需要总控决定」**（如有）。
- **不要自己合并 PR，不要推 main，不要 force-push 别人的分支。** 合并由总控做。
- 中途停下或上下文将满：把「已完成 / 进行中 / 下一步 / 坑」写进 `tasks/progress/Txx.md` 并提交。任何 agent（含另一家模型）都应能只凭任务卡 + 进度日志续做。

## 4. 共享文件与变更请求

以下文件只有总控能改：`AGENTS.md`、`CLAUDE.md`、`Makefile`、`requirements.txt`、`docs/`、`schemas/`、`tools/`、`conftest.py`、`tasks/`（各任务自己的 `tasks/progress/Txx.md` 除外）。

需要改它们（例如 schema 少一个字段、校验器误报）时：不要绕过，在 PR 描述或进度日志写「需要总控决定：…」，并在不阻塞的部分继续工作。

## 5. 资料与证据规则

- **原始资料**在主 checkout 的 `sources/`（gitignore，不入库，只读）。worktree 里没有这个目录，一律用绝对路径或环境变量：
  - `ALEVEL_CS_SOURCES`，默认 `/Users/zhangheqing/Desktop/alevel cs/sources`
  - `sources/pastpapers/`：真题与配套（来自老师提供的 Teach Cambridge 官方导出，即原件），命名 `9618_<季><yy>_<类>_<卷号>.pdf`，类 = `qp` 题卷、`ms` 评分方案、`in` P2 插页（内置函数表）、`er` 考官报告（每季一份，无卷号）、`gt` 分数线（同）；P4 源文件是**目录** `9618_<季><yy>_sf_<卷号>/`（数据 `.txt` + 证据文档模板 `evidence.doc`）。
  - `sources/official/`：2027–2029 考纲、考纲更新说明、伪代码指南（**唯一权威写法**）。
  - `sources/official/support/`：Example Candidate Responses（P1–P4，2021 与 2024 版，真实考生答卷 + 考官点评）、Specimen Paper Answers（P1–P3）、Learner Guide、Scheme of Work、旧版伪代码指南（2023–25、2026）与 2026 考纲。
  - `sources/official/specimen/`：2021 样卷 `9618_y21_sp_<qp|ms|in>_<n>.pdf`（不进 `corpus/rows`，可作冲刺整卷练习）。
  - `sources/textbooks/`：`Langfield_Duddell_Coursebook_2e_2019.pdf`（对应 9618，概念讲解主参考）、`ZNotes_AS_Theory_2026.pdf`（精简笔记，仅作核对）。
  - `sources/teach_cambridge_raw/`、`sources/teach_cambridge_sf/`：导出包原样解压，**不要直接引用**，用上面规范化后的路径。
- 不得编辑、改名、移动、删除 `sources/` 下任何文件；不得把 PDF/ZIP 提交进 git。
- **语料**：核验语料 = 2022–2026s 全部 variant，每份 QP 与其**同季同年同 variant** 的 MS 精确配对；2021 为扩展语料（也有 MS，但统计与优先级只用核验语料）。
- 任何关于「某题得几分 / MS 接受什么写法」的陈述，必须来自该题自己的 MS 原文。不得用相似题、别的 variant、记忆或 OCR 摘要代替；需要看图、表、代码排版时回到 PDF 原页。
- 考官报告（ER）、Example Candidate Responses、Specimen Paper Answers 只用于「易错与失分」、范答展示与教学示范，**不能作为给分依据**；给分只认该题自己的 MS。
- 教材与 ZNotes 只用于概念讲解与直觉补充；与 MS 冲突时以 MS 为准，并记录差异。不整段复制教材或笔记原文。

## 6. 编号与数据约定

| 对象 | 格式 | 例 |
|:--|:--|:--|
| 卷 | `9618_<季><yy>_<卷号>`，季 ∈ m/s/w | `9618_s24_22` |
| 小问行 | `<卷>:<题号>`，题号到最细一级 | `9618_s24_22:3(b)(ii)` |
| 题型 | `P<卷>-<章节码>-<两位序号>` | `P1-DB-03` |
| 技能标签 | 小写短横线 | `file-close`、`loop-to-eof` |
| 阶梯 | `L<两位>`、练习 `E<两位>` | `L05/E03` |

- 文本 UTF-8；JSON 2 空格缩进、`ensure_ascii=False`；JSONL 每行一个对象；记录表 CSV 用 `utf-8-sig`。
- 教学文字用中文；MS 得分句、伪代码、Python 代码与代码注释用英文。
- 伪代码一律遵循 2027–2029 版剑桥伪代码指南（关键字大写，`DECLARE x : INTEGER`、`ENDIF`、`←` 赋值等）。

## 7. 目录地图

| 路径 | 内容 | 归属 |
|:--|:--|:--|
| `docs/` | 方案与说明 | 总控 |
| `schemas/` | JSON Schema 与格式规范 | 总控 |
| `tools/` | 校验器、测试工具 | 总控 |
| `pipeline/download/` | 下载与配对脚本 | T01 |
| `pipeline/extract/` | 抽文本、拆小问脚本 | T12 |
| `corpus/inventory.csv` | 资料清单与配对结果 | T01 |
| `corpus/rows/p<N>/<卷>.jsonl` | 最细小问行 | T12 产出，T24 起追加题型/得分点字段 |
| `papers/p<N>/` | 题型体系 `taxonomy.json`、题型卡 `cards/`、概念表 `core/`、技能标签 `skill_tags.json` | 各卷设计任务 |
| `practice/p2/`, `practice/p4/` | 真题练习文件夹 | T25 及 P4 对应任务 |
| `ladder/` | Python 阶梯：设计、对照卡、练习 | T10（设计与卡）、T14（练习实现） |
| `skill/cie-9618-cs-tutor/` | 教学 skill 源 | T11 |
| `build/` | md → html/json 构建器 | T13 |
| `output/` | 生成物（gitignore，`make build` 重建，不得手改） | 构建器 |
| `ledger/`, `handoff/`, `attempts/` | 学习记录、交接文档、学生作答 | 学习会话 |
| `tasks/` | 任务卡、看板、范围表、进度日志 | 总控（进度日志归各任务） |

## 8. 练习文件夹约定（真题与阶梯通用）

详见 `schemas/exercise-format.md`。要点：每个练习含 `task.md`、`meta.json`、`starter.py`、`test_task.py`、`ref/solution.py`、至少一个 `ref/mutant_*.py`。测试通过根目录 `conftest.py` 的 `sol` fixture 加载被测代码；`make check` 要求参考解全过、每个 mutant 至少挂一个测试。学生作答在 `attempts/<同路径>/solution.py`，用 `make try EX=<练习路径>` 测。

## 9. 环境

- Python 环境共用 `~/.venvs/alevel-cs`（目录名含空格，不在仓库内建 venv）。首次 `make setup`。
- 命令统一走 Makefile：`make check`、`make check-scope TASK=Txx`、`make build`、`make try EX=…`。
- PDF 抽取可用 PyMuPDF（`import pymupdf`）或 `pdftotext -layout`（poppler 已装）。

## 10. 学习会话（教学时）

学习在主 checkout 的 Claude Code 会话里进行，使用 skill `cie-9618-cs-tutor`（源在 `skill/`）。学习会话只写 `ledger/`、`handoff/`、`attempts/`，不改建设产物；发现手册错误时记进 `handoff/勘误.md`，由总控转成修正任务。
