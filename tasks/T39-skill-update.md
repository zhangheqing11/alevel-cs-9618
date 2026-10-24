# T39 · 教学 skill 更新到全四卷（执行工位 codex）

## 目标

教学 skill `skill/cie-9618-cs-tutor/`（T11，已软链到 `~/.claude/skills/`，改了即生效）写于项目初期，只完整覆盖 P1、P2 与阶梯。现在 P3、P4 手册与 P4 上机练习、模考批改包、分数线表、考官报告摘录都已就绪，决策也到了 D45。本任务把 skill 更新到能教全四卷、能带整卷模考，并为学习会话建好 P3 / P4 学习记录表。**skill 的教学协议（掌握门槛、讲解结构、批改纪律、写入边界）保持不变，只补缺口、改过时处**。

## 现状（总控核查，2026-10-24）

- `SKILL.md` 374 行；`references/` 有 `theory.md`、`programming.md`、`ladder.md`、`syllabus-map.md`、`few-shots.md`、`handoff-template.md`；`scripts/rows.py`（`get`、`find`、`drills`、`ex`、`render` 已能处理 P3 / P4 行）、`scripts/ledger.py`（已识别 P1 P2 P3 P4 ladder 五个名字）。
- **完全没提到**：模考批改包 `pipeline/mock/`（`make_mock.py`、`score_mock.py`）、分数线 `corpus/thresholds/`、`make try … K=<小问>`、P4 练习约定（`files/`、证据格对照表、人工核对清单、P4 骨架例外，`papers/p4/practice-notes.md`）、AD-06 的 `answer.steps.md`（D38）。
- `ledger/` 只有 `P1.csv`、`P2.csv`、`ladder.csv`，**缺 `P3.csv`、`P4.csv`**。

## 要改什么

1. **资源表**（`SKILL.md` 开头的“去哪里找”）：补 P3 / P4 手册（`papers/p3|p4/`、构建产物 `output/p3|p4/` 与 `index.json`）、`practice/p4/`、`pipeline/mock/`、`corpus/thresholds/`、行的 `er` 字段、`corpus/er/` 的每卷总评。
2. **P3 学习流程**：理论题型照 P1 流程；写代码题型（指南 §8 拆分题型）照 P2 的伪代码批改流程；BNF / RPN / 卡诺图 / Dijkstra / A* 等“逐步作答”题型按卡里的步骤模板逐步批。
3. **P4 学习流程**：先过阶梯 L09–L12 → 读 P4 卡（Python 模板、证据格怎么交）→ `make try EX=practice/p4/<卷>_q<题号>` 全题或 `K=1b` 单小问 → 自动测全绿后，按 task.md 的证据格对照表与人工核对清单逐项人工核（模块头、类型注释、截图内容）→ 记录。说明 P4 练习的 `starter.py` 只有分节注释（学生从空文件写），数据文件在 `files/`。
4. **批改纪律补充**：D31（练习自动测按 QP，人工按该题 MS 得分点，QP 未定义的边界不扣分）；D37 ②（语料 `markpoints[].n` 与 MS 印的 MP 编号可能不同，按 task.md / 卡里的对照）；D2 / D32（非指南写法、ER 说接受但 MS 没写的写法不默认给分）；D33（ER 只用于易错，展示为“考官报告指出 …”，不作给分依据）；D38（AD-06 用 `answer.steps.md` 编号英文步骤，人工按 MS）；D45（已知 MS 范例缺陷清单：遇到这些题时说明“照 MS 得分点给分，自己的程序按正确写法”）。
5. **整卷模考流程**（新小节）：s26 的 12 份卷只用于考前限时模考（D1；s26 的 MS 原句可出现在讲解里，D44 ①）。流程：确认卷别与时长 → `python3 pipeline/mock/make_mock.py <卷 id>` 生成批改包（`output/mock/<卷>/marking.md|html`、`score.csv`）→ 学生限时作答（看原卷 QP）→ 学生按批改包自批、填 `score.csv`，学习会话复核每个丢分点 → `python3 pipeline/mock/score_mock.py <score.csv>` 汇总与估等级（`corpus/thresholds/`，学生对应的 option 见其 README）→ 把失分题型 / 技能写进 ledger 与交接。只读 `pipeline/mock/README.md` 的实际用法，命令以它为准。
6. **`references/syllabus-map.md`**：补考纲 13–20 节 → P3 / P4 章节与题型码（取自 `papers/p3|p4/taxonomy.json` 的 `syllabus` 字段，用脚本生成表格）。
7. **`references/few-shots.md`**：补两个短示范——P3 写代码题按 MP 批改一例、P4 一个小问的“自动测通过 + 人工清单”批改一例（行与原文取自真实语料；MS 原文用该题自己的 MS）。
8. **学习记录表**：照 `ledger/P2.csv` 的格式（`schemas/ledger-format.md`，`utf-8-sig`，13 列）生成 `ledger/P3.csv`（79 型）与 `ledger/P4.csv`（36 型）：`类型`、`名称`、`章节`（“码 中文章名”）、`优先级`（星级取 `output/p3|p4/index.json`，先 `python3 build/build.py p3 p4`）、`状态=未学`，其余空。写一个可重复运行的生成脚本放在 `skill/cie-9618-cs-tutor/scripts/`（如 `init_ledger.py P3`，已存在的表不覆盖，除非 `--force`）。
9. 过时处：全文检查与现状不符的说法（例如“P3 / P4 尚未就绪”、只提 P1 / P2 的列举、旧决策号），逐一改正。

## 允许写的路径

`skill/cie-9618-cs-tutor/**`、`ledger/P3.csv`、`ledger/P4.csv`、`tasks/progress/T39.md`。不改 `ledger/P1.csv`、`P2.csv`、`ladder.csv`（学生的真实记录），不改手册、练习、语料、工具。

## 完成标准

- `make check` 全绿（ledger 表头合法）；`make check-scope TASK=T39` 全绿。
- skill 里出现的每条命令都实际跑过一次（模考包用一份 s26 卷生成、`score_mock.py` 用一份填了假数据的 `score.csv` 跑；`make try` 用一道 P4 练习的参考解跑 `K=` 单小问）——在 PR 里贴命令与输出摘要；生成物放 `output/` 或 `work/tmp/`，不入库。
- `ledger.py summary` 能读出 P3 / P4 两张新表。
- PR 描述：每处改动的位置与理由、实测命令、仍不确定而需要总控决定的教学协议问题。
