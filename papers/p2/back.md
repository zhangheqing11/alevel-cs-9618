## 书末　跨章入口、写代码得分链与命令词 {#back}

前面 4 章按题型拆开讲；真卷里一道大题往往连问好几个题型，写模块的大题又总是按同一条链给分。本部分把它们收拢：①看到一个题目特征或一个情境，知道去哪张卡；②写代码大题从模块头到返回值，每一环拿什么分、怎样丢分；③每个命令词要你做什么。每一条都配了真实例题行，学的时候回到对应题型卡。

### 跨章入口一：按题目特征找题型

先看这一小问**要你产出什么**（填表、画图、写文字、写伪代码），再看里面的关键词。

| 看到 | 去哪张卡 |
|:--|:--|
| 表格里每行打勾：selection / iteration / assignment / input/output / subroutine | P2-PG-01 |
| 表格的 Evaluates to 一栏空着，可能要写 ERROR | P2-PG-02 |
| 表格的表达式里有空，要填插页函数；写一条调用语句；化简一条语句 | P2-PG-03 |
| 表格只要填数据类型 | P2-DT-01 |
| 标识符表：变量名、说明、示例值；变量名为什么不好 | P2-AD-03 |
| abstraction：需要 / 不需要的数据项、对数据的操作 | P2-AD-01 |
| decomposition、stepwise refinement、列出子模块与用途 | P2-AD-02 |
| without using a CASE structure；four separate IF statements | P2-PG-04 |
| more appropriate loop structure；identify the type of loop | P2-PG-05 |
| subroutine / library routine / local and global / passed by reference | P2-PG-06 |
| Write the (pseudocode) module header(s) | P2-PG-07 |
| constants、features that make it easier to understand、not efficient | P2-PG-08 |
| Draw / Complete the program flowchart | P2-AD-04 |
| 给了流程图，Write pseudocode | P2-AD-05 |
| Describe the algorithm … Do not include pseudocode statements；Complete the steps | P2-AD-06 |
| TYPE … ENDTYPE、给记录字段赋值 | P2-DT-02 |
| 写数组声明；维数、元素个数、上下界；未用元素 | P2-DT-03 |
| 为什么用数组 / 记录 / 记录数组 | P2-DT-04 |
| Write pseudocode + 全局一维数组（含并行数组） | P2-DT-05 |
| Write pseudocode + `ARRAY[1:r, 1:c]` | P2-DT-06 |
| Write pseudocode + 记录数组 `Loan[Index].Field` | P2-DT-07 |
| bubble sort | P2-DT-08 |
| Write pseudocode + 只读文件（`EOF`、`READFILE`） | P2-DT-09 |
| Write pseudocode + 写 / 追加 / 复制文件（`WRITEFILE`） | P2-DT-10 |
| 文件的好处、模式、一行里怎样存多项数据 | P2-DT-11 |
| stack / queue / linked list 的特征与选择 | P2-DT-12 |
| 在栈 / 队列 / 链表的图上做操作 | P2-DT-13、P2-DT-14、P2-DT-15 |
| 用数组和指针变量实现栈 / 队列 / 链表 | P2-DT-16 |
| Write pseudocode + 键盘反复输入、到结束值为止、随机数 | P2-PG-09 |
| Write pseudocode + 参数是几个数（阶乘、校验位、时间、直角三角形） | P2-PG-10 |
| Write pseudocode + 参数是字符串（逐字符、子串、分隔符、拼接） | P2-PG-11 |
| SETDATE、DAYINDEX、TODAY、of type DATE | P2-PG-12 |
| life cycle stage、activities、document | P2-SD-01 |
| waterfall、iterative、RAD | P2-SD-02 |
| structure chart、diamond、curved arrow | P2-SD-03 |
| state-transition diagram、Current state \| Input \| Output \| Next state | P2-SD-04 |
| syntax / logic / run-time error、IDE、breakpoint | P2-SD-05 |
| State the error in each case / NO ERROR；Identify the errors and corrections | P2-SD-06 |
| Complete the trace table by dry running | P2-SD-07 |
| never performed、not needed、Explain why the program gives unexpected results、purpose | P2-SD-08 |
| stub、integration、beta、walkthrough、acceptance | P2-SD-09 |
| test plan、normal / abnormal / boundary、test data、checks on parameters | P2-SD-10 |
| corrective / adaptive / perfective | P2-SD-11 |
| The requirements are changed. Describe / Outline the changes | P2-SD-12 |

**写代码大题判型**：一个模块同时用到文件、数组、字符串时，按 MS 里哪种结构拿到 ≥ 2 分来定，优先级从高到低：栈 / 队列 / 链表的数组实现（DT-16）→ 冒泡排序（DT-08）→ 写文件（DT-10）→ 只读文件（DT-09）→ 记录数组（DT-07）→ 二维数组（DT-06）→ 一维数组（DT-05）→ 日期（PG-12）→ 字符串（PG-11）→ 参数数值计算（PG-10）→ 循环输入（PG-09）。例：⟦9618_s24_22:8(c)⟧ 读一个文件、处理每行后写进另一个文件，字符串处理交给已写好的模块，归 DT-10；⟦9618_w25_21:4(a)⟧ 输入一串数并存进数组，归 DT-05（循环输入是副题型 PG-09）。

### 跨章入口二：同一情境常跨哪些章

P2 的后半卷是情境大题：先给一段情境，再连问 3–6 个小问，常从概念问到写代码、再问测试或修改。读完情境先预判会出哪几型，做到一半就不会被突然换章打乱。

| 情境 | 常见的小问顺序 | 跨的题型 | 真题例 |
|:--|:--|:--|:--|
| 一组模块的说明表或结构图 | 哪些是函数 → BYVAL 与 BYREF 的效果 → 画结构图 → 写模块头 → 解释菱形 / 弧形箭头 | PG-06、SD-03、PG-07 | ⟦9618_s24_23:7(a)(i)⟧ 至 ⟦9618_s24_23:7(b)⟧；⟦9618_s25_23:6(a)⟧ 至 ⟦9618_s25_23:6(c)⟧ |
| 老师分阶段处理学生的伪代码项目文件 | 为什么分阶段 → 去行首空格 / 去注释（字符串）→ 逐行处理后写进新文件 | AD-02、PG-11、DT-10 | ⟦9618_s24_22:8(a)⟧ 至 ⟦9618_s24_22:8(c)⟧；⟦9618_s24_21:8(a)⟧ |
| 计算机之间收发消息 | 读消息文件 → 文件模式与格式 → 按位置取字段 → 收发循环 → 消息格式要改 | DT-09、DT-11、PG-11、PG-09、SD-12 | ⟦9618_w23_21:8(a)⟧ 至 ⟦9618_w23_21:8(d)⟧；⟦9618_w23_23:8(c)⟧、⟦9618_w23_23:8(d)⟧ |
| 图书馆借书记录 | 定义记录类型 → 遍历记录数组计数 / 修改 → 加罚款规则后改记录结构 | DT-02、DT-07、SD-12 | ⟦9618_w25_21:8(a)⟧ 至 ⟦9618_w25_21:8(c)⟧ |
| 咖啡店会员积分 | 用日期函数更新积分 → 从客户字符串里取积分 → 把日期串转成 DATE | PG-12、PG-11 | ⟦9618_s25_23:7(a)(i)⟧ 至 ⟦9618_s25_23:7(b)(ii)⟧ |
| 文件的最后三行 | 写读文件代码或文字步骤 → 某几步的目的 → 输出顺序为什么会错 → 需求变了怎样改 | DT-09、AD-06、SD-08、SD-06、SD-12 | ⟦9618_s22_22:4(a)⟧、⟦9618_s22_22:4(b)⟧；⟦9618_w24_21:3(a)⟧ 至 ⟦9618_w24_21:3(c)⟧ |
| 给定一个模块的代码 | 解释初值和条件的作用 → 循环是否合适 → 找错改错 → 运行时停止响应是哪种错 | SD-08、PG-05、SD-06、SD-05 | ⟦9618_w25_21:5(a)(i)⟧ 至 ⟦9618_w25_21:5(b)(ii)⟧；⟦9618_s24_22:5(a)(i)⟧ 至 ⟦9618_s24_22:5(b)⟧ |
| 写一个算法，再测试它 | 写过程 / 函数 → 设计测试数据或测试计划 | PG-09、PG-10、SD-10 | ⟦9618_w23_22:4(a)⟧、⟦9618_w23_22:4(b)⟧；⟦9618_w22_23:6(a)⟧、⟦9618_w22_23:6(b)⟧；⟦9618_w25_21:6(a)⟧、⟦9618_w25_21:6(b)⟧ |
| Q1 开卷：一段程序的变量与语句 | 结构打勾 → 填插页函数 → 标识符表 / 数据类型 → 表达式求值 | PG-01、PG-03、AD-03、DT-01、PG-02 | ⟦9618_s24_22:1(a)⟧ 至 ⟦9618_s24_22:1(c)⟧；⟦9618_w23_22:1(a)⟧ 至 ⟦9618_w23_22:1(c)⟧ |
| 开发一个网站 / 程序的过程 | 数据类型 → 生命周期的好处与文档 → RAD 原则与优缺点 → 适应性维护 | DT-01、SD-01、SD-02、SD-11 | ⟦9618_w22_23:1(a)⟧ 至 ⟦9618_w22_23:1(d)⟧ |
| 用数组实现 ADT | 栈 / 队列 / 链表的状态图 → 特征与选择 → 实现时的声明与代码 | DT-13、DT-14、DT-15、DT-12、DT-16 | ⟦9618_s25_23:2(a)(i)⟧ 至 ⟦9618_s25_23:2(c)⟧；⟦9618_w22_23:4(a)⟧ 至 ⟦9618_w22_23:4(b)(ii)⟧ |

两个提醒：

1. **情境不决定题型，命令决定。** 同一个借书情境，问“定义记录”是 DT-02，问“遍历记录数组”是 DT-07，问“需求变了怎样改”是 SD-12。先看这一小问在问什么，再去对应的卡。
2. **前面小问给的名字，后面照抄。** 记录类型名、字段名、数组名、模块名、文件名都在前面小问或情境里给过，后面写代码时一字不差地用。

### 写代码大题的通用得分链

不论数据在数组、文件、字符串还是键盘输入里，写模块大题的 MS 计分清单几乎都是同一条链。按这条链写，每一环都对上一类得分点；写完再按这条链逐环检查。

```text
模块头 → 声明与初值 → 循环 → 循环里取值与判断 → 处理 → 输出 / 返回 / 关闭文件
```

#### 第 1 环　模块头与结尾

**写法**　`PROCEDURE 名字(参数 : 类型, …)` … `ENDPROCEDURE`；或 `FUNCTION 名字(参数 : 类型, …) RETURNS 类型` … `ENDFUNCTION`。要把值带回调用者的过程参数加 BYREF。模块名、参数名照抄题目。

**MS 原文例**
- 「Function heading and ending, including parameters and return type」⟦9618_s23_21:4⟧
- 「Procedure heading and ending」⟦9618_w23_22:4(a)⟧
- 「...and use of BYREF for the three extracted values」⟦9618_w22_23:5(a)(i)⟧

**丢分**　漏了 ENDFUNCTION；参数不写类型；`RETURNS` 后写变量名；该用函数却写成过程（或反过来）。技能标签 `module-header`、`byval-byref`。详见 PG-07。

#### 第 2 环　声明与初值

**写法**　模块里用到的局部变量一个一个 `DECLARE`，类型写对（循环变量也要声明）；计数器、累加器设 0，累乘器设 1，结果字符串设 `""`，标志设 FALSE / TRUE，“没找到”设 −1。**全部写在循环之前**。全局数组不在模块里重新声明（决策 D24）。

**MS 原文例**
- 「Declaration of local variables used including loop counter」⟦9618_s23_21:4⟧
- 「Declare and initialise Count, Total and NumString」⟦9618_s22_22:6⟧
- 「Declaration and initialisation (to 1) of local Integer Value for result」⟦9618_s22_23:6(a)⟧

**丢分**　初值写进了循环里（每轮清零）；漏了某一个计数器的初值（MS 常写 must have been initialised）；用关键字或插页函数名作变量名（`String`、`Year`）。技能标签 `declare-variables`、`initialise-variables`、`data-types`。

#### 第 3 环　循环

**写法**　次数已知 → `FOR … TO … NEXT 变量`（遍历数组到上界、字符串到 `LENGTH`）；到文件尾 → `WHILE NOT EOF(文件名)`；到结束值 → 先读一次再 `WHILE 值 <> 结束值`；找到就停（efficient）→ `WHILE` + 标志变量；至少一次 → `REPEAT … UNTIL`。循环条件不依赖 AND 短路（决策 D25）。

**MS 原文例**
- 「Loop for length of OldString」⟦9618_s23_21:4⟧
- 「Conditional loop while ThisNum <> 99」⟦9618_w23_22:4(a)⟧
- 「Conditional loop until EOF()」⟦9618_w22_21:8(a)⟧
- 「Loop for 100 iterations」⟦9618_w24_23:2(a)⟧

**丢分**　次数差一（`0 TO 199`、`1 TO LENGTH(S) - 1`）；WHILE 条件里的变量还没有值；要求 efficient 却用 FOR 扫到底；`ENDFOR`、`FOR Line IN File` 之类非指南写法（D2）。技能标签 `loop-bounds`、`count-loop`、`pre-condition-loop`、`post-condition-loop`、`loop-to-eof`、`sentinel-loop`、`char-loop`。

#### 第 4 环　循环里取值与判断

**写法**　每轮先取出“当前这一个”：`Data[Index]`、`Grid[Row, Col]`、`Loan[Index].OnLoan`、`READFILE F, Line`、`MID(S, Index, 1)`、`INPUT X`；再判断：等于参数、在范围内、是不是空、是不是字母、奇偶。

**MS 原文例**
- 「Extract char and test in a loop」⟦9618_s23_21:4⟧
- 「Read a line in a loop」⟦9618_w22_21:8(a)⟧
- 「Check ThisNum is odd or even in a loop」⟦9618_w23_22:4(a)⟧

**丢分**　把字符串当数组（`S[Index]`）、把文件当数组（`File[Index]`）；二维数组写成 `Grid[Row][Col]`、记录写成 `Loan.Field[Index]`；比较方向或等号写错（`>` 与 `>=`）；题目没要求却转换大小写。技能标签 `array-index`、`array-2d`、`array-of-records`、`file-open-read`、`string-functions`、`char-compare`、`relational-ops`、`logic-ops`。

#### 第 5 环　处理

**写法**　满足条件时做事：计数 `Count ← Count + 1`、累加 `Total ← Total + X`、记最大最小、拼接 `NewS ← NewS & Ch`、设标志、写文件 `WRITEFILE`、调用题目给的模块并用它的返回值、交换（冒泡）、移动指针（ADT）。

**MS 原文例**
- 「Use of concatenate to build NewString replace char if necessary, in a loop」⟦9618_s23_21:4⟧
- 「Increment appropriate count in a loop, both counts must have been initialised before loop」⟦9618_w23_22:4(a)⟧
- 「Multiply Try by Num in a loop」⟦9618_w22_22:6(a)⟧

**丢分**　处理写在了循环外；`&` 连接数值、`+` 连接字符串；写文件前没有把数值转成字符串；题目指定要用的模块没有调用（或用 CALL 调函数）。技能标签 `accumulator`、`max-min`、`string-concat`、`flag-variable`、`file-write`、`procedure-call`、`bubble-sort`。

#### 第 6 环　输出 / 返回 / 关闭文件

**写法**　循环**之后**：输出结果并配说明文字（`OUTPUT "Total: ", Total`），或 `RETURN` 结果；两种情况（找到 / 没找到、TRUE / FALSE）都要有输出或返回；打开过的文件在返回之前 `CLOSEFILE`。

**MS 原文例**
- 「Return NewString after reasonable attempt」⟦9618_s23_21:4⟧
- 「After the loop output COdd and CEven with a suitable message following a reasonable attempt at counting」⟦9618_w23_22:4(a)⟧
- 「Return INTEGER value correctly in both cases: ThisNum < 0 and >= 0」⟦9618_s22_23:6(a)⟧
- 「OPEN in READ mode and CLOSE」⟦9618_w22_21:8(a)⟧

**丢分**　输出写在循环里（每轮输出一次）；只在一种情况下返回；用 OUTPUT 代替 RETURN；`CLOSEFILE` 写在 RETURN 之后（永远执行不到）或干脆漏写。“following a reasonable attempt”表示主体算法写得像样，这一分才给。技能标签 `output-format`、`return-value`、`boolean-return`、`file-close`。

#### 同一条链在不同数据里的样子

| 数据在哪里 | 第 3 环：循环头 | 第 4 环：取出当前这一个 | 第 6 环：结束时 | 题型 |
|:--|:--|:--|:--|:--|
| 一维数组 | `FOR Index ← 1 TO 500` | `Data[Index]` | 返回 / 输出 | DT-05 |
| 二维数组 | `FOR Row ← 1 TO 1000`（全表再套 `FOR Col`） | `Grid[Row, Col]` | 返回 / 输出 | DT-06 |
| 记录数组 | `FOR Index ← 1 TO 7000` | `Loan[Index].OnLoan` | 返回 / 输出 | DT-07 |
| 读文件 | `WHILE NOT EOF(FileName)` | `READFILE FileName, Line` | `CLOSEFILE FileName` 后返回 | DT-09 |
| 写 / 复制文件 | 读文件的循环 | 读一行，处理后 `WRITEFILE OutFile, Line` | 两个文件都 `CLOSEFILE` | DT-10 |
| 字符串 | `FOR Index ← 1 TO LENGTH(S)` | `MID(S, Index, 1)` | 返回新串 / 计数 | PG-11 |
| 键盘输入 | `FOR Count ← 1 TO 100`，或先读再 `WHILE X <> 99` | `INPUT X`（先提示） | 输出 | PG-09 |
| 日期 | `REPEAT … UNTIL Found = 3` | `SETDATE(Day, Month, Year)`、`DAYINDEX(…)` | 返回 | PG-12 |
| 链表 | `WHILE Current <> 0` | `List[Current].Data`，再 `Current ← List[Current].Pointer` | 返回 / 输出 | DT-16 |

#### 开写之前先落下的骨架

拿到一道写模块题，先花 30 秒把下面的骨架写在答题区，再往空里填算法。骨架本身就覆盖了模块头、声明、初值、循环、返回这几分。

```pseudocode
FUNCTION ModuleName(Param : STRING) RETURNS INTEGER   // 1 header: names and types from the question
   DECLARE Index : INTEGER                            // 2 every local variable, one DECLARE each
   DECLARE Count : INTEGER
   Count ← 0                                          // 2 initial values before the loop
   FOR Index ← 1 TO LENGTH(Param)                     // 3 the loop that fits the data
      IF MID(Param, Index, 1) = ' ' THEN              // 4 take the current item and test it
         Count ← Count + 1                            // 5 process it
      ENDIF
   NEXT Index
   RETURN Count                                       // 6 after the loop: return / output / close
ENDFUNCTION
```

写完按六环自查：每一环有没有、位置对不对（循环前 / 循环里 / 循环后）、有没有混进 Python 写法（`==`、`!=`、`+=`、`elif`、`len()`、切片）。

### P2 常见命令词的作答要求

| 命令词 | 要你做什么 | 怎样拿分 | 例 |
|:--|:--|:--|:--|
| Write pseudocode (for the module / algorithm) | 写出完整的伪代码 | 按六环得分链写；只用指南写法与插页函数；题目说 declare all variables 就全部声明 | ⟦9618_s23_21:4⟧ |
| Complete the pseudocode | 在给出的框架里补全 | 照抄已给的名字和结构，补齐缺的那几环 | ⟦9618_w24_21:2⟧ |
| Write the (pseudocode) statement / header | 只写一行 | 一行里每个部分都对：关键字、名字、参数、类型 | ⟦9618_s24_21:7(b)(ii)⟧ |
| Describe the algorithm / steps（Do not include pseudocode） | 用英文句子一步一步说 | 一步一句，说清循环的范围和位置（in a loop、after the loop），不写伪代码语句 | ⟦9618_w22_21:3⟧ |
| Draw / Complete（流程图、结构图、状态转换图） | 画图或补图 | 符号用对；每个判断两个出口标 Yes / No；每个参数、每条转换都画上 | ⟦9618_s24_23:7(b)⟧ |
| Complete the table | 填表 | 一行或一格一分；一行里几栏都要对 | ⟦9618_w24_21:5(a)⟧ |
| Evaluate | 算出表达式的值 | 写出结果的类型（字符串带引号）；有错写 ERROR | ⟦9618_w23_22:1(b)⟧ |
| Complete the trace table / dry run | 逐行执行并记录 | 第一行初值、每一轮一组、循环后的语句都要有 | ⟦9618_w23_23:5⟧ |
| Identify / State / Give | 说出一个名称或一句事实 | 用 MS 的术语原词；点数等于分值 | ⟦9618_s23_22:8(c)⟧ |
| Explain / Describe | 说明原因或过程 | 写出“是什么 + 为什么 / 怎样起作用”，点名题目里的模块、变量 | ⟦9618_s24_23:7(a)(ii)⟧ |
| Justify / Suggest and justify | 选一个并给理由 | 选择本身常只 1 分，理由扣情境 | ⟦9618_w25_21:5(b)(ii)⟧ |
| Outline / Describe the changes | 概述要做的修改 | 只写改动，一处一句：头部、数据、循环、处理、返回 | ⟦9618_w24_21:3(c)⟧ |
| State the error / Identify the errors | 找出错误 | 哪一句 + 错在哪；要求改正时写出改成什么 | ⟦9618_s24_22:5(a)(i)⟧ |

最后一条通用提醒：**写代码题的分在得分点上，不在“程序能不能跑”上。** 一段几乎写对、只差一个 ENDIF 的代码，可能只丢一分；一段思路巧妙但漏了模块头、初值和返回的代码，可能丢掉一半。先把六环的“骨架分”拿稳，再去挣中间的算法分。
