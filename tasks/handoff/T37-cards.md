# 交接 · T37 P4 题型卡（T37A / T37B 续做）

任务卡：`tasks/T37-p4-cards.md`（卡片结构、Python 模板 / 得分点地图 / 对应练习三项、选题规则、六条审计教训、允许路径、完成标准）——**全文照做**。这是设计类产物，交给 Codex 续写：已写好的 4 章是质量标杆，总控验收时会逐张对照原页抽查，不合格的卡会按卡打回。

## 现状（2026-10-24）

| 批 | 分支 | 已完成（范本） | 剩下 |
|:--|:--|:--|:--|
| T37A | `task/T37A-p4-cards`（已推） | PR（3 型）、AR（5 型）：`papers/p4/cards/PR.md`、`AR.md` + `core/PR.md`、`AR.md` | **FL**（FL-01–03）、**SR**（SR-01–04）、**RC**（RC-01–02）三章 cards + core，`papers/p4/front.md` |
| T37B | `task/T37B-p4-cards`（已推） | SQ（4 型）、LT（5 型）：`cards/SQ.md`、`LT.md` + `core/SQ.md`、`LT.md` | **OP**（OP-01–07）、**MP**（MP-01–03）两章 cards + core，`papers/p4/back.md` |

进度日志：各分支的 `tasks/progress/T37A.md` / `T37B.md`（含已定的代表题、计划、坑），先读。T37A 已为 FL / SR / RC 预选了代表题与变式（见其进度日志「进行中 / 下一步」），核对原页后可直接用。

## 工具

T37B 上一个工位写的临时脚本已保存在 `~/Desktop/alevel-cs-wt/handoff/t37b-scripts/`（不入库；复制到你 worktree 的 `work/tmp/`，`work/` 已 gitignore）：

| 脚本 | 用途 |
|:--|:--|
| `mps.py <题型码…>` | 列该型全部行的得分点（MS 原文、技能） |
| `skillmap.py <题型码…>` | 按口径统计技能标签（得分点地图） |
| `q.py <卷> <题号> --ms --short` | 看整道大题（题干 + MS） |
| `run.py <程序> <卷> '<stdin>'` | 把该卷源文件 .txt 复制到临时目录后运行程序 |
| `blocks.py <md…>` | 执行卡里所有 python 块 |
| `same.py <card> <prog…>` | 核对卡里的完整作答与跑过的程序逐字相同 |
| `progs/` | 已跑过的整题程序（SQ、LT 章） |

脚本里若写死了旧 worktree 路径，改成你的路径。

## 每张卡的执行方案

1. `mps.py <码>` / `rows.py drills <码> --all` 看该型全部行；`skillmap.py <码>` 出得分点地图（口径：核验语料 2022–2026s、主题型行、同一行同一标签计一次、去 `equivalent_of`；s26 只进计数）。
2. **选代表题与变式**：2022–25、主题型行、不同卷、非 s26、非 `equivalent_of`；找不到按 D41 ① 替代顺序。
3. **看原页**：QP 该题全部页、MS 对应页的渲染图（MS 的 Python 缩进只看图）。
4. **写完整作答**：整道大题的可运行 Python 写进 `work/tmp/.../progs/`，用官方源文件 / QP 测试数据跑（`run.py`），输出与 MS 截图一致；卡里的完整作答与程序逐字相同（`same.py`）。
5. **写卡**：照已完成 4 章的结构与口吻；得分表述 3–6 条 `「MS 原文」⟦行 id⟧`（优先 MS 开头语言无关清单的句子）；MP 对齐表按 `markpoints[].n`（与 MS 印的编号不一致时列对照，D37 ②）；ER 只作易错，写“考官报告指出 …（行 id）”；对应练习写 `practice/p4/<卷>_q<题号>/`（T35 并行生成，按命名规则写纯文本路径）；前置阶梯 `Lxx Eyy` 要确认 `ladder/levels/` 下存在。
6. 每章写完：`make check`、`python3 build/build.py p4`、`blocks.py` 跑通本章全部 python 块 → 提交 → 更新进度日志。

## front.md（T37A）与 back.md（T37B）

- front：使用指南、记号、P4 考情总览（`<!-- auto:chapter-stats -->`）、P4 通用得分规则（模块头 “(and end where appropriate)”、类型注释、按伪代码结构写、截图格看什么、不用内置函数代劳……每条附 MS 原句）；参照 `papers/p2/front.md`、`papers/p3/front.md`。
- back：跨章入口（按题目特征找题型，覆盖 9 章 36 型）、一道大题的典型得分链（声明 → ADT 操作 → 读文件 → 主程序 → 截图）、证据文档怎样交、P4 命令词与 MS 常用语；参照 `papers/p2/back.md`、`papers/p3/back.md`。

## 审计教训（总控验收重点）

任务卡 §「T26 / T36 审计教训」六条，外加：完整作答必须真能按该题 MS 拿满分（逐个独立得分点数，`//` 是替代说法）；所有页码逐个核对；不照抄有缺陷的 MS 范例（已知缺陷清单见 `tasks/handoff/T35-practice.md`「已知的坑」）。

## 交付

各批：rebase → `make check` → `python3 build/build.py p4` → `make check-scope TASK=T37A|T37B` → push → `gh pr create --base main --title "T37 batch A: P4 front + PR/AR/FL/SR/RC cards"`（B：`T37 batch B: P4 SQ/LT/OP/MP cards + back`）。PR 描述按任务卡「完成标准」，并列出每张新卡的代表题原页与程序运行结果。
