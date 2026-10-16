# T10 · Python 阶梯设计与对照卡（设计工位 cc-A，Opus）

## 目标

为学生设计一条 12 级「剑桥伪代码 ↔ Python」阶梯，让一个只会读简单代码的学生在 3 个月内能独立写 P2 伪代码、在 A2 阶段能独立完成 P4 Python 实操。你负责**课程设计**：每级学什么、按什么顺序、对照卡怎么讲、每道练习练什么。练习的代码与测试由 codex（T14）按你的规格实现——所以你的规格必须精确到无需追问。

## 学生画像

IGCSE CS A*（熟悉 IGCSE 版剑桥伪代码与基础概念）；Python 只能读懂简单代码，愿意真正学会；中文教学，代码与注释用英文。学习顺序：10–12 月走 L01–L08（服务 AS P2），1–3 月走 L09–L12（服务 A2 P4）。

## 输入

- `AGENTS.md`、`docs/PLAN.md`、`schemas/card-format.md` §5、`schemas/exercise-format.md`、`schemas/examples/`（练习格式示例）。
- 考纲与伪代码指南（2027–2029 版）：`$ALEVEL_CS_SOURCES/official/`（默认 `/Users/zhangheqing/Desktop/alevel cs/sources/official/`）。**伪代码写法以指南为唯一权威，卡片里注明指南页码。**
- 公开课：CS50P（https://cs50.harvard.edu/python/ ，讲义与习题）、Think Python 3e（https://allendowney.github.io/ThinkPython/ ）。二者 CC BY-NC-SA 4.0：可改编，必须注明出处；只链接与改写，不整页复制。

## 初拟分级（可调整，调整须在 design.md 写理由）

| 级 | 主题 | 考纲 |
|:--|:--|:--|
| L01 | 变量、数据类型、输入输出、运算与类型转换 | 10.1, 11.1 |
| L02 | 选择：IF / CASE ↔ if/elif、match | 11.2 |
| L03 | 循环：FOR / WHILE / REPEAT…UNTIL ↔ for/while（REPEAT 的写法） | 11.2 |
| L04 | 过程与函数、BYVAL/BYREF ↔ def、返回值、可变对象 | 11.3 |
| L05 | 字符串：剑桥内置函数（MID/LEFT/RIGHT/LENGTH/UCASE/…，1 起下标）↔ 切片与方法 | 插页函数表 |
| L06 | 一维/二维数组 ARRAY[1:n] ↔ list；线性查找、冒泡排序 | 10.2, 9.2 |
| L07 | 文本文件：OPENFILE/READFILE/WRITEFILE/EOF/CLOSEFILE ↔ open/with | 10.3 |
| L08 | 记录 TYPE…ENDTYPE；用数组 + 指针实现栈与队列 | 10.1, 10.4 |
| L09 | 异常处理与输入校验 TRY…EXCEPT | 20.2 |
| L10 | 链表与二叉树（数组 + 指针实现） | 19.1 |
| L11 | 递归；二分查找、插入排序；算法比较 | 19.1, 19.2 |
| L12 | OOP：类、私有属性、构造、getter/setter、继承、多态 | 20.1 |

## 产出（全部在 `ladder/`）

1. `ladder/design.md`：分级总表（每级目标、前置、考纲映射、对应 CS50P / Think Python 讲次）、全局「伪代码 ↔ Python」速查表、阶梯与 P2/P4 题型的衔接说明、每级过关标准。
2. `ladder/levels/L<nn>-<slug>/card.md`：对照卡，按 `schemas/card-format.md` §5 的必需小节。重点讲**剑桥写法与 Python 写法不对应的地方**（1 起 vs 0 起下标、`MID` vs 切片、`REPEAT…UNTIL` 无直接对应、`BYREF` 与可变对象、整除与 `DIV/MOD`、`ENDIF` 等）。
3. `ladder/levels/L<nn>-<slug>/exercises/E<nn>-<slug>/spec.md`：每级 4–6 道练习规格，每份写明：
   - 练习目标与对应的卡片小节；
   - 题面要点（中文导读 + 给学生的英文题干）；
   - **函数名与签名**或脚本型的输入输出约定（标识符用 snake_case；在 L09 以后加入 P4 风格的 CamelCase 指定标识符练习）；
   - 是否先写伪代码（`pseudocode: true/false`）；
   - 必测行为：至少 3 条具体输入 → 期望输出，含边界情况；
   - 需要的数据文件内容（若有）；
   - **mutant 建议**：2–3 个学生真实会犯的错（下标差一、字符串比较数字、漏关文件等）；
   - 人工核对清单（测试测不到的点）；
   - 出处（改编自公开课时写明讲次/习题与许可）。
   - 你**不写** `test_task.py`、`starter.py`、`ref/`——那是 T14 的。

## 分批交付（每批一个 PR）

1. **批 1**：`design.md` + L01–L03 的卡与练习规格。尽快交，codex-2 要等它开工。
2. **批 2**：L04–L08。
3. **批 3**：L09–L12（1 月前交即可；总控届时提醒）。

## 允许写的路径

见 `tasks/scope.json` 的 `T10`：`ladder/README.md`、`ladder/design.md`、`ladder/levels/*/card.md`、`ladder/levels/*/exercises/*/spec.md`，以及 `tasks/progress/T10.md`。

## 完成标准

- `make check` 与 `make check-scope TASK=T10` 全绿。
- 每张卡的伪代码与指南逐字一致（关键字、赋值符号 `←`、数组声明、文件操作语法），并注明指南页码——codex 会逐条审计。
- 规格可执行：codex 不需要追问就能写出测试。
- PR 描述列出本批级别、练习数、对公开课的引用清单、需要总控决定的事项。

## 交叉审计（你的另一项职责）

T14 每批 PR 合并前，总控会请你抽查 codex 写的测试：是否真的测到规格里的行为、mutant 是否像真实错误、有没有把学生正确的不同写法误判。

## 工作方式

- worktree 与分支由总控启动会话时创建：分支 `task/T10-ladder-design`。
- 进度写进 `tasks/progress/T10.md`（已完成 / 进行中 / 下一步 / 坑）。
- 交付：`git fetch origin && git rebase origin/main` → 两个检查 → `git push -u origin HEAD` → `gh pr create --base main --title "T10 batch N: …"`。不要合并。

## 考纲事实（总控已核对 2027–29 版原文）

- 所有卷禁用计算器（考纲第 11 页）。
- P4 只考 19–20 节，**不考低级语言与声明式编程**；考生须提交完整代码与测试证据；**官方源文件不再含二进制文件**——阶梯里的文件练习只需文本文件（L07、L09 不要设计二进制/随机存取文件练习，除非作为可选拓展并注明）。
- 2021 年起认可的教材仍适用。
