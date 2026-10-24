## DR　数据表示 {#ch-DR}

<!-- auto:chapter-stats -->

### 核心思想

DR 对应考纲 13.1–13.3，是 P3 每卷开头的两三道题，三块互不相干，各有一套固定写法：

1. **用户定义类型**（DR-01 至 DR-05，考纲 13.1）：语言自带的类型不够用时，程序员自己造类型。先分清两大类——**非组合（non-composite）**：枚举、指针，定义里不引用别的类型；**组合（composite）**：记录、集合、类 / 对象，由别的类型拼成、放在一个名字下。题目要么用文字问（DR-01），要么要你按伪代码指南写出 `TYPE` 语句（DR-02 枚举 / 指针、DR-03 记录、DR-05 集合），要么在记录变量上赋值（DR-04）。写代码的四型几乎是送分题，丢分全在格式：`TYPE` 不是 `DECLARE`，枚举值不加引号，`ENDTYPE` 不能漏。
2. **文件组织与存取**（DR-06 至 DR-08，考纲 13.2）：先分**组织**（记录在文件里怎样排：串行 serial 按到达先后、顺序 sequential 按键字段、随机 random 按散列地址），再分**存取**（怎样找到一条记录：顺序存取从头逐条比，直接存取用索引或散列一步到位），最后是**散列**本身（算地址、冲突怎样处理）。描述题永远要说“**记录**（records）怎样……”，不是“文件怎样……”。
3. **浮点数**（DR-09 至 DR-12，考纲 13.3）：尾数（mantissa）和阶码（exponent）都是**补码**。四个方向：位串 → 十进制（DR-09）、十进制 → 规格化位串（DR-10）、二进制 / 未规格化 → 规格化与最大最小值（DR-11）、用文字解释精度 / 范围 / 舍入 / 上溢下溢（DR-12）。计算题 MS 永远是“过程分 + 答案分”，**过程必须写出来**。

**浮点速查**（全章计算的地基）

| 要点 | 内容 |
|:--|:--|
| 尾数的权 | 二进制小数点紧跟在最高位（符号位）后面：`a.bcd…` 的权依次是 −1、1/2、1/4、1/8 …… |
| 阶码 | n 位补码整数，范围 −2ⁿ⁻¹ 至 2ⁿ⁻¹−1（4 位：−8 至 7；6 位：−32 至 31；8 位：−128 至 127） |
| 数值 | 尾数 × 2^阶码：阶码为 +k 就把小数点右移 k 位，为 −k 就左移 k 位 |
| 规格化 | 正数尾数以 `01` 开头，负数尾数以 `10` 开头（前两位不同） |
| 最大正数 | 尾数 `0111…1`、阶码取最大正值 `0111…1` |
| 最负的数 | 尾数 `1000…0`（= −1）、阶码取最大正值 |
| 负数的补码 | 先写正数的二进制（前面补 0 作符号位），按位取反再在最低位加 1；或直接用“最高位为负权”凑出 |

### 题型树
<!-- auto:type-tree -->

### P3-DR-01　用户定义类型的概念与分类　{#P3-DR-01}

<!-- auto:stats P3-DR-01 -->

**考法**　只用文字回答，不写声明：①说明为什么需要用户定义类型；②解释组合与非组合类型（常两边各 Max 2）；③描述枚举、指针（各 Max 2）或描述集合、记录（Max 3）；④列出另外两种组合类型；⑤说出枚举值列表的特征；⑥在给定记录里挑一个适合改成枚举的字段并给理由。1–4 分。

**识别信号**　Describe the purpose of a user-defined data type；Explain what is meant by non-composite and composite data types；Describe what is meant by enumerated and pointer data types；Describe the user-defined data type set / record；Identify two other types of composite user-defined data types；Identify one field … that could be an efficient enumerated data type。

**解题思路**
1. **先定大类**：枚举、指针 → 非组合；记录、集合、类 / 对象 → 组合。描述某一种类型时，第一句先写出它属于哪一类：“A user-defined non-composite data type …”。
2. **再写本类型独有的特征**（这是第二、三分）：
   - 枚举：一个**有序的、列出全部可能值的**列表（ordered list of all possible values）。
   - 指针：存的是**内存地址**，并说明该地址里存的数据是什么类型。
   - 记录：由其他数据类型组成的单个新类型；包含固定数量的相关数据项；成员可以是基本类型，也可以是别的用户定义类型。
   - 集合：组合类型；元素无序；可做交集、并集等集合运算；定义里写明元素的数据类型，所有元素同类型。
3. **组合 vs 非组合**：组合类型在定义里引用其他数据类型（由多个元素组成，放在一个标识符下）；非组合类型定义时不引用其他数据类型。两者都可以是用户定义的或语言内置的。
4. **“为什么需要”**：语言里没有程序需要的类型 → 自己构造 / 扩展已有类型 → 正好符合程序需求、代码更易读。
5. **挑枚举字段**：找取值是**固定的几种**的字段（格式、颜色、等级），理由写“只有固定范围的可能值”；姓名、编号、日期、数量都不行。

**得分表述**（引自对应 MS）
- 「A (user-defined non-composite) data type with an ordered list of possible values」⟦9618_w22_31:3(a)⟧
- 「A user-defined non-composite data type used to reference a memory location」⟦9618_w22_31:3(b)⟧
- 「Composite data types refer to other data types in their definition/contain more than one data type in their definition」⟦9618_s24_31:3(a)⟧
- 「A data type that is defined without referencing another data type」⟦9618_s24_32:3(a)⟧
- 「Set theory operations, such as intersection and union, can be applied to these elements」⟦9618_w24_31:6(a)⟧
- 「This field can have a fixed range of possible values」⟦9618_s25_33:1(b)⟧

**易错与失分**
- 用名字解释名字：“a pointer data type points to a memory location”不够。考官报告指出这样写没有说明 point 的含义，要写“stores / references a memory address”（⟦9618_w23_31:3⟧ 的考官报告）。
- 枚举只写“a list of values”：漏了 ordered、all possible values 这两个限定词，只得“非组合”那一分。考官报告也指出要写出枚举独有的“ordered list of possible values”（⟦9618_w22_31:3(a)⟧ 的考官报告）。
- 两种类型一起问时，“user-defined non-composite”往往**只给一次**（MS 写 only award once），另一种类型必须靠自己的特征拿满。
- 把组合类型说成“只能是用户定义的”：MS 明说组合、非组合都可以是用户定义的或内置的（⟦9618_s24_31:3(a)⟧ 的 MP1、MP4）。
- “另外两种组合类型”题干已给了 record，再写 record 不得分；写 array 也不在该题 MS 的答案里（MS 列的是 set、class / object）。

#### 代表题精讲　⟦9618_w23_31:3⟧

**在考什么**　Describe what is meant by enumerated and pointer data types. 4 分：枚举 Max 2、指针 Max 2。MS 在两边都列了“A user-defined non-composite (data type)”，并注明 **only award once**——这一点全题只给一次。

**完整作答**
- Enumerated：枚举是用户定义的非组合数据类型，它给出一个列出全部可能值的列表，而且这些值是有序的。
- Pointer：指针类型的变量只存内存地址；定义时还指明该地址里存放的数据是什么类型。

**与 MS 对齐**　枚举两句对应 MP1（user-defined non-composite）、MP2（list of all possible values）、MP3（ordered），三点取 2；指针因为 MP4 与 MP1 只算一次，要靠 MP5「…that stores addresses/memory locations only」⟦9618_w23_31:3⟧ 和 MP6「…and indicates the type of data stored in the memory location」⟦9618_w23_31:3⟧ 拿满 2 分。所以指针那一栏不要只写“also user-defined non-composite”。

**英文作答句**　Enumerated: a user-defined non-composite data type with a list of all possible values, which is ordered. Pointer: a data type that stores memory addresses only, and indicates the type of data stored in the memory location it references.

**直观**　枚举像点餐单上的固定选项（小、中、大，有先后）；指针像一张写着门牌号的纸条——纸条上不是东西本身，而是东西放在哪里，纸条上还注明“这间房放的是 STRING”。

**迁移与卡点**
- **卡点**：“user-defined non-composite”这一分在同一题里只给一次，所以第二种类型必须靠它**独有**的特征拿分（枚举：ordered、all possible values；指针：stores a memory address + 指明所指数据的类型）。
- **考官在换什么**：问哪两种类型、问大类（组合 / 非组合）还是具体类型、问目的、挑枚举字段。每种类型都是“大类一句 + 独有特征两句”。
- **从代表题到变式**：代表题是两种具体类型；变式是组合 vs 非组合两个大类——每边写“定义（引用 / 不引用别的类型）+ 可以是用户定义的也可以是内置的 + 举例”。搬过去的是“分类句 + 特征句”的形状；要换的是层级（从具体类型上升到大类）。
- **反例**：用名字解释名字（a pointer points to …）；把组合类型说成只能是用户定义的。

**下一道变式**　⟦9618_s24_31:3(a)⟧　（换成组合 vs 非组合：两边各 Max 2，每边要写“是什么 + 可以是用户定义或内置 + 举例”。）

<!-- auto:drills P3-DR-01 -->

### P3-DR-02　声明与使用枚举类型和指针类型　{#P3-DR-02}

<!-- auto:stats P3-DR-02 -->

**考法**　①按给出的值写枚举类型声明（2 分：`TYPE 名 =` 一分、括号里的值列表一分）；②写指针类型声明（2 分：`TYPE 名 =` 一分、`^类型` 一分）；③记录里某字段改用这个枚举类型，写出替换后的那一行 `DECLARE 字段 : 枚举类型名`（1 分）。常和 DR-03、DR-04 在同一大题。

**识别信号**　Write pseudocode to create an enumerated type called …；Write the pseudocode statement to declare a non-composite data type … that holds the following data；Write pseudocode to create a pointer type …；Write the new pseudocode statement required to replace / update the declaration of … in the definition of …。

**解题思路**
1. **枚举**：`TYPE <类型名> = (值1, 值2, …)`。关键字是 `TYPE`，有等号，值放在圆括号里、逗号分隔，**每个值不加引号**，顺序照题目抄。
2. **指针**：`TYPE <类型名> = ^<被指向的类型>`。`^` 写在类型名前面；被指向的类型可以是 STRING、INTEGER，也可以是前面定义的枚举类型。
3. **改字段类型**：只写一行 `DECLARE <字段名> : <新类型名>`，字段名照原记录、类型名用新定义的枚举名。
4. 类型名、值、字段名一律照题目拼写；题目没给类型名时自己起一个有意义的（`TPrime`、`TDayPointer`）。

**伪代码模板**

```pseudocode
// enumerated type: values are identifiers, not strings
TYPE Activity = (Badminton, Football, Golf, Snooker, Swimming, Tennis)

// pointer type: ^ followed by the type of the data pointed to
TYPE TDayPointer = ^STRING

// a field of a record changed to the enumerated type
DECLARE Choice : Activity

// using them (guide 2027-29, User-defined data types)
DECLARE ThisActivity : Activity
DECLARE MyPointer : TDayPointer          // no ^ in the variable declaration
ThisActivity ← Golf                      // no quotes around an enumerated value
```

**得分表述**（引自对应 MS）
- 「TYPE Activity=」⟦9618_w25_31:1(b)(i)⟧
- 「(Badminton, Football, Golf, Snooker, Swimming, Tennis)」⟦9618_w25_31:1(b)(i)⟧
- 「DECLARE Choice : Activity」⟦9618_w25_31:1(b)(ii)⟧
- 「TYPE TDayPointer = ^STRING // ^DayOfWeek」⟦9618_s23_31:4(b)⟧
- 「TYPE SelectParts = ^Parts」⟦9618_w21_31:3(b)⟧

**易错与失分**
- 考官报告列出的四种常见错误：不以 `TYPE` 开头、漏了类型名与列表之间的等号、列表不加圆括号、给每个值加引号（⟦9618_w25_31:1(b)(i)⟧ 的考官报告）。
- 用 `DECLARE` 或 `ENUM` 代替 `TYPE`：考官报告多次点名（⟦9618_w22_32:4(a)⟧、⟦9618_s22_32:1(b)(i)⟧ 的考官报告）。`DECLARE` 声明变量，`TYPE` 定义类型。
- 改字段时把类型写回 STRING，或把字段名与类型名写反（`DECLARE GateID : Gate`）——考官报告指出这两种错误（⟦9618_w25_31:1(b)(ii)⟧、⟦9618_s25_32:1(b)(ii)⟧ 的考官报告）。
- 题目说“a data type to point to a day …”却写成另一个枚举：看到 point / reference a memory location 就是指针（⟦9618_s23_31:4(b)⟧ 的考官报告指出很多人在这里写了枚举）。
- 题干说 “a set of prime numbers” 但该题 MS 给的是枚举写法 `TYPE Prime = (2, 3, 5, …)`（⟦9618_s23_31:4(a)⟧）；真正要写集合时题目会说 “the set data type”（DR-05）。

#### 代表题精讲　⟦9618_w25_31:1(b)(i)⟧

**在考什么**　记录类型 ClubMember 已给出（Code、LastName、…、FeesPaid）。An enumerated data type, Activity, is required … Write the pseudocode statement for the type declaration of Activity to hold the names of the available activities: Badminton, Football, Golf, Snooker, Swimming, Tennis. 2 分；紧接着 (b)(ii) 1 分：把新字段 Choice 的声明写出来。

**完整作答**

```pseudocode
TYPE Activity = (Badminton, Football, Golf, Snooker, Swimming, Tennis)
```

(b)(ii)：

```pseudocode
DECLARE Choice : Activity
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 |
|:--|:--|:--|
| 1 | TYPE Activity= | `TYPE`、类型名、等号 |
| 2 | (Badminton, Football, Golf, Snooker, Swimming, Tennis) | 圆括号、六个值、无引号 |
| (b)(ii) | DECLARE Choice : Activity | 字段名在左、枚举类型名在右 |

**直观**　`TYPE` 是在“发明一个新词”：从此 Activity 和 INTEGER、STRING 一样可以拿来声明变量和字段。枚举值是这个新类型自己的“常量名”，不是字符串，所以不加引号。

**同题 Python 版要点**　Python 用 `enum.Enum`：`class Activity(Enum): BADMINTON = 1 …`；赋值写 `member.choice = Activity.GOLF`。P4 很少要求枚举，阶梯 L08 对照卡只作了解。

**迁移与卡点**
- **卡点**：`TYPE` 不是 `DECLARE`——`TYPE` 发明类型，`DECLARE` 声明变量；枚举值不加引号；指针是 `= ^被指向的类型`。
- **考官在换什么**：枚举还是指针、给不给类型名、是否接着问“把记录里某字段改成这个类型”。得分点只有两处：`TYPE 名 =` 和等号右边。
- **从代表题到变式**：代表题是枚举（圆括号里的值列表）；变式是指针（`^` 后面写被指向的类型，类型名自己起）。搬过去的是 `TYPE 名 =` 这半句；要换的是等号右边的形状。看到 point / reference a memory location 就是指针，不是另一个枚举。
- **反例**：`DECLARE Activity = (…)`；`TYPE DayPointer = STRING^`；给枚举值加引号。

**下一道变式**　⟦9618_s23_31:4(b)⟧　（换成指针：“A data type to point to a day in the week”，类型名自己起，`^` 后面写被指向的类型。）

<!-- auto:drills P3-DR-02 -->

### P3-DR-03　声明记录类型　{#P3-DR-03}

<!-- auto:stats P3-DR-03 -->

**考法**　①按字段清单写整个 `TYPE … ENDTYPE`（4 分，最常见），常要求某字段用前一小问定义的枚举类型；②改写已给记录定义里的一行：取值范围（`1 .. 10`）或改成数组字段（1–2 分）。

**识别信号**　Write pseudocode statements to declare the composite data type … to hold data about …；Write pseudocode statements to declare the record data type …；Write pseudocode statements to define this record；Use the most appropriate data type in each case (including the enumerated data type from part (a))；Write the updated line / the extra line of pseudocode … in the type definition。

**解题思路**
1. **骨架**：第一行 `TYPE <类型名>`（类型名照题目），最后一行 `ENDTYPE`；中间**每个字段一行** `DECLARE <字段名> : <类型>`。
2. **字段名**：题目只给中文意思般的描述（“date team joined the league”）时，自己起一个无空格的标识符（`DateOfJoining`）；题目给了字段名就照抄。
3. **类型按规则选**（这是 MS 分值最多的地方）：

   | 数据 | 类型 | 理由 |
   |:--|:--|:--|
   | 编号含字母或“any combination of letters and numbers”、电话号码、姓名、地址 | STRING | 电话有前导 0 / 空格 / +，不做算术 |
   | 日期 | DATE | — |
   | 人数、名次、年份、分钟数 | INTEGER | 整数计数 |
   | 价格、费用、频率 | REAL | 有小数 |
   | yes / no、是否完成 | BOOLEAN | 只有两种取值 |
   | 题目说用前面定义的枚举 | 该枚举类型名 | MS 单独给一分 |

4. **改一行**：取值范围按该题 MS 写成 `DECLARE NumberOfCopies : 1 .. 10`（2027–29 指南没有列出这种范围写法，这里是 ⟦9618_s22_31:1(b)(i)⟧ 的 MS 答案）；多个同类值写成数组字段 `DECLARE AccessionNumber : ARRAY[1:NumberOfCopies] OF INTEGER`。
5. 写完数一遍：字段数 = 题目列出的数据项数；每行都有 `DECLARE`。

**伪代码模板**

```pseudocode
TYPE Booking                              // type name exactly as given
   DECLARE BookingNumber : STRING         // letters and numbers -> STRING
   DECLARE ClientTelephone : STRING       // telephone numbers are STRING
   DECLARE DateOfDeparture : DATE
   DECLARE NumberOfSeats : INTEGER
   DECLARE Fare : REAL
   DECLARE Paid : BOOLEAN
   DECLARE TaxiUsed : Vehicle             // enumerated type from an earlier part
ENDTYPE
```

**得分表述**（引自对应 MS）
- 「TYPE Booking and ENDTYPE correct」⟦9618_s25_31:1(b)⟧
- 「Declare used correctly for every field in the response」⟦9618_s25_31:1(b)⟧
- 「One mark for every two correct declarations」⟦9618_s24_31:3(b)⟧
- 「DECLARE AircraftType as Aircraft (correct data type from part 4(a))」⟦9618_w22_32:4(b)⟧
- 「DECLARE AccessionNumber : ARRAY[1:NumberOfCopies] OF INTEGER」⟦9618_s22_31:1(b)(ii)⟧

**得分点地图**（核验语料 2022–2026s、主题型为 DR-03、去掉 `equivalent_of` 的已拆分行，共 7 道写整个 `TYPE … ENDTYPE` 的 4 分题；“题数”= 有这类得分点的题数，同题同标签只计一次；脚本按 `markpoints[].skills` 统计）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| `TYPE <名>` 与 `ENDTYPE` 正确 | 7 | `record-type` |
| 字段按组给分：every two correct declarations / shaded / any four fields / remaining fields | 7 | `data-types`（多数同时标 `record-type`） |
| 每个字段都正确使用 `DECLARE` | 4 | `record-type` |
| 字段使用题目前一问定义的枚举类型 | 3 | `user-defined-type` |

7 道题都有“首尾一分 + 字段类型按组给分”；2024 年 11 月（w24）起的题多了一分专给“每行都用 DECLARE”（w24_32、s25_31、s25_33、w25_33 四道）。2024 年 6 月的 ⟦9618_s24_31:3(b)⟧ 还没有这一分，但范答照样每行都写 DECLARE。

**易错与失分**
- 电话号码写成 INTEGER、会员人数写成 STRING：考官报告点名的两种错误（⟦9618_s24_31:3(b)⟧ 的考官报告）。
- 漏写 `DECLARE` 或把它放错位置：考官报告指出这是常见失分（⟦9618_s25_31:1(b)⟧、⟦9618_s25_33:1(a)⟧ 的考官报告），2024 年 11 月（w24）起的 MS 专门有一分。
- 题目要求用前面的枚举类型，却把该字段写成 STRING（⟦9618_w25_33:1(b)⟧ 的考官报告指出 Colour 被写成 STRING 而不是 Spectrum）。
- 写成 `TYPE Booking = …`、`RECORD … ENDRECORD`、`END TYPE`：首尾一分丢掉。
- 改一行题写成整个新数组声明 `DECLARE NumberOfCopies : ARRAY …`：考官报告指出范围题常见错误是写成数组（⟦9618_s22_31:1(b)(i)⟧ 的考官报告）；反过来，“每本书一个或多个编号”那题必须用数组（⟦9618_s22_31:1(b)(ii)⟧ 的考官报告）。

#### 代表题精讲　⟦9618_s25_31:1(b)⟧

**在考什么**　出租车公司。(a) 已定义枚举类型 Vehicle（M100, M230, T101, T102, T120, T150）。Write pseudocode statements to declare the composite data type, Booking … booking number (any combination of letters and numbers)、destination、client name、client telephone number、date of departure、address for pick-up、the identity code of the taxi used. Use the most appropriate data type in each case, including the enumerated data type from part (a). 4 分。

**完整作答**

```pseudocode
TYPE Booking
   DECLARE BookingNumber : STRING
   DECLARE Destination : STRING
   DECLARE ClientName : STRING
   DECLARE ClientTelephone : STRING
   DECLARE DateOfDeparture : DATE
   DECLARE PickupAddress : STRING
   DECLARE TaxiUsed : Vehicle
ENDTYPE
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 |
|:--|:--|:--|
| 1 | TYPE Booking and ENDTYPE correct | 首尾两行 |
| 2 | Declare used correctly for every field in the response | 七行都以 `DECLARE` 开头 |
| 3 | Any four fields correct | 任意四个字段的类型对 |
| 4 | Remaining fields correct | 其余字段，含 `TaxiUsed : Vehicle` |

四个点各自独立，共 4 分，不设 Max。七个字段里最容易错的是电话（STRING）和出租车编号（用枚举 Vehicle，不是 STRING）。

**直观**　记录类型是一张空白表格的“表头设计”：每一栏写明栏名和能填什么。枚举类型那一栏相当于下拉菜单，只能从 M100 … T150 里选。

**同题 Python 版要点**
- Python 没有 `TYPE`，用只有属性的类：`__init__` 里每个字段赋一个对应类型的初值（P4 要求能看出字段类型）。
- 记录数组要写 `[Booking() for _ in range(n)]`，不能写 `[Booking()] * n`。
- 先过阶梯 **L08 E01**（图书记录：TYPE ↔ class）。

```python
class Booking:
    def __init__(self):
        self.booking_number = ""     # STRING
        self.destination = ""        # STRING
        self.client_name = ""        # STRING
        self.client_telephone = ""   # STRING, not an integer
        self.date_of_departure = None  # DATE (datetime.date in Python)
        self.pickup_address = ""     # STRING
        self.taxi_used = None        # Vehicle (an Enum member in Python)
```

**迁移与卡点**
- **卡点**：类型选择——电话号码、含字母的编号一律 STRING，人数 INTEGER，费用 REAL，是 / 否 BOOLEAN，题目前一问定义的枚举就用那个名字。每行都写 `DECLARE`（2024 年 11 月起 MS 专门有一分）。
- **考官在换什么**：字段数、有没有枚举字段、按“每两个声明一分”还是“任四个 + 其余”给分、是写整个类型还是改一行。首尾 `TYPE … ENDTYPE` 一分永远在。
- **从代表题到变式**：代表题七个字段含枚举；变式六个字段、没有枚举、按每两个声明一分。搬过去的是骨架和类型选择表；要盯的是电话和人数这两个最容易选错的类型。
- **反例**：`TYPE Booking = …`、`RECORD … ENDRECORD`；把“改一行”题写成整个数组声明。

**下一道变式**　⟦9618_s24_31:3(b)⟧　（FootballClub 六个字段，“每两个声明一分”共 3 分 + 首尾 1 分；没有枚举字段，注意电话和人数的类型。这道 s24 题的 MS 没有“每行都用 DECLARE”的专分，但照样每行都要写 DECLARE。）

<!-- auto:drills P3-DR-03 -->

### P3-DR-04　记录变量的声明与字段赋值　{#P3-DR-04}

<!-- auto:stats P3-DR-04 -->

**考法**　①为已定义的记录类型声明一个变量（1 分）；②用点号给这个变量的若干字段赋值（2–3 分，按数据类型分组给分：字符串一组、日期一分、字符 / 整数 / 布尔 / 枚举各一分）；③字段改成枚举类型后重写一条赋值（1 分）。

**识别信号**　Write the pseudocode statement to set up a variable for one record of the composite data type …；Write pseudocode to store the details of the following … in the variable you set up；Write pseudocode statements to assign: … to … of …；Use the field names you created in part (b)。

**解题思路**
1. **声明变量**：`DECLARE <变量名> : <记录类型名>`。变量名自己起（`Flight1`），**不能用类型名本身当变量名**。
2. **赋值**：每个字段一行 `<变量名>.<字段名> ← <值>`；字段名用前面类型定义里的（自己写的那一问就用自己的名字）。
3. **值的写法看字段类型**：

   | 字段类型 | 写法 | 例 |
   |:--|:--|:--|
   | STRING | 双引号 | `"Cambridge"` |
   | CHAR | 单引号 | `'M'` |
   | DATE | dd/mm/yyyy，不加引号 | `12/12/2022` |
   | INTEGER / REAL | 直接写数 | `8` |
   | BOOLEAN | `TRUE` / `FALSE` | `FALSE` |
   | 枚举 | 直接写值名，不加引号 | `C350` |

4. 已经声明过变量就不要在赋值前再写 `DECLARE`。

**伪代码模板**

```pseudocode
DECLARE Flight1 : Flight                 // variable of the record type
Flight1.FlightNumber ← "XA782"           // STRING: double quotes
Flight1.DepartureDate ← 12/12/2022       // DATE: no quotes
Flight1.AircraftType ← C350              // enumerated value: no quotes
Pet1.PetGender ← 'M'                     // CHAR: single quotes
LibraryBook.Fiction ← FALSE              // BOOLEAN
```

**得分表述**（引自对应 MS）
- 「DECLARE Member1 : ClubMember」⟦9618_w25_31:1(a)(i)⟧
- 「Correct assignments of both string data values」⟦9618_w22_32:4(c)(ii)⟧
- 「Correct assignments of enumerated data value」⟦9618_w22_32:4(c)(ii)⟧
- 「Use of correct Flight1 variable with given field names」⟦9618_s25_32:1(a)⟧
- 「BuildingRegister.BuildingGroup ← house」⟦9618_s22_32:1(b)(iii)⟧

**易错与失分**
- 用类型名作变量名（`DECLARE Pet : Pet`、`ClubMember.Code ← …`）：考官报告多次点名（⟦9618_w22_31:3(d)(i)⟧、⟦9618_w25_31:1(a)(ii)⟧ 的考官报告）。
- 字符串不加引号：考官报告指出的常见错误（⟦9618_s22_31:1(a)⟧ 的考官报告）。
- 同一个值 house：字段是 STRING 时写 `"house"`（⟦9618_s22_32:1(a)⟧ 的 MS），字段改成枚举类型后写 `house`（⟦9618_s22_32:1(b)(iii)⟧ 的 MS）——引号由**字段类型**决定。
- 在赋值语句前多写 `DECLARE`，或漏了变量名只写字段名：考官报告指出的另两种错误（⟦9618_w22_32:4(c)(ii)⟧、⟦9618_s25_32:1(a)⟧ 的考官报告）。

#### 代表题精讲　⟦9618_w22_32:4(c)(ii)⟧

**在考什么**　机场航班。(a) 枚举 Aircraft；(b) 记录 Flight（FlightNumber、Destination、DepartureDate、AircraftType : Aircraft）；(c)(i) 声明变量 `DECLARE Flight1 : Flight`。本问：Write pseudocode to store the details of the following flight in the variable you set up in part (c)(i)：flight number XA782、destination Cambridge、date of departure 12/12/2022、type of aircraft used C350。Use the field names you created in part (b). 3 分。

**完整作答**

```pseudocode
Flight1.FlightNumber ← "XA782"
Flight1.Destination ← "Cambridge"
Flight1.DepartureDate ← 12/12/2022
Flight1.AircraftType ← C350
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 |
|:--|:--|:--|
| 1 | Correct assignments of both string data values | 前两行，双引号 |
| 2 | Correct assignments of date data value | 第三行，日期不加引号 |
| 3 | Correct assignments of enumerated data value | 第四行，C350 不加引号 |

**直观**　声明变量 = 复印一张空白表格；赋值 = 往格子里填字。填之前先看格子的类型：文字栏加引号，日期栏照格式写，下拉菜单栏直接写选项名。

**同题 Python 版要点**　`flight1 = Flight()` 后逐个 `flight1.flight_number = "XA782"`；日期用 `datetime.date(2022, 12, 12)`，枚举用 `Aircraft.C350`。阶梯 **L08 E01**。

**下一道变式**　⟦9618_w22_31:3(d)(ii)⟧　（Pet 记录：字符串、字符 'M'、整数三组各一分；要用 (d)(i) 自己声明的变量名。）

<!-- auto:drills P3-DR-04 -->

### P3-DR-05　声明集合类型　{#P3-DR-05}

<!-- auto:stats P3-DR-05 -->

**考法**　按给出的元素写集合类型的两行声明：`TYPE … = SET OF …` 与 `DEFINE … (…) : …`。4 分，按片段给分（类型行、DEFINE 与集合名、括号里的值、冒号后的类型名）。核验语料只考过 2 次，但每次 4 分，写法只有一种，背下来就是满分。

**识别信号**　Write pseudocode statements to declare the set data type … to hold …；… using the variable …；题目列出一串元素（数字或符号）。

**解题思路**
1. **第一行定义类型**：`TYPE <类型名> = SET OF <元素类型>`。元素是整数 → `INTEGER`；是单个符号 / 字母 → `CHAR`。
2. **第二行定义集合本身**：`DEFINE <集合名> (<元素>, …) : <类型名>`。元素放在圆括号里、逗号分隔；CHAR 元素加单引号，数字不加。
3. **两个名字别弄混**：类型名出现两次（第一行的 TYPE 后、第二行的冒号后），集合名只在 DEFINE 后出现一次。题目只给一个名字时，用它作集合名（DEFINE 后），自己另起类型名（⟦9618_s24_32:3(b)⟧ 的 MS 就是 `TYPE Numbers` + `DEFINE EvenNumbers`）；题目给了两个名字而角色说得不清时，该题 MS 两种分配都接受（⟦9618_w24_31:6(b)⟧）。

**伪代码模板**

```pseudocode
// guide 2027-29: TYPE <identifier1> = SET OF <data type>
//                DEFINE <identifier2> (value1, value2, ...) : <identifier1>
TYPE Numbers = SET OF INTEGER
DEFINE EvenNumbers (2, 4, 6, 8, 10, 12) : Numbers

TYPE SymbolSet = SET OF CHAR
DEFINE Operators ('+', '-', '*', '/', '^') : SymbolSet
```

**得分表述**（引自对应 MS）
- 「Type statement fully correct」⟦9618_s24_32:3(b)⟧
- 「DEFINE EvenNumbers」⟦9618_s24_32:3(b)⟧
- 「Correct list of values in brackets」⟦9618_s24_32:3(b)⟧
- 「: <set identifier> from Type statement used」⟦9618_s24_32:3(b)⟧
- 「SET OF CHAR」⟦9618_w24_31:6(b)⟧

**得分点地图**（核验语料 2022–2026s、主题型 DR-05、去掉 `equivalent_of`：2 道已拆分题，⟦9618_s24_32:3(b)⟧ 4 条、⟦9618_w24_31:6(b)⟧ 5 条 Max 4；口径同 DR-03）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| `TYPE <名> =` 与 `SET OF <类型>`（s24 合为一条 “Type statement fully correct”，w24 拆成两条） | 2 | `user-defined-type` |
| `DEFINE <集合名>` | 2 | `user-defined-type` |
| 圆括号里的元素列表 | 2 | `user-defined-type` |
| `: <类型名>`（用第一行的类型名） | 2 | `user-defined-type` |

**易错与失分**
- 用 `DECLARE` 代替 `DEFINE`，或把元素写进第一行 `TYPE … = (2, 4, …)`（那是枚举）。
- 漏了冒号后的类型名，或冒号后写成集合名自己。
- CHAR 元素不加单引号、整数元素反而加了引号。
- 考官报告指出：用了最新伪代码指南集合写法的考生更容易拿满分（⟦9618_s24_32:3(b)⟧ 的考官报告）——这一型只认指南格式，别自创。

#### 代表题精讲　⟦9618_s24_32:3(b)⟧

**在考什么**　Write pseudocode statements to declare the set data type EvenNumbers to hold this set of even numbers between 2 and 12: 2, 4, 6, 8, 10, 12. 4 分。

**完整作答**

```pseudocode
TYPE Numbers = SET OF INTEGER
DEFINE EvenNumbers (2, 4, 6, 8, 10, 12) : Numbers
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 |
|:--|:--|:--|
| 1 | Type statement fully correct | `TYPE Numbers = SET OF INTEGER` |
| 2 | DEFINE EvenNumbers | `DEFINE EvenNumbers` |
| 3 | Correct list of values in brackets | `(2, 4, 6, 8, 10, 12)` |
| 4 | : <set identifier> from Type statement used | `: Numbers` |

题目只给了一个名字 EvenNumbers，MS 把它当集合名，类型名 Numbers 是自己起的。

**直观**　第一行说“我要一种装整数的袋子”（类型）；第二行说“拿一个这种袋子，起名 EvenNumbers，装进 2、4 … 12”（具体的集合）。

**同题 Python 版要点**　Python 直接有集合：`even_numbers = {2, 4, 6, 8, 10, 12}`，交集 `a & b`、并集 `a | b`；不需要先定义类型。阶梯没有专门的集合练习，P4 不考集合声明。

**下一道变式**　⟦9618_w24_31:6(b)⟧　（CHAR 集合：`+ – * / ^` 五个运算符，要加单引号；题目给了 SymbolSet 与 Operators 两个名字，MS 五条 Max 4。）

<!-- auto:drills P3-DR-05 -->

### P3-DR-06　文件组织方式　{#P3-DR-06}

<!-- auto:stats P3-DR-06 -->

**考法**　①描述某一种组织方式里记录怎样排列（2 分）；②描述两种（顺序与随机，各 Max 2）；③比较串行与顺序（2021 扩展卷）；④各举一个适用的例子（1 分）。

**识别信号**　Describe serial / sequential / random file organisation；Describe how records are organised in … files；Compare sequential and serial methods of file organisation；State one example of a use for serial file organisation。

**解题思路**
1. 每句话的主语都是 **records**：“Records are stored …”。
2. **串行 serial**：记录一条接一条、按**到达先后**（chronological）存；新记录**追加到文件末尾**。例：未排序的临时事务文件、数据日志。
3. **顺序 sequential**：记录一条接一条、按**键字段**排好序；新记录要插到正确位置——更新时要生成一个新版本的文件。例：批处理、账单 / 工资单。
4. **随机 random**：记录**不按任何顺序**存放；记录的键与它在文件里的位置有关系——用**散列算法**由键算出位置；可以直接更新。例：订票系统。
5. 比较串行与顺序：相同点（都一条接一条存、都要逐条访问）+ 不同点（时间顺序 vs 键顺序；追加到末尾 vs 插入正确位置）。

**得分表述**（引自对应 MS）
- 「Records are stored one after the other as they are collected // records are stored in chronological order」⟦9618_w24_32:2(a)⟧
- 「New records are appended to the end of the file」⟦9618_w24_32:2(a)⟧
- 「Records (in the file) are ordered」⟦9618_w23_31:4(a)⟧
- 「A new version (of the file) has to be created to update the file」⟦9618_w23_31:4(a)⟧
- 「There is a relationship between the key of the record and its location within the file // a hashing algorithm is used to find the location of the record」⟦9618_w23_31:4(a)⟧
- 「Creating unsorted / temporary transaction files」⟦9618_w24_32:2(b)⟧

**易错与失分**
- 写“files are stored in chronological order”：考官报告明确指出要写**记录**按时间顺序存，写成文件不给分（⟦9618_w24_32:2(a)⟧、⟦9618_w23_31:4(a)⟧ 的考官报告）。
- 顺序文件只写“stored in order”：MS 第二分要“based on the key field”。
- 随机文件写成“stored randomly”就停：要说出位置由键经散列算法决定。
- 组织方式题里大谈怎样查找（顺序存取、直接存取）：那是 DR-07 的分，组织方式题只问记录怎样排、新记录放哪、用在哪里。

#### 代表题精讲　⟦9618_w23_31:4(a)⟧

**在考什么**　Describe sequential and random methods of file organisation. 4 分：顺序 Max 2（MP1–MP3）、随机 Max 2（MP4–MP6）。

**完整作答**
- Sequential：记录在文件里是排好序的，顺序依据键字段；要更新文件必须生成一个新版本。
- Random：记录在文件里不按任何顺序存放；记录的键与它的存放位置有关系，用散列算法求出位置；更新可以直接进行。

**与 MS 对齐**　顺序三句对应 MP1、MP2、MP3（取 2）；随机三句对应 MP4、MP5、MP6（取 2）。每边写满三点是保险。

**英文作答句**　Sequential: the records in the file are ordered, based on the key field; a new version of the file has to be created to update it. Random: the records are stored in no particular order within the file; there is a relationship between the key of a record and its location, as a hashing algorithm is used to find the location of the record; updates can be carried out directly.

**直观**　串行像排队登记簿，来一个记一个；顺序像按学号排好的花名册；随机像寄存柜，柜号由号码牌算出来，柜子之间没有先后。

**下一道变式**　⟦9618_w24_32:2(a)⟧　（只问串行：两分分别是“按收集先后一条接一条”和“新记录追加到末尾”。）

<!-- auto:drills P3-DR-06 -->

### P3-DR-07　文件存取方式　{#P3-DR-07}

<!-- auto:stats P3-DR-07 -->

**考法**　①描述顺序存取（2 分）；②说明顺序存取怎样用于串行文件与顺序文件（3 分）；③概述直接存取（2 分）；④说明直接存取怎样用于顺序文件（索引）与随机文件（散列）（各 2 分）；⑤描述在顺序文件里记录怎样组织与存取（3 分）；⑥按情境选存取方式（1 分）。

**识别信号**　Describe the sequential method of file access；Outline what is meant by direct access as a method of file access；Explain how the sequential method of file access is applied to files with serial organisation and to files with sequential organisation；Explain how direct access is used to locate a specific record in sequential files and random files；Outline the process … to find a record。

**解题思路**
1. **顺序存取**：从文件的物理开头起，**一条接一条**读记录，比较键，直到找到或到文件尾。
   - 用于**串行文件**：记录按时间顺序，**每一条都要查**，直到找到或全部查完。
   - 用于**顺序文件**：记录按键字段排序，比较的是键字段；找到就停，或当前记录的键**已经大于**目标键就停（后面不可能再有）。
2. **直接存取**：不读其他记录就能找到目标记录。
   - 用于**顺序文件**：保留一张所有键字段的**索引**，在索引里查到目标记录的地址，再直接去取。
   - 用于**随机文件**：对键字段用**散列算法**算出记录应在的地址；若不在那里（冲突），用线性探测或查溢出区找（这一分属 DR-08 的知识）。
3. 答案的主语一律是 record：“a record is found …”，不是“the file is accessed …”。

**得分表述**（引自对应 MS）
- 「Sequential access method searches for records one after the other」⟦9618_s24_31:4(a)⟧
- 「… from the physical start of the file until the record is found/the end of file」⟦9618_s24_31:4(a)⟧
- 「Direct access allows a record to be found in a file without other records being read」⟦9618_s24_32:7(a)⟧
- 「In sequential files, an index of all key fields is kept」⟦9618_s24_32:7(b)(i)⟧
- 「A hashing algorithm is used on the key field of the record」⟦9618_s24_32:7(b)(ii)⟧
- 「… until the required record is found or key field value is exceeded」⟦9618_s23_32:2(a)⟧

**易错与失分**
- “直接存取用于顺序文件”却写成顺序存取：考官报告指出很多人这样答，该题要的是**索引**（⟦9618_s24_32:7(b)(i)⟧ 的考官报告）。
- 说“散列算法作用于文件”：考官报告指出要写作用于**记录的键字段**（⟦9618_s24_32:7(b)(ii)⟧ 的考官报告）。
- 顺序文件的顺序存取只写“until found”：漏了“键已超过目标就停”，这是顺序文件区别于串行文件的那一分。
- 只写“access the file”：考官报告反复强调要说明存取的是文件里的一条**记录**（⟦9618_s24_31:4(a)⟧、⟦9618_s24_31:4(b)⟧ 的考官报告）。

#### 代表题精讲　⟦9618_s24_31:4(b)⟧

**在考什么**　Explain how the sequential method of file access is applied to files with serial organisation and to files with sequential organisation. 3 分，MS 四点 Max 3：串行两点（排列 + 查法）、顺序两点（排列 + 查法）。

**完整作答**
- 串行文件：记录按时间先后存放；查找时每条记录都要检查，直到找到该记录或全部记录都检查完。
- 顺序文件：记录按键字段（索引）排序，比较的是键字段；逐条检查，直到找到该记录，或当前记录的键字段已经大于目标记录的键字段。

**与 MS 对齐**　四句依次对应 MP1–MP4，任 3 点满分。MP1、MP3 讲记录怎样排（所以本行副题型是 DR-06），MP2、MP4 讲怎样查。四点都写是保险。

**英文作答句**　For serial files, the records are stored in chronological order, so every record needs to be checked until the record is found, or all records have been checked. For sequential files, the records are stored in order of a key field, and it is the key field that is compared; every record is checked until the record is found, or the key field of the current record is greater than the key field of the target record.

**直观**　在乱序的登记簿里找人，只能一页页翻到底；在按学号排好的花名册里找 1050 号，翻到 1060 号还没见到就可以合上了。

**下一道变式**　⟦9618_s24_32:7(b)(i)⟧　（换成**直接**存取用于顺序文件：答索引，不是逐条比较。）

<!-- auto:drills P3-DR-07 -->

### P3-DR-08　散列算法与冲突处理　{#P3-DR-08}

<!-- auto:stats P3-DR-08 -->

**考法**　①用给定散列函数（MOD n）算出几个键的散列值并填表（2 分）；②解释文件存取中的散列算法（3 分）；③说明什么是冲突（2 分）；④说明写入随机文件时怎样处理冲突（3 分），或存取两方面都说（4 分）；⑤给出两种处理“同一地址”的方法（2 分）。

**识别信号**　A hashing algorithm is used to calculate storage locations for records in a random access file；Complete the table to show the remaining hash values；Explain what is meant by a hashing algorithm in the context of file access；Outline what is meant by the term collision；Explain how a collision can be dealt with；the calculated hash value is a duplicate of a previously calculated hash value。

**解题思路**
1. **算散列值**：`键 MOD n` = 键除以 n 的余数，范围 0 至 n−1。手算：找最接近且不超过的 n 的倍数（1025 MOD 3：1023 = 3 × 341，余 2）。
2. **散列算法是什么**：一个数学公式，作用于记录的**键字段**，算出的结果就是记录应该存放 / 查找的**地址**；用于直接存取。
3. **冲突**：两个不同的键经散列算法得到**同一个散列值**，所以算出的位置可能已被别的记录占用。
4. **处理冲突**（写入时）三种做法，答一种要写完整：
   - 从原散列位置起**线性**往后找，存入第一个空位（MS 括注 closed hash）；
   - 存入**溢出区**的下一个空位（MS 括注 open hash）；
   - 每个位置挂一条链，存入链上第一个空位。
5. **查找时**也要说：先看散列位置，键不对就按同样规则线性查找（或查溢出区），直到找到键相同的记录；查完仍没有 → 记录不在文件里。

**得分表述**（引自对应 MS）
- 「It is a mathematical formula」⟦9618_w24_31:5(a)⟧
- 「… used to perform a calculation applied to the key field of the record being searched / stored」⟦9618_w24_31:5(a)⟧
- 「The result of the calculation gives the address where the record should be found / stored」⟦9618_w24_31:5(a)⟧
- 「… this means the determined storage location has already been used for another record」⟦9618_s23_31:3(b)⟧
- 「An overflow area is set up and the record is stored in the next free memory space in the overflow area」⟦9618_w24_31:5(b)⟧
- 「If not found record is not in file」⟦9618_s23_31:3(b)⟧

**易错与失分**
- 把冲突写成数据传输中的冲突：考官报告点名这种错误（⟦9618_w23_32:3(a)⟧ 的考官报告）。这里的冲突是两个键得到同一散列值。
- 只写“use open hash / closed hash”：考官报告指出这不够具体（⟦9618_w24_31:5(b)⟧ 的考官报告），要写出“在哪里、怎样找下一个空位”。考官报告还指出很多人把两个名称用反（⟦9618_s23_31:3(b)⟧ 的考官报告）；不确定时只描述做法、不写名称。
- 只讲存、不讲取（或反之）：题目写 storage **or retrieval** 时两边都写，取的时候还要写“查完仍没有 → 不在文件里”。
- MOD 算错：先确认是余数，不是商。

#### 代表题精讲　⟦9618_s23_31:3(b)⟧

**在考什么**　（同题 3(a)：散列函数 modulus 3，求 1050、1025 的散列值——答 0、2。）Describe what happens, in relation to the storage or retrieval of a record in the file, when the calculated hash value is a duplicate of a previously calculated hash value for a different record key. 4 分，MS 九点 Max 4：冲突是什么（MP1–MP2）、存的时候（MP3–MP6）、取的时候（MP7–MP9）。

**完整作答**
1. 这时发生冲突：该位置上已存记录的键与当前记录的键不一致。
2. 也就是说，算出的存放位置已经被另一条记录占用。
3. 存放时：从该位置起在文件里线性查找，找到下一个可用的位置存入。
4. 查找时：从散列位置起线性往下找，直到找到键相同的记录。
5. 如果找遍了仍没有找到，说明该记录不在文件里。

**与 MS 对齐**　1 → MP1，2 → MP2，3 → MP3 + MP4（线性查找 + 找下一个空位，是两个点），4 → MP8，5 → MP9。前四个点已满 4 分，后两句是保险。若改用溢出区，对应 MP5、MP6、MP7。

**英文作答句**　A collision occurs: the record key does not match the stored record key, which means the determined storage location has already been used for another record. To store the record, search the file linearly to find the next available storage space. To find the record, search linearly from the hashed location until the matching record key is found; if it is not found, the record is not in the file.

**直观**　寄存柜按号码牌算柜号，两张牌算出同一个柜号就是冲突。存的时候往后找第一个空柜；取的时候从算出的柜子往后一个个看牌号，看完都没有就是没存过。

**下一道变式**　⟦9618_w23_32:3(b)⟧　（只问写入时怎样处理，3 分；MS 给了线性、溢出区、链表三套，答其中一套写满三步。）

<!-- auto:drills P3-DR-08 -->

### P3-DR-09　浮点数换算成十进制　{#P3-DR-09}

<!-- auto:stats P3-DR-09 -->

**考法**　给出补码尾数与补码阶码（10 + 6、12 + 4、11 + 5 位；8 + 8 位见 DR-10 / DR-11），求十进制值，Show your working。3 分，MS 写法有两种：“两个过程分 + 一个答案分”，或 MP1 阶码、MP2 移位、MP3 答案；个别 2 分题是一个过程分 + 一个答案分。正数、负数都考。

**识别信号**　Calculate the denary value of the given (normalised) (binary) floating-point number. Show your working；表格 Mantissa | Exponent 下已填好 0 / 1；Working … Answer / Denary value …。

**解题思路**
1. **算阶码**：把阶码当补码整数读（最高位为负权）。`000101` = 5，`001011` = 11，`1110` = −2。
2. **写出尾数**：在符号位后点小数点：`1010110011` → `1.010110011`。
3. **移小数点**：阶码为 +k 就右移 k 位（`1.010110011` 右移 5 位 → `101011.0011`）；为负就左移，左边按符号位补齐。
4. **按补码求值**：最左一位是负权。`101011.0011` = −32 + 8 + 2 + 1 + 0.125 + 0.0625 = −20.8125。也可以用分数法：尾数值 × 2^阶码。
5. **负数的另一种算法**：把移位后的数取补码得正数（按位取反加 1），算出正值再加负号。
6. 检查：结果的符号与尾数最高位一致（1 → 负）；把三步都写在 Working 里。

**得分表述**（引自对应 MS）
- 「application of exponent to go from 1.010110011 to 101011.0011」⟦9618_w24_31:1(b)⟧
- 「–32 + 8 + 2 + 1 + .125 + .0625」⟦9618_w24_31:1(b)⟧
- 「conversion of exponent 001001 to 9」⟦9618_s24_31:1(a)⟧
- 「correct calculation/application of exponent seen」⟦9618_w25_32:2(a)⟧
- 「correct method to find the final answer」⟦9618_w25_32:2(a)⟧

**易错与失分**
- 把阶码当成要“加”到尾数上的小数：考官报告点名这一错误（⟦9618_w25_32:2(a)⟧ 的考官报告）。阶码只决定小数点移几位。
- 负数忘了负号，或算到一半停下：考官报告指出这两种失分（⟦9618_s25_32:2(b)⟧ 的考官报告）。
- 只写答案：过程分是 2 分，答案错时过程还能保住分，只写答案又写错就是 0 分。考官报告指出要写清阶码怎样算、怎样作用于尾数（⟦9618_w22_32:1(b)⟧ 的考官报告）。
- 负尾数按无符号读（`101011.0011` 读成 43.1875）：最高位是 −32，不是 +32。

#### 代表题精讲　⟦9618_w24_31:1(b)⟧

**在考什么**　10 位尾数、6 位阶码，都用补码。Calculate the denary value of the given normalised binary floating-point number：尾数 `1010110011`，阶码 `000101`。Show your working. 3 分（过程 Max 2 + 答案 1）。

**完整作答**
1. 阶码 `000101` = 4 + 1 = 5。
2. 尾数 `1.010110011`，小数点右移 5 位：`101011.0011`。
3. 补码求值：−32 + 8 + 2 + 1 + 0.125 + 0.0625 = −20.8125。
4. 核对（分数法）：尾数 = −1 + 1/4 + 1/16 + 1/32 + 1/256 + 1/512 = −333/512；× 2⁵ = −333/16 = −20.8125 ✓。

答：−20.8125。

**与 MS 对齐**　第 2 步对应过程分一「application of exponent to go from 1.010110011 to 101011.0011」⟦9618_w24_31:1(b)⟧；第 3 步对应过程分二（−32 + 8 + 2 + 1 + .125 + .0625 seen，MS 用 `//` 列出的分数写法是同一点的替代）；答案分：−20.8125（MS 也接受分数写法 −20 13/16）。过程两点 Max 2 + 答案 1 = 3 分。

**直观**　尾数是“几位有效数字”，阶码是“小数点往哪挪几格”。挪好以后它就是一个普通的补码数：最左一位是负的那一大块，其余位加回来。

**迁移与卡点**
- **卡点**：阶码不是“加到尾数上的数”，它只说小数点挪几位；移完以后它就是一个普通补码数——最左一位是负权。负尾数按无符号读是最常见的错。
- **考官在换什么**：正负、阶码大小与正负（负阶码左移）、位数分配、答案是整数还是带分数。三步不变：算阶码 → 移小数点 → 按补码求值；过程两分、答案一分。
- **从代表题到变式**：代表题负尾数、右移 5 位；变式正尾数、右移 11 位——小数点移到尾数末尾之外，小数部分全是 0，答案是整数，正数直接按位权加。搬过去的是三步；要注意的是移位超过尾数位数时右边补 0。
- **反例**：阶码 `1110` 读成 14（它是 −2，要左移）；负数忘了负号。

**下一道变式**　⟦9618_w25_32:2(a)⟧　（正数、阶码 11：小数点右移 11 位后小数部分全是 0，答案是整数。）

<!-- auto:drills P3-DR-09 -->

### P3-DR-10　十进制写成规格化浮点数　{#P3-DR-10}

<!-- auto:stats P3-DR-10 -->

**考法**　给一个带符号的十进制数（常带 .25、.75、.0625 这类小数），在指定位数的系统里写出规格化浮点表示，Show your working。3–4 分：转二进制（负数还要取补码）、阶码（移位位数）、答案（尾数、阶码）。变化：①同一个数写进两种位数分配的系统（尾数不够会丢精度）；②正负两问连出，阶码相同；③尾数位数不够、要截断，答案旁写一句“精度损失”。

**识别信号**　Calculate / Write the normalised (binary) floating-point representation of –102.75 / +202 in this system；show how it would be represented in each of these two systems；Show your working；空的 Mantissa | Exponent 格子。

**解题思路**
1. **整数部分、小数部分分别转二进制**：102 = 64 + 32 + 4 + 2 → `1100110`；0.75 = 0.5 + 0.25 → `.11`。前面补一个 0 作符号位：`01100110.11`。
2. **负数取补码**：按位取反 `10011001.00`，在最低位加 1 → `10011001.01`。（核对：−128 + 16 + 8 + 1 + 0.25 = −102.75。）
3. **规格化**：把小数点移到最高两位之间，使尾数以 `01`（正）或 `10`（负）开头：`10011001.01` → `1.001100101`，小数点左移了 7 位 → 阶码 = +7。
4. **写进格子**：尾数按位数从左填，**右边不足补 0**；位数不够就截掉最右边的位（并写一句 precision is lost）。阶码按位数写成补码（7 → `000111`）。
5. **核对**：负数的尾数一定以 `10` 开头、正数以 `01` 开头；把答案按 DR-09 的方法换回十进制，应等于原数（或截断后的近似值）。

**得分表述**（引自对应 MS）
- 「number converted to binary 10011001.01」⟦9618_s24_31:1(b)⟧
- 「exponent = 7 // Moving binary point the correct number of places」⟦9618_s24_31:1(b)⟧
- 「correct mantissa」⟦9618_w23_31:1(a)⟧
- 「correct exponent」⟦9618_w23_31:1(a)⟧
- 「statement regarding number losing precision/rounding error」⟦9618_w24_31:1(a)⟧
- 「Realisation that the exponent doesn’t change」⟦9618_w22_31:1(b)⟧

**易错与失分**
- 不写过程：考官报告指出常见的遗漏是没有说明阶码怎样得出（⟦9618_w25_32:2(b)⟧ 的考官报告）。至少写出：二进制形式、补码形式、“小数点移了 k 位，阶码 = k”。
- 负数先规格化再取补码，或只把符号位改成 1（原码）：P3 一律补码，要按位取反加 1。
- 尾数右边没补 0、或左边多留了一位：格子位数必须正好填满。
- 截断时没有说明丢精度：⟦9618_w24_31:1(a)⟧ 的答案分可以由“正确答案”或“说明精度损失 / 舍入误差”得到；考官报告指出写出截断后的尾数或说明尾数要截断的考生拿分最好。
- 阶码写成原码或无符号：阶码也是补码，负阶码（DR-11 常见）最容易错。

#### 代表题精讲　⟦9618_s24_31:1(b)⟧

**在考什么**　10 位尾数、6 位阶码，补码。Calculate the normalised floating-point representation of –102.75 in this system. Show your working. 3 分：MP1 转成二进制（补码）、MP2 阶码 = 7、MP3 答案。

**完整作答**
1. +102.75：102 = 64 + 32 + 4 + 2，0.75 = 0.5 + 0.25 → `01100110.11`。
2. 取补码：按位取反 `10011001.00`，加 1（加在最低位）→ `10011001.01`。核对：−128 + 16 + 8 + 1 + 0.25 = −102.75 ✓。
3. 规格化：`10011001.01` = `1.001100101` × 2⁷，小数点左移 7 位，阶码 = 7。
4. 尾数（10 位）：`1001100101`；阶码（6 位）：7 = `000111`。

| 尾数 | 阶码 |
|:-:|:-:|
| 1 0 0 1 1 0 0 1 0 1 | 0 0 0 1 1 1 |

**与 MS 对齐**　第 1–2 步 → MP1（MS 接受“转成 102.75、取反加 1”或“−128 + 16 + 8 + 1 + 0.25”两种过程）；第 3 步 → MP2「exponent = 7 // Moving binary point the correct number of places」⟦9618_s24_31:1(b)⟧；第 4 步 → MP3 正确答案。三点各 1 分。

**直观**　规格化就是“把数写成 1.xxx × 2ᵏ 那样的科学记数法”，只是二进制、带符号：正数要 0.1 开头，负数要 1.0 开头，这样尾数里没有浪费的前导位。

**迁移与卡点**
- **卡点**：负数的顺序——先写正数的二进制（带符号位 0），取反加一，**再**规格化；先规格化再取补码会错。规格化的判据只有一句：正数以 `01` 开头，负数以 `10` 开头。
- **考官在换什么**：正负、小数部分（.25、.75、.0625、.125）、位数够不够（不够要截断并说精度损失）、同一个数两套位数分配。过程分永远在“二进制形式、补码、移了几位”。
- **从代表题到变式**：代表题尾数刚好放下；变式有效位比尾数多——按位数截掉最右边的位，答案旁写 precision is lost / truncated。搬过去的是转换、规格化、填格；要新增的是截断与一句说明。
- **反例**：阶码写成原码；尾数右边不补 0；负数只把符号位改成 1。

**下一道变式**　⟦9618_w24_31:1(a)⟧　（+201.125 写进 10 位尾数：二进制有 11 位有效数字，尾数放不下，要截断并说明精度损失。）

<!-- auto:drills P3-DR-10 -->

### P3-DR-11　规格化与可表示的最大最小值　{#P3-DR-11}

<!-- auto:stats P3-DR-11 -->

**考法**　①把给定的二进制数（常是 0.0000001101… 这样很小的正数，或 0101010.111）写成规格化浮点（2 分：尾数、阶码各 1 分，负阶码最常错）；②给出一个未规格化的位串，说明为什么不是规格化（1 分）并规格化（2 分）；③写出最大正数（1 分），或再给出它的十进制值（用 2 的幂表示，1 分）；④解释为什么要规格化（2021 扩展卷）。

**识别信号**　Write the normalised floating-point representation of the following (positive / unsigned) binary number using this system；The given binary floating-point number is not normalised；State why the number is not normalised；Write / Give the largest positive (normalised) two’s complement binary number that can be stored in this system；expressed in terms of powers of 2。

**解题思路**
1. **判断是否规格化**：看尾数最高两位——`01` 或 `10` 才是规格化；`00` 或 `11` 开头就不是（前两位相同）。
2. **规格化一个位串**：尾数左移，直到最高两位不同；**左移几位，阶码就减几**（数值不变）。例：尾数 `00011110` 左移 2 位 → `01111000`，阶码 24 → 22。
3. **规格化一个二进制数**：
   - 大于 1（`0101010.111`）：小数点左移到第一个 1 之前，得 `0.101010111`，左移了 6 位 → 阶码 +6。
   - 小于 1（`0.00000011010111`）：小数点右移到第一个 1 之前，得 `0.11010111`，右移了 6 位 → 阶码 −6，写成补码（6 位：`111010`）。
   - 尾数右边补 0 到规定位数。
4. **最大正数**：尾数 `0` 后面全 1（`0111…1`），阶码取最大正值（`0111…1`）。十进制：尾数 = 1 − 2^−(尾数位数−1)，阶码 = 2^(阶码位数−1) − 1。8 + 8 位：(127/128) × 2¹²⁷。
5. **为什么规格化**：使有效位最多、精度最高；避免同一个数有多种表示；用给定位数表示尽量大的范围。

**得分表述**（引自对应 MS）
- 「The mantissa does not begin with 01/10 (as its most significant bits)」⟦9618_w22_31:1(c)(i)⟧
- 「correct exponent with associated working」⟦9618_s23_32:1(a)⟧
- 「calculation of denary 6 to binary (000)110」⟦9618_s23_32:1(a)⟧
- 「One mark for two’s complement version and one mark for denary version」⟦9618_s25_33:2(a)⟧
- 「Avoids the possibility of many numbers having multiple representations」⟦9618_w21_31:1(b)⟧

**易错与失分**
- 小数往右移时阶码写成 +7：考官报告指出很多答案阶码写成了正七，正确是负七的补码（⟦9618_w25_31:2(a)⟧ 的考官报告）。数变大（小数点右移）→ 阶码为负。
- 规格化未规格化位串时只改了尾数、忘了改阶码：考官报告指出能写对阶码的人少得多（⟦9618_w22_31:1(c)(ii)⟧ 的考官报告）。
- 最大正数的十进制值：考官报告指出能写出位串的人多、能给出十进制值的人少（⟦9618_s25_33:2(a)⟧ 的考官报告）。记住“尾数 1 − 2⁻⁽ⁿ⁻¹⁾、阶码 2⁽ᵐ⁻¹⁾ − 1”。
- 最大正数的尾数写成全 1：最高位是符号位，必须是 0。

#### 代表题精讲　⟦9618_w22_31:1(c)(ii)⟧

**在考什么**　8 位尾数、8 位阶码，补码。给出位串：尾数 `00011110`，阶码 `00011000`。(c)(i) State why the number is not normalised（1 分）；(c)(ii) Write the normalised floating-point representation of the number（2 分：尾数、阶码各 1 分）。

**完整作答**
- (c)(i)：尾数以 `00` 开头，最高两位相同（不是 01 或 10）。
- (c)(ii)：
  1. 尾数 `0.0011110` 左移 2 位，使最高两位成为 `01`：`0.1111000` → `01111000`。
  2. 尾数左移 2 位，数值变成原来的 4 倍，阶码要减 2 抵消：阶码 `00011000` = 24，24 − 2 = 22 = `00010110`。

| 尾数 | 阶码 |
|:-:|:-:|
| 0 1 1 1 1 0 0 0 | 0 0 0 1 0 1 1 0 |

**与 MS 对齐**　(c)(i) 对应「The mantissa does not begin with 01/10 (as its most significant bits)」⟦9618_w22_31:1(c)(i)⟧（MS 也接受“begins with 00 / first two digits are the same”）。(c)(ii) 两点：Correct mantissa、Correct exponent，正是上表两格。

**直观**　未规格化就是“前面有浪费的 0”。把有效位往左推到顶，推了几格，阶码就少记几格——就像把 0.0045 × 10⁵ 改写成 4.5 × 10²。

**下一道变式**　⟦9618_s25_31:2(a)⟧　（10 + 6 位系统，给二进制数 0.00000011010111：小数点要右移，阶码是 −6 的 6 位补码。）

<!-- auto:drills P3-DR-11 -->

### P3-DR-12　精度、范围、舍入误差与上溢下溢　{#P3-DR-12}

<!-- auto:stats P3-DR-12 -->

**考法**　只用文字解释（常跟在 DR-10 / DR-11 计算之后）：①改变尾数 / 阶码位数分配的影响（2–3 分）；②为什么某数不能精确表示：尾数位数不够要截断，或 0.2 这类小数无法用 2 的负幂精确表示（2–3 分）；③二进制表示为什么有时只是近似（3 分）；④什么时候发生上溢 / 下溢，举一个情境并说后果（2–3 分）；⑤要精确存储某数应怎样改变位数分配（2021 扩展卷）。

**识别信号**　Describe the effect of changing the allocation of bits used for the mantissa and for the exponent；Explain the problem that occurred / will occur in storing …；Describe the reason why the normalised form of the following binary number cannot be represented accurately；Explain why a binary representation is sometimes only an approximation；State when underflow occurs；Describe one example of a situation that could cause an overflow。

**解题思路**
1. **位数分配**（总位数固定）：尾数位多 → **精度**高；阶码位多 → **范围**大；一方增加另一方就减少，精度与范围此消彼长。答题时两个方向都写：“尾数增加则精度提高……阶码减少则范围缩小……”。
2. **某个数存不准**，先算再说：
   - 尾数位不够：数出规格化后需要几位（含符号位），对比尾数位数，说出要截掉最低的几位 → 精度损失。
   - 小数部分无法精确表示：二进制小数只能由 1/2、1/4、1/8 … 组成，0.2 这类数凑不准（65.20 最接近的是 .25 或 .1875）→ 舍入误差。
3. **上溢 overflow**：运算（如两个大数相乘 / 相加）结果超出系统能表示的最大值 → 最高位丢失。要计算时写出结果值和系统最大值作对比。
4. **下溢 underflow**：运算结果太小（阶码负得超出范围），无法表示 → 结果变成 0 / 无法精确表示。
5. 后果一律落到“precision is lost / rounding error / truncation / most significant bits lost”上。

**得分表述**（引自对应 MS）
- 「When the range increases the accuracy decreases // When the range decreases the accuracy increases」⟦9618_s24_32:1(a)⟧
- 「… it can only store 10 bits / digits」⟦9618_s23_32:1(b)⟧
- 「The 3 least significant digits would be truncated」⟦9618_s23_32:1(b)⟧
- 「therefore, there will be a loss of precision due to a rounding error/truncation」⟦9618_w23_31:1(b)⟧
- 「the result might be outside of the range of values possible to store in the given system」⟦9618_w25_33:2(b)⟧
- 「Following an arithmetic/logical operation」⟦9618_w22_32:1(c)⟧

**易错与失分**
- 只写“精度和范围会变”：要说出**哪一边增加时哪一项提高**。考官报告指出拿分的答案说清了“尾数位增加 → 精度提高、阶码位减少 → 范围缩小”（⟦9618_s24_32:1(a)⟧ 的考官报告）。
- 不能精确表示的题不给具体数字：考官报告指出拿高分的考生说出了尾数可用的具体位数和后果（⟦9618_s23_32:1(b)⟧ 的考官报告）。
- 下溢只写“数太小”：考官报告指出很少有人写出“这种很小的数通常是运算后产生的”（⟦9618_w22_32:1(c)⟧ 的考官报告），那是第一分。
- 把上溢、下溢弄反：上溢 = 太大（超出最大值），下溢 = 太小（比能表示的最小值还接近 0）。

#### 代表题精讲　⟦9618_s23_32:1(b)⟧

**在考什么**　10 位尾数、6 位阶码，补码。Describe the reason why the normalised form of the following binary number cannot be represented accurately using this system: `0101011.111001`. 3 分，MS 四点 Max 3。

**完整作答**
1. 规格化后尾数需要是 `0.101011111001`，共 13 位（1 位符号 + 12 位）。
2. 而这个系统的尾数只能存 10 位。
3. 所以最低的 3 位（`001`）会被截掉。
4. 结果存进去的数会损失精度（不再精确等于原数）。

**与 MS 对齐**　1 → MP1「the mantissa of the number would need to be 0.101011111001 / 13 bits」⟦9618_s23_32:1(b)⟧，2 → MP2「… it can only store 10 bits / digits」⟦9618_s23_32:1(b)⟧，3 → MP3，4 → MP4。四点任三点满分，四点都写最稳。

**英文作答句**　The mantissa of the normalised number would need to be 0.101011111001, which is 13 bits, but the system can only store 10 bits in the mantissa. The 3 least significant digits would be truncated, causing a loss of precision.

**直观**　尾数格子就是计算器屏幕的位数：数有 13 位而屏幕只有 10 位，最后 3 位只能丢掉，显示的就只是近似值。

**迁移与卡点**
- **卡点**：说清“哪一边变了、哪一项跟着变”——尾数位管精度、阶码位管范围，总位数固定时此消彼长；回答“存不准”时要给出具体数字（需要几位、只有几位、截掉几位）。
- **考官在换什么**：位数分配的影响、某数为什么存不准（位数不够 / 0.2 这类无法用 2 的负幂凑出）、上溢 / 下溢何时发生。后果一律落到 precision lost / rounding error / truncation / most significant bits lost。
- **从代表题到变式**：代表题是“某个数存不准”（算出需要 13 位 vs 只有 10 位）；变式是“改分配的影响”——尾数少 2 位 → 精度降低，阶码多 2 位 → 范围增大，两个方向都写。搬过去的是“精度 ↔ 尾数、范围 ↔ 阶码”；要换的是从具体数字转到两条因果句。
- **反例**：只写“精度和范围会变”；上溢下溢弄反；下溢没写“运算之后产生的很小的数”。

**下一道变式**　⟦9618_w25_33:2(a)⟧　（12 + 4 位改成 10 + 6 位：尾数少 2 位 → 精度降低，阶码多 2 位 → 范围增大，三点都要写。）

<!-- auto:drills P3-DR-12 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| DR-01 vs DR-02 / 03 / 05 | 只用文字说类型是什么 → DR-01；要写 `TYPE` 语句 → 写声明的题型 | 有没有 Write pseudocode |
| 枚举 vs 集合 | 枚举：`TYPE 名 = (值, …)` 一行；集合：`TYPE 名 = SET OF 类型` + `DEFINE 集合名 (…) : 类型名` 两行 | 题干是否说 “the set data type”；MS 以该题为准（⟦9618_s23_31:4(a)⟧ 说 set、给的是枚举） |
| `TYPE` vs `DECLARE` | `TYPE` 定义新类型（枚举、指针、记录、集合）；`DECLARE` 声明变量或记录里的字段 | 要“造类型”还是“要一个变量” |
| DR-03 vs DR-04 | 写类型定义 `TYPE … ENDTYPE` → DR-03；为已定义的类型声明变量、给字段赋值 → DR-04 | 有没有 “set up a variable” / “store the details” |
| `"house"` vs `house` | 字段是 STRING → 加双引号；字段是枚举 → 不加引号 | 看字段的类型，不看值长什么样 |
| DR-06 vs DR-07 | 记录怎样排列、用在哪里 → DR-06；怎样找到一条记录 → DR-07 | organised 还是 accessed / find a record |
| 顺序组织 vs 顺序存取 | sequential organisation 是“按键排好”；sequential access 是“从头逐条找”，串行、顺序文件都可用 | organisation 还是 access |
| DR-07 vs DR-08 | 怎样在随机文件里直接存取 → DR-07（散列是手段）；问散列算法本身、算散列值、冲突 → DR-08 | 题干的主语是 access 还是 hashing / collision |
| DR-09 vs DR-10 | 位串 → 十进制 → DR-09；十进制 → 位串 → DR-10 | 格子是填好的还是空的 |
| DR-10 vs DR-11 | 给的是十进制数 → DR-10；给的是二进制数或未规格化位串、问最大最小值 → DR-11 | 题目里的数是不是只由 0、1 组成 |
| DR-11 vs DR-12 | 要写出位串 → DR-11；只用文字解释精度、范围、上溢下溢 → DR-12 | 有没有 Mantissa / Exponent 格子要填 |
| 精度 vs 范围 | 精度由尾数位数决定；范围由阶码位数决定 | 改的是尾数还是阶码 |
| 上溢 vs 下溢 | 上溢：结果太大，超出最大值；下溢：结果太小（太接近 0），阶码不够负 | 计算结果比最大值大，还是比最小正数小 |
