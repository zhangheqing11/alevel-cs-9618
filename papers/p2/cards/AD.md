## AD　算法设计与问题求解 {#ch-AD}

<!-- auto:chapter-stats -->

### 核心思想

AD 章考的是**动手写代码之前**的两件事：想清楚问题（计算思维），再把解法写成一种别人能照着做的形式（算法表示）。6 个题型分两块：

1. **计算思维**（AD-01 至 AD-03，考纲 9.1–9.2）：抽象——从情境里只留下这个模块需要的数据和操作；分解与逐步求精——把大问题拆成有名字、有用途的模块，再把每一步细化到能直接写成代码；标识符表——给每个要用的变量起有意义的名字、写说明与类型。这三型是 Q1、Q7(a) 常见的 1–4 分短答，套路固定、几乎不丢分。
2. **算法的三种写法**（AD-04 至 AD-06，考纲 9.2）：同一个算法可以写成**程序流程图**、**伪代码**或**文字步骤**（structured English）。题目要你在三者之间转换：文字 / 伪代码 → 流程图（AD-04）；流程图 → 伪代码（AD-05）；不写伪代码、用编号步骤描述（AD-06）。

整章有一条主线：**无论哪种写法，MS 给分的都是同一串逻辑步骤——初值 → 循环（次数或结束条件）→ 循环里的判断与处理 → 循环后的输出 / 返回。** 画流程图时这串步骤是方框、菱形和回路箭头；写伪代码时是 `←`、`IF`、`WHILE`；写文字步骤时是一句一步的英文。学会把一个算法拆成这几步，三个题型就是同一件事的三种抄法。

### 三种写法对照（同一个算法：找出数组 Data 中最大值）

| 步骤 | 流程图 | 伪代码 | 文字步骤 |
|:--|:--|:--|:--|
| 初值 | 矩形：Set Max to Data[1] | `Max ← Data[1]` | Assign the value of the first element to Max. |
| 循环 | 菱形 Is Index > 200 ? + 回路箭头 | `FOR Index ← 2 TO 200` … `NEXT Index` | Repeat for each element from the second to the last. |
| 判断 | 菱形：Is Data[Index] > Max ?（标 Yes / No） | `IF Data[Index] > Max THEN` | If the value of the current element is greater than Max … |
| 处理 | 矩形：Set Max to Data[Index] | `Max ← Data[Index]` | … then assign this value to Max. |
| 输出 | 平行四边形：OUTPUT Max | `OUTPUT Max` | After the loop, output Max. |

### 题型树
<!-- auto:type-tree -->

### P2-AD-01　抽象：需要的信息与操作　{#P2-AD-01}

<!-- auto:stats P2-AD-01 -->

**考法**　①说明抽象的目的 / 好处（1 分）；②在情境里挑出新模块**需要**的 n 个数据项并逐项说明理由（每项“数据 + 理由”1 分）；③挑出**不需要**的数据项并说明理由；④列出每次要存储的 n 个数据项（常是每两项 1 分）；⑤列出处理这些数据需要的 n 个操作（每个 1 分）；⑥（2021 扩展）勾选哪些信息是必要的。

**识别信号**　abstraction；filter out；Identify (three) items of information that will be required / would not be required；Justify your choice(s)；State (four) items of data that must be stored；Identify two operations that would be required to process the … data；essential。

**解题思路**
1. **先读清新模块要干什么**（发短信、发邮件、处理还书、出租汽车……）。抽象的标准只有一个：这个模块做这件事时用不用得上。
2. **需要的数据项**：从情境给出的数据清单里挑，每一项配一个**指向这个模块动作**的理由——“mobile phone number → to send the text message”。理由不能只写“because it is needed”。
3. **不需要的数据项**：同样从情境清单里挑，理由说明**为什么这个动作用不上它**——“postal address → we are sending an email, not a letter”。
4. **要存储的数据项**（如每次租车）：想“一次交易”由谁、什么、何时、多少构成——顾客、物品、日期 / 时间、时长、费用、状态。
5. **操作**：写对数据做的动作，用动词开头——Input / Search / Create / Update / Cancel / Calculate / Send。题目已给的那一个操作不能再写。
6. **目的 / 好处**：抽象 = 滤掉与任务无关的信息，只留必要的 → 解法更简单、更容易设计和实现。

**得分表述**（引自对应 MS）
- 「Abstraction is used to filter out information / data that is not necessary for the task」⟦9618_w22_21:2(a)⟧
- 「To make the solution easier to design / implement / solve」⟦9618_s24_21:7(a)(i)⟧
- 「Justification: to send the text message」⟦9618_s24_21:7(a)(ii)⟧
- 「Justification: sending an email, not a letter」⟦9618_s23_22:7(a)(ii)⟧
- 「Add a member to a list of those interested in the new class」⟦9618_s24_21:7(a)(iii)⟧
- 「One mark for each TWO data items」⟦9618_w22_21:2(a)⟧

**易错与失分**
- 数据项和理由要**一一对应**才给分：写对了项、理由泛泛（“it is important”）通常整点丢。
- 挑情境里**没有**的数据项：题目给了清单时，从清单里挑；没给清单（如租车）才自己想。
- “需要”和“不需要”看错：一题里常常两问都有，看清 required / not required。
- 操作题写成数据项（“customer name”）或写成模块名而不说动作：操作要用动词。
- “每两项 1 分”的题（⟦9618_w22_21:2(a)⟧）写 4 项才有 2 分，写 3 项只有 1 分。

#### 代表题精讲　⟦9618_s24_21:7(a)(ii)⟧

**在考什么**　健身俱乐部为每位会员存：姓名、家庭住址、邮箱、手机号、出生日期、感兴趣的运动。新模块要给对某项运动感兴趣的会员发个性化短信。Identify three items of information that will be required by the new module. Justify your choices with reference to the given scenario. 3 分 = 3 组“数据项 + 理由”。

**完整作答**
| 需要的数据项 | 理由（扣住“发短信”） |
|:--|:--|
| 手机号 | 短信要发到这个号码 |
| 姓名 | 短信是个性化的，要称呼会员的名字 |
| 感兴趣的运动 | 判断这位会员会不会对新课感兴趣、要不要发给这位会员 |

**与 MS 对齐**　MS 三组：“Item: mobile phone number / Justification: to send the text message”“Item: name / Justification: to personalise the text message”“Item: exercise interest / Justification: to determine whether this member would be interested”；「One mark per item and justification」⟦9618_s24_21:7(a)(ii)⟧。住址、邮箱、出生日期都与“发短信”无关，写了不得分。

**英文作答句**　Item 1: mobile phone number — to send the text message to the member. Item 2: name — to personalise the text message. Item 3: exercise interest — to decide whether this member would be interested in the new class.

**直观**　抽象像出门前收拾背包：只带这趟用得上的东西。发短信这一趟，要的是号码、称呼和“他想不想去”。

**下一道变式**　⟦9618_s23_22:7(a)(ii)⟧　（反过来：挑两项**不需要**的顾客信息并说明理由。）

<!-- auto:drills P2-AD-01 -->

### P2-AD-02　分解与逐步求精　{#P2-AD-02}

<!-- auto:stats P2-AD-02 -->

**考法**　①描述分解（decomposition）是什么（2–3 分）；②描述逐步求精（stepwise refinement）（2 分）；③为情境里的新模块列出 3 个子模块 / 模块，写名称与用途（每个 1 分）；④说出把问题分解的 3 个好处；⑤说明程序为什么分成若干阶段、每阶段产生不同文件有什么好处。

**识别信号**　Decomposition will be used to break the problem down into sub-problems；Identify three program modules / sub-modules … and describe their use；Module 1 … Use …；Describe decomposition / stepwise refinement；Describe three benefits of this approach；split into a number of stages。

**解题思路**
1. **定义题**按 MS 的两段式写：做什么 + 为了什么。
   - 分解：把一个问题拆成子问题 → 每个子问题更容易理解和解决 → 最后每个子问题成为一个模块（过程 / 函数）。
   - 逐步求精：把算法的每一步逐层细化、增加细节 → 直到每一步都能直接写成一行代码。
2. **列模块题**：每个模块写成“动词 + 名词()”的名字，用途写一句“这个模块对什么数据做什么”，**扣住情境**。三个模块要覆盖新模块流程的不同阶段（找人 → 取联系方式 → 生成消息 → 发送）。
3. **好处题**：更易理解 / 解决；更易编程、测试、维护（可以单独测试）；可以分给不同程序员 / 团队并行完成；模块可复用。
4. **分阶段的理由**：程序更易设计、实现、测试、调试；每阶段一个文件 → 能检查每一阶段是否按预期工作。

**得分表述**（引自对应 MS）
- 「Breaking down a problem into sub problems」⟦9618_s25_21:1(c)⟧
- 「until steps can be directly translated into lines of code」⟦9618_s25_22:2(a)⟧
- 「One mark for name and use」⟦9618_s24_22:7(a)⟧
- 「Use: Gets the mobile phone number of a member」⟦9618_s24_22:7(a)⟧
- 「Smaller problems are easier to program / test / maintain」⟦9618_s22_22:3(b)⟧
- 「Easier to check that each stage works as expected」⟦9618_s24_22:8(a)⟧

**易错与失分**
- 模块用途写得与名称一样（“SendMessage — sends message”）勉强可以，但最好写清对象：sends a text message **to a member on the waiting list**。
- 三个模块写成同一件事的不同说法（GetPhone、FindPhone）只算一个。
- 把“分解”和“抽象”写混：分解是**拆问题**，抽象是**删信息**。
- 逐步求精只写“break into smaller steps”丢后一分：要补“until each step can be programmed directly”。
- 好处题写“程序更快、更安全”：MS 没有这些点。

#### 代表题精讲　⟦9618_s24_22:7(a)⟧

**在考什么**　健身俱乐部的课满了就建候补名单；系统发现某课有空位时，新模块要给候补名单上的每位会员发短信。Decomposition will be used to break the new module into sub-modules. Identify three sub-modules that could be used in the design and describe their use. 3 分 = 3 个“名称 + 用途”。

**完整作答**
| 子模块 | 用途 |
|:--|:--|
| `IdentifyMember()` | 找出候补名单上、对这门课表示过兴趣的会员 |
| `GetMemberPhoneNumber()` | 取得这位会员的手机号 |
| `SendMessage()` | 给候补名单上的会员发送空位通知短信 |

**与 MS 对齐**　MS 列了四个例子（IdentifyMember、GetMemberPhoneNumber、CreateMessage、SendMessage），「One mark for name and use」⟦9618_s24_22:7(a)⟧，Max 3。任选三个、名称与用途配对就满分；也可以写 CreateMessage()——Generates a text message to a member。

**英文作答句**　Sub-module 1: IdentifyMember() — identifies a club member on the waiting list for the given class. Sub-module 2: GetMemberPhoneNumber() — gets the mobile phone number of that member. Sub-module 3: SendMessage() — sends the text message to the member on the waiting list.

**直观**　分解像把“办一场聚会”拆成“列名单 → 查电话 → 写邀请 → 发出去”，每一件都能交给一个人单独完成。

**下一道变式**　⟦9618_s25_22:2(a)⟧　（换成定义：描述 stepwise refinement，两段式各 1 分。）

<!-- auto:drills P2-AD-02 -->

### P2-AD-03　标识符命名与标识符表　{#P2-AD-03}

<!-- auto:stats P2-AD-03 -->

**考法**　①补全标识符表：按“示例值 + 说明”写出有意义的变量名和数据类型（每行 1 分，名称与类型都对）；②指出表中哪个变量名不好并说明原因；③说明这些名字为什么不合适、会造成什么问题；④说明用什么方式记录变量（标识符表）及要记录的信息；⑤标识符表除了名字还应包含哪两项信息。

**识别信号**　identifier table；Complete the identifier table by adding meaningful variable names；Example value / Explanation / Variable name / Data type；not an example of good practice；State why these variable names are not suitable；State a suitable way of documenting the variables。

**解题思路**
1. **起名**：用说明里的关键名词拼成 CamelCase：“The name of the customer” → `CustomerName`；“The number of items in the order” → `NumItems`；“whether this is a new customer” → `NewCustomer` / `IsNewCustomer`。不用空格、不用缩写到看不懂、不用 `Temp`、`X`、`A1`。
2. **定类型**看示例值：带引号的文字 → STRING（单个字符 → CHAR）；整数个数 → INTEGER；有小数的钱、平均数 → REAL；TRUE / FALSE → BOOLEAN；`dd/mm/yyyy` 形式的日期 → DATE（DT-01 的规则）。
3. **坏名字的原因**：名字不能反映变量的用途 → 程序更难理解、调试、维护。
4. **记录变量的方式**：标识符表（identifier table）；表里记：名字、数据类型、用途说明、示例值 / 初值、数组元素个数或字符串长度、作用域（局部 / 全局）。

**得分表述**（引自对应 MS）
- 「One mark for each row with appropriate variable name and data type」⟦9618_w23_22:1(a)⟧
- 「The names do not reflect / indicate the purpose of the variable」⟦9618_s24_21:1(c)(i)⟧
- 「They make the program more difficult to understand / debug / maintain」⟦9618_s24_21:1(c)(ii)⟧
- 「Identifier table」⟦9618_s24_22:1(c)⟧
- 「The data type of the identifier」⟦9618_s22_22:1(c)⟧
- 「The scope of the variable (local or global)」⟦9618_s22_22:1(c)⟧

**易错与失分**
- 一行里名字对、类型错（或相反）这一行就 0 分：两样都要对。
- 名字里有空格（`Customer Name`）或用了关键字（`Date`、`String`）：不是合法标识符。
- 钱写 INTEGER（15.75 有小数）、日期写 STRING（示例值 20/02/2025 没有引号是 DATE）。
- “标识符表还应包含什么”时又写“名字”：题干已经说了名字，要写**其他**信息。

#### 代表题精讲　⟦9618_w23_22:1(a)⟧

**在考什么**　汽车配件店的顾客订单程序。Complete the identifier table by adding meaningful variable names and appropriate data types. 4 行，每行“名字 + 类型”1 分。

**完整作答**
| Example value | Explanation | Variable name | Data type |
|:--|:--|:--|:--|
| "Mr Khan" | The name of the customer | `CustomerName` | STRING |
| 3 | The number of items in the order | `NumItems` | INTEGER |
| TRUE | To indicate whether this is a new customer | `NewCustomer` | BOOLEAN |
| 15.75 | The deposit paid by the customer | `Deposit` | REAL |

**与 MS 对齐**　MS 答案正是 CustomerName / STRING、NumItems / INTEGER、NewCustomer / BOOLEAN、Deposit / REAL；「One mark for each row with appropriate variable name and data type」⟦9618_w23_22:1(a)⟧——别的有意义的名字（`ItemCount`、`IsNewCustomer`、`DepositPaid`）同样给分。

**英文作答句**　（本题答案即上表。）

**直观**　变量名是贴在盒子上的标签：别人不打开盒子，光看标签就该知道里面装的是什么。

**下一道变式**　⟦9618_s24_22:1(c)⟧　（换成文档：说出记录变量的方式，并给一项要记录的信息。）

<!-- auto:drills P2-AD-03 -->

### P2-AD-04　画或补全程序流程图　{#P2-AD-04}

<!-- auto:stats P2-AD-04 -->

**考法**　①按编号步骤或要点描述画完整流程图（给了 START / END 两个框）；②补全只画了一部分的流程图；③按标号（A–G）把流程图框内文字填进表格。算法内容常是：遍历一维数组计数 / 找最小值、输入一串数到哨兵值为止、输入并存进数组、三数取最大并求平均、调用一个函数并统计返回 TRUE 的次数。5–6 分。

**识别信号**　Draw a program flowchart to represent the algorithm；Complete the program flowchart；START … END；Variable declarations are not required；Complete the table by writing the text that should replace each of the labels。

**解题思路**
1. **先把算法写成 4–6 行伪代码草稿**（写在草稿处），再“翻译”成框，这样不会漏初值或画错回路。
2. **符号**：起止用圆角框（START / END）；赋值、计算、调用过程用矩形；`INPUT` / `OUTPUT` 用平行四边形；判断用菱形，**两个出口都要标 Yes / No**；所有框用箭头连起来，不留悬空的框。
3. **初值放在循环外**：计数器、累加器、下标、最小值在第一个判断菱形之前设好。
4. **画循环**：计数循环 = 初值框 → 判断菱形（Is Index > 30 ?）→ 循环体 → `Set Index to Index + 1` → 箭头回到判断菱形；条件循环同理，判断条件写结束条件。
5. **输出位置**：要输出最终结果的，放在循环出口那一侧；每个元素都要输出的，放在循环体里。
6. **框内文字**可以写 `Set Count to Count + 1`、`Count ← Count + 1` 或 `INPUT Num`，都给分；条件写成问句 `Is Num = 99.9 ?`。

**伪代码模板**（先写草稿，再逐行画成框）

```pseudocode
// draft for an array-processing flowchart: each line becomes one box
Count ← 0                          // rectangle, before the loop
Index ← 1                          // rectangle, before the loop
WHILE Index <= 30                  // diamond: Is Index > 30 ?  Yes -> exit
   IF Data[Index] <> "" THEN       // diamond with Yes / No labels
      OUTPUT Data[Index]           // parallelogram
      Count ← Count + 1            // rectangle
   ENDIF
   Index ← Index + 1               // rectangle, then arrow back to the first diamond
ENDWHILE
OUTPUT "Total output: ", Count     // parallelogram on the exit path, then END
```

**得分表述**（引自对应 MS）
- 「Initialise Min to first value in Data and MinIndex to 1」⟦9618_w23_23:2(a)⟧
- 「Loop through exactly 30 elements in the array」⟦9618_w25_21:2⟧
- 「Test for termination value (99.9) and correct ending」⟦9618_w25_22:2⟧
- 「Test for Count = 10 (10th time A > B) – MUST include Yes / No labels」⟦9618_s24_21:2(a)⟧
- 「Output of Ans and average in output symbol / parallelogram」⟦9618_s24_22:2(a)⟧

**得分点地图**（核验语料 12 道已拆分的流程图题；“题数”= 有这类得分点的题数）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 输出结果（循环后输出一次 / 条件满足时输出），放在平行四边形里 | 10 | `output-format` |
| 计数器、累加器、下标、最小值在循环前赋初值 | 9 | `initialise-variables` |
| 循环次数恰好（30 个元素、100 次、到 20 个存满为止） | 8 | `loop-bounds` |
| 循环里计数 / 累加 / 下标加 1 | 8 | `accumulator` |
| 判断条件写对（比较方向、`>` 与 `>=`） | 5 | `relational-ops` |
| 菱形标 Yes / No、输出用平行四边形 | 4 | `flowchart-draw` |
| 循环里输入 | 4 | `input-prompt` |
| 用下标访问数组元素 | 4 | `array-index` |
| 遇到哨兵值（0、99.9）结束 | 3 | `sentinel-loop` |

几乎每次都有的是前四项：**初值、循环次数、循环里更新、循环后输出**。画完逐项打勾。

**易错与失分**
- 菱形只画一个出口，或两个出口没标 Yes / No：MS 明写 MUST include Yes / No labels。
- 初值画进了循环里：每轮都被清零，计数和累加都错。
- 循环少一次或多一次：“输出最小值的下标”时，Min 已取 Data[1]，再比较 29 个；若从 1 开始比较 30 个也给分，但不能只到 29。
- 哨兵值被存进数组或加进总数：判断哨兵要在存储 / 累加**之前**。
- 求平均用 DIV：「Reject use of DIV」⟦9618_s24_22:2(a)⟧，用 `/`。
- 回路箭头指向初值框之前：等于每轮重新初始化。

#### 代表题精讲　⟦9618_w23_23:2(a)⟧

**在考什么**　Data 是 30 个互不相同整数的一维数组。An algorithm will output the index of the element with the smallest value. Draw a program flowchart to represent the algorithm. 给了 START 和 END，5 分。

**完整作答**（自己画时每个框照下图；`< >` 是菱形，`/ /` 是平行四边形，`[ ]` 是矩形）

```text
            START
              |
   [ Set Min to Data[1] ]
   [ Set MinIndex to 1  ]
   [ Set Index to 2     ]
              |
              v
   < Is Index > 30 ? > ----Yes----> / OUTPUT MinIndex / ---> END
              | No
              v
   < Is Data[Index] < Min ? > ----No-----+
              | Yes                      |
              v                          |
   [ Set Min to Data[Index] ]            |
   [ Set MinIndex to Index  ]            |
              |                          |
              v                          |
   [ Set Index to Index + 1 ] <----------+
              |
              +----> (arrow back to "Is Index > 30 ?")
```

**与 MS 对齐**
| MP | MS 要求（原文） | 图中对应 |
|:--|:--|:--|
| 1 | Initialise Min to first value in Data and MinIndex to 1 | 前两个矩形 |
| 2 | Loop through 29 more values (or 30 values in total) | Index 从 2 到 30，菱形 Is Index > 30 ? 加回路 |
| 3 | Compare element from Data[] with Min | 菱形 Is Data[Index] < Min ? |
| 4 | Set new Min AND save MinIndex when element value < Min in a loop | Yes 分支两个矩形，同时更新 Min 和 MinIndex |
| 5 | Output MinIndex | 出口的平行四边形 |

**规范代码**（同一算法的伪代码，供对照）

```pseudocode
Min ← Data[1]
MinIndex ← 1
FOR Index ← 2 TO 30
   IF Data[Index] < Min THEN
      Min ← Data[Index]
      MinIndex ← Index
   ENDIF
NEXT Index
OUTPUT MinIndex
```

**直观**　像在一排 30 个人里找最矮的：先认定第一个人最矮，然后从第二个人起一个个比，遇到更矮的就换人并记住这个人的位置。

**同题 Python 版要点**
- 下标：Python 列表从 0 起，`data[0]` 是伪代码的 `Data[1]`。题目要的是**伪代码意义上的下标**时，输出 `min_index + 1`，或者在 Python 里也让下标从 1 起（`data = [None] + values`）。
- 不要用 `min(data)` 与 `data.index(...)` 代劳：题目考的是比较算法本身。
- 先过阶梯 **L03**（循环）与 **L06 E02**（线性查找）。

```python
min_value = data[0]
min_index = 0
for index in range(1, 30):
    if data[index] < min_value:
        min_value = data[index]
        min_index = index
print(min_index + 1)        # convert to the 1-based index used in the pseudocode
```

**下一道变式**　⟦9618_w25_22:2⟧　（换成条件循环：输入一串实数存进数组，遇到 99.9 或存满 20 个就结束，99.9 不能存。）

<!-- auto:drills P2-AD-04 -->

### P2-AD-05　流程图转伪代码　{#P2-AD-05}

<!-- auto:stats P2-AD-05 -->

**考法**　①给一张流程图（常含函数调用、标志变量、嵌套回路），写出等价的伪代码（5–6 分）；②说出流程图里的循环属于哪种结构（pre-condition / post-condition / count-controlled，1 分）。核验语料出现少，但与 AD-04 互为逆过程，2021 扩展卷也考过同型。

**识别信号**　Write the equivalent pseudocode for the algorithm represented by the flowchart；Write pseudocode for the algorithm；Give the name of the iterative construct in the flowchart；流程图里有 Set Flag to GetStat()、Is Port = 4 ? 这类框。

**解题思路**
1. **先找回路**：每一条指回上方的箭头就是一个循环。回路里的菱形在循环体**之前** → 前测循环 `WHILE`；在循环体**之后** → 后测循环 `REPEAT … UNTIL`；有“设初值—判断—加 1”三件套 → 计数循环 `FOR`。
2. **定循环条件的方向**：菱形里写的是“退出”条件（Is Flag = TRUE ? Yes → END）。`WHILE` 写**继续**条件（取反：`WHILE Flag <> TRUE`）；`UNTIL` 写**退出**条件（`UNTIL Flag = TRUE`）。
3. **数清计数循环的次数**：Set Port to 1 → Is Port = 4 ? → 循环体只在 Port = 1、2、3 时执行 → `FOR Port ← 1 TO 3`。
4. **翻译每个框**：`Set X to Y` → `X ← Y`；`Set Flag to GetStat()` 是函数调用并赋值；`CALL Reset(Port)` 是过程调用；平行四边形 → `INPUT` / `OUTPUT`；非回路的菱形 → `IF … THEN … ELSE … ENDIF`。
5. **注意回路里有没有重复赋值**：前测循环在循环前和循环体末尾都要更新条件变量（Flag ← GetStat() 写两次）。

**伪代码模板**

```pseudocode
// outer decision before the body  ->  pre-condition loop
Flag ← GetStat()
WHILE Flag <> TRUE                // flowchart asks "Is Flag = TRUE ?"; WHILE needs the opposite
   // counter box + "Is Port = 4 ?" + increment box  ->  count-controlled loop
   FOR Port ← 1 TO 3
      CALL Reset(Port)
   NEXT Port
   Flag ← GetStat()               // update the condition variable inside the loop
ENDWHILE

// decision after the body  ->  post-condition loop
REPEAT
   CALL ReBoot()
   Count ← Count + 1
UNTIL Count > 5                   // UNTIL takes the exit condition as drawn
```

**得分表述**（引自对应 MS）
- 「(Outer) conditional loop testing Flag」⟦9618_s24_22:2(b)⟧
- 「Correct assignment of Flag from GetStat() in a loop」⟦9618_s24_22:2(b)⟧
- 「Pre-condition (loop) / count-controlled (loop)」⟦9618_w22_22:4(b)⟧
- 「WHILE ... ENDWHILE // REPEAT ... UNTIL loop」⟦9618_w21_21:2(b)⟧
- 「Final test of Flag AND call to Alert(27) not in a loop」⟦9618_w21_21:2(b)⟧

**得分点地图**（AD-05 的 3 道不同的已拆分题：s24/22、w22/22 与 2021 扩展 w21/21）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 正确的循环结构（WHILE / REPEAT / FOR）对应流程图回路 | 3 | `flowchart-to-pseudocode`、`pre-condition-loop` |
| 函数调用并把返回值赋给变量 / 调用过程，且在循环里 | 3 | `procedure-call` |
| 循环次数或循环条件正确（含两个条件用 AND 连接） | 3 | `loop-bounds`、`logic-ops` |
| 循环前的初值 | 2 | `initialise-variables` |
| 回路之外的判断写成 IF … ENDIF，放在循环后 | 2 | `nested-if` |

**易错与失分**
- 把 WHILE 的条件照抄菱形（`WHILE Flag = TRUE`）：方向反了，循环一次都不执行。
- 前测循环只在循环前读一次 Flag，循环里不再更新：死循环。
- 计数循环写成 `FOR Port ← 1 TO 4`：Port = 4 时流程图已经离开回路。
- 用 `CALL` 调函数（`CALL GetStat()`），或把过程的结果当返回值用。
- 漏掉 `ENDWHILE` / `NEXT Port`，只靠缩进：按 D2 不给结构分。

#### 代表题精讲　⟦9618_s24_22:2(b)⟧

**在考什么**　流程图：START → Set Flag to GetStat() → 菱形 Is Flag = TRUE ?（Yes → END）→ No → Set Port to 1 → 菱形 Is Port = 4 ?（Yes → 回到 Set Flag to GetStat()）→ No → CALL Reset(Port) → Set Port to Port + 1 → 回到 Is Port = 4 ?。Write pseudocode for the algorithm. 5 分。讲解时请对照原卷 QP p.6（看两条回路箭头各指回哪里）。

**完整作答**

```pseudocode
Flag ← GetStat()
WHILE Flag <> TRUE
   FOR Port ← 1 TO 3
      CALL Reset(Port)
   NEXT Port
   Flag ← GetStat()
ENDWHILE
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 |
|:--|:--|:--|
| 1 | (Outer) conditional loop testing Flag | `WHILE Flag <> TRUE … ENDWHILE` |
| 2 | Correct assignment of Flag from GetStat() in a loop | 循环体末尾的 `Flag ← GetStat()` |
| 3 | (Inner) loop checking / counting port // Check if Port is different to 4 | `FOR Port ← … NEXT Port` |
| 4 | … loop for 3 iterations | `1 TO 3` |
| 5 | a call to Reset()in a loop | `CALL Reset(Port)` 在内层循环里 |

MS 另给了 REPEAT 版（`REPEAT Flag ← GetStat() IF Flag <> TRUE THEN … ENDIF UNTIL Flag = TRUE`），同样满分。

**直观**　外层：“状态不好就继续修”；内层：“把 1、2、3 号端口各重置一遍”。修完一轮再查一次状态。

**同题 Python 版要点**
- `WHILE Flag <> TRUE` ↔ `while not flag:`（`flag` 是布尔值时不必写 `== True`）。
- `FOR Port ← 1 TO 3` ↔ `for port in range(1, 4):`——`range` 不含终点，所以写 4。
- 过程调用不写 CALL：`reset(port)`。先过阶梯 **L03**（循环互译）、**L04 E04**（流程图）。

```python
flag = get_stat()
while not flag:
    for port in range(1, 4):
        reset(port)
    flag = get_stat()
```

**下一道变式**　⟦9618_w22_22:4(a)⟧　（流程图里有数组元素与 IF…ELSE，循环从 Index = 4 到 6；讲解时请对照原卷 QP p.8 的流程图，p.9 为作答要求。）

<!-- auto:drills P2-AD-05 -->

### P2-AD-06　用文字步骤描述算法　{#P2-AD-06}

<!-- auto:stats P2-AD-06 -->

**考法**　①不写伪代码，描述算法要做的步骤（Do not include pseudocode statements，4–7 分）；②补全已给出一部分的编号步骤（Step 1 : open the file … in …）；③用 n 步表达一个算法（Express … as five steps / using four steps）；④说明怎样用某个数组完成某件事（2 分）。内容覆盖全卷：数组找最大值、读文件到数组、文件复制、链表遍历、栈与队列互倒、输入到哨兵值。

**识别信号**　Describe the algorithm (that would be required)；Do not include pseudocode statements in your answer；Describe the steps that the algorithm should perform；Express an algorithm for … as five steps；Complete the steps / Complete the following numbered steps；Outline, using stepwise refinement, the five steps。

**解题思路**
1. **先在草稿处写出伪代码**，再把每一行“念”成一句英文。这是最不容易漏步的办法——但交上去的答案里不能出现伪代码语句。
2. **一步一句，一句一个动作**，顺序与伪代码一致：初值 → 打开文件 → 循环（说清次数或结束条件）→ 循环里读 / 取元素 → 判断 → 处理 → 循环后关闭文件、输出或返回。
3. **说清位置**：in the loop、after the loop、before the loop；循环的结束条件写完整（until the end of the file is reached / until the value 0 is input / 200 times）。
4. **用题目给的名字**：数组名、文件名、变量名照抄（Data、Sales.txt、Max）；可以说“the loop counter”“the array index”。
5. **补全步骤题**：每个空填一个具体的东西（文件名、模式、变量名、条件），不要填“the file”“the data”这样的空话。
6. **按该题计分清单覆盖逻辑步骤**：得分点数、作答步骤数可以大于分值，按 MS 的 Max 封顶；题干指定几步时按指定格式作答。本卡代表题列 7 点、Max 5，不能把 5 分当成只能写 5 步。

**步骤模板**（代替伪代码模板；英文句型，按题目替换名字）

```text
1  Declare / initialise <Count / Total / Index> to <0 / 1>.
2  Open the file <Name.txt> in READ / WRITE / APPEND mode.
3  Repeat the following steps <n times / for each element of <Array> /
   until the end of the file is reached / until <value> is input>:
4     Read the next line from the file // input the next value //
      use the loop counter as the index to access the current element of <Array>.
5     If <condition on the current value> then <add it to Total / increment Count /
      assign it to Max / write it to the file / output it>.
6  After the loop, close the file and output / return <the result>.
```

**得分表述**（引自对应 MS）
- 「Declare a variable / an integer Max」⟦9618_w22_21:3⟧
- 「Use the loop counter as the array index」⟦9618_w22_21:3⟧
- 「After the loop, Output Max」⟦9618_w22_21:3⟧
- 「Repeat (the next three steps) until the end of file is reached」⟦9618_s24_23:2(a)⟧
- 「Open the file in append mode (and subsequently close) before loop」⟦9618_w25_23:2(a)⟧
- 「Check if number greater than 29 and less than 71」⟦9618_w23_21:2(a)⟧

**得分点地图**（核验语料 21 道已拆分的文字步骤题）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 判断条件（大于某值、在范围内、等于查找值） | 11 | `relational-ops` |
| 循环后（或条件满足时）输出 / 返回结果 | 11 | `output-format` |
| 计数器、累加器、下标赋初值 | 9 | `initialise-variables` |
| 循环里计数 / 累加 / 下标加 1 | 8 | `accumulator` |
| 以正确模式打开文件、读一行 | 7 | `file-open-read` |
| 循环后关闭文件 | 7 | `file-close` |
| 重复到文件尾 | 7 | `loop-to-eof` |
| 循环次数或范围（200 次、从头到尾） | 6 | `loop-bounds` |
| 用下标访问数组元素 | 5 | `array-index` |

**易错与失分**
- 答案里写了伪代码语句（`Max ← Data[1]`、`FOR i ← 1 TO 200`）：题目明令禁止，按语句写有不给分的风险；写成英文句子。
- 只写“loop through the array”不说次数或范围：循环次数那一分常常丢。
- 输出写在循环里（每轮输出一次）：要的是 after the loop 输出一次。
- 找最大值时把 Max 初值设成 0：数组可能全是负数；MS 要的是「Assign value of first / any element to Max」⟦9618_w22_21:3⟧。
- 文件题漏了关闭，或关闭写在循环里。
- 写哨兵值算法时把哨兵值也累加进去。

#### 代表题精讲　⟦9618_w22_21:3⟧

**在考什么**　一维整数数组 Data 有 200 个元素，值各不相同。An algorithm is required to search for the largest value and output it. Describe the steps that the algorithm should perform. Do not include pseudocode statements in your answer. 5 分，MS 列 7 点。

**完整作答**
1. Declare an integer variable Max.
2. Assign the value of the first element of Data to Max.
3. Set up a loop to repeat 200 times, from the start to the end of the array.
4. Use the loop counter as the array index to access the current element.
5. If the value of the current element is greater than Max …
6. … then assign this value to Max.
7. After the loop, output Max.

**与 MS 对齐**　七步依次对应 MS 的 1–7 点：「Declare a variable / an integer Max」⟦9618_w22_21:3⟧ → “Assign value of first / any element to Max” → “Set up a loop to repeat 200 times / from start to end of array” → 「Use the loop counter as the array index」⟦9618_w22_21:3⟧ → “If value of current element is greater than Max...” → “...then assign value to Max” → 「After the loop, Output Max」⟦9618_w22_21:3⟧。Max 5：写满 7 步有两步的余量。

**英文作答句**　（本题答案即上面的七步。）

**直观**　这就是 AD 章首“三种写法对照”表的最右一列：把伪代码的每一行念成一句话。

**同题 Python 版要点**
- 同题 Python 就是 L06 的线性扫描：`max_value = data[0]`，`for index in range(1, 200):`，循环后 `print(max_value)`。
- 不要用 `max(data)`：题目考的是扫描算法。先过阶梯 **L06 E02**。

**下一道变式**　⟦9618_s24_23:2(a)⟧　（换成文件：把文本文件逐行读进一维数组，描述 5 步；记得“打开并在之后关闭”合成一分。）

<!-- auto:drills P2-AD-06 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| AD-01 vs AD-02 | 挑选需要 / 不需要的数据项、列对数据的操作 → AD-01；拆成有名字的模块并写用途 → AD-02 | items of information / operations 还是 modules / sub-modules |
| 抽象 vs 分解 | 抽象 = 删掉与任务无关的信息；分解 = 把问题拆成子问题 | filter out 还是 break down |
| 分解 vs 逐步求精 | 分解拆的是问题（成模块）；逐步求精细化的是算法步骤（直到能写成代码） | sub-problems 还是 more detail / lines of code |
| AD-02 vs PG-06 | 为情境拆模块、分阶段的理由 → AD-02；为什么用子程序、过程与函数的区别 → PG-06 | Decomposition will be used 还是 subroutine / procedure / function |
| AD-03 vs DT-01 | 表里要填变量名（和类型）、问怎样记录变量 → AD-03；只填数据类型 → DT-01 | Variable name 一栏是不是空的 |
| AD-04 vs AD-05 | 文字 / 伪代码 → 画流程图 → AD-04；给流程图 → 写伪代码 → AD-05 | Draw / Complete the flowchart 还是 Write pseudocode |
| AD-04 vs SD-03 / SD-04 | 程序流程图（框、菱形、回路）→ AD-04；结构图（模块与参数）→ SD-03；状态转换图 → SD-04 | program flowchart 还是 structure chart / state-transition diagram |
| AD-06 vs 写代码题型 | 要求文字描述、不写伪代码 → AD-06；要求写伪代码 → 按数据结构定（DT-05、DT-09 …） | Do not include pseudocode statements |
| AD-06 vs SD-12 | 描述一个新算法的步骤 → AD-06；描述对已有程序要做的修改 → SD-12 | describe the algorithm 还是 describe the changes |
| WHILE vs REPEAT | 判断在循环体前、可能一次都不执行 → WHILE（写继续条件）；判断在后、至少执行一次 → REPEAT（UNTIL 写退出条件） | 流程图菱形在回路的哪一头 |
