# T11 · 教学 skill `cie-9618-cs-tutor`（设计工位 cc-B，Opus）

## 目标

写出学生在 Claude Code 里学 9618 时使用的教学 skill。它把物理 skill 的成熟做法迁移过来，并为 CS 新增编程卷流程（伪代码批改 + pytest + MS 得分点核对）。这是整个系统里**最需要教学判断**的文件：它决定每一次学习对话的质量。

## 输入（先通读）

- 物理 skill 与配套（只读，在学生电脑上）：
  - `/Users/zhangheqing/Desktop/a2 physics/alevel-physics-SKILL.md`（模式、证据规则、代表题流程、掌握门槛、错误分类、学习锚点、长对话恢复、禁止行为）
  - `/Users/zhangheqing/Desktop/a2 physics/references/teaching-few-shots.md` 与 `teaching-sample-analysis.md`（教学语气）
  - `/Users/zhangheqing/Desktop/a2 physics/P4交接文档_量子起.md`（**学生实际偏好**：加速模式、一条回复的节奏、作图规范、学生常见错误类型、交接文档写法）
- 本仓库：`AGENTS.md`（特别是 §5 证据规则、§10 学习会话）、`docs/PLAN.md`、`schemas/`（行、题型、练习、记录表、卡片格式）、`schemas/examples/`、`Makefile`（`make try`）。

## 已定的教学决策（必须写进 skill）

- 场所：主 checkout 的 Claude Code 会话；中文教学，MS 得分句、伪代码、代码用英文。
- **默认加速模式**：一条回复内完成「批改上一题 → 更新记录表 → 讲下一题型概念与代表题 → 布置变式」；有明显缺口标「学习中」写清问题点、不反复追问；卡住或学生要求时给一次详细讲解后继续；「学习中」留到章末/总复习统一复测。
- **编程题过关标准**：pytest 全绿 **且** MS 得分点（含测试测不到的人工核对清单）齐全才标「已掌握」。
- **不摸底**：每章完整首学。
- 学习顺序：AS 先行（P1、P2、阶梯 L01–08），理论课与编程课交替；A2 在 1–3 月；4–5 月冲刺。skill 根据记录表与学生开场白决定从哪里继续。
- 记录表一卷一个（`ledger/P1.csv` … `ledger/ladder.csv`），格式见 `schemas/ledger-format.md`；用 Python `csv` 以 `utf-8-sig` 原地改写。

## 产出（全部在 `skill/cie-9618-cs-tutor/`）

1. `SKILL.md`：带 frontmatter（`name: cie-9618-cs-tutor`，`description` 写清触发场景：学/复习/刷题/冲刺 9618 任一卷、做真题、批改、Python 阶梯）。正文是**各卷共用协议**：
   - 开场恢复（读记录表 + 最新交接文档 + 上一锚点，一行报告位置与模式）；
   - 三种模式（首学 / 专项刷题 / 考前冲刺）与加速节奏；
   - 证据规则（精确 QP/MS 配对；从 `corpus/rows/` 取题干与 MS，`has_figure` 时用 PyMuPDF 渲染原页给学生看；作答前不泄露答案或 MS）；
   - 定义三层（英文 MS 句 / 中文 / 直观理解）；
   - 错误分类（**为 CS 重写**：概念、题型识别、算法设计、伪代码规范、边界与差一、数据结构、文件处理、类型与转换、考试措辞、漏 MS 得分点、测试与调试、综合迁移），以及「失分技能」标签的使用；
   - 学习锚点（5 行）、交接文档（说「交接」时按模板生成到 `handoff/`）、长对话恢复；
   - 作图：逻辑电路、数据结构指针图、追踪表、状态转换图、网络拓扑、ER 图等——优先用会话里的内联可视化工具，否则渲染图片；读图题作答前不标答案；
   - 学习会话只写 `ledger/ handoff/ attempts/`；阶段结束时提交这些路径；发现手册错误记 `handoff/勘误.md`；
   - 禁止行为清单。
2. `references/theory.md`：P1/P3 的首学单元流程与代表题精讲步骤（对应物理的 Unit workflow + Representative procedure，改为 CS 语境）。
3. `references/programming.md`：P2/P4 流程——题型卡 → 代表题精讲 → `make try EX=…` 生成作答文件 → 学生在 VS Code 写 → 「测一下」：运行测试 + 逐条对 MS 得分点 → 记录失分技能。包括：
   - **P2 伪代码批改规则**：按 MS 得分点给分（MS 接受合理的等价写法，不因非指南写法扣得分点），但另行指出不符合 2027–29 指南的写法并给规范版本；
   - 再把同一算法改写为 Python 跑测试；
   - **P4**：证据文档要求（代码 + 运行截图）、标识符必须用题目指定名称、官方源文件的使用。
4. `references/ladder.md`：阶梯的教学流程（对照卡 → 讲解 → 练习 → 全绿升级）与公开课材料的使用方式。
5. `references/few-shots.md`：2–3 段 CS 教学示范（模仿物理 few-shots 的语气与讲解结构，例如：补码为什么能用加法做减法；BYREF 与 BYVAL；为什么需要第三范式）。标明它们是语气示范，不是 MS。
6. `references/handoff-template.md`：交接文档模板（参照物理交接文档的结构：开场怎么做、学习模式、文件备忘、进度总览、常见错误、待办）。

## 不要做

- 不要复制物理 skill 里与 9702 相关的内容（数据表、物理图像清单、P5 排除条款等）。
- 不要硬编码尚未存在的输出文件名：手册路径用「`output/p<N>/` 下由 `make build` 生成的手册」描述，或读 `output/p<N>/index.json`。
- 不要安装 skill（软链到 `~/.claude/skills/` 由总控在合并后做）。

## 允许写的路径

`skill/**` 与 `tasks/progress/T11.md`。

## 完成标准

- `make check`、`make check-scope TASK=T11` 全绿。
- SKILL.md 正文 ≤ 约 600 行，分卷细节在 references/ 里按需加载。
- 总控审读通过；教学流程部分请学生过目（总控转达）。

## 工作方式

分支 `task/T11-tutor-skill`（总控创建）；进度写 `tasks/progress/T11.md`；交付走 rebase → 检查 → push → `gh pr create --base main`。不要合并。
