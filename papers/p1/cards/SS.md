## SS　系统软件 {#ch-SS}

<!-- auto:chapter-stats -->

### 核心思想

这一章讲**站在硬件和应用程序之间的那层软件**，分两半：

1. **让计算机能用、好用**（SS-01 至 SS-03）：操作系统管理内存、文件、进程、硬件、安全，替用户挡住硬件的复杂性（SS-01）；实用软件做维护和优化——格式化、杀毒、碎片整理、备份、磁盘修复（SS-02）；程序库让程序员直接调用别人写好、测好的例程，DLL 更进一步在运行时才链接（SS-03）。
2. **让程序员写的代码能跑起来**（SS-04 至 SS-07）：翻译程序把高级语言变成机器码，编译器整体翻译、解释器逐行翻译执行（SS-04）；两者各有长处，开发时用解释器、发布时用编译器（SS-05）；有的语言折中，先编译成中间代码、再解释（SS-06）；程序员在 IDE 里完成编写、排版、调试（SS-07）。

这一章几乎全是“说出名称 + 说明作用/理由”的文字题。MS 的结构高度固定：**“benefit / feature 1 分 + expansion 1 分”成对给分**。所以每一点都要写成“是什么 → 所以/因为什么”两截，单写一个名词通常只拿一半。

### 题型树
<!-- auto:type-tree -->

### P1-SS-01　操作系统的作用与管理任务　{#P1-SS-01}

<!-- auto:stats P1-SS-01 -->

**考法**　①操作系统的目的（1–5 分）；②说出 OS 的关键管理任务（常给一个，要“另外两个/三个”）；③描述某一项管理任务具体做什么（内存、进程、文件、硬件、安全）；④解释内存管理与进程管理怎样支持多任务；⑤连线：管理任务 ↔ 描述。

**识别信号**　Operating System (OS)；Describe the purpose of an OS；key management tasks；memory / file / process / security / hardware management；support multi-tasking。

**解题思路**
1. **目的**三条主线：提供用户界面（让用户能与硬件交互）；隐藏硬件的复杂性；管理资源（内存、文件、进程、输入输出），为应用软件提供运行平台。
2. **五项管理任务**（名称要写全：“… management”）及各自做什么：

| 任务 | 做什么 |
|:--|:--|
| Memory management | 把 RAM 分块、动态分配给进程，进程结束后回收；防止两个进程占用同一块内存；管理虚拟内存/分页，需要时从辅存调入 |
| Process management | 调度：决定下一个运行哪个进程；分配时间片，在进程间切换（多任务）；分配进程所需资源；处理中断与优先级；解决冲突、允许进程间交换数据 |
| File management | 建立目录结构；命名规则；分配辅存空间给文件；提供打开、关闭、删除、复制等操作；控制访问权限；搜索 |
| Hardware (peripheral) management | 安装/加载设备驱动程序，使外设与计算机能通信；向输出设备发送、从输入设备接收数据；管理缓冲区；处理来自设备的中断 |
| Security management | 认证用户、防止未授权访问；设置访问权限；安全更新；数据恢复；记录活动日志 |

3. **多任务**题分两边写：内存管理——让所有正在运行的程序的数据同时放在 RAM 中、互不覆盖；进程管理——暂停一个进程、运行另一个，决定下一个运行谁，轮流共享处理器。
4. 描述题每个任务写“名称 + 一个具体动作”，⟦9618_s22_13:4(a)⟧ 写明只列名称最多得 2 分。

**得分表述**（引自对应 MS）
- 「To hide the complexities of the hardware from the user」⟦9618_w23_12:8(a)⟧
- 「To provide a user interface」⟦9618_s25_11:6(b)⟧
- 「Stores data from all currently running programs concurrently in RAM」⟦9618_s24_12:6⟧
- 「Stops the data from overwriting each other in RAM/primary storage」⟦9618_s24_12:6⟧
- 「Switches between processes to allow them to share the use of the processor」⟦9618_s24_12:6⟧
- 「Installs device drivers」⟦9618_s23_11:3(a)⟧

**易错与失分**
- 已给的任务（如 hardware management）又写一遍：题目要的是 “other”。
- 写成实用软件的活（“defragments the disk”“scans for viruses”）：那是 SS-02。
- 进程管理只写“manages processes”：要写出调度、时间片、切换、资源分配等具体动作。
- 中断的检测与处理细节属于 PF-04；在 OS 题里只需写“handles interrupts”。

#### 代表题精讲　⟦9618_s24_12:6⟧

**在考什么**　Explain how memory management and process management support multi-tasking. 4 分，每一项最多 3 分——两边都要写。

**完整作答**
- 内存管理：把当前所有正在运行的程序的数据同时存放在 RAM 中；阻止这些数据在 RAM 中互相覆盖；决定哪些进程应该放在主存里。
- 进程管理：允许一个进程暂停、另一个进程执行；决定下一个运行哪个进程（调度）；在进程之间切换，让它们轮流使用处理器。

**与 MS 对齐**　内存管理 ←“Stores data from all currently running programs concurrently in RAM”“Stops the data from overwriting each other in RAM/primary storage”“Decides which processes should be in main memory”；进程管理 ←“Allows one process to be paused whilst another process can be actioned”“Decides which process is to be run next”“Switches between processes to allow them to share the use of the processor”。各写两点即可拿满 4 分，各写三点更稳。

**英文作答句**　Memory management stores data from all currently running programs concurrently in RAM and stops the data from overwriting each other. Process management allows one process to be paused whilst another process is actioned, decides which process is to be run next, and switches between processes so that they share the use of the processor.

**直观**　多任务像一个厨师同时做几道菜：内存管理是给每道菜分一块案板、不让它们混在一起；进程管理是决定此刻翻哪个锅、几秒后换下一个。

**下一道变式**　⟦9618_s23_11:3(a)⟧　（换成硬件管理：描述 OS 怎样管理外设，4 分。）

<!-- auto:drills P1-SS-01 -->

### P1-SS-02　实用软件　{#P1-SS-02}

<!-- auto:stats P1-SS-02 -->

**考法**　①实用软件的目的；②某个实用程序（磁盘格式化、碎片整理、备份、病毒检查、磁盘修复/内容分析、文件压缩）的作用或必要性；③碎片整理怎样提高性能（3 分常见）；④连线：实用程序 ↔ 用途；⑤情境：给出问题（图片损坏、新硬盘），选合适的实用程序；⑥举一个“不是为了提高安全”的实用程序并解释为何需要。

**识别信号**　utility software；defragmentation；disk formatter；virus checker；back-up software；disk repair / disk contents analysis；compression。

**解题思路**
1. **目的**：执行维护/“打扫”任务，帮助用户设置、分析、优化、维护计算机，提高整体性能。
2. 每个实用程序背“做什么 → 为什么”：

| 实用程序 | 做什么 | 为什么需要 / 好处 |
|:--|:--|:--|
| Disk formatter | 为初次使用准备磁盘：建立文件系统、设置文件分配表、分区、命名卷、清除全部数据 | 新磁盘不格式化就不能存文件 |
| Defragmentation | 把同一文件分散的块重新排成连续的块，把空闲空间集中 | 读写头移动更少 → 访问文件更快 |
| Back-up | 定期（自动）为数据做副本 | 数据丢失/损坏时可以恢复；用户不必记着备份 |
| Virus checker | 扫描恶意程序代码，隔离/删除 | 防止数据被破坏或窃取 |
| Disk repair / contents analysis | 检查并修复磁盘不一致，标记坏扇区，恢复损坏文件 | 找回因硬件故障丢失的数据 |
| File compression | 减小文件大小 | 省存储空间、缩短传输时间 |

3. 碎片整理三连：文件长期增删后被拆散存放 → 整理后连续 → 读写头不用在多处来回找 → 访问更快。

**得分表述**（引自对应 MS）
- 「Perform housekeeping/maintenance tasks」⟦9618_s26_13:5(b)(i)⟧
- 「Rearranges blocks of individual files (on the HDD) so they are contiguous」⟦9618_s23_11:3(c)⟧
- 「so less head movement is needed」⟦9618_s23_11:3(c)⟧
- 「To make a copy of data at regular intervals」⟦9618_s22_13:4(b)(i)⟧
- 「So that if it is lost/corrupted it can be retrieved」⟦9618_s22_13:4(b)(i)⟧
- 「A new file system needs to be generated on the disk」⟦9618_w23_13:5(b)(ii)⟧

**易错与失分**
- 碎片整理写成“deletes unwanted files / frees up space”：它不删文件、不增加空间，只是重新排列。
- 碎片整理说“makes the computer faster”而不说机制：要写连续存放、读写头移动少。
- 备份写成“stores data”：要写“副本”“定期”“丢失后可恢复”。
- “不是为了安全”的实用程序选了病毒检查：⟦9618_w23_12:8(b)⟧ 排除的正是安全类。
- 碎片整理用在固态硬盘上没有意义（没有读写头）；题目情境是 SSD 时别选它。

#### 代表题精讲　⟦9618_s22_13:4(b)(i)⟧

**在考什么**　Describe the purpose of back-up software and defragmentation software. 4 分，每个最多 2 分。

**完整作答**
- 备份软件：定期为数据做副本，这样当数据丢失或损坏时可以找回。
- 碎片整理软件：让单个文件占据连续的块（并把空闲空间集中在一起），从而缩短磁盘访问时间、文件加载更快。

**与 MS 对齐**　Back-up ←“To make a copy of data at regular intervals”+“So that if it is lost/corrupted it can be retrieved”；Defragmentation ←“Make individual files occupy contiguous blocks // move free space together”+“Improve disk access times // Data/files can be loaded faster”。

**英文作答句**　Back-up software makes a copy of data at regular intervals, so that if the data is lost or corrupted it can be retrieved. Defragmentation software makes individual files occupy contiguous blocks, which improves disk access times so files can be loaded faster.

**直观**　碎片化的磁盘像一本书被拆成散页塞在书架各处，读一本要满屋跑；整理后每本书的页按顺序放在一起，一伸手就拿完。

**下一道变式**　⟦9618_w23_12:8(b)⟧　（自己挑一个不是为安全服务的实用程序，名称 1 分 + 解释 2 分。）

<!-- auto:drills P1-SS-02 -->

### P1-SS-03　程序库与 DLL　{#P1-SS-03}

<!-- auto:stats P1-SS-03 -->

**考法**　①定义程序库；②使用程序库/库例程的好处（2–3 分，最常见）；③使用库例程的一个缺点；④团队创建程序库的好处；⑤使用 DLL（相对普通库）的好处（2–4 分，常“好处 + 展开”成对给分）。

**识别信号**　program library；library routines / library files；Define the term program library；Dynamic Link Library (DLL)；benefits / drawback of using library routines。

**解题思路**
1. **定义**：一组预先写好、编译好、测试好的子程序（例程），可以通过导入在其他程序中调用。
2. **好处**（每点“好处 + 因为”）：
   - 节省编程时间——代码不必从零写；
   - 节省测试时间、更可靠——例程已测试过、有文档；
   - 能用自己写不出来的复杂例程；
   - 库更新后程序自动受益；源代码更短更易读；
   - 团队里可以共享、复用，发挥各自专长。
3. **缺点**：可能与当前程序不兼容；未必经过充分测试（可能有 bug/病毒）；不完全符合需求，需要修改再测试；别人改了库，结果可能出乎意料。
4. **DLL 的好处**（与“静态”库对比，成对写）：
   - 可执行文件更小——可执行文件里不包含（全部）库例程，运行时才链接；
   - 内存需求更少——DLL 只在需要时装入一次，多个程序可共用同一个 DLL；
   - 维护不用程序员做——DLL 与程序分开，由库作者维护；
   - DLL 改了不必重新编译主程序——DLL 可独立更新，所有用它的程序都受益。

**得分表述**（引自对应 MS）
- 「Set of pre-written / pre-compiled / pre-tested subroutines」⟦9618_s23_12:7(a)(i)⟧
- 「Programming time is saved as code does not have to written from scratch」⟦9618_w25_13:8(b)⟧
- 「Code is already tested so it is more robust/likely to work」⟦9618_s22_11:5(c)⟧
- 「(main) memory requirements for program is reduced」⟦9618_s23_12:7(a)(ii)⟧
- 「the executable file size of the program using the DLL will be smaller」⟦9618_s23_12:7(a)(ii)⟧
- 「no need to recompile the main program when changes are made to DLL」⟦9618_s23_12:7(a)(ii)⟧

**易错与失分**
- 程序库的好处与 DLL 的好处混用：问 DLL “instead of” 普通库时，“节省编程时间”不是 DLL 独有的，不得分；要写可执行文件小、内存省、独立更新。
- 只写好处不写展开：“Mark in pairs”时第二分来自 “because …”。
- 定义里漏掉“pre-written / pre-tested”：只说“a collection of code”太泛。

#### 代表题精讲　⟦9618_s23_12:7(a)(ii)⟧

**在考什么**　开发者为团队写一个新程序库。Explain two benefits to the developer of choosing to create a Dynamic Link Library (DLL). 4 分：每个好处 1 分 + 对应展开 1 分。

**完整作答**
1. 使用 DLL 的程序，其可执行文件更小——因为可执行文件不包含（全部）库例程，例程在运行时才链接。
2. 修改 DLL 后不需要重新编译主程序——因为对 DLL 代码的改进、纠错是独立于主程序完成的。
（还可写：主存需求减少，因为 DLL 只在需要时装入一次；一个 DLL 可供多个应用程序共用，节省内存。）

**与 MS 对齐**　“the executable file size of the program using the DLL will be smaller”+“... because the executable does not contain (all) the library routines”；“no need to recompile the main program when changes are made to DLL”+“... because changes / improvements/ error correction to the DLL file code are done independently of the main program”。

**英文作答句**　The executable file size of the program using the DLL will be smaller, because the executable does not contain all the library routines. There is no need to recompile the main program when changes are made to the DLL, because changes to the DLL code are done independently of the main program.

**直观**　普通库像把整本参考书复印进你的报告；DLL 像在报告里写“见图书馆某书第几页”——报告薄了，书更新了你的报告自动引用新版。

**下一道变式**　⟦9618_w25_11:5(b)(ii)⟧　（反面：使用库例程的一个缺点，“缺点 + 展开”。）

<!-- auto:drills P1-SS-03 -->

### P1-SS-04　翻译程序及其工作方式　{#P1-SS-04}

<!-- auto:stats P1-SS-04 -->

**考法**　①为什么需要翻译程序；②描述编译器 / 解释器的工作方式（各 2 分）；③填空完成对编译器与解释器的描述；④说出另一种翻译程序（汇编器）。

**识别信号**　language translators；Explain why language translators are needed；Describe the operation of a compiler / an interpreter；Complete the description of compilers and interpreters；Identify one other type of translator。

**解题思路**
1. **为什么需要**：计算机只能执行机器码，程序员用高级语言写程序 → 需要把高级语言（或汇编语言）转换成机器码。
2. **三种翻译程序**：编译器、解释器（高级语言 → 机器码）；汇编器（汇编语言 → 机器码）。
3. **编译器**：先检查/翻译**整个**源代码；在翻译结束时生成一份错误报告，**一次列出全部错误**；没有错误时生成**可执行文件**，运行它不再需要源代码和编译器。
4. **解释器**：读一行 → 翻译这一行 → 立即执行，再读下一行；遇到错误就**停下**并显示该错误；程序员可以**立刻**改正，从出错处继续；不生成可执行文件，每次运行都要重新解释。

**得分表述**（引自对应 MS）
- 「To convert a high-level language to a low-level language/assembly/machine code」⟦9618_s26_11:2(a)⟧
- 「Attempts to translate the whole source code」⟦9618_s22_12:6(a)⟧
- 「Creates a separate error report at the end of the translation process」⟦9618_s22_12:6(a)⟧
- 「If translation successful / no errors creates an executable file」⟦9618_s22_12:6(a)⟧
- 「Reads each line then translates it and executes it」⟦9618_s22_12:6(b)⟧
- 「Stops when an error is encountered」⟦9618_s22_12:6(b)⟧

**易错与失分**
- 说“编译器执行程序”：编译器只翻译、生成可执行文件；执行的是可执行文件。
- 说“解释器生成目标码文件”：解释器边翻译边执行，不留下可执行文件。
- “另一种翻译程序”写 IDE、链接器：答案是 assembler。
- 填空题按句子意思填词：⟦9618_s25_13:3(a)⟧ 四空是 executable file、source code、stops、immediately / in real-time。

#### 代表题精讲　⟦9618_s25_13:3(a)⟧

**在考什么**　Complete the description of compilers and interpreters by writing the missing words. 4 空，每空 1 分。

**完整作答**　A compiler checks all the code before attempting to translate the program. If any errors are found, they are all reported at the same time and the program does not translate or run. If there are no errors found, the compiler produces **an executable file** which can run without access to the **source code**. An interpreter translates one line of code and then runs it, before moving to the next line of code. If the line of code has an error, the interpreter **stops** and displays the error. The programmer can correct the error **immediately / in real-time** and then the interpreter continues translating from that point.

**与 MS 对齐**　MS 四空：“an executable file/.exe”“source/program code”“stops”“immediately/in real-time”。

**英文作答句**　（见上段粗体词。）

**直观**　编译器像笔译：整本书译完交一个译本，读者以后只看译本；解释器像同声传译：说一句译一句，说错了当场停下纠正，但每次开会都要再请一次翻译。

**下一道变式**　⟦9618_s22_12:6(a)⟧　（不给填空，自己描述编译器的工作方式，2 分。）

<!-- auto:drills P1-SS-04 -->

### P1-SS-05　编译器与解释器：优缺点与选择　{#P1-SS-05}

<!-- auto:stats P1-SS-05 -->

**考法**　①开发阶段用解释器的理由/好处；②开发阶段用编译器的缺点；③程序完成后用编译器的理由（可执行文件）；④在某阶段选解释器还是编译器并论证（选择本身不给分）；⑤解释怎样先用解释器、再用编译器。

**识别信号**　benefits / advantages of using an interpreter instead of a compiler；drawbacks of using a compiler compared to an interpreter during program development；Explain the reasons why the programmer uses a compiler when the program has been written；Identify whether an interpreter or a compiler would be more appropriate … Justify your choice；first use an interpreter and then a compiler。

**解题思路**
1. **开发阶段 → 解释器**（每点“好处 + 因为”）：
   - 实时调试：遇错即停，错误位置清楚，改了马上能看到效果，并能从出错处继续；
   - 一次只报一个错误，没有连带的“假错误”（dependent errors）；
   - 程序没写完也能测试其中一部分。
2. **开发阶段用编译器的缺点**（解释器好处的反面）：大量源代码编译耗时；每次改动都要重新编译；有错误就无法运行；不能实时改错；一个错误可能引出多个假错误；难以测试未完成的代码。
3. **完成后 → 编译器**：
   - 生成可执行文件 → 发布时不给源代码，别人不能查看/修改/盗用；
   - 用户运行时不需要翻译程序，也不必每次重新翻译；
   - 可执行文件可以反复测试而无需重新翻译。
4. **先解释后编译**题分两栏写：解释器——写代码时用来测试/调试未完成的程序，因为可以实时改错；编译器——程序完成后用来生成可执行文件，不暴露源代码、可反复测试。

**得分表述**（引自对应 MS）
- 「Use an interpreter while writing/coding the program」⟦9618_w25_12:10(a)⟧
- 「to test / debug the partially completed program」⟦9618_w25_12:10(a)⟧
- 「Use the compiler after the program is complete」⟦9618_w25_12:10(a)⟧
- 「to create an executable file so source code not seen」⟦9618_w25_12:10(a)⟧
- 「Programmer can debug in real time」⟦9618_s23_13:5(a)(i)⟧
- 「Users do not require the translator to run the program」⟦9618_s24_11:3(b)⟧

**易错与失分**
- 写“interpreters are faster”：解释后的程序**运行**更慢；解释器的优势在调试，不在速度。
- 选择题只写选择不写理由：⟦9618_s23_12:7(b)⟧ 明写“No mark for choice”。
- 论证写成两种翻译程序的定义：要写“对这个阶段/这个人有什么用”。
- 完成后用编译器的理由写“to find errors”：发布阶段的核心是可执行文件、保护源代码、用户不需要翻译程序。

#### 代表题精讲　⟦9618_w25_12:10(a)⟧

**在考什么**　Explain how the programmer can first use an interpreter and then a compiler to develop the computer program. 4 分，每栏最多 2 分。

**完整作答**
- 解释器：在编写程序的过程中使用解释器，用来测试和调试尚未完成的程序；因为出错时可以当场改正、从停下的地方继续执行。
- 编译器：程序完成后使用编译器，生成可执行文件，这样别人看不到源代码；也可以用它对完成的部分反复测试，而不必每次重新解释。

**与 MS 对齐**　Interpreter ←“Use an interpreter while writing/coding the program”“… to test / debug the partially completed program”“… because errors can be corrected and processing continue from where the execution stopped”；Compiler ←“Use the compiler after the program is complete”“… to create an executable file so source code not seen”“Use the compiler to repeatedly test the same completed section without having to re-interpret every time”。

**英文作答句**　Interpreter: use an interpreter while writing the program to test and debug the partially completed program, because errors can be corrected in real time and processing can continue from where the execution stopped. Compiler: use the compiler after the program is complete to create an executable file, so the source code is not seen.

**下一道变式**　⟦9618_s23_12:7(b)⟧　（团队开发中途：选解释器还是编译器并论证；选择本身不给分。）

<!-- auto:drills P1-SS-05 -->

### P1-SS-06　部分编译、部分解释　{#P1-SS-06}

<!-- auto:stats P1-SS-06 -->

**考法**　解释为什么有些高级语言（如 Java）先部分编译、再部分解释。1–2 分，题目很短，答案点几乎固定。

**识别信号**　partially compiled and partially interpreted。

**解题思路**
1. 过程：源代码先被**编译**成中间代码（如 Java 的字节码 bytecode）；运行时，各平台上的虚拟机再把中间代码**解释**（或即时编译）成该机器的机器码。
2. 理由三条，记住 MS 的原句：
   - 跨平台：同一份中间代码在不同平台上运行时再解释；
   - 针对 CPU 优化：机器码在运行时才生成；
   - 运行更高效：源代码不必重新编译（比纯解释快）。

**得分表述**（引自对应 MS）
- 「partially compiled programs can be used on different platforms as they are interpreted when run」⟦9618_w22_12:1(b)(ii)⟧
- 「code is optimised for the CPU as machine code is generated at run time」⟦9618_w22_12:1(b)(ii)⟧
- 「Source code does not need recompiling so more efficient to run」⟦9618_w23_11:6(b)⟧

**易错与失分**
- 只写“to get the advantages of both”：没有说出具体好处，不给分。
- 跨平台的理由要带“因为运行时才解释”，只写“portable”太短。

#### 代表题精讲　⟦9618_w22_12:1(b)(ii)⟧

**在考什么**　Explain why high-level language programs might be partially compiled and partially interpreted. 2 分。

**完整作答**　部分编译得到的中间代码可以在不同平台上使用，因为它在运行时才被（该平台的）解释器解释；而且机器码是在运行时生成的，因此代码能针对所运行的 CPU 进行优化。

**与 MS 对齐**　“partially compiled programs can be used on different platforms as they are interpreted when run”+“code is optimised for the CPU as machine code is generated at run time”。

**英文作答句**　Partially compiled programs can be used on different platforms as they are interpreted when run. The code is optimised for the CPU as machine code is generated at run time.

**直观**　像出版一本“通用乐谱”（中间代码）：不管拿到的是钢琴还是吉他（不同平台），演奏者现场按自己的乐器演奏（运行时解释）。

**下一道变式**　⟦9618_w23_11:6(b)⟧　（同一问题的 1 分版本，写出一条理由即可。）

<!-- auto:drills P1-SS-06 -->

### P1-SS-07　集成开发环境 IDE　{#P1-SS-07}

<!-- auto:stats P1-SS-07 -->

**考法**　①描述给定的 IDE 功能（断点、动态语法检查、上下文提示、单步执行……）；②说出两个“呈现”功能或两个“调试”功能；③已给一个功能，再说出并描述另一个；④按“编码 / 呈现 / 调试”三类各举一个功能并描述（6 分）；⑤说明程序员在编写和测试时怎样使用 IDE；⑥连线：功能 ↔ 描述。

**识别信号**　Integrated Development Environment (IDE)；context-sensitive prompts；dynamic syntax checks；prettyprint；expand and collapse code blocks；single stepping；breakpoints；report window / variable watch。

**解题思路**
1. 按三类记功能，每个功能配一句“做什么 → 有什么用”：

| 类 | 功能 | 描述 |
|:--|:--|:--|
| 编码 coding | Context-sensitive prompts / auto-complete | 输入时提示可用的代码、自动补全语句 |
| 初步查错 | Dynamic syntax checks | 输入时就高亮/下划线标出语法错误 |
| 呈现 presentation | Prettyprint | 给关键字等上色，便于阅读和发现错误 |
| | Expand / collapse code blocks | 展开看块内内容，或折叠暂不处理的代码 |
| | Auto-indentation / formatting | 输入时自动缩进，结构清楚 |
| 调试 debugging | Single stepping | 一次执行一行，查看每行的效果、变量值、程序流程 |
| | Breakpoints | 在设定的行停下，检查此时的变量值与进度 |
| | Report window / variable watch | 显示变量和数据结构的值及其在运行中的变化 |

2. “怎样使用调试功能”题按“名称 + 怎么用 + 看什么”三截写，如“设置断点 → 运行到该行停下 → 检查变量内容”。
3. 题目已给的功能、翻译程序（compiler/interpreter）不算答案。

**得分表述**（引自对应 MS）
- 「Stop the code at a specific line to check the current progress / values」⟦9618_s23_12:7(c)⟧
- 「Highlight / underline / colour syntax errors as the code is entered」⟦9618_s23_12:7(c)⟧
- 「Suggest the code to add // automatically complete statements」⟦9618_s23_12:7(c)⟧
- 「Run the code one line at a time so the values can be checked」⟦9618_s23_12:7(c)⟧
- 「Expanding and collapsing code blocks」⟦9618_w25_11:5(c)⟧
- 「shows the values in variables/data structures and how they change when each line is run」⟦9618_w24_11:4(d)(ii)⟧

**易错与失分**
- 呈现与调试混淆：prettyprint、折叠、缩进是**呈现**；单步、断点、报告窗口是**调试**。
- 单步与断点混淆：单步是“一次一行”，断点是“跑到某一行停”。
- 动态语法检查写成“finds all errors”：它只在输入时标出**语法**错误，逻辑错误要靠调试工具。
- 描述只重复名字（“breakpoints are points where it breaks”）：要写停下来**检查什么**。

#### 代表题精讲　⟦9618_s23_12:7(c)⟧

**在考什么**　Complete the table by describing the typical features found in an IDE：Breakpoints、Dynamic syntax checks、Context-sensitive prompts、Single stepping。4 分，每个 1 分。

**完整作答**

| Feature | Description |
|:--|:--|
| Breakpoints | 让代码在指定的行停下，以检查当前的进度/变量值 |
| Dynamic syntax checks | 在输入代码的同时高亮、下划线或上色标出语法错误 |
| Context-sensitive prompts | 提示接下来可加的代码，自动补全语句 |
| Single stepping | 一次运行一行代码，以便检查各个值 |

**与 MS 对齐**　四格依次对应 MS：“Stop the code at a specific line to check the current progress / values”“Highlight / underline / colour syntax errors as the code is entered”“Suggest the code to add // automatically complete statements”“Run the code one line at a time so the values can be checked”。

**英文作答句**　Breakpoints: stop the code at a specific line to check the current progress and values. Dynamic syntax checks: highlight or underline syntax errors as the code is entered. Context-sensitive prompts: suggest the code to add and automatically complete statements. Single stepping: run the code one line at a time so the values can be checked.

**直观**　断点像录像的“暂停在某一帧”，单步像“一帧一帧往前按”，报告窗口是旁边实时显示的计分板。

**下一道变式**　⟦9618_s24_12:8(b)⟧　（编码、呈现、调试三类各举一个不同功能并描述，6 分。）

<!-- auto:drills P1-SS-07 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| SS-01 vs SS-02 | OS 自身的管理任务（内存、进程、文件、硬件、安全）→ SS-01；额外的维护工具（格式化、碎片整理、备份……）→ SS-02 | management 还是 utility |
| SS-02 vs SP-03 | 病毒检查作为实用软件的作用 → SS-02；作为防范某种威胁的安全措施 → SP-03 | 情境是“维护计算机”还是“保护数据免受威胁” |
| SS-01 vs PF-04 | OS 任务里提一句“handles interrupts” → SS-01；中断何时检测、怎样处理 → PF-04 | 有没有 F-E cycle / ISR / priority |
| SS-03 程序库 vs DLL | 用库的好处（省时间、已测试）→ 普通库；DLL 独有的好处（可执行文件小、内存省、独立更新不必重编译）| 题目有没有 “DLL instead of …” |
| SS-04 vs SS-05 | 只描述编译器/解释器怎样工作 → SS-04；比较优缺点、结合阶段选择 → SS-05 | describe the operation 还是 benefits / drawbacks / justify |
| SS-05 vs SS-06 | 纯编译与纯解释的比较 → SS-05；先编译成中间代码再解释 → SS-06 | partially compiled and partially interpreted |
| SS-04 vs PF-07 | 为什么需要翻译程序、汇编器是一种翻译程序 → SS-04；两遍汇编每一遍做什么 → PF-07 | first pass / second pass / symbol table |
| 单步执行 vs 断点 | 一次一行 / 运行到设定行停下 | one line at a time 还是 at a set line |
| 编译器错误报告 vs 解释器错误报告 | 翻译结束时一次报告全部错误 / 遇到第一个错误就停下 | 题目问调试方便与否 |
