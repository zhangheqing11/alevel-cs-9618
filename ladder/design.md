# Python 阶梯 · 总设计（T10）

> 读者：导师会话（教学 skill）、T14 实现者（codex）、总控。学生看 `ladder/README.md` 即可。
> 版本：批 1（本文件全量 + L01–L03 的卡与练习规格）。L04–L12 的卡与规格分别在批 2、批 3 交付；本文件中它们的条目是**计划**，届时可能细调（调整写进 §3）。

## 1. 定位与原则

阶梯是 P2（伪代码笔试）与 P4（Python 上机）共同的基本功线。学生 IGCSE CS A*，熟悉 IGCSE 剑桥伪代码；Python 只会读简单代码。目标：L01–L08（10–12 月）结束时能独立写出 P2 级别的伪代码模块并把它翻译成能过测试的 Python；L09–L12（1–3 月）结束时能独立完成 P4 的典型任务。

设计原则：

1. **伪代码先行、Python 落地。** 每级先讲剑桥写法，再讲 Python 写法，重点放在**两者不对应的地方**（每张卡的 `## 伪代码 ↔ Python 对照` 与 `## 常见坑`）。
2. **伪代码以 2027–29 伪代码指南为唯一权威**（`sources/official/9618_pseudocode_guide_2027-2029.pdf`，下称「指南」），卡片里每个语法点注明指南页码。指南没有、但考试插页给出的函数（`LEFT`、`NUM_TO_STR`、`STR_TO_NUM`、`TO_UPPER`、`ASC`…）注明插页出处（以 `9618_s26_in_21` 为代表，下称「插页」）。考纲 11.1 规定「指南以外的函数会在考试中给出；字符串函数一定会给」（考纲 p.29）。
3. **只做文本输入输出与文本文件。** P4 官方源文件不含二进制文件（考纲 p.40）；随机文件（指南 §9.2 p.26–27）只作可选拓展。
4. **测试判对错，人工判写法。** 行为由 pytest 自动判；伪代码写法、提示语、注释、变量命名等测不到的点写进每题的「人工核对清单」，由导师按指南逐条核对。
5. **错误来自真实考生。** 常见坑与 mutant 优先取自官方 Example Candidate Responses（ECR）的考官点评、Scheme of Work（SoW）里点名的误区；ECR 只用于「易错」，不作给分依据（AGENTS.md §5）。
6. **公开课只链接与改写。** CS50P、Think Python 3e 均为 CC BY-NC-SA 4.0：改编的练习在 `adapted_from` 写明出处与改动；卡片只给讲次链接，不复制原文。

## 2. 分级总表

月份为建议进度（今天 2026-10-16 开学）。「指南」列为伪代码指南页码；「CS50P / TP3e」列给讲次（链接见各卡 `## 延伸阅读`）；教材 = Langfield & Duddell 2e（2019），只作概念参考。

| 级 | 主题 | 目标（学完能做什么） | 前置 | 考纲 | 指南 | CS50P / TP3e | 教材 | 建议时间 | 练习 |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| L01 | 变量、数据类型、输入输出、算术与类型转换 | 写出「输入 → 计算 → 输出」程序的伪代码与 Python；正确使用 `DIV`/`MOD`、`/`、类型转换与输出格式 | IGCSE | 9.2, 10.1, 11.1 | §1–2 p.5–9；§5.1–5.2 p.15；§5.5–5.6 p.16–17 | Lecture 0；PS0 / TP3e ch.1, ch.2, §5.1 | 12.04–12.05, 14.02–14.03, 14.07 | 10 月第 3–4 周 | 5（批 1） |
| L02 | 选择：IF / CASE ↔ if/elif、match | 用嵌套 IF 与 CASE（含范围、OTHERWISE）写多分支；写对复合条件；会选边界测试值 | L01 | 11.1（逻辑运算）, 11.2, 12.3（测试数据） | §5.3–5.4 p.16；§6 p.18–19 | Lecture 1；PS1 / TP3e ch.5 §5.2–5.7, §6.5 | 12.06, 14.04–14.05 | 10 月末–11 月第 1 周 | 5（批 1） |
| L03 | 循环：FOR / WHILE / REPEAT…UNTIL ↔ for/while | 三种循环互译互改；`REPEAT` 的 Python 写法；计数器、累加器、哨兵、输入校验、嵌套循环；能说明为什么选某种循环 | L02 | 11.2 | §7 p.20–21 | Lecture 2；PS2 / TP3e §3.4, ch.7 | 12.07, 14.06 | 11 月第 1–2 周 | 6（批 1） |
| L04 | 过程与函数、BYVAL/BYREF ↔ def、返回值、作用域 | 写过程/函数头、调用（`CALL` 与表达式调用）；BYREF 在 Python 里的三种替代；局部/全局与 `global` | L03 | 9.1（分解）, 11.3, 12.2（结构图） | §8 p.22–24 | Lecture 0（def, return）/ TP3e ch.3, ch.6 | 12.09, 14.08–14.12 | 11 月第 2–3 周 | 5（批 2） |
| L05 | 字符串与插页内置函数（含日期函数） | `MID/LEFT/RIGHT/LENGTH/TO_UPPER/ASC/CHR/NUM_TO_STR/STR_TO_NUM/IS_NUM` ↔ 切片与方法；逐字符处理；1 起与 0 起下标 | L04 | 11.1（内置函数） | §5.5 p.16–17；插页 p.2–4 | Lecture 0（strings）；PS2 / TP3e ch.8 | 14.07 | 11 月第 3–4 周 | 5–6（批 2） |
| L06 | 一维/二维数组 ↔ list；线性查找、冒泡排序 | 声明与初始化 `ARRAY[1:n]`、二维 `[1:r,1:c]` ↔ list / 嵌套 list；下标换算；线性查找、冒泡排序（含提前结束） | L05 | 10.2, 9.2 | §3 p.10–11 | Lecture 2（lists）/ TP3e ch.9, §7.6 | 13.03–13.05, 14.14 | 11 月末–12 月第 1 周 | 5–6（批 2） |
| L07 | 文本文件 | `OPENFILE … FOR READ/WRITE/APPEND`、`READFILE`、`EOF`、`WRITEFILE`、`CLOSEFILE` ↔ `open`/`with`；读到文件尾、读入数组、写出结果 | L06 | 10.3, 20.2（文本部分） | §9.1 p.25–26 | Lecture 6 / TP3e ch.13 | 13.06, 14.15 | 12 月第 1–2 周 | 5（批 2） |
| L08 | 记录 TYPE…ENDTYPE；数组 + 指针实现栈与队列 | 定义与使用记录、记录数组 ↔ 只有属性的 class；用数组 + 栈顶/队首队尾指针实现栈、（线性与循环）队列的入/出 | L07 | 10.1, 10.4；预习 19.1 | §4 p.12–14 | — / TP3e ch.14 | 13.02, 13.07–13.09, 26.01 | 12 月第 2–3 周 | 5（批 2） |
| L09 | 异常处理与输入校验；P4 工作方式 | Python `try/except`；用 `IS_NUM` 式校验与异常两种思路；P4 规定标识符（CamelCase）、全局数组、证据文档 | L08 | 20.2 | 指南无 TRY（见 §3 调整 5）；§9.2 p.26–27 选学 | Lecture 3 / — | 26.02–26.03 | 1 月第 1–2 周 | 4–5（批 3） |
| L10 | 链表与二叉树（数组 + 指针实现） | 链表的查找、插入、删除；二叉树的插入、查找、遍历；空指针约定（-1 或 0） | L09 | 19.1 | §4 p.12–14（指针） | — / — | 23.05–23.09 | 1 月第 3 周–2 月第 1 周 | 5（批 3） |
| L11 | 递归；二分查找、插入排序；算法比较 | 写递归函数并追踪调用栈；二分查找（迭代与递归）、插入排序；Big O 比较 | L10 | 19.1, 19.2 | §8 p.22–24 | — / TP3e §5.8–5.10, §6.6–6.8 | 23.01–23.04, 23.13, 24 | 2 月 | 5（批 3） |
| L12 | OOP：类、私有属性、构造、getter/setter、继承、多态 | `CLASS…ENDCLASS`、`PRIVATE`、`NEW`、`INHERITS`、`SUPER` ↔ `class`、`__init__`、`self.__x`、`super()`；聚合 | L11 | 20.1 | §10 p.28–29 | Lecture 8 / TP3e ch.14–17 | 27 | 3 月 | 5（批 3） |

### 2.1 考纲覆盖核对（Learner Guide p.20 的 Paper 2 自查清单）

| Learner Guide「You should be able to」 | 覆盖的级 | 批 1 状态 |
|:--|:--|:--|
| Write pseudocode from structured English or a flowchart | L02–L04 | **缺口**：批 1 的题面都是文字描述，还没有流程图转伪代码的题；批 2 的 L04 补一道（9618_s24_22 Q2 是流程图题，见 ECR P2 2024 p.8–11） |
| Select and use basic data types including records | L01（基本类型）、L08（记录） | L01 已覆盖 |
| Select and use 1D and 2D arrays；Write pseudocode for 1D and 2D arrays and to process array data | L06 | 批 2 |
| Understand and use text files | L07 | 批 2 |
| Understand and use ADTs including stacks, queues and linked lists | L08、L10 | 批 2、批 3 |
| Write pseudocode statements for declaration of variables and constants, assignment, expressions (arithmetic / logical), input and output | L01、L02 | 已覆盖 |
| Write pseudocode statements for IF, CASE and loop statements | L02、L03 | 已覆盖 |
| Define and use procedures and functions | L04（L01 起当外壳） | 外壳已用，系统讲解在批 2 |
| Test … choice of test data | L02 起每份规格 | 「必测行为」示范边界选值；L02 有专项过关点 |

Learner Guide p.16 对 Paper 2 的建议（伪代码命令用大写、尽量只用考纲给出的命令、给伪代码加注释）已写进 §4.1 第 2 条的核对项。

## 3. 对初拟分级的调整及理由

| # | 调整 | 理由 |
|:--|:--|:--|
| 1 | **关系运算与逻辑运算（`= <> AND OR NOT`）从 L01 移到 L02。** L01 只管算术、连接与类型转换。 | 它们只在条件里用；L01 内容已多。考纲 11.1 的「logical operators」因此跨 L01–L02 覆盖。 |
| 2 | **模块头前移：从 L01 起，练习模板就带 `FUNCTION … RETURNS … ENDFUNCTION` / `PROCEDURE … ENDPROCEDURE` 与 Python `def`**，先只当「外壳」用；L04 再系统讲参数传递、`CALL`、作用域、BYVAL/BYREF。 | P2 写代码题几乎都以「写出过程/函数 X」出题（例：9618_s24_22 Q4 的 `IsRA()`，见 ECR P2 2024 p.14）；IGCSE 已学过这两种头；pytest 函数型测试也需要 `def`。 |
| 3 | **每级至少 1 道「干跑」练习（形态 `trace`）。** 给一段指南写法的伪代码，学生先手算输出填进 `PREDICTED`，再逐行翻译成 Python 自证。 | P2 大量考读码、追踪表；SoW Unit 11（p.35–36）反复要求「给伪代码让学生干跑找错」。手填答案可自动判分。 |
| 4 | **每级至少 1 道「改错/改写」练习**（L01 E04 改错；L02 E05 判断能否改成 CASE；L03 E06 循环改写）。 | P2 常见「找出并改正错误」「用另一种循环改写」题型；SoW p.35–36 的互转与找错活动。 |
| 5 | **L09 的 `TRY…EXCEPT` 改为 Python-only。** 伪代码侧讲「不用异常的输入校验」（`IS_NUM` 等插页函数 + 循环）。 | 指南没有 TRY/EXCEPT 关键字（索引 p.30）；考纲 20.2 只要求「write program code to use exception handling」（考纲 p.38）。 |
| 6 | **L05 增加插页日期函数**（`DAY/MONTH/YEAR/DAYINDEX/SETDATE/TODAY` ↔ `datetime.date`）。 | 日期函数在每份插页里都有（插页 p.3），指南只定义 `DATE` 类型（p.7）；放在「内置函数」一级最自然。 |
| 7 | **L08 的队列包含循环队列**（原表只写「栈与队列」）。 | AS 10.4 要求描述数组如何实现队列；A2 19.1 要求写入/删除算法。循环队列放在 L08 能减轻 L10 的负担。细节批 2 定。 |
| 8 | **L04 加入作用域与 Python `global`。** | P4 大量使用全局数组与全局计数器；Python 在函数里给全局整数重新赋值必须写 `global`，这是 P4 的高频运行错误（批 2 卡片细讲）。 |
| 9 | **P4 风格标识符从 L09 开始**：练习指定 CamelCase 名称（如 `ReadWords()`、`WordArray`），测试按该名称调用；L01–L08 用 snake_case。 | 任务卡要求；P4 题目给定标识符（如 9618_s24_42 Q1，见 ECR P4 2024 p.5），考生必须照用。 |

其余与初拟表一致。

## 4. 过关标准

### 4.1 每级通用（写进 `ledger/ladder.csv` 时据此标「已掌握」）

1. **全绿**：本级全部练习 `make try EX=…` 通过，且没有先看 `ref/`。
2. **伪代码合格**：`pseudocode: true` 的练习，`answer.pseudo` 经导师按指南逐条核对（关键字大写与拼写、`←`、`DECLARE`/`CONSTANT` 格式、每个结构的结束关键字、提示语；关键步骤有 `//` 注释——Learner Guide p.16 建议给伪代码加注释）——人工核对清单全部勾上；错一处就改到对为止。
3. **能讲坑**：导师从本卡 `## 常见坑` 抽 2 条，学生能说出「错在哪、为什么、怎么改」。
4. **过关小测**：导师现编一道本级同类变式（新情境、新数据，不入库），学生先写伪代码再写 Python，20 分钟内完成且自测通过。
5. 1–4 都满足 → `已掌握`；否则 `学习中`，在「解释证据」列写清缺口，章末复测（加速模式，见 T11 skill）。

### 4.2 各级专项（在通用标准之外必须当场演示）

| 级 | 专项过关点 |
|:--|:--|
| L01 | 不看卡说出 `17 / 5`、`17 DIV 5`、`17 MOD 5` 的结果与 Python 写法；解释为什么 `input()` 后要 `int()`；`OUTPUT "A", X` 与 `print("A", x)` 的空格差别 |
| L02 | 把一段多分支 IF 改写成 CASE（或说明为何不能）；给一个条件写出全部边界测试值 |
| L03 | 把一个 `REPEAT…UNTIL` 正确译成 Python 并说明条件为什么不取反；为一个场景选择循环并说出理由；`FOR i ← 1 TO N` 的 `range` 写法脱口而出 |
| L04–L12 | 批 2、批 3 补 |

## 5. 全局「伪代码 ↔ Python」速查表

伪代码列严格按指南（页码）；Python 列为本阶梯推荐写法。「级」= 首次教学的级别。

| 主题 | 剑桥伪代码（指南页） | Python | 级 | 不对应之处 |
|:--|:--|:--|:--|:--|
| 注释 | `// text`（p.6） | `# text` | L01 | |
| 声明变量 | `DECLARE Counter : INTEGER`（p.8） | `counter = 0`（可写 `counter: int = 0`） | L01 | Python 没有声明，第一次赋值才创建变量 |
| 常量 | `CONSTANT HourlyRate = 6.50`（p.8） | `HOURLY_RATE = 6.50` | L01 | 常量用 `=` 不用 `←`，且只能是字面量；Python 常量只靠全大写约定 |
| 赋值 | `Counter ← Counter + 1`（p.9） | `counter = counter + 1`（或 `counter += 1`） | L01 | 伪代码没有 `+=` |
| 数据类型 | `INTEGER REAL CHAR STRING BOOLEAN DATE`（p.7） | `int float str str bool datetime.date` | L01 | Python 没有单独的字符类型 |
| 字面量 | `5`、`4.0`、`'x'`、`"Hi"`、`TRUE`（p.7） | `5`、`4.0`、`"x"`、`"Hi"`、`True` | L01 | 伪代码 CHAR 用单引号、STRING 用双引号；实数两边都要有数字 |
| 输入 | `INPUT Answer`（p.15） | `answer = input("Prompt: ")` | L01 | `input()` 永远返回 `str`，数字要 `int()`/`float()` |
| 输出 | `OUTPUT "You have ", Lives, " lives left"`（p.15） | `print(f"You have {lives} lives left")` | L01 | `OUTPUT` 的逗号不加空格；`print` 的逗号加一个空格 |
| 算术 | `+ - * /`（p.15） | `+ - * /` | L01 | `/` 结果一律为 REAL / float |
| 整除、取余 | `17 DIV 5`、`17 MOD 5`（p.15；插页 p.4） | `17 // 5`、`17 % 5` | L01 | 负数时 `//` 向下取整，与指南「小数点前的整数」不同 |
| 乘方 | 指南没有乘方运算符 | `x ** 2` | L01 | 伪代码写 `X * X` |
| 取整 | `INT(27.5415)`（p.17） | `int(27.5415)` | L01 | |
| 随机数 | `RAND(87)`（p.17） | `random.random() * 87`；`INT(RAND(6)) + 1` ↔ `random.randint(1, 6)` | L01 | `randint` 两端都包含 |
| 连接 | `"Summer" & " " & "Pudding"`（p.17） | `"Summer" + " " + "Pudding"` | L01 | Python 的 `+` 两边必须都是 `str` |
| 数 ↔ 串 | `NUM_TO_STR(87.5)`、`STR_TO_NUM("23.45")`（插页 p.2） | `str(87.5)`、`float("23.45")` / `int("23")` | L01 | |
| 比较 | `= <> < > <= >=`（p.16） | `== != < > <= >=` | L02 | 伪代码 `=` 是比较；Python 比较是 `==` |
| 逻辑 | `AND OR NOT`（p.16） | `and or not` | L02 | Python 可写 `0 <= x <= 100`，伪代码不行 |
| IF | `IF … THEN … ELSE … ENDIF`（p.18） | `if …:` / `else:` | L02 | |
| 多分支 | ELSE 里嵌套 IF（p.18） | `elif` | L02 | 指南没有 `ELSEIF` |
| CASE | `CASE OF Move … OTHERWISE : … ENDCASE`（p.19） | `if/elif/else` 或 `match/case`（`case _:`） | L02 | 范围 `80 TO 100 :` 在 `match` 里要用守卫 `case m if 80 <= m <= 100:` |
| 计数循环 | `FOR Index ← 1 TO 30 … NEXT Index`（p.20） | `for index in range(1, 31):` | L03 | `range` 不含终点 |
| 步长 | `FOR Position ← 20 TO 10 STEP -1`（p.20, p.27） | `for position in range(20, 9, -1):` | L03 | |
| 前测循环 | `WHILE Number > 9 … ENDWHILE`（p.21） | `while number > 9:` | L03 | 没有 `DO` |
| 后测循环 | `REPEAT … UNTIL Password = "Secret"`（p.20–21） | `while True:` … `if password == "Secret": break` | L03 | Python 没有后测循环；`UNTIL` 是**退出**条件 |
| 过程 | `PROCEDURE Square(Size : INTEGER) … ENDPROCEDURE`；`CALL Square(100)`（p.22–23） | `def square(size: int) -> None:`；`square(100)` | L04（L01 起当外壳） | Python 调用不写 `CALL` |
| 函数 | `FUNCTION Max(Number1 : INTEGER, Number2 : INTEGER) RETURNS INTEGER … RETURN … ENDFUNCTION`（p.23–24） | `def max_of(number1: int, number2: int) -> int:` … `return …` | L04（L01 起当外壳） | 函数只在表达式里调用，不写 `CALL`（p.23） |
| 参数传递 | `BYVAL` / `BYREF`（p.24） | 没有直接对应：返回新值；可变对象（list）原地修改；或返回多个值 | L04 | |
| 一维数组 | `DECLARE StudentNames : ARRAY[1:30] OF STRING`（p.10） | `student_names = [""] * 30`（下标 0–29） | L06 | 指南一般下界为 1，Python 从 0 起 |
| 二维数组 | `DECLARE NoughtsAndCrosses : ARRAY[1:3,1:3] OF CHAR`；`NoughtsAndCrosses[2,3] ← 'X'`（p.10） | `grid = [[" "] * 3 for _ in range(3)]`；`grid[1][2] = "X"` | L06 | 不能写 `[[" "] * 3] * 3`（三行是同一个 list） |
| 字符串函数 | `LENGTH(S)`、`MID(S, X, Y)`、`RIGHT(S, X)`（p.16–17）；`LEFT(S, X)`（插页 p.2） | `len(s)`、`s[x - 1:x - 1 + y]`、`s[len(s) - x:]`、`s[:x]` | L05 | 1 起 vs 0 起；`s[-0:]` 是整个串 |
| 大小写 | `UCASE/LCASE`（CHAR，p.17）；`TO_UPPER/TO_LOWER`（CHAR 或 STRING，插页 p.2） | `.upper()` / `.lower()` | L05 | 指南与插页名称不同，以当卷插页为准 |
| 字符编码 | `ASC('A')`、`CHR(65)`（插页 p.3） | `ord("A")`、`chr(65)` | L05 | |
| 文本文件 | `OPENFILE "F.txt" FOR READ`、`READFILE`、`EOF("F.txt")`、`WRITEFILE`、`CLOSEFILE`（p.25–26） | `open("F.txt", "r")`、`readline()` / `for line in f`、`write(text + "\n")`、`close()` / `with` | L07 | `READFILE` 读出的行不含换行符；Python 读出的行带 `"\n"` |
| 记录 | `TYPE StudentRecord … ENDTYPE`；`Pupil1.LastName ← "Johnson"`（p.13–14） | 只有属性的 `class`（或 `@dataclass`） | L08 | |
| 指针、枚举、集合 | `TYPE TIntPointer = ^INTEGER`、`TYPE Season = (…)`、`SET OF`（p.12–13） | 用数组下标充当指针；`enum.Enum`；`set` | L08/L10 | 阶梯里指针一律用数组下标实现 |
| 随机文件 | `OPENFILE … FOR RANDOM`、`SEEK`、`GETRECORD`、`PUTRECORD`（p.26–27） | 选学（P4 源文件不含二进制文件） | L09 选学 | |
| 异常 | 指南没有 | `try:` / `except ValueError:` / `finally:` | L09 | |
| 类 | `CLASS Pet` / `PRIVATE Name : STRING` / `PUBLIC PROCEDURE NEW(GivenName : STRING)` / `ENDCLASS`（p.28） | `class Pet:` / `def __init__(self, given_name: str):` / `self.__name = given_name` | L12 | 构造过程名为 `NEW`；Python 私有靠 `__` 前缀（名字改写） |
| 继承 | `CLASS Cat INHERITS Pet`；`SUPER.NEW(GivenName)`（p.28） | `class Cat(Pet):`；`super().__init__(given_name)` | L12 | |
| 创建对象 | `MyCat ← NEW Cat("Kitty", "Shorthaired")`（p.29） | `my_cat = Cat("Kitty", "Shorthaired")` | L12 | |
| 调用方法 | `Player.SetAttempts(5)`（p.28） | `player.set_attempts(5)` | L12 | |

**字形说明（给审计）**：指南 PDF 文本层里的 CHAR 单引号是排版字符（抽出来是 U+A78C `ꞌ`），减号有时是 `–`/`−`。本阶梯一律写 ASCII `'` 与 `-`，这不算与指南不一致。

## 6. 阶梯与 P2 / P4 题型的衔接

题型码由 T21（P2）与 T3x（P4）定义；届时各题型卡写「阶梯前置：Lxx」，本表随之回填题型码。

| 考试中的典型任务 | 先修级 | 阶梯里对应的练习形态 |
|:--|:--|:--|
| P2：按文字描述写出过程/函数的伪代码（提示、输入、处理、输出） | L01–L04 | 每级 `pseudocode: true` 的 io 过程型/函数型练习 |
| P2：读伪代码、填追踪表、写输出 | L01–L03 起每级 | `trace` 型（`PREDICTED` + 翻译自证） |
| P2：找出并改正伪代码错误 | L01 起 | 改错题（L01 E04 等） |
| P2：流程图 / 结构化英语 → 伪代码 | L02–L04 | 批 2 起加入「按结构化英语写伪代码」题 |
| P2：用另一种循环/CASE 改写 | L02–L03 | L02 E05、L03 E06 |
| P2：选择测试数据（正常、异常、边界） | L02 起 | 每份规格的「必测行为」示范边界选值；L02 过关点 |
| P2：字符串处理（插页函数、逐字符循环） | L05 | 批 2 |
| P2：数组、线性查找、冒泡排序 | L06 | 批 2 |
| P2：文本文件读写 | L07 | 批 2 |
| P2：记录；栈、队列、链表的概念与数组实现 | L08 | 批 2 |
| P4：读源文件到全局数组、处理并输出 | L06–L07, L09 | 批 2、批 3（P4 风格标识符、`script` 型） |
| P4：栈、队列、链表、二叉树 | L08, L10 | 批 2、批 3 |
| P4：查找、排序、递归 | L06, L11 | 批 2、批 3 |
| P4：类、继承、getter/setter | L12 | 批 3 |
| P4：异常处理与测试证据 | L09 | 批 3 |

## 7. 练习规格约定（给 T14）

### 7.1 目录与命名

- 级目录：`ladder/levels/L<nn>-<slug>/`；练习目录：`exercises/E<nn>-<slug>/`；每个练习目录里只有一份 `spec.md`（T10 写），其余文件 T14 写。
- 本批：`L01-variables-io`、`L02-selection`、`L03-iteration`。计划中的后续级：`L04-subroutines`、`L05-strings`、`L06-arrays`、`L07-text-files`、`L08-records-stacks-queues`、`L09-exceptions-validation`、`L10-linked-lists-trees`、`L11-recursion-algorithms`、`L12-oop`。
- Python 标识符：L01–L08 用 snake_case；伪代码标识符按指南用 PascalCase（p.5）。规格同时给出两者，例如 `FUNCTION Grade(Mark : INTEGER) RETURNS STRING` ↔ `def grade(mark: int) -> str`。

### 7.2 四种练习形态

| 形态 | 学生写什么 | 测试怎么测 | `meta.entry` |
|:--|:--|:--|:--|
| `function` 函数型 | 纯函数：参数进、`return` 出 | 直接调 `sol.<entry>(…)`；比对返回值，必要时比对类型（`type(r) is int` 等） | 函数名 |
| `io` 输入输出过程型 | `def <entry>() -> None`，内部用 `input()` / `print()` | `feed_input(monkeypatch, …)` 喂输入 → 调 `sol.<entry>()` → `capsys.readouterr().out` 取输出，按 7.3 比对 | 过程名 |
| `trace` 干跑型 | 模块级常量 `PREDICTED`（手算答案）+ 一个翻译函数 | ① `sol.PREDICTED` 与期望逐项比对；② 运行翻译函数，按 7.3 或返回值比对 | 翻译函数名 |
| `script` 脚本型 | 整个程序（读写文件） | `tools/testkit.run_script` | `main`（L07 起使用；本批没有） |

`io` 与 `trace` 的 `starter.py` 末尾必须有守卫，保证测试 `import` 时不会卡在 `input()` 上：

```python
if __name__ == "__main__":
    split_seconds()
```

### 7.3 输出比对规则（`io` 与 `trace`）

- 「输出行」= `capsys` 取到的 stdout 按行切开、去掉每行行尾空白、丢掉空行（与 `testkit.ScriptResult.lines` 同一规则）。
- 规格「必测行为」里写的期望输出就是输出行列表，**逐行完全相等**（列表相等，不多不少）。
- 提示语不检查：`feed_input` 替换后的 `input()` 不会打印提示语。因此 `task.md` 要告诉学生：**提示语写进 `input("…")` 的括号里，不要另起一行 `print` 提示**；除规定输出外不要 `print` 别的东西。
- 喂入的输入条数恰好等于正确程序需要的条数：程序多要一次输入时，`feed_input` 抛 `AssertionError`，测试失败——这正是检查「循环该停没停」的手段。

### 7.4 数值比对

- 函数返回 `float`：`pytest.approx(expected, abs=1e-9)`。
- 打印出来的数：按规格给的格式逐字比对（规格会写明「保留 1 位/2 位小数」或「原样 print」）。规格里的测试值已经避开 `.5` 舍入临界点，T10 已用参考实现核对过。

### 7.5 测试与 mutant

- 「必测行为」每一行（`B1`、`B2`…）至少对应一个测试，测试 docstring 写该编号，如 `"""B3: boundary 79 -> B"""`。同类的多行可合并成一个参数化测试，但 docstring 要列出覆盖的编号。
- 规格「mutant 建议」逐条实现为 `ref/mutant_<n>.py`（编号同规格的 M1、M2…）。每个 mutant 必须让至少一个测试失败；**不得写成死循环**（会拖垮 `make check`）。
- 不要对实现细节过拟合：`for`/`while`、`if/elif`/`match`、链式比较、字符串方法等不同的正确写法都必须能通过。写法上的要求（如「伪代码必须用 CASE」）只进人工核对清单。
- 只用标准库；单个练习测试总时长 < 5 秒；不依赖随机数与时间。

### 7.6 `task.md` 与 `answer.pseudo`

- `task.md` = 规格「题面」的中文导读 + English task（原样）+ 规格给出的伪代码块（原样，`pseudocode` 围栏）+ 「人工核对清单」。
- `pseudocode: true` 时，`answer.pseudo` 照抄规格「接口」里给出的模板（模块头、注释行、结束关键字），一字不改。

### 7.7 规格文件的结构（每份 `spec.md` 都按此顺序）

1. 属性表：`id`、目录、形态、`entry`、`pseudocode`、`files`、`skills`、`difficulty`、`title`（meta 用英文标题）、`adapted_from`、对应卡片小节。
2. 练习目标。
3. 题面：中文导读；English task（给学生的英文题干）；给定伪代码（若有）。
4. 接口：Python 签名（`starter.py` 用）与 `answer.pseudo` 模板（若有）。
5. 必测行为：编号表（输入 → 期望），含边界。
6. 数据文件（若有）。
7. mutant 建议：M1、M2…（错误描述 + 应在哪条行为上失败）。
8. 人工核对清单。
9. 出处。

### 7.8 技能标签（`meta.skills`）

本批使用的词表（小写短横线）。T21 定义 `papers/p2/skill_tags.json` 后，二者对齐（见「需要总控决定」）。

| 标签 | 含义 | 标签 | 含义 |
|:--|:--|:--|:--|
| `trace-dry-run` | 干跑、预测输出 | `relational-ops` | 比较运算 |
| `translate-pseudocode` | 伪代码逐行译成 Python | `logic-ops` | AND / OR / NOT |
| `declare-constant` | DECLARE 与 CONSTANT | `nested-if` | 嵌套 IF / elif |
| `type-conversion` | `input` → `int`/`float`、`str()`、`NUM_TO_STR` | `case-of` | CASE / match |
| `div-mod` | 整除与取余 | `case-range` | CASE 范围子句 |
| `operator-precedence` | 运算优先级与括号 | `boundary-values` | 边界值 |
| `output-format` | OUTPUT 分隔、print 空格、小数位 | `boolean-return` | 返回 BOOLEAN |
| `string-concat` | `&` ↔ `+` | `char-compare` | 字符大小比较 |
| `input-prompt` | 输入前的提示 | `count-loop` | FOR 计数循环 |
| `find-fix-errors` | 找错改错 | `loop-step` | STEP 与负步长 |
| `return-value` | 返回值 | `pre-condition-loop` | WHILE |
| `accumulator` | 累加器、计数器 | `post-condition-loop` | REPEAT…UNTIL |
| `sentinel-loop` | 哨兵值（rogue value）循环 | `input-validation` | 输入校验循环 |
| `nested-loops` | 嵌套循环 | `loop-choice` | 选择与改写循环 |
| `loop-bounds` | 循环边界、差一 | | |

## 8. 出处与许可

| 资料 | 用法 | 许可 / 说明 |
|:--|:--|:--|
| CS50's Introduction to Programming with Python（CS50P），David J. Malan，<https://cs50.harvard.edu/python/> | 讲义链接（`notes/<n>/`）；L01 E03、L02 E03、L03 E03、L03 E04 改编自其习题或讲义思路（改了数据、规则与输出） | CC BY-NC-SA 4.0：署名、链接许可、注明改动；改编物同许可 |
| Think Python, 3rd edition，Allen B. Downey，<https://allendowney.github.io/ThinkPython/> | 只给章节链接，不改编练习 | CC BY-NC-SA 4.0 |
| 剑桥 2027–29 伪代码指南、考纲；P2 插页；SoW；Learner Guide；ECR P2/P4 | 语法权威（指南）、函数表（插页）、误区与 mutant 来源（ECR、SoW） | 剑桥版权；只引页码与短语，不整页复制 |
| Langfield & Duddell, *Cambridge International AS & A Level Computer Science Coursebook* 2e（2019） | 概念参考，注明节号与页码 | 版权所有；不复制原文。书中伪代码与 2027–29 指南不一致处以指南为准 |

本批引用清单：

- CS50P Lecture 0 notes <https://cs50.harvard.edu/python/notes/0/>；Lecture 1 notes <https://cs50.harvard.edu/python/notes/1/>；Lecture 2 notes <https://cs50.harvard.edu/python/notes/2/>。
- CS50P Problem Set 0 “Tip Calculator” <https://cs50.harvard.edu/python/psets/0/tip/>（→ L01 E03）；Problem Set 1 “Math Interpreter” <https://cs50.harvard.edu/python/psets/1/interpreter/>（→ L02 E03）；Problem Set 2 “Coke Machine” <https://cs50.harvard.edu/python/psets/2/coke/>（→ L03 E04）；Lecture 2 “Improving with User Input”（→ L03 E03）。
- Think Python 3e ch.1、2、3、5、6、7（各卡列出具体小节锚点）。

## 9. 待定与需要总控决定

见 `tasks/progress/T10.md` 与 PR 描述「需要总控决定」。本批涉及：输出比对辅助函数是否进 `tools/testkit.py`；阶梯技能标签与 P2 词表对齐；`ledger/ladder.csv` 的「优先级」列对阶梯的填法；ECR 考官范答中出现的非指南写法（`ELSIF`、`INPUT a, b, c`）在 P2 批改时如何对待（属 T11）。
