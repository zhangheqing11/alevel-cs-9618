## FP　进一步编程：核心概念 {#core-FP}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。写代码的部分（`CLASS … ENDCLASS`、随机文件与文本文件的处理）在对应题型卡里。

### 编程范式

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Programming paradigm | A style or approach to programming, with its own way of structuring and writing programs.（非 MS 原句） | 写程序的一种风格与组织方式；考纲列出命令式、声明式、面向对象、低级四种 | 同一件事的不同“说法” | P3-FP-01 |
| Imperative (procedural) | 「Imperative languages use variables」⟦9618_s21_31:9(a)⟧；「The statements provide a sequence of commands for the computer to perform」⟦9618_s21_31:9(a)⟧ | 用变量，用赋值语句改变变量的值；程序是一串按书写顺序执行的命令，常有循环；过程式把命令组织成过程与函数 | 菜谱：第一步、第二步…… | P3-FP-01 |
| Declarative | 「Instructs a program on what needs to be done instead of how to do it」⟦9618_s21_31:9(b)⟧ | 只描述要什么结果（事实、规则、目标），由系统去找出满足目标的答案 | 跟餐厅说“我要一份番茄炒蛋” | P3-FP-01、P3-FP-07 至 FP-09 |
| Object-oriented | Programs are built from classes and objects, using inheritance, encapsulation and polymorphism.（非 MS 原句） | 用类和对象组织程序：数据（属性）和操作数据的方法放在一起 | 先定义“厨师”能做什么，再请几位厨师来做 | P3-FP-01、P3-FP-04 至 FP-06 |
| Low-level | 「Programs using the instruction set of a processor」⟦9618_w21_31:2⟧ | 直接用处理器指令集写的程序（汇编语言、机器码） | 直接指挥每块肌肉怎么动 | P3-FP-01 至 FP-03 |

### 汇编与寻址方式

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Accumulator (ACC) | The register that holds the value being worked on; results of ADD and SUB are left in it.（非 MS 原句） | 本卷汇编题设定处理器只有 ACC 这一个寄存器可用（题干语）：取数放进 ACC，加减在 ACC 上做，结果再从 ACC 存出去 | 只有一只手 | P3-FP-02、P3-FP-03 |
| Immediate addressing | 「LDM #500: Immediate 500」⟦9618_s22_31:9(a)⟧ | 操作数本身就是要用的数（前面带 `#`） | 直接把钱给你 | P3-FP-02、P3-FP-03 |
| Direct addressing | 「LDD 500: Direct 100」⟦9618_s22_31:9(a)⟧ | 操作数是一个地址，取这个地址里的内容 | 钱在 500 号柜子里 | P3-FP-02、P3-FP-03 |
| Indirect addressing | 「LDI 500: Indirect 20」⟦9618_s22_31:9(a)⟧ | 操作数地址里存的是另一个地址，取那个地址里的内容 | 500 号柜子里有张纸条：钱在 100 号 | P3-FP-02、P3-FP-03 |
| Label | 「Storing 100 at a labelled address away from the code」⟦9618_w25_31:11(a)⟧ | `<label>: <data>` 给一个内存位置起名字并设初值，代码里可以用标签代替地址；标签写在代码之外 | 柜子上贴的名字 | P3-FP-03 |

### 面向对象（OOP）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Class | 「A class is a template / blueprint from which objects are created」⟦9618_w24_32:10(b)⟧ | 定义一类对象有哪些属性和方法的模板；定义一次，可以创建很多对象 | 饼干模具 | P3-FP-04 至 FP-06 |
| Object | 「An instantiation / instance of a class」⟦9618_s25_33:5⟧ | 按类创建出来的一个具体实体，有自己的属性值；创建时分配内存 | 一块饼干 | P3-FP-04 |
| Instance | 「an occurrence of an object」⟦9618_w22_31:11(a)⟧ | 由类创建的一个具体对象；创建它的过程叫实例化（instantiation） | “这一块”饼干 | P3-FP-04 |
| Property / attribute | 「the data items / attributes」⟦9618_s22_31:7(b)⟧ | 类中定义的数据项，每个有名字和数据类型 | 身份证上的各个栏目 | P3-FP-04、P3-FP-05 |
| Method | 「A programmed function / procedure / subroutine / subprogram defined as part of a class」⟦9618_s25_33:5⟧ | 类中定义的过程或函数，实现对象的行为、作用在属性上 | 对象会做的动作 | P3-FP-04、P3-FP-05 |
| Constructor | 「that is used to create instances / objects of this class」⟦9618_w24_32:10(a)⟧ | 创建对象并给属性设初值的方法；伪代码里叫 `NEW`，类图里常写 `Constructor()` | 新生儿登记 | P3-FP-05、P3-FP-06 |
| Getter | 「A method that accesses the value of a property」⟦9618_s25_33:5⟧ | 返回某个属性值的方法，通常不带参数 | 查看窗口 | P3-FP-04、P3-FP-05 |
| Setter | 「A method that changes the value of a property」⟦9618_s25_33:5⟧ | 更新某个属性值的方法，带一个参数（参数名与属性名不同） | 修改窗口 | P3-FP-04、P3-FP-05 |
| Encapsulation | 「putting properties and methods inside a class」⟦9618_w22_32:10(a)⟧ | 把属性和方法放进同一个类，并把属性隐藏起来，外部只能通过类的方法访问 | 药装进胶囊，只留一个口 | P3-FP-04 |
| PRIVATE | 「To ensure that attributes can only be accessed by the class’s own methods」⟦9618_s22_32:1(c)(ii)⟧ | 属性只能被本类自己的方法访问；是实现封装的手段，不是“对未授权用户保密” | 只有柜员能开的柜台 | P3-FP-04、P3-FP-06 |
| Inheritance | 「Inheritance is where a derived class takes properties / behaviours」⟦9618_s25_31:11(b)(ii)⟧ | 子类（派生类）获得父类（基类、超类）的全部属性和方法，还可以增加或重写；伪代码用 `INHERITS`、`SUPER` | 在“动物”模具上加花纹做成“猫”模具 | P3-FP-04、P3-FP-05 |
| Polymorphism | 「Polymorphism is when methods with the same name are redefined / behave differently」⟦9618_s25_32:12(b)(ii)⟧ | 同名方法在不同的子类中被重新定义，所以表现不同 | 同一句“叫一声”，猫喵狗汪 | P3-FP-04、P3-FP-05 |
| Containment (aggregation) | A class contains objects of another class as attributes (a "has-a" relationship).（非 MS 原句） | 一个类的属性里有另一个类的对象（或对象数组）；与继承（“是一种”）不同；考纲列出，语料尚未单独出题 | 班级“有”很多学生，学生不“是”班级 | P3-FP-04 |

### 声明式编程

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Fact | A clause that states something that is unconditionally true, e.g. person(carlos).（非 MS 原句） | 无条件成立的一句：谓词 + 小写常量参数 + 句点 | 名册上的一行登记 | P3-FP-07 |
| Rule | 「using facts and rules」⟦9618_s21_31:9(b)⟧ | 有条件成立的一句：规则头 IF 子目标 AND 子目标 AND NOT 子目标 | 入场条件清单 | P3-FP-09 |
| Goal (query) | 「using queries to satisfy goals」⟦9618_s21_31:9(b)⟧ | 向事实库提出的问题；系统找出使目标成立的所有变量值 | 向名册查询“谁符合条件” | P3-FP-08 |
| Variable vs constant | A name starting with a capital letter is a variable; a name starting with a lower-case letter is a constant.（非 MS 原句） | 大写开头是变量（等着被匹配）；小写开头是常量（具体的人或物） | `Carlos` 是空格子，`carlos` 是那个人 | P3-FP-07 至 FP-09 |

### 文件处理

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Text file | Lines of text read or written one after another as strings.（非 MS 原句，见指南 §9.1） | 一行一个字符串，按顺序读写；打开方式 `READ`、`WRITE`（新建，原内容丢失）、`APPEND`（加在末尾） | 一卷录音带 | P3-FP-10 |
| Random file | Records of fixed length that can be read or written at any position using a file pointer.（非 MS 原句，见指南 §9.2） | 由定长记录组成，可以把文件指针移到任一位置直接读写；打开方式 `RANDOM` | 编了号的储物柜 | P3-FP-10 |
| SEEK | 「SEEK "StoredResults.dat", Position」⟦9618_s25_32:13⟧ | 把文件指针移到给定位置；每次 `GETRECORD` / `PUTRECORD` 之前都要先 `SEEK` | 走到第几号柜子前 | P3-FP-10 |
| GETRECORD / PUTRECORD | 「PUTRECORD "StoredResults.dat", Grade」⟦9618_s25_32:13⟧ | `GETRECORD` 读出指针处的记录存进变量；`PUTRECORD` 把变量写进指针处，覆盖原来的记录 | 从柜子里拿出 / 放进去 | P3-FP-10 |
| EOF | 「UNTIL EOF(DentalFile)」⟦9618_s23_32:6(b)⟧ | 没有更多数据可读时返回 TRUE 的函数；用作读文件循环的结束条件 | 录音带放到头了 | P3-FP-10 |

### 异常

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Exception | 「An exception is an unplanned / unexpected event that occurs when a program is running」⟦9618_w25_33:12(a)⟧ | 程序运行时发生的意外事件，打断正常执行，可能使程序意外停止 | 路上桥断了 | P3-FP-11 |
| Exception handling | 「responding to an unexpected event when the program is running so it does not halt unexpectedly」⟦9618_w23_31:8(b)⟧ | 对异常作出响应的过程，使程序不会意外停止（如给出有意义的错误信息） | 事先备好的绕行方案 | P3-FP-11 |
| Causes of exceptions | 「Programming errors」⟦9618_w23_31:8(c)⟧；「User errors」⟦9618_w23_31:8(c)⟧；「Hardware failure」⟦9618_w23_31:8(c)⟧ | 编程错误（除以零、数组越界）、用户错误（数据类型或文件名输错）、硬件故障（硬盘损坏、打印机断开） | 车坏了、司机走错了、路塌了 | P3-FP-11 |
| Reasons for exception handling | 「To prevent a program halting unexpectedly」⟦9618_s22_32:9⟧ | 捕获运行时错误、防止程序意外停止、给出有意义的错误信息 | 出事时有人指挥，不是一哄而散 | P3-FP-11 |
