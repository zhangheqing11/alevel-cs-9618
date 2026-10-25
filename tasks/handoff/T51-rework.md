# 交接 · T51 返工（#66 题库内容打回）

任务卡与格式不变：`tasks/T51-retrieval-bank.md`、`tasks/handoff/T51-retrieval.md`。续做分支 `task/T51-retrieval-bank`（PR #66），推送后 PR 自动更新。

## 1. 验收结论（总控 2026-10-25）

**保留**：`scripts/retrieval.py` 的 `pick` / `show` 逻辑、`references/retrieval/README.md`、`few-shots.md` / `theory.md` / `handoff-template.md` 的挂钩改动、文件格式与题号。

**打回**：题库正文是按模板批量生成的，学生拿到不知道在问什么，导师也批不了：

| 问题 | 数量 | 例 |
|:--|:--|:--|
| 题面是同一句万能模板 | 72 / 235 | `P4-SQ-02-R2`：“In a queue of help-desk tickets, for linear queue in an array, state one required step, condition, or reason.” |
| 「测」是同一句空话 | 103 / 235 | “只测这一题型的一个关键得分点。” |
| 「测」从卡里截断粘贴，以“……”结尾 | 12 | `P4-SQ-02-R1` 的测把整段卡点截在半个词 |
| 〔换情境〕只是在 R1 的问题前加一个场景短语，答案与 R1 同一句 MS | 大多数 R2 | “In an 8-bit register adding two large positive values, in a fixed-width register, what does overflow mean?” |
| 题型名直接贴进题面 | 多处 | “for compression methods: rle and lossy techniques, …”；“In a new situation, …” |
| 答案不回答题面 | 多处 | `P4-SQ-02-R2` 问“一个步骤 / 条件 / 理由”，答案是 Dequeue 取值那一分，测却在讲判空 |
| 全库 0 道代码答案 | — | P2 / P4 写代码的题型，检索题应当让学生写出关键的那一行 |

## 2. 重写规则（每一道都要满足）

1. **手写，不用脚本生成文字**。脚本只用于解析、校验和统计。每道题都要能回答：“学生不看卡，30 秒内知道要答什么吗？答案是不是正好回答了这个问题？”
2. **Q**：针对这一题型的具体一环，问法具体、只有一个答案；不出现题型名、不出现 “state one required step, condition, or reason”“In a new situation”“In a different …” 这类套话。
3. **测**：一句中文，不超过 40 字，说清这题测哪一环（导师批 ✗ 时就讲这一句）。同卷内不允许两道题的测完全相同。不以“……”结尾。
4. **A 必须直接回答 Q**：
   - 能用该卡已出现的 MS 原句完整回答时，写 `「…」⟦行 id⟧`；
   - 否则（换情境题、代码题大多如此）写自己的答案并标 `（非 MS 原文）`，下一行 `依据：「…」⟦行 id⟧` 给出支撑它的 MS 句。
5. **〔换情境〕要真的换**：把同一个模型放进一个新场景，学生必须**用**模型推出答案，答案的字面与 R1 不同。范例（few-shots 示例 8）：光盘写入的缓冲区 → “Streaming a video: at which end is the buffer, and whose speed difference does it smooth out?”，答案“在接收端，抹平到达速度与播放速度之差”。R2 的 A 与 R1 的 A 是同一句 MS 的，一律不算换情境。
6. **写代码的题型**（P2 的 PG / DT / SD 中要写伪代码的型、P4 全部写代码的型、P3 写伪代码的型）：至少一半的题让学生写出关键的 1–3 行（循环头、判满 / 判空条件、指针移动、文件打开模式、递归基本情况），A 是代码块（非 MS 原文，伪代码合 2027–29 指南，Python 合 D10）+ `依据：` 行。

## 3. 给 `check` 加护栏（`retrieval.py`，在你的范围内）

把下面这些变成 `check` 的报错，返工完成时全部为 0：

- Q 含 `state one required step`、`In a new situation`、`In a different`，或含该题型的 `name_en` 原文（不区分大小写；只对三个词以上的 `name_en` 生效，免得 “Interrupts” 这类短名误报）；
- 测是 “只测这一题型的一个关键得分点” 或以 “……” / “...” 结尾，或超过 40 个字符，或在同卷内与另一道题的测完全相同；
- 〔换情境〕题的 A 与同题型另一道题的 A 完全相同；
- 写代码题型（在脚本里列出题型码清单，PR 里贴出）里代码答案不足一半。

## 4. 执行方案

1. 续做 worktree（交接 README §1），`git pull` 到 PR 最新。
2. 先改 `check`（§3），跑一次，把报错清单存进 `work/tmp/t51-errors.txt`，作为返工清单。
3. 逐卷逐章重写（P1 → P2 → P3 → P4）：每章先 `rows.py card <章码>` 重读卡点、反例、考官在换什么，再写；已经合格的题（具体问法 + 具体的测 + A 正好回答）可以保留。每章跑 `retrieval.py check <卷>` 与 `make check`，提交 `T51: rewrite <章码> retrieval items by hand`，更新进度日志。
4. 全部完成后：`retrieval.py check` 全过；用临时记录表副本重跑 `pick` / `show` 演示。
5. PR 描述加「返工」一节：§3 各项计数前后对比、每卷代码题比例、每卷随机抽 5 道（`pick --seed`）的完整 Q / A / 测。
6. 交付：rebase → `retrieval.py check` → `make check` → `make check-scope TASK=T51` → `git push --force-with-lease`。不合并、不推 main。
