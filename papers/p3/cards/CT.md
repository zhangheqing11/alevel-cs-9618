## CT　计算思维与问题求解 {#ch-CT}

<!-- auto:chapter-stats -->

### 核心思想

CT 对应考纲 19.1（算法）与 19.2（递归），是 P3 里**最像 P2** 的一章：一半的分要写伪代码，另一半是“说清楚算法怎样工作”。12 个题型分三块：

1. **查找与排序**（CT-01 至 CT-04）：说出二分查找的前提与步骤（CT-01）；补全线性 / 二分查找的伪代码（CT-02）；写插入排序（CT-03）；用 Big O 比较算法的效率（CT-04）。
2. **抽象数据类型 ADT**（CT-05 至 CT-09）：ADT 的种类、栈与队列的比较、用一种 ADT 实现另一种（CT-05）；用数组 + 指针实现栈（CT-06）、队列（CT-07）；链表的指针表与查找（CT-08）；二叉树的结点图、存储表与查找（CT-09）。
3. **递归**（CT-10 至 CT-12）：递归的定义、三个要素与适用场合（CT-10）；为什么用栈实现递归、编译器怎样用栈（CT-11）；追踪递归函数（CT-12）。

整章有一条主线：**指针就是下标**。栈的 Top、队列的 Front / Rear、链表的 NextPointer、二叉树的 LeftPtr / RightPtr，都是存着数组下标的整数变量；“移动指针”就是给这个整数加 1、减 1 或换成另一格里存的下标。写代码前先抄下三件事：**数组的上下界、指针指的是“最后一个值”还是“下一个空位”、空指针用哪个值（0 还是 −1）**。这三件事定了，判满判空的条件、先移指针还是先存值，就都定了。

和 P2 的关系：P2-DT-08（冒泡排序）、P2-DT-12 至 DT-16（栈、队列、链表）是本章的 AS 版；P3 在此基础上加了二分查找、插入排序、Big O、二叉树和递归。P4 用 Python 写同样的算法（见各卡的“与阶梯 / P4 的衔接”）。

### 本章伪代码速查（2027–29 指南写法）

```pseudocode
// integer division for the middle index: DIV, never /
Mid ← (Low + High) DIV 2

// a stack on a 1-based array; Top points to the LAST item added, 0 = empty
CONSTANT Capacity = 25
DECLARE Top : INTEGER
DECLARE Stack : ARRAY[1:25] OF REAL

// a node of a binary tree stored in an array of records
TYPE TreeNode
   DECLARE LeftPtr : INTEGER
   DECLARE Data : STRING
   DECLARE RightPtr : INTEGER
ENDTYPE
DECLARE BinTree : ARRAY[0:7] OF TreeNode
NowPtr ← BinTree[NowPtr].LeftPtr          // follow a pointer: the pointer is an index

// calling: a procedure with CALL, a function inside an expression
CALL Push(MyData)
OUTPUT "The data removed from the stack is ", Pop()
```

### 题型树
<!-- auto:type-tree -->

### P3-CT-01　线性查找与二分查找：条件与步骤　{#P3-CT-01}

<!-- auto:stats P3-CT-01 -->

**考法**　①说出二分查找的前提（1 分）；②用文字描述二分查找怎样进行（4 分，按步骤给分）；③比较线性查找与二分查找的方法（4 分，常要求同时写 Big O——那几分属于 CT-04 的内容）。不写代码。

**识别信号**　State the necessary condition for a binary search；State a condition that must be true for an array to be searchable for a binary search；Describe how to perform a binary search；Compare the methods used by the linear and binary search algorithms。

**解题思路**
1. **前提**只有一句：数组（表）里的数据必须**已排序**（升序或降序）。线性查找没有这个要求。
2. **二分查找的步骤**按顺序写，一句一步：
   - 找到中间元素（中间下标）；
   - 把中间元素与要找的值比较；
   - 相等 → 找到了；
   - 不相等 → 判断目标比中间值大还是小，**舍去不可能包含目标的那一半**；
   - 对剩下的一半重复以上步骤，直到找到，或只剩一个元素仍不相等（下界大于上界）为止。
3. **比较两种查找的方法**：每一点都写成“线性 …，二分 …”的对照：线性从第一个元素开始逐个比较，直到找到或到达末尾；二分从中间开始、每次舍去一半；二分要求数据有序、线性不要求；二分在找到目标之前的比较次数通常少得多。
4. 题目加了 Refer to Big O：另写 O(n)、O(log₂ n)，并说明 Big O 表示算法的时间 / 空间复杂度（写法见 CT-04）。

**得分表述**（引自对应 MS）
- 「The list to be searched must be ordered/sorted」⟦9618_s22_32:8(b)(i)⟧
- 「Find the middle item / index」⟦9618_s22_32:8(b)(ii)⟧
- 「discard the half of the list that does not contain the search item」⟦9618_s22_32:8(b)(ii)⟧
- 「Repeat the above steps until the item searched for is found」⟦9618_s22_32:8(b)(ii)⟧
- 「Linear search sequentially checks each element of the array / list」⟦9618_s24_32:8(b)⟧
- 「The binary search requires the elements to be sorted」⟦9618_s24_32:8(b)⟧

**易错与失分**
- 问二分查找，却描述了线性查找：考官报告指出有少数考生这样答（⟦9618_s22_32:8(b)(ii)⟧）。
- 只写“它把表分成两半”：要写出**比较中间值 → 决定舍去哪一半 → 重复**这一串动作，以及什么时候停。
- 漏了“找不到”的结束条件：只剩一个元素仍不相等、或下界超过上界。
- 前提写成“数组不能太大”“数据要是数字”：唯一的前提是有序。
- 比较题只写一边（只描述二分查找）：每一点都要两边对照。

#### 代表题精讲　⟦9618_s22_32:8(b)(ii)⟧

**在考什么**　情境：可以用二分查找或线性查找在数组里找一个值。Describe how to perform a binary search. 4 分；MS 列了 7 个点，Any four from。讲解时对照原卷 QP p.11（同页上方是 8(a) 线性查找的伪代码）。

**完整作答**（5 句，多写一句作保险）
1. Find the middle item of the list.
2. Compare the middle item with the item being searched for; if they are equal, the item has been found.
3. If it is not equal, decide whether the search item is greater or less than the middle item …
4. … and discard the half of the list that cannot contain the search item.
5. Repeat these steps on the remaining half until the item is found, or until there is only one item left and it is not the search item (the lower bound becomes greater than the upper bound).

**与 MS 逐点对齐**（MS p.9）

| MP | MS 要点 | 作答中对应 |
|:--|:--|:--|
| 1 | Find the middle item / index | 第 1 句 |
| 2 | Check the value of middle item in the list to be searched | 第 2 句前半 |
| 3 | If equal item searched for is found | 第 2 句后半 |
| 4 | If this is not equal/greater/less than the item searched for | 第 3 句 |
| 5 | … discard the half of the list that does not contain the search item | 第 4 句 |
| 6 | Repeat the above steps until the item searched for is found | 第 5 句前半 |
| 7 | … or there is only one item left in the list and it is not the item searched for // lower bound > / = upper bound | 第 5 句后半 |

7 个点里任意 4 个就满分；MP5、MP7 前面的“…”表示它们要跟在前一句后面才成立。

**英文作答句**　Find the middle item and compare it with the search item. If they are equal, the item is found. If not, discard the half of the list that does not contain the search item, and repeat on the remaining half until the item is found or only one item is left and it is not the search item.

**直观**　翻字典找一个词：翻到中间一页，看目标在前半本还是后半本，把另一半整个放下，再在剩下的一半里翻中间——每翻一次，要看的页数减半。前提是字典按字母排好了序。

**下一道变式**　⟦9618_s24_32:8(b)⟧　（比较线性与二分查找的**方法**，并要求写 Big O：方法最多 3 分、Big O 最多 2 分，共 4 分。）

<!-- auto:drills P3-CT-01 -->

### P3-CT-02　写或补全查找算法　{#P3-CT-02}

<!-- auto:stats P3-CT-02 -->

**考法**　①补全二分查找的伪代码（填空，5–6 分）：用两个 BOOLEAN 标志的 `WHILE`、或 `REPEAT … UNTIL Exit`；②补全线性查找的伪代码（4 分）；③补全函数形式的二分查找，找到返回下标、找不到返回 −1，并补全变量说明表（标识符、类型、说明）。

**识别信号**　Complete this pseudocode algorithm for a linear search；Complete the given pseudocode to find an item in a 1D array … using a binary search；Complete this pseudocode binary search algorithm；Complete the pseudocode for the function to perform a binary search；Complete the following table to define the variables used in the function。

**解题思路**
1. **先读题给代码**：哪种查找；循环是 `WHILE`（前测）还是 `REPEAT`（后测）；上下界变量叫什么、数组下标从 0 还是 1 起；有哪些标志（Found、NotInList、Exit）。填空只填空，题目已给的行不改，但要顺着它的约定填。
2. **二分查找的五个部件**：
   - 初值：下界 = 数组下界，上界 = 数组上界；标志设 FALSE。
   - 循环条件：还没找到，并且范围不空（`Low <= High`，或两个标志都是 FALSE）。
   - 中点：`Mid ← (Low + High) DIV 2`，必须用 `DIV`。
   - 比较：相等 → 找到（置标志 / `RETURN Mid`）。
   - 不相等：目标比中间值大 → `Low ← Mid + 1`；小 → `High ← Mid - 1`；范围已空 → 置“不在表中”标志 / 循环后 `RETURN -1`。
3. **线性查找**：下标从下界开始；循环里比较 → 相等置 Found；下标加 1；结束条件是“找到或越过上界”。上界是数组的上界：`ARRAY[0:9]` 的上界是 9，不是 10。
4. **变量说明表**：上下界与中点都是 INTEGER（它们是下标）；要找的项与数组元素同类型；说明写“搜索范围的最低 / 最高 / 中间下标”“要找的项”。
5. **不依赖 AND 短路**（决策 D25）：`WHILE` 条件里只放标志和下标的比较，取数组元素放进循环体。

**伪代码模板**

```pseudocode
// binary search: global Names : ARRAY[1:500] OF STRING, sorted A-Z
FUNCTION BinarySearch(SearchItem : STRING) RETURNS INTEGER
   DECLARE Low : INTEGER
   DECLARE High : INTEGER
   DECLARE Mid : INTEGER
   Low ← 1                                    // lower bound of the array
   High ← 500                                 // upper bound of the array
   WHILE Low <= High                          // the search area is not empty
      Mid ← (Low + High) DIV 2
      IF Names[Mid] = SearchItem THEN
         RETURN Mid                           // found
      ELSE
         IF Names[Mid] < SearchItem THEN
            Low ← Mid + 1                     // discard the lower half
         ELSE
            High ← Mid - 1                    // discard the upper half
         ENDIF
      ENDIF
   ENDWHILE
   RETURN -1                                  // not found
ENDFUNCTION

// linear search with a flag: Index stays on the item that was found
Found ← FALSE
Index ← 1
WHILE Found = FALSE AND Index <= 500
   IF Names[Index] = SearchItem THEN
      Found ← TRUE
   ELSE
      Index ← Index + 1
   ENDIF
ENDWHILE
```

**得分表述**（引自对应 MS）
- 「Found ← FALSE」⟦9618_s24_31:10(b)⟧
- 「WHILE Found = FALSE AND NotInList = FALSE」⟦9618_s24_31:10(b)⟧
- 「TopOfList ← CurrentItem + 1」⟦9618_s24_31:10(b)⟧
- 「Test if upper bound is less than lower bound」⟦9618_w22_31:12(a)⟧
- 「Re-setting of mid value if current value is lower than the target」⟦9618_w22_31:12(a)⟧
- 「IF Found = FALSE AND Count > EndOfList THEN」⟦9618_s24_32:8(a)⟧

**得分点地图**（口径：核验语料、主题型为本型、已拆得分点的行；同一行同一标签计一次；去掉 `equivalent_of` 行，并去掉与 ⟦9618_s24_31:10(b)⟧ 逐字相同的 ⟦9618_s24_33:10(b)⟧。共 5 行：⟦9618_s22_32:8(a)⟧、⟦9618_s24_31:10(b)⟧、⟦9618_s24_32:8(a)⟧、⟦9618_w22_31:12(a)⟧，以及 s26 的一道）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 初值：标志设 FALSE、上界设数组上界、左右下标设初值 | 4 | `initialise-variables` |
| 比较：目标 = 当前元素；上界 < 下界 | 4 | `relational-ops` |
| 循环：两个标志都为 FALSE 时继续 / 范围不空时继续 / `UNTIL Exit` | 4 | `pre-condition-loop` 3、`post-condition-loop` 1 |
| 二分：中点、按大小移动上下界（`Mid + 1`、`Mid - 1`） | 3 | `binary-search`（取中点另标 `div-mod` 1） |
| 标志：找到 / 不在表中时置 TRUE | 3 | `flag-variable` |
| 两个条件用 AND 连起来 | 2 | `logic-ops` |
| 线性：上界、越过上界的判断、下标加 1 | 2 | `linear-search`、`loop-bounds` |
| 函数头；找到返回位置、找不到返回 −1 | 1 | `module-header`、`return-value` |
| 线性查找填空里的类型、下标加 1、没找到的提示 | 1 | `data-types`、`accumulator`、`output-format` |

**易错与失分**
- `Mid ← (Low + High) / 2`：`/` 的结果是实数，不能当下标。
- 移动上下界写成 `Low ← Mid` / `High ← Mid`：范围可能不再缩小，循环停不下来。
- 线性查找的上界多 1：`ARRAY[0:9]` 写成 10。考官报告指出常见错误是 MaxIndex 设大了一个，以及在“没找到”的输出里也带上 Index（⟦9618_s22_32:8(a)⟧）。
- REPEAT 版二分查找：考官报告指出典型错误是循环开头的 IF 写错、新的 Lower / Upper 赋值写错、REPEAT 的结束条件写错（⟦9618_w22_31:12(a)⟧）。该题 MS 的范例在置 `Exit ← TRUE` 之后仍会计算 Mid 并读 `Names[Mid]`——填空照 MS 填；自己写时用模板里的 `WHILE Low <= High`。
- 函数头漏 `RETURNS INTEGER`；找不到时没有 `RETURN -1`。
- 比较方向写反：数组升序时，目标 **大于** 中间值才去右半边（`Low ← Mid + 1`）。

#### 代表题精讲　⟦9618_s24_31:10(b)⟧

**在考什么**　Complete the given pseudocode to find an item in a 1D array `Names` of type STRING using a binary search. 题目给出 `Names : ARRAY[1:100000] OF STRING`、`TopOfList ← 1`、`EndOfList ← 100000`、标志 `Found`、`NotInList`，留 5 处空。5 分，每填对一行 1 分。讲解时对照原卷 QP p.10。

**完整作答**（需要填的是带注释的 5 行）

```pseudocode
DECLARE Names : ARRAY[1:100000] OF STRING
DECLARE TopOfList : INTEGER
DECLARE EndOfList : INTEGER
DECLARE CurrentItem : INTEGER
DECLARE ToFind : STRING
DECLARE Found : BOOLEAN
DECLARE NotInList : BOOLEAN
TopOfList ← 1
EndOfList ← 100000
OUTPUT "Which name do you wish to find? "
INPUT ToFind
Found ← FALSE                                       // gap 1
NotInList ← FALSE
WHILE Found = FALSE AND NotInList = FALSE           // gap 2 (both halves)
   CurrentItem ← (TopOfList + EndOfList) DIV 2
   IF ToFind = Names[CurrentItem] THEN              // gap 3
      Found ← TRUE
   ELSE
      IF TopOfList >= EndOfList THEN
         NotInList ← TRUE                           // gap 4
      ELSE
         IF ToFind > Names[CurrentItem] THEN
            TopOfList ← CurrentItem + 1             // gap 5
         ELSE
            EndOfList ← CurrentItem - 1
         ENDIF
      ENDIF
   ENDIF
ENDWHILE
IF Found = TRUE THEN
   OUTPUT "Item found at position ", CurrentItem, " in array"
ELSE
   OUTPUT "Item not in array"
ENDIF
```

**与 MS 逐点对齐**（MS p.12，One mark for each correctly completed line）

| MP | MS 原文 | 为什么这样填 |
|:--|:--|:--|
| 1 | Found ← FALSE | 下一行已有 `NotInList ← FALSE`，两个标志都要在循环前设初值 |
| 2 | WHILE Found = FALSE AND NotInList = FALSE | 两个空合起来一分：没找到、也还没断定不在表中 |
| 3 | IF ToFind = Names[CurrentItem] // Names[CurrentItem] = ToFind THEN | THEN 分支是 `Found ← TRUE`，所以这里是“相等” |
| 4 | NotInList ← TRUE | 范围只剩一个（或已空）且不相等 → 不在表中 |
| 5 | TopOfList ← CurrentItem + 1 | 目标比中间值大 → 舍去下半部分；ELSE 分支已给出 `EndOfList ← CurrentItem – 1` |

**规范代码要点**　五个空里有三个可以从**对称**推出来：已经有 `NotInList ← FALSE` 就补 `Found ← FALSE`；ELSE 里是 `EndOfList ← CurrentItem – 1`，对面就是 `TopOfList ← CurrentItem + 1`；THEN 里置 Found，条件就是“相等”。

**直观**　猜 1 到 100000 之间的数：每次猜中间，对方说“大了 / 小了”，你就把一半的数划掉。最多猜 17 次左右，因为 2¹⁷ > 100000。

**同题 Python 版要点**
- 下标从 0 起：`top_of_list = 0`、`end_of_list = len(names) - 1`；中点用 `//`。
- `while not found and not not_in_list:`；不能用 `names.index(to_find)` 或 `in` 代劳（决策 D10）。

**与阶梯 / P4 的衔接**　先过阶梯 **L11 E03**（迭代与递归的二分查找）；线性查找见 **L06 E02**。P4 要求用 Python 写迭代二分查找，例如 ⟦9618_s24_41:1(e)(i)⟧；递归版见 ⟦9618_s22_42:2(c)(i)⟧。

**下一道变式**　⟦9618_s24_32:8(a)⟧　（同一套变量名换成**线性**查找：补 `Found ← FALSE`、循环条件、相等判断、`IF Found = FALSE AND Count > EndOfList THEN`，4 分。）

<!-- auto:drills P3-CT-02 -->

### P3-CT-03　写或补全排序算法　{#P3-CT-03}

<!-- auto:stats P3-CT-03 -->

**考法**　①按题给标识符表写插入排序（4–5 分，常要求升序，并说明“不必声明变量”）；②两个或三个**并行数组**同步排序：移动一个数组的元素时，另一个数组的对应元素也要一起移动；③把题给的冒泡排序改写成实现同样功能的插入排序（2021 扩展卷）。

**识别信号**　Write the pseudocode for an insertion sort to sort the array into ascending order；Use the identifiers from the table in your algorithm；Make sure that the data in both arrays is swapped as required；The given algorithm is a simple bubble sort … perform the same task using an insertion sort。

**解题思路**
1. **外层循环**从第二个元素到最后一个：下界为 1 的数组写 `FOR Index ← 2 TO n`，下界为 0 的写 `FOR Index ← 1 TO n - 1`。
2. 循环一开始**先把当前元素存进临时变量**（Value / Temp），插入位置设为 `Index - 1`。
3. **内层条件循环**：插入位置还没越过下界，并且那里的元素比临时值大（升序；降序用“小”）→ 把它往后挪一格 `A[Pos + 1] ← A[Pos]`，插入位置减 1。
4. 内层循环结束后（**在内层循环外面**）把临时值放进 `A[Pos + 1]`。
5. **并行数组**：临时保存、后移、放回这三步，每个数组都要各做一次。
6. **不依赖 AND 短路**（决策 D25）：`WHILE Pos >= 1 AND A[Pos] > Value` 在 Pos 变成 0 时可能去读 `A[0]`；用一个标志结束内层循环（与阶梯 L11 §4 的写法相同）。

**伪代码模板**

```pseudocode
// DataArray : ARRAY[1:1000] OF INTEGER, sorted into ascending order
DECLARE Index : INTEGER
DECLARE Position : INTEGER
DECLARE Value : INTEGER
DECLARE KeepGoing : BOOLEAN
FOR Index ← 2 TO 1000
   Value ← DataArray[Index]                   // copy the item to insert
   Position ← Index - 1
   KeepGoing ← TRUE
   WHILE KeepGoing = TRUE                     // inner loop
      IF Position < 1 THEN
         KeepGoing ← FALSE                    // passed the lower bound
      ELSE
         IF DataArray[Position] > Value THEN
            DataArray[Position + 1] ← DataArray[Position]    // move up one place
            Position ← Position - 1
         ELSE
            KeepGoing ← FALSE                 // insertion point found
         ENDIF
      ENDIF
   ENDWHILE
   DataArray[Position + 1] ← Value            // re-insert outside the inner loop
NEXT Index

// parallel arrays: every step is done to BOTH arrays
//    Temp1 ← ID[Index]           Temp2 ← Name[Index]
//    ID[Position + 1] ← ID[Position]
//    Name[Position + 1] ← Name[Position]
//    ID[Position + 1] ← Temp1    Name[Position + 1] ← Temp2
```

**得分表述**（引自对应 MS）
- 「Temporary assignment of the element being ‘inserted’ before inner loop」⟦9618_s25_33:12(b)⟧
- 「Check if current DataArray content is > Value」⟦9618_s25_33:12(b)⟧
- 「Moving data to adjacent element as required」⟦9618_s25_33:12(b)⟧
- 「Re-insertion of the element outside the inner loop」⟦9618_s25_33:12(b)⟧
- 「Use of WHILE loop with correct exit clause」⟦9618_s21_31:8(b)⟧
- 「Moving of all three elements of data to next array elements」⟦9618_s21_31:8(b)⟧

**得分点地图**（口径同 CT-02；本型核验语料只有 2 行，都已拆分：⟦9618_s25_33:12(b)⟧ 与 s26 的一道）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 内层条件循环（嵌在外层 FOR 里） | 2 | `pre-condition-loop`、`nested-loops`、`insertion-sort` |
| 把元素后移到相邻位置 | 2 | `shift-values`、`insertion-sort` |
| 插入位置减 1 | 2 | `array-index` |
| 循环前临时保存要插入的元素（及插入位置的初值） | 2 | `assign-value` 1、`initialise-variables` 1 |
| 比较：当前元素 > 临时值 | 1 | `relational-ops` |
| 外层循环从第二个元素开始、到数组末尾 | 1 | `count-loop`、`loop-bounds` |
| 并行数组同步移动 | 1 | `parallel-arrays` |

**易错与失分**
- 写成了冒泡排序（相邻比较交换）：考官报告指出这是最常见的错误之一（⟦9618_s25_33:12(b)⟧）。
- 外层循环从第一个元素开始：第一个元素自己已经是“排好的部分”。
- 把放回临时值的语句写在内层循环**里面**：每挪一格就写一次，结果错乱。
- 并行数组只移动了一个：ID 排好了，名字却对不上人。
- 题目给了标识符表却换了名字：题目说 Use the identifiers from the table，就用表里的名字。

#### 代表题精讲　⟦9618_s25_33:12(b)⟧

**在考什么**　一维数组 DataArray 最多 1000 个整数，要排成升序。Write the pseudocode for an insertion sort。标识符表：Index（外层循环计数）、Position（内层循环计数——插入位置）、DataArray、Value（要插入的值）。不必声明数组和变量；第一行已给出 `FOR Index ← 2 to 1000`。4 分，MS 列 6 个点（Max 4）。讲解时对照原卷 QP p.14。

**完整作答**（按决策 D25 用标志结束内层循环；KeepGoing 是表外新增的 BOOLEAN 变量）

```pseudocode
FOR Index ← 2 TO 1000
   Value ← DataArray[Index]
   Position ← Index - 1
   KeepGoing ← TRUE
   WHILE KeepGoing = TRUE
      IF Position < 1 THEN
         KeepGoing ← FALSE
      ELSE
         IF DataArray[Position] > Value THEN
            DataArray[Position + 1] ← DataArray[Position]
            Position ← Position - 1
         ELSE
            KeepGoing ← FALSE
         ENDIF
      ENDIF
   ENDWHILE
   DataArray[Position + 1] ← Value
NEXT Index
```

**与 MS 逐点对齐**（MS p.15）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | Temporary assignment of the element being ‘inserted’ before inner loop | `Value ← DataArray[Index]` |
| 2 | Appropriate inner loop | `WHILE KeepGoing = TRUE … ENDWHILE` |
| 3 | Check if current DataArray content is > Value | `IF DataArray[Position] > Value THEN` |
| 4 | Moving data to adjacent element as required | `DataArray[Position + 1] ← DataArray[Position]` |
| 5 | Appropriate updating of Position variable | `Position ← Index - 1`、`Position ← Position - 1` |
| 6 | Re-insertion of the element outside the inner loop | 循环后的 `DataArray[Position + 1] ← Value` |

6 个点任得 4 个满分。MS 的范例写的是 `WHILE Position >= 1 AND DataArray[Position] > Value`，外面还套了一层 `IF DataArray[Position] > Value THEN`；这种写法依赖 AND 短路（Position 为 0 时会去读 `DataArray[0]`），本手册不这样写，但上表六点在标志写法里都一一对得上。

**规范代码要点**　插入排序的“形状”只有三件事：**拿出来（Value）→ 大的往后挪（内层循环）→ 放回空位（循环外）**。冒泡排序没有“拿出来”这一步，看到自己写了 `Temp ← A[i]; A[i] ← A[i+1]; A[i+1] ← Temp` 就说明写成冒泡了。

**直观**　理扑克牌：左手是已经理好的牌，右手每次拿一张新牌，从右往左跟左手的牌比，比它大的牌都往右让一格，让出的空位就是新牌的位置。

**同题 Python 版要点**
- Python 的 `and` 会短路，所以 `while position >= 0 and data_array[position] > value:` 在 Python 里是安全的；伪代码里不这样写。
- 不能用 `sort()` / `sorted()` 代劳（决策 D10）。

**与阶梯 / P4 的衔接**　先过阶梯 **L11 E04**（一次插入 + 完整插入排序）；冒泡排序对照 **L06 E03**。P4 要求用 Python 写插入排序，例如 ⟦9618_s25_43:2(b)⟧（不得用内置排序函数）、⟦9618_w22_42:1(e)⟧（二维数组按优先级排序）。

**下一道变式**　⟦9618_s21_31:8(b)⟧　（2021 扩展卷：把题给的降序冒泡排序改写成插入排序，分数数组与二维的名字数组三项一起移动，6 分。核验语料里本型只有两道，另一道在 s26，留作模考。）

<!-- auto:drills P3-CT-03 -->

### P3-CT-04　算法效率与大 O 表示法　{#P3-CT-04}

<!-- auto:stats P3-CT-04 -->

**考法**　①写出某个算法的 Big O（线性查找、插入排序最坏情况）；②解释 O(log n) 对二分查找意味着什么；③描述数据量增加时查找时间怎样变化（Refer to Big O）；④用 Big O 比较二分查找与线性查找；⑤说出影响排序性能的因素并说明怎样影响。

**识别信号**　State the Big O notation for time complexity of …；Describe the meaning of O(log n) as it applies to a binary search；Describe the performance of a binary search in relation to the number of data items；Compare the performance of the algorithms … using Big O notation；factors … that may affect the performance of a sorting algorithm。

**解题思路**
1. **背这张表**（最坏情况的时间复杂度）：

| 算法 | Big O | 一句话 |
|:--|:--|:--|
| 线性查找 | O(n) | 时间随数据量**线性**增长 |
| 二分查找 | O(log n)（MS 也写 O(log₂ n)） | 时间随数据量**对数**增长：数据量指数增长时，时间只线性增长 |
| 插入排序、冒泡排序 | O(n²) | 数据量翻倍，时间约变 4 倍 |

2. **Big O 是什么**：表示算法的时间（或空间）复杂度，通常指最坏情况。
3. **描述“怎样随数据量变化”**的两句标准句：线性——the time increases linearly as the number of items increases；二分——the time increases logarithmically as the number of items increases linearly // the time increases linearly as the number of items increases exponentially。
4. **比较题**：先并排写两个 Big O，再写“线性增长 vs 对数增长”，最后写“二分查找的时间增长得慢、线性增长得快”。
5. **排序性能的因素**：每个因素后面都要写**怎样影响**——数据项越多，排序越慢；数据已经部分有序，（插入）排序越快、完全乱序则越慢。

**得分表述**（引自对应 MS）
- 「Linear search O(n) and Binary search O(log2n) / O(Log n)」⟦9618_s22_32:8(c)⟧
- 「time to search increases less rapidly for a binary search and time to search increases more rapidly for a linear search」⟦9618_s22_32:8(c)⟧
- 「The time taken goes up linearly as the number of items rises exponentially」⟦9618_w22_31:12(b)(ii)⟧
- 「Big O notation is used to indicate the time/space complexity of an algorithm」⟦9618_s24_31:10(c)⟧
- 「The time taken to complete the search increases logarithmically as the number of search items increases linearly」⟦9618_s24_31:10(c)⟧
- 「The performance of a sorting routine should improve if the data is already partially sorted」⟦9618_s25_33:12(c)⟧

**易错与失分**
- 问 O(log n) 的含义，却去比较二分与线性查找：考官报告指出有考生这样误读题意（⟦9618_w22_31:12(b)(ii)⟧）。
- 只写 Big O 不解释：考官报告指出很多考生会写 Big O，但很少有人真正说明它的含义（⟦9618_s22_32:8(c)⟧）。
- 排序因素只说名称（“数据量”“初始顺序”）不说影响：考官报告指出很多考生没有描述因素怎样影响性能，拿不到满分（⟦9618_s25_33:12(c)⟧）。
- “二分查找的时间不随数据量变化”：会变，只是变得慢（对数）。
- 把 O(log n) 说成“比较 log n 个元素”而不说“随数据量对数增长”。

#### 代表题精讲　⟦9618_s22_32:8(c)⟧

**在考什么**　Compare the performance of the algorithms for a binary search and a linear search using Big O notation for order of time complexity. 3 分，MS 3 个点。讲解时对照原卷 QP p.12。

**完整作答**
1. A linear search is O(n) and a binary search is O(log₂ n).
2. For a linear search the time to search increases linearly with the number of items in the list, whereas for a binary search it increases logarithmically.
3. So as the list gets larger, the time to search increases less rapidly for a binary search and more rapidly for a linear search.

**与 MS 逐点对齐**（MS p.9）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | Linear search O(n) and Binary search O(log2n) / O(Log n) | 第 1 句：两个 Big O **都要有**（MS 用 **and**） |
| 2 | time to search increases linearly in relation to the number of items in the list for a linear search and logarithmically for a Binary search | 第 2 句 |
| 3 | time to search increases less rapidly for a binary search and time to search increases more rapidly for a linear search | 第 3 句 |

**英文作答句**　Linear search is O(n) and binary search is O(log n): the search time grows linearly with the number of items for a linear search but only logarithmically for a binary search, so it grows less rapidly for a binary search.

**直观**　1000 个名字：线性查找最坏要看 1000 个；二分查找最多看 10 个左右（2¹⁰ = 1024）。数据涨到 100 万，线性要看 100 万个，二分只要 20 个左右。

**下一道变式**　⟦9618_w22_31:12(b)(ii)⟧　（只解释 O(log n) 对二分查找的含义，2 分：对数时间、数据量指数增长时时间只线性增长、它是最坏情况。）

<!-- auto:drills P3-CT-04 -->

### P3-CT-05　ADT 的概念、选择与相互实现　{#P3-CT-05}

<!-- auto:stats P3-CT-05 -->

**考法**　①举出其他 ADT（栈、队列、链表、二叉树、图）；②说出栈的其他用途；③比较栈与队列的异同；④说明为什么打印任务用队列比用栈好；⑤说明为什么用链表而不是数组实现栈；⑥说明用两个栈实现队列时怎样加入新元素。考纲还列了字典（dictionary），语料中尚未单独出题。

**识别信号**　Identify two (other) ADTs；State two other uses of a stack；Compare and contrast the queue and stack Abstract Data Types；Explain the reasons why a queue ADT works better than a stack ADT in …；Justify the use of a linked list instead of an array to implement a stack；if it is implemented using two stacks。

**解题思路**
1. **ADT 名单**：stack、queue、linked list、binary tree、graph（考纲另有 dictionary）。题目已经给出的那个不要再写。
2. **栈的用途**（⟦9618_s22_31:5(c)⟧ 的 MS 所列）：递归、过程调用（保存返回地址）、中断处理（保存寄存器内容）、实现其他 ADT（如链表）。那道题的情境本身就是 RPN 求值（SY 章），所以 RPN 不算“其他”用途。
3. **栈与队列比较**：每一点两边都写——队列先进先出（FIFO）、栈后进先出（LIFO / FILO）；队列在两端（队尾进、队首出），栈只在同一端（栈顶）进出；队列有两个移动的指针，栈只有一个；**相同点**：两者大小都可以变化。
4. **为什么用队列**：任务应按到达的先后处理 → 队列先进先出，第一个送来的任务第一个打印；如果用栈，第一个送来的任务要等其他所有任务都打印完。
5. **链表 vs 数组实现栈**：两边各写一句——链表是动态结构、大小不受限制，可以按需增删结点；数组是静态结构、大小固定，满了栈就不能再扩展。
6. **两个栈实现队列（加入新元素）**：栈 1 存着队列（最新的元素在栈底）；把栈 1 的元素全部弹出、压进栈 2（顺序反过来）；把新元素压入；再把栈 2 的元素全部弹回栈 1。

**得分表述**（引自对应 MS）
- 「A queue is a first in first out / FIFO data structure and a stack is a first in last out / FILO / LIFO data structure」⟦9618_w23_31:10(c)⟧
- 「A stack has only one moveable pointer whereas a queue has two」⟦9618_w23_31:10(c)⟧
- 「Print jobs are expected to be actioned by the printer in the order they are received」⟦9618_s23_32:11(b)⟧
- 「A linked list is a dynamic data structure / not restricted in size」⟦9618_w23_32:9(b)⟧
- 「When the array is full, the stack cannot be extended any further」⟦9618_w23_32:9(b)⟧
- 「To add an element, pop all the elements from stack 1 and push onto stack 2」⟦9618_s23_31:11(c)⟧

**易错与失分**
- 比较题每句只写一种 ADT：考官报告指出“compare and contrast”要求两种 ADT 出现在同一句里，才算比较（⟦9618_w23_31:10(c)⟧）。
- 链表 vs 数组只写链表的好处：MS 是“链表一分 + 数组一分”，考官报告指出多数考生只写了一种，只得 1 分（⟦9618_w23_32:9(b)⟧）。
- 打印队列只写“队列是 FIFO”：要扣到情境——任务按到达顺序打印；如果用栈，第一个任务最后才打印。
- 把 array 当答案写进“其他 ADT”：⟦9618_s25_33:12(a)⟧ 题干已给出 array。

#### 代表题精讲　⟦9618_w23_31:10(c)⟧

**在考什么**　情境是用数组实现的栈（BasePointer、TopPointer、Stack）。Compare and contrast the queue and stack Abstract Data Types (ADT). 2 分，MS 4 个点（Max 2）。讲解时对照原卷 QP p.11（情境表在 p.10）。

**完整作答**（3 句，每句两边都写）
1. A queue is a first in first out (FIFO) structure, whereas a stack is a last in first out (LIFO) structure.
2. Items are added to and removed from a stack at the same end, but a queue adds items at one end and removes them from the other end; so a stack has one moveable pointer and a queue has two.
3. Both a stack and a queue can vary in size.

**与 MS 逐点对齐**（MS p.8）

| MP | MS 要点 | 作答中对应 |
|:--|:--|:--|
| 1 | A queue is a first in first out / FIFO data structure and a stack is a first in last out / FILO / LIFO data structure | 第 1 句 |
| 2 | Both ADTs can vary in size / are of indeterminate length | 第 3 句（这是“contrast”之外的相同点） |
| 3 | Data is popped and pushed … at the same end but it is enqueued and dequeued … at different/opposite ends | 第 2 句前半 |
| 4 | A stack has only one moveable pointer whereas a queue has two | 第 2 句后半 |

**英文作答句**　A queue is FIFO whereas a stack is LIFO; a stack is accessed at one end only (one moveable pointer) whereas a queue is accessed at both ends (two pointers); both can vary in size.

**直观**　栈是一摞盘子：放和拿都在最上面；队列是排队买票：从队尾排进来、从队首离开。

**下一道变式**　⟦9618_s23_31:11(c)⟧　（用两个栈实现队列时怎样加入新元素，4 分：为什么要两个栈 → 栈 1 的元素全部弹到栈 2 → 压入新元素 → 栈 2 的元素全部弹回栈 1。）

<!-- auto:drills P3-CT-05 -->

### P3-CT-06　用数组实现栈　{#P3-CT-06}

<!-- auto:stats P3-CT-06 -->

**考法**　①按标识符表写声明：一个 CONSTANT、两个 INTEGER 指针、一个数组（3 分）；②写初始化过程，给底指针、顶指针设初值（3 分）；③补全 Push：判满、移动顶指针、存值、满时输出提示；④补全 Pop：函数头 `RETURNS` 类型、判空、取值、顶指针减 1、返回；⑤写调用语句：输入一个值并 `CALL Push(…)`；输出 `Pop()` 的结果；⑥补全标识符表的类型与说明。

**识别信号**　A stack is to be set up / implemented using the information in the table；Write the pseudocode for the required declarations；Write pseudocode for a procedure to initialise the top and bottom pointers；Complete the pseudocode function Pop() / the procedure to add a data item onto the stack；Write pseudocode to input a new data item and add it to the stack using Push()。

**解题思路**
1. **先定约定**：本型语料里的题（w23、w25 两季，以及 2021 扩展卷）Top 都指向**栈顶那个值**（最后放进去的），空栈时 Top = Base − 1（Base 为 1 → Top 为 0；Base 为 0 → Top 为 −1）。P2-DT-16 有的题让指针指向“下一个空位”，那时顺序相反——读题时先确认。
2. **声明**：`CONSTANT Capacity = 25`（常量用 `=`，不用 `←`，不写类型）；两个指针 `DECLARE … : INTEGER`；数组 `DECLARE Stack : ARRAY[1:25] OF REAL`（元素类型照表）。
3. **Push（入栈）**：先判**满**（1 起数组 `Top < Max`；0 起数组 `Top < Max - 1`）→ 先 `Top ← Top + 1` → 再 `Stack[Top] ← NewItem`；满了按题目要求输出提示或返回 FALSE。
4. **Pop（出栈）**：先判**空**（`Top >= Base`，或 `Top > -1`）→ 先取值 `Item ← Stack[Top]` → 再 `Top ← Top - 1` → 循环 / 判断结束后 `RETURN Item`。函数头 `FUNCTION Pop() RETURNS REAL`（类型 = 数组元素类型）。
5. **调用**：过程用 `CALL Push(MyData)`；函数放在表达式里，不写 CALL：`OUTPUT "…", Pop()`。

**伪代码模板**

```pseudocode
CONSTANT Capacity = 25
DECLARE BasePointer : INTEGER
DECLARE TopPointer : INTEGER
DECLARE Stack : ARRAY[1:25] OF REAL

PROCEDURE Initialise()
   BasePointer ← 1
   TopPointer ← 0                             // empty: one below the base
ENDPROCEDURE

PROCEDURE Push(NewItem : REAL)
   IF TopPointer < Capacity THEN              // not full
      TopPointer ← TopPointer + 1             // move first ...
      Stack[TopPointer] ← NewItem             // ... then store
   ELSE
      OUTPUT "Stack full - item not added"
   ENDIF
ENDPROCEDURE

FUNCTION Pop() RETURNS REAL
   DECLARE Item : REAL
   Item ← 0
   IF TopPointer >= BasePointer THEN          // not empty
      Item ← Stack[TopPointer]                // take first ...
      TopPointer ← TopPointer - 1             // ... then move
   ELSE
      OUTPUT "Stack empty"
   ENDIF
   RETURN Item
ENDFUNCTION

// using them
INPUT MyData
CALL Push(MyData)
OUTPUT "The item removed is ", Pop()
```

**得分表述**（引自对应 MS）
- 「IF TopPointer >= BasePointer THEN」⟦9618_w23_31:10(b)⟧
- 「Item ← Stack[TopPointer]」⟦9618_w23_31:10(b)⟧
- 「IF TopPointer < MaxSize THEN」⟦9618_w23_32:9(a)(ii)⟧
- 「Top ← Top + 1」⟦9618_w25_32:12(a)(i)⟧
- 「Procedure call for Push with parameter used matching input variable」⟦9618_w25_32:12(a)(ii)⟧
- 「OUTPUT "The data removed from the stack is ", Pop()」⟦9618_w25_31:9(a)(ii)⟧

**得分点地图**（口径同 CT-02；本型核验语料 10 行，已拆分 4 行：⟦9618_w23_31:10(b)⟧、⟦9618_w23_32:9(a)(ii)⟧、⟦9618_w25_31:9(a)(i)⟧、⟦9618_w25_32:12(a)(i)⟧。其余 6 行是声明、初始化、标识符表与调用语句，MS 按条给分、未拆）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 移动顶指针（`+ 1` 入栈、`- 1` 出栈） | 4 | `stack-array` |
| 用顶指针作下标存值 / 取值 | 4 | `stack-array`、`array-index` |
| 函数 / 过程头：`RETURNS` 类型、参数及类型 | 3 | `module-header` |
| 判满 / 判空的条件 | 3 | `relational-ops` |
| `RETURN` 取出的值 | 2 | `return-value` |
| 初始化底指针、顶指针 | 1 | `initialise-variables` |
| 满时输出提示 | 1 | `output-format` |

**易错与失分**
- 常量写成变量（`DECLARE Capacity : INTEGER`）：考官报告指出这是声明题的常见错误（⟦9618_w25_33:10(a)⟧）。
- 初始化过程加了参数：考官报告指出很多考生在过程定义里写了不需要的参数（⟦9618_w25_33:10(b)⟧）。
- 顶指针与底指针的初值写反：考官报告指出这是常见错误（⟦9618_w23_32:9(a)(ii)⟧）。
- Push 的参数漏了类型：考官报告指出这是 Push 过程头的常见失分（⟦9618_w25_32:12(a)(i)⟧）。
- 调用过程漏了 `CALL`（⟦9618_w25_32:12(a)(ii)⟧）；反过来，调用函数时写了 `CALL Pop()`。
- `RETURN` 与 `RETURNS` 用反、出栈时 Top 加 1：考官报告列为 Pop 的常见错误（⟦9618_w25_31:9(a)(i)⟧）。
- 题目要求返回提示，却用 OUTPUT 输出：考官报告指出这样得分更少（⟦9618_w21_31:10(d)⟧）。

#### 代表题精讲　⟦9618_w23_31:10(b)⟧

**在考什么**　标识符表：BasePointer（INTEGER，栈底）、TopPointer（INTEGER，栈顶）、Stack（REAL，一维数组）；常量 Capacity 把栈限制为 25 项。Complete the pseudocode function Pop() to pop an item from Stack. 5 处空，5 分。讲解时对照原卷 QP p.10（同页上方是 10(a) 的声明题）。

**完整作答**（带注释的 5 行是要填的）

```pseudocode
// popping an item from the stack
FUNCTION Pop() RETURNS REAL                   // gap 1
   DECLARE Item : REAL
   Item ← 0
   IF TopPointer >= BasePointer THEN          // gap 2
      Item ← Stack[TopPointer]                // gap 3
      TopPointer ← TopPointer - 1             // gap 4
   ELSE
      OUTPUT "The stack is empty – error"
   ENDIF
   RETURN Item                                // gap 5
ENDFUNCTION
```

**与 MS 逐点对齐**（MS p.8，One mark for each correctly completed line）

| MP | MS 原文 | 为什么这样填 |
|:--|:--|:--|
| 1 | FUNCTION Pop() RETURNS REAL | 函数要写返回类型；Item 是 REAL |
| 2 | IF TopPointer >= BasePointer THEN | 空格后面紧跟 `BasePointer THEN`，ELSE 是“栈空”→ 条件是“栈不空” |
| 3 | Item ← Stack[TopPointer] | 先取栈顶的值 |
| 4 | TopPointer ← TopPointer – 1 | 再把顶指针往下移 |
| 5 | RETURN Item | 函数的最后一行把值带回去 |

**规范代码要点**　出栈的顺序是“**先取值、再减指针**”，入栈是“**先加指针、再存值**”——因为 Top 指着最后一个值。如果题目让指针指“下一个空位”，两句都要反过来。

**直观**　TopPointer 是一根插在最上面那个盘子上的小旗：拿走盘子之后，小旗往下挪一格。

**同题 Python 版要点**
- 在函数里修改全局的 `top_pointer` 必须先写 `global top_pointer`。
- Python 列表下标从 0 起：空栈时 `top_pointer = -1`，判满写 `top_pointer < capacity - 1`。

**与阶梯 / P4 的衔接**　先过阶梯 **L08 E03**（数组栈，约定与本型相同：1 起数组、空栈 Top = 0）。P2 的同类题见 P2-DT-16。P4 用 Python 实现栈，例如 ⟦9618_s22_42:1(a)⟧、⟦9618_s23_41:3(a)⟧——这两题的指针都指“下一个空位”，与本型相反，先读清题目。

**下一道变式**　⟦9618_w25_32:12(a)(i)⟧　（换成 Push：0 起数组、Top 初值 −1、判满用 `Top < Max – 1`，补参数、`Top ← Top + 1`、存值、满时的提示，4 分。）

<!-- auto:drills P3-CT-06 -->

### P3-CT-07　用数组实现队列　{#P3-CT-07}

<!-- auto:stats P3-CT-07 -->

**考法**　①按标识符表声明常量、数组和三个整数（FrontPointer、RearPointer、Length）（3 分）；②看伪代码补全标识符表（标识符名）；③补全初始化过程与入队过程（Enqueue）：长度检查、队尾指针加 1、越界回绕、存值、长度加 1；④补全出队函数（Dequeue）：长度检查、取队首、队首指针加 1、长度减 1、回绕或在队列变空时重置指针。

**识别信号**　Pseudocode is to be written to implement a queue Abstract Data Type (ADT)；Write the pseudocode to declare MaxSize, FrontPointer, RearPointer, Length and Queue；PROCEDURE Enqueue；FUNCTION Dequeue；Study the pseudocode and insert the identifiers to complete this table。

**解题思路**
1. **先定约定**：本型语料里的题（s23 两卷）FrontPointer 指**队首那个值**，RearPointer 指**队尾那个值**（最后加入的），Length 记录队中元素个数；判满、判空都看 Length。
2. **Enqueue**：`IF Length < MaxLength` → `Rear ← Rear + 1` → 越过上界就回到下界（**回绕**）→ `Queue[Rear] ← NewItem` → `Length ← Length + 1`。
3. **Dequeue**：`IF Length > 0` → `Item ← Queue[Front]` → `Front ← Front + 1` → `Length ← Length - 1` → 越过上界回到下界（或队列变空时按题目重置指针）→ 返回 Item；空队列时按题目输出提示。
4. **上下界与回绕值**看数组声明：`ARRAY[0 : MaxLength – 1]` → 越过 `MaxLength – 1` 回到 0；`ARRAY[1:60]` → 越过 60 回到 1。
5. **初值照题目**（决策 D10）：题目给了 FrontPointer 的初值，其余指针按同一约定设；没有题目约定时，用下面模板的约定。

**伪代码模板**（0 起数组；一种自洽的约定：Front 初值 0、Rear 初值 −1、Length 初值 0）

```pseudocode
CONSTANT MaxLength = 50
DECLARE FrontPointer : INTEGER
DECLARE RearPointer : INTEGER
DECLARE Length : INTEGER
DECLARE Queue : ARRAY[0:49] OF STRING

PROCEDURE Initialise()
   FrontPointer ← 0
   RearPointer ← -1
   Length ← 0
ENDPROCEDURE

PROCEDURE Enqueue(NewItem : STRING)
   IF Length < MaxLength THEN                 // not full
      RearPointer ← RearPointer + 1
      IF RearPointer > MaxLength - 1 THEN
         RearPointer ← 0                      // wrap round
      ENDIF
      Queue[RearPointer] ← NewItem
      Length ← Length + 1
   ELSE
      OUTPUT "Queue full"
   ENDIF
ENDPROCEDURE

FUNCTION Dequeue() RETURNS STRING
   DECLARE Item : STRING
   Item ← ""
   IF Length > 0 THEN                         // not empty
      Item ← Queue[FrontPointer]
      FrontPointer ← FrontPointer + 1
      IF FrontPointer > MaxLength - 1 THEN
         FrontPointer ← 0                     // wrap round
      ENDIF
      Length ← Length - 1
   ELSE
      OUTPUT "Queue empty"
   ENDIF
   RETURN Item
ENDFUNCTION
```

**得分表述**（引自对应 MS）
- 「RearPointer ← -1」⟦9618_s23_32:11(a)(ii)⟧
- 「IF Length < MaxLength THEN」⟦9618_s23_32:11(a)(ii)⟧
- 「Queue[RearPointer] ← NewItem」⟦9618_s23_32:11(a)(ii)⟧
- 「three correctly defined integers」⟦9618_s23_31:11(a)⟧
- 「IF Length > 0 THEN」⟦9618_s23_31:11(b)⟧
- 「Item ← Queue[FrontPointer]」⟦9618_s23_31:11(b)⟧

**得分点地图**（口径同 CT-02；本型核验语料 4 行，已拆分 2 行：⟦9618_s23_32:11(a)(ii)⟧、⟦9618_s23_31:11(b)⟧；另两行是声明与标识符表）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 判满 / 判空：`Length < MaxLength`、`Length > 0` | 2 | `queue-array`、`relational-ops` |
| 用指针作下标存值 / 取值 | 2 | `queue-array`、`array-index` |
| 指针初值、Length 初值 | 1 | `initialise-variables` |
| 移动指针：队尾加 1 / 队首回绕到下界 | 2 | `queue-array` |
| Length 减 1 | 1 | `accumulator` |

**易错与失分**
- RearPointer 初值写 0、满的条件写成 `Length < MaxLength - 1`：考官报告列为本题的常见错误（⟦9618_s23_32:11(a)(ii)⟧）。
- 标识符表不用伪代码里给的名字：考官报告指出出错多半是没用题给标识符（⟦9618_s23_32:11(a)(i)⟧）。
- 声明三件套（常量、数组、三个整数）很少有人全对：考官报告指出能同时写对三部分的考生很少（⟦9618_s23_31:11(a)⟧）。常量写 `CONSTANT MaxSize = 60`，数组写 `ARRAY[1:60]`（MS 也接受 `[0:59]` 或用常量作上界）。
- 忘了回绕，或回绕到错误的下标（0 起数组回到 0，1 起数组回到 1）。
- ⟦9618_s23_31:11(b)⟧ 的 Dequeue：考官报告说明，原卷没有说清 FrontPointer 是否已在调用前更新，因此该题 4 分全体考生都给了；公开发布的试卷补了一行让考生更新 FrontPointer。练这道题时以公开版为准。

#### 代表题精讲　⟦9618_s23_32:11(a)(ii)⟧

**在考什么**　题目给出一个不完整的队列：`CONSTANT MaxLength = 50`，`Queue : ARRAY[0 : MaxLength – 1] OF STRING`，初始化过程里已有 `FrontPointer ← -1`，入队过程里已有回绕的 IF 和 `Length ← Length + 1`。Complete the given pseudocode. 5 处空，5 分。讲解时对照原卷 QP p.13（代码和 (a)(i) 的表都在这一页）。

**完整作答**（带注释的 5 行是要填的）

```pseudocode
// initialisation of queue
PROCEDURE Initialise
   FrontPointer ← -1
   RearPointer ← -1                           // gap 1
   Length ← 0                                 // gap 2
ENDPROCEDURE

// adding a new item to the queue
PROCEDURE Enqueue(NewItem : STRING)
   IF Length < MaxLength THEN                 // gap 3
      RearPointer ← RearPointer + 1           // gap 4
      IF RearPointer > MaxLength – 1 THEN
         RearPointer ← 0
      ENDIF
      Queue[RearPointer] ← NewItem            // gap 5
      Length ← Length + 1
   ENDIF
ENDPROCEDURE
```

**与 MS 逐点对齐**（MS p.12，One mark for each correctly completed line）

| MP | MS 原文 | 为什么这样填 |
|:--|:--|:--|
| 1 | RearPointer ← -1 | 空队列：队尾“在第一个位置之前”；第一次入队加 1 后正好是 0 |
| 2 | Length ← 0 | 空格后面已经印了 `← 0`，只缺左边的 Length |
| 3 | IF Length < MaxLength THEN // IF Length <= MaxLength - 1 THEN | 还没满才入队 |
| 4 | RearPointer ← RearPointer + 1 | 先移动队尾，下一行马上检查回绕 |
| 5 | Queue[RearPointer] ← NewItem | 回绕之后才存值，所以这一行在回绕的 IF 下面 |

**规范代码要点**　填空的顺序线索：回绕的 IF 检查的是 RearPointer，所以它**上一行**一定是移动 RearPointer；`Length ← Length + 1` 在最后，所以存值在它**上一行**。

**直观**　环形停车场：车位 0 到 49 排成一圈，“最后一辆车”的标记往前挪一格，挪过 49 就回到 0；Length 是场内车数，到 50 就不放行。

**同题 Python 版要点**
- 回绕可以写成 `rear_pointer = (rear_pointer + 1) % max_length`；伪代码里两种写法都行（`MOD` 在指南里有）。
- 全局指针要 `global`；题目给的初值照抄（决策 D10）。
- 注意：这道题的设计里 FrontPointer 初值是 −1，而 Enqueue 不改 FrontPointer——这是题目给定的部分，作答只填空，不改题给的行。

**与阶梯 / P4 的衔接**　先过阶梯 **L08 E04**（循环队列：队首、队尾指针与绕回）。P2 的同类题见 P2-DT-16。P4 用 Python 写循环队列，例如 ⟦9618_s22_41:3(b)⟧（把题给的 Enqueue 伪代码补全后写成程序）。

**下一道变式**　⟦9618_s23_31:11(a)⟧　（只写声明：`CONSTANT MaxSize = 60`、`Queue : ARRAY[1:60] OF STRING`、三个 INTEGER，3 分。）

<!-- auto:drills P3-CT-07 -->

### P3-CT-08　链表的操作与实现　{#P3-CT-08}

<!-- auto:stats P3-CT-08 -->

**考法**　用两个一维数组（数据数组 + NextPointer 数组）和 HeadPointer 实现的“简化链表”：①删除若干结点后，写出新的 HeadPointer 与各结点的 NextPointer，使剩下的结点仍按顺序连起来（3 分）；②补全沿指针查找某个值的伪代码（5 分）；③说明怎样改进这个简化链表（加空闲表指针，2 分）。

**识别信号**　A simplified linked list is used to store …；implemented using two 1D arrays；HeadPointer indicates the index of the first …；When the end of the linked list is reached, the next pointer has the value of 0；Complete the table to show the new values of HeadPointer and NextPointer；The linked list is searched, in order；Explain how you could improve the simplified linked list structure。

**解题思路**
1. **链表的顺序不是数组的顺序**：从 HeadPointer 出发，每次跳到 NextPointer 指的那一格，直到遇到空指针（题目约定的值，这里是 0）。
2. **删结点后改指针**：先把剩下的结点按要求的顺序（如字母序）排一遍；HeadPointer 指向第一个；每个剩下的结点的 NextPointer 指向它后面的那个剩下的结点；最后一个写空指针。被删的行在该题 MS 的答案表里留空。
3. **查找**：`Pointer ← HeadPointer`；`WHILE Pointer <> 0`：当前结点的数据等于目标 → 记下位置并让循环结束；否则 `Pointer ← NextPointer[Pointer]`。
4. **循环后判断找没找到，用“记下的位置”**（`Found <> 0`）。该题 MS 也列了 `IF Pointer = 0`，但循环结束时 Pointer 一定是 0，这个条件永远为真，没找到也会走“找到”分支——自己写用 `Found <> 0`。没找到的提示里不能输出 `Flower[Found]`（Found 是 0，不是一个结点）。
5. **改进**：加一个空闲表指针（free list pointer），把未用 / 删掉的位置也串成一个链表（空闲链表），插入时从空闲链表取位置，空间可以重复使用。

**伪代码模板**

```pseudocode
// Flower : ARRAY[1:10] OF STRING, NextPointer : ARRAY[1:10] OF INTEGER, 0 = null pointer
Pointer ← HeadPointer
Found ← 0
OUTPUT "Enter a flower name "
INPUT FlowerName
WHILE Pointer <> 0                            // stop at the null pointer
   IF Flower[Pointer] = FlowerName THEN
      Found ← Pointer                         // remember where it is
      Pointer ← 0                             // end the loop
   ELSE
      Pointer ← NextPointer[Pointer]          // follow the pointer
   ENDIF
ENDWHILE
IF Found <> 0 THEN
   OUTPUT Flower[Found], " is found"
ELSE
   OUTPUT "The flower you wanted is not in the list"
ENDIF
```

**得分表述**（引自对应 MS）
- 「WHILE Pointer <> 0」⟦9618_w22_32:11(b)⟧
- 「Pointer ← NextPointer[Pointer]」⟦9618_w22_32:11(b)⟧
- 「OUTPUT "The flower you wanted is not in the list"」⟦9618_w22_32:11(b)⟧
- 「All six NextPointer correct」⟦9618_w22_32:11(a)⟧
- 「Include a free list pointer」⟦9618_w22_32:11(c)⟧
- 「to reuse the unused space」⟦9618_w22_32:11(c)⟧

**得分点地图**（口径同 CT-02；本型核验语料 3 行，只有 ⟦9618_w22_32:11(b)⟧ 拆了得分点，下面就是它的 5 个点）

| MP | 得分点（MS 原文） | 技能标签 |
|:--|:--|:--|
| 1 | INPUT FlowerName | `input-prompt` |
| 2 | WHILE Pointer <> 0 | `linked-list`、`pre-condition-loop` |
| 3 | Pointer ← NextPointer[Pointer] | `linked-list` |
| 4 | IF Pointer = 0 THEN // IF Found <> 0 THEN | `linked-list`、`relational-ops` |
| 5 | OUTPUT "The flower you wanted is not in the list" | `output-format` |

**易错与失分**
- 考官报告列出的典型错误：WHILE 条件写错、下一个 Pointer 的赋值写错、IF 漏了 THEN、在“没找到”的输出里写了 Flower(Found)——花不在数组里，这样写不可能工作（⟦9618_w22_32:11(b)⟧）。
- 改进题答成“改进算法”：考官报告指出很多考生误读了题意，题目问的是改进**链表结构**（⟦9618_w22_32:11(c)⟧）。
- 删除后按**数组下标**顺序连指针，而不是按链表应有的顺序。
- 最后一个结点忘了写空指针；或者空指针写成 −1（这道题约定是 0）。

#### 代表题精讲　⟦9618_w22_32:11(b)⟧

**在考什么**　花名按字母序存在简化链表里：Flower 数组存名字、NextPointer 数组存下一个的下标，HeadPointer 为 6，链表末尾的 NextPointer 为 0。补全算法：输入花名 → 按链表顺序查找 → 找到 / 没找到各输出提示 → 指针为 0 时结束。5 分，每填对一行 1 分。讲解时对照原卷 QP p.11（数组初始内容在 p.10）。

**完整作答**（带注释的 5 行是要填的）

```pseudocode
Pointer ← HeadPointer
Found ← 0
OUTPUT "Enter a flower name "
INPUT FlowerName                                        // gap 1
WHILE Pointer <> 0                                      // gap 2
   IF Flower[Pointer] = FlowerName THEN
      Found ← Pointer
      Pointer ← 0
   ELSE
      Pointer ← NextPointer[Pointer]                    // gap 3
   ENDIF
ENDWHILE
IF Found <> 0 THEN                                      // gap 4
   OUTPUT Flower[Found], " is found"
ELSE
   OUTPUT "The flower you wanted is not in the list"    // gap 5
ENDIF
```

**与 MS 逐点对齐**（MS p.16，One mark for each correct line）

| MP | MS 原文 | 说明 |
|:--|:--|:--|
| 1 | INPUT FlowerName | 变量名要和下面 IF 里的 `FlowerName` 一致 |
| 2 | WHILE Pointer <> 0 | 题目说“下一个指针为 0 时结束” |
| 3 | Pointer ← NextPointer[Pointer] | 沿指针走到下一个结点 |
| 4 | IF Pointer = 0 THEN // IF Found <> 0 THEN | MS 两种都列；按上面思路第 4 条，写 `Found <> 0` |
| 5 | OUTPUT "The flower you wanted is not in the list" | 任何合适的提示；不能带 `Flower[Found]` |

**直观**　寻宝游戏：每张纸条上写着一个词和“下一张纸条藏在几号盒子”，从 HeadPointer 给的盒子开始，一张一张往下找；纸条上写着 0 就是最后一张。

**同题 Python 版要点**
- 数组按题目的下界真建出来，空指针照题目用 0（决策 D10）：Python 列表多建一格，下标 0 不存数据，下标 1–10 对应题目的 1–10。
- 不能用 `in`、`index()` 在 Flower 列表里直接找（决策 D10），要沿 NextPointer 走。

**与阶梯 / P4 的衔接**　先过阶梯 **L10 E01**（沿指针遍历的干跑），再做 **L10 E02–E04**（表头插入、按序插入、删除并归还空闲表）。P2 的同类题见 P2-DT-15、DT-16。P4 用 OOP 写链表结点，例如 ⟦9618_s25_43:3(a)(i)⟧。

**下一道变式**　⟦9618_w22_32:11(a)⟧　（同一组数组，删掉 4 个花名后填新的 HeadPointer 与 6 个 NextPointer，3 分。核验语料中本型只有这一组题，所以变式只能取同卷的另一小问。）

<!-- auto:drills P3-CT-08 -->

### P3-CT-09　二叉树：结点图、存储表与查找　{#P3-CT-09}

<!-- auto:stats P3-CT-09 -->

**考法**　①把给出的有序二叉树画成“左指针 | 数据 | 右指针”的结点图，补全结点、箭头和空指针（4 分）；②把一组新数据插入已有的有序二叉树并画出（4 分）；③把结点填进记录数组或二维数组表：每行的 LeftPtr、RightPtr，以及 RootPtr、FreePtr（4 分）；④补全在记录数组里查找某值的函数（4 分）。

**识别信号**　The following diagram shows an ordered binary tree；A linked list of nodes is used to store …；Each node consists of a left pointer, the data and a right pointer；−1 / 0 is used to represent a null pointer；Complete this linked list / the binary tree, including null pointers；A user-defined record structure / A 2D array is used to store the nodes；RootPtr、FreePtr；searches for an element in the array of records。

**解题思路**
1. **插入规则**：从根开始，新值比当前结点小 → 走左；大 → 走右；一直走到空位置放下。字符串按字母序比（Aa < Gg < Kk < Mm < Pp）。
2. **画结点图**：每个结点三格（左指针 | 数据 | 右指针）；有孩子的那一侧画箭头，**箭头从对应的指针格出发**指向孩子结点；没有孩子的那一侧写空指针（照题目：−1 或 0）；有箭头的指针格里不写数字。
3. **填存储表**：每一行的 LeftPtr / RightPtr 填**孩子所在行的 Index**，没有孩子填空指针；RootPtr = 根所在的 Index；FreePtr = 第一个空行的 Index，**那一行完全留空**。
4. **查找函数**：`NowPtr ← RootPtr`；`WHILE NowPtr <> 空指针`：当前数据 > Item → 走左；< Item → 走右；相等 → `RETURN NowPtr`；循环结束返回空指针。函数头写 `RETURNS INTEGER`（返回的是下标）。

**伪代码模板**

```pseudocode
// BinTree : ARRAY[0:7] OF TreeNode (LeftPtr, Data, RightPtr); -1 = null pointer
FUNCTION SearchTree(Item : STRING) RETURNS INTEGER
   DECLARE NowPtr : INTEGER
   NowPtr ← RootPtr                           // start at the root
   WHILE NowPtr <> -1
      IF BinTree[NowPtr].Data > Item THEN
         NowPtr ← BinTree[NowPtr].LeftPtr     // smaller values are on the left
      ELSE
         IF BinTree[NowPtr].Data < Item THEN
            NowPtr ← BinTree[NowPtr].RightPtr // larger values are on the right
         ELSE
            RETURN NowPtr                     // found: return its index
         ENDIF
      ENDIF
   ENDWHILE
   RETURN -1                                  // fell off the tree: not found
ENDFUNCTION
```

**得分表述**（引自对应 MS）
- 「Correct arrows to represent pointers joining parent nodes to child nodes」⟦9618_w24_31:11(a)⟧
- 「Correct null pointers (-1) added throughout」⟦9618_s25_31:4(a)⟧
- 「Correct FreePtr with blank row 7」⟦9618_w24_31:11(b)⟧
- 「One mark for correct FreePtr with last row of table completely blank」⟦9618_w24_32:11(b)⟧
- 「NowPtr ← RootPtr」⟦9618_w24_31:11(c)⟧
- 「IF BinTree[NowPtr].Data > Item THEN」⟦9618_w24_31:11(c)⟧

**得分点地图**（口径同 CT-02；本型核验语料 8 行，拆了得分点的只有两道查找函数：⟦9618_w24_31:11(c)⟧、⟦9618_w24_32:11(c)⟧；结点图与存储表 MS 按“结点数据 / 空指针 / 箭头 / 整体位置”或“按行”给分，未拆）

| 得分点（MS 原文举例） | 行数 | 技能标签 |
|:--|--:|:--|
| 函数头：`RETURNS INTEGER` | 2 | `module-header` |
| `NowPtr ← RootPtr` | 2 | `binary-tree`、`initialise-variables` |
| 比较：`… .Data > Item` | 2 | `binary-tree`、`relational-ops`、`array-of-records` |
| 沿左 / 右指针移动：`NowPtr ← … .LeftPtr` / `.RightPtr` | 2 | `binary-tree`、`array-of-records` |

**易错与失分**
- 结点图：考官报告列出的常见错误是箭头没有箭头头、指针不是从正确的左 / 右指针格出发、指针格里写了空指针以外的数字（⟦9618_w24_31:11(a)⟧、⟦9618_s25_31:4(a)⟧）。
- 存储表：考官报告指出常见错误是在 FreePtr 指的那一行写了数据，这一行必须留空（⟦9618_w24_31:11(b)⟧）。
- 查找函数：考官报告列出的常见错误有函数头写成 RETURN 而不是 RETURNS、给 NowPtr 赋了错的值（如 −1）、用错下标变量名、该走右指针却写了左指针（⟦9618_w24_31:11(c)⟧）；另一卷还有比较符写成 `<` 或 `>=`（⟦9618_w24_32:11(c)⟧）。
- 空指针用错值：w24 两卷用 −1，⟦9618_s25_32:11(a)⟧ 用 0，照题目。

#### 代表题精讲　⟦9618_w24_31:11(a)⟧

**在考什么**　有序二叉树：根 Red；Red 的左孩子 Green、右孩子 Yellow；Green 的左孩子 Blue、右孩子 Orange；Orange 的左孩子 Indigo；Yellow 的左孩子 Violet。题目已画出 RootPtr → Red → Green → Blue（Blue 两侧已写 −1）。Complete this linked list to represent the given binary tree，−1 表示空指针。4 分。讲解时对照原卷 QP p.12（树和待补的结点图都在这一页）。

**完整作答**（每个结点写成 [左指针 | 数据 | 右指针]，“→”表示从该指针格画出的箭头）

```text
RootPtr → [ →Green | Red    | →Yellow ]
          [ →Blue  | Green  | →Orange ]
          [  -1    | Blue   |  -1     ]      (given)
          [ →Indigo| Orange |  -1     ]
          [  -1    | Indigo |  -1     ]
          [ →Violet| Yellow |  -1     ]
          [  -1    | Violet |  -1     ]
```

新加的结点是 Yellow、Orange、Indigo、Violet 四个；新写的空指针共 6 个：Yellow 右、Orange 右、Indigo 左右、Violet 左右。Red 的右指针、Green 的右指针、Orange 的左指针、Yellow 的左指针都画箭头，不写数字。

**与 MS 逐点对齐**（MS p.15）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | Four additional nodes with correct data values | Yellow、Orange、Indigo、Violet |
| 2 | Correct null pointers in all added nodes (6) with no extra null pointers where the arrow points to the next node | 上面列出的 6 个 −1；画箭头的格不写 −1 |
| 3 | Correct arrows to represent pointers joining parent nodes to child nodes | Red→Yellow、Green→Orange、Orange→Indigo、Yellow→Violet |
| 4 | All nodes in correct order and no extra data added to pointers | 位置与原树一致，指针格只有箭头或 −1 |

**同组续问**（同一棵树，QP p.13）
- ⟦9618_w24_31:11(b)⟧ 把结点存进记录数组（Index 0–7，数据已按 Red、Green、Yellow、Blue、Orange、Indigo、Violet 填好）：LeftPtr / RightPtr 依次为 Red 1 / 2，Green 3 / 4，Yellow 6 / −1，Blue −1 / −1，Orange 5 / −1，Indigo −1 / −1，Violet −1 / −1；RootPtr 已给 0；FreePtr = 7，第 7 行留空。MS p.16 按“Red 与 Green 行”“Yellow 与 Blue 行”“Orange、Indigo、Violet 行”“FreePtr 且第 7 行空”给 4 分。
- ⟦9618_w24_31:11(c)⟧ 补全查找函数的 4 处：`RETURNS INTEGER`、`NowPtr ← RootPtr`、`IF BinTree[NowPtr].Data > Item THEN`、`NowPtr ← BinTree[NowPtr].RightPtr`（MS p.17，One mark for any correct row）。整段与上面的伪代码模板相同，只是循环结束时题目写的是 `RETURN NowPtr`（此时 NowPtr 已是 −1）。

**直观**　二叉树是一棵“比大小的分岔路”：每到一个路口，比当前路标小就往左，大就往右。指针格就是路口的两个路牌，路牌上要么画着箭头指向下一个路口，要么写着 −1（死路）。

**同题 Python 版要点**
- 结点用类或三个并行列表；左右指针初值 −1；空树 `root_ptr = -1`。
- Python 里 `tree[-1]` 不报错（是最后一个元素），所以先判断 `now_ptr != -1` 再取结点。

**与阶梯 / P4 的衔接**　先过阶梯 **L10 E05**（二叉查找树的插入与查找）和 **L11 E05**（递归遍历）。P4 用 Python 写二叉树，例如 ⟦9618_s24_42:2(a)(i)⟧（结点类与构造方法）、⟦9618_w22_41:3(c)⟧（二维数组存树、递归查找）。

**下一道变式**　⟦9618_s25_31:4(a)⟧　（把 6、15、41、66 插入已有的整数二叉树并画出结点图，−1 为空指针，4 分。）

<!-- auto:drills P3-CT-09 -->

### P3-CT-10　递归的概念、特征与适用场合　{#P3-CT-10}

<!-- auto:stats P3-CT-10 -->

**考法**　①描述什么是递归（2 分）；②说出递归的三个基本特征（3 分）；③说明什么时候用递归有好处并举例（2–3 分）；④说出一种可以用递归实现的 ADT（1 分）。

**识别信号**　Describe what is meant by recursion；State (the) three essential features of recursion；Describe when the use of recursion would be beneficial and give an example；Identify one feature of an algorithm that makes it beneficial to use recursion；Identify one other ADT that a designer can implement using recursive algorithms。

**解题思路**
1. **定义**两截：子程序（函数 / 过程）**调用自身**（用自身定义）——一般情况；直到满足终止条件——基本情况，此时不再递归调用。
2. **三个特征**（一条一分，背原句）：
   - 必须调用自身 / 有一般情况；
   - 必须有基本情况 / 终止条件；
   - 每次调用都必须改变状态、**向基本情况靠近**。
3. **何时有益**：问题能自然地分解成同类的、更小的子问题；尤其是分支多、用迭代写太复杂的问题。**例子**：阶乘、数学数列（斐波那契）、复利计算、树的遍历、RPN 求值。
4. **可用递归实现的 ADT**：二叉树（遍历、插入）、栈。

**得分表述**（引自对应 MS）
- 「A recursive algorithm must call itself / have a general case」⟦9618_w25_31:9(b)⟧
- 「It must have a base case / have a stopping condition」⟦9618_w25_31:9(b)⟧
- 「It must change its state and move towards the base case」⟦9618_w25_31:9(b)⟧
- 「A technique used to solve problems using a function/procedure/subroutine that calls itself (general case)」⟦9618_s25_31:4(b)⟧
- 「Recursion is beneficial for problems that can be broken down into smaller, repetitive problems」⟦9618_w25_33:11⟧
- 「Recursion is beneficial for algorithms when a problem naturally breaks down into smaller versions of itself」⟦9618_s25_32:11(b)⟧

**易错与失分**
- 三个特征只写出两个：考官报告指出大多数考生知道一般情况和基本情况，只有最好的考生写出了第三条“改变状态、向基本情况靠近”（⟦9618_w25_31:9(b)⟧）。
- “何时有益”写不出来、只会举例：考官报告指出很少有考生能描述何时有益，但多数能举出例子（⟦9618_w25_33:11⟧）；另一卷也说第一部分（特征）更难（⟦9618_s25_32:11(b)⟧）。
- 定义只写“调用自身”：再补一句“直到基本情况为止”拿第二分（⟦9618_s25_31:4(b)⟧ 的考官报告：完整描述一般情况和基本情况的才得 2 分）。
- 把递归说成“循环”：递归是子程序调用自身，不是 WHILE。

#### 代表题精讲　⟦9618_w25_31:9(b)⟧

**在考什么**　题干：A stack is used to implement recursion. State the three essential features of recursion. 3 分，三条各 1 分。讲解时对照原卷 QP p.10。

**完整作答**
1. A recursive algorithm must call itself (it has a general case).
2. It must have a base case (a stopping condition) where no further recursive call is made.
3. Each recursive call must change its state and move towards the base case.

**与 MS 逐点对齐**（MS p.14）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | A recursive algorithm must call itself / have a general case | 第 1 条 |
| 2 | It must have a base case / have a stopping condition | 第 2 条 |
| 3 | It must change its state and move towards the base case | 第 3 条 |

**英文作答句**　A recursive algorithm must call itself (general case), must have a base case (stopping condition), and must change its state and move towards the base case.

**直观**　俄罗斯套娃：打开一个（调用自身），里面是更小的一个（向基本情况靠近），打开到最小那个实心的就停（基本情况）。少了“越来越小”，就永远打不完。

**与阶梯 / P4 的衔接**　阶梯 **L11 §1** 讲三要素与展开，**L11 E02** 练写递归函数（检查确实递归）。P4 会要求写递归程序，例如 ⟦9618_s24_42:3(b)(i)⟧（递归插入排序）。

**下一道变式**　⟦9618_s23_31:12(a)⟧　（Describe what is meant by recursion，2 分：调用自身 + 基本情况 / 展开 + 一般情况，任两点。）

<!-- auto:drills P3-CT-10 -->

### P3-CT-11　递归与栈：编译器怎样实现递归　{#P3-CT-11}

<!-- auto:stats P3-CT-11 -->

**考法**　①解释为什么执行递归算法时要用栈（3 分）；②解释编译器翻译递归代码时怎样使用栈（4 分）。两题都要讲“压栈—到基本情况—逆序弹栈”这条链。

**识别信号**　Explain the reasons why a stack is used when a recursive algorithm is executed；Explain the reasons why a stack is a suitable ADT to implement recursion；Explain how a compiler makes use of a stack when translating recursive programming code。

**解题思路**
1. **栈的性质**：后进先出（LIFO / FILO）——这正好对应递归“最后调用的最先返回”。
2. **每次递归调用**：把返回地址、参数、局部变量的值**压栈**（winding，深入）。
3. **到达基本情况后**：开始展开（unwinding），按压栈的**相反顺序**逐个**弹栈**，恢复返回地址和局部变量，回到上一层继续算。
4. **编译器题**先写一句“编译器必须生成目标代码，让程序在运行时……”，再接压栈、每次调用、弹栈、基本情况之后四步——MS 把第一句单独作一分（Max 1），后四步里最多拿 3 分。

**得分表述**（引自对应 MS）
- 「Stacks store data in Last In First Out (LIFO) / First In Last Out (FILO) order」⟦9618_w25_32:12(b)⟧
- 「Each time a recursive algorithm calls itself data is pushed onto the stack」⟦9618_w25_32:12(b)⟧
- 「data is popped from the stack in the reverse order to which it was pushed onto it」⟦9618_w25_32:12(b)⟧
- 「The compiler must produce object code to」⟦9618_w23_32:9(c)⟧
- 「push return addresses / values of local variables onto a stack」⟦9618_w23_32:9(c)⟧
- 「after the base case is reached」⟦9618_w23_32:9(c)⟧

**易错与失分**
- 答成“什么是递归”：考官报告指出很多考生觉得编译器这题难，只是（还错误地）解释了递归；先写“编译器必须生成目标代码”、再写压入返回地址、基本情况后弹出的考生拿到最高分（⟦9618_w23_32:9(c)⟧）。
- 只写“栈是 LIFO”：考官报告指出能把 LIFO 与“递归时压栈、再按相反顺序弹栈”联系起来的考生才得到更多分（⟦9618_w25_32:12(b)⟧）。
- 压什么说不清：要写出“返回地址 / 局部变量的值”。

#### 代表题精讲　⟦9618_w23_32:9(c)⟧

**在考什么**　Explain how a compiler makes use of a stack when translating recursive programming code. 4 分：MP1 单独一组（Max 1），MP2–MP5 一组（Max 3）。讲解时对照原卷 QP p.9。

**完整作答**
1. The compiler must produce object code that will use a stack at run time.
2. With each recursive call, the code pushes the return address and the values of the local variables onto the stack (winding).
3. When the base case is reached, unwinding begins …
4. … and the return addresses and local variable values are popped off the stack in reverse order, so each call returns to the correct place.

**与 MS 逐点对齐**（MS p.7）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1（Max 1） | The compiler must produce object code to | 第 1 句 |
| 2 | …push return addresses / values of local variables onto a stack | 第 2 句 |
| 3 | …with each recursive call // … to set up winding | 第 2 句的 with each recursive call |
| 4 | …pop return addresses / values of local variables off the stack … | 第 4 句 |
| 5 | …after the base case is reached // … to implement unwinding. | 第 3 句 |

MP2–MP5 四个里最多拿 3 分，加上 MP1，共 4 分。

**英文作答句**　The compiler produces object code that pushes the return address and local variables onto a stack with each recursive call, and pops them off the stack in reverse order after the base case is reached, to implement unwinding.

**直观**　读书时一层层查脚注：每翻去一个脚注，就在便签上记下“看完回到第几页第几行”，一张张往上叠；查到底了，再从最上面那张便签开始，一张张撕掉、一层层翻回去。

**下一道变式**　⟦9618_w25_32:12(b)⟧　（Explain the reasons why a stack is used when a recursive algorithm is executed，3 分：LIFO、每次调用压栈、到基本情况开始展开、逆序弹栈。）

<!-- auto:drills P3-CT-11 -->

### P3-CT-12　追踪递归算法　{#P3-CT-12}

<!-- auto:stats P3-CT-12 -->

**考法**　按给定的递归函数或递归过程完成追踪表：①递归函数——调用序号、函数调用、参数、Result 表达式、返回值（5 分）；②递归过程——每次调用时的参数，以及数组内容怎样一步步改变（4 分）。考纲还要求会写递归算法，语料中尚未单独出题，出现时也归本型。

**识别信号**　This function calculates … and uses recursion；The recursive procedure … is defined as follows；Complete the trace table for the function when it is called as …；Complete the trace table for the algorithm for the procedure call: CALL …。

**解题思路**
1. 先找**基本情况**（不再调用自己的那个分支）和**一般情况**（调用自己、参数变小）。
2. **深入（winding）**：从第一次调用开始，每调用一次写一行，直到基本情况——这时 Result 还是一个“等着下层结果”的表达式。
3. **展开（unwinding）**：基本情况得到值后，按调用的**相反顺序**逐层回填：把下层的返回值代进表达式，算出本层的返回值。
4. **递归过程**里，递归调用之前的语句在“深入”时执行；调用之后的语句在“返回”时执行。数组每改一个元素，表里就记一次。
5. **照该题 MS 的表格格式填**：哪些列在哪一行写、值不变时写不写，以该题 MS 为准（例如 ⟦9618_s25_33:13⟧ 的 MS 只在值改变的那一行写数）。

**得分表述**（引自对应 MS）
- 「Call number column correct」⟦9618_s23_31:12(b)⟧
- 「Function call and Number columns correct」⟦9618_s23_31:12(b)⟧
- 「Result column down to base case (Winding) rows 1–6 correct」⟦9618_s23_31:12(b)⟧
- 「Result column down from base case (Unwinding) rows 7–10 correct」⟦9618_s23_31:12(b)⟧
- 「Correct Index and Target columns」⟦9618_s25_33:13⟧
- 「Correct Numbers[8] column and no incorrect data added to any other of columns [1, 2, 3, 4, 9, 10]」⟦9618_s25_33:13⟧

**易错与失分**
- 递归过程的 Index 列提前停或多走：考官报告指出有考生在 Index 到 9 之前就停了，也有人超过了 9（⟦9618_s25_33:13⟧）。
- 递归函数的追踪普遍觉得难：考官报告指出这一点，但也有相当多考生拿到 4–5 分（⟦9618_s23_31:12(b)⟧）。
- 展开时顺序写反：返回是从最深的一层往外走。
- 在没有改变的数组格里也抄一遍数：该题 MS 要求其他列不出现错误数据，按 MS 的格式只写改变的格。

#### 代表题精讲　⟦9618_s23_31:12(b)⟧

**在考什么**　斐波那契函数：

```pseudocode
FUNCTION Fib(Number : INTEGER) RETURNS INTEGER
   IF Number <= 1 THEN
      Result ← Number
   ELSE
      Result ← Fib(Number – 1) + Fib(Number – 2)
   ENDIF
   RETURN Result
ENDFUNCTION
```

Complete the trace table for the function when it is called as Fib(5). 表头：Call number、Function call、Number、Result、Return value；第一行的 Number 已给 5。5 分。讲解时对照原卷 QP p.12（表格有 15 个空行，MS 只用了 10 行）。

**完整作答**（按 MS 的格式：先沿 `Fib(Number – 1)` 一路深入到基本情况，再逐层返回；括号里的序号表示回到那一次调用）

| Call number | Function call | Number | Result | Return value |
|:--|:--|:--|:--|:--|
| 1 | Fib(5) | 5 | Fib(4) + Fib(3) | |
| 2 | Fib(4) | 4 | Fib(3) + Fib(2) | |
| 3 | Fib(3) | 3 | Fib(2) + Fib(1) | |
| 4 | Fib(2) | 2 | Fib(1) + Fib(0) | |
| 5 | Fib(1) | 1 | 1 | 1 |
| 6 | Fib(0) | 0 | 0 | 0 |
| (4) | Fib(2) | 2 | 1 + 0 | 1 |
| (3) | Fib(3) | 3 | 1 + 1 | 2 |
| (2) | Fib(4) | 4 | 2 + 1 | 3 |
| (1) | Fib(5) | 5 | 3 + 2 | 5 |

**与 MS 逐点对齐**（MS p.10，One mark per mark point）

| MP | MS 原文 | 表中对应 |
|:--|:--|:--|
| 1 | Call number column correct | 1–6，再 (4)(3)(2)(1) |
| 2 | Function call and Number columns correct | Fib(5) 到 Fib(0)，再 Fib(2) 到 Fib(5) |
| 3 | Result column down to base case (Winding) rows 1–6 correct | 前 6 行的表达式与 1、0 |
| 4 | Result column down from base case (Unwinding) rows 7–10 correct | 1 + 0、1 + 1、2 + 1、3 + 2 |
| 5 | Return value column correct | 1、0，然后 1、2、3、5 |

**说明**　这张表是 MS 的“简化追踪”：每个 Number 只展开一次（第 3 行 Fib(3) 里的 Fib(1)、第 2 行 Fib(4) 里的 Fib(2) 都直接用已算出的值，不另起一行）。真实执行时 Fib(5) 一共会调用 15 次（原卷表格正好 15 行），但 MS 给的是上面 10 行的写法，没有显示是否接受 15 行的完整调用记录。考试时照 MS 的这种格式写最稳。

**直观**　像爬楼梯问“第 5 级怎么来”：先一路问下去（第 4 级、第 3 级……问到第 1 级和第 0 级是已知的），再一路往回加，答案就从底下一层层冒上来。

**与阶梯 / P4 的衔接**　先过阶梯 **L11 E01**（递归的深入与展开干跑）。

**下一道变式**　⟦9618_s25_33:13⟧　（递归过程 Delete(1, 15)：数组 Numbers 里从 15 开始的元素逐个前移，Index 从 1 走到 9，只在改变的格写数，4 分。）

<!-- auto:drills P3-CT-12 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| CT-01 与 CT-04 | CT-01 讲二分查找的**前提和步骤**、比较两种查找的**做法**；CT-04 讲**效率**：Big O、时间随数据量怎样增长 | 题干出现 Big O、performance、time efficiency → CT-04；Describe how to perform / necessary condition → CT-01；两者都有时按 MS 分数多的一边 |
| CT-01 与 CT-02 | CT-01 用文字描述；CT-02 写伪代码 | Complete the pseudocode → CT-02 |
| CT-02 与 CT-08 / CT-09 | CT-02 在**数组**里按下标查找；CT-08 / CT-09 沿**指针**查找 | 有 NextPointer / LeftPtr / RightPtr → CT-08 / CT-09 |
| CT-03（插入排序）与 P2-DT-08（冒泡排序） | 插入排序：拿出一个、大的后移、放回空位；冒泡：相邻比较、交换 | 题目点名 insertion sort 却写出 Temp 交换 → 写成冒泡了 |
| CT-06 / CT-07 与 P2-DT-16 | P3 本型题目的指针多指“最后一个值”；P2 有的题指“下一个空位” | 先读指针的说明：points to the top / last item，还是 next free / available location |
| CT-06（栈）与 CT-07（队列） | 栈一个指针、同一端进出；队列两个指针、要回绕、常用 Length 判满判空 | 有 FrontPointer / RearPointer / Length → CT-07 |
| CT-05 与 CT-06 / CT-07 | CT-05 是文字：选哪种 ADT、比较、用一种实现另一种；CT-06 / CT-07 写声明与代码 | Compare / Justify / Explain why → CT-05；Write pseudocode / Complete → CT-06 / CT-07 |
| CT-08 与 CT-09 | 单指针（NextPointer）是链表；左右两个指针是二叉树——即使题干把它叫 linked list | 结点有 left pointer 和 right pointer → CT-09 |
| CT-10 与 CT-11 | CT-10 是递归本身（定义、三特征、何时有益）；CT-11 是递归怎样**靠栈**实现 | 题干问 stack / compiler → CT-11 |
| CT-11 与 CT-05 | CT-11 只讲栈在递归中的作用；CT-05 是“栈的用途”清单之一 | State two other uses of a stack → CT-05 |
| CT-12 与 P2-SD-07 | CT-12 追踪**递归**（有深入与展开）；P2-SD-07 是普通追踪表 | 被追踪的子程序调用了自己 → CT-12 |
