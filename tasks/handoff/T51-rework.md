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

## 5. 第二轮返工（总控 2026-10-25 验收 a921fc2）

第一轮返工把模板去掉了（万能题面 0、空话「测」0、截断 0、235 条「测」各不相同、115 道自写答案、42 个代码块），方向对。抽查 40 道仍有三类会误导导师的问题，**只修这三类，其余保留**：

| 类 | 规模 | 例 |
|:--|:--|:--|
| A 不回答 Q，或「依据」与 A 无关 | 抽查约 1 / 10 | `P4-SQ-02-R1` 问空队列两个指针的初值，A 却是 Dequeue 判空代码；`P4-MP-01-R1` 问空 / 非空两种情况，A 只写了非空，依据是“输出全部记录”；`P4-AR-04-R2` 的依据是“拼接加空格再返回”，与“逐行打印”无关；`P3-SY-12-R1` 问 why，A 是一句给分备注；`P3-DR-02-R2` 题面已经说出答案（“refer to an object in memory”） |
| A 直接用了 MS 的**给分备注**而不是知识 | 约 10 道 | 「1 mark for first 4 rows, 1 mark for second 4 rows」、「Two marks if no errors present」、「XOR (with remainder correct and bracketed and nothing extra)」、「Lines from S3 with correct event labels …」、「Do not allow operators in stacks」、「Any correct Boolean term」、「All original fields are in correct tables」、「Use of correct Flight1 variable …」、「Two correct attributes (…)」、「all correct Boolean operators and punctuation …」 |
| 伪代码答案结构没闭合 | 17 个伪代码块里 13 个 | `IF TopOfStack = 8 THEN` / `RETURN FALSE` 没有 `ENDIF`；`FOR … ` 没有 `NEXT`；`WHILE` 没有 `ENDWHILE`；`PROCEDURE` 没有 `ENDPROCEDURE`。P2 卷首「考场作答方法」第一条就是漏 ENDIF 丢分，题库不能示范它 |

### 做法

1. **`check` 再加三条护栏**：
   - 伪代码块里每个 `IF` / `WHILE` / `FOR` / `REPEAT` / `CASE` / `FUNCTION` / `PROCEDURE` / `CLASS` 都有对应的结束词（`ENDIF` / `ENDWHILE` / `NEXT` / `UNTIL` / `ENDCASE` / `ENDFUNCTION` / `ENDPROCEDURE` / `ENDCLASS`）；省略的循环体用一行 `...` 表示，但结束词必须写。Python 块用 `ast.parse` 能解析（省略处写 `...`，它在 Python 里合法）。
   - A 是直接 MS 引文（不是「非 MS 原文」）时，引文里出现 `mark`、`Accept`、`Reject`、`Allow`、`Do not`、`correct`（不区分大小写）就报错——这些是给分备注，要换成「（非 MS 原文）知识句 + 依据：给分句」，或换一句真正陈述知识的 MS 原句。
   - 输出被这三条拦下的题号清单，作为第二轮返工清单。
2. **逐题核对全部 235 道的 Q / A / 依据三者对齐**（不是只修护栏拦下的）：A 是否**正好**回答 Q（问 initial values 就答初值，问 why 就答原因，问两种情况就两种都答）；「依据」是否支撑 A 的那句话；题面是否已经泄露答案。核对结果记进进度日志：每卷改了哪些题号、为什么。
3. 修完跑 `retrieval.py check`、`make check`，按卷提交 `T51: fix answer alignment in P<N> retrieval items`。
4. PR 描述加「第二轮返工」一节：三条新护栏的前后计数、逐题核对改动的题号清单、上表点名的 15 道题各自改后的完整 Q / A / 依据。

### 补充（总控 2026-10-25，第一轮 PR 里「需要总控决定」的答复）

- 五道“较弱题”：`P3-BL-05-R1`（A 是给分备注，已在上表）、`P1-IR-12-R1`（题面说 “this multimedia calculation” 却没给数据，A 只是一个数，学生无从作答——改成给出图像尺寸与色深、问文件大小的一步，或改测单位换算那一环）、`P4-MP-03-R1`（`print(LinkedList)` 打印的是原始数组，不是按指针遍历的输出——A 改成遍历输出，或改问截图里必须能看到什么）**必须改**；`P4-SQ-04-R1` 的代码块 `while` 没有循环体，被 Python 护栏拦下后补一行 `...` 即可；`P4-FL-02-R2` 合格，保留。
- 当前 Python 代码块里 5 个不能被 `ast.parse` 解析（`P4-PR-01-R1`、`P4-SQ-04-R1` 等，都是循环 / 分支头后缺循环体），第一条护栏会把它们列出来。
- SKILL.md §1 的题库入口由总控在合并 #66 时补，执行工位不改。
