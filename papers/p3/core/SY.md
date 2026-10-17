## SY　系统软件：核心概念 {#core-SY}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义（核验语料里没有可直接引用的 MS 句子），作答时以所答那题的 MS 为准。

### 操作系统（16.1）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| User interface（hiding complexity） | 「The user interface hides the complexities of the computer hardware/operating system from the user」⟦9618_w23_31:7(a)⟧ | 用户通过界面（如 GUI 的图标、菜单）操作计算机，不需要了解或直接操作硬件 | 方向盘与踏板，藏起发动机 | P3-SY-01 |
| Device driver | 「Makes it easier to control peripherals such as printers within the operating system of the computer rather than on the separate device itself」⟦9618_w25_31:4(b)⟧ | 让 OS 能控制某种外设的软件，用户在 OS 里就能操作打印机等设备 | 不同插头的转换器 | P3-SY-01 |
| Process | A process is a program that is being executed, together with the resources and state the OS keeps for it.（非 MS 原句） | 正在执行的程序（连同 OS 为它保存的状态与资源） | 菜谱是程序，正在做的那道菜是进程 | P3-SY-02 |
| Multi-tasking | 「multi-tasking allows computers to carry out / seem to carry out more than one process at a time」⟦9618_w24_32:9(b)(i)⟧ | 多个进程看起来同时运行：处理器时间和资源在进程间共享、由调度决定谁运行 | 一个厨师轮流照看几口锅 | P3-SY-02 |
| Running state | 「CPU time has been allocated and the process is being executed」⟦9618_w25_32:5(b)⟧ | 进程已分到 CPU 时间，正在执行 | 手里拿着游戏手柄 | P3-SY-02 |
| Ready state | 「The process is waiting (in the ready queue) for a slice of CPU time. It could run」⟦9618_w25_32:5(b)⟧ | 进程能运行，正在 ready queue 里等 CPU 时间片 | 排队等手柄 | P3-SY-02 |
| Blocked state | 「The process is waiting for an I/O operation / some event to take place / be completed」⟦9618_w25_32:5(b)⟧ | 进程在等 I/O 或某事件完成，给它 CPU 也不能运行 | 去拿外卖了，轮到也玩不了 | P3-SY-02 |
| Scheduling | 「Process scheduling allows more than one program/task to appear to be executed at the same time」⟦9618_w22_32:9(a)⟧ | OS 决定哪个进程何时使用 CPU，使多任务可行、CPU 保持忙碌、进程公平获得 CPU | 食堂窗口的叫号规则 | P3-SY-03 |
| Round robin | 「Each process is served by the CPU for a fixed time/time slice」⟦9618_w22_32:9(b)⟧ | 按到达排队，每个进程轮流用固定时间片；用完保存状态回到队列；抢占式 | 每人限时 30 秒，没完回队尾 | P3-SY-03 |
| First come first served | 「No complex logic, each process request is queued as it is received and executed one by one」⟦9618_w22_32:9(b)⟧ | 按到达顺序一个接一个执行到底 | 普通排队 | P3-SY-03 |
| Shortest job first | 「The process with the shortest time to complete/burst time is selected first and executed」⟦9618_s25_32:5(b)⟧ | 选完成所需时间最短的进程先执行；开始后运行到结束或进入等待（非抢占） | 只买一瓶水的先结账 | P3-SY-03 |
| Shortest remaining time | 「When a process with a shorter burst time arrives the existing process is replaced by the shorter process」⟦9618_s25_31:8(b)⟧ | 选剩余时间最短的进程；更短的新进程到达会替下当前进程（抢占） | 结账中途来了更快的人，先让他 | P3-SY-03 |
| Starvation | 「The scheduler will continue to choose shorter processes over longer processes if they continue to be added to the queue can cause starvation for longer jobs」⟦9618_s25_32:5(b)⟧ | 某些进程一直得不到 CPU（如短作业不断加入时的长作业） | 永远轮不到的人 | P3-SY-03 |
| Kernel as interrupt handler | 「the kernel receives a signal when an interrupt is generated」⟦9618_w24_32:9(a)⟧ | 内核收到中断信号，比较优先级，查中断分派表，保存被中断进程的状态，处理后再恢复 | 值班经理按轻重缓急接电话 | P3-SY-03 |
| Interrupt dispatch table (IDT) | 「the kernel consults the interrupt dispatch table / IDT」⟦9618_w24_32:9(a)⟧ | 把每种中断映射到对应中断服务例程（ISR）的表 | 电话分机号码表 | P3-SY-03 |
| Low-level scheduling | 「The low-level scheduler manages the handling of interrupts based on priority」⟦9618_w25_32:5(a)⟧ | 低级调度程序按优先级处理中断，使紧急事件不被耽搁 | 急诊分诊 | P3-SY-03 |
| Virtual memory | 「Disk / secondary storage is used to extend the RAM / memory available」⟦9618_w22_31:8(a)⟧ | 用辅存扩展可用内存，数据按需在 RAM 与磁盘间换入换出 | 书桌放不下就放身后书架 | P3-SY-04 |
| Paging | 「Paging allows the memory to be divided into fixed size blocks and Segmentation divides the memory into variable sized blocks」⟦9618_w22_31:8(b)⟧ | 把内存按固定大小的块（页）划分，由 OS 划分 | 统一规格的储物格 | P3-SY-04 |
| Segmentation | 「the logical / virtual address space is broken into varying sized blocks called segments」⟦9618_w24_31:8(a)⟧ | 把逻辑地址空间按可变大小的段划分，每段有名字、大小和编号 | 按物品大小定做的柜子 | P3-SY-04 |
| Segment map table | 「A segment map table maps logical / virtual addresses to physical addresses / contains the segment number and offset」⟦9618_w24_31:8(a)⟧ | 用段号作下标，把逻辑地址（段号 + 偏移量）映射成物理地址的表 | 柜子编号对照表 | P3-SY-04 |
| Page replacement | When a page that is needed is not in RAM and RAM is full, the OS swaps a page out to disk (e.g. first in first out, least recently used) and loads the needed page.（非 MS 原句） | 缺页且内存已满时，选一页换出到磁盘，再调入需要的页 | 书桌满了，先把最久没看的书放回书架 | P3-SY-04 |
| Disk thrashing | 「Eventually, more time is spent swapping the pages/data than processing the data」⟦9618_w23_32:5(b)⟧ | 使用虚拟内存时页面换入换出过于频繁，磁头忙于换页，处理时间反而少于换页时间 | 一直转身拿书，没空读书 | P3-SY-04 |

### 翻译程序（16.2）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Interpreter（execution） | 「The interpreter translates the source code one line at a time」⟦9618_s25_31:6⟧ | 逐行翻译并立即执行，遇错停止报错，不保存可执行文件，每次运行都要重新翻译 | 同声传译 | P3-SY-05 |
| Lexical analysis | 「It takes modified source code and breaks it into a series of tokens」⟦9618_s25_32:8⟧ | 编译第一阶段：去空白注释，切成记号并分类，标识符入符号表 | 先把句子拆成单词并查字典 | P3-SY-06 |
| Token | 「To convert the high-level source code / program into a sequence of tokens」⟦9618_w25_31:8(a)⟧ | 源代码中有意义的最小单位（关键字、标识符、运算符、常数等） | 句子里的单词 | P3-SY-06 |
| Symbol table | 「Identifiers are stored in a symbol table」⟦9618_s25_32:8⟧ | 记录程序中标识符及其信息的表 | 人名通讯录 | P3-SY-06 |
| Syntax analysis | 「It checks that the tokens conform with the rules of the programming language」⟦9618_w22_32:2(b)⟧ | 编译第二阶段：按语言文法分析记号流，报告语法错误，产生语法树 | 检查单词排成的句子合不合语法 | P3-SY-06 |
| Parse tree | 「The output from this phase is a parse tree」⟦9618_s25_33:8⟧ | 语法分析产生的、表示语句结构的树 | 句子成分分析图 | P3-SY-06 |
| Code generation | 「Code generation」⟦9618_w22_32:2(a)⟧ | 把源代码的中间表示转换成可执行的目标代码 | 把提纲写成正文 | P3-SY-06 |
| Optimisation | 「To improve the code by making it use minimum resources (CPU, memory/storage, time)」⟦9618_w25_32:8(a)⟧ | 删冗余代码、化简表达式、调整顺序，使程序占用的存储、内存、时间最少 | 文章删去废话 | P3-SY-06 |
| Syntax diagram | A syntax diagram shows the grammar rules of a language graphically: boxes for components, arrows for order, branches for alternatives and loops for repetition.（非 MS 原句） | 用方框、箭头、分支、回环表示语法规则的图 | 单行道地图 | P3-SY-07、P3-SY-09 |
| Backus-Naur Form (BNF) | 「<passcode> ::= <uppercase><code>」⟦9618_s25_31:7(b)⟧ | 用 `::=`（定义为）、竖线（或）、`<非终结符>` 书写语法规则的记法；“一个或多个”用递归表示 | 语法规则的公式写法 | P3-SY-07、P3-SY-08 |
| Non-terminal / terminal | A non-terminal (written in angle brackets) is defined by another rule; a terminal is an actual character that appears in the string.（非 MS 原句） | 非终结符是还要继续展开的名字；终结符是真正出现在字符串里的字符 | 菜单上的“套餐”与具体的菜 | P3-SY-08 |
| Reverse Polish Notation (RPN) | 「Reverse Polish Notation provides an unambiguous method of representing an expression」⟦9618_s21_31:4(a)(i)⟧ | 运算符写在两个操作数之后的表达式写法；无括号、无优先级规则、从左到右一次读完 | 先报材料、后报做法 | P3-SY-10、P3-SY-11 |
| Evaluating RPN with a stack | 「Pop the last two elements from the stack and apply the operator」⟦9618_w23_31:9(b)⟧ | 从左到右读，数值入栈；遇运算符弹出两个值运算、结果入栈；最后栈中唯一的值是结果 | 叠盘子算账 | P3-SY-10、P3-SY-12 |
