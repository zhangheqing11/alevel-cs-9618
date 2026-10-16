## SS　系统软件：核心概念 {#core-SS}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Operating system (OS) | 「To hide the complexities of the hardware from the user」⟦9618_w23_12:8(a)⟧ | 管理硬件与软件资源、提供用户界面、为应用程序提供运行平台的系统软件 | 大楼物业：管水电、门禁、房间分配，住户不用懂管道 | P1-SS-01 |
| User interface | 「To provide a user interface」⟦9618_s25_11:6(b)⟧ | 用户与计算机交互的方式（图形界面、命令行等），由 OS 提供 | 遥控器 | P1-SS-01 |
| Memory management | 「Stores data from all currently running programs concurrently in RAM」⟦9618_s24_12:6⟧ | 把 RAM 分配给进程、回收，防止进程互相覆盖，管理虚拟内存 | 分案板 | P1-SS-01 |
| Process management | 「Switches between processes to allow them to share the use of the processor」⟦9618_s24_12:6⟧ | 调度进程、分配时间片与资源、在进程间切换以实现多任务 | 厨师轮流翻锅 | P1-SS-01 |
| File management | Organises files in a directory structure and controls how they are stored, named, accessed and shared.（非 MS 原句） | 建立目录结构、分配存储空间、规定命名、提供文件操作与访问控制 | 图书管理员 | P1-SS-01 |
| Hardware management | 「Installs device drivers」⟦9618_s23_11:3(a)⟧ | 安装驱动、与外设收发数据、管理缓冲区和设备中断 | 翻译加调度员 | P1-SS-01 |
| Security management | 「Prevents unauthorised access」⟦9618_w25_11:5(a)(ii)⟧ | 认证用户、设置访问权限、安全更新、日志与恢复 | 门卫 | P1-SS-01 |
| Multi-tasking | 「Stops the data from overwriting each other in RAM/primary storage」⟦9618_s24_12:6⟧ | 多个进程看起来同时运行：内存管理让它们同时驻留 RAM，进程管理让它们轮流使用处理器 | 一边听歌一边打字 | P1-SS-01 |
| Utility software | 「Perform housekeeping/maintenance tasks」⟦9618_s26_13:5(b)(i)⟧ | 帮助设置、分析、优化、维护计算机的系统软件 | 工具箱 | P1-SS-02 |
| Disk formatter | 「A new file system needs to be generated on the disk」⟦9618_w23_13:5(b)(ii)⟧ | 为磁盘初次使用做准备：建立文件系统与分配表、分区、清除数据 | 给新本子画格子 | P1-SS-02 |
| Defragmentation | 「Rearranges blocks of individual files (on the HDD) so they are contiguous」⟦9618_s23_11:3(c)⟧ | 把文件分散的块重排为连续块、集中空闲空间，减少读写头移动、加快访问 | 把散页按顺序装订回书里 | P1-SS-02 |
| Back-up software | 「To make a copy of data at regular intervals」⟦9618_s22_13:4(b)(i)⟧ | 定期自动为数据做副本，丢失或损坏后可恢复 | 存档 | P1-SS-02 |
| Disk repair / contents analysis | Checks a disk for errors, marks bad sectors and recovers corrupted data.（非 MS 原句） | 检查并修复磁盘不一致、标记坏扇区、恢复损坏文件 | 体检加手术 | P1-SS-02 |
| Program library | 「Set of pre-written / pre-compiled / pre-tested subroutines」⟦9618_s23_12:7(a)(i)⟧ | 一组预先写好、编译好、测试好的子程序，可导入并在其他程序中调用 | 现成的零件库 | P1-SS-03 |
| Library routine benefit | 「Code is already tested so it is more robust/likely to work」⟦9618_s22_11:5(c)⟧ | 省编程与测试时间、更可靠、能用自己写不出的复杂功能 | 买现成的轮子而不是自己造 | P1-SS-03 |
| Dynamic Link Library (DLL) | 「the executable file size of the program using the DLL will be smaller」⟦9618_s23_12:7(a)(ii)⟧ | 运行时才链接、可被多个程序共用、可独立更新的库文件 | 报告里写“见图书馆某书”，而不是把整本书复印进去 | P1-SS-03 |
| Language translator | 「To convert a high-level language to a low-level language/assembly/machine code」⟦9618_s26_11:2(a)⟧ | 把高级语言或汇编语言转换成机器码的程序：编译器、解释器、汇编器 | 翻译 | P1-SS-04 |
| Compiler | 「Attempts to translate the whole source code」⟦9618_s22_12:6(a)⟧ | 整体翻译源代码，结束时一次报告全部错误，无错时生成可执行文件 | 笔译：整本译完交译本 | P1-SS-04、P1-SS-05 |
| Interpreter | 「Reads each line then translates it and executes it」⟦9618_s22_12:6(b)⟧ | 逐行翻译并立即执行，遇错即停，不生成可执行文件 | 同声传译 | P1-SS-04、P1-SS-05 |
| Assembler | Translates assembly language into machine code.（非 MS 原句） | 把汇编语言翻译成机器码的翻译程序 | 助记符字典 | P1-SS-04、P1-PF-07 |
| Executable file | 「to create an executable file so source code not seen」⟦9618_w25_12:10(a)⟧ | 编译生成的可直接运行的机器码文件，运行时不需要源代码和翻译程序 | 成品菜，不附菜谱 | P1-SS-04、P1-SS-05 |
| Real-time debugging | 「Programmer can debug in real time」⟦9618_s23_13:5(a)(i)⟧ | 解释器遇错即停，改正后立即看到效果并从该处继续 | 边唱边纠音 | P1-SS-05 |
| Dependent errors | Errors reported only because of an earlier error; an interpreter shows one error at a time so they do not appear.（非 MS 原句） | 由前一个错误引出的连带“假错误”；编译器一次报全部错误时容易出现 | 第一张多米诺倒了，后面全跟着倒 | P1-SS-05 |
| Partially compiled, partially interpreted | 「partially compiled programs can be used on different platforms as they are interpreted when run」⟦9618_w22_12:1(b)(ii)⟧ | 先编译成中间代码（如字节码），运行时在各平台上解释，兼顾跨平台与效率 | 通用乐谱，各乐器现场演奏 | P1-SS-06 |
| Integrated Development Environment (IDE) | Software that provides the tools for writing, translating, testing and debugging programs in one place.（非 MS 原句） | 把编辑器、翻译程序、调试工具集成在一起的软件 | 一站式工作台 | P1-SS-07 |
| Context-sensitive prompts | 「Suggest the code to add // automatically complete statements」⟦9618_s23_12:7(c)⟧ | 输入时提示可用代码、自动补全 | 输入法联想 | P1-SS-07 |
| Dynamic syntax checks | 「Highlight / underline / colour syntax errors as the code is entered」⟦9618_s23_12:7(c)⟧ | 输入时即时标出语法错误 | 拼写检查的红波浪线 | P1-SS-07 |
| Prettyprint | Displays source code with keywords coloured and formatted so it is easier to read.（非 MS 原句） | 给关键字等上色、排版，提高可读性 | 彩色高亮 | P1-SS-07 |
| Expand / collapse code blocks | 「Expanding and collapsing code blocks」⟦9618_w25_11:5(c)⟧ | 展开查看块内代码，或折叠暂不处理的块 | 文件夹开合 | P1-SS-07 |
| Single stepping | 「Run the code one line at a time so the values can be checked」⟦9618_s23_12:7(c)⟧ | 一次执行一行，观察每行效果 | 逐帧播放 | P1-SS-07 |
| Breakpoint | 「Stop the code at a specific line to check the current progress / values」⟦9618_s23_12:7(c)⟧ | 程序运行到设定行时停下，检查此时状态 | 暂停在某一帧 | P1-SS-07 |
| Report window / variable watch | 「shows the values in variables/data structures and how they change when each line is run」⟦9618_w24_11:4(d)(ii)⟧ | 显示变量与数据结构的值及其变化 | 实时计分板 | P1-SS-07 |
