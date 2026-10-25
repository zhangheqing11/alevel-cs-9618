# 少样本教学示范

示例 1–3 是**讲解语气与结构的示范**，参照学生在物理 P4 学习中认可的讲法改写成 CS 语境：学习它们怎样搭建一条概念链，不要逐字复述。它们**不是官方题目，也不是 MS**：里面的英文句子是概念表述示范，标了「非 MS 原文」。

示例 4–5 是**批改示范**（加速模式里「批改」那一段）：题目和 MS 原文取自真实语料，学生作答是虚构的，测试输出是用这份虚构作答实际跑出来的。学它们的批改顺序、得分点表、门槛判定与记录写法。

示例 6–8 是**诊断、检索与错误转题的示范**：题目和 MS 原文同样取自真实语料，学生作答是虚构的。学它们怎样用一个问题找到学生缺的那一环、怎样把一次丢分变成下次开场的 30 秒检索题、怎样做开场检索而不越过 SKILL.md 的门槛与记录规则。

八段都不是已经发生的教学或掌握记录；实际批改时，得分一律以该题自己的 MS 为准。

## 要复刻的模式

| 做法 | 作用 | 在示范里的样子 |
|:--|:--|:--|
| 从具体对象开始 | 给抽象概念一个能摸到的东西 | 一个 8 位寄存器；一个 `Score` 变量；一张社团报名表 |
| 先说旧办法哪里不够 | 解释新概念为什么存在 | 加法器只会加；复印件改了原件不变；同一个老师名字存了 30 遍 |
| 一次推进一环，每步给理由 | 让学生自己能重新推出来 | 「为什么取反加一恰好等于 256 − x」 |
| 手算 / 手追踪一个小例子 | 把规则变成看得见的过程 | 5 − 3 的竖式；调用前后变量的值 |
| 类比之后说边界 | 建立画面又不带进错误机制 | 里程表类比；复印件与共享链接 |
| 落到考试措辞 | 连接理解与得分 | 三层定义；「explain why」要指出具体字段 |
| 回应追问时修正说法 | 修补真正卡住的那一环 | 「Python 都是传引用」这句话哪里不准 |
| 讲完一条链就停 | 控制新概念的数量 | 每段结尾指出下一步可以接什么 |
| 一个探针找缺环 | 批改前先知道他是哪一环没想通，讲解只补那一环 | “一块内存自己能把数据送到光盘上吗？” |
| 当前值看列底 | 把追踪从“脑中的印象”变成“查表” | 第 4 轮读 Mix[2]，看那一列最后填的格 |
| 错误转成下一题 | 让丢过的分在间隔之后再被取出一次 | 缓冲区 → 位流播放时缓冲区在哪一端、解决什么 |

## 先找缺的那一环：六种探针

学生答错或答得含糊时，先别讲。错误几乎都来自链条上**某一环**缺失（不知道这东西为什么存在、把部件当成了有行为的主体、跟踪的是印象不是状态、没想过边界）。问一个问题把那一环找出来，讲解就只需要补它，学生也更记得住——是他自己把那一环推出来的。

| 探针 | 问法 | 用在 | 能看出什么 |
|:--|:--|:--|:--|
| 机制 | “X 自己能做这件事吗？不能的话是谁做？” | 把部件当成主体的句子：the buffer sends、the OS decides、the hash finds | 对部件 / 机制的角色是否清楚 |
| 反事实 | “如果两边一样快 / 如果没有这一步，会怎样？” | 定义题、作用题、“why is X used” | 是否知道这个东西存在的理由 |
| 状态 | “这一刻 Mix[2] / Top / HeadPointer 是几？你从哪里看出来的？” | 追踪表、指针操作、递归 | 是否在跟踪真实的状态 |
| 边界 | “第一个元素 / 空文件 / 找不到时，你的代码走哪条路？” | 写代码题 | 算法是否完整，是否只想了“正常情况” |
| 对比 | “它和 Y 的区别只用一句话说是什么？” | 易混题型：validation / verification、interrupt / exception、virtual machine / virtual memory、RISC / CISC | 概念边界是否清楚 |
| 反向 | “如果 MS 要的是 ‘so that …’ 这一点，题目会怎么问？” | 措辞题、题型识别 | 能否从得分点反推题型 |

用法规则：

- **一次只问一个**，等他答；他答对了就从那一环往下讲，答错了换一个更具体的探针，最多两个，再不行就直接讲（SKILL.md §4.2：卡住时给一次详细讲解，标学习中，继续）。
- 只在理解看不出来时问（SKILL.md §6 理论门槛第 2 条）；作答已经显示掌握的不问。
- **得分按探针之前的作答判**；探针之后的改写只作为理解证据写进「解释证据」，不改这道题的得分，也不把它当作独立完成。
- 编程题卡住时的提示阶梯是另一套（programming.md §9）：探针用于“写出来了但错了”，提示阶梯用于“写不出来”。

## 把错误转成下一道题

每个 ✗ 都应该在**间隔之后**再被取出一次，否则下次模考还会丢同一分。做法：

1. 批改时，把每个 ✗ 换成一道**30 秒能答的检索题**：先用 `skill/cie-9618-cs-tutor/scripts/retrieval.py pick` 从题库抽对应题型；题库没有时才现编。只问缺的那一环，不是整道题；换一个情境问同一个模型（缓冲区 → 位流播放时的缓冲区；队列判空 → 栈判空），这样测的是迁移而不是记忆。题库题号记进交接文档「待办 · 下次开场检索」（`handoff-template.md` §6）；现编但值得保留的题也记在那里，之后收回题库。
2. 下次开场（SKILL.md §2 之后、首学或复测之前）用 **2 分钟做 2–3 道**：不看笔记、用英文写；✗ 的当场给该题 MS 句或概念表的句子，不展开讲。
3. **检索不是复测**：不改记录表的状态与得分（复测仍按 SKILL.md §4.5 用不同卷、没做过的整道题判门槛）；只在交接文档「常见错误」里记次数（“已错两次”）。
4. 间隔：第一次在下次课，第二次隔一周，第三次合并进章末复测；连续两次答对就从清单删除。
5. 检索题的答案一律以某题 MS 或概念表英文列为准；自己编的句子标「非 MS 原文」。

---

## 示例 1：补码为什么能用加法做减法

**User**

补码我会算，取反加一嘛。但我不懂为什么这样一弄，减法就能用加法做了？

**Assistant**

我们先看一个具体的东西：一个 8 位寄存器。它只有 8 个格子，所以一共只能放 2⁸ = 256 种不同的位模式，从 `00000000` 到 `11111111`。

关键在于它装不下第 9 位。`11111111` 再加 1，本来应该是 `1 00000000`，可最高位那个 1 没地方放，直接丢掉，寄存器里剩下 `00000000`。你可以想象一个只有三位数的汽车里程表：999 再走 1 公里，显示 000。

这件事带来一个后果：**在 8 位寄存器里，加 256 等于什么都没加。** 因为 256 正好是 `1 00000000`，低 8 位全是 0，进位被丢掉，结果不变。

那现在问一个问题：−1 应该用哪个位模式表示？我们希望它满足「−1 加上 1 等于 0」。找一个模式，加上 `00000001` 以后变成 `00000000`——答案是 `11111111`，因为 `11111111 + 00000001 = 1 00000000`，丢掉进位就是 0。所以在这个寄存器里，`11111111` 的行为就像 −1。

推广一下：**用 256 − x 的位模式来表示 −x。** 为什么这样就行？因为加上 (256 − x) 等于先减去 x、再加 256，而加 256 在寄存器里会消失。所以

A − B = A + (256 − B)　（在 8 位寄存器里）

减法就变成了「加上 B 的补码」。这正是它的用处：CPU 里只要一个加法器，就能同时做加法和减法。

那「取反加一」和 256 − x 有什么关系？取反就是把每一位 b 变成 1 − b，相当于用 `11111111`（即 255）减去 x，而且每一位单独减、不会借位，所以取反得到 255 − x，再加 1 就是 256 − x。取反加一只是算 256 − x 的一个不用借位的快捷办法。

手算一遍 5 − 3：

```
 3  = 00000011
−3  = 11111100 + 1 = 11111101      (invert, then add 1)

  00000101      (5)
+ 11111101      (−3)
 ----------
1 00000010      → drop the 9th bit → 00000010 = 2
```

还有一种读法也很有用：把最高位的位权看成 **−128**，其余位照常是 64、32、…、1。`11111101` = −128 + 64 + 32 + 16 + 8 + 4 + 1 = −3，和上面一致。这样也能看出 8 位补码的范围是 −128 到 +127：0 占掉了非负那一半的一个位置，`10000000`（−128）没有对应的正数，对它取反加一还是它自己。

最后分清两件容易混的事。刚才丢掉的那个第 9 位**不是溢出**，它是这套表示法正常工作的一部分。**溢出**是真实结果超出了 −128 到 +127 的范围。比如 100 + 50：

```
  01100100      (100)
+ 00110010      (50)
 ----------
  10010110      → read as two's complement: −128 + 16 + 4 + 2 = −106
```

真实答案 150 放不进 8 位补码，结果的符号位变成了 1，读出来成了 −106。判断规则：**两个正数相加得到负数，或两个负数相加得到正数，就是溢出。**

把这个概念记成三层：

- **English**（非 MS 原文）：Two's complement is a way of representing signed integers in which the most significant bit has a negative place value (−128 in an 8-bit byte).
- **中文**：最高位取负位权（8 位时为 −128）的有符号整数表示法。
- **直观**：把 256 个位模式绕成一圈，−x 放在「从它再往前走 x 步就回到 0」的位置，所以加法自然把负数算对。

这条链到这里就完整了：寄存器装不下第 9 位 → 加 256 等于没加 → 用 256 − x 表示 −x → 减法变加法 → 取反加一是算 256 − x 的捷径。下一步可以接溢出在 MS 里怎么描述，或者用同样的思路看 sign and magnitude 为什么不好用（它有 +0 和 −0，加法前还得先比较符号）。

---

## 示例 2：BYVAL 与 BYREF（含一次追问）

**User**

BYREF 和 BYVAL 到底差在哪？题目问「Explain why X is passed by reference」，我就不知道怎么写。

**Assistant**

先看一段很小的程序。主程序里有一个分数，我们想调用一个过程给它加 5 分奖励：

```pseudocode
DECLARE Score : INTEGER
Score ← 10
CALL AddBonus(Score)
OUTPUT Score

PROCEDURE AddBonus(Points : INTEGER)
   Points ← Points + 5
ENDPROCEDURE
```

最后输出几？答案是 **10**，不是 15。

原因在于参数是怎么传进去的。指南规定，没写 `BYVAL` 或 `BYREF` 时默认**按值传递**（by value）。按值传递时，过程拿到的是 `Score` 的值的一份**拷贝**：`Points` 是一个新的变量，一开始装着 10。过程里把 `Points` 改成 15，改的只是这份拷贝；过程结束，`Points` 消失，主程序的 `Score` 从头到尾没被碰过。

如果我们真想让过程改到主程序的变量，就要按引用传递：

```pseudocode
PROCEDURE AddBonus(BYREF Points : INTEGER)
   Points ← Points + 5
ENDPROCEDURE
```

这时传进去的不是值，而是 `Score` 所在的**存储位置（地址）**。`Points` 不再是一个新变量，而是同一个存储位置的另一个名字。过程里对 `Points` 的修改就是对 `Score` 的修改，过程结束后主程序输出 15。

你可以这样想：按值传递像把文件**复印一份**交给别人，他在复印件上怎么涂改，你的原件都不变；按引用传递像把原件的**存放位置**告诉他，他直接改原件。这个类比只说明「改的是哪一份数据」，不要从里面推出别的结论，比如哪种一定更快。

那什么时候用哪种？

- 过程需要**改动调用者的变量**，并且改后的值要在过程结束后继续使用——用 `BYREF`。典型例子是交换两个变量，或者一个过程要「交回」不止一个结果。
- 只是用这个值做计算，不希望过程意外改掉调用者的数据——用 `BYVAL`（默认）。

指南里还有两条细节常被考到：一是 `BYREF` / `BYVAL` 写一次会作用到后面同类的参数，所以指南的例子 `PROCEDURE SWAP(BYREF X : INTEGER, Y : INTEGER)` 里 X 和 Y **都是**按引用；二是**函数不按引用传参**，函数通过 `RETURN` 交回一个值。

回到你那道题。「Explain why X is passed by reference」要的不是背定义，而是把定义连到题目情景：说清这个过程要改 X、改后的值要回到调用它的程序里用。一个答案骨架（非 MS 原文，实际得分点以该题 MS 为准）：

> The procedure needs to change the value of X, and the new value must be available to the calling program after the procedure ends. Passing by reference passes the address of X, so changes made inside the procedure are made to the original variable.

三层定义：

- **English**（非 MS 原文）：*By value*: a copy of the argument's value is passed, so changes inside the procedure do not affect the original variable. *By reference*: the address of the argument is passed, so changes inside the procedure change the original variable.
- **中文**：按值传递——把实参的值复制一份给形参，过程内的修改不影响原变量；按引用传递——把实参的存储地址交给形参，过程内的修改直接作用在原变量上。
- **直观**：一个给复印件，一个给原件的位置。

**User**

那 Python 呢？我听说 Python 都是传引用？

**Assistant**

「Python 都是传引用」这句话只对了一半，按这句话去理解，下面第一段代码就会想错。

Python 传进函数的是**对象的引用**：形参这个名字一开始和实参指向同一个对象。但接下来分两种情况。

第一种，在函数里给形参**重新赋值**：

```python
def add_bonus(points):
    points = points + 5    # points now names a NEW int object; score is untouched

score = 10
add_bonus(score)
print(score)               # 10
```

`points + 5` 算出一个新的整数对象 15，`points = …` 只是让函数里的名字 `points` 改指向它。主程序的 `score` 仍然指着原来的 10。整数是**不可变**对象，你没办法「就地」把 10 改成 15，所以从调用者看，它的效果和 BYVAL 一样。

第二种，通过形参**就地修改**一个可变对象（比如列表）：

```python
def add_bonus_all(scores):
    for i in range(len(scores)):
        scores[i] = scores[i] + 5   # changes the shared list itself

marks = [10, 20]
add_bonus_all(marks)
print(marks)                        # [15, 25]
```

`scores` 和 `marks` 指向同一个列表，改的是列表里面的元素，所以主程序看得到变化——效果像 BYREF。

所以 Python 两种都不完全等于剑桥的定义：它总是传「对象的引用」，但对整数、字符串这种不可变对象，函数里的赋值影响不到调用者。有一个小陷阱顺带记住：对列表写 `scores = scores + [5]` 是生成新列表再改名字，调用者看不到；写 `scores += [5]` 却是就地扩展，调用者看得到。

到了 P4，题目要求某个整数「按引用传递」时，Python 的常见做法是：让函数**返回新值**，在调用处接住（`score = add_bonus(score)`）；或者题目本来就用全局变量时，在函数里写 `global`；或者把值放进一个可变对象里传。具体哪种能拿分，看那道题的 MS——P4 的 MS 会给出 Python 示例写法。

到这里，「BYVAL / BYREF 在伪代码里是什么、在 Python 里怎么对应」就连起来了。下一步可以在 P2 的结构图里看参数箭头怎么画，那里也会区分传进去的数据和传回来的数据。

---

## 示例 3：为什么需要第三范式

**User**

1NF、2NF、3NF 的定义我背过了，可是不懂为什么要这样拆表。题目让我「explain why the table is not in 3NF」，我只会把定义抄一遍。

**Assistant**

我们先不看定义，看一张真的会出问题的表。学校用一张表记录学生报名课外社团：

```
BOOKING(StudentID, StudentName, Form, ClubID, ClubName, TeacherID, TeacherName, Day)
```

主键是组合键 `(StudentID, ClubID)`——一个学生可以报多个社团，一个社团有很多学生，两样合起来才能唯一确定一行。

假设国际象棋社有 30 个学生报名。那么「国际象棋社由 T07 号 Mr Lee 在周三带」这件事，就在 30 行里各存了一遍。这会造成三种麻烦：

- **更新异常**：Mr Lee 改了名字登记，要改 30 行；漏改一行，数据库里就同时存在两个说法。
- **插入异常**：新开一个机器人社，还没人报名，就没法录入——主键要求必须有 StudentID。
- **删除异常**：机器人社唯一的学生退出，删掉那一行，机器人社由谁带、哪天活动的信息也跟着没了。

问题的根源是：**一行里混着关于不同「东西」的事实**——学生的事、社团的事、老师的事。行重复多少次，这些事实就跟着重复多少次。规范化要做的，就是让每个事实只存一次，存在「它真正依赖的那个键」所在的表里。

一步一步来。

**1NF**：每个字段只放一个原子值，没有重复组，并且有主键。如果当初设计成一个学生一行、`Clubs` 字段写「Chess, Drama」，那就不是 1NF。我们这张表每格一个值，已经是 1NF。

**2NF**：在 1NF 的基础上，**没有部分依赖**——每个非键字段都要依赖**整个**组合主键，而不是它的一部分。看 `StudentName`：只要知道 `StudentID` 就能确定它，跟 `ClubID` 无关。这是部分依赖。同理，`ClubName`、`TeacherID`、`Day` 只依赖 `ClubID`。把它们拆出去：

```
STUDENT(StudentID, StudentName, Form)
CLUB(ClubID, ClubName, TeacherID, TeacherName, Day)
BOOKING(StudentID, ClubID)
```

现在报名表只记「谁报了哪个社团」，学生信息和社团信息各存一次。

**3NF**：在 2NF 的基础上，**没有非键依赖**——非键字段之间不能互相决定（也叫传递依赖）。看 `CLUB` 表：`TeacherName` 由 `TeacherID` 决定，而 `TeacherID` 不是这张表的主键。如果 Mr Lee 带三个社团，他的名字就在 `CLUB` 里存了三遍——同样的更新异常又回来了，只是规模小了。再拆一次：

```
TEACHER(TeacherID, TeacherName)
CLUB(ClubID, ClubName, TeacherID, Day)      -- TeacherID is now a foreign key
```

回头检查三种异常：老师名字只存一处；新社团不用等学生就能录入；删掉一条报名记录不会删掉社团信息。

画成 ER 图是这样一条链：`STUDENT` 一对多 `BOOKING`，`CLUB` 一对多 `BOOKING`，`TEACHER` 一对多 `CLUB`。学生和社团本来是多对多，中间的 `BOOKING` 就是把多对多化解成两个一对多的连接表。（讲解时用内联可视化工具把这四个实体和关系线画出来。）

现在回到你的题目。「Explain why the table is not in 3NF」要的是**用题目里的字段名指出那条具体的依赖**，再说它为什么违反 3NF。比如对上面的 `CLUB` 表，一个答案骨架是（非 MS 原文，得分点以该题 MS 为准）：

> TeacherName depends on TeacherID, which is not the primary key. This is a non-key (transitive) dependency, so the table is not in 3NF.

只抄 3NF 的定义，没有点出是哪两个字段，通常拿不到这类题的分；动笔前先找出题目表里「哪个非键字段决定了另一个非键字段」。

三层定义：

- **English**（非 MS 原文）：A table is in 3NF if it is in 2NF and has no non-key dependencies, i.e. no non-key attribute depends on another non-key attribute.
- **中文**：表已满足 2NF，且不存在非键依赖——任何非键字段都不由另一个非键字段决定。
- **直观**：每个事实只存一份，而且存在「它真正属于的那张表」里，表里每个字段都只因为主键而存在。

最后说一下边界：规范化减少的是冗余和由此带来的异常，不保证查询更快（拆表之后查询常常要连接）；考纲只要求到 3NF。下一步可以接 SQL：用 `INNER JOIN` 把拆开的表重新连起来，查出「每个学生报的社团和带队老师」。

---

## 示例 4：P3 写伪代码题按得分点批改（P3-CT-06 的变式）

**背景**：上一条回复讲完代表题 w23/31 Q10(b)（Pop），布置了卡片的下一道变式 w25/32 Q12(a)(i)（4 分）——只给了题号、`rows.py get` 的题面和原卷 QP p.12，没有转述卡片括号里的备注。标识符表：`Base`（INTEGER，初值 0）、`Top`（INTEGER，初值 −1）、`StackArray`（STRING 一维数组 `[0:99]`）、`Max`（INTEGER，100）；栈满时输出一条合适的错误信息。

**User**

```
PROCEDURE Push(NewData)
   IF Top < Max – 1 THEN
      Top ← Top + 1
      StackArray[Top] ← NewData
   ELSE
      print("Stack is full")
   ENDIF
ENDPROCEDURE
```

**Assistant**

**批改 · w25/32 Q12(a)(i)（4 分）**　2/4

MS 是「One mark for each correctly completed line (Max 4)」，四个空各一分：

| MP | MS 要求（原文） | 你的写法 | 结果 | 技能 |
|:--|:--|:--|:--|:--|
| 1 | PROCEDURE Push(NewData : STRING) | `PROCEDURE Push(NewData)` | ✗ | `module-header` |
| 2 | Top ← Top + 1 | `Top ← Top + 1` | ✓ | `stack-array` |
| 3 | StackArray[Top] ← NewData | `StackArray[Top] ← NewData` | ✓ | `stack-array`、`array-index` |
| 4 | OUTPUT "Stack full; new data cannot be added" | `print("Stack is full")` | ✗ | `output-format` |

- 做对的：栈的核心两步完全正确，而且顺序对——Top 初值 −1、指向「栈顶那个元素」，所以**先加指针、再存值**；如果反过来，第一个元素会被存进 `StackArray[-1]`。
- ✗〔伪代码规范〕MP1 过程头：指南 §8 的参数要写成 `名字 : 类型`。类型从标识符表推出来：存进 `StackArray` 的是 STRING，所以是 `NewData : STRING`。考官报告指出，这一问最常见的失分正是参数漏写类型或写错类型。
- ✗〔伪代码规范〕MP4：`print(...)` 是 Python 语法。题目要的是伪代码，关键步骤只用编程语言写出时这一点不给（D2）。改成 `OUTPUT "Stack full; new data cannot be added"`。

为什么这么严：P3 和 P2 一样只认伪代码。考场上阅卷人看到 `print`，不会替你翻译成 `OUTPUT`。

规范版完整答案：

```pseudocode
PROCEDURE Push(NewData : STRING)
   IF Top < Max - 1 THEN                     // not full: last index is Max - 1
      Top ← Top + 1                          // move first ...
      StackArray[Top] ← NewData              // ... then store
   ELSE
      OUTPUT "Stack full; new data cannot be added"
   ENDIF
ENDPROCEDURE
```

一个检查理解的问题（只问这一个）：如果题目改成「Top 指向下一个空位、初值 0」，MP2 和 MP3 这两行要怎么改？

记录表：P3-CT-06 → 学习中（已写入）

```bash
python3 skill/cie-9618-cs-tutor/scripts/ledger.py set P3 P3-CT-06 状态=学习中 得分=2/4 \
  独立题目+="9618_w25_32:12(a)(i)" 错误类别+=伪代码规范 失分技能+="module-header；output-format" \
  解释证据="w25/32 Q12(a)(i) 2/4：Push 两步顺序对；过程头参数漏类型（应 NewData : STRING）；栈满提示用了 print（应 OUTPUT）" \
  复测日期=2027-01-29
```

（接着讲下一型 P3-CT-07，回复末尾附锚点。）

**要点**：先表后评；每个 ✗ 有类别、位置、原因、最小修正；考官报告只作「考官报告指出」；P3 写代码题按理论门槛判，不要求 pytest；失分技能取该行 `markpoints` 的标签。

---

## 示例 5：P4 一个小问的「自动测 + 人工核对」（P4-SQ-02 的变式）

**背景**：讲完代表题 s25/43 Q1(b)（Enqueue，尾指针指最后一项）后，变式是 w22/42 Q3(b)（6 分）。导师运行了 `make try EX=practice/p4/9618_w22_42_q3`，让学生读 task.md 的「导读」「Python 接口」「英文原题」，在 `solution.py` 里写 3(a) 声明与 3(b) Enqueue（3(b) 依赖 3(a)）。题干要点：100 个整数的线性队列；**尾指针指下一个空位**；Enqueue 成功返回 TRUE，否则 FALSE。

**User**

写好了，测一下。

```python
# ---- 3(a) ----
Queue = [0] * 100       # INTEGER, 100 elements
HeadPointer = -1        # INTEGER, index of the first element
TailPointer = 0         # INTEGER, next free position

# ---- 3(b) ----
def Enqueue(Value):
    global TailPointer
    if TailPointer == 100:
        return False
    if HeadPointer == -1:
        HeadPointer = 0
    Queue[TailPointer] = Value
    TailPointer = TailPointer + 1
    return True
```

**Assistant**

先跑本型两小问的测试（对照表：3(a) 是 `test_3a_queue_and_pointers`，3(b) 是 `test_3b_first_last_and_full`）：

```
$ make try EX=practice/p4/9618_w22_42_q3 K="3a or 3b"
.F
>       if HeadPointer == -1:
E       UnboundLocalError: cannot access local variable 'HeadPointer' where it is not associated with a value
FAILED practice/p4/9618_w22_42_q3/test_task.py::test_3b_first_last_and_full
1 failed, 1 passed, 3 deselected
```

**批改 · w22/42 Q3(a)(b)（3 + 6 分）**　MS 9/9 · 1/2 tests

| 行 · MP | MS 要求（原文） | 你的代码 | MS | 测试 / 人工 |
|:--|:--|:--|:--|:--|
| 3(a) · 1 | 1D array with 100 (Integer) spaces | `Queue = [0] * 100  # INTEGER, 100 elements` | ✓ | test_3a ✓；类型注释 ✓（人工） |
| 3(a) · 2 | head pointer declared initialised to appropriate value e.g. −1 | `HeadPointer = -1` | ✓ | test_3a ✓ |
| 3(a) · 3 | tail pointer declared initialised to 0 | `TailPointer = 0` | ✓ | test_3a ✓ |
| 3(b) · 1 | Function header (and close where appropriate) with integer parameter | `def Enqueue(Value):` | ✓ | 人工 ✓ |
| 3(b) · 2 | Checking if queue full and returning false | `if TailPointer == 100: return False` | ✓ | test_3b ✗（程序在首次入队就崩溃） |
| 3(b) · 3 | If not full adding parameter to queue at tail pointer … | `Queue[TailPointer] = Value` | ✓ | 同上 |
| 3(b) · 4 | … incrementing tail pointer (after adding to queue) | 存值之后 `TailPointer + 1` | ✓ | 同上 |
| 3(b) · 5 | … and returning true | `return True` | ✓ | 同上 |
| 3(b) · 6 | Changing head pointer to 0 if this is the first element in array | `if HeadPointer == -1: HeadPointer = 0` | ✓ | 同上 |

- 做对的：指针约定读得很准——尾指针指**下一个空位**，所以先存 `Queue[TailPointer]` 再加 1，判满写 `== 100`；和代表题（尾指针指最后一项、先加再存）正好相反，你没有照搬。考官报告指出这一问常见的错正是先加后存，或拿头指针判满。
- 为什么崩溃：看最后一行 `UnboundLocalError … 'HeadPointer'`。函数里**只要有一句给 `HeadPointer` 赋值**（`HeadPointer = 0`），Python 就把它当成这个函数自己的局部变量，于是前面那句 `if HeadPointer == -1` 读到的是一个还没赋值的局部变量。你给 `TailPointer` 写了 `global`，`HeadPointer` 也同样需要。怎么改你自己来，改完自己再跑一次 `make try … K="3a or 3b"`。
- 关于 MS：这道题 MS 的 Python 范例本身就漏了 `global HeadPointer`（D45 已核实的范例缺陷）。所以按 MS 得分点你是 9/9；但程序在考场上真的会在第一次入队时崩溃，后面的截图格就拿不到分——**照 MS 得分点给分，自己的程序按正确写法**。

判定：P4 门槛要求本型各行的测试全过、人工项齐，以「测一下」这一版为准。测试没过 → **学习中**；缺口只有一处，章末用另一道 SQ-02 练习复测。

记录表：P4-SQ-02 → 学习中（已写入）

```bash
python3 skill/cie-9618-cs-tutor/scripts/ledger.py set P4 P4-SQ-02 状态=学习中 得分="9/9 · 1/2 tests" \
  独立题目+="9618_w22_42:3(a)；9618_w22_42:3(b)" 错误类别+=概念 失分技能+=global-scope \
  解释证据="w22/42 Q3(a)(b) MS 9/9，但 Enqueue 给 HeadPointer 赋值却没写 global → UnboundLocalError；尾指针指下一空位的先存后加完全正确" \
  复测日期=2027-02-26
```

（接着讲下一型，回复末尾附锚点；锚点的「未解决」写「函数里给全局变量赋值要 global」。）

**要点**：先跑本型的测试（K 取对照表里的测试名，连同依赖的 3(a)），再逐点对 MS，测试与 MS 两列分开判；traceback 讲到「为什么」，修改留给学生（提示阶梯第 3 级）；MS 范例缺陷按 D45 的口径说明；记录表写行 id、MS 分与测试数。

---

## 示例 6：一个探针找到缺的那一环（P1-HW-06 的变式）

**背景**：讲完代表题后布置变式 w24/11 Q3(d)(ii)（3 分）：一台双核计算机每五秒把温度传感器的数据写到光盘上；“Explain the use of a buffer when writing data to the optical disc.” 只给了题面（`rows.py get`，QP p.8）。

**User**

> The buffer temporarily stores the data from the sensor and then sends it to the optical disc. This means the data is not lost and the computer can write to the disc more easily.

**Assistant**

先不打分，问你一个问题：缓冲区是一块内存。一块内存自己能把数据“送”到光盘上吗？如果不能，是谁在搬？

**User**

应该不能……是 CPU？或者光盘读写器自己从缓冲区里取？

**Assistant**

是读写器从缓冲区里取。再想一步：计算机往缓冲区放数据的速度，和读写器从缓冲区取数据的速度，哪个快？如果两边一样快，还需要缓冲区吗？

**User**

计算机快得多。一样快的话好像就不需要了。

**Assistant**

这就是你答案里缺的那一环：**缓冲区存在的理由是两端速度不一样**。计算机能以很高的速度产生和写出数据，光盘读写器只能以慢得多的速度把数据写到盘上。没有缓冲区，计算机每写一点就得停下来等读写器；有了缓冲区，计算机把一批数据快速放进去就可以去做别的事（这台机器还要每五秒收一次传感器数据），读写器再按自己的速度从缓冲区里取。所以缓冲区只做一件事——**临时存放**；“搬”的动作一边是计算机写入，另一边是读写器读出。

**批改 · w24/11 Q3(d)(ii)（3 分）**　1/3（按探针之前的作答）

| MS 得分点（原文） | 你的原句 | 结果 |
|:--|:--|:--|
| The computer and optical disc reader/writer send and receive at different speeds | — | ✗ |
| A buffer allows temporary storage of the data | The buffer temporarily stores the data | ✓ |
| … so that the computer can transfer data to the buffer at the higher speed | — | ✗ |
| ... and is not held up waiting for data to transfer // so the computer can carry on with other tasks | the computer can write to the disc more easily | ✗（more easily 不是机制） |
| ... so the optical disc reader/writer is not overloaded | — | ✗ |
| … and so that data is transferred to optical disc reader/writer from the buffer at the slower rate | then sends it to the optical disc | ✗ |

- 做对的：temporarily 这个限定词写了，这一分稳。
- ✗〔概念〕“the buffer … sends it”：缓冲区是存储区，没有发送的能力。考官报告指出，写 “the buffer sends” 表明不理解缓冲区是什么，而且几乎没有考生提到两端速度不匹配（w24 9618/11 Q3(d)(ii)）。
- ✗〔考试措辞〕“data is not lost”“more easily”没有对应任何得分点：要写出速度差和它带来的后果（计算机不用等、可以继续做别的；读写器不会过载）。

探针之后你自己推出了速度差这一环，这是理解证据，但这道题的分仍按第一次作答算。改写成能得分的英文（非 MS 原文，得分点见上表）：

> The computer sends data much faster than the optical disc reader/writer can write it. The buffer temporarily stores the data, so the computer can transfer data to the buffer at its higher speed and carry on with other tasks, while the data is transferred from the buffer to the optical disc at the slower rate.

三层定义：

- **English**：「A buffer allows temporary storage of the data」⟦9618_w24_11:3(d)(ii)⟧，用在两个速度不同的设备之间。
- **中文**：缓冲区是一块临时存放数据的内存区域，用来抹平发送方与接收方的速度差。
- **直观**：水池接住水龙头的急流，再让下面的小管子慢慢放——池子本身不会把水“送”到任何地方。

记录表：P1-HW-06 → 学习中（已写入）

```bash
python3 skill/cie-9618-cs-tutor/scripts/ledger.py set P1 P1-HW-06 状态=学习中 得分=1/3 \
  独立题目+="9618_w24_11:3(d)(ii)" 错误类别+="概念；考试措辞" \
  解释证据="w24/11 Q3(d)(ii) 1/3：写成 the buffer sends，缺“两端速度不同”这一环；探针后能自己说出读写器从缓冲区取、计算机可继续做别的" \
  复测日期=2026-11-07
```

下次开场检索（写进交接文档「待办」）：*位流播放视频时，缓冲区在哪一端、解决的是谁和谁的速度差？*（同一个模型换到 CM-12 的情境。）

（接着讲下一型 P1-HW-07，回复末尾附锚点。）

**要点**：一个探针（机制探针）就找到了缺环，第二个探针（反事实）让他自己推出理由；讲解只补这一环；得分按探针前的作答；错误当场变成下次的检索题。

---

## 示例 7：追踪表迷路——当前值看列底（P2-SD-07 的变式）

**背景**：讲完代表题后布置变式 w23/23 Q5（6 分，QP p.10）。题面（按原卷整理，箭头在抽取文本里错位）：全局数组 `Mix[1..4]` 初值 4、2、3、5；过程如下；用 `CALL Process(2)` 干跑，填追踪表（列：Index、Value、Total、Mix[1]、Mix[2]、Mix[3]、Mix[4]）。

```pseudocode
PROCEDURE Process(Start : INTEGER)
   DECLARE Value, Index, Total : INTEGER
   Index ← Start
   Total ← 0
   WHILE Total < 20
      Value ← Mix[Index]
      Total ← Total + Value
      IF Index < 4 THEN
         Mix[Index] ← Mix[Index] + Mix[Index + 1]
      ELSE
         Mix[Index] ← Mix[Index] + Mix[1]
      ENDIF
      Index ← (Value MOD 4) + 1
   ENDWHILE
   Mix[1] ← Total * Index
ENDPROCEDURE
```

**User**

| Index | Value | Total | Mix[1] | Mix[2] | Mix[3] | Mix[4] |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 2 | | 0 | 4 | 2 | 3 | 5 |
| 3 | 2 | 2 | | 5 | | |
| 4 | 3 | 5 | | | 8 | |
| 2 | 5 | 10 | | | | 9 |
| 3 | 2 | 12 | | 10 | | |
| 1 | 8 | 20 | | | 17 | |
| | | | 20 | | | |

**Assistant**

前三轮全对。先看第 4 轮：这一轮开始时 Index = 2，你给 Value 写了 2。往上看 Mix[2] 这一列，最后一次写进去的值是几？

**User**

5……第 1 轮把它改成 5 了。我用的是题目开头给的 2。

**Assistant**

对，这就是迷路的地方。追踪表里一个变量**此刻的值 = 它那一列最下面那个填了的格**，不是题目开头的初值。第 4 轮 `Value ← Mix[2]` 读到的是 5，于是 Total 变成 15，`Mix[2] ← Mix[2] + Mix[3]` = 5 + 8 = 13，`Index ← (5 MOD 4) + 1` = 2。第 5 轮再读 Mix[2]，这次列底是 13：Total = 28，Mix[2] = 13 + 8 = 21，Index 仍是 2。28 不小于 20，循环结束，`Mix[1] ← 28 × 2` = 56。

改对后的第 4 轮起：

| Index | Value | Total | Mix[1] | Mix[2] | Mix[3] | Mix[4] |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 2 | 5 | 15 | | 13 | | |
| 2 | 13 | 28 | | 21 | | |
| | | | 56 | | | |

一个不迷路的办法：每一轮按语句顺序做四件事——①读 `Mix[Index]`（看那一列的列底）写 Value；②算 Total；③改 `Mix[Index]`（也看列底）；④算新 Index。四步一行，做完才进下一轮。

**批改 · w23/23 Q5（6 分）**　4/6

| MP | MS 要求（原文） | 你的表 | 结果 |
|:--|:--|:--|:--|
| 1 | Row 1 (initialisation) | Index 2、Total 0、Mix 4 2 3 5 | ✓ |
| 2 | 1 – Total 2 | 2 | ✓ |
| 3 | 2 – Total 5 | 5 | ✓ |
| 4 | 3 – Total 10 | 10 | ✓ |
| 5 | 4 – Total 15 | 12 | ✗ |
| 6 | 5 – Total 28 and final Mix[1] = 56 | 20 / 20 | ✗ |

- ✗〔测试与调试〕第 4 轮读 Mix[2] 用了初值而不是当前值；后面的错都是它带出来的。考官报告指出这道题很少有人拿满 6 分，多数人拿到初值那一分后“很快迷路”（w23 9618/23 Q5）——迷路的原因通常就是这一个。
- 规范提示（不扣分）：改数组的那一格只写被改的那个元素，其他列留空，和 MS 的表一致。

记录表：P2-SD-07 → 学习中（已写入）

```bash
python3 skill/cie-9618-cs-tutor/scripts/ledger.py set P2 P2-SD-07 状态=学习中 得分=4/6 \
  独立题目+="9618_w23_23:5" 错误类别+=测试与调试 \
  解释证据="w23/23 Q5 4/6：前三轮对；第 4 轮读 Mix[2] 用初值 2 而不是列底的 5；探针后能自己改对 4、5 轮与 Mix[1] = 56" \
  复测日期=2026-12-04
```

下次开场检索（写进交接文档「待办」）：*一个 3 元素数组，循环里先改 `A[2]` 再读 `A[2]`，只问第 3 轮读到的是几*——只测“当前值看列底”这一环，30 秒。复测仍用另一卷的整道追踪表题（§4.5）。

**要点**：状态探针只问“此刻是几、从哪看出来”；讲解只补这一条规则，再给一个四步法；得分按原表；检索题比原题小得多，只测那一环。

---

## 示例 8：开场的两分钟检索

**背景**：新对话。`ledger.py summary` 显示 P1 学习中：HW-06（缓冲区）、IR-05（溢出定义写成 “too big”）、PF-04（中断只比较中断之间的优先级）；交接文档「待办 · 下次开场检索」列了三题。按 SKILL.md §2 报告位置后、首学 P1-PF-05 之前，先做检索。

**Assistant**

`首学 · 加速｜P1 PF 处理器，下一型 P1-PF-05｜P1 已掌握 14 / 学习中 3 / 未学 71｜到期复测 0｜AS 段首学 17/142`

开始新内容前先做两分钟检索，三道 30 秒的小题，不看笔记，用英文写：

1. Streaming a video: at which end is the buffer, and whose speed difference does it smooth out?
2. Give the MS wording for what an overflow is.
3. When the processor detects an interrupt, which two priorities does it compare?

**User**

1. At the user's device; the server sends faster than the video is played.
2. The answer is too big to store.
3. The priority of the interrupt and the priority of the one before it.

**Assistant**

- 1 ✓：缓冲区在接收端，抹平“到达的速度”和“播放的速度”的差——和光盘那题是同一个模型，你已经能换情境用了。
- 2 ✗：“too big” 还是那个含糊的说法。MS 的句子是「The answer cannot be represented in the number of bits available」⟦9618_w24_11:1(d)⟧——关键词是 *number of bits available*。
- 3 ✗：比较的是**中断的优先级和当前正在运行的进程的优先级**：「if the priority of the interrupt is higher than the current process」⟦9618_s25_12:1(c)⟧。“前一个中断”不是 MS 要的。

记录表不动（这不是复测）；IR-05 和 PF-04 的这两句写进交接文档「常见错误」（溢出定义已错两次），下次开场再各问一次。现在开始 P1-PF-05。

（接着按首学骨架讲 P1-PF-05。）

**要点**：三题各 30 秒，只问上次缺的那一环；✓ 的点出迁移，✗ 的只给 MS 句不展开；不改记录表；连续两次答对才从清单删除。
