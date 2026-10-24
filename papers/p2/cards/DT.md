## DT　数据类型与数据结构 {#ch-DT}

<!-- auto:chapter-stats -->

### 核心思想

DT 是 P2 分值最多的一章：Q6–Q8 的“写一个模块”大题，大多数在这里。16 个题型分四块：

1. **数据怎么装**（DT-01 至 DT-04）：选数据类型；用 `TYPE … ENDTYPE` 定义记录；声明一维 / 二维数组、记录数组；说明为什么用数组、记录或记录数组。都是 1–4 分的短答，规则固定。
2. **数组处理模块**（DT-05 至 DT-08）：遍历一维数组（含并行数组）、二维数组、记录数组，做计数、求和、最值、查找、找空位写入；以及冒泡排序。6–8 分的大题。
3. **文本文件**（DT-09 至 DT-11）：读文件逐行处理（DT-09）；写、追加、复制、过滤文件（DT-10）；文件的用途、模式与一行里怎样存多项数据（DT-11）。
4. **抽象数据类型 ADT**（DT-12 至 DT-16）：栈、队列、链表的特征（DT-12）；在状态图上做入栈出栈、入队出队、插入删除结点（DT-13 至 DT-15）；用数组 + 指针变量实现它们，写 Push / AddTo 等代码（DT-16）。

整章有一条主线：**数据结构决定循环怎么写。** 一维数组 → 一个下标从 1 到 n；二维数组 → 行、列两个下标（嵌套循环或固定一列）；记录数组 → 下标加点号 `Loan[Index].OnLoan`；文本文件 → 没有下标，只有“读到文件尾”；栈、队列、链表 → 下标由指针变量给出。写模块时先认出是哪一种，模板就定了；MS 的得分点也总是同一串：**模块头 → 声明与初值 → 正确的循环 → 循环里的访问与判断 → 处理 → 循环后的输出 / 返回 / 关闭文件。**

### 本章伪代码速查（2027–29 指南写法）

```pseudocode
// declarations
DECLARE Count : INTEGER
CONSTANT MaxItems = 500
DECLARE Names : ARRAY[1:30] OF STRING
DECLARE Grid : ARRAY[1:5, 1:5] OF CHAR

// record type and array of records
TYPE Loan
   DECLARE StudentID : STRING
   DECLARE BookID : STRING
   DECLARE OnLoan : BOOLEAN
ENDTYPE
DECLARE Loans : ARRAY[1:7000] OF Loan
Loans[1].OnLoan ← TRUE

// text files: after opening, the file is still referred to by its name
OPENFILE "Stock.txt" FOR READ          // or FOR WRITE / FOR APPEND
WHILE NOT EOF("Stock.txt")
   READFILE "Stock.txt", ThisLine
ENDWHILE
WRITEFILE "New.txt", ThisLine
CLOSEFILE "Stock.txt"
```

### 题型树
<!-- auto:type-tree -->

### P2-DT-01　选择数据类型　{#P2-DT-01}

<!-- auto:stats P2-DT-01 -->

**考法**　①按变量用途给出最合适的数据类型（表格，每行 1 分）；②按示例值给类型；③按一条合法的赋值语句，给左边变量的类型（要看右边表达式的结果类型）；④给出一个表达式结果的类型（`RIGHT(…)`、`NOT Status`、`IS_NUM(…)`）；⑤举例说明什么时候用 BOOLEAN。

**识别信号**　Complete the table by writing the most appropriate data type；Give the appropriate data types for the following variables；valid pseudocode assignment statements … data type；Example data value；the data type of the evaluated expression。

**解题思路**
1. 只有六种答案：`INTEGER`、`REAL`、`CHAR`、`STRING`、`BOOLEAN`、`DATE`。写全大写的指南名称（MS 也接受 Integer、Real 等写法），不写 `int`、`float`、`str`。
2. **按用途**：个数、序号、下标 → INTEGER；钱、平均数、温度、带小数的测量 → REAL；一个字母 → CHAR；名字、邮箱、编号（含字母或前导零）→ STRING；只有两种状态（开 / 关、是否已读）→ BOOLEAN；日期 → DATE。
3. **按示例值**：带双引号 → STRING（即使里面是日期 `"18/04/2021"`）；带单引号的一个字符 → CHAR；`TRUE` / `FALSE` → BOOLEAN；不带引号的 `27/10/2023` → DATE；有小数点 → REAL；整数 → INTEGER。
4. **按表达式**：`/` 的结果永远是 REAL（`INT(ItemCost) / 3` 也是）；`DIV`、`MOD`、`LENGTH()`、`INT()` → INTEGER；`AND`、`OR`、`NOT`、比较、`IS_NUM()` → BOOLEAN；`&` 连接、`RIGHT()`、`MID()`、`NUM_TO_STR()` → STRING（取 1 个字符时 CHAR 也接受）；`Total * 2` 看 Total 的类型。

**得分表述**（引自对应 MS）
- 「MyVar1 ← Total1 / Total2 REAL」⟦9618_w23_23:1(a)⟧
- 「C ← INT(ItemCost) / 3 REAL」⟦9618_s24_21:1(a)⟧
- 「Received "18/04/2021" STRING」⟦9618_w24_23:1(b)⟧
- 「IS_NUM(Check) BOOLEAN」⟦9618_s25_22:1(c)⟧
- 「Store the first letter of the customer's first name CHAR」⟦9618_w22_23:1(a)⟧
- 「When the variable can take only one of two possible values」⟦9618_s22_23:1(b)(ii)⟧

**易错与失分**
- 钱写 INTEGER：15.75、12.67 有小数，是 REAL。
- 电话号码、编号写 INTEGER：有前导零或字母时只能是 STRING。
- 加了引号的日期写 DATE：引号说明它是字符串。
- 写 `FLOAT`、`int`、`Text`、`Number`：不是指南类型名。
- 除法结果写 INTEGER：`/` 一律 REAL，即使两边都是整数。

#### 代表题精讲　⟦9618_w23_23:1(a)⟧

**在考什么**　The following table shows four valid pseudocode assignment statements. Complete the table by giving the data type that should be used to declare the variable underlined in each assignment statement. 4 行各 1 分。

**完整作答**
| 赋值语句 | 类型 | 理由 |
|:--|:--|:--|
| `MyVar1 ← Total1 / Total2` | REAL | `/` 的结果总是实数 |
| `MyVar2 ← 27/10/2023` | DATE | 不带引号的日期字面量 |
| `MyVar3 ← "Sum1 / Sum2"` | STRING | 双引号里的是文字，不是除法 |
| `MyVar4 ← Result1 AND Result2` | BOOLEAN | `AND` 的结果是 TRUE / FALSE |

**与 MS 对齐**　MS 四行正是 REAL、DATE、STRING、BOOLEAN：「MyVar1 ← Total1 / Total2 REAL」⟦9618_w23_23:1(a)⟧。陷阱在第 3 行：引号里的“/”不做运算。

**英文作答句**　（本题答案即上表。）

**直观**　看右边“出来的是什么东西”：一个数（带不带小数）、一个日期、一串字、还是一个是 / 否。

**下一道变式**　⟦9618_s25_22:1(c)⟧　（换成表达式本身的类型：`RIGHT(MachineCode, 4)`、`Speed * 2.5`、`NOT Status`、`IS_NUM(Check)`。）

<!-- auto:drills P2-DT-01 -->

### P2-DT-02　记录类型：定义与字段访问　{#P2-DT-02}

<!-- auto:stats P2-DT-02 -->

**考法**　①按字段表写 `TYPE … ENDTYPE` 记录定义（3–4 分）；②补全记录定义；③写一条给记录变量某字段赋值的语句（1 分）；④写一个检查记录数组元素某字段是否在范围内的条件子句（3 分）；⑤指出记录定义里的错误（字段类型不对）。

**识别信号**　Write pseudocode to declare the record structure for type …；Complete the pseudocode to create a record structure with the identifier …；Write pseudocode to define MyType；assign the value … to the … field of …；State the error in the record declaration；Field / Example value / Comment 表。

**解题思路**
1. **格式**：第一行 `TYPE <类型名>`，每个字段一行 `DECLARE <字段名> : <类型>`，最后 `ENDTYPE`。类型名、字段名照题目抄（大小写、下划线都照抄）。
2. **每个字段的类型**按 DT-01 的规则从示例值和说明定：`123478 a numeric value used as an array index` → INTEGER；`'B'` → CHAR；`13.5` → REAL；`TRUE` → BOOLEAN。
3. **字段访问**：记录变量 `LineData.Cost ← 12.99`；记录数组元素 `Batch[ThisIndex].Weight`。
4. **范围检查子句**：`IF Batch[ThisIndex].Weight >= Min AND Batch[ThisIndex].Weight <= Max THEN`——两个比较都要写完整的左边。

**伪代码模板**

```pseudocode
TYPE Component                     // type name exactly as given
   DECLARE Item_Num : INTEGER      // one DECLARE per field
   DECLARE Reject : BOOLEAN
   DECLARE Stage : CHAR
   DECLARE Limit_1 : REAL
ENDTYPE

DECLARE ThisItem : Component       // a single record variable
ThisItem.Stage ← 'B'               // field access with the dot
DECLARE Item : ARRAY[1:2000] OF Component
Item[1].Reject ← FALSE             // element of an array of records
```

**得分表述**（引自对应 MS）
- 「One mark for TYPE and ENDTYPE statements」⟦9618_s24_22:3(a)(i)⟧
- 「One mark for Limit fields as REAL」⟦9618_s24_22:3(a)(i)⟧
- 「LineData.Cost ← 12.99」⟦9618_w22_23:5(b)(i)⟧
- 「Reference to Batch[ThisIndex].Weight」⟦9618_s24_23:3(a)(i)⟧
- 「ErrCode should be an INTEGER」⟦9618_w22_22:7(c)(i)⟧

**得分点地图**（核验语料写 TYPE 的题：3 道已拆分，另有 3 道按字段计分未拆，含 s26 两道）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| `TYPE <名>` 与 `ENDTYPE` 一分（题目已给 TYPE 行时只看 ENDTYPE） | 5 | `record-type` |
| 按 MS 指定字段组计分，一组可含多个字段，组内字段名与类型都要正确 | 6 | `record-type`、`data-types` |

例如 ⟦9618_s22_23:5(a)(i)⟧ 的 MS 把 EmployeeNumber、Name、Department 三个字段合为 1 分，并非固定每 1–2 个字段一分。

**易错与失分**
- 写成 `TYPE Component = …`、`RECORD … END`、`ENDRECORD`：结构分丢。
- 字段写成赋值 `Item_Num ← 0` 或漏了 `DECLARE`。
- 数字编号（用作下标）写成 STRING；单个字母写成 STRING（MS 常接受，但 CHAR 最稳）。
- 字段访问写成 `Batch.Weight[ThisIndex]`：下标跟在数组名后面，点号在下标后面。
- 范围条件写成 `Weight >= Min AND <= Max`：右半边缺了左操作数。

#### 代表题精讲　⟦9618_s24_22:3(a)(i)⟧

**在考什么**　工厂为每个零件存一条 Component 记录，字段表：Item_Num 123478（a numeric value used as an array index）、Reject FALSE、Stage 'B'（a letter）、Limit_1 13.5、Limit_2 26.4（0 到 100 的任意值）。Write pseudocode to declare the record structure for type Component. 4 分。

**完整作答**

```pseudocode
TYPE Component
   DECLARE Item_Num : INTEGER
   DECLARE Reject : BOOLEAN
   DECLARE Stage : CHAR
   DECLARE Limit_1 : REAL
   DECLARE Limit_2 : REAL
ENDTYPE
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 |
|:--|:--|:--|
| 1 | One mark for TYPE and ENDTYPE statements | 首尾两行 |
| 2 | One mark for Item_Num and Reject fields | INTEGER、BOOLEAN |
| 3 | One mark for Stage field | CHAR |
| 4 | One mark for Limit fields as REAL | 两个 REAL |

**直观**　TYPE 是在设计一张“表格模板”：每个零件都按这张模板填一份，每一栏规定好填什么类型。

**同题 Python 版要点**
- Python 没有 TYPE，用只有属性的类：在 `__init__` 里给每个字段赋一个对应类型的初值；或用 `@dataclass`。
- 记录数组不能写 `[Component()] * 2000`（2000 个引用指向同一个对象），要写 `[Component() for _ in range(2000)]`。
- 先过阶梯 **L08 E01**（记录）。

```python
class Component:
    def __init__(self):
        self.item_num = 0        # INTEGER
        self.reject = False      # BOOLEAN
        self.stage = ""          # CHAR (Python has no separate char type)
        self.limit_1 = 0.0       # REAL
        self.limit_2 = 0.0       # REAL
```

**下一道变式**　⟦9618_w25_21:3(a)(i)⟧　（同型：RentalRecord 的 6 个字段，按两个一组给分。）

<!-- auto:drills P2-DT-02 -->

### P2-DT-03　数组：声明、术语与未用元素　{#P2-DT-03}

<!-- auto:stats P2-DT-03 -->

**考法**　①写一维 / 二维数组的声明（含记录数组），2 分 = 上下界 1 分 + 其余部分 1 分；②回答术语：维数、元素个数、下标变量名、上界 / 下界、下标（index / subscript）；③说明声明数组前还缺什么信息（元素的类型）；④给出标记未用元素的办法，并说明为什么要统一标记。

**识别信号**　Write pseudocode to declare the … array；Give the pseudocode declaration for the array；Complete the pseudocode statement used to declare the global 2D array；the number of dimensions / total number of elements / lower bound / upper bound / index；unused array element；State the one additional piece of information required。

**解题思路**
1. **声明格式**：`DECLARE <名> : ARRAY[<下界>:<上界>] OF <类型>`；二维 `ARRAY[<行下界>:<行上界>, <列下界>:<列上界>]`。元素类型可以是记录类型名（`OF Component`）。
2. **上下界**照题目：题目说 2000 个元素没说起点 → `[1:2000]`（MS 也接受 `[0:1999]`）；题目给了下界上界表 → 照表。
3. **元素个数** = 各维（上界 − 下界 + 1）相乘：`[0:99, 0:9]` → 100 × 10 = 1000。
4. **术语**：dimension（维数）；index / subscript（下标）；lower bound / upper bound（下界 / 上界）。
5. **未用元素**：放一个**不可能出现的值**——空字符串 `""`、负数或 0、超出范围的编号、`999`、很久以前的日期。**为什么要统一**：处理和查找时能认出未用元素；否则元素里可能是旧的或意外的数据。

**得分表述**（引自对应 MS）
- 「DECLARE Rental : ARRAY[1:500] OF RentalRecord」⟦9618_w25_21:3(a)(ii)⟧
- 「1 mark for correct upper and lower bound」⟦9618_s25_22:1(d)(iii)⟧
- 「The data type (of the item to be stored)」⟦9618_w22_23:4(a)⟧
- 「It identifies / references an individual array element」⟦9618_w22_21:1(b)(ii)⟧
- 「So that unused elements may be recognised when processing / searching」⟦9618_s22_23:5(b)(i)⟧
- 「An array can only store data of the same type」⟦9618_s25_22:7(c)(i)⟧

**易错与失分**
- 写成 `ARRAY[1..2000]`、`ARRAY[1 TO 2000]`、`ARRAY(2000)`：用冒号 `:`。
- 二维数组写成 `ARRAY[1:100][1:2]`：两维写在同一对方括号里，用逗号隔开。
- 漏了 `OF <类型>`，或把类型写成 `OF ARRAY`。
- 元素个数算成 99 × 9：上下界都包含，各维要 +1。
- 未用元素用 `NULL`、“nothing”：要给出一个具体的、该类型的不可能值。

#### 代表题精讲　⟦9618_s25_22:1(d)(iii)⟧

**在考什么**　全局数组 Product 存每天的次品数，赋值语句 `Product[x, y] ← 23`；下界与上界表：x 为 0–99，y 为 0–9。Give the pseudocode declaration for the array Product. 2 分。

**完整作答**

```pseudocode
DECLARE Product : ARRAY[0:99, 0:9] OF INTEGER
```

**与 MS 对齐**　「1 mark for correct upper and lower bound」⟦9618_s25_22:1(d)(iii)⟧——`[0:99, 0:9]`；另 1 分给其余部分：`DECLARE Product : ARRAY … OF INTEGER`（次品数是整数）。同一组的前两问：维数 2；元素总数 100 × 10 = 1000。

**英文作答句**　（本题答案即上面的声明。）

**直观**　二维数组是一张 100 行 × 10 列的表格；声明就是先说清“几行几列、每格装什么”。

**下一道变式**　⟦9618_s22_23:5(b)(ii)⟧　（换成未用元素：在员工记录数组里，怎样标记一条未用的记录。）

<!-- auto:drills P2-DT-03 -->

### P2-DT-04　选择数据结构并说明好处　{#P2-DT-04}

<!-- auto:stats P2-DT-04 -->

**考法**　①说出用数组（代替许多单独变量）的好处（2–3 分）；②说出用记录数组的三个好处；③为“一个顾客的多项不同类型数据”选结构（记录）并说明好处；④为所有顾客的数据描述结构（记录数组）；⑤比较两种设计：两个并行数组 vs 一个记录数组、数组查表 vs 多重 IF；⑥结构改变后（类型不同了）说明为什么旧的二维数组不能用、新的怎样设计。

**识别信号**　Explain why it would be good practice to use arrays；State three benefits of using an array of records；Identify a suitable structure for storing the information for one customer；Describe an effective way of storing this data for many customer orders；An alternative design would involve the use of multiple selection statements；single array of the user-defined data type。

**解题思路**
1. **结构怎么选**：一个对象的多项数据、类型不同 → **记录**；很多个同类对象 → **数组**；很多个对象、每个有多项不同类型的数据 → **记录数组**；同类型的表格数据 → 二维数组；两项数据、想用两个数组 → 两个**并行一维数组**，靠同一下标对应。
2. **数组的好处**（任选够分）：一个标识符引用许多值，标识符更少；可以用循环和下标遍历、查找、排序；代码更短、更易写、易读、易测试、易维护；数量变化时容易改程序。
3. **记录的好处**：不同类型的数据放在一个标识符下；同一对象的数据保持在一起。
4. **记录数组 vs 两个并行数组**：数据项之间关联更紧，不会“错位”；代码更简单（点号一起引用）。
5. **数组查表 vs 多重 IF**：代码行更少、更简单；用下标直接取值（如用月份号取当月天数）；数据改了只改数组。

**得分表述**（引自对应 MS）
- 「Allows for iteration / can use a loop to access the records / data items」⟦9618_s24_22:3(b)⟧
- 「Use of index to directly access a record in the array」⟦9618_s24_22:3(b)⟧
- 「Different data types held (for each rental) under a single identifier」⟦9618_w25_21:3(b)⟧
- 「Declare an array of the given composite / record (type)」⟦9618_w23_22:1(c)⟧
- 「values cannot get out of step as with two arrays」⟦9618_w22_22:7(c)(ii)⟧
- 「Fewer lines of code are needed」⟦9618_w24_21:6(a)⟧

**易错与失分**
- 只写“easier”“more efficient”：要说清**怎样**更容易（用循环、用下标、标识符更少）。
- 把三个好处写成同一个意思（easier to write / easier to code）只算一分。
- 要求结构的题只写“array”：多种类型的数据要写 array **of records**，并说出记录类型。
- 把 ADT（栈、队列）或文件当作这里的答案：那是 DT-12、DT-11。

#### 代表题精讲　⟦9618_s24_22:3(b)⟧

**在考什么**　零件数据存在 Component 记录里，所有零件用一个记录数组 Item。State three benefits of using an array of records to store the data for all items. 3 分。

**完整作答**
1. 可以用循环遍历数组，逐条访问每个零件的记录。
2. 可以用下标直接访问某一条记录，并用点号引用字段（如 `Item[1].Stage`）。
3. 代码更简单、重复更少，程序更容易写、理解、测试和维护；记录也更容易查找和排序。

**与 MS 对齐**　三点依次对应 MS 的 1、2、3：「Allows for iteration / can use a loop to access the records / data items」⟦9618_s24_22:3(b)⟧；「Use of index to directly access a record in the array」⟦9618_s24_22:3(b)⟧（MS 还接受以 dot notation 举例）；“Simplifies the code / algorithm // Reduces duplication of code // Program easier to write / understand / maintain / test / debug”。

**英文作答句**　1 It allows iteration: a loop can be used to access each record. 2 An index can be used to directly access a record in the array, for example Item[1].Stage. 3 It simplifies the code and reduces duplication, so the program is easier to write, test and maintain.

**直观**　记录数组像一个文件柜：每个抽屉（下标）放一张同样格式的表格（记录）；要找就按号拉抽屉，要全查就一个个拉过去。

**下一道变式**　⟦9618_w23_22:1(c)⟧　（换成设计题：订单数据类型不同，描述在程序运行时存很多订单的有效方式。）

<!-- auto:drills P2-DT-04 -->

### P2-DT-05　一维数组处理模块　{#P2-DT-05}

<!-- auto:stats P2-DT-05 -->

**考法**　按模块描述写（或补全）遍历全局一维数组的过程 / 函数：①数某值出现几次并与上限比较；②分别累加奇数位、偶数位元素；③找最大 / 最小或其下标；④有序数组里高效查找（找到或越过就停）；⑤找第一个未用元素写入新值；⑥并行数组（ErrCode 与 ErrText）按同一下标读写；⑦输入一串值存进数组；⑧初始化数组全部元素。6–8 分。

**识别信号**　A global 1D array … contains n elements；Write pseudocode for the function / procedure …；corresponding elements / parallel arrays；Unused elements contain the empty string / the value 999；search for the largest value；efficient；All variables used must be declared。

**解题思路**
1. **读模块描述，抄下模块头**：过程还是函数、参数名与类型、返回类型。描述里每个圆点通常就是一两个得分点。
2. **声明局部变量**：下标、计数器、累加器、标志；全局数组**不要**再声明。
3. **选循环**：要看完全部元素（计数、求和、最值）→ `FOR Index ← 1 TO n`；找到就停、遇到未用元素就停、题目写 efficient → 条件循环（WHILE + 标志）。
4. **循环体**：用 `Data[Index]` 访问当前元素；判断；更新计数 / 累加 / 最值 / 标志。
5. **循环后**：比较结果并返回 / 输出——**两种情况都要有**（找到 / 没找到，TRUE / FALSE）。
6. **并行数组**：同一个 Index 同时用于 `ErrCode[Index]` 与 `ErrText[Index]`。

**伪代码模板**

```pseudocode
// A: visit every element (count / total / max / min)
FUNCTION CountMatches(Search : STRING, Limit : INTEGER) RETURNS BOOLEAN
   DECLARE Index : INTEGER
   DECLARE Count : INTEGER
   Count ← 0                                  // initialise before the loop
   FOR Index ← 1 TO 150                       // exact bounds of the global array
      IF Data[Index] = Search THEN
         Count ← Count + 1                    // update inside the loop
      ENDIF
   NEXT Index
   IF Count > Limit THEN                      // decide after the loop
      RETURN TRUE
   ELSE
      RETURN FALSE                            // a return in both cases
   ENDIF
ENDFUNCTION

// B: stop as soon as found (efficient search / first unused element)
FUNCTION FindFirst(Search : STRING) RETURNS INTEGER
   DECLARE Index : INTEGER
   DECLARE FoundAt : INTEGER
   FoundAt ← -1
   Index ← 1
   WHILE FoundAt = -1 AND Index <= 150        // neither test reads the array, so no
      IF Data[Index] = Search THEN            // short-circuit is needed (D25)
         FoundAt ← Index
      ENDIF
      Index ← Index + 1
   ENDWHILE
   RETURN FoundAt                             // -1 means "not found"
ENDFUNCTION
```

**得分表述**（引自对应 MS）
- 「Function heading, ending and return type」⟦9618_w23_21:4(a)⟧
- 「Loop (any type) for 150 iterations」⟦9618_w23_21:4(a)⟧
- 「Compare Data element with parameter - if equal, increment Count in a loop」⟦9618_w23_21:4(a)⟧
- 「Sum Odd and Even element values in a loop」⟦9618_s24_21:4⟧
- 「Test for unused element in a loop」⟦9618_w22_23:7(b)(i)⟧
- 「terminating when ErrNum found」⟦9618_w22_22:7(a)⟧

**得分点地图**（核验语料 13 道已拆分题；“题数”= 有这类得分点的题数）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 用下标访问元素 / 记下符合条件元素的下标 | 13 | `array-index` |
| 循环次数恰好覆盖整个数组（150、500、100 …） | 10 | `loop-bounds` |
| 循环里的比较（等于参数、大于上一个、空字符串） | 9 | `relational-ops` |
| 声明局部变量（常要求写明类型） | 8 | `declare-variables`、`data-types` |
| 两个条件组合（找到 OR 到末尾；在范围内） | 6 | `logic-ops` |
| 计数器 / 累加器赋初值 | 5 | `initialise-variables` |
| 模块头与结尾（题目没给模块头时） | 5 | `module-header` |
| 条件循环（找到就停） | 5 | `pre-condition-loop` |
| 循环里计数 / 累加 | 4 | `accumulator` |
| 循环后输出 / 返回（两种情况都有） | 9 | `output-format`、`return-value`、`boolean-return` |

几乎每次都有的四分：**下标访问、循环范围、循环里的比较、声明（与初值）**。再加上模块头和“两种情况的返回 / 输出”，一道 6 分题就齐了。

**易错与失分**
- 在模块里重新 `DECLARE Data : ARRAY…`：全局数组已存在，重声明会产生一个新的局部空数组。
- 循环写成 `FOR Index ← 0 TO 150` 或 `1 TO 149`：下标范围照声明。
- 返回写在循环里：`IF … THEN RETURN TRUE ELSE RETURN FALSE` 放进循环，第一个元素就结束了。
- 只写找到时的返回，漏了循环后的 `RETURN FALSE` / `RETURN -1`。
- 用 `WHILE Index <= 500 AND Data[Index] <> 999`：Index = 501 时可能越界（D25），改用标志变量。
- 函数里用 `OUTPUT` 代替 `RETURN`。

#### 代表题精讲　⟦9618_w23_21:4(a)⟧

**在考什么**　全局数组 `DECLARE Data : ARRAY[1:150] OF STRING`。函数 TooMany()：①两个参数：搜索串（STRING）、最大值（INTEGER）；②数数组里与搜索串完全相同的元素个数；③个数大于最大值返回 TRUE，否则 FALSE。Write pseudocode for the function TooMany(). 6 分。

**完整作答**

```pseudocode
FUNCTION TooMany(Search : STRING, Max : INTEGER) RETURNS BOOLEAN
   DECLARE Count : INTEGER
   DECLARE Index : INTEGER
   Count ← 0
   FOR Index ← 1 TO 150
      IF Data[Index] = Search THEN
         Count ← Count + 1
      ENDIF
   NEXT Index
   IF Count > Max THEN
      RETURN TRUE
   ELSE
      RETURN FALSE
   ENDIF
ENDFUNCTION
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function heading, ending and return type | 首行 `FUNCTION … RETURNS BOOLEAN` 与 `ENDFUNCTION` | `module-header` |
| 2 | Declare Count and Index as integers | 两个 `DECLARE … : INTEGER` | `declare-variables`、`data-types` |
| 3 | Initialise Count | `Count ← 0`（循环前） | `initialise-variables` |
| 4 | Loop (any type) for 150 iterations | `FOR Index ← 1 TO 150` | `loop-bounds`、`array-index` |
| 5 | Compare Data element with parameter - if equal, increment Count in a loop | 循环里的 IF | `array-index`、`accumulator` |
| 6 | Compare Count with Max and return Boolean in both cases outside the loop | 循环后的 IF … ELSE，两个 RETURN | `relational-ops`、`boolean-return` |

`RETURN Count > Max` 一句也能表达，但 MS 写的是“both cases”，两个 RETURN 最稳。

**直观**　点名册数人头：从第 1 号点到第 150 号，名字对上就划一笔，点完再看笔数是否超过上限。

**同题 Python 版要点**
- 全局数组在 Python 里是模块级 list，函数里只读它不需要 `global`。
- 参数名 `Max` 在 Python 里不要用 `max`（会遮住内置函数），改 `max_count`。
- 不要用 `data.count(search)` 代劳；`range(150)` 对应下标 0–149。先过阶梯 **L06 E02**。

```python
def too_many(search: str, max_count: int) -> bool:
    count = 0
    for index in range(150):
        if data[index] == search:
            count = count + 1
    return count > max_count
```

**迁移与卡点**
- **卡点**：选错循环。要看完全部元素（计数、求和、最值）用 FOR；“找到就停 / efficient / 遇到未用元素就停”必须用条件循环 + 标志，而且条件里不读数组（D25）。判断标准只有一个：**这个循环能不能提前结束**——能就 WHILE，不能就 FOR。
- **考官在换什么**：数组是全局的、下标范围题目给、循环里只有三种动作（比较、计数 / 累加、记下标）；换的是“做完全部还是找到就停”“结果是布尔、下标还是计数”“一个数组还是并行数组”。六分里“下标访问、循环范围、比较、声明与初值”四分固定。
- **从代表题到变式**：代表题 TooMany 看完 150 个再比较（FOR + 循环后 IF）；变式是在升序的 ErrCode 里找一个编号——找到、越过（当前值已大于目标）或查完 500 个都要停，所以是 WHILE + 标志，而且“越过就停”这一分（efficiency）在代表题里不存在。搬过去的是声明、初值、`Data[Index]`、循环后两种情况各一句输出；要重写的是循环头和停下来的条件。
- **反例**：`WHILE Index <= 500 AND ErrCode[Index] <> Target` 在第 501 次判断时读了不存在的元素；考场上 MS 可能照样给分，但自己写时用标志变量——同一个习惯 P3-CT-02 也用得上。

**下一道变式**　⟦9618_w22_22:7(a)⟧　（换成高效查找：ErrCode 升序，找到、越过或查完 500 个就停，两种情况各输出一句。）

<!-- auto:drills P2-DT-05 -->

### P2-DT-06　二维数组处理模块　{#P2-DT-06}

<!-- auto:stats P2-DT-06 -->

**考法**　按模块描述写遍历全局二维数组的模块：①两列表（第 1 列 ID、第 2 列数值），按行扫描、只看某一列，找到 / 遇到未用行就停；②全表嵌套循环：按列求平均写进结果数组、统计满足条件的格；③查重：外层每行、内层从下一行起比较；④找空行写入两列。6–8 分。

**识别信号**　A global 2D array … organised as n rows by 2 columns；column 1 contains … column 2 contains …；ARRAY[1:r, 1:c]；rows that are not currently being used have the value … 99999；Unused elements contain the empty string (""). These may occur anywhere in the array。

**解题思路**
1. **先画出表头**：哪一维是行、哪一维是列；每列存什么；未用行怎么标记（如第 1 列为 99999 或 ""）。
2. **两列表**只需要**一个行下标**：`Loyalty[Index, 1]` 是 ID，`Loyalty[Index, 2]` 是数值。不用嵌套循环。
3. **全表**要两个下标、两层循环：外层行、内层列（或按题意反过来，如“每列的平均”外层列、内层行）。初值放在**内层循环之前**（每行 / 每列重新计数）。
4. **高效 / 找到就停**：条件循环 + 标志，或在行循环里分层判断，不用 `AND` 去保护越界下标（D25）。
5. **结果**：循环后输出 / 返回；求平均用 `/`，要整数时用 `INT()`。

**伪代码模板**

```pseudocode
// A: n rows x 2 columns, scan one row at a time, stop at the first unused row
PROCEDURE Report()
   DECLARE Index : INTEGER
   DECLARE Finished : BOOLEAN
   Index ← 1
   Finished ← FALSE
   WHILE Finished = FALSE
      IF Table[Index, 1] = 99999 THEN         // unused-row marker
         Finished ← TRUE
      ELSE
         // process Table[Index, 1] and Table[Index, 2]
         Index ← Index + 1
         IF Index > 1000 THEN                 // checked before Table[Index, 1] is read again
            Finished ← TRUE
         ENDIF
      ENDIF
   ENDWHILE
ENDPROCEDURE

// B: whole grid, nested loops
FOR Row ← 1 TO 6
   Count ← 0                                  // reset before the inner loop
   FOR Col ← 1 TO 128
      IF Sample[Row, Col] > 10 THEN
         Count ← Count + 1
      ENDIF
   NEXT Col
NEXT Row
```

**得分表述**（引自对应 MS）
- 「Create procedure header and ending」⟦9618_s25_22:7(b)⟧
- 「Declare and initialise Index, Sum and Count」⟦9618_s25_22:7(b)⟧
- 「Inner loop for six iterations」⟦9618_s23_21:6⟧
- 「Use of INT()/ DIV to convert average to integer」⟦9618_s23_21:6⟧
- 「Compare value of element in column 1 with parameter passed into function」⟦9618_s22_21:8(b)⟧
- 「Check for unused element by testing value in column 1 in a loop」⟦9618_s22_23:9(b)⟧

**得分点地图**（核验语料 10 道已拆分题）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 二维下标写对 `Array[Row, Col]`、取对列 | 10 | `array-2d` |
| 循环里的比较（等于参数、≥ 阈值、是否未用） | 9 | `relational-ops` |
| 输出（循环里逐个 / 循环后汇总，带说明文字） | 6 | `output-format` |
| 循环范围（行数、列数） | 6 | `loop-bounds` |
| 条件循环（找到 / 遇到未用行就停） | 5 | `pre-condition-loop` |
| 声明局部变量 | 5 | `declare-variables` |
| 找到就停 / 查重 | 4 | `linear-search` |
| 嵌套循环 | 4 | `nested-loops` |
| 初值与累加 | 4 | `initialise-variables`、`accumulator` |

**易错与失分**
- 下标写成 `Loyalty[Index][2]`（Python 写法）：伪代码是 `Loyalty[Index, 2]`。
- 行列写反：`[1:1000, 1:2]` 是 1000 行 2 列，第二个下标才是列。
- 内层计数器的初值放在外层循环之前：第二行开始就带着上一行的数。
- 两列表也写嵌套循环去“遍历列”：只需固定列号。
- 平均数用 `DIV` 或忘了题目要求整数时的 `INT()`。

#### 代表题精讲　⟦9618_s25_22:7(b)⟧

**在考什么**　咖啡店会员积分：全局二维整数数组 Loyalty，1000 行 × 2 列，第 1 列会员 ID、第 2 列积分；未用行第 1 列为 99999；数组按 ID 升序（未用行都在末尾）。模块 PointsReport()：输出积分 ≥ 11 的每个会员 ID；输出全部会员的平均积分并配说明文字。Write efficient pseudocode for module PointsReport(). 假设至少有一位会员。7 分（MS 列 8 点）。

**完整作答**

```pseudocode
PROCEDURE PointsReport()
   DECLARE Index : INTEGER
   DECLARE Count : INTEGER
   DECLARE Sum : INTEGER
   DECLARE Average : REAL
   DECLARE Finished : BOOLEAN
   Index ← 1
   Count ← 0
   Sum ← 0
   Finished ← FALSE
   WHILE Finished = FALSE
      IF Loyalty[Index, 1] = 99999 THEN
         Finished ← TRUE
      ELSE
         IF Loyalty[Index, 2] >= 11 THEN
            OUTPUT Loyalty[Index, 1]
         ENDIF
         Count ← Count + 1
         Sum ← Sum + Loyalty[Index, 2]
         Index ← Index + 1
         IF Index > 1000 THEN
            Finished ← TRUE
         ENDIF
      ENDIF
   ENDWHILE
   Average ← Sum / Count
   OUTPUT "The average points of all the customers is ", Average
ENDPROCEDURE
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Create procedure header and ending | `PROCEDURE PointsReport()` … `ENDPROCEDURE` | `module-header` |
| 2 | Declare and initialise Index, Sum and Count | 声明并赋初值 | `declare-variables`、`initialise-variables` |
| 3 | Loop through all elements in Loyalty array | WHILE 到第 1000 行为止 | `loop-bounds`、`array-2d` |
| 4 | … or terminates when column1 of Loyalty array equals 99999 in a loop | `Loyalty[Index, 1] = 99999` 时 Finished | `array-2d`、`relational-ops` |
| 5 | Check if loyalty points greater than or equal to 11 in a loop | `Loyalty[Index, 2] >= 11` | `array-2d`、`relational-ops` |
| 6 | If true output customer ID | `OUTPUT Loyalty[Index, 1]` | `array-2d`、`output-format` |
| 7 | Sum points and Increment Count in a loop | `Sum ← …`、`Count ← …` | `array-2d`、`accumulator` |
| 8 | Calculate and output average with an appropriate message | 循环后 `/` 求平均并输出 | `operator-precedence`、`output-format` |

MS 范例写的是 `WHILE Loyalty[Index, 1] <> 99999 AND Index <= 1000`；按该题 MS 给分，不改其计分清单。但 Index = 1001 时，即使按从左到右短路求值，左侧数组访问也已越界，右侧边界检查不能保护它。指南未保证 AND 短路，本手册按 D25 保留先检查边界、再访问数组的标志变量方案。

**直观**　从表头往下一行行读，读到“空行记号”或读到底就停；每读一行做两件事：够 11 分就念出 ID，并把积分记进总账。

**同题 Python 版要点**
- 二维数组是“列表的列表”：`loyalty[index][0]` 是 ID、`loyalty[index][1]` 是积分（0 起）。
- 循环可写 `for row in loyalty:` 再 `if row[0] == 99999: break`——Python 里这很自然，但写伪代码时不能这样写（D2）。
- 先过阶梯 **L06 E04**（二维数组）。

```python
def points_report() -> None:
    count = 0
    total = 0
    for row in loyalty:
        if row[0] == 99999:
            break
        if row[1] >= 11:
            print(row[0])
        count = count + 1
        total = total + row[1]
    print("The average points of all the customers is", total / count)
```

**迁移与卡点**
- **卡点**：分不清“两列表”和“全表”。n 行 × 2 列的表每行是一条记录（ID、数值），只要**一个**行下标、列号固定写 1 或 2；真正的网格（6 行 × 128 列样本）才要两层循环。先画表头再决定循环层数，画错一次就多写一层循环。
- **考官在换什么**：行列大小、未用行的标记（99999、""）、按行还是按列汇总、找到就停还是看完全部。二维下标 `[Row, Col]` 一分、取对列一分、比较一分、输出一分，题题都有。
- **从代表题到变式**：代表题 PointsReport 是两列表 + 提前停；变式是 6 × 128 的全表、按列求平均写进结果数组——两层循环，**内层开始前重置计数器**，内层结束后算平均并 `INT()`。搬过去的是声明、`Sample[Row, Col]` 的写法、`/` 求平均；要重建的是嵌套结构和初值的位置。
- **反例**：把 `Count ← 0` 放在外层循环之前，第二列起就带着上一列的数——二维题最常丢的一分，自查时盯住“初值在哪一层”。

**下一道变式**　⟦9618_s23_21:6⟧　（全表嵌套循环：6 行 × 128 列的声音样本，按列统计大于 10 的样本求整数平均，写进结果数组。）

<!-- auto:drills P2-DT-06 -->

### P2-DT-07　记录数组处理模块　{#P2-DT-07}

<!-- auto:stats P2-DT-07 -->

**考法**　按模块描述写遍历记录数组的模块：①按某字段（StudentID）筛选，再按另一字段（OnLoan）分别计数并输出；②查找满足两个字段条件的记录，找到就修改字段并返回 TRUE；③找第一个未用记录写入新数据；④统计某字段之和；⑤输出满足条件的记录的若干字段；⑥（2021 扩展）比较一条记录的多个同类字段。6–8 分，常有 efficient 要求。

**识别信号**　The programmer has defined a record type …；A global array … stores n … records；Data item | Data type | Comment 表；Unused elements have the StudentID set to an empty string；Write (efficient) pseudocode for module …。

**解题思路**
1. **抄出记录的字段名**（大小写照抄）与数组名、元素个数、未用标记。
2. **访问写法**：`Loan[Index].StudentID`——数组名、下标、点号、字段名。
3. **选循环**：统计全部 → FOR 全部元素；找到就停 / efficient → WHILE + 标志。
4. **多个条件**：两个字段都要满足 → `AND`，或嵌套 IF 写清两种结果（借出中 / 已归还各计一个数）。
5. **未用记录**：未用元素的字段是空串，统计时它们自然不等于参数；找空位时要判断 `= ""`。
6. **循环后**输出或返回，两种情况都要有。

**伪代码模板**

```pseudocode
// A: count over all records
PROCEDURE CountByField(ThisID : STRING)
   DECLARE Index : INTEGER
   DECLARE Count : INTEGER
   Count ← 0
   FOR Index ← 1 TO 7000
      IF Loan[Index].StudentID = ThisID AND Loan[Index].OnLoan = TRUE THEN
         Count ← Count + 1
      ENDIF
   NEXT Index
   OUTPUT "Books on loan: ", Count
ENDPROCEDURE

// B: find the first matching record, change it, stop
FUNCTION Update(ThisID : STRING) RETURNS BOOLEAN
   DECLARE Index : INTEGER
   DECLARE Found : BOOLEAN
   Found ← FALSE
   Index ← 1
   WHILE Found = FALSE AND Index <= 7000
      IF Loan[Index].StudentID = ThisID THEN
         Loan[Index].OnLoan ← FALSE
         Found ← TRUE
      ENDIF
      Index ← Index + 1
   ENDWHILE
   RETURN Found
ENDFUNCTION
```

**得分表述**（引自对应 MS）
- 「Index references an indexed data item with correct .dot notation」⟦9618_w25_22:8(a)⟧
- 「Test of the OnLoan field and correct logic for both outcomes」⟦9618_w25_22:8(a)⟧
- 「Output includes both counts with a suitable message」⟦9618_w25_22:8(a)⟧
- 「Test for correct StudentID field in a loop」⟦9618_w25_21:8(a)⟧
- 「attempt to skip unused element」⟦9618_s22_23:5(c)⟧
- 「When character found set termination condition/flag」⟦9618_w24_22:8(a)⟧

**得分点地图**（核验语料 11 道已拆分题）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 点号访问字段 `Array[Index].Field` | 11 | `array-of-records` |
| 循环覆盖全部记录（7000、45、500 …） | 11 | `loop-bounds` |
| 输出（带说明文字；两种情况；只一次） | 8 | `output-format` |
| 字段与参数比较 | 7 | `relational-ops` |
| 两个字段条件组合 | 7 | `logic-ops` |
| 模块头与结尾 | 4 | `module-header` |
| 找到就停 | 4 | `linear-search` |
| 循环里计数 / 累加 | 4 | `accumulator` |

几乎每次都有的三分：**点号访问、循环范围、输出**；再加两个字段的比较与组合。

**易错与失分**
- 写成 `Loan.StudentID[Index]` 或 `Loan[Index, StudentID]`。
- 字段名拼写改成了另一个名字（如 `StudentNumber`）：照题目表格抄。建议大小写也保持一致，但指南 §2.3 规定标识符不区分大小写，`StudentId` 与 `StudentID` 仅大小写不同，不能据此认定为不同字段或当然扣分。
- 布尔字段写成字符串比较 `= "TRUE"`。
- 两个计数器只初始化一个；或计数写在 IF 外面（每条记录都加）。
- efficient 题用 FOR 跑完全部元素：找到后还在循环，丢“terminate”那一分。

#### 代表题精讲　⟦9618_w25_22:8(a)⟧

**在考什么**　图书馆借书：记录字段 StudentID（STRING）、BookID（STRING）、OnLoan（BOOLEAN，TRUE 表示还没还）；全局数组 Loan 存 7000 条记录，未用元素的 StudentID 为空串、可能在任何位置。模块 CountLoans()：参数为一个 StudentID；数出该学生目前借着的书和已经还了的书；两个数都输出，配说明文字。7 分。

**完整作答**

```pseudocode
PROCEDURE CountLoans(ThisStudentID : STRING)
   DECLARE Index : INTEGER
   DECLARE LCount : INTEGER
   DECLARE RCount : INTEGER
   LCount ← 0
   RCount ← 0
   FOR Index ← 1 TO 7000
      IF Loan[Index].StudentID = ThisStudentID THEN
         IF Loan[Index].OnLoan = TRUE THEN
            LCount ← LCount + 1
         ELSE
            RCount ← RCount + 1
         ENDIF
      ENDIF
   NEXT Index
   OUTPUT "Student has ", LCount, " books on loan"
   OUTPUT "and has returned ", RCount, " books"
ENDPROCEDURE
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Declaration of Index and two count variables | 三个 DECLARE | `declare-variables` |
| 2 | Loop for 7000 iterations | `FOR Index ← 1 TO 7000` | `loop-bounds` |
| 3 | Index references an indexed data item with correct .dot notation | `Loan[Index].StudentID` | `array-of-records` |
| 4 | Attempt to compare the StudentID field = parameter in a loop | 外层 IF | `array-of-records`、`relational-ops` |
| 5 | Test of the OnLoan field and correct logic for both outcomes | 内层 IF … ELSE | `array-of-records`、`nested-if` |
| 6 | Both count variables initialised and increment appropriate count in a loop | 两个 `← 0` 与两个 `+ 1` | `accumulator`、`initialise-variables` |
| 7 | Output includes both counts with a suitable message | 循环后两句 OUTPUT | `output-format` |

未用元素的 StudentID 是空串，不会等于参数，所以不必单独跳过。

**直观**　翻 7000 张借书卡，只看写着这个学生名字的那几张；每张再看一眼“还了没”，分成两堆数。

**同题 Python 版要点**
- 记录数组 = 对象列表：`loan[index].student_id`；布尔字段直接 `if loan[index].on_loan:`。
- `for record in loan:` 直接遍历对象最自然；要下标时用 `range(7000)`。
- 先过阶梯 **L08 E01**（记录与记录数组）。

```python
def count_loans(this_student_id: str) -> None:
    l_count = 0
    r_count = 0
    for record in loan:
        if record.student_id == this_student_id:
            if record.on_loan:
                l_count = l_count + 1
            else:
                r_count = r_count + 1
    print("Student has", l_count, "books on loan")
    print("and has returned", r_count, "books")
```

**迁移与卡点**
- **卡点**：`Loan[Index].StudentID`——先下标后点号——以及两个字段条件怎样组合。一个字段筛选、另一个字段分两堆时，是外层 IF（筛选）套内层 IF … ELSE（分堆）；两个条件都要满足才用 AND。先说出“哪个字段决定进不进来、哪个字段决定进哪一堆”，再动笔。
- **考官在换什么**：记录的字段（名字照抄）、元素个数、未用元素的标记、要找一条还是数全部、是否 efficient。“点号访问、循环范围、输出带说明文字”三分固定。
- **从代表题到变式**：代表题 CountLoans 看完 7000 条、分两堆；变式是“数到上限 Max 就停、输出能借 / 不能借”——循环变成 WHILE + 标志（够数就停），输出变成两种情况各一句。搬过去的是 `Loan[Index].StudentID = ThisStudentID` 的比较和 OnLoan 的判断；要换的是循环头、停止条件和循环后的两种输出。
- **反例**：布尔字段写成 `Loan[Index].OnLoan = "TRUE"`（和字符串比）或 `= 1`：BOOLEAN 字段直接 `= TRUE`，或者干脆 `IF Loan[Index].OnLoan THEN`。

**下一道变式**　⟦9618_w25_21:8(a)⟧　（换成 efficient：数到上限 Max 就停，输出“可以借 / 不能借”两种消息之一。）

<!-- auto:drills P2-DT-07 -->

### P2-DT-08　冒泡排序　{#P2-DT-08}

<!-- auto:stats P2-DT-08 -->

**考法**　①写高效冒泡排序：同时交换两个并行数组，或交换二维数组的两列（8 分）；②描述把升序改成降序要改哪里（1 分）；③解释为什么第二种冒泡比第一种高效（内层循环每轮少一次 + 没有交换就停，4 分）；④什么情况下外层循环次数最少（数组已有序）。核验语料次数少但分值大，考纲 10.2 点名要求。

**识别信号**　Write an efficient bubble sort algorithm in pseudocode；Sorts the arrays into ascending order；Explain why the second bubble sort algorithm is more efficient；descending order；move the largest value to the end。

**解题思路**
1. **两层循环**：外层 `REPEAT … UNTIL NoSwaps = TRUE`；内层 `FOR J ← 1 TO Boundary` 比较相邻两个元素 `J` 与 `J + 1`。
2. **Boundary 初值 = 元素个数 − 1**（比较 J 与 J + 1，J 最大到 n − 1），每趟外层结束 `Boundary ← Boundary - 1`（每趟最大的值已“冒”到末尾）。
3. **交换**用一个临时变量，三句：`Temp ← A[J]`、`A[J] ← A[J + 1]`、`A[J + 1] ← Temp`；临时变量的类型与被交换的元素一致。
4. **并行数组 / 二维数组**：比较一个数组（一列），交换时**两个数组（两列）都换**。
5. **NoSwaps 机制**：每趟开始 `NoSwaps ← TRUE`；内层一有交换就 `NoSwaps ← FALSE`；一趟没有交换说明已排好，外层结束。
6. **降序**：把比较的 `>` 改成 `<`。

**伪代码模板**

```pseudocode
PROCEDURE SortArrays()
   DECLARE J : INTEGER
   DECLARE Boundary : INTEGER
   DECLARE TempInt : INTEGER
   DECLARE TempStr : STRING
   DECLARE NoSwaps : BOOLEAN
   Boundary ← 499                       // number of elements - 1
   REPEAT
      NoSwaps ← TRUE                    // reset the flag for each pass
      FOR J ← 1 TO Boundary
         IF ErrCode[J] > ErrCode[J + 1] THEN       // use < for descending order
            TempInt ← ErrCode[J]
            ErrCode[J] ← ErrCode[J + 1]
            ErrCode[J + 1] ← TempInt
            TempStr ← ErrText[J]                   // swap the parallel array too
            ErrText[J] ← ErrText[J + 1]
            ErrText[J + 1] ← TempStr
            NoSwaps ← FALSE
         ENDIF
      NEXT J
      Boundary ← Boundary - 1           // the last element of this pass is in place
   UNTIL NoSwaps = TRUE
ENDPROCEDURE
```

**得分表述**（引自对应 MS）
- 「Comparison (element J with J+1) in a loop」⟦9618_w22_22:7(b)⟧
- 「Swap elements in both arrays in a loop」⟦9618_w22_22:7(b)⟧
- 「Reducing Boundary in the outer loop」⟦9618_w22_22:7(b)⟧
- 「Both SensorID and Speed values were swapped in a loop」⟦9618_s25_21:6(b)⟧
- 「The inner loop iterates one less time (in algorithm B) each time the outer / repeat loop iterates」⟦9618_s26_22:5(b)(i)⟧

**得分点地图**（写排序的 3 道不同题：w22/22、s25/21 与 2021 扩展 s21/21；三题的计分清单几乎相同）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 外层条件循环（REPEAT … UNTIL）正确结束 | 3 | `post-condition-loop` |
| 内层循环 + 正确范围 | 3 | `nested-loops`、`loop-bounds` |
| 比较 J 与 J + 1 | 3 | `bubble-sort`、`relational-ops` |
| 交换（并行数组 / 两列都换） | 3 | `bubble-sort`、`parallel-arrays`、`array-2d` |
| NoSwap 机制：每趟重置标志 + 有交换时置标志 | 3 | `bubble-sort`、`flag-variable` |
| 外层每趟缩小 Boundary | 3 | `bubble-sort`、`loop-bounds` |
| 模块头与结尾 | 2 | `module-header` |

一道 8 分的冒泡题，**8 个得分点就是模板的 8 个部件**——把模板默写熟就是满分。

**易错与失分**
- 内层循环到 n：`ErrCode[J + 1]` 在 J = n 时越界；上界是 n − 1（再减去已排好的）。
- 交换写成 `A[J] ← A[J + 1]`、`A[J + 1] ← A[J]`：没有临时变量，两个都变成同一个值。
- 只换了 ErrCode 没换 ErrText：两个数组从此错位。
- NoSwaps 在 REPEAT 之前设一次而不是每趟开头重置：只排一趟就停或永远不停。
- 用 `WHILE NoSwaps = FALSE` 却没先给 NoSwaps 赋 FALSE：一次都不执行。

#### 代表题精讲　⟦9618_w22_22:7(b)⟧

**在考什么**　两个全局一维数组各 500 个元素：ErrCode（错误号，整数）、ErrText（错误描述，字符串），同一下标对应同一个错误；未用元素 ErrCode 为 999。Write an efficient bubble sort algorithm in pseudocode for module SortArrays()（按 ErrCode 升序）。8 分，MS 列 9 点。

**完整作答**　即上面的“伪代码模板”（本题正是模板的来源）。

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure heading and ending as shown | `PROCEDURE SortArrays()` … `ENDPROCEDURE` | `module-header` |
| 2 | Conditional loop correctly terminated | `REPEAT … UNTIL NoSwaps = TRUE` | `post-condition-loop` |
| 3 | An inner loop | `FOR J …` | `nested-loops` |
| 4 | Correct range for inner loop | `1 TO Boundary`，Boundary 从 499 起 | `loop-bounds` |
| 5 | Comparison (element J with J+1) in a loop | `IF ErrCode[J] > ErrCode[J + 1]` | `bubble-sort`、`array-index` |
| 6 | Swap elements in both arrays in a loop | 两组三句交换 | `bubble-sort`、`parallel-arrays` |
| 7 | 'No-Swap' mechanism: • Conditional outer loop including flag reset • Flag set in inner loop to indicate swap | 每趟 `NoSwaps ← TRUE`，交换时 `← FALSE` | `bubble-sort`、`flag-variable` |
| 8 | Efficiency (this scenario): terminate inner loop when ErrCode = 999 | （模板未做；Max 8，不做也满分） | `array-index`、`relational-ops` |
| 9 | Reducing Boundary in the outer loop | `Boundary ← Boundary - 1` | `bubble-sort`、`loop-bounds` |

模板拿到 MP1–7 与 MP9，共 8 点 = 满分。MP8 要把内层改成条件循环、遇到 999 就停，写对可作保险。

**直观**　一排人按身高站：从左往右两两比较，高的往右换；一趟下来最高的到了最右边，下一趟就不用再管他所在的位置；某一趟谁都没换，说明已经排好了。

**同题 Python 版要点**
- 交换可以一句 `a[j], a[j + 1] = a[j + 1], a[j]`——这是 Python 特有写法，伪代码里必须三句加临时变量。
- `REPEAT … UNTIL` ↔ `while True:` … `if no_swaps: break`。
- 不要用 `sort()` 代劳；并行数组两个都要换。先过阶梯 **L06 E03**（冒泡排序）。

```python
def sort_arrays() -> None:
    boundary = 499                      # compare j with j + 1, j = 0 .. boundary - 1
    while True:
        no_swaps = True
        for j in range(boundary):
            if err_code[j] > err_code[j + 1]:
                err_code[j], err_code[j + 1] = err_code[j + 1], err_code[j]
                err_text[j], err_text[j + 1] = err_text[j + 1], err_text[j]
                no_swaps = False
        boundary = boundary - 1
        if no_swaps:
            break
```

**下一道变式**　⟦9618_s25_21:6(b)⟧　（二维数组版：Reading 有 2000 行 × 2 列（传感器 ID、速度），按 ID 排序，两列一起交换。）

<!-- auto:drills P2-DT-08 -->

### P2-DT-09　读文本文件逐行处理　{#P2-DT-09}

<!-- auto:stats P2-DT-09 -->

**考法**　写只读文件的模块：①数非空行，够 10 行就停并返回 TRUE；②逐行检查（调用已写好的 CheckLine()）并数错误，超过上限就停；③在按编号排序的文件里查一个编号是否已存在；④按字段筛选并输出报表；⑤把每行拆成字段写进数组；⑥保留最后三行并按原顺序输出；⑦只输出前 5 行，空文件给警告。6–8 分。

**识别信号**　text file；Each line of the file contains …；take the name of a text file as a parameter；OPENFILE … FOR READ；search the file for …；output the … lines from that file；Assume CheckFile() … have been written and can be used。

**解题思路**
1. **文件名**是参数（STRING）或题目给的字面量（`"Stock.txt"`）。打开以后仍用这个名字指代文件。
2. **骨架三件套**：`OPENFILE <名> FOR READ` → `WHILE NOT EOF(<名>)` … `READFILE <名>, Line` … `ENDWHILE` → `CLOSEFILE <名>`。先判断 EOF、再读，空文件也安全。
3. **循环里**处理 `Line`：判断非空 `Line <> ""`；用 `LEFT` / `MID` / `RIGHT` 取字段；`STR_TO_NUM` 转数字；调用题目给的模块。
4. **提前结束**（够数、找到、超过上限）：在 WHILE 条件里加一个标志或计数条件——`WHILE NOT EOF(F) AND Found = FALSE`（两边都不会出错，可以放心用 AND）。
5. **关闭文件**在循环之后、`RETURN` 之前。

**伪代码模板**

```pseudocode
FUNCTION CheckFile(ThisFile : STRING) RETURNS BOOLEAN
   DECLARE ThisLine : STRING
   DECLARE Count : INTEGER
   DECLARE Valid : BOOLEAN
   Count ← 0
   Valid ← FALSE
   OPENFILE ThisFile FOR READ
   WHILE NOT EOF(ThisFile) AND Valid = FALSE   // stop early when the goal is reached
      READFILE ThisFile, ThisLine              // the line has no newline character
      IF ThisLine <> "" THEN
         Count ← Count + 1
         IF Count = 10 THEN
            Valid ← TRUE
         ENDIF
      ENDIF
   ENDWHILE
   CLOSEFILE ThisFile                          // close before returning
   RETURN Valid
ENDFUNCTION
```

**得分表述**（引自对应 MS）
- 「OPEN in READ mode and CLOSE」⟦9618_w22_21:8(a)⟧
- 「Conditional loop until EOF()」⟦9618_w22_21:8(a)⟧
- 「Read a line in a loop」⟦9618_w22_21:8(a)⟧
- 「Terminate loop when 10 non-blank lines have been read」⟦9618_w22_21:8(a)⟧
- 「Read a line from Stock.txt AND extract ThisItemNum in a loop」⟦9618_s23_21:8(b)⟧
- 「Correctly shuffle LineX, LineY and LineZ in a loop」⟦9618_s22_22:4(a)⟧

**得分点地图**（核验语料 10 道已拆分题）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 以 READ 模式打开；循环里读一行 | 10 | `file-open-read` |
| 循环到 EOF | 9 | `loop-to-eof` |
| 打开后关闭（常与打开合成一分） | 8 | `file-close` |
| 循环里的比较（非空、等于参数、> 某值） | 6 | `relational-ops` |
| 计数器 / 标志赋初值 | 5 | `initialise-variables` |
| 输出（循环里或循环后，带说明文字） | 5 | `output-format` |
| 循环里计数 | 5 | `accumulator` |
| 调用题目给的模块并使用返回值 | 5 | `procedure-call` |
| 从一行里取出字段 | 4 | `field-extract` |

几乎每次都有的三分：**READ 打开 + 循环到 EOF + 循环里读一行**，再加关闭。这三四分与题目内容无关，开卷就该先写下。

**易错与失分**
- `FOR Line IN File`、`WHILE NOT EOF()` 不写文件名、`READFILE Line`（不写文件名）：Python 式写法不给分（D2）。
- 先 READFILE 再判断 EOF 的写法在空文件上会出错；按“判断 EOF → 读”的顺序。
- 忘了 `CLOSEFILE`，或把 `CLOSEFILE` 写进循环、写在 `RETURN` 之后（永远执行不到）。
- 打开模式写成 WRITE：文件内容被清空。
- 把文件当数组用：`File[Index]`。

#### 代表题精讲　⟦9618_w22_21:8(a)⟧

**在考什么**　学生程序以文本文件提交（project file），可能有空行。模块 CheckFile()：参数为一个已存在的项目文件名（STRING）；文件有效（至少 10 个非空行）返回 TRUE，否则 FALSE。Write pseudocode for module CheckFile(). 7 分，MS 列 8 点。

**完整作答**　即上面的“伪代码模板”（本题正是模板的来源）。

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function heading and ending including parameter and return type | `FUNCTION CheckFile(ThisFile : STRING) RETURNS BOOLEAN` … `ENDFUNCTION` | `module-header` |
| 2 | Declaration and initialisation of local Integer for Count | `DECLARE Count : INTEGER`、`Count ← 0` | `declare-variables`、`initialise-variables`、`data-types` |
| 3 | OPEN in READ mode and CLOSE | `OPENFILE … FOR READ`、`CLOSEFILE …` | `file-open-read`、`file-close` |
| 4 | Conditional loop until EOF() | `WHILE NOT EOF(ThisFile) …` | `loop-to-eof` |
| 5 | Read a line in a loop | `READFILE ThisFile, ThisLine` | `file-open-read` |
| 6 | If non-blank, increment count in a loop | `IF ThisLine <> "" THEN Count ← Count + 1` | `relational-ops`、`accumulator` |
| 7 | Terminate loop when 10 non-blank lines have been read | `Valid ← TRUE` 让 WHILE 结束 | `flag-variable`、`relational-ops` |
| 8 | Return Boolean in both cases | `RETURN Valid`（TRUE 或 FALSE） | `boolean-return` |

MS 范例写的是 `OPEN ThisFile FOR READ`；指南的关键字是 `OPENFILE`，本手册一律写 OPENFILE。

**直观**　翻一本作业本数“写了字的页”，数到第 10 页就合上本子说“合格”；翻到最后都不够 10 页就说“不合格”。

**同题 Python 版要点**
- `with open(this_file) as file:` 自动关闭；`for line in file:` 逐行读，但每行**带着** `"\n"`，要 `line.rstrip("\n")` 后再判断是否为空。
- 提前结束可以直接 `return True`（`with` 会负责关闭）；伪代码里则要先 `CLOSEFILE` 再 `RETURN`。
- 先过阶梯 **L07 E02**（逐行读并计数）。

```python
def check_file(this_file: str) -> bool:
    count = 0
    with open(this_file) as file:
        for line in file:
            if line.rstrip("\n") != "":
                count = count + 1
                if count == 10:
                    return True
    return False
```

**迁移与卡点**
- **卡点**：先读还是先判断 EOF。顺序是“判断 EOF → 读一行 → 处理”，空文件也安全；写成“读一行 → 判断”会在空文件上读一次不存在的行。第二个卡点是 `CLOSEFILE` 的位置——循环后、`RETURN` 前；函数要提前返回时，也必须先关闭。
- **考官在换什么**：文件每行是什么（一个值、一条记录、一行代码）、读的时候做什么（计数、取字段、调用模块、与参数比较）、什么时候提前停（够数、找到、超限）。“READ 打开 + 循环到 EOF + 循环里读一行 + 关闭”三四分固定，开卷先写下。
- **从代表题到变式**：代表题 CheckFile 数非空行到 10 行就停；变式是“只保留最后三行”——循环不再提前停，而是每读一行就把三个变量前移（`LineX ← LineY`、`LineY ← LineZ`、`LineZ ← Line`），循环后按顺序输出。搬过去的是打开 / EOF 循环 / 读 / 关闭的骨架；要重写的是循环体（移位代替计数）和循环后的输出。移位的顺序一错（先写 `LineZ ← Line`）就把新行盖掉了——在草稿上用三行数据走一遍。
- **反例**：`WHILE NOT EOF()` 不写文件名、`READFILE Line` 不写文件名：指南写法两处都要文件名，少一处就是不完整的语句。

**下一道变式**　⟦9618_s22_22:4(a)⟧　（换成“滚动缓存”：读到文件尾，只用 LineX、LineY、LineZ 三个变量保留最后三行，循环里每读一行就把三者依次前移。技能标签为 `shift-values`，已按 D30、D37③回填。）

<!-- auto:drills P2-DT-09 -->

### P2-DT-10　写入或复制文本文件　{#P2-DT-10}

<!-- auto:stats P2-DT-10 -->

**考法**　写有 WRITEFILE 的模块：①把一个文件逐行复制到另一个文件，复制前用给定模块处理每行、跳过空行，并数被删的行（追加到**已存在**的文件）；②把记录数组的每条记录拼成一行（字段间用分隔符）写进新文件；③从二维数组 / 一维数组按条件挑出数据写进文件；④按编号顺序把一个新行插进有序文件的正确位置（复制到新文件）；⑤先读文件找到最后的编号，再以 APPEND 追加新行；⑥生成多个文件名并各写一行。6–8 分。

**识别信号**　copies each line from the input file to the existing output file；create a new file / creates a new file NewStock.txt；A new module will store the contents of the … array in a text file；write … to the file；form a string from each record with fields separated by the character …；does not write blank lines。

**解题思路**
1. **定模式**：新建或有意覆盖文件 → `WRITE`（原内容清空）；需要保留原内容并在末尾追加 → `APPEND`；读来源文件 → `READ`。同一时刻一个文件只用一种模式；要先读后追加，就先 `CLOSEFILE` 再用新模式打开。
2. **复制 / 过滤骨架**：两个文件都打开 → `WHILE NOT EOF(输入)` → `READFILE 输入, Line` → 处理 → 满足条件才 `WRITEFILE 输出, Line` → 循环后两个都关闭。
3. **数组 → 文件骨架**：打开输出文件 → `FOR` 全部元素 → 跳过未用元素 → 拼成一行 → `WRITEFILE` → 关闭。
4. **写之前转成字符串**：`NUM_TO_STR(…)` 处理数字；布尔值先编码成字符（如 `'T'` / `'F'`）；多个字段用 `&` 和分隔符拼成一行。
5. **计数与输出**：被跳过 / 被写入的行数在循环里计数，循环后输出一次。

**伪代码模板**

```pseudocode
// A: copy / filter one file into another
PROCEDURE CopyFile(InFile : STRING, OutFile : STRING)
   DECLARE Line : STRING
   DECLARE Count : INTEGER
   Count ← 0
   OPENFILE InFile FOR READ
   OPENFILE OutFile FOR APPEND               // Preserve existing data; WRITE to create or overwrite
   WHILE NOT EOF(InFile)
      READFILE InFile, Line
      IF Line <> "" THEN
         WRITEFILE OutFile, Line
      ELSE
         Count ← Count + 1
      ENDIF
   ENDWHILE
   CLOSEFILE InFile
   CLOSEFILE OutFile
   OUTPUT Count, " blank lines were removed"
ENDPROCEDURE

// B: array of records -> one line per record, fields separated by '^'
PROCEDURE Save()
   DECLARE Index : INTEGER
   DECLARE Line : STRING
   OPENFILE "SaveFile.txt" FOR WRITE
   FOR Index ← 1 TO 45
      Line ← NUM_TO_STR(Character[Index].Player) & "^" & Character[Index].Role
      WRITEFILE "SaveFile.txt", Line
   NEXT Index
   CLOSEFILE "SaveFile.txt"
ENDPROCEDURE
```

**得分表述**（引自对应 MS）
- 「Open both files in correct modes and subsequently close」⟦9618_s24_22:8(c)⟧
- 「Loop to EOF(F1)」⟦9618_s24_22:8(c)⟧
- 「Count the blank lines in a loop」⟦9618_s24_22:8(c)⟧
- 「Correct use of NUM_TO_STR()x2 (Player and Level) in a loop」⟦9618_w24_22:8(b)⟧
- 「OPENFILE in WRITE mode and subsequent CLOSE in a loop」⟦9618_w23_22:6(a)⟧
- 「Open file in read mode and close (before opening in append mode)」⟦9618_s25_21:7(b)(i)⟧

**得分点地图**（核验语料 9 道已拆分题）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 打开（模式正确）并在之后关闭 | 9 | `file-close`（加对应模式标签） |
| 循环里 WRITEFILE 写一行 | 8 | `file-write` / `file-append` |
| 循环里计数（写了几行、删了几行、记录数） | 6 | `accumulator` |
| 来源文件以 READ 打开、循环里读一行 | 5 | `file-open-read` |
| 循环到 EOF | 5 | `loop-to-eof` |
| 拼行：字段、分隔符、文件名用 `&` 连接 | 5 | `string-concat` |
| 写之前把数字转成字符串 | 4 | `type-conversion` |
| 调用给定模块处理每行 | 4 | `procedure-call` |
| 只写满足条件的行（非空、匹配） | 4 | `relational-ops` |
| 循环后输出计数（带说明文字） | 4 | `output-format` |

每道写文件题都有的一分：**模式正确地打开 + 之后关闭**（两个文件时两个都要）。

**易错与失分**
- 题目要求保留原内容并追加时却用 WRITE：原有内容被清空；应用 APPEND。文件已存在本身不决定模式，若要求覆盖仍用 WRITE；本卡代表题按其 MS 用 APPEND。
- 读文件与写文件用同一个名字同时打开两次（先读后追加要先关闭）。
- `WRITEFILE` 写数字或布尔值：先 `NUM_TO_STR`，布尔值先编码成字符或字符串。
- 拼行用 `+` 或逗号（`WRITEFILE F, A, B`）：用 `&` 拼成一个字符串再写。
- 跳过空行的判断写在调用处理模块**之前**：处理后才变成空行的那些就漏了（MS：Check return value following both MP5 function calls）。

#### 代表题精讲　⟦9618_s24_22:8(c)⟧

**在考什么**　老师分阶段处理学生的伪代码项目文件。已写好 DeleteComment()（去掉一行里的注释）和 DeleteSpaces()（去掉行首空格，本题 (b) 写过）。Stage_2()：两个参数——输入文件名、输出文件名（STRING）；把输入文件每一行去掉行首空格和注释后复制到**已存在的**输出文件；空行不写；最后输出删掉了多少空行。Write pseudocode for module Stage_2(). 8 分。

**完整作答**

```pseudocode
PROCEDURE Stage_2(F1 : STRING, F2 : STRING)
   DECLARE Line : STRING
   DECLARE Count : INTEGER
   Count ← 0
   OPENFILE F1 FOR READ
   OPENFILE F2 FOR APPEND
   WHILE NOT EOF(F1)
      READFILE F1, Line
      Line ← DeleteSpaces(Line)
      Line ← DeleteComment(Line)
      IF Line <> "" THEN
         WRITEFILE F2, Line
      ELSE
         Count ← Count + 1
      ENDIF
   ENDWHILE
   CLOSEFILE F1
   CLOSEFILE F2
   OUTPUT Count, " blank lines were removed"
ENDPROCEDURE
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure heading, parameters, ending | 首尾两行 | `module-header` |
| 2 | Open both files in correct modes and subsequently close | F1 READ、F2 APPEND，两个 CLOSEFILE | `file-open-read`、`file-append`、`file-close` |
| 3 | Loop to EOF(F1) | `WHILE NOT EOF(F1)` | `loop-to-eof` |
| 4 | Read a line from F1 in a loop | `READFILE F1, Line` | `file-open-read` |
| 5 | Assign return values from DeleteComment() and DeleteSpaces() in a loop | 两句赋值调用 | `procedure-call` |
| 6 | Check return value following both MP5 function calls is not an empty string and if so write to F2 in a loop | `IF Line <> "" THEN WRITEFILE F2, Line` | `file-write`、`relational-ops` |
| 7 | Count the blank lines in a loop | ELSE 分支 `Count ← Count + 1` | `accumulator` |
| 8 | Output number of blank lines removed following a reasonable attempt after the loop | 循环后 OUTPUT | `output-format` |

MS 范例写 `OPEN F1 FOR READ`，指南写法是 `OPENFILE`。

**直观**　抄作业：一行行念原稿，先擦掉开头的空格和批注，剩下有字的才抄到新本子上，空白的就记一笔“删了几行”。

**同题 Python 版要点**
- `open(f2, "a")` 对应 APPEND；`"w"` 会清空文件。
- `file.write(line + "\n")`：`write` 不会自动换行；读进来的行要先 `rstrip("\n")`。
- 先过阶梯 **L07 E04**（追加与写入）、**E05**（过滤文件）。

```python
def stage_2(f1: str, f2: str) -> None:
    count = 0
    with open(f1) as source, open(f2, "a") as target:
        for raw in source:
            line = delete_comment(delete_spaces(raw.rstrip("\n")))
            if line != "":
                target.write(line + "\n")
            else:
                count = count + 1
    print(count, "blank lines were removed")
```

**迁移与卡点**
- **卡点**：模式。规则只有一句——**要保留原内容就 APPEND，要新建或覆盖就 WRITE，读来源就 READ**；一个文件同一时刻只用一种模式，先读后追加要先 `CLOSEFILE` 再重新打开。第二个卡点：写出去的必须是**一个字符串**——数字先 `NUM_TO_STR`，多个字段用 `&` 和分隔符拼好再写。
- **考官在换什么**：数据从哪来（另一个文件、记录数组、二维数组、键盘）、写之前做什么（调用模块处理、过滤空行、拼字段）、要不要计数。“模式正确地打开 + 之后关闭”每题都有，两个文件就是两份。
- **从代表题到变式**：代表题 Stage_2 是文件到文件（读 + 追加）；变式是记录数组到新文件（WRITE 新建）——循环从 EOF 变成 `FOR Index ← 1 TO 45`，读一行变成拼一行：`NUM_TO_STR(Character[Index].Player) & "^" & Character[Index].Role`。搬过去的是打开 / 写 / 关闭的骨架；要换的是循环头和“当前这一行从哪来”。
- **反例**：`WRITEFILE F, Player, "^", Role` 用逗号写多个值——WRITEFILE 只接一个字符串，先拼再写。

**下一道变式**　⟦9618_w24_22:8(b)⟧　（数组 → 文件：把 45 条 Character 记录各拼成一行、字段间用 '^'、数字字段先 NUM_TO_STR，写进新文件。）

<!-- auto:drills P2-DT-10 -->

### P2-DT-11　文件的用途、模式与存储格式　{#P2-DT-11}

<!-- auto:stats P2-DT-11 -->

**考法**　不写代码，问文件的概念：①用文本文件代替数组的好处（数量不受数组大小限制、永久保存）；②选文件模式并说明为什么不能用 WRITE；③写入前必须做的转换（数字 / 布尔 → 字符串）；④一行里存多项数据的格式：分隔符（选什么字符、为什么）或定长字段 / 长度前缀，以及各自的缺点；⑤一项一行 vs 一条记录一行的利弊；⑥有意义的文件名（加日期 / 序号后缀）；⑦传输时为什么用结束标记。1–3 分。

**识别信号**　Give two benefits of using a text file instead of an array；State the file mode that should be used；Explain why WRITE mode cannot be used；State any change that will need to be made before each value is written to the file；Suggest a suitable separator character；Explain how a single line of the text file can be used to store …；meaningful filename。

**解题思路**
1. **文件 vs 数组**：文件**永久保存**（程序结束、断电后还在，下次不必重新输入）；**大小不受数组声明的限制**（只受外存容量限制）。
2. **模式**：只读 → READ；新建 / 覆盖 → WRITE；在已有内容后面加 → APPEND。不能用 WRITE 的理由：会覆盖已有数据。
3. **写入前**：文本文件只存字符串 → 数字用 `NUM_TO_STR`、布尔值编码成字符 / 字符串。
4. **一行多项的两种格式**：
   - **分隔符**：逐个分隔符拆全部字段时，选一个不会出现在待拆字段里的字符；若只拆成前后两项，也可选一个不会出现在第一项里的字符，只在首次出现处拆分，后面整段作为第二项。
   - **定长 / 长度前缀**：把某个字段的长度转成**固定位数的字符串**放在行首，再接上数据；读回时先取长度再取子串。所有待分隔字段都可含任意字符、无法排除分隔符时，可用长度前缀避免歧义；仅一个字段可含任意字符不代表必须放弃分隔符。
5. **利弊**：一行一条记录 → 文件操作次数少，但拼接 / 拆分算法更复杂；一项一行 → 读写简单，但文件访问次数多。补前导零定长 → 文件变大。

**得分表述**（引自对应 MS）
- 「The data is stored permanently / non-volatile」⟦9618_w25_21:4(b)(i)⟧
- 「Each (real) value would have to be converted to a string」⟦9618_w25_21:4(b)(ii)⟧
- 「So that existing file data is not overwritten」⟦9618_w22_22:2(a)(iii)⟧
- 「It does not appear in (any of) the data items」⟦9618_w25_22:3(b)⟧
- 「Select a (separator) character that cannot occur in the domain name」⟦9618_s22_23:9(c)⟧
- 「More file accesses needed (to read / write a complete record)」⟦9618_w25_23:8(c)(iii)⟧

**易错与失分**
- 好处只写“easier”“more secure”：要写永久保存 / 不受大小限制。
- 选分隔符时没检查字段的字符范围：逗号、空格、字母或数字能否使用，要看该题限制；本卡代表题的 MS 明确允许域名后的空格。
- 把一个字段可含任意字符误当成所有字段都无法排除分隔符。本题域名不能含空格，只寻找域名后的第一个空格；密码中再出现空格不影响拆分。若所有待分隔字段均无可排除字符，才不能直接靠这种分隔符方案消除歧义。
- 长度前缀没说“固定位数”：读回时不知道长度本身占几位。
- 模式题答成 `OPEN` / `INPUT`：答 READ、WRITE、APPEND 之一。

#### 代表题精讲　⟦9618_s22_23:9(c)⟧

**在考什么**　数组 Secret 存网站域名与加密后的密码，要备份到文本文件，并能读回再拆开。两项都是长度可变的字符串，**加密密码可能包含字符集里的任何字符**。Explain how a single line of the text file can be used to store the website domain name and the encrypted password. 3 分。

**完整作答**　（两种方案任选其一，各 3 点。）
- **按字段长度**：把域名的长度转成**固定长度**的字符串（如 3 位：`"015"`），再与域名、加密密码拼接成一个字符串，作为文件的一行写入。读回时先取前 3 位得到长度，再按长度取出域名，剩下的就是密码。
- **按分隔符**：选一个不可能出现在域名里的字符（如空格）作分隔符；把域名、分隔符、加密密码拼成一行写入。读回时找第一个分隔符：前面是域名，后面全部是密码（密码里出现分隔符也不影响，因为只按第一个拆）。

**与 MS 对齐**　MS 两套方案：①「Convert the length of the website domain name (either field) …」⟦9618_s22_23:9(c)⟧ → “… to a string of fixed length” → “Form a string by concatenate this string with the other two (and write as one line of the file)”；②「Select a (separator) character that cannot occur in the domain name」⟦9618_s22_23:9(c)⟧ → “Create a string from the domain name followed by the separator” → “...Concatenate the encrypted password (and write as one line of the file)”。

**英文作答句**　Convert the length of the domain name to a string of fixed length, for example three digits. Concatenate this string with the domain name and the encrypted password to form a single string. Write this string as one line of the file.

**直观**　分隔符像在两件货物之间插一块隔板；只要第一件里不会出现隔板，找到第一块就能分开，第二件里再有隔板也不影响。长度前缀像在箱子上先写“前面这件长 15 厘米”，按长度取出即可。

**下一道变式**　⟦9618_w25_22:3(c)⟧　（两个新加密项可含任何字符、最长 99：怎样在已有的 '\' 分隔格式后面存它们。）

<!-- auto:drills P2-DT-11 -->

### P2-DT-12　ADT 的概念与选择　{#P2-DT-12}

<!-- auto:stats P2-DT-12 -->

**考法**　①“栈是一种 ADT，再举一种 ADT 并描述其主要特征”（1 + 2 分）；②描述队列的两个特征；③由图或代码识别是哪种 ADT（链表、栈、队列）并说出某过程做什么操作；④指出用栈会出什么问题（顺序反了）并建议更合适的 ADT（队列）；⑤链表相对数组的优点、缺点；⑥为应用选队列并说明理由。

**识别信号**　Abstract Data Type (ADT)；Identify one other example of an ADT and describe its main features；Describe two features of a queue；Identify the ADT；Suggest a more appropriate Abstract Data Type；Explain the advantages / disadvantages … linked list instead of an array。

**解题思路**
1. **三种 ADT 的特征**（每种背 3–4 句）：
   - **栈 Stack**：后进先出（LIFO / FILO）；只在栈顶操作：PUSH 加入、POP 取出；一个栈顶指针。
   - **队列 Queue**：先进先出（FIFO）；从队尾加入、从队首取出；队首、队尾两个指针；可以是循环队列。
   - **链表 Linked list**：每个结点有数据和指向下一个结点的指针；有起始指针；最后一个结点是空指针；插入删除只改指针、不移动数据；未用结点在空闲表（free list）上。
2. **识别**：只在一端进出 → 栈；一端进另一端出 → 队列；有“数据 + 指针”两列、靠指针串起来 → 链表。
3. **选择**：要保持原来顺序（打印任务、消息、读入的文件行）→ 队列；要倒序 / 撤销 / 返回上一步 → 栈；要经常在中间插入删除并保持有序 → 链表。
4. **链表 vs 数组**：优点——顺序由指针决定，插入删除只改指针，不必移动数据；缺点——要额外存指针，实现更复杂。

**得分表述**（引自对应 MS）
- 「Data is added at back / end and removed from front / start // works on a FIFO basis」⟦9618_w22_22:3(a)⟧
- 「Each node contains data and a pointer to the next node」⟦9618_w22_22:3(a)⟧
- 「Data may be added / removed by manipulating pointers (not moving data)」⟦9618_w22_22:3(a)⟧
- 「Two pointers needed to indicate the start and end of the queue」⟦9618_s25_23:2(c)⟧
- 「The stack operates as a FILO device」⟦9618_w23_22:8(c)(i)⟧
- 「Need to store pointers as well as data」⟦9618_w22_21:4(a)(iii)⟧

**易错与失分**
- 题目说“栈之外”还答栈；或答“数组”“记录”（不是 ADT）。
- 特征只写名字的直译（“queue is a queue”）：要写 FIFO + 两个指针 + 从哪端进出。
- 把 FIFO / LIFO 写反。
- 描述特征写了 3 条，其中两条是同一个意思（“first in first out”“the first item added leaves first”）。

#### 代表题精讲　⟦9618_w22_22:3(a)⟧

**在考什么**　程序用一个栈存几个模块要访问的字符串数据。A stack is an example of an Abstract Data Type (ADT). Identify one other example of an ADT and describe its main features. 3 分 = 名称 1 + 特征 2。

**完整作答**　ADT：队列（queue）。特征：①数据从队尾加入、从队首取出，先进先出（FIFO）；②有一个指向队首的指针和一个指向队尾的指针；③（保险）队列可以是循环的，指针到数组末尾后绕回开头。

**与 MS 对齐**　名称 ← “Name: Queue”；特征 ←「Data is added at back / end and removed from front / start // works on a FIFO basis」⟦9618_w22_22:3(a)⟧、“A Pointer to the front / start of the queue”“A Pointer to the back / end of the queue”“May be circular”。MS 也接受链表：「Each node contains data and a pointer to the next node」⟦9618_w22_22:3(a)⟧ 等。

**英文作答句**　Example: a queue. Features: data is added at the back and removed from the front, so it works on a FIFO basis; there is a pointer to the front of the queue and a pointer to the back of the queue; it may be circular.

**直观**　栈是一摞盘子（最后放上的先拿走）；队列是食堂排队（先来的先打饭）；链表是寻宝游戏（每张纸条写着下一张在哪）。

**下一道变式**　⟦9618_w23_22:8(c)(i)⟧　（反过来用：解释把文件各行先存进栈再取出会出什么问题——顺序反了。）

<!-- auto:drills P2-DT-12 -->

### P2-DT-13　栈的操作与状态　{#P2-DT-13}

<!-- auto:stats P2-DT-13 -->

**考法**　给出用一段内存（或数组）实现的栈的当前状态图（地址、值、TopOfStack 指针），①执行一串 PUSH / POP 后画出新状态和指针（3–5 分）；②回答在栈里最久的值、连续 POP 几次会出错、连续 PUSH 几次指针到某地址；③POP 出的值存进变量，最后写出变量的值；④两个栈配合（浏览器后退 / 前进栈）。

**识别信号**　The following diagram shows the current state of the stack；TopOfStack / Stack Pointer / Memory location；Complete the diagram to show the state of the stack after the following operations；the value that has been on the stack for the longest time；maximum number of consecutive POP operations。

**解题思路**
1. **先看栈往哪个方向长**：TopOfStack 指着最后加入的值；栈底那一端的值从没动过。地址往小长（栈底在 207，顶在 202）或往大长（栈底在 400）都有。
2. **逐个操作走一遍**，在草稿上记“指针 + 栈顶值”：
   - `POP`：取出指针所指的值（存进变量或丢弃），指针向栈底方向退一格。
   - `PUSH x`：指针向栈顶方向进一格，把 x 写进那一格。
3. **被 POP 掉、之后没有被新值覆盖的格子**：画成空最稳（POP 以后那格的内容已经不属于栈）；新 PUSH 的值覆盖原来的格子。
4. **画最终图**：每个地址写值；指针箭头指到最终栈顶；没动过的值原样抄下来。
5. **最久的值** = 栈底的值；**最多连续 POP 次数** = 栈里值的个数。

**得分表述**（引自对应 MS）
- 「TopOfStack pointing to 'D'」⟦9618_s22_21:4(b)⟧
- 「Values 'X' to 'P' unchanged (204 to 207)」⟦9618_s22_21:4(b)⟧
- 「Values 'D' to 'F' unchanged in 400 to 405 and 409 is empty」⟦9618_s25_23:2(a)(ii)⟧
- 「Both pointers and labelled」⟦9618_s23_23:3(a)(ii)⟧

**易错与失分**
- 指针方向弄反：先确认 PUSH 时地址是变大还是变小。
- POP 之后忘了把指针退回，接着 PUSH 写到了错误的格子。
- 没动过的栈底值漏抄：MS 单独给一分“unchanged”。
- 指针没标名字（TopOfStack / BottomOfStack）。
- POP 出的值没有写进题目要求的变量。

#### 代表题精讲　⟦9618_s22_21:4(b)⟧

**在考什么**　栈占用内存 200–207；当前：202 'W'（TopOfStack）、203 'Y'、204 'X'、205 'Z'、206 'N'、207 'P'（栈往小地址长）。依次执行：POP、POP、PUSH 'A'、PUSH 'B'、POP、PUSH 'C'、PUSH 'D'。Complete the diagram to show the state of the stack after the operations have been performed. 4 分。

**完整作答**　逐步：

| 操作 | 指针 | 栈顶值 |
|:--|:--|:--|
| 开始 | 202 | 'W' |
| POP（取出 W） | 203 | 'Y' |
| POP（取出 Y） | 204 | 'X' |
| PUSH 'A' | 203 | 'A' |
| PUSH 'B' | 202 | 'B' |
| POP（取出 B） | 203 | 'A' |
| PUSH 'C' | 202 | 'C' |
| PUSH 'D' | 201 | 'D' |

最终图：200 空；201 'D' ← TopOfStack；202 'C'；203 'A'；204 'X'；205 'Z'；206 'N'；207 'P'。

**与 MS 对齐**　四点：「TopOfStack pointing to 'D'」⟦9618_s22_21:4(b)⟧；“Value 'D' in 201”；“Values 'C' & 'A' in 202 and 203”；「Values 'X' to 'P' unchanged (204 to 207)」⟦9618_s22_21:4(b)⟧。

**英文作答句**　（本题答案即最终状态图。）

**直观**　往一摞书上拿放：拿走两本，放上 A、B，拿走 B，再放 C、D——最上面是 D，压在最底下的 P、N、Z、X 一直没动。

**下一道变式**　⟦9618_s25_23:2(a)(ii)⟧　（栈往大地址长：从 407 'A' 开始执行 PUSH 'T'、POP、POP、PUSH 'Z'、PUSH 'X'、POP、PUSH 'Y'。）

<!-- auto:drills P2-DT-13 -->

### P2-DT-14　队列的操作与状态　{#P2-DT-14}

<!-- auto:stats P2-DT-14 -->

**考法**　①在给定（循环）队列上描述加入两个数据项的过程，包括满检查和指针绕回（4 分）；②执行若干次入队 / 出队后画出新状态和队首、队尾指针（2–3 分）；③按描述画出队列状态（数组 + FrontOfQueue、EndOfQueue、NumItems）；④描述实现队列要的两个操作及各自的检查（不满 / 不空）；⑤说出队里有几个数据项；⑥两个指针相等表示什么。

**识别信号**　queue；Front of Queue Pointer / End of Queue Pointer (FoQ / EoQ)；The queue is circular so that locations can be reused；Describe how … are added to the queue；Complete the diagram to show the state of the queue after the following operations；State the check that must be carried out。

**解题思路**
1. **先读清指针的约定**：FoQ 指“下一个要取出的”；EoQ 指“最后加入的”（也有题目约定指下一个空位，照题目）。
2. **入队**：①检查队列不满；②EoQ 前进一格（到数组末尾就绕回第一格）；③把数据存进 EoQ 指的位置；④（有计数器时）NumItems 加 1。
3. **出队**：①检查队列不空；②取出 FoQ 指的值；③FoQ 前进一格（必要时绕回）；④NumItems 减 1。
4. **绕回**：位置 0–9 的队列，EoQ 在 9 时下一格是 0；位置 1–8 的，在 8 时下一格是 1。
5. **数据项个数**：仅在 FoQ 指首项、EoQ 指末项且队列非空的约定下，从 FoQ 数到 EoQ（跨过末尾就加上绕回的那段），两者相等表示只有一个数据项。空 / 满状态须结合该题初值、计数器或留空位规则判断，不能只看指针是否相等。

**得分表述**（引自对应 MS）
- 「Check that the queue is not full」⟦9618_s23_22:3(a)(i)⟧
- 「Data item Orange will be stored in location referenced by EoQ pointer」⟦9618_s23_22:3(a)(i)⟧
- 「EoQ pointer will move to point to location 0」⟦9618_s23_22:3(a)(i)⟧
- 「Check: There are items in the array // The queue is not empty」⟦9618_w22_23:4(b)(i)⟧
- 「FoQ value matches index with D3」⟦9618_w23_23:3(a)⟧
- 「There is only one data item in the queue」⟦9618_w21_21:3(a)(iii)⟧（限该题 FoQ 指首项、EoQ 指末项的非空队列情境，不是所有队列的相等判据。）

**易错与失分**
- 漏了“先检查不满 / 不空”这一分。
- 先存数据再移动 EoQ：覆盖了最后一个数据项（按题目约定的指针含义来定顺序）。
- 到末尾不绕回，写“位置 10”。
- 出队后把旧值“删除”或把后面的数据往前挪：队列只移动指针，不移动数据。
- FoQ 和 EoQ 两个指针只画了一个。

#### 代表题精讲　⟦9618_s23_22:3(a)(i)⟧

**在考什么**　程序从文本文件读数据放进循环队列，位置 0–9，最多 10 项。FoQ 指下一个要取出的数据项，EoQ 指最后加入的数据项。当前：5 Red（FoQ）、6 Green、7 Blue、8 Pink（EoQ）。Describe how the data items Orange and Yellow are added to the queue shown in the diagram. 4 分，MS 列 5 点。

**完整作答**
1. 检查队列不满（现在只有 4 项）。
2. EoQ 指针移到位置 9。
3. 把 Orange 存进 EoQ 所指的位置（9）。
4. EoQ 指针移到下一个位置——队列是循环的，从 9 绕回位置 0。
5. 把 Yellow 存进 EoQ 所指的位置（0）。

**与 MS 对齐**　五步依次对应 MS 1–5：「Check that the queue is not full」⟦9618_s23_22:3(a)(i)⟧ → “EoQ pointer will move to point to location 9” → 「Data item Orange will be stored in location referenced by EoQ pointer」⟦9618_s23_22:3(a)(i)⟧ → 「EoQ pointer will move to point to location 0」⟦9618_s23_22:3(a)(i)⟧ → “Data item Yellow will be stored in location referenced by EoQ pointer”。Max 4。

**英文作答句**　1 Check that the queue is not full. 2 The EoQ pointer moves to point to location 9. 3 Orange is stored in the location referenced by the EoQ pointer. 4 The EoQ pointer wraps round to point to location 0. 5 Yellow is stored in the location referenced by the EoQ pointer.

**直观**　圆桌排队：队尾的人坐到 9 号椅子，下一个人没有 10 号椅子，就坐回 0 号——桌子是圆的。

**下一道变式**　⟦9618_w23_23:3(a)⟧　（按文字描述把 D3、D4、D1、D2、D5 画进 8 格数组，并填 FrontOfQueue、EndOfQueue 的值；讲解时请对照原卷 QP p.6。）

<!-- auto:drills P2-DT-14 -->

### P2-DT-15　链表的操作与状态　{#P2-DT-15}

<!-- auto:stats P2-DT-15 -->

**考法**　①在链表图上加入、删除结点后画出新状态（起始指针、各结点指针、空指针），4 分；②补全插入结点的步骤（用空闲表的第一个结点、改两个指针、移动空闲表指针）；③由数据与指针两列补全指针域，使链表按字母顺序；给出起始指针的值；④描述初始化后、加入数据前的链表；⑤术语：起始指针、空指针及其含义；⑥（2021 扩展）解释怎样按字母顺序加入一个结点。

**识别信号**　linked list；start pointer / Ptr1；free list pointer / Ptr2；null pointer Ø；Complete the pointer field to produce a linked list that is in alphabetical order；Nodes with data … are added … Nodes … are deleted；Complete the steps。

**解题思路**
1. **认清两个链**：数据链（起始指针 → … → 空指针）和空闲链（空闲指针 → 未用结点 → … → 空指针）。
2. **插入**一个结点（在 P 与 Q 之间）：
   1. 取空闲表的第一个结点，把数据存进去；
   2. 新结点的指针指向 Q（**先连后面**，不然 Q 就找不到了）；
   3. 空闲指针移到空闲表的下一个结点；
   4. P 的指针改为指向新结点。
   插在最前面时，改的是**起始指针**；插在最后时，新结点的指针是空指针。
3. **删除**结点 Q（P → Q → R）：P 的指针改为指向 R；Q 放回空闲表。删的是第一个结点时，改起始指针。
4. **补全指针域**：先按要求的顺序（字母序）排出各结点，起始指针 = 第一个结点的下标；每个结点的指针 = 下一个结点的下标；最后一个写空指针（题目约定 −1 或 0）。
5. **初始化**：起始指针为空指针；空闲指针指向第一个元素；所有结点都在空闲表上。

**得分表述**（引自对应 MS）
- 「Set Ptr2 to point to F2」⟦9618_w23_22:3(b)⟧
- 「Set pointer of D32 to point to D6」⟦9618_w23_22:3(b)⟧
- 「Start pointer points to Node A」⟦9618_w22_21:4(a)(i)⟧
- 「Node K contains Null Pointer」⟦9618_w22_21:4(a)(i)⟧
- 「The PS contains a null pointer」⟦9618_s24_21:3(a)⟧
- 「All the nodes are on the free list」⟦9618_s24_21:3(a)⟧

**易错与失分**
- 先改 P 的指针再连新结点：原来 P 后面的结点丢了。
- 插在最前面却没改起始指针。
- 删除时把后面的数据往前挪：链表只改指针。
- 最后一个结点的指针没写空指针，或写成自己的下标。
- 用了空闲结点却没移动空闲指针。
- 写成代码时，F1 原来的指针正指着 F2：要先把空闲指针移到 F2（或先记下 F2），再改 F1 的指针，否则空闲表就断了。

#### 代表题精讲　⟦9618_w23_22:3(b)⟧

**在考什么**　链表：Ptr1（起始指针）→ D40 → D32 → D11 → D100 → Ø；空闲表：Ptr2 → F1 → F2 → F3 → F4 → Ø。要在 D32 与 D11 之间插入新结点 D6。The algorithm required is expressed in four steps. Complete the steps. 4 分。讲解时请对照原卷 QP p.7（看箭头）。

**完整作答**
1. Assign the data item **D6** to **F1**.
2. Set the **pointer** of this node to point to **D11**.
3. Set Ptr2 to point to **F2**.
4. Set pointer of **D32** to point to **D6**.

**与 MS 对齐**　四步依次对应 MS：“Assign the data item D6 to F1”“Set the pointer of this node to point to D11”「Set Ptr2 to point to F2」⟦9618_w23_22:3(b)⟧「Set pointer of D32 to point to D6」⟦9618_w23_22:3(b)⟧。

**英文作答句**　（本题答案即上面四步。）

**直观**　在一串手拉手的人里插进一个新人：新人先拉住 D11 的手，D32 再松开 D11 去拉新人——顺序反了，D11 后面那一串就走散了。

**下一道变式**　⟦9618_s25_23:2(b)(i)⟧　（按字母顺序补全 6 个行星结点的指针域，−1 表示链表结尾。）

<!-- auto:drills P2-DT-15 -->

### P2-DT-16　用数组实现栈、队列与链表　{#P2-DT-16}

<!-- auto:stats P2-DT-16 -->

**考法**　①补全 Push() / Pop() 的伪代码（按空计分，4–5 分）；②写声明语句与 InitialiseQueue() 过程；③给出栈指针等变量的初值、说明为什么不必初始化数组元素；④用文字补全 Push() 的五步或循环队列 AddTo() 的六步；⑤描述怎样用数组和变量实现栈、队列、链表（声明、初始化，4–5 分）；⑥补全链表初始化的流程图（每个结点指向下一个，最后一个为空指针）；⑦空指针选 0 的原因、头指针的取值范围。

**识别信号**　The stack is implemented using two integer variables and a 1D array；Explain how the stack can be implemented using an array；Describe the declaration and initialisation of the variables and data structures used to implement the queue；A function Push() / AddTo() … will add a value；The design uses two variables and two 1D arrays to implement the linked list。

**解题思路**
1. **先抄出题目的指针约定**——这是本型最容易丢分的地方：
   - 栈指针指“最后一个值”（`TopOfStack`，空栈为 0）还是“下一个空位”（`SP`，空栈为 1）？
   - 队列的 EndOfQueue 指最后一个值还是下一个空位？有没有 NumItems？
   - 链表的空指针是 0 还是 −1？
2. **入栈 / 入队**：先检查**满**→ 满了就返回 FALSE（或报错）；否则按约定移动指针、存值（或先存值再移动）、计数加 1、返回 TRUE。
3. **出栈 / 出队**：先检查**空**→ 空了返回 FALSE 或标记；否则取值、移动指针、计数减 1。
4. **循环队列的绕回**：指针加 1 后若超过上界，回到下界。
5. **描述实现**：一个（或两个）一维数组存数据（链表另一个存指针，或用记录数组）；整数变量作指针（栈顶 / 队首、队尾 / 起始、空闲）；常量或变量记最大容量；初值表示空结构；需要入、出、查找等子程序。

**伪代码模板**

```pseudocode
// stack: SP points to the NEXT FREE location, OnStack counts the values (as in w24/22)
FUNCTION Push(ThisValue : REAL) RETURNS BOOLEAN
   IF OnStack = 60 THEN
      RETURN FALSE                    // stack is already full
   ENDIF
   ThisStack[SP] ← ThisValue          // store first, then move the pointer
   SP ← SP + 1
   OnStack ← OnStack + 1
   RETURN TRUE
ENDFUNCTION

// circular queue on ARRAY[1:8]: EndOfQueue points to the LAST value added
FUNCTION AddTo(Item : STRING) RETURNS BOOLEAN
   IF NumItems = 8 THEN
      RETURN FALSE                    // queue is full
   ENDIF
   EndOfQueue ← EndOfQueue + 1        // move first, then store
   IF EndOfQueue = 9 THEN
      EndOfQueue ← 1                  // wrap round
   ENDIF
   Queue[EndOfQueue] ← Item
   NumItems ← NumItems + 1
   RETURN TRUE
ENDFUNCTION

// linked list on ARRAY[1:200] OF Node: every node points to the next, the last holds 0
PROCEDURE InitialiseList()
   DECLARE Index : INTEGER
   FOR Index ← 1 TO 199
      List[Index].Pointer ← Index + 1
   NEXT Index
   List[200].Pointer ← 0              // null pointer
   HeadPointer ← 0                    // empty data list
   FreePointer ← 1                    // all nodes are on the free list
ENDPROCEDURE
```

**得分表述**（引自对应 MS）
- 「If TopOfStack = 8 // (stack) full then return FALSE」⟦9618_w23_21:3(b)⟧
- 「Use TopOfStack as an index to the Array」⟦9618_w23_21:3(b)⟧
- 「If EndOfQueue = 9 then set EndOfQueue to 1」⟦9618_w23_23:3(b)⟧
- 「Declare an integer / variable for StackPointer」⟦9618_w22_22:3(b)⟧
- 「Declare two (1D) arrays」⟦9618_w22_21:4(b)⟧
- 「Unused values cannot be popped / taken off the stack」⟦9618_w24_22:3(a)(ii)⟧

**得分点地图**（本型多数按空或按步计分、未拆得分点；下表据核验语料中 6 道写代码 / 补步骤题的 MS 计分清单整理：w24/22 Q3(b)、w25/23 Q3、w23/21 Q3(b)、w23/23 Q3(b)、w24/23 Q3(b)、s26/21 Q7(c)）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 操作前检查满 / 空，不行就返回 FALSE | 4 | `stack-array` / `queue-array`、`boolean-return` |
| 按约定移动指针（加 1 / 减 1） | 4 | `stack-array` / `queue-array` |
| 用指针作下标存值 / 取值 | 4 | `array-index` |
| 成功 / 失败时返回 TRUE / FALSE（或标记取出是否成功） | 2 | `boolean-return` |
| 计数变量（NumItems、OnStack）同步加减 | 1 | `queue-array`、`stack-array` |
| 循环队列绕回 | 1 | `queue-array` |
| 初始化：循环给每个结点 / 元素赋值，最后一个为空指针 | 2 | `linked-list`、`count-loop`、`initialise-variables` |

**易错与失分**
- 把 L08 的“TopPointer 指最后一个值”习惯带进“SP 指下一个空位”的题：先移动还是先存，顺序就反了。
- 满检查写成 `SP = 60`（SP 指下一个空位时，满是 61 或 OnStack = 60）。
- 循环队列忘了绕回，或绕回写成 `EndOfQueue ← 0`（数组下界是 1）。
- 函数里用 `OUTPUT "Stack full"` 代替返回 FALSE。
- 描述实现只写“use an array”：要写数组的类型与大小、指针变量（整数）、初值表示空。

#### 代表题精讲　⟦9618_w24_22:3(b)⟧

**在考什么**　栈最多 60 个数值：`DECLARE ThisStack : ARRAY[1:60] OF REAL`；全局 SP 指**下一个可用位置**；全局 OnStack 是栈里值的个数；栈从下标 1 往上长。补全 Push() 的 4 个空：

```pseudocode
FUNCTION Push(ThisValue : REAL) RETURNS BOOLEAN
   DECLARE ReturnValue : BOOLEAN
   IF ………… THEN
      RETURN ………… // stack is already full
   ENDIF
   ………… ThisValue
   SP …………
   OnStack ← OnStack + 1
   RETURN TRUE
ENDFUNCTION
```

4 分，每空 1 分。

**完整作答**

```pseudocode
FUNCTION Push(ThisValue : REAL) RETURNS BOOLEAN
   DECLARE ReturnValue : BOOLEAN
   IF OnStack = 60 THEN
      RETURN FALSE // stack is already full
   ENDIF
   ThisStack[SP] ← ThisValue
   SP ← SP + 1
   OnStack ← OnStack + 1
   RETURN TRUE
ENDFUNCTION
```

**与 MS 对齐**　MS 逐空：条件 “OnStack = 60 / >59 // SP = 61 / SP > 60 // SP outside the range 1 to 60”；“RETURN FALSE”；“ThisStack[SP] ← ThisValue”；“SP ← SP + 1”；One mark per gap。因为 SP 指的是**下一个空位**，所以先存值、再把 SP 加 1。同一题 (a)(i)：初值 SP 为 1、OnStack 为 0。

**直观**　SP 像“下一个空停车位”的指示牌：车先停进指示的位置，再把牌子往后挪一格；停满 60 辆就不放行。

**同题 Python 版要点**
- 全局变量在函数里要改（`sp = sp + 1`）就必须先写 `global sp, on_stack`；只改列表元素不需要。
- Python 列表下标 0–59：SP 的初值相应为 0，满的条件仍是 `on_stack == 60`。
- 先过阶梯 **L08 E03**（数组栈）、**E04**（循环队列）；链表初始化见 **L10**。

```python
this_stack = [0.0] * 60
sp = 0           # next free location (0-based)
on_stack = 0

def push(this_value: float) -> bool:
    global sp, on_stack
    if on_stack == 60:
        return False
    this_stack[sp] = this_value
    sp = sp + 1
    on_stack = on_stack + 1
    return True
```

**下一道变式**　⟦9618_w23_23:3(b)⟧　（循环队列 AddTo() 的六步：满检查 → EndOfQueue 加 1 → 等于 9 时置 1 → NumItems 加 1 → 存值。）

<!-- auto:drills P2-DT-16 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| DT-01 vs DT-02 | 只填类型 → DT-01；写出 TYPE … ENDTYPE → DT-02 | 表格还是记录定义 |
| DT-02 vs DT-03 | 定义记录类型 → DT-02；声明“记录数组”那一句 `DECLARE … : ARRAY … OF 类型` → DT-03 | TYPE 还是 DECLARE … ARRAY |
| DT-03 vs DT-04 | 写声明、回答下标 / 上下界 / 未用元素 → DT-03；说明为什么用数组 / 记录 → DT-04 | declare / bound 还是benefit / why |
| DT-05 vs DT-06 vs DT-07 | 一维数组（含并行数组）→ DT-05；二维 `[Row, Col]` → DT-06；元素是记录、用点号 → DT-07 | 访问元素的写法 |
| DT-05 vs DT-08 | 只查找、计数、找空位 → DT-05；要排序 → DT-08 | sort / bubble |
| DT-09 vs DT-10 | 只读 → DT-09；有 WRITEFILE（写新文件、追加、复制）→ DT-10 | 有没有写 |
| DT-09 / DT-10 vs DT-11 | 写读写文件的代码 → DT-09 / DT-10；只问用途、模式、格式 → DT-11 | Write pseudocode 还是 state / explain |
| DT-04 vs DT-11 vs DT-12 | 内存里的结构（数组、记录）→ DT-04；文件或文件里的格式 → DT-11；栈 / 队列 / 链表 → DT-12 | 选的是什么 |
| DT-12 vs DT-13 / 14 / 15 | 特征、识别、选择 → DT-12；在状态图上做操作 → DT-13（栈）/ DT-14（队列）/ DT-15（链表） | describe features 还是 complete the diagram |
| DT-14 vs DT-16 | 描述入队出队及满 / 空检查 → DT-14；描述实现队列要声明与初始化什么、写 AddTo 代码 → DT-16 | operations / check 还是 declaration / initialisation / pseudocode |
| WRITE vs APPEND | 新建或覆盖 → WRITE；保留原内容并在末尾追加 → APPEND | 是否需要保留原内容 |
| 栈指针的两种约定 | 指最后一个值（空栈 0，先加 1 再存）/ 指下一个空位（空栈 1，先存再加 1） | 题干怎样定义指针 |
| LIFO vs FIFO | 栈：后进先出；队列：先进先出 | stack 还是 queue |
