## FP　进一步编程 {#ch-FP}

<!-- auto:chapter-stats -->

### 核心思想

FP 对应考纲 20.1（编程范式）与 20.2（文件处理与异常处理）。11 个题型分四块，每块的“答题手艺”完全不同：

1. **范式与低级编程**（FP-01 至 FP-03）：认出命令式、声明式、面向对象、低级四种范式（FP-01）；读汇编：说出寻址方式、算出 ACC 的值（FP-02）；只用题给指令写一小段汇编，并在表里写出标签的初值（FP-03）。
2. **面向对象 OOP**（FP-04 至 FP-06）：术语的定义（FP-04）；补全类图（FP-05）；写 `CLASS … ENDCLASS` 伪代码（FP-06）。
3. **声明式编程（Prolog 风格）**（FP-07 至 FP-09）：写事实（FP-07）；写目标、求目标的结果（FP-08）；写带 `IF … AND … AND NOT …` 的规则（FP-09）。这三型几乎总是同一道大题的 (a)(b)(c)。
4. **文件与异常**（FP-10、FP-11）：补全随机文件或文本文件的处理伪代码（FP-10）；异常与异常处理的概念（FP-11）。

整章有一条主线：**照抄题目给的名字和格式**。汇编题只能用表里的指令；类图里 setter 的名字决定属性的名字（`SetPatientID` → 属性 `PatientID`）；声明式题的谓词名、参数顺序照抄事实库；文件题的文件名、记录变量照抄上下文。这一章的分很多是“名字对上就给”的分，自创的名字再合理也可能不给。

和其他卷的关系：P1-PF-08 至 PF-10 是汇编的 AS 版（P3 的行一律归 P3 题型）；P3-DR-03 是 `TYPE … ENDTYPE` 记录，FP-10 的随机文件常用它；DR-06 至 DR-08 讲文件组织与存取方式的**概念**，FP-10 写**代码**。P4 用 Python 写类、读写文本文件、写 `try … except`（见各卡的“与阶梯 / P4 的衔接”）。

### 本章伪代码速查（2027–29 指南写法）

```pseudocode
// a class (guide §10): PRIVATE attributes, constructor NEW, getter
CLASS Pet
   PRIVATE Name : STRING
   PUBLIC PROCEDURE NEW(GivenName : STRING)
      Name ← GivenName
   ENDPROCEDURE
   PUBLIC FUNCTION GetName() RETURNS STRING
      RETURN Name
   ENDFUNCTION
ENDCLASS

// a subclass: INHERITS, and SUPER to call the parent constructor
CLASS Cat INHERITS Pet
   PRIVATE Breed : STRING
   PUBLIC PROCEDURE NEW(GivenName : STRING, GivenBreed : STRING)
      SUPER.NEW(GivenName)
      Breed ← GivenBreed
   ENDPROCEDURE
ENDCLASS
MyCat ← NEW Cat("Kitty", "Shorthaired")

// random file (guide §9.2): open, move the file pointer, read / write one record
OPENFILE "StudentFile.dat" FOR RANDOM
SEEK "StudentFile.dat", Position
GETRECORD "StudentFile.dat", Pupil
PUTRECORD "StudentFile.dat", Pupil
CLOSEFILE "StudentFile.dat"

// text file (guide §9.1): READ / WRITE / APPEND, read to EOF one line at a time
OPENFILE "FileA.txt" FOR READ
WHILE NOT EOF("FileA.txt")
   READFILE "FileA.txt", LineOfText
ENDWHILE
CLOSEFILE "FileA.txt"
```

### 题型树
<!-- auto:type-tree -->

### P3-FP-01　编程范式　{#P3-FP-01}

<!-- auto:stats P3-FP-01 -->

**考法**　①描述命令式（过程式）语言是什么（2 分）；②描述声明式语言是什么（2 分）；③给出 4 段代码，判断各属于哪种范式（4 分）；④范式与描述连线（4 分）。核验语料（2022–26）没有出过本型，题目全在 2021 扩展卷；考纲 20.1 单独列出，所以保留。

**识别信号**　Describe what is meant by an imperative (procedural) / a declarative programming language；Identify the programming paradigm for each of these program code examples；Draw one line from each programming paradigm to its most appropriate description。

**解题思路**
1. **四种范式各记一句“它是怎样写程序的”**：
   - 命令式（imperative / procedural）：用变量，用赋值语句改变变量；程序是一串**按顺序执行的命令**，常有循环。
   - 声明式（declarative）：只说**要什么**（事实、规则、目标），不说怎样做；由系统去满足目标。
   - 面向对象（object-oriented）：用类、对象、继承、封装、多态组织程序。
   - 低级（low-level）：直接用处理器的指令集（汇编、机器码）。
2. **认代码**：小写开头、句点结尾的 `male(john).` → 声明式；`FOR … NEXT` 与赋值 → 命令式；`LDD`、`STO`、`ACC` → 低级；`class`、`private`、构造方法 → 面向对象。
3. **描述题**每点一句，2 分写 2–3 句：定义一句，再加一个特征（命令式：变量、顺序、循环；声明式：事实与规则、用查询满足目标）。
4. **连线题**常多给一个干扰描述（如“基于事件的程序”= 事件驱动，不在四种范式里），不要硬连。

**得分表述**（引自对应 MS）
- 「Imperative languages use variables」⟦9618_s21_31:9(a)⟧
- 「which are changed using (assignment) statements」⟦9618_s21_31:9(a)⟧
- 「The statements provide a sequence of commands for the computer to perform」⟦9618_s21_31:9(a)⟧
- 「Instructs a program on what needs to be done instead of how to do it」⟦9618_s21_31:9(b)⟧
- 「using facts and rules」⟦9618_s21_31:9(b)⟧
- 「Programs that specify the desired result rather than how to get to it」⟦9618_w21_31:2⟧

**易错与失分**
- 声明式写成“程序员声明变量的语言”：declarative 的意思是“声明要什么结果”，不是 `DECLARE`。
- 命令式只写“一步步执行”：再补“用变量、用赋值改变变量”拿第二分。
- 连线题把“基于事件的程序”连给面向对象：它是干扰项，题目给的四种范式里没有它的位置。
- 把 Prolog 风格的事实当成命令式的函数调用：只要是 `谓词(常量, 常量).` 的格式，就是声明式。

#### 代表题精讲　⟦9618_s21_31:9(c)⟧

**在考什么**　给出四段代码，写出每段的编程范式。4 分，每段 1 分。讲解时对照原卷 QP p.12（同页上方是 9(a)(b) 两个描述题）。本题是 2021 扩展卷：核验语料里本型没有题，代表题与变式都只能用扩展卷。

**完整作答**

| 代码 | 范式 | 认它的依据 |
|:--|:--|:--|
| `male(john).` `female(ethel).` `parent(john, ethel).` | Declarative | 事实子句：谓词 + 小写常量 + 句点 |
| `FOR Counter = 1 TO 20` / `X = X * Counter` / `NEXT Counter` | Procedural / imperative | 循环 + 赋值改变变量 |
| `Start: LDD Counter` / `INC ACC` / `STO Counter` | Low-level / assembly | 助记符、累加器 ACC、标签 |
| `public class Vehicle { private speed; public Vehicle() … }` | Object oriented | 类、私有属性、构造方法 |

**与 MS 逐点对齐**（MS p.10，One mark for each correct programming paradigm，Max 4）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | Declarative | 第 1 行 |
| 2 | Procedural / imperative | 第 2 行 |
| 3 | Low-level / assembly | 第 3 行 |
| 4 | Object oriented / (OOP) | 第 4 行 |

**英文作答句**　(1) Declarative. (2) Procedural / imperative. (3) Low-level (assembly language). (4) Object-oriented.

**直观**　同样是“做一顿饭”：命令式是菜谱（第一步、第二步……）；声明式是告诉餐厅“我要一份番茄炒蛋”；面向对象是先定义“厨师”“灶台”各能做什么；低级是直接告诉手每块肌肉怎么动。

**下一道变式**　⟦9618_w21_31:2⟧　（2021 扩展卷：四种范式与五条描述连线，4 分；“基于事件的程序”是多出来的干扰项。）

<!-- auto:drills P3-FP-01 -->

### P3-FP-02　寻址方式与汇编代码执行结果　{#P3-FP-02}

<!-- auto:stats P3-FP-02 -->

**考法**　①给出内存内容，对 `LDM #n`、`LDD`、`LDI` 各一条指令，写出寻址方式与执行后 ACC 的值（3 分）；②FP-03 写好的代码运行后，某个标签变量的值是多少（1 分）。

**识别信号**　State the addressing mode and the contents of ACC after each instruction has been executed；State the value of Answer after the code described in part (a) has executed；Show the values of the variables … after the code has been run。

**解题思路（逐步作答模板）**
1. **先把题给的内存内容抄成一张小表**（地址 → 内容），后面每一步都查这张表。
2. **看操作数前有没有 `#`、指令是哪个**：
   - `LDM #n`：**立即寻址**（immediate），操作数本身就是数，ACC = n。
   - `LDD addr`：**直接寻址**（direct），ACC = 地址 addr 里的内容（查表一次）。
   - `LDI addr`：**间接寻址**（indirect），addr 里存的是**另一个地址**，ACC = 那个地址里的内容（查表两次）。
3. **每条指令单独从题给内存出发**（题目说 after each instruction，三条之间互不影响，除非题目说按顺序执行）。
4. **算代码运行结果**：按代码一行行走，写下每一步后 ACC 与各标签的值；`SUB` 是 ACC 减去地址里的数，结果可以是**负数**。

**得分表述**（引自对应 MS）
- 「LDM #500: Immediate 500」⟦9618_s22_31:9(a)⟧
- 「LDD 500: Direct 100」⟦9618_s22_31:9(a)⟧
- 「LDI 500: Indirect 20」⟦9618_s22_31:9(a)⟧

**易错与失分**
- 认不出立即寻址：考官报告指出多数考生认出了直接和间接寻址，认出立即寻址的少一些（⟦9618_s22_31:9(a)⟧）。记住：有 `#` 就是立即。
- `LDI 500` 只查了一次表、写成 100：100 是地址 500 里存的“另一个地址”，还要再去地址 100 取数。
- 减法顺序反了：`SUB` 是 ACC 减去地址里的数。考官报告指出很多考生把 −55 写成 55（⟦9618_w25_31:11(b)⟧）。

#### 代表题精讲　⟦9618_s22_31:9(a)⟧

**在考什么**　地址 500 存着 100，地址 100 存着 20。对 `LDM #500`、`LDD 500`、`LDI 500` 各写出寻址方式与执行后 ACC 的内容。3 分。讲解时对照原卷 QP p.14（指令表与本小问在同一页）。

**完整作答**

| 指令 | 寻址方式 | ACC | 怎样得到 |
|:--|:--|:--|:--|
| `LDM #500` | Immediate | 500 | `#500` 本身就是数 |
| `LDD 500` | Direct | 100 | 查地址 500 → 100 |
| `LDI 500` | Indirect | 20 | 查地址 500 → 100（一个地址），再查地址 100 → 20 |

**与 MS 逐点对齐**（MS p.11）

| 行 | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | LDM #500: Immediate 500 | 第 1 行 |
| 2 | LDD 500: Direct 100 | 第 2 行 |
| 3 | LDI 500: Indirect 20 | 第 3 行 |

MS 只列出三行答案、共 3 分，没有写明一分怎样拆（寻址方式与 ACC 值是否各算半分）。每行两样都写对最稳。

**英文作答句**　LDM #500: immediate addressing, ACC = 500. LDD 500: direct addressing, ACC = 100. LDI 500: indirect addressing, ACC = 20.

**直观**　立即寻址是“直接给你钱”；直接寻址是“钱在 500 号柜子里”；间接寻址是“500 号柜子里有张纸条，写着钱在 100 号柜子”。

**下一道变式**　⟦9618_w25_31:11(b)⟧　（先读同题 (a) 的代码：把常量 100 存进标签，再用地址 632 的值 45 减去它。Answer 是多少，1 分。）

<!-- auto:drills P3-FP-02 -->

### P3-FP-03　用给定指令集写汇编代码　{#P3-FP-03}

<!-- auto:stats P3-FP-03 -->

**考法**　只用题给的指令（`LDM`、`LDD`、`LDI`、`ADD`、`SUB`、`STO`，以及 `<label>: <data>`）写 5–7 行汇编，完成“存常量 → 取数 → 加减 → 存结果”，并在**另一张表**里写出各标签及其初值或运行后的值。6–7 分，一个动作一分，标签的设置另给分。

**识别信号**　Use only the given instruction set to write assembly language code to；Write assembly language code, using only the given instruction set to；store … as a named constant / labelled variable；Show the initialisation of the constant and Answer in the table provided。

**解题思路（逐步作答模板）**
1. **把题目的要点逐条变成指令**，题目的每个圆点通常对应 1–2 行：
   - 存常量 n：`LDM #n` → `STO 标签`（并在标签表里写 `标签: n`）。
   - 把地址 a 的内容存成变量：`LDD a` → `STO 标签`。
   - “地址存在变量 V 里”的值：`LDI V`（间接）。
   - 加 / 减：`ADD 标签或地址`、`SUB 标签或地址`（ACC 加上 / 减去那里的数）。
   - 存结果：`STO 结果标签`。
2. **代码写在横线上，标签写在表里**：标签与初值放在代码**之外**（MS 说 away from the program code）；结果变量在表里只写标签（题目要运行后的值时再填值）。
3. **操作数不加尖括号**：`STO Answer`，不是 `STO <Answer>`；`#` 只用在 `LDM`（以及题目明确给出的 `ADD #n`、`SUB #n`）。
4. **题目要运行后的值**：自己按 FP-02 的方法走一遍，把 ACC 的变化写在草稿上。

**得分表述**（引自对应 MS）
- 「LDM #20 seen」⟦9618_s22_31:9(b)⟧
- 「One mark for labelling that address e.g. Twenty away from the program code」⟦9618_s22_31:9(b)⟧
- 「Correct use of LDI B」⟦9618_w25_32:11⟧
- 「Correct labelling of three addresses A:, B: and Answer:」⟦9618_w25_32:11⟧
- 「Storing 100 at a labelled address away from the code」⟦9618_w25_31:11(a)⟧
- 「Correct use of SUB with address 899」⟦9618_w25_33:13⟧

**易错与失分**
- 把代码塞进标签表：考官报告指出这是比较常见的错误，代码应写在横线上，标签与值写在表里（⟦9618_w25_32:11⟧）。
- 操作数加尖括号：考官报告指出有考生写成 `<address>` 的样子，这是不对的（⟦9618_w25_33:13⟧）。
- 用了表里没有的指令（`INC`、`LDR`、`ADD #n` 在没给时）：题目说 only the given instruction set。
- 间接取数写成 `LDD B`：B 里存的是地址，要 `LDI B`。
- 结果变量只写在代码里，没在表里设标签：标签的设置单独给分。

#### 代表题精讲　⟦9618_w25_32:11⟧

**在考什么**　内存：地址 150 存 26，300 存 86，420 存 150。要求：把地址 300 的内容存为标签变量 A；把地址 420 的内容存为 B；把“B 里存的地址”所指的值加上 A；结果存进 Answer。并在表里写出 A、B、Answer 的标签与值。7 分；MS 列了 8 个点，Max 7。讲解时对照原卷 QP p.10（指令表与内存表）与 p.11（题目要求、作答横线与标签表）。

**完整作答**

代码（写在横线上）：

| Opcode | Operand | 作用 |
|:--|:--|:--|
| LDD | 300 | ACC ← 86 |
| STO | A | A ← 86 |
| LDD | 420 | ACC ← 150 |
| STO | B | B ← 150 |
| LDI | B | B 里是地址 150 → ACC ← 26 |
| ADD | A | ACC ← 26 + 86 = 112 |
| STO | Answer | Answer ← 112 |

标签表：

| Label | Contents |
|:--|:--|
| A: | 86 |
| B: | 150 |
| Answer: | 112 |

**与 MS 逐点对齐**（MS p.16，One mark per mark point，Max 7）

| MP | MS 要点 | 作答中对应 |
|:--|:--|:--|
| 1 | LDD 300 seen | 第 1 行 |
| 2 | Correct use of STO seen (at least once) | `STO A` 等 |
| 3 | Correct use of LDD 420 seen | 第 3 行 |
| 4 | Correct use of LDI B | 第 5 行 |
| 5 | Correct use of ADD A | 第 6 行 |
| 6 | Correct labelling of three addresses A:, B: and Answer: | 标签表三行的标签 |
| 7 | Correct contents in A: and B: | 86 与 150 |
| 8 | Correct value in Answer: | 112 |

8 个点里拿 7 个就满分。

**规范代码要点**　题目的四个圆点 → 七行代码：每个“store … as labelled variable”都是“取到 ACC → STO 标签”两行；“the address contained in variable B”是 `LDI B` 的信号。

**直观**　ACC 是你手里唯一的一只手：每次只能拿一样东西，拿新的之前要先把旧的放进某个贴了标签的盒子（STO）。

**迁移与卡点**
- **卡点**：代码写在横线上、标签与值写在表里，两处分开各有分；“变量 B 里存的地址所指的值”是 `LDI` 的信号；每个“存成标签变量”都是两行（取到 ACC → STO 标签）。
- **考官在换什么**：要不要先存常量（`LDM #n`）、几个变量、间接寻址在哪一步、要不要写运行后的值。一个动作一分、标签设置另给分。
- **从代表题到变式**：代表题从内存取两个值；变式先把常量 20 存起来并贴标签（`LDM #20` → `STO Twenty`），再 `LDI Y`、`ADD`、`STO Z`，表里设三个标签。搬过去的是“取 → 存 → 间接取 → 加 → 存”的链；要新增的是常量的存放与标签。
- **反例**：操作数加尖括号；用表里没有的指令；结果变量没在表里设标签。

**下一道变式**　⟦9618_s22_31:9(b)⟧　（常量 20 要先存起来并贴标签，再加上“变量 Y 里那个地址”所指的值，结果存进 Z，7 分：`LDM #20`、`STO`、`LDI Y`、`ADD`、`STO Z`，再在代码外设 Twenty、Y、Z 三个标签。）

<!-- auto:drills P3-FP-03 -->

### P3-FP-04　OOP 术语　{#P3-FP-04}

<!-- auto:stats P3-FP-04 -->

**考法**　①给 2–3 个 OOP 术语下定义（每个 1 分）；②描述 properties、methods、inheritance（各最多 2 分）；③认出某个特征是哪个术语（1 分）；④术语与描述连线或填表（4 分）；⑤说明属性为什么设成 `PRIVATE`（1–2 分）；⑥概述类的结构、给出对象与类的三点区别（各 3 分）。

**识别信号**　Define these Object-Oriented Programming (OOP) terms；Describe what is meant by the terms properties, methods and inheritance；Identify the OOP feature / term；Draw one line from each OOP term；Complete the table by filling in the missing OOP terms；Explain why the properties have been set to PRIVATE；Outline the structure of a class；Give three differences between an object and a class。

**解题思路**
1. **定义时用 OOP 的词**：class、object、property / attribute、method、parent / derived class。不要用术语本身解释它自己（“inheritance 就是 inherit 父类”不够，要说“新类**获得**父类的属性和方法”）。
2. **一组最常考的定义**（每条一句话）：
   - instance：一个具体的对象，由类创建（an occurrence of an object）。
   - inheritance：新类（子类）获得父类的全部属性与方法，还可以扩展或重写。
   - polymorphism：同名方法在子类中被重新定义，表现不同。
   - encapsulation：把属性和方法放进同一个类，并把数据隐藏起来。
   - getter：返回属性值的方法；setter：更新属性值的方法。
   - constructor：创建对象（实例）、给属性设初值的方法。
3. **为什么 PRIVATE**：属性只能被**这个类自己的方法**访问（实现封装）。不是“防止黑客 / 未授权用户看数据”。
4. **对象与类的区别**：三点必须是三个不同的方面——①模板与实例；②定义类时不分配内存、创建对象时分配；③类不能直接操作、对象可以；④类是定义的，对象是创建 / 实例化的。
5. **类的结构**：属性（及其类型）、方法（作用在属性上的子程序）、getter / setter、构造方法；每样东西写名字 + 一句作用，才能拿到“展开”那一分。

**得分表述**（引自对应 MS）
- 「an occurrence of an object」⟦9618_w22_31:11(a)⟧
- 「the capability of defining a new class of objects that has all the attributes and methods from a parent class」⟦9618_w22_31:11(a)⟧
- 「methods can be redefined for derived classes」⟦9618_w22_31:11(a)⟧
- 「method that is used to return the value of a property」⟦9618_w22_32:10(a)⟧
- 「To ensure that attributes can only be accessed by the class’s own methods」⟦9618_s22_32:1(c)(ii)⟧
- 「A class is a template / blueprint from which objects are created」⟦9618_w24_32:10(b)⟧

**易错与失分**
- 用术语解释术语：考官报告指出“getter 是用来 get 属性值的方法”不如“用来 return 属性值的方法”；定义里要用 property、method、class、object 这些词（⟦9618_w22_32:10(a)⟧、⟦9618_w22_31:11(a)⟧）。
- 把 PRIVATE 理解成数据保密：考官报告指出很多考生以为 PRIVATE 表示数据不能给未授权用户看（⟦9618_w24_31:9(a)⟧）；另一卷也指出常见错误是泛泛地谈数据安全（⟦9618_s22_32:1(c)(ii)⟧）。
- 对象与类的三点区别其实是同一点换说法：考官报告指出很多考生把“类是模板”换着说了几遍，只得 1 分（⟦9618_w24_32:10(b)⟧）。
- 类的结构只列名字：考官报告指出列出属性、方法、构造方法能拿一两分，还要给其中至少一个写出作用才得下一分（⟦9618_w24_32:10(a)⟧）。

#### 代表题精讲　⟦9618_w22_31:11(a)⟧

**在考什么**　Define these OOP terms: Instance、Inheritance、Polymorphism。3 分，每个术语 1 分。讲解时对照原卷 QP p.10（同页下方是 11(b) 的类伪代码）。

**完整作答**
1. **Instance**: a specific object created from a class (an occurrence of an object).
2. **Inheritance**: the capability of defining a new class of objects that has all the attributes and methods of a parent class.
3. **Polymorphism**: methods can be redefined for derived classes, so the same method behaves differently depending on which class is instantiated.

**与 MS 逐点对齐**（MS p.12，One mark for each correct OOP term definition）

| 术语 | MS 原文（`//` 后是同一分的另一种说法） | 作答中对应 |
|:--|:--|:--|
| Instance | an occurrence of an object // a specific object based on the class // an instantiation of a class | 第 1 条 |
| Inheritance | the capability of defining a new class of objects that has all the attributes and methods from a parent class | 第 2 条 |
| Polymorphism | allows the same method to take on different behaviours depending on which class is instantiated // methods can be redefined for derived classes | 第 3 条 |

**英文作答句**　An instance is a specific object created from a class. Inheritance is the capability of defining a new class that has all the attributes and methods of a parent class. Polymorphism means methods can be redefined in derived classes, so the same method behaves differently in each class.

**直观**　类是饼干模具，实例是一块块饼干；继承是在“动物”模具上加花纹做出“猫”模具；多态是“动物.叫()”在猫身上是“喵”、在狗身上是“汪”。

**与阶梯 / P4 的衔接**　阶梯 **L12** 的对照卡把这些术语逐一配了伪代码与 Python；**L12 E05**（形状类的多态）把 polymorphism 写成代码。

**迁移与卡点**
- **卡点**：用 OOP 的词定义（class、object、attribute、method、parent class），不用术语本身解释它自己；getter 写 return the value，不写 get the value。PRIVATE 是“只能被本类的方法访问”，不是数据保密。
- **考官在换什么**：问哪几个术语、定义还是描述（各 Max 2）、为什么 PRIVATE、对象与类的三点区别、类的结构。每个术语一句固定的话。
- **从代表题到变式**：代表题三个“关系类”术语；变式三个“封装类”术语——encapsulation 写“数据和方法放进同一个类、数据隐藏”，getter / setter 写 return / update the value of a property。搬过去的是“用 OOP 的词写一句”；要换的是三句话的内容。
- **反例**：对象与类的三点区别其实是同一点换说法；类的结构只列名字不写作用。

**下一道变式**　⟦9618_w22_32:10(a)⟧　（定义 Encapsulation、Getter、Setter，3 分；getter 要写 return the value，不要写 get the value。）

<!-- auto:drills P3-FP-04 -->

### P3-FP-05　补全类图　{#P3-FP-05}

<!-- auto:stats P3-FP-05 -->

**考法**　①给出类的部分属性与方法，按要点清单补全类图：缺的属性及类型、缺的 setter（带参数及类型）与 getter、构造方法（5 分）；②补全继承图：子类特有的属性与方法、从子类指向父类的继承箭头（5 分）；③给一个对象的例子，补全它的属性、getter、setter（3 分）。

**识别信号**　Complete the class diagram for … to include；Complete this class inheritance diagram to show the properties, methods and inheritance；Complete the diagram for the object …。

**解题思路**
1. **把要点清单逐条打勾**：题目每个圆点（attribute and data type for …、methods to assign …、method to return …）都对应类图里的一行或几行。数一下空行，通常正好够写。
2. **名字互相对上**：题目已给出 `SetPatientID(…)`，属性就叫 `PatientID`，getter 就叫 `GetPatientID()`。属性名、setter 名、getter 名三者一致。
3. **setter 带一个参数，并写类型**：`SetDateSeen(NewDate : DATE)`；参数名**和属性名不同**（属性 `Doctor` → 参数 `DoctorID`）。getter 不带参数：`GetDateSeen()`。
4. **类型照情境选**：以年份开头的 8 位数字编号 → `INTEGER`（该题 MS 的写法）；电话号码 → `STRING`（开头的 0 不能丢）；是 / 否 → `BOOLEAN`；日期 → `DATE`；1–5 的优先级 → `INTEGER`。
5. **继承图**：子类只写**自己特有**的属性和**重写**的方法；每个子类画一条箭头**指向父类**。
6. **构造方法**：题目要“创建对象并设置属性”的方法时，写 `Constructor()`（类图的写法）；伪代码里它叫 `NEW`（见 FP-06）。

**伪代码模板**（类图本身；补全时照这个格式一行一项）

```pseudocode
// Appointment (class diagram: attributes, then methods)
// DateSeen     : DATE
// PatientID    : INTEGER
// Doctor       : STRING
// ---------------------------------------
// Constructor()
// SetDateSeen(NewDate : DATE)           // setter: one parameter with its type
// SetPatientID(PatientNumber : INTEGER) // parameter name differs from the attribute
// GetDateSeen()                         // getter: no parameter
// GetPatientID()
```

**得分表述**（引自对应 MS）
- 「Two correct attributes (PatientID : INTEGER and Doctor : STRING)」⟦9618_s25_31:11(a)⟧
- 「GetPatientID() and GetDoctor() seen」⟦9618_s25_31:11(a)⟧
- 「SetDateSeen(…) and GetDateSeen fully correct with appropriate parameter and correct data type in setter」⟦9618_s25_31:11(a)⟧
- 「Constructor present」⟦9618_w24_31:9(b)⟧
- 「Two correct setters with exact names and appropriate parameters and data types」⟦9618_w24_31:9(b)⟧
- 「Acrylic, Wool and Mix all inherit (all arrows correct) from Yarn」⟦9618_s22_31:7(a)⟧

**得分点地图**（口径：核验语料、主题型为本型、已拆得分点的行；同一行同一标签计一次；去掉 `equivalent_of` 行。共 4 行：⟦9618_s22_31:7(a)⟧、⟦9618_s25_31:11(a)⟧、⟦9618_s25_32:12(a)⟧、⟦9618_w24_31:9(b)⟧）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 缺的属性写对名字与类型（两项一分） | 4 | `data-types` |
| setter 名字对、带合适的参数与类型；getter 名字对；名字与属性一致 | 3 | `getter-setter` |
| 有构造方法 | 1 | `class-definition` |
| 子类指向父类的继承箭头（至少一条 / 全部） | 1 | `inheritance` |
| 子类各自写出重写的同名方法 | 1 | `polymorphism` |

**易错与失分**
- 名字前后不一致：考官报告指出，setter 已给出 `SetPatientID`，属性就必须叫 `PatientID`、getter 叫 `GetPatientID()`；setter 的参数名要和属性名不同（⟦9618_s25_31:11(a)⟧、⟦9618_s25_32:12(a)⟧）。
- setter 漏参数或漏类型：考官报告指出 setter 那一分要参数与类型都对，很少有人拿到（⟦9618_w24_31:9(b)⟧）。
- 电话号码用 INTEGER：考官报告把它列为典型错误（⟦9618_w22_32:10(b)⟧）。
- 继承箭头漏画、方向反、没有箭头：考官报告指出这是继承图的常见失分（⟦9618_s22_31:7(a)⟧）。

#### 代表题精讲　⟦9618_s25_31:11(a)⟧

**在考什么**　医疗中心的 `Appointment` 类。已有属性 `DateSeen : DATE`、`Treatments : STRING`、`Medications : STRING`；已有方法 `SetPatientID(PatientNumber : INTEGER)`、`SetDoctor(DoctorID : STRING)`、`GetTreatments()`、`GetMedications()`。病人用以出生年份开头的 8 位数字识别（如 20108989），医生用名字识别。要求补：病人与医生的属性及类型、给就诊日期 / 治疗 / 药物赋值的方法、返回就诊日期与病人、医生属性的方法。5 分。讲解时对照原卷 QP p.12（类图空行：属性两行、方法区第一行 1 行、`SetDoctor` 之后 5 行）。

**完整作答**（加粗的是要补的行）

| Appointment | |
|:--|:--|
| DateSeen | : DATE |
| **PatientID** | **: INTEGER** |
| **Doctor** | **: STRING** |
| Treatments | : STRING |
| Medications | : STRING |
| **SetDateSeen(NewDate : DATE)** | |
| SetPatientID(PatientNumber : INTEGER) | |
| SetDoctor(DoctorID : STRING) | |
| **SetTreatments(NewTreatments : STRING)** | |
| **SetMedications(NewMedications : STRING)** | |
| **GetDateSeen()** | |
| **GetPatientID()** | |
| **GetDoctor()** | |
| GetTreatments() | |
| GetMedications() | |

**与 MS 逐点对齐**（MS p.14，One mark per mark point）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | Two correct attributes (PatientID : INTEGER and Doctor : STRING) | 属性区补的两行 |
| 2 | SetTreatments(…) and SetMedications(…) seen | 两个 setter 的名字 |
| 3 | … and appropriate parameters, with string data types | 两个 setter 的参数都是 STRING |
| 4 | GetPatientID() and GetDoctor() seen | 两个 getter |
| 5 | SetDateSeen(…) and GetDateSeen fully correct with appropriate parameter and correct data type in setter | `SetDateSeen(NewDate : DATE)` 与 `GetDateSeen()` |

MP3 跟在 MP2 后面（“…”）：setter 名字先对，参数类型才给分。

**规范代码要点**　属性名从已给的 setter 倒推（`SetPatientID` → `PatientID`、`SetDoctor` → `Doctor`）；PatientID 的类型照已给的参数 `PatientNumber : INTEGER`。

**直观**　类图像一张身份证模板：上半部分是要填的栏目（属性），下半部分是“改某一栏”（setter）和“看某一栏”（getter）的窗口；窗口的名字必须和栏目对得上。

**同题 Python 版要点**
- 属性写成私有的 `self.__PatientID`，在 `__init__` 里设初值；setter 是 `def SetDateSeen(self, NewDate):`，getter 是 `def GetDateSeen(self): return self.__DateSeen`。
- 名字照抄类图（P4 的类说明表也是这样给名字）。

**与阶梯 / P4 的衔接**　先过阶梯 **L12 E01**（按说明表写 `Pet` 类：私有属性、构造、getter / setter），继承图对应 **L12 E03**。P4 要求按类说明写 Python 类，例如 ⟦9618_w24_41:2(a)(i)⟧。

**下一道变式**　⟦9618_w24_31:9(b)⟧　（宠物类 `Pet`：补宠物名、主人名两个属性，构造方法，`SetPetID`、`SetDateRegistered` 两个 setter，`GetPetName`、`GetOwnerTelephone` 两个 getter，5 分。）

<!-- auto:drills P3-FP-05 -->

### P3-FP-06　用伪代码定义类　{#P3-FP-06}

<!-- auto:stats P3-FP-06 -->

**考法**　①补全 `CLASS … ENDCLASS`：类名、`PRIVATE` 属性及类型、构造方法的参数表、构造方法里的赋值（5 分）；②写出把某个属性声明为 `PRIVATE` 的一句（1 分）。

**识别信号**　Complete the pseudocode for the class … to enable objects to be created；Write pseudocode statements to declare the … class, its attributes and the constructor；Write the declaration in pseudocode for … as PRIVATE；The attributes must be available only through the methods of the class。

**解题思路**
1. **结构四件套**（指南 §10）：`CLASS 类名` → `PRIVATE 属性 : 类型`（每个属性一行）→ `PUBLIC PROCEDURE NEW(参数 : 类型, …)` … `ENDPROCEDURE` → `ENDCLASS`。
2. **“只能通过类的方法访问”= PRIVATE**：属性全部写 `PRIVATE`。
3. **名字从已给的赋值语句倒推**：构造方法里已有 `BodyType ← CarBodyType`，属性就叫 `BodyType`、参数就叫 `CarBodyType`。题目里已经出现的名字一律照抄。
4. **哪些属性进参数表**：只有用参数赋值的属性；赋固定初值的（`Fuel ← ""`、`NumberBuilt ← 0`）不进参数表。
5. **类型照题目文字**：“string attributes … an integer attribute …”。
6. 构造方法名按指南写 `NEW`；子类写 `CLASS 子类 INHERITS 父类`，构造里先 `SUPER.NEW(…)`。

**伪代码模板**

```pseudocode
CLASS Car
   PRIVATE Make : STRING
   PRIVATE Model : STRING
   PRIVATE NumberBuilt : INTEGER
   PUBLIC PROCEDURE NEW(CarMake : STRING, CarModel : STRING)
      Make ← CarMake                  // attributes set from parameters
      Model ← CarModel
      NumberBuilt ← 0                 // fixed initial value: not a parameter
   ENDPROCEDURE
   PUBLIC FUNCTION GetNumberBuilt() RETURNS INTEGER
      RETURN NumberBuilt
   ENDFUNCTION
   PUBLIC PROCEDURE SetNumberBuilt(NewNumber : INTEGER)
      NumberBuilt ← NewNumber
   ENDPROCEDURE
ENDCLASS

// creating an object
MyCar ← NEW Car("Ford", "Focus")
```

**得分表述**（引自对应 MS）
- 「Car and ENDCLASS」⟦9618_w22_31:11(b)⟧
- 「must use the identifiers used in the assignments」⟦9618_w22_31:11(b)⟧
- 「Constructor header – must use CarBodyType」⟦9618_w22_31:11(b)⟧
- 「Constructor identifier for the car model and the identifier in the Model assignment statement match」⟦9618_w22_31:11(b)⟧
- 「PRIVATE OwnerName : STRING」⟦9618_s22_32:1(c)(i)⟧

**得分点地图**（口径同 FP-05。本型核验语料只有 2 行，都已拆分：⟦9618_w22_31:11(b)⟧ 与 s26 的一道）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| `CLASS 类名 … ENDCLASS`、构造方法头 | 2 | `class-definition` |
| 属性声明为 `PRIVATE` 并带类型 | 2 | `encapsulation`、`data-types` |
| 构造方法里用参数给属性赋值，名字前后一致 | 2 | `assign-value` |

**易错与失分**
- 漏 `ENDCLASS`、声明与构造方法里没用题目已有的名字：考官报告指出这些是典型错误，题目里已经在用的变量名必须照用（⟦9618_w22_31:11(b)⟧）。
- 属性写 `PUBLIC` 或干脆不写：题目说 available only through the methods of the class，就要 `PRIVATE`。
- 参数表漏类型，或把赋固定值的属性也放进参数表。
- 构造方法写成 Python 的 `__init__` 或 `def`：要求伪代码时按 D2 不给分。

#### 代表题精讲　⟦9618_w22_31:11(b)⟧

**在考什么**　补全类 `Car` 的伪代码，使它能创建对象。要有 make、model、body type、fuel type 四个字符串属性和一个整数属性（同类车造了多少辆）；属性只能通过类的方法访问。题目已给 `PRIVATE Make : STRING`、构造方法的第一个参数 `CarMake : STRING`、赋值 `BodyType ← CarBodyType`、`Fuel ← ""`、`NumberBuilt ← 0`。5 分。讲解时对照原卷 QP p.10（同页上方是 11(a) 的术语定义）。

**完整作答**（带注释的是要填的部分；题目末尾列出的 `GetFuel()`、`GetNumberBuilt()` 只是方法名，不用写方法体）

```pseudocode
CLASS Car                                     // gap: class name
   PRIVATE Make : STRING
   PRIVATE Model : STRING                     // gap: four declarations
   PRIVATE BodyType : STRING
   PRIVATE Fuel : STRING
   PRIVATE NumberBuilt : INTEGER
   PUBLIC PROCEDURE NEW(CarMake : STRING, CarModel : STRING, CarBodyType : STRING)   // gap: two parameters
      Make ← CarMake                          // gap
      Model ← CarModel                        // gap
      BodyType ← CarBodyType
      Fuel ← ""
      NumberBuilt ← 0
   ENDPROCEDURE
   // GetFuel() and GetNumberBuilt() are listed here in the question
ENDCLASS                                      // gap
```

原卷印的构造方法名是 `New`；MS 与 2027–29 指南都写 `NEW`。

**与 MS 逐点对齐**（MS p.13，One mark for each point）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | Car and ENDCLASS | 第一行的 `Car` 与最后一行的 `ENDCLASS`，两处合一分 |
| 2 | Four declarations – must use the identifiers used in the assignments | `Model`、`BodyType`、`Fuel`、`NumberBuilt` 四行，名字与下面赋值语句左边一致 |
| 3 | Constructor header – must use CarBodyType | 参数表里有 `CarBodyType : STRING` |
| 4 | Two assignments – must use CarMake | `Make ← CarMake`、`Model ← CarModel` |
| 5 | Constructor identifier for the car model and the identifier in the Model assignment statement match | 参数 `CarModel` 与 `Model ← CarModel` 用同一个名字 |

**规范代码要点**　这道题的五分里有三分是“名字对上”：属性名对上赋值左边，参数名对上赋值右边，`CarBodyType` 从已给的赋值里抄。

**直观**　类是一张空白登记表的设计：`PRIVATE` 那几行是表上的栏目，`NEW` 是“新登记一辆车时，前台按客户报的三样信息填表，另外两栏先填默认值”。

**同题 Python 版要点**
- `class Car:`；`def __init__(self, CarMake, CarModel, CarBodyType):`，里面 `self.__Make = CarMake` 等；私有属性用两个下划线开头。
- 固定初值也写在 `__init__` 里：`self.__Fuel = ""`、`self.__NumberBuilt = 0`。

**与阶梯 / P4 的衔接**　先过阶梯 **L12 E01**（私有属性、构造、getter / setter），**L12 E02** 练读 `INHERITS` 与 `SUPER`。P4 例：⟦9618_w24_41:2(a)(i)⟧（声明类 `Horse` 及其构造方法）。

**下一道变式**　⟦9618_s22_32:1(c)(i)⟧　（记录类型改写成类后，写出把 `OwnerName` 声明为 PRIVATE 的一句，1 分。）

<!-- auto:drills P3-FP-06 -->

### P3-FP-07　声明式编程：写事实　{#P3-FP-07}

<!-- auto:stats P3-FP-07 -->

**考法**　给出一个事实库（带行号）和几行“子句 → 含义”的对照，再用一句话描述新信息，要求把它写成 2–4 个新的事实子句，一句一分。

**识别信号**　More facts are to be included；Write the additional clauses to record these facts；Write additional clauses to represent this information。

**解题思路（逐步作答模板）**
1. **把题目的一句话拆成几件事**，每件事对应事实库里**已有的一种谓词**。例：“Carlos is a person who enjoys the hobby of cycling but does not like music” → 是一个人 / 骑车是一种爱好 / 喜欢骑车 / 不喜欢音乐。
2. **逐个查事实库**：新出现的人或物，如果库里还没有说明它属于哪一类的事实（`person(…)`、`hobby(…)`），就要补这一句；已经有的（`hobby(music).` 在库里）不用重复。补几句以 MS 为准，答题空行的数目是很好的提示。
3. **照抄谓词名与参数顺序**：看“子句 → 含义”表——`enjoys(natasha, travelling)` 是“Natasha enjoys travelling”，所以人在前、爱好在后。
4. **格式**：谓词与常量全部**小写**；多个词用下划线连成一个（`sliding_doors`）；参数之间逗号；每句以**句点**结束。

**得分表述**（引自对应 MS）
- 「One mark for each correctly completed clause」⟦9618_w23_32:11(a)⟧
- 「hobby(cycling)」⟦9618_w23_32:11(a)⟧
- 「dislikes(carlos, music)」⟦9618_w23_32:11(a)⟧
- 「feature(sliding_doors)」⟦9618_s24_31:8(a)⟧
- 「unavailable(sliding_doors, hatchback)」⟦9618_s24_31:8(a)⟧
- 「tutors(nina, sam)」⟦9618_s22_32:2(a)⟧

**易错与失分**
- 大写字母与漏句点：考官报告指出，记得每句以句点结束、全文不出现大写字母的考生拿到最高分（⟦9618_s24_31:8(a)⟧）。大写开头的词在声明式语言里是**变量**，`Carlos` 会被当成变量。
- 漏写“它属于哪一类”的事实：新的爱好 cycling、新的功能 sliding_doors 都要先补 `hobby(cycling).`、`feature(sliding_doors).`。
- 参数顺序颠倒：`tutors(sam, nina)` 的意思变成“Sam 是 Nina 的导师”。
- 多词常量写成两个词或带空格：`sliding doors` 要写成 `sliding_doors`。

#### 代表题精讲　⟦9618_w23_32:11(a)⟧

**在考什么**　事实库：`hobby(…)`（01–06，含 music、caving、climbing、camping、baking、travelling）、`person(…)`（07–12）、`enjoys(人, 爱好)`（13–18）、`dislikes(toby, caving)`（19）。新信息：Carlos is a person who enjoys the hobby of cycling but does not like music. 写出 20–23 四句，4 分。讲解时对照原卷 QP p.10。

**完整作答**

```text
20 person(carlos).
21 hobby(cycling).
22 enjoys(carlos, cycling).
23 dislikes(carlos, music).
```

**与 MS 逐点对齐**（MS p.8，One mark for each correctly completed clause，Max 4）

| MP | MS 原文 | 为什么要写这一句 |
|:--|:--|:--|
| 1 | person(carlos). | Carlos 是新出现的人，库里没有 |
| 2 | hobby(cycling). | cycling 不在 01–06 的爱好里 |
| 3 | enjoys(carlos, cycling). | 按 `enjoys(人, 爱好)` 的顺序 |
| 4 | dislikes(carlos, music). | “does not like” 对应库里已有的谓词 `dislikes`；music 已是爱好（01），不必再写 `hobby(music).` |

**英文作答句**　person(carlos). hobby(cycling). enjoys(carlos, cycling). dislikes(carlos, music).

**直观**　事实库是一本只能“登记”的名册：新来的人先登记“他是谁”，新出现的东西先登记“它是什么”，然后才能登记“谁喜欢什么”。

**下一道变式**　⟦9618_s24_31:8(a)⟧　（汽车功能库：滑门是一种功能，minivan 有、hatchback 没有，写三句，3 分。）

<!-- auto:drills P3-FP-07 -->

### P3-FP-08　声明式编程：目标及其结果　{#P3-FP-08}

<!-- auto:stats P3-FP-08 -->

**考法**　①给出一个目标的结果作示范，要求写出另一个目标返回的变量值（1 分）；②用指定变量写出一个查询目标（1 分）；③用两三个子目标与共享变量组合条件写目标（2–4 分）。

**识别信号**　Using the variable …, the goal: … returns …；Write the result returned by the goal；Write the goal, using the variable …, to find all the …。

**解题思路（逐步作答模板）**
1. **求结果**：在事实库里找出所有与目标匹配的事实（谓词相同、常量位置相同），把变量位置上的常量**按库里的顺序**列出，逗号分隔、全部小写、不加句点。
2. **写单个目标**：把要找的东西放在变量的位置，已知条件写成常量。“找出所有家养的猫”→ `type(Pet, domestic)`。变量名用题目指定的（大写开头）。
3. **写组合目标**：
   - 把条件拆成几个子目标，每个子目标是库里已有的一种谓词；
   - 题目指定的变量放在“要找的人 / 物”的位置；
   - 子目标之间要**共享**的东西用同一个新变量（如 R、S），放在正确的参数位置；
   - 子目标之间用逗号连接。本型 MS 范例只见逗号；目标里写 AND 的写法 MS 未见，不保证给分。规则题 FP-09 的 MS 写 “allow , for AND”，意思是规则里可以用逗号代替 AND，不是反过来。
4. **检查**：把一个题目给的例子代进去，看每个子目标是否都在库里成立。

**得分表述**（引自对应 MS）
- 「one mark for correct use of X」⟦9618_s22_32:2(c)⟧
- 「one mark for two other variables in correct positions」⟦9618_s22_32:2(c)⟧
- 「one mark for three correct clauses in any order」⟦9618_s22_32:2(c)⟧
- 「one mark for correct syntax」⟦9618_s22_32:2(c)⟧
- 「spots(WildSpotty, yes)」⟦9618_s22_31:2(c)(ii)⟧
- 「X = tomaz, pietre, nico」⟦9618_w23_31:11(b)⟧

**易错与失分**
- 结果里带了大写或句点：考官报告指出，写对结果并且没有引入大写字母、末尾没加句点的考生拿到这一分（⟦9618_s24_31:8(b)⟧、⟦9618_w23_31:11(b)⟧）。
- 组合目标的两部分没有连起来：考官报告指出很多考生写出了两部分，但没有用正确的连接写法（⟦9618_s22_31:2(c)(ii)⟧）。
- 组合目标缺少共享变量或位置放错：考官报告指出很多回答没有用合适的变量、语法也不对（⟦9618_s22_32:2(c)⟧）。
- 把常量写成大写（`Domestic`）：它就变成了变量，会匹配所有类型。

#### 代表题精讲　⟦9618_s22_32:2(c)⟧

**在考什么**　学校事实库：`teaches(老师, 科目)`、`studies(学生, 科目)`、`tutors(导师, 学生)`。用变量 X 写出一个目标，找出所有“导师也教他某门课”的学生；例子：Hua 的导师是 Alan，Alan 也教 Hua 数学。4 分。讲解时对照原卷 QP p.4（事实库与子句含义表）与 p.5（本小问）。

**完整作答**

```text
teaches(R, S), studies(X, S), tutors(R, X).
```

拆开看：R 是一位老师，教科目 S；学生 X 也学 S；R 是 X 的导师。三个子目标共享 R（老师 = 导师）和 S（同一门课）。用例子检查：R = alan，S = mathematics，X = hua，三句都在库里。

**与 MS 逐点对齐**（MS p.4）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | one mark for correct use of X | X 在 `studies` 的学生位置和 `tutors` 的学生位置 |
| 2 | one mark for two other variables in correct positions | R 在老师 / 导师位置，S 在科目位置 |
| 3 | one mark for three correct clauses in any order | `teaches`、`studies`、`tutors` 三个子目标都有 |
| 4 | one mark for correct syntax | 逗号连接、括号、句点 |

**英文作答句**　teaches(R, S), studies(X, S), tutors(R, X).

**直观**　组合目标像一份“同时满足”的筛选：同一个字母出现在两处，就是在说“这两处必须是同一个人 / 同一门课”。

**下一道变式**　⟦9618_s22_31:2(c)(ii)⟧　（猫的事实库：用变量 WildSpotty 找出所有有斑点的野猫，两个子目标用逗号连起来，2 分。）

<!-- auto:drills P3-FP-08 -->

### P3-FP-09　声明式编程：写规则　{#P3-FP-09}

<!-- auto:stats P3-FP-09 -->

**考法**　给出规则头（如 `may_choose_option(F, B)`）和一句条件文字，要求写出 `IF` 后面的部分。4 分：每个子目标一分（通常三个），运算符与标点全对、没有多余代码再一分。

**识别信号**　Write this as a rule；… IF；may choose … if … and … is not / has not already …。

**解题思路（逐步作答模板）**
1. **把条件句按 and 拆开**，每一段对应事实库里的一种谓词。
2. **肯定的部分直接写子目标**：“F is a feature” → `feature(F)`；“B is a body style” → `bodystyle(B)`。
3. **否定的部分加 NOT**：“F is not unavailable for that body style” → `NOT unavailable(F, B)`；“C has not already done A” → `NOT done(C, A)`。
4. **变量照抄规则头里的字母**，位置照谓词的参数顺序。
5. **用 AND（或逗号）连接，结尾加句点**；不多写任何子目标或行。

**得分表述**（引自对应 MS）
- 「feature(F) AND bodystyle(B) AND NOT unavailable(F, B)」⟦9618_s24_31:8(c)⟧
- 「all correct Boolean operators and punctuation (allow , for AND) and no additional lines of code」⟦9618_s24_31:8(c)⟧
- 「There must be the correct number of terms」⟦9618_s24_32:10(c)⟧
- 「IF person(N) AND hobby(H) AND NOT dislikes(N, H)」⟦9618_w23_32:11(c)⟧
- 「all logical operators correct with no additional code」⟦9618_w23_32:11(c)⟧

**易错与失分**
- 漏了“它是一个 …”的子目标，只写了否定的那一句：三个子目标各一分，漏一个就丢一分；⟦9618_s24_32:10(c)⟧ 的 MS 还写明运算符那一分要求项数正确。
- 否定写成 `unavailable(F, B) = FALSE` 或 `NOT_unavailable`：MS 的范例都写 `NOT 子目标`。
- 多写了行（例如把规则头又写一遍、或再加一个子目标）：MS 要求 no additional lines of code。
- 变量换了字母或位置：规则头是 `(F, B)`，子目标里也要用 F、B，`unavailable(F, B)` 的顺序照事实库。
- 这一问比前两问难：考官报告指出最后一部分要根据给定信息构造规则，难度更大，但多数考生至少拿到一分（⟦9618_w23_31:11(c)⟧）。

#### 代表题精讲　⟦9618_s24_31:8(c)⟧

**在考什么**　汽车功能库（`feature(…)`、`bodystyle(…)`、`available(功能, 车型)`、`unavailable(功能, 车型)`）。条件：F may be available for B if F is a feature and B is a body style and F is not unavailable for that body style. 写出规则 `may_choose_option(F, B) IF …`。4 分。讲解时对照原卷 QP p.9（事实库在 p.8）。

**完整作答**

```text
may_choose_option(F, B)
IF feature(F) AND bodystyle(B) AND NOT unavailable(F, B).
```

**与 MS 逐点对齐**（MS p.11，One mark per mark point，Max 4）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | feature(F) | 第 1 个子目标 |
| 2 | bodystyle(B) | 第 2 个子目标 |
| 3 | unavailable(F, B) | 第 3 个子目标（前面带 NOT） |
| 4 | all correct Boolean operators and punctuation (allow , for AND) and no additional lines of code | 两个 AND、一个 NOT、句点，没有多余行 |

MS 还给了逗号版的范例：`feature(F), bodystyle(B), NOT unavailable(F, B).`

**英文作答句**　may_choose_option(F, B) IF feature(F) AND bodystyle(B) AND NOT unavailable(F, B).

**直观**　规则是一张“入场条件”清单：先确认身份（它是功能、它是车型），再排除黑名单（这款车型不提供这个功能）。

**下一道变式**　⟦9618_w23_32:11(c)⟧　（爱好库：N might enjoy H if H is a hobby and N does not dislike H，写出 `might_enjoy(N, H) IF …`，4 分。）

<!-- auto:drills P3-FP-09 -->

### P3-FP-10　文件处理伪代码　{#P3-FP-10}

<!-- auto:stats P3-FP-10 -->

**考法**　补全文件处理伪代码，5–7 处空，一空（一行）一分。几种常见情境：①随机文件按位置读出并显示（`SEEK` + `GETRECORD`）；②逐个位置查找某条记录（标志 + 条件循环）；③找第一个空位插入新记录（`PUTRECORD`）；④把一个随机文件的记录复制到另一个随机文件；⑤用散列函数算出位置后直接读记录；⑥文本文件逐行复制到另一个文件，读到 `EOF`。

**识别信号**　Complete this file handling / file-handling pseudocode；The pseudocode algorithm … uses random file access to …；… reads … records stored in a random file using the user-defined data type …；A function is required to find … in a random file。

**解题思路**
1. **先认文件种类**：出现 `SEEK`、`GETRECORD`、`PUTRECORD`、`.dat`、用户定义的记录类型 → 随机文件，`FOR RANDOM`；出现 `READFILE`、`WRITEFILE`、`.txt`、一行一行 → 文本文件，`FOR READ` / `FOR WRITE` / `FOR APPEND`。
2. **四步骨架**：打开 → （循环里）定位 → 读 / 写 → 关闭。填空时先检查这四步哪一步缺了。
3. **随机文件：每一次 GETRECORD / PUTRECORD 前面都有一个 SEEK**，把文件指针移到要读写的位置。复制到另一个文件时，**两个文件各自 SEEK**。
4. **用到的每个文件都要打开、都要关闭**：题目只给了一个 `OPENFILE`，另一个文件的 `OPENFILE` 往往就是一空；同理 `CLOSEFILE`。
5. **循环**：位置个数已知 → `FOR Position ← 1 TO n`；找到就停 → `WHILE NOT Found AND Position <= Max`；读到文件末尾 → `WHILE NOT EOF(…)` 或 `REPEAT … UNTIL EOF(…)`。
6. **名字照抄**：文件名（字符串字面量，或存文件名的变量）、记录变量、字段名（`Grade.ExamGrade`）都用题目已有的。
7. **不依赖 AND 短路**（决策 D25）：`WHILE` 条件里只放标志与位置的比较，读记录放进循环体。

**伪代码模板**

```pseudocode
// random file: find a record by searching every position in turn
DECLARE Customer : TAccount
DECLARE Location : INTEGER
DECLARE Found : BOOLEAN
OPENFILE "AccountRecord.dat" FOR RANDOM
Found ← FALSE
Location ← 1
WHILE NOT Found AND Location <= 1000
   SEEK "AccountRecord.dat", Location        // move the file pointer first
   GETRECORD "AccountRecord.dat", Customer   // then read the record there
   IF Customer.Name = SearchName THEN
      OUTPUT Customer
      Found ← TRUE
   ENDIF
   Location ← Location + 1
ENDWHILE
IF NOT Found THEN
   OUTPUT "Customer does not exist"
ENDIF
CLOSEFILE "AccountRecord.dat"

// random file: copy every record from one file to another
OPENFILE "Current.dat" FOR RANDOM
OPENFILE "Stored.dat" FOR RANDOM              // every file used is opened ...
FOR Position ← 1 TO 50
   SEEK "Current.dat", Position
   GETRECORD "Current.dat", Grade
   SEEK "Stored.dat", Position                // ... and has its own SEEK
   PUTRECORD "Stored.dat", Grade
NEXT Position
CLOSEFILE "Current.dat"                       // ... and is closed
CLOSEFILE "Stored.dat"

// text file: copy line by line until the end of the file
OPENFILE "ActiveFile.txt" FOR READ
OPENFILE "ArchiveFile.txt" FOR WRITE
WHILE NOT EOF("ActiveFile.txt")
   READFILE "ActiveFile.txt", Account
   WRITEFILE "ArchiveFile.txt", Account
ENDWHILE
CLOSEFILE "ActiveFile.txt"
CLOSEFILE "ArchiveFile.txt"
```

**得分表述**（引自对应 MS）
- 「OPENFILE "CurrentResults.dat" FOR RANDOM」⟦9618_s25_32:13⟧
- 「SEEK "StoredResults.dat", Position」⟦9618_s25_32:13⟧
- 「PUTRECORD "StoredResults.dat", Grade」⟦9618_s25_32:13⟧
- 「GETRECORD "StockList.dat", CurrentStock」⟦9618_s25_33:11⟧
- 「WHILE NOT EOF("ActiveFile.txt")」⟦9618_s23_31:10⟧
- 「CLOSEFILE "ActiveFile.txt"」⟦9618_s23_31:10⟧

**得分点地图**（口径同 FP-05。共 8 行：⟦9618_s23_31:10⟧、⟦9618_s23_32:6(b)⟧、⟦9618_s25_31:12⟧、⟦9618_s25_32:13⟧、⟦9618_s25_33:11⟧、⟦9618_w23_31:8(a)⟧、⟦9618_w23_32:12(b)⟧，以及 s26 的一道）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 随机文件语句：`OPENFILE … FOR RANDOM`（7 行）、`SEEK 文件, 位置`（6 行）、`GETRECORD 文件, 变量`（5 行）、`PUTRECORD 文件, 变量`（2 行） | 7 | `random-file` |
| `CLOSEFILE 文件` | 4 | `file-close` |
| 初值：文件名变量、位置从 1 开始、标志设 FALSE | 3 | `initialise-variables` |
| 读到文件末尾：`WHILE NOT EOF(…)` / `UNTIL EOF(…)` | 2 | `loop-to-eof` |
| 输出记录或“不存在”的提示 | 2 | `output-format` |
| 给字段或位置赋值（`Grade.ExamGrade ← "Missing grade"`、`Location ← Hash(…)`） | 2 | `assign-value` |
| 找到 / 已存放的标志：设初值、循环后判断 | 2 | `flag-variable` |
| 比较：标志或字段与值比较 | 2 | `relational-ops` |
| 文本文件：`FOR READ` 打开、`WRITEFILE` 写出 | 1 | `file-open-read`、`file-write` |
| 循环的写法：`FOR Position ← 1 TO 50`；`WHILE NOT FoundFlag AND Location <= MaxSize`；`REPEAT … UNTIL` | 各 1 | `count-loop` 与 `loop-bounds`、`pre-condition-loop` 与 `logic-ops`、`post-condition-loop` |
| 其他标签（各 1 行） | 各 1 | `module-header`、`return-value`、`nested-if`、`procedure-call`、`input-prompt`、`array-index` |

**易错与失分**
- 不按指南写：考官报告指出，作答越贴近已出版伪代码指南里的例子，得分越高（⟦9618_s23_32:6(b)⟧）；另几卷也说熟悉指南里文件处理写法的考生分最高（⟦9618_s25_31:12⟧、⟦9618_s25_32:13⟧、⟦9618_s25_33:11⟧）。
- `GETRECORD` 前没有 `SEEK`，或只给一个文件 `SEEK`：复制题里两个文件要各自定位。
- 只打开 / 关闭了题目已给的那个文件：另一个文件的 `OPENFILE`、`CLOSEFILE` 常常就是空。
- 随机文件用 `READFILE` / `WRITEFILE`，或文本文件用 `FOR RANDOM`：两套命令不能混。
- 用了编程语言的写法（`open()`、`for line in file`）：要求伪代码时按 D2 不给分。
- 散列定位题：考官报告指出很多考生觉得难（⟦9618_w23_31:8(a)⟧）。关键是 `Location ← Hash(Customer.AccountNumber)`，参数是记录里的账号字段。

#### 代表题精讲　⟦9618_s25_32:13⟧

**在考什么**　用随机文件存取，把 50 条记录从 `CurrentResults.dat` 逐条复制到 `StoredResults.dat`；记录类型 `StudentResult`（`LastName`、`FirstName`、`ExamGrade`）。如果成绩缺失（空字符串），存到新文件里的 `ExamGrade` 写成 `"Missing grade"`。5 处空，5 分。讲解时对照原卷 QP p.13（同页上方是 12(b) 的 OOP 术语）。

**完整作答**（带注释的 5 行是要填的）

```pseudocode
DECLARE Grade : StudentResult
DECLARE Position : INTEGER
OPENFILE "CurrentResults.dat" FOR RANDOM            // gap 1
OPENFILE "StoredResults.dat" FOR RANDOM
FOR Position ← 1 TO 50                              // gap 2
   SEEK "CurrentResults.dat", Position
   GETRECORD "CurrentResults.dat", Grade
   IF Grade.ExamGrade = "" THEN
      Grade.ExamGrade ← "Missing grade"             // gap 3
   ENDIF
   SEEK "StoredResults.dat", Position               // gap 4
   PUTRECORD "StoredResults.dat", Grade             // gap 5
NEXT Position
CLOSEFILE "CurrentResults.dat"
CLOSEFILE "StoredResults.dat"
```

**与 MS 逐点对齐**（MS p.12，One mark for each correctly completed line）

| MP | MS 原文 | 为什么这样填 |
|:--|:--|:--|
| 1 | OPENFILE "CurrentResults.dat" FOR RANDOM | 后面要从它 SEEK、GETRECORD，最后也关闭了它，却没打开 |
| 2 | FOR Position ← 1 TO 50 | 结尾有 `NEXT Position`；复制 50 条 |
| 3 | Grade.ExamGrade ← "Missing grade" | IF 判断成绩为空，改的是记录里的字段 |
| 4 | SEEK "StoredResults.dat", Position | 写入前把新文件的指针移到同一位置 |
| 5 | PUTRECORD "StoredResults.dat", Grade | 把（可能改过的）记录写进新文件 |

**规范代码要点**　五个空全部能从“已给的行”推出来：有 `CLOSEFILE` 就要有 `OPENFILE`；有 `NEXT` 就要有 `FOR`；有 `GETRECORD` 读出来，就要有 `SEEK` + `PUTRECORD` 写进去。

**直观**　随机文件像一排编了号的储物柜：`SEEK` 是走到第几号柜子前，`GETRECORD` 是把里面的东西拿出来，`PUTRECORD` 是放进去（原来的东西被换掉）。复制就是在两排柜子之间，同号对同号地搬。

**同题 Python 版要点**
- P4 的文件题只用文本文件：`open("Data.txt", "r")`、逐行读到文件尾、`close()`，并把文件操作放进 `try … except`。随机文件的 `SEEK` / `GETRECORD` 只在伪代码里考。

**与阶梯 / P4 的衔接**　文本文件先过阶梯 **L07 E01**（读到文件尾、跳过空行、写新文件的干跑与翻译）和 **L07 E05**（按条件写出）；带异常处理的读文件见 **L09 E03**。P4 例：⟦9618_w24_42:3(b)⟧（从文本文件读数据存进数组）。

**迁移与卡点**
- **卡点**：每次 GETRECORD / PUTRECORD 前面都要有 SEEK；用到的每个文件都要 OPENFILE 和 CLOSEFILE；随机文件与文本文件两套命令不能混。填空题从已给的行推：配对、对称、名字。
- **考官在换什么**：复制、查找、插入、散列定位、文本文件复制；循环种类（固定次数、找到就停、到 EOF）。四步骨架（打开 → 定位 → 读 / 写 → 关闭）不变。
- **从代表题到变式**：代表题固定 50 次、两个文件各自 SEEK；变式是按名字逐位置查找——条件循环 `WHILE NOT FoundFlag AND Location <= MaxSize`，循环里 SEEK + GETRECORD + 比较字段，找到设标志，循环后找不到输出提示。搬过去的是四步骨架和 SEEK 的位置；要换的是循环（从计数变成标志）和循环后的判断。
- **反例**：`WHILE` 条件里读记录、依赖 AND 短路（D25）；用 READFILE 读随机文件。

**下一道变式**　⟦9618_w23_32:12(b)⟧　（在随机文件里按名字逐个位置查找客户记录，找不到输出提示，7 分：打开、标志初值、输入、`WHILE NOT FoundFlag AND Location <= MaxSize`、`SEEK`（2 分）、提示文字。）

<!-- auto:drills P3-FP-10 -->

### P3-FP-11　异常与异常处理　{#P3-FP-11}

<!-- auto:stats P3-FP-11 -->

**考法**　①定义或解释异常处理（1–3 分，常要求举一个异常的原因）；②描述什么是异常并举例（2–3 分）；③说出两个可能引起异常的原因（2 分）；④说明写异常处理程序的理由（4 分）；⑤怎样避免程序因异常而终止（2 分）。P3 不写异常处理代码（那是 P4）。

**识别信号**　Define the term exception handling；Explain what is meant by exception handling；Describe, with an example, what is meant by an exception；State / Identify two possible causes of an exception；State the reasons for including exception handling routines；Describe how program termination due to an exception can be avoided。

**解题思路**
1. **先分清问的是 exception 还是 exception handling**：
   - exception（异常）：程序**运行时**发生的意外 / 不想要的事件，打断正常执行，可能让程序意外停止。
   - exception handling（异常处理）：**对这类事件作出响应**的过程，使程序不会意外停止。
2. **原因三大类**（各举一个具体例子更稳）：编程错误（除以零、数组下标越界）；用户错误（输入了错误类型的数据、错误的文件名）；硬件故障（硬盘损坏、与打印机断开连接）。
3. **为什么要写异常处理程序**：捕获运行时错误；防止程序意外停止；给出有意义的错误信息；再举一个例子（除以零、文件不存在、读到文件尾）。
4. **怎样避免终止**：写异常处理例程（`try … except` / catch），出错时给出提示而不是崩溃。

**得分表述**（引自对应 MS）
- 「Exception handling is a process that responds to unwanted / unexpected events when a program runs」⟦9618_w25_31:10⟧
- 「to prevent the program / computer from stopping unexpectedly」⟦9618_w25_31:10⟧
- 「Hardware failure // losing connection to a device such as a printer」⟦9618_w25_31:10⟧
- 「An exception is an unplanned / unexpected event that occurs when a program is running」⟦9618_w25_33:12(a)⟧
- 「To prevent a program halting unexpectedly」⟦9618_s22_32:9⟧
- 「To produce meaningful error messages for these errors」⟦9618_s22_32:9⟧

**易错与失分**
- 问异常，答成异常处理（或反过来）：考官报告多次指出这一点（⟦9618_w25_33:12(a)⟧、⟦9618_w23_32:12(a)⟧、⟦9618_w23_31:8(b)⟧）。
- 把异常和中断混为一谈：考官报告指出有考生这样答（⟦9618_w25_32:10(a)⟧、⟦9618_w25_33:12(a)⟧）；问异常处理的理由时，常见错误是去解释中断处理（⟦9618_s22_32:9⟧）。中断是硬件 / 软件发给处理器的信号（P1-PF），异常是程序运行中的错误事件。
- 原因只写“出错了”：写成“编程错误 / 用户错误 / 硬件故障”之一，最好再带一个具体例子。

#### 代表题精讲　⟦9618_w25_31:10⟧

**在考什么**　Explain what is meant by exception handling. Include an example of a possible cause of an exception in your answer. 3 分：解释最多 2 分，例子 1 分。讲解时对照原卷 QP p.10。

**完整作答**
- Explanation: Exception handling is a process that responds to unexpected events (exceptions) when a program is running, so that the program does not stop unexpectedly.
- Example: a hardware failure, such as losing the connection to a printer while the program is printing.

**与 MS 逐点对齐**（MS p.14）

| MP | MS 原文 | 作答中对应 |
|:--|:--|:--|
| 1 | Exception handling is a process that responds to unwanted / unexpected events when a program runs | 解释的前半句 |
| 2 | … to prevent the program / computer from stopping unexpectedly | 解释的后半句（so that …） |
| 3–5 | Programming errors / User errors / Hardware failure // losing connection to a device such as a printer | 例子：任写一个，Max 1 |

解释部分 Max 2，例子部分 Max 1，两栏各自封顶。

**英文作答句**　Exception handling is the process of responding to unexpected events when a program is running, to prevent the program from stopping unexpectedly. For example, losing the connection to a printer (hardware failure).

**直观**　异常是“路上突然断了桥”；异常处理是事先准备好的绕行方案——不至于整车翻进河里（程序崩溃）。

**与阶梯 / P4 的衔接**　阶梯 **L09 E01**（`try` / `except ValueError` 安全转换）与 **L09 E03**（读文件时处理文件不存在与坏数据行）。P4 例：⟦9618_w24_42:3(b)⟧ 的 MS 要求读文件时有异常处理。

**下一道变式**　⟦9618_s22_32:9⟧　（State the reasons for including exception handling routines，并举一个异常的例子，4 分：捕获运行时错误、防止程序意外停止、给出有意义的错误信息、例子。）

<!-- auto:drills P3-FP-11 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| FP-02 与 FP-03 | FP-02 读代码：说寻址方式、算 ACC 或标签的值；FP-03 写代码 | Write assembly language code → FP-03；State the addressing mode / the value of … → FP-02 |
| FP-02 / FP-03 与 P1-PF-08 至 PF-10 | 内容相同，P3 卷的行一律归 P3 题型 | 看卷号：9618_x_3x 是 P3 |
| `LDD` 与 `LDI` | `LDD a`：取地址 a 的内容；`LDI a`：a 里是另一个地址，取那个地址的内容 | 题目说 the address contained in the variable → `LDI` |
| FP-04 与 FP-05 / FP-06 | FP-04 是文字定义；FP-05 补类图；FP-06 写 `CLASS … ENDCLASS` 伪代码 | Define / Describe / Identify the term → FP-04；Complete the class diagram → FP-05；Complete the pseudocode for the class → FP-06 |
| FP-06 与 P3-DR-03 | 类：属性 + 方法 + 构造方法，常带 `PRIVATE`；记录：`TYPE … ENDTYPE`，只有字段 | 有 `CLASS`、`NEW`、`PRIVATE` → FP-06 |
| 封装与 PRIVATE 的“安全” | 封装是属性只能被本类的方法访问；不是防止未授权用户看数据 | 答 PRIVATE 的理由时写 class’s own methods |
| 继承与多态 | 继承：子类获得父类的属性和方法；多态：同名方法在子类中被重新定义、表现不同 | 题目说 redefined / behave differently → 多态 |
| FP-07 与 FP-08 | FP-07 写**事实**（全是常量，句点结尾）；FP-08 写**目标**或目标的结果（含变量） | 题目给了变量名 → FP-08 |
| FP-08 与 FP-09 | FP-08 是查询：子目标用逗号连起来；FP-09 是规则：有规则头和 `IF`，常带 `NOT` | Write this as a rule … IF → FP-09 |
| 常量与变量（声明式） | 小写开头是常量，大写开头是变量 | `carlos` 是人，`Carlos` 是变量 |
| 随机文件与文本文件（FP-10） | 随机：`FOR RANDOM`、`SEEK`、`GETRECORD`、`PUTRECORD`、记录变量；文本：`FOR READ / WRITE / APPEND`、`READFILE`、`WRITEFILE`、一行一个字符串 | `.dat` + 用户定义类型 → 随机；`.txt` + 逐行 → 文本 |
| FP-10 与 P3-DR-06 至 DR-08 | FP-10 写文件处理代码；DR 题型讲文件组织、存取方式、散列的概念 | Complete the pseudocode → FP-10；Describe / State the file organisation → DR |
| FP-11 的 exception 与 exception handling | 异常是运行时的意外事件；异常处理是对它的响应，使程序不意外停止 | Define exception handling / Explain what is meant by an exception：先看清问哪个 |
| 异常与中断 | 异常是程序运行时的错误事件；中断是发给处理器、要求它处理某事的信号（P1-PF） | 题目问 exception 却想写 ISR、优先级 → 写偏了 |
