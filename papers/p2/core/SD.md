## SD　软件开发：概念表、图示约定与伪代码 ↔ Python 对照 {#core-SD}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。SD 章以概念短答为主，这里先给三层术语表，再给结构图、状态转换图的画法约定，以及错误、干跑、测试在伪代码与 Python 里的对应。

### 1. 开发生命周期（SD-01、SD-02）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Program development life cycle（好处） | 「Easier to manage/plan/cost // Clear deliverables produced at (end of) each stage」⟦9618_w22_23:1(b)(i)⟧ | 把开发分成分析、设计、编码、测试、维护几个阶段，每个阶段有明确的产出 | 盖房子的工序表 | P2-SD-01 |
| Analysis | 「The problem definition」⟦9618_w22_23:1(b)(ii)⟧（分析阶段产出的文档） | 调查现有系统、访谈客户、可行性研究，写出问题定义与需求说明 | 先问业主要什么 | P2-SD-01 |
| Design | 「Algorithms / flowcharts / pseudocode」⟦9618_w21_22:2(b)(ii)⟧（设计阶段的决定） | 定数据结构、算法、模块结构、界面、测试计划 | 画图纸 | P2-SD-01 |
| Coding | 「An algorithm is implemented in a programming language. Coding」⟦9618_w24_21:5(a)⟧ | 用编程语言实现设计好的算法 | 施工 | P2-SD-01 |
| Testing | 「The walkthrough method is used. Testing」⟦9618_w24_21:5(a)⟧ | 用干跑、走查、各类测试找出错误 | 验收检查 | P2-SD-01、P2-SD-09 |
| Maintenance | 「The program is modified to run on new hardware. Maintenance」⟦9618_w24_21:5(a)⟧ | 交付使用后对程序的修改 | 住进去后的修补改造 | P2-SD-01、P2-SD-11 |
| Waterfall（向下箭头） | 「Downward arrows: result from one stage is input / passed to the next」⟦9618_s22_23:8(b)⟧ | 各阶段依次进行，上一阶段的结果是下一阶段的输入 | 水往低处流 | P2-SD-02 |
| Waterfall（向上箭头） | 「Upward arrows: more work is required at a previous stage to complete the current stage」⟦9618_s22_23:8(b)⟧ | 发现问题时回到前一阶段补做 | 回头补图纸 | P2-SD-02 |
| Waterfall（缺点） | 「No working software until late in the life cycle so slower to market than competitors」⟦9618_s23_21:5(a)(i)⟧ | 到后期才有可用软件，难以应对需求变化 | 盖完才能看 | P2-SD-02 |
| Iterative | 「Provides a working model / prototype at an early stage for the principal to approve / review」⟦9618_w21_22:2(b)(i)⟧ | 先做简单版本，再一轮轮完整走一遍生命周期，逐步增加功能 | 先搭毛坯再逐层装修 | P2-SD-02 |
| RAD（原则） | 「Small incremental releases are made, each adding functionality」⟦9618_w22_23:1(c)(i)⟧ | 模块并行开发、做原型、少做详细规划、客户全程参与 | 样板间边看边改 | P2-SD-02 |
| RAD（客户参与） | 「Client involved during (all stages) of development」⟦9618_w22_23:1(c)(i)⟧ | 客户在各阶段都参与评审与反馈 | 业主天天来工地 | P2-SD-02 |

### 2. 结构图：符号 ↔ 伪代码（SD-03、PG-07）

| 结构图上的东西 | 含义 | 伪代码里对应 |
|:--|:--|:--|
| 矩形框 | 一个模块 | 一个 `PROCEDURE` 或 `FUNCTION` |
| 上下两框之间的直线 | 上面的模块调用下面的模块 | `CALL Sub()`，或在表达式里调用函数 |
| 同一调用者下从左到右的几个框 | 按顺序调用 | 几句调用依次写 |
| 调用者下沿的菱形 | 选择：调用其中一个，运行时决定 | `IF … THEN CALL A() ELSE CALL B() ENDIF` 或 CASE |
| 跨过几条连线的弧形箭头 | 重复：反复依次调用这几个模块 | 把这几句调用放进一个循环 |
| 向下的箭头（空心圆箭尾） | 传入的数据参数 | 模块头里的参数 `Name : STRING` |
| 向下的箭头（实心圆箭尾） | 传入的标志（BOOLEAN） | `Flag : BOOLEAN` |
| 向上的箭头 | 返回值（函数）或传回的值 | `RETURNS 类型`，或 BYREF 参数 |
| 同一参数下去又回来（双头箭头） | 按引用传递 | `BYREF P : 类型` |

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Structure chart（用途） | 「module relationships / hierarchy / selection / repetition // how a problem is broken down」⟦9618_s22_23:3(a)⟧ | 用框和连线表示模块的层次、调用关系、选择与重复，以及模块间传递的参数 | 公司组织图加快递单 | P2-SD-03 |
| Structure chart（参数） | 「the parameters that are passed between the sub-tasks / modules」⟦9618_s22_23:3(a)⟧ | 图上还要标出模块之间传递的参数与返回值 | 快递单上写着寄了什么 | P2-SD-03 |
| Diamond（selection） | 「Means that Update calls (one of) either Sub-A, Sub-B or Sub-C」⟦9618_s24_21:7(b)(i)⟧ | 菱形：调用者在几个模块中选一个调用 | 岔路口 | P2-SD-03 |
| Curved arrow（iteration） | 「Means that Sync repeatedly calls Reset and (then) Enable」⟦9618_w24_21:7(b)⟧ | 弧形箭头：调用者反复依次调用这几个模块 | 环岛 | P2-SD-03 |

### 3. 状态转换图（SD-04）

| 图上的东西 | 含义 |
|:--|:--|
| 圆圈 S1、S2 … | 一个状态 |
| 黑点 + 箭头（START） | 初始状态 |
| 两个圆圈之间的箭头 | 转换：在箭尾的状态下发生某事件，进入箭头指向的状态 |
| 箭头上的 `A1 \| X1` | 事件（输入）A1 引起这次转换，同时产生输出 X1；没有输出只写事件 |
| 从圆圈出发又回到自己的箭头 | 状态不变的转换（自环），可能有输出 |
| 双圈（或标明的终止状态） | 终止状态 |

| 术语 | 英文定义 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| State-transition diagram | A diagram that shows the states of a system, the events that cause a change from one state to another and any outputs produced.（非 MS 原句） | 表示系统的各个状态、引起状态改变的事件以及产生的输出的图 | 地铁线路图 | P2-SD-04 |

状态转换表写成伪代码：**当前状态用 CASE 分，表里的每一行是一个 IF**。

```pseudocode
CASE OF State
   "S1" : IF Event = "A1" THEN
             OUTPUT "X1"
             State ← "S2"
          ENDIF
   "S2" : IF Event = "A3" THEN
             State ← "S1"
          ELSE
             IF Event = "A2" THEN
                OUTPUT "X4"
                State ← "S5"
             ENDIF
          ENDIF
ENDCASE
```

```python
# one dictionary entry per row of the table: (state, event) -> (output, next state)
table = {("S1", "A1"): ("X1", "S2"), ("S2", "A3"): ("", "S1"), ("S2", "A2"): ("X4", "S5")}
output, state = table[(state, event)]
if output != "":
    print(output)
```

### 4. 错误类型与调试（SD-05、SD-06）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| No syntax errors | 「The program obeys the rules / grammar of the programming language used」⟦9618_w21_21:1(a)(i)⟧ | 语法错误 = 违反了语言的规则 / 语法，编译器会报出 | 错别字、病句 | P2-SD-05 |
| Logic error | 「An error in the algorithm / design of the solution」⟦9618_w21_21:1(a)(ii)⟧ | 算法本身错了，程序能运行但结果不对；编译器发现不了 | 句子通顺但意思错了 | P2-SD-05、P2-SD-06 |
| Run-time error | 「The program performs an illegal instruction / invalid operation」⟦9618_w21_21:1(a)(ii)⟧ | 运行时执行了非法操作（除以 0、越界），或死循环导致停止响应 | 开车开进了死胡同 | P2-SD-05 |
| Breakpoint | 「Breakpoint」⟦9618_s22_22:1(a)⟧（让程序停在某一句检查变量的位置） | 程序运行到这一句就暂停 | 在可疑路段停车 | P2-SD-05 |
| Single stepping | 「Explanation of single stepping – execute ‘line by line’ / statements」⟦9618_w24_22:1(b)⟧ | 一次只执行一条语句 | 一步一步慢慢走 | P2-SD-05 |
| Watch window | 「Explanation of watch window – displaying the value of variable(s)」⟦9618_w24_22:1(b)⟧ | 运行中显示变量当前值的窗口（也叫 report window） | 仪表盘 | P2-SD-05 |

**同一种错误在伪代码与 Python 里的样子**

| 错误 | 伪代码例子 | Python 里的表现 | 类型 |
|:--|:--|:--|:--|
| 结构不配对 | WHILE 循环用 `NEXT Index` 结尾 | 缩进错误 `IndentationError` / `SyntaxError`，程序不能运行 | Syntax |
| 赋值号当比较号 | `IF EMPTY ← "" THEN` | `if empty = "":` 报 `SyntaxError` | Syntax |
| 类型不对 | `"Done" + LENGTH(S)`、`"Total " & Count` | `"Done" + len(s)` 报 `TypeError`（运行到这一句才报） | Syntax（伪代码）/ 运行时（Python） |
| 比较方向反了 | 找最小值用 `IF Num > Min` | 能运行，结果是最大值 | Logic |
| 循环次数差一 | `FOR I ← 1 TO 9`（应为 10） | `range(1, 10)` 少一次 | Logic |
| 除以 0 | `INT(100 / Number)`，Number 为 0 | `ZeroDivisionError` | Run-time |
| 下标越界 | 数组下界 1，却访问 `Data[0]` | 列表 `data[200]` 报 `IndexError`；`data[-1]` 不报错但取到最后一个 | Run-time |
| 非数字串转数字 | `STR_TO_NUM("abc")` | `int("abc")` 报 `ValueError` | Run-time |
| 死循环 | 条件循环的结束条件永远不满足 | 程序无响应 | Run-time |

### 5. 干跑与追踪表（SD-07）

| 步骤 | 做法 |
|:--|:--|
| 1 | 先填第一行：参数、计数器、数组的初值 |
| 2 | 执行一句赋值，就在该变量列的**新一行**写新值；值不变不写 |
| 3 | 每轮先判断循环条件；WHILE 在前判断，REPEAT 在后判断 |
| 4 | 下标由变量算出时，先在草稿上算出这一轮的下标 |
| 5 | 数组元素改过之后，后面读到的是新值 |
| 6 | 循环结束后的语句、RETURN、OUTPUT 也要记下 |

在阶梯里可以用 Python 验证自己的追踪表：把伪代码逐行译成 Python，在每个赋值后 `print` 出变量（阶梯各级的 `trace` 型练习就是这样设计的，如 L03 E01、L05 E02、L06 E01）。

### 6. 测试（SD-09、SD-10）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Walkthrough / dry run | 「The program is checked by creating a trace table / going through the program a line at a time」⟦9618_w22_23:5(d)⟧ | 不运行程序，逐行走一遍、填追踪表，看变量值与路径是否符合预期 | 当一次电脑 | P2-SD-07、P2-SD-09 |
| White-box testing | 「so that all paths through the program can be tested」⟦9618_s23_23:5(a)⟧ | 看着代码设计测试数据，走遍程序里的每条路径 | 打开机器盖子检查每条线路 | P2-SD-09、P2-SD-10 |
| Black-box testing | Testing in which the tester compares the actual output with the expected output for given inputs, without looking at the code.（非 MS 原句） | 不看代码，只比较给定输入的实际输出与预期输出 | 只按按钮看灯亮不亮 | P2-SD-09 |
| Integration testing | 「Modules that have already been tested individually」⟦9618_s22_22:5(c)⟧ + 「are combined into a single (sub) program which is then tested as a whole」⟦9618_s22_22:5(c)⟧ | 把各自测过的模块组合起来作为整体测试 | 零件都合格，再装成整机试 | P2-SD-09 |
| Stub testing | 「A dummy/simple module is written to replace the module that does not work properly」⟦9618_s23_21:8(c)(ii)⟧ | 用只返回已知值或输出一句话的简单模块代替未完成 / 有错的模块，让其他部分能继续测试 | 排练时的替身演员 | P2-SD-09 |
| Alpha testing | Testing carried out in-house by the developers before the program is released.（非 MS 原句） | 开发方内部在发布前做的测试 | 公司内部试吃 | P2-SD-09 |
| Beta testing | 「Testing carried out by a small group of (potential) users」⟦9618_w22_22:1(b)⟧ | 一小群（潜在）用户在真实环境中使用并反馈问题 | 请几位熟客试吃 | P2-SD-09 |
| Acceptance testing | 「Acceptance testing」⟦9618_w25_22:5(b)⟧（由客户进行的最后测试阶段） | 客户在交付前确认程序满足需求 | 业主验收签字 | P2-SD-09 |
| Normal data | 「23 Normal Data Data is accepted」⟦9618_w21_21:4(a)⟧ | 合法范围内的典型值，应被接受 | 正常身高的人过门 | P2-SD-10 |
| Boundary / extreme data | 「0 Boundary Data Data is accepted」⟦9618_w21_21:4(a)⟧ | 恰好在合法范围边上的值（应被接受）；边界外一步的值应被拒绝 | 刚好踩线 | P2-SD-10 |
| Abnormal data | 「>= 41 Abnormal Data Data is rejected」⟦9618_w21_21:4(a)⟧ | 范围外或类型不对的值，应被拒绝 | 明显不该进门的 | P2-SD-10 |
| Validity check | 「Value for month is between 1 and 12 (inclusive)」⟦9618_s23_23:2(b)(i)⟧ | 对参数或输入做的范围、长度、类型、一致性检查 | 门口验票 | P2-SD-10 |

**范围检查：伪代码 ↔ Python ↔ 测试数据**（24 到 37 含两端）

```pseudocode
FUNCTION InRange(Value : INTEGER) RETURNS BOOLEAN
   IF Value >= 24 AND Value <= 37 THEN
      RETURN TRUE
   ELSE
      RETURN FALSE
   ENDIF
ENDFUNCTION
```

```python
def in_range(value: int) -> bool:
    return 24 <= value <= 37

# normal, both boundaries, just outside both boundaries, far outside
for value, expected in [(30, True), (24, True), (37, True), (23, False), (38, False), (99, False)]:
    assert in_range(value) == expected
```

### 7. 维护（SD-11、SD-12）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Corrective maintenance | 「Type: Corrective Reason: The program does not operate as expected / contains a bug」⟦9618_s22_23:2⟧ | 改正程序里的错误 | 坏了修 | P2-SD-11 |
| Adaptive maintenance | 「Type: Adaptive Reason: To accommodate a change in the requirement / technology / legislation」⟦9618_s22_23:2⟧ | 需求、技术、硬件、库或法规变了，让程序适应 | 搬家换雪地胎 | P2-SD-11 |
| Perfective maintenance | 「Perfective」⟦9618_s23_23:5(b)⟧（程序交付后为提高响应速度而做的修改） | 程序没错，为了更快、更好用、更易维护而改进 | 车没坏，想更省油 | P2-SD-11 |

### 8. 常见失分（SD 章）

| 失分 | 正确做法 | 题型 |
|:--|:--|:--|
| 标识符表、结构图、测试计划归到 Coding / Testing | 它们是 Design 阶段的产出 | P2-SD-01 |
| RAD 的好处不与瀑布比较 | 写瀑布没有的：早有原型、易改需求 | P2-SD-02 |
| 解释菱形 / 弧形箭头不写模块名 | 写出“A 调用 B、C 之一”“A 反复依次调用 B、C” | P2-SD-03 |
| 返回值画成向下箭头；BYREF 只画一个方向 | 返回向上；BYREF 双向 | P2-SD-03 |
| 状态图漏自环、箭头方向反了 | 表里每一行画一条从当前状态指向下一状态的箭头 | P2-SD-04 |
| IDE 题只列术语；说 IDE 能自动改错 | 断点 → 单步 → 监视窗口，每个配一句作用 | P2-SD-05 |
| 只指出错误不写改正 | 哪一句 + 错在哪 + 改成什么 | P2-SD-06 |
| 追踪表用了数组的旧值、漏了最后一句 | 改过的元素用新值；循环后的语句也要填 | P2-SD-07 |
| 只说“哪一句”不说“为什么” | 两部分各给分 | P2-SD-08 |
| 桩测试写成“跳过模块” | 写一个返回已知值或输出消息的替身模块 | P2-SD-09 |
| 测试数据只测一边边界；预期结果写 works | 两端边界及边界外一步都测；写具体结果 | P2-SD-10 |
| 提高速度判成 adaptive | 没错、外部没变、只是要更好 → perfective | P2-SD-11 |
| 改程序题复述旧程序 | 只写改动：头部、数据、循环、处理、返回 | P2-SD-12 |
