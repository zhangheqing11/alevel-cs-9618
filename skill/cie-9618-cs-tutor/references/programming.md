# P2 伪代码卷：题型卡 → 代表题 → 练习 → 「测一下」；伪代码批改规则（P3 写代码题共用）

> 在 SKILL.md 的共用协议之下使用。证据规则、模式、门槛、记录表以 SKILL.md 为准。P4 上机见 p4-practical.md；P3 写伪代码题的流程见 theory.md §6.2，批改用本文件 §6。

## 1. 这张卷

| 项 | 内容 |
|:--|:--|
| 时长 / 分值 | 2 h / 75 |
| 考纲 | 9–12 节 |
| 手册 | 4 章 46 型：AD 算法设计与问题求解 → DT 数据类型与数据结构 → PG 编程 → SD 软件开发 |
| 作答 | 笔答，**用剑桥伪代码**；附插页（内置函数与运算符表，以当卷为准） |
| 题目特点 | 情景 + 多个小问：写过程 / 函数、补全算法、追踪表、找错改错、测试数据、结构图、状态转换图、文件处理、字符串处理、记录与数组、栈 / 队列 / 链表的使用 |

学生在 P2 写伪代码，同题再写 Python 跑测试：伪代码按 MS 人工批，Python 用 pytest 自动测（同一算法的两种写法，Python 帮他确认逻辑，也是 P4 的基本功）。

## 2. 资料

- **题型卡**：`rows.py card P2-XX-NN`——考法、识别信号、解题思路、伪代码模板与 Python 对照、得分表述、得分点地图、易错、代表题、变式、刷题清单。**对照表**：`rows.py card P2-<章码> --core`（伪代码 ↔ Python 模板）。
- **小问行**：写代码小问（≥ 4 分）带 `markpoints`：`n`、`text`（MS 原文）、`marks`、`skills`；`ms_max` 是 Max 上限。其余小问看 `ms_text`。
- **练习文件夹**：`practice/p2/<卷>_<小问>/`（126 道，格式 `schemas/exercise-format.md`）。找法：`index.json` 的 `exercise_paths`，或 `rows.py ex "<行 id>"`。题目有图时 `assets/` 里有 QP 原图裁切，task.md 里引用。
- **技能词表**：`papers/p2/skill_tags.json`。
- **插页**：`rows.py files <卷>` 的 `in` 行（P2 每卷一份）。
- **范答与点评**：ECR 2021 覆盖 `9618_s21_22`；Example Responses 2024 覆盖 `9618_s24_22`；SPA 覆盖 2021 样卷 2。用法同 theory.md §8。
- **阶梯**：`ladder/design.md`（全局伪代码 ↔ Python 速查表 §5、各级与 P2 题型的衔接 §6）、`ladder/levels/*/card.md`。

## 3. 首学单元流程（P2）

1. **开章**：同 theory.md §2，另查本章题型依赖的阶梯级（卡片「阶梯衔接」+ `ladder/design.md` §6 + `ledger/ladder.csv`）。没过的阶梯级先补（可以只做该级对照卡 + 1–2 道练习的快速版，记在 ladder 表）。
2. **概念速览**：本章的结构或模式（例如「读文件到 EOF 的循环」「数组实现的队列」）：用途 → 伪代码模板（逐字按指南）→ Python 对照 → 两者不对应的地方（§7）→ 一个手追踪的小例子。
3. **逐型**：题型卡 → 代表题精讲（§4）→ 变式（练习文件夹，§5）→「测一下」批改（§5–§6）→ 记录表（得分、测试数、失分技能）。
4. **阶段检查 / 章末**：同 SKILL.md §5；章末复测编程题型时，另选一道有练习文件夹、没做过的题。

非编程小问（追踪表、找错、测试数据、结构图、生命周期等）按 theory.md §3 的理论版步骤讲，要点见 §10。

## 4. 代表题精讲（编程版）

适用于写代码的小问（「Write pseudocode for…」「Complete the algorithm…」；P3 写伪代码题同样适用）。**直接讲，不先让学生做。**

1. **出处与题型**：题号、分值、得分点数与 Max 上限、题型码；确认已拿到 QP、配对 MS 与插页。
2. **读规格**：把题干要求逐条列成清单——标识符名、参数（及 BYVAL / BYREF）、返回类型、全局变量、文件名与数据格式、输出格式与提示语。告诉学生：MS 的得分点几乎一一对应这些要求。
3. **设计**：先用 structured English 写步骤；选循环（计数 / 前测 / 后测）并说出理由；需要的数据结构；边界情况（空文件、找不到、第一个 / 最后一个元素）。
4. **完整解**：伪代码逐字按指南、带注释，在注释里标出对应的得分点号（`// MP3`），让学生看到「哪几行换哪一分」。
5. **MS 逐点对齐**：表格列出每个得分点的 MS 原文、对应的行、技能标签；说明 Max 上限；MS 给的是「示例解」，其他正确算法只要满足得分点描述同样给分。
6. **规范要点**：这道题涉及的指南规则（`←`、`ENDIF`、`NEXT i`、过程用 `CALL`、函数不用 `CALL`、`RETURN` 与 `OUTPUT` 的区别、文件命令格式等），注明指南节号（§6 表）。
7. **对照**：同一算法的 Python 写法与不对应的坑（§7）。
8. **易错**：卡片「易错与失分」+ 该题考官报告摘录（「考官报告指出 …」）+ 该卷若有范答 / 点评就展示相关段落。
9. **迁移**：常见变化（换文件格式、换数据结构、加一个条件、改成函数返回值）各自影响哪几行。

## 5. 练习文件夹工作流

1. **选变式**：卡片「下一道变式」（括号备注只给自己看）或刷题清单里有练习文件夹的题。
2. **布置**：你运行 `make try EX=practice/p2/<练习>`，它创建 `attempts/practice/p2/<练习>/solution.py`（函数签名 + `raise NotImplementedError`），`meta.json` 里 `pseudocode: true` 时还有 `answer.pseudo`（含题目要求的模块头），P2-AD-06 是 `answer.steps.md`（编号英文步骤，D38）。告诉学生：
   - 题面在 `practice/p2/<练习>/task.md`：作答前只读开头的说明、「英文原题与给定信息」「Python 接口」（有图时看 `assets/` 的原图）；**「人工核对清单」是 MS 得分点，写完再看**。
   - 在 VS Code 打开 `attempts/practice/p2/<练习>/`：**先**写 `answer.pseudo`（或 `answer.steps.md`），再写 `solution.py`（同一算法的 Python，接口按「Python 接口」一节）。
   - 程序要读的数据文件在练习的 `files/`；测试会把它们复制到临时目录，程序里直接用文件名打开（`open("Trees.txt")`），不写绝对路径。
   - 不看 `test_task.py` 和 `ref/`；可以随时自己跑 `make try EX=…` 看 Python 测试结果。
3. **学生说「测一下」**：
   1. **先批伪代码**（或步骤）：读 `answer.pseudo`，`rows.py get "<行 id>" --ms`，按 §6 逐点给分，填得分点表，再另列规范提示。伪代码的**首次提交**就是这道题的伪代码成绩（之后改对了也不改首次成绩）。
   2. 运行 `make try EX=…`，用中文解读：失败的测试名、docstring 里的行 id 与得分点、输入 / 期望 / 实际、可能的原因。不直接给修正代码，按提示阶梯（§9）走。`skipped` 表示没找到作答文件，`NotImplementedError` 表示函数还没写。
   3. task.md「人工核对清单」逐条检查。
   4. 判定（SKILL.md §6 编程门槛）→ 写记录表：`得分="5/7 · 6/7 tests"`、独立题目（行 id）、错误类别、失分技能、解释证据。
4. **改了再测**：Python 可以改到全绿（这是允许的调试）；记录表「得分」写伪代码首次的 MS 分与最后的测试结果，状态按门槛判定。

> **提示语规则（D13）**：练习的提示语要写在 `input("…")` 括号里。学生照伪代码先 `print` 提示再 `input()`，测试会因多出的输出行失败——这时先解释规则、让学生改，不算逻辑错误、不记错误类别。
>
> **QP 与 MS 范例不一致（D31）**：task.md「Python 接口」会写明测试按 QP 判的边界；人工批伪代码时按 MS 得分点给分，学生写成 MS 范例那样不扣分。

## 6. 伪代码批改规则（P2，P3 写代码题同样适用）

**权威**：写法以 2027–29 伪代码指南为准；给分以该题 MS 为准。

| 指南节 | 内容 | 页 |
|:--|:--|:--|
| §1.3–1.5 | 关键字大写、标识符混合大小写、注释 `//` | 5–6 |
| §2.4–2.6 | `DECLARE x : INTEGER`、`CONSTANT x = 5`（只能是字面量）、赋值 `←` | 8–9 |
| §3 | `DECLARE A : ARRAY[1:30] OF STRING`、二维 `ARRAY[1:3,1:3]`、不能写 `A[1 TO 30] ← ""` | 10–11 |
| §4 | `TYPE … ENDTYPE` 记录、枚举、指针、集合，点号访问 | 12–14 |
| §5 | `INPUT` / `OUTPUT`、`/` 结果为 REAL、`DIV` / `MOD`、比较 `=` `<>`、`AND` `OR` `NOT`、`&` 连接、字符串与数值函数（P2 以插页为准） | 15–17 |
| §6 | `IF … THEN … ELSE … ENDIF`、`CASE OF … OTHERWISE … ENDCASE` | 18–19 |
| §7 | `FOR … ← … TO … STEP … NEXT i`、`REPEAT … UNTIL`、`WHILE … ENDWHILE` | 20–21 |
| §8 | `PROCEDURE … ENDPROCEDURE` 用 `CALL` 调用；`FUNCTION … RETURNS … ENDFUNCTION` 只在表达式里调用、不用 `CALL`；`BYVAL` / `BYREF`（默认按值；关键字作用到后面同类参数；函数不按引用传参） | 22–24 |
| §9 | `OPENFILE … FOR READ/WRITE/APPEND`、`READFILE`、`WRITEFILE`、`EOF()`、`CLOSEFILE`；随机文件 `RANDOM`、`SEEK`、`GETRECORD`、`PUTRECORD` | 25–27 |
| §10 | `CLASS`、`PUBLIC` / `PRIVATE`、构造过程 `NEW`、`INHERITS`、`SUPER` | 28 |

**给分**：

1. **按 MS 得分点逐点判断**：学生的写法是否满足该点描述的意思。MS 的代码是示例解，算法不同但满足得分点描述同样给分；MS 列出的替代答案都接受；Max 封顶。得分点编号按该行 `markpoints[].n`，与 MS 印的编号不同时以 task.md / 卡片里的对照为准，对学生说 MS 原文（D37 ②）。
2. **书写细节不合指南、结构与关键字都对**（关键字小写、缩进不齐、少了 `DECLARE`——除非得分点要求声明、`NEXT` 后没重复循环变量等）：**不因此扣得分点**；在「规范提示」里列出，给出指南写法并注明节号。
3. **混入编程语言语法或插页以外的语言函数**（`def`、`print` / `input`、`len()`、`range()`、切片 `s[1:3]`、`elif`、`==`、`+` 连接字符串、`FOR Line IN InputFile`、只靠缩进没有 `ENDIF` / `ENDWHILE`、默认 0 起下标）：关键步骤只用 Python 语法写出时，该点**不给**，记「伪代码规范」，并给出伪代码版本（D2）。拿不准时按不给处理并说明理由——考场上宁严勿宽。考官报告写明考 pseudocode 时 "variations with their studied programming language will be unacceptable"（引用它只为解释为什么严格，不是给分依据）。
4. **指南里没有的关键字或结构**（如 `ELSIF`、`ENDFOR`、`INPUT a, b, c`、用 `=` 赋值、`FOR i = 1 TO 10`）：只有**该题 MS 原文**显示接受（MS 示例就这样写，或列为可接受写法）时才给分；否则按不给处理，记「伪代码规范」，并给指南写法。考官报告说「也拿了分」、考官范答或教材里出现过，都不等于该题 MS 接受（D2、D32）。
5. **语义错误照常不给**：变量未初始化、循环边界错、函数里用 `OUTPUT` 代替 `RETURN`、用 `CALL` 调函数、过程写了 `RETURNS`、文件没打开就读等。
6. **数组与短路**：示范与模板用带上下界的全局数组（D24）；不依赖 `AND` 短路，先查下标 / 指针、再读元素（D25）。学生依赖短路写出的条件，按该题 MS 判分，另在规范提示里说明风险。
7. **AD-06 的文字步骤**（`answer.steps.md`，D38）：不写伪代码语句，一句一步；逐点按 MS（如「Open the file (in read mode and subsequently close)」），并检查循环的终止条件与动作位置（in the loop / after the loop）是否写清。
8. **顺序**：先给得分点表，再给「规范版完整答案」（指南写法 + 注释）。

得分点表格式（示例行取自 s24/22 Q6(a) 的 MS 第 1 点）：

| MP | MS 要求（原文） | 你的写法 | 结果 | 技能标签 |
|:--|:--|:--|:--|:--|
| 1 | Function heading, ending, parameter and return type | `FUNCTION Trim(Name : STRING) RETURNS STRING` … `ENDFUNCTION` | ✓ | （取自该行 `markpoints`） |

**P2 已核实的官方笔误**：`9618_w22_22:1(c)` MS 复述表达式时误印 `Count >= 99`（QP 为 `Count >= 29`）：以 QP 讲，给分按 MS 的答案（D16）。`9618_w25_23:3` QP 与 MS 都把类型名 `PopData` 当变量用：教学用 `ThisPop.<字段>` 并说明笔误，其余按 MS 给分（D17）。`9618_s23_21:8(b)` MP5「… OR when ThisItemNum < NewItemNum」指提前结束的第三个条件：循环含这层判断就给分，写成继续条件 `<` 或结束条件 `>` 均可（D37 ①）。

## 7. 同题 Python 版（P2）与常见不对应

伪代码批完后，学生在 `solution.py` 里写同一算法的 Python，`make try` 测。下面是批改时最常用的对照（完整速查表在 `ladder/design.md` §5，以阶梯卡与指南为准）：

| 伪代码 | Python | 坑 |
|:--|:--|:--|
| `DECLARE A : ARRAY[1:10] OF INTEGER` | `a = [0] * 10`（下标 0–9），或 `[0] * 11` 空出 0 号 | 1 起 vs 0 起；按题目和测试约定 |
| `FOR i ← 1 TO n` … `NEXT i` | `for i in range(1, n + 1):` | `range` 不含终点 |
| `FOR i ← n TO 1 STEP -1` | `for i in range(n, 0, -1):` | 终点要写 0 |
| `REPEAT` … `UNTIL c` | `while True:` … `if c: break` | 至少执行一次 |
| `WHILE c` … `ENDWHILE` | `while c:` | |
| `CASE OF x` … `OTHERWISE` | `if / elif / else`（或 `match`） | |
| `MID(S, x, y)` | `s[x - 1 : x - 1 + y]` | 起点减 1；第二个数是终点不是长度 |
| `LEFT(S, n)`、`RIGHT(S, n)` | `s[:n]`、`s[len(s) - n:]` | `s[-n:]` 在 n = 0 时返回整串 |
| `LENGTH(S)` | `len(s)` | |
| `TO_UPPER(S)`、`TO_LOWER(S)` | `s.upper()`、`s.lower()` | 以当卷插页的函数名为准 |
| `NUM_TO_STR(x)`、`STR_TO_NUM(s)` | `str(x)`、`int(s)` / `float(s)` | |
| `ASC(c)`、`CHR(n)` | `ord(c)`、`chr(n)` | |
| `x DIV y`、`x MOD y`、`x / y` | `x // y`、`x % y`、`x / y` | 负数时 `//` 向负无穷取整 |
| `INT(x)` | `int(x)` | |
| `INT(RAND(6)) + 1` | `random.randint(1, 6)` | `randint` 两端都含 |
| `S1 & S2` | `s1 + s2`；数字先 `str()` | |
| `INPUT X` | `x = input()`；数字 `int(input())` | 忘了转换 |
| `OUTPUT "Total: ", T` | `print("Total: ", t, sep="")` 或 f-string | `print` 默认在值之间加空格，测试比对输出时会挂 |
| `PROCEDURE P(BYREF X : INTEGER)` | 返回新值 `x = p(x)`；或传可变对象；或题目用全局变量时 `global` | Python 不能按引用传整数（few-shots 示例 2） |
| `OPENFILE F FOR READ` + `WHILE NOT EOF(F)` + `READFILE F, Line` | `with open(f) as file:` + `for line in file:` + `line = line.rstrip("\n")` | 行尾换行符 |
| `OPENFILE F FOR WRITE` / `APPEND` + `WRITEFILE F, D` | `open(f, "w")` / `open(f, "a")` + `file.write(d + "\n")` | `"w"` 会清空文件；换行要自己加 |
| `CLOSEFILE F` | `file.close()`，或用 `with` 自动关闭 | |
| `TYPE R … ENDTYPE` | 类：在 `__init__` 里给每个字段赋初值 | |
| 二维数组 `ARRAY[1:3,1:4]` | `[[0] * 4 for _ in range(3)]` | `[[0] * 4] * 3` 三行共用一个列表 |

## 8. 考场伪代码习惯（批改时顺带提醒）

- 先写模块头与结束行、再写声明、再写主体；每个结构写完立刻补 `ENDIF` / `ENDWHILE` / `NEXT i`。
- 关键步骤加 `//` 注释（Learner Guide 的建议，阶梯 §4.1 也要求）。
- 文件题：打开 → 读到 EOF / 写 → 关闭，三步缺一都丢分；`WRITE` 会覆盖、`APPEND` 追加。
- 写完对照题干的规格清单逐条打勾（§4 第 2 步）；时间约每分 1.5 分钟。

## 9. 提示阶梯与读 traceback（P2、P4、阶梯通用）

学生卡住时，由轻到重，够用就停：

0. 问清卡在哪：读不懂题、不会设计、语法、还是报错。各用一个问题定位——读题：“规格清单的第几条你说不出来？”；设计：“循环的一轮处理的是哪一个东西（一个字符 / 一行 / 一个元素）？”；边界：“第一个元素 / 空文件 / 找不到时，你的代码走哪条路？”；语法：“哪一行你觉得不像伪代码？”；报错：“traceback 最后一行说的是什么？”。写出来了但错了的，用 few-shots.md「六种探针」；写不出来的，才往下走提示阶梯。
1. 复述规格；指出哪个测试失败，给出它的输入、期望、实际。
2. 指向模式：对照卡 / 题型卡的哪个模板。
3. 指向出错的那一行或缺的那一步（不写代码）。
4. 给骨架：结构与空行，关键表达式留空。
5. 完整示范：写在回复里，不写进 `attempts/`。

用到第 4 级起，这道题不算独立完成（SKILL.md §6）。

**读 traceback**：先看最后一行的异常类型与信息，再看 `solution.py` 的行号。常见：`IndentationError`（缩进）、`NameError`（拼错名字或没定义）、`TypeError: can only concatenate str`（字符串加数字）、`IndexError`（下标差一）、`FileNotFoundError`（写了绝对路径或文件名拼错）、`ValueError: invalid literal for int()`（把空行或带换行的字符串转成整数）、`UnboundLocalError`（函数里给全局变量赋值却没写 `global`）、`AttributeError: module … has no attribute`（模块名没照抄题目或还没写）。

## 10. P2 的非编程小问

| 设问 | 教法要点 | 批改要点 |
|:--|:--|:--|
| 追踪表（dry run） | 先给空表；逐行执行；每执行一次赋值记一次（值没变也记，如 w23/23 Q5 的 Index = 2），行的分法照该题 MS（D40） | 每格对 MS；循环次数；输出列 |
| 找错 / 改错 | 分清语法错误、逻辑错误、运行时错误；给行号与改正 | 指出的行与改法是否都对 |
| 选择构造 / 说明用途 | 计数循环 vs 前测 vs 后测，各自为什么合适 | 理由是否扣题 |
| 测试数据 | 正常 / 异常 / 边界（extreme / boundary）：值 + 理由 + 期望结果 | 边界值是否真在边界 |
| 结构图 | 模块、参数方向（数据与标志）、选择与循环符号 | 参数名与方向；BOOLEAN 返回值按该题 MS 画 |
| 状态转换图 | 状态、事件、条件、初始状态 | 转换是否完整 |
| 流程图 ↔ 伪代码 | 逐个符号对应 | 判断分支与循环的结构 |
| 抽象、分解、逐步求精 | 用题目情景举例 | 是否扣情景 |
| 用文字描述算法（AD-06） | 一句一步、写清循环与动作位置 | §6 第 7 条 |
| 生命周期、测试方法、维护类型 | waterfall / iterative / RAD；白盒 / 黑盒 / alpha / beta / acceptance / stub / integration；corrective / adaptive / perfective | 术语准确、与情景对应 |
| 栈 / 队列 / 链表的使用（AS 不要求写伪代码） | 画指针图，逐步操作 | 每步后的指针与内容 |
| 写高效伪代码 | 提前退出循环、避免重复计算 | 是否真的减少了操作 |

## 11. 失分技能与针对练习

- 每个丢掉的得分点 → 它的 `skills` → 记录表「失分技能」（SKILL.md §7.5）。
- 同一标签累计两次以上：`rows.py find --skill <标签>` 找别卷的同技能小问做针对练习；回到阶梯对应卡的小节复习；在交接文档「常见错误」里点名。
- 整卷限时与冲刺：见 mock-exam.md。
