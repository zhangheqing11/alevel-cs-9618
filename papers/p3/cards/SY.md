## SY　系统软件 {#ch-SY}

<!-- auto:chapter-stats -->

### 核心思想

这一章是 P1「系统软件」（P1-SS）的 A2 加深版，分两半：

| 半边 | 回答的问题 | 题型 |
|:--|:--|:--|
| **操作系统（16.1）** | OS 怎样让多个程序“同时”跑、怎样分 CPU、怎样分内存 | SY-01 ～ SY-04 |
| **翻译程序（16.2）** | 源程序怎样被翻译执行；语言的语法怎样精确写下来；表达式怎样不靠括号求值 | SY-05 ～ SY-12 |

操作系统这半边是一条链，按顺序学：

1. **隐藏复杂性**（SY-01）：用户界面、设备驱动让用户不用碰硬件细节。
2. **进程与多任务**（SY-02）：程序运行起来就是进程；一个 CPU 轮流给多个进程用，进程就在 running / ready / blocked 三种状态间转。
3. **调度**（SY-03）：谁下一个上 CPU？四种调度算法各有规则和好处；中断来了由内核按优先级接手。
4. **内存**（SY-04）：内存不够就用磁盘冒充（虚拟内存），按固定大小切叫分页、按可变大小切叫分段；换页太频繁就“抖动”。

翻译程序这半边有两类题，答法完全不同：

- **文字题**（SY-05 解释器、SY-06 编译阶段、SY-10 RPN 的用法）：按 MS 的“步骤链”一句一步写，每句一个得分点。
- **操作题**（SY-07 ～ SY-09 语法图与 BNF，SY-11、SY-12 RPN 转换与求值）：有固定的逐步作答模板，MS 按片段 / 按“圈”给分，照模板做几乎不失分。

本章文字题的共同规律：MS 常写 “One mark per mark point (Max n)”，列出的点比满分多。答题时按 **“定义 → 怎样做 → 结果 / 好处”** 的顺序写满 n 句，每句只说一件事；带 “…” 的 MS 点是前一点的展开，要和前一点一起写才自然。

### 题型树
<!-- auto:type-tree -->

### P3-SY-01　操作系统：资源利用与隐藏硬件复杂性　{#P3-SY-01}

<!-- auto:stats P3-SY-01 -->

**考法**　①描述两种向用户隐藏硬件复杂性的方式（每种“识别 1 + 描述 1”，共 4 分）；②说出用户界面对用户的一个好处并举一个例子（2 分）。考纲 16.1 还要求“OS 怎样最大化利用资源”，核验语料里还没有单独考过的 MS。

**识别信号**　complexities of the computer hardware are hidden from the user；user interface；State one benefit … and give an example；maximise the use of resources。

**解题思路**
1. 隐藏复杂性的方式，每种都写成“名称 + 它让用户省掉了什么”两截：

| 方式 | 怎样隐藏（描述那一分） |
|:--|:--|
| User interface / GUI | 用图标、菜单点选来操作，不用写涉及内存地址、总线的命令或代码 |
| Device drivers | 在 OS 里就能控制打印机等外设，不用在设备本身上操作 |
| Device mapping | 网络上的设备（实体或虚拟）容易识别、查看状态、使用 |
| 只接触应用层 | 用户只和 TCP/IP 的应用层打交道，下面几层的复杂性被隐藏 |

2. “好处 + 例子”题：好处写“界面向用户隐藏了硬件 / OS 的复杂性”（或“为不同需要的用户提供合适的访问方式”“不用写涉及内存位置、总线的复杂命令”），例子写一个具体动作：点图标而不是写代码。
3. 最大化利用资源（核验语料未考，以下非 MS 原句，作答时以所答那题的 MS 为准）：调度让 CPU 尽量不空闲（SY-03 的 MS 有 “To keep the CPU busy all the time”）；多任务让等待 I/O 的进程让出 CPU（SY-02）；虚拟内存让内存不够时程序仍能运行（SY-04）。

**得分表述**（引自对应 MS）
- 「Provision of a User Interface // Provision of a Graphical User Interface」⟦9618_w25_31:4(b)⟧
- 「Allows the user to interact with the computer in a more intuitive way」⟦9618_w25_31:4(b)⟧
- 「Makes it easier to control peripherals such as printers within the operating system of the computer rather than on the separate device itself」⟦9618_w25_31:4(b)⟧
- 「leaving the lower layers and their complexities hidden from the user」⟦9618_w25_31:4(b)⟧
- 「The user interface hides the complexities of the computer hardware/operating system from the user」⟦9618_w23_31:7(a)⟧
- 「Clicking on icon rather than writing code」⟦9618_w23_31:7(a)⟧

**易错与失分**
- 只写名称（“GUI”“device drivers”）不写描述：每种方式的第二分要写出“用户因此不必做什么”。
- 两种方式其实是一种：“GUI”和“icons and menus”都是用户界面，算一种；第二种换成设备驱动。
- 例子写成好处（“it is easier to use”）：例子必须是具体操作，如 clicking on an icon。
- 考官报告指出，最常见的得分答案是“用户界面 + 恰当展开”“设备驱动 + 恰当展开”（⟦9618_w25_31:4(b)⟧）。

#### 代表题精讲　⟦9618_w25_31:4(b)⟧

**在考什么**　Describe two ways in which the complexities of the computer hardware are hidden from the user. 4 分。MS 写明 “One mark for identification and one mark for a description (Max 4)”：两种方式各 2 分。

**完整作答**
1. 方式一：提供图形用户界面。描述：用户用图标和菜单点选来控制设备，交互更直观，不需要知道硬件怎样工作。
2. 方式二：使用设备驱动程序。描述：打印机等外设可以在计算机的操作系统里控制，而不用在设备本身上操作。

**与 MS 对齐**　1 ← “Provision of a User Interface // Provision of a Graphical User Interface” + “Allows the user to interact with the computer in a more intuitive way // Icons and menus are used to control devices by simply ‘pointing and clicking’”；2 ← “Use of device drivers” + “Makes it easier to control peripherals such as printers within the operating system of the computer rather than on the separate device itself”。`//` 两边是同一分的两种说法，写一边即可。

**英文作答句**　1: The OS provides a graphical user interface. Icons and menus are used to control devices by simply pointing and clicking, so the user interacts with the computer in a more intuitive way. 2: The OS uses device drivers. These make it easier to control peripherals such as printers within the operating system of the computer rather than on the separate device itself.

**直观**　开车只需要方向盘和踏板，不用懂发动机怎样点火：界面是方向盘，驱动程序是方向盘和发动机之间的那套连杆。

**下一道变式**　⟦9618_w23_31:7(a)⟧　（只问用户界面：好处 1 分 + 例子 1 分，例子要具体到动作。）

<!-- auto:drills P3-SY-01 -->

### P3-SY-02　进程、多任务与进程状态　{#P3-SY-02}

<!-- auto:stats P3-SY-02 -->

**考法**　①多任务是什么、目的、对进程管理有什么好处（1–2 分）；②多任务怎样实现、OS 怎样保证多任务高效（2–3 分）；③说出三种进程状态，或已给两种、说出另一种（1–3 分）；④进程从 running 变为 ready 的条件（2 分）；⑤填表：每种状态各给一个“为什么处在这个状态”的原因（3 分）。

**识别信号**　multi-tasking；process states；running / ready / blocked；change from the running state to the ready state；Complete the table to identify one reason why a process could be in each of the three states。

**解题思路**
1. **多任务**：多个进程“同时”运行——单个 CPU 实际上是轮流运行，所以 MS 写 “carry out / seem to carry out more than one process at a time”。好处：比一个接一个运行完成更多任务。
2. **怎样实现**：处理器时间与硬件资源在任务间共享 → 用调度决定执行哪个进程，避免冲突 → 高优先级任务可以中断正在运行的任务；OS 监视每个进程的状态。
3. **三种状态与转换**（每个箭头都可能被问“什么条件”）：

```
              调度程序分给它 CPU 时间片
     ready  ───────────────────────────►  running
       ▲    ◄───────────────────────────    │
       │    时间片用完 / 被更高优先级抢占 / 中断    │ 要等 I/O 或某个事件
       │                                    ▼
       └──────────  等待的事件完成  ──────────  blocked
```

| 状态 | 原因（填表时写这个，不要写状态名本身） |
|:--|:--|
| running | 已分到 CPU 时间，正在被执行 |
| ready | 能运行，在 ready queue 里等一片 CPU 时间；或被更高优先级的进程挤下来 |
| blocked | 在等 I/O 操作或某个事件发生 / 完成，给它 CPU 也运行不了 |

4. running → ready 的条件：时间片用完（轮转）；ready queue 里有更高优先级的进程，当前进程被抢占；有中断到达 CPU。注意 **要等 I/O 是去 blocked，不是去 ready**。

**得分表述**（引自对应 MS）
- 「Running multiple processes concurrently」⟦9618_s25_31:8(a)⟧
- 「To enable multiple programs/processes to be executed at the same time」⟦9618_w25_33:5(a)⟧
- 「processor time/common hardware and resources is/are shared between tasks」⟦9618_w24_32:9(b)(ii)⟧
- 「the operating system monitors the state of each task/process」⟦9618_w25_33:5(b)⟧
- 「When the time slice of the running process expires (round robin)」⟦9618_w23_31:7(c)⟧
- 「The process is waiting for an I/O operation / some event to take place / be completed」⟦9618_w25_32:5(b)⟧

**易错与失分**
- 考官报告指出，常见错误是把状态名当原因写，如 running 写 “the process is currently running”、ready 写 “the process is ready to run”，不给分（⟦9618_w25_32:5(b)⟧）。
- running → ready 写成“在等 I/O”：那是 running → blocked。
- “OS 怎样保证多任务高效”只写“用调度”：考官报告指出能拿第二、三分的是展开“保证进程不冲突”和“监视每个进程的状态”（⟦9618_w25_33:5(b)⟧）。
- 第三种状态写 waiting / stopped / paused：MS 只给 blocked（⟦9618_w23_31:7(b)⟧）。

#### 代表题精讲　⟦9618_w25_32:5(b)⟧

**在考什么**　A process can be in one of three process states: running, ready or blocked. Complete the table to identify one reason why a process could be in each of the three states. 3 分，每行 1 分。

**完整作答**

| 状态 | 原因 |
|:--|:--|
| running | 进程已分到 CPU 时间，正在被执行 |
| ready | 进程在 ready queue 里等一片 CPU 时间，它本身可以运行（或：被更高优先级的进程替下，否则还能继续运行） |
| blocked | 进程在等一个 I/O 操作或某个事件发生 / 完成 |

**与 MS 对齐**　三行分别对应 MS 表中的 “CPU time has been allocated and the process is being executed.”、“The process is waiting (in the ready queue) for a slice of CPU time. It could run. // It has been displaced by a higher priority process and could otherwise still run.”、“The process is waiting for an I/O operation / some event to take place / be completed.”。ready 一行 `//` 两边任写一种。

**英文作答句**　Running: CPU time has been allocated to the process and it is being executed. Ready: the process is waiting in the ready queue for a slice of CPU time; it could run. Blocked: the process is waiting for an I/O operation or some other event to be completed.

**直观**　一台游戏机三个孩子：手里拿着手柄的是 running；排着队、随时能接手的是 ready；去上厕所了、轮到他也玩不了的是 blocked——回来以后先去排队（ready），不能直接抢手柄。

**下一道变式**　⟦9618_w23_31:7(c)⟧　（问箭头：什么条件下 running 会变回 ready，2 分。）

<!-- auto:drills P3-SY-02 -->

### P3-SY-03　进程调度与中断处理　{#P3-SY-03}

<!-- auto:stats P3-SY-03 -->

**考法**　①为什么需要调度（2–3 分）；②说出两种调度算法（2 分）；③描述某种调度算法并给一个好处（单个算法 4 分：功能 Max 3 + 好处 Max 1；三个算法一起问时每个 2 分）；④内核怎样充当中断处理程序（2 分）；⑤中断处理怎样用于低级调度（2 分）。

**识别信号**　scheduling routine；round robin；shortest job first；first come first served；shortest remaining time；Explain the function of … and give a benefit；kernel … interrupt handler；low-level scheduling。

**解题思路**
1. **为什么要调度**（写满分值那么多条）：让多个程序看起来同时执行（实现多任务）；让高优先级作业先完成；让 CPU 一直忙、减少空闲；让所有进程及时、高效地执行；减少等待时间、公平使用 CPU、防止某些进程“饿死”。
2. **四种算法**：

| 算法 | 怎样选下一个进程 | 抢占？ | 好处（MS 说法） |
|:--|:--|:--|:--|
| First come first served | 按到达顺序排队，一个接一个执行 | 否 | 逻辑简单、处理器开销小；每个进程最终都能运行，不会饿死 |
| Round robin | 按到达排队；每个进程轮流得到固定时间片；时间片用完就保存状态、回到队列，下一个进程恢复状态继续 | 是 | 不会饿死；限制每个进程的时间，平均响应时间短 |
| Shortest job first | 选完成所需时间（burst time）最短的；一旦开始就运行到结束或进入等待 | 否 | 短作业不用等长作业；平均等待时间大大减少；吞吐量高 |
| Shortest remaining time | 选剩余时间最短的；新来一个更短的进程会替下当前进程 | 是 | 短进程很快处理完；等待时间最小 |

SJF 与 SRT 共同的缺点：短进程不断加入时，长作业可能一直等（starvation）。

3. **内核作为中断处理程序**（按顺序写）：内核收到中断信号 → 比较中断与当前进程 / 其他中断的优先级 → 优先级更高就进入内核态，查中断分派表（IDT）→ 把被中断进程的状态（寄存器内容）存到内核栈 → 处理完中断后恢复进程状态。
4. **低级调度里的中断处理**：低级调度程序按优先级处理中断，使紧急事件不被耽搁；用中断向量表 / 中断分派表查到该中断对应的服务例程（ISR）。

**得分表述**（引自对应 MS）
- 「Process scheduling allows more than one program/task to appear to be executed at the same time」⟦9618_w22_32:9(a)⟧
- 「To keep the CPU busy all the time」⟦9618_w22_32:9(a)⟧
- 「A fixed time quantum is given to each process」⟦9618_s25_33:6(b)⟧
- 「The process with the shortest time to complete/burst time is selected first and executed」⟦9618_s25_32:5(b)⟧
- 「When a process with a shorter burst time arrives the existing process is replaced by the shorter process」⟦9618_s25_31:8(b)⟧
- 「the kernel consults the interrupt dispatch table / IDT」⟦9618_w24_32:9(a)⟧

**易错与失分**
- 描述算法只是把名字换个说法（“shortest job first runs the shortest job first”）：考官报告指出，好的答案“说出了比名字本身更多的东西”并给出该算法自己的好处（⟦9618_w22_32:9(b)⟧）。要加上“按到达排队”“是否抢占”“时间片用完后怎样”。
- SJF 与 SRT 的抢占性写反：SJF 开始后不被打断（non-pre-emptive），SRT 会被更短的新进程替下（pre-emptive）。
- 好处与算法不配套：轮转的好处是不饿死、响应快；SJF 的好处是吞吐量高、平均等待短。
- 功能写了四五条、好处一条没写：功能最多 3 分，第 4 分只能来自好处。
- 中断题写成处理器层面的取指—执行周期检查中断：那是 HV-02。本型要写内核、优先级、IDT、保存与恢复进程状态。

#### 代表题精讲　⟦9618_s25_33:6(b)⟧

**在考什么**　Explain the function of the round robin scheduling routine and give a benefit of this routine. 4 分：功能 MP1–MP6 中最多 3 分，好处 MP7–MP8 中最多 1 分。

**完整作答**
- 功能：①进程按到达顺序排队。②这是一种抢占式调度。③每个进程得到相同的固定时间片。④时间片用完时，进程的状态被保存、回到队列，下次轮到时从中断处继续，下一个进程执行它的时间片。
- 好处：不会出现资源饿死，每个进程都会轮到。

**与 MS 对齐**　① ← MP1 “Processes are queued as they arrive.”；② ← MP2 “It is a pre-emptive scheduling routine.”；③ ← MP3 “A fixed time quantum is given to each process. // Each process has an equal time slice.”；④ ← MP4（还可以接 MP5 “and the next process is executed for its time slice …”）。功能写满 4 条也只计 3 分，第 4 分来自好处 MP8 “No issue with starvation of resources.”（或 MP7 “Reduces average response time …”）。

**英文作答句**　Function: processes are queued as they arrive. It is a pre-emptive scheduling routine: a fixed time quantum is given to each process. When a time slice ends, the status of the process is saved and it is queued, so it can continue from where it left off in its next time slice, and the next process is executed for its time slice. Benefit: there is no issue with starvation of resources.

**直观**　食堂只有一个窗口：轮转就是每人只许点 30 秒，没点完的回队尾接着排——没人会被饿着，但长单子的人要排好几轮。

**下一道变式**　⟦9618_s25_32:5(b)⟧　（换成 shortest job first：注意它是非抢占式，好处换成吞吐量高或平均等待短。）

<!-- auto:drills P3-SY-03 -->

### P3-SY-04　虚拟内存、分页、分段与磁盘抖动　{#P3-SY-04}

<!-- auto:stats P3-SY-04 -->

**考法**　①解释虚拟内存是什么（3 分）；②OS 为什么可能要用虚拟内存（2 分）；③分页与分段在划分内存方式上的一个区别（1 分）；④描述分段的过程（4 分）；⑤解释磁盘抖动是什么 / 在什么情况下发生（3 分）。

**识别信号**　virtual memory；paging；segmentation；pages / segments；segment map table；disk thrashing。

**解题思路**
1. **虚拟内存**三句：用磁盘（辅存）扩展可用的 RAM → CPU 看上去能访问比实际 RAM 更多的内存 → 只有正在用的数据需要在内存里，数据按需在 RAM 与虚拟内存之间换入换出。为什么用：RAM 快不够时（同时运行很多进程）；暂时不用的程序和数据移出 RAM，更有效地利用 RAM。
2. **分页**：内存按**固定大小**的块划分（由 OS 划分）。**分段**：逻辑 / 虚拟地址空间按**可变大小**的块（段）划分，段的大小由编译器算出；每段有名字和大小、有编号；地址由段名（号）和偏移量组成；段号作为下标去查段映射表（segment map table），表把逻辑地址映射到物理地址；执行时把需要的段从虚拟内存装进物理内存。
3. **页面替换**（考纲 “How pages can be replaced”，核验语料尚无 MS，以下非 MS 原句）：程序要用的页不在 RAM 里时（缺页），若 RAM 已满，OS 选一页换出到磁盘（例如先进先出、最近最少使用），再把需要的页调入。
4. **磁盘抖动**因果链（一句一环）：使用虚拟内存时可能发生 → 内存装满后，越来越多的页需要换入换出 → 磁盘访问频率极高、磁头大量移动 → 移动磁头很费时 → 最后换页的时间多于处理数据的时间（thrash point），程序卡死或不能运行。

**得分表述**（引自对应 MS）
- 「Disk / secondary storage is used to extend the RAM / memory available」⟦9618_w22_31:8(a)⟧
- 「so the CPU appears to be able to access more memory space than the available RAM」⟦9618_w22_31:8(a)⟧
- 「Paging allows the memory to be divided into fixed size blocks and Segmentation divides the memory into variable sized blocks」⟦9618_w22_31:8(b)⟧
- 「the logical / virtual address space is broken into varying sized blocks called segments」⟦9618_w24_31:8(a)⟧
- 「As the main memory fills up, more and more pages need to be swapped in and out of virtual memory」⟦9618_w24_31:8(b)⟧
- 「Eventually, more time is spent swapping the pages/data than processing the data」⟦9618_w23_32:5(b)⟧

**易错与失分**
- 考官报告指出，一些考生把 virtual memory 答成了 virtual machine（⟦9618_w22_31:8(a)⟧）。虚拟机是 HV-05。
- 区别题只写了分页或只写了分段：考官报告指出这样不构成“区别”（⟦9618_w22_31:8(b)⟧）。一句话里两边都要有；固定 / 可变别写反。
- 考官报告指出，有考生把磁盘抖动和磁盘碎片混为一谈（⟦9618_w23_32:5(b)⟧）。抖动的核心是“换页太频繁”，与文件是否连续存放无关。
- 分段过程题普遍偏难（考官报告，⟦9618_w24_31:8(a)⟧）：最容易拿的三点是“地址空间分成可变大小的段”“段有编号”“段号作为段映射表的下标”。

#### 代表题精讲　⟦9618_w22_31:8(a)⟧

**在考什么**　Virtual memory, paging and segmentation are used in memory management. Explain what is meant by virtual memory. 3 分，MS 四点中任三点。

**完整作答**
1. 用磁盘（辅存）来扩展可用的 RAM / 内存。
2. 因此 CPU 看上去能访问比实际 RAM 更多的内存空间。
3. 只有正在使用的数据需要放在主存里，数据按需要在 RAM 和虚拟内存之间换入换出。
4. 虚拟内存是临时建立的。

**与 MS 对齐**　1 ← “Disk / secondary storage is used to extend the RAM / memory available”；2 ← “… so the CPU appears to be able to access more memory space than the available RAM”；3 ← “Only the data in use needs to be in main memory so data can be swapped between RAM and virtual memory as necessary”；4 ← “Virtual memory is created temporarily.”。四点各自独立，写三点即满分，写四点更稳。

**英文作答句**　Virtual memory is where disk / secondary storage is used to extend the RAM available, so the CPU appears to be able to access more memory space than the available RAM. Only the data in use needs to be in main memory, so data can be swapped between RAM and virtual memory as necessary. Virtual memory is created temporarily.

**直观**　书桌（RAM）太小，就把暂时不看的书放到身后的书架（磁盘）上，要用时再换回来；换得太勤，人一直在转身拿书、根本没空读书——这就是抖动。

**下一道变式**　⟦9618_w24_31:8(b)⟧　（解释磁盘抖动，3 分：按因果链一句一环写。）

<!-- auto:drills P3-SY-04 -->

### P3-SY-05　解释器怎样执行程序　{#P3-SY-05}

<!-- auto:stats P3-SY-05 -->

**考法**　描述用解释器执行程序的过程，或解释解释器怎样不生成完整的翻译版本就执行程序，4 分。考得少（见上方考情），但问法和 MS 几乎固定，背熟步骤链就是满分。

**识别信号**　interpreter；executes a program without producing a complete translated version；the process of executing a program using an interpreter。

**解题思路**　按解释器的循环一步一句写：
1. 解释器每次翻译源代码的一行（一条语句）。
2. 检查这一行有没有错误。
3. 没有语法错误就立即执行这一行。
4. 发现错误就报告错误信息并停止。
5. 不保存可执行文件；所以循环里的行每执行一次都要重新翻译，每次运行程序也要重新翻译。

**得分表述**（引自对应 MS）
- 「The interpreter translates the source code one line at a time」⟦9618_s25_31:6⟧
- 「If the line is syntax error free it is executed」⟦9618_s25_31:6⟧
- 「It is not stored in executable format」⟦9618_s25_31:6⟧
- 「If an error is found, the program halts with an error message」⟦9618_s25_31:6⟧
- 「Interpretation is repeated for every iteration in repeated sections of code/in loops」⟦9618_s21_31:3(b)⟧
- 「Interpretation has to be repeated every time the program is run」⟦9618_s21_31:3(b)⟧

**易错与失分**
- 考官报告指出，有考生写的是编译或编译的某些阶段，而不是解释（⟦9618_s25_31:6⟧）。不要出现“目标代码”“可执行文件生成”。
- 写成解释器与编译器的优缺点比较：这是 P1-SS-04 / SS-05 的问法；本型问“过程”，写步骤。
- 只写“translates line by line”：那只是 1 分。检查、执行、遇错停止、每次重新翻译各是一分。

#### 代表题精讲　⟦9618_s25_31:6⟧

**在考什么**　Describe the process of executing a program using an interpreter. 4 分，MS 五点中任四点。

**完整作答**
1. 解释器每次把源代码翻译一行。
2. 如果这一行没有语法错误，就执行它。
3. 如果发现错误，程序停止并给出错误信息。
4. 翻译结果不以可执行格式保存。
5. 每一行每次运行都必须重新翻译，循环里多次执行的行也一样。

**与 MS 对齐**　1 ← MP1 “The interpreter translates the source code one line at a time”；2 ← MP2；3 ← MP4；4 ← MP3 “It is not stored in executable format”；5 ← MP5。五点互相独立，写满四点即满分。

**英文作答句**　The interpreter translates the source code one line at a time. If the line is syntax error free it is executed. If an error is found, the program halts with an error message. The translated code is not stored in executable format, so each line must be translated every time it is run, including lines that run multiple times in loops.

**直观**　解释器像同声传译：说一句翻一句，听众马上听到；说错了当场停下。没有书面译稿，所以同一段话再讲一遍，还得再翻一遍。

**下一道变式**　⟦9618_s21_31:3(b)⟧　（2021 扩展题，核验语料没有第二道；问法换成“不生成完整翻译版本”，MS 把“检查—无错执行—有错报告并停止”分成三点。）

<!-- auto:drills P3-SY-05 -->

### P3-SY-06　编译的各个阶段　{#P3-SY-06}

<!-- auto:stats P3-SY-06 -->

**考法**　①已给词法分析、语法分析，说出另外两个阶段（2 分）；②解释词法分析（目的 2 分 / 过程 4 分）；③语法分析的目的或过程（2–4 分）；④优化阶段的目的或过程（1–2 分）；⑤四个阶段与描述连线（4 分，有一个干扰项）。

**识别信号**　stages … compilation；lexical analysis；syntax analysis；code generation；optimisation；tokens；parse tree；symbol table。

**解题思路**
1. 四个阶段（考纲 16.2 的顺序）与各自的“输入 → 做什么 → 输出”：

| 阶段 | 做什么 | 产出 / 交给谁 |
|:--|:--|:--|
| Lexical analysis（第一阶段） | 去掉空白和注释；把源代码切成一串记号（tokens），给每个记号分类；标识符存入符号表；遇到非法记号报错 | 记号流交给语法分析 |
| Syntax analysis（第二阶段） | 把记号流按语言的语法规则（BNF / 语法图，见 SY-07 ～ SY-09）分析（parse），检查代码是否符合文法 | 语法树（parse tree）；报告语法错误 |
| Code generation | 把源代码的中间表示转换成可执行形式 | 目标代码 |
| Optimisation | 找出并删除冗余代码、化简表达式、调整代码顺序 | 存储、内存、CPU 时间、执行时间等资源用得最少 |

2. 连线题（⟦9618_w22_31:4⟧ 的 MS）：lexical ↔ “converting a sequence of characters into a sequence of tokens”；syntax ↔ “using parsing algorithms to interpret the meaning of a sequence of tokens”；code generation ↔ “converting an intermediate representation of source code into an executable form”；optimisation ↔ “minimising a program’s execution time and memory requirement”。干扰项 “directly executing instructions written in a scripting language” 说的是解释器，不连。
3. “目的”题（2 分）写“做什么 + 为了什么”；“过程 / explain”题（4 分）把表格那一行全部写出来，第一句可以写“它是编译的第几阶段”——MS 把这句也算一分。

**得分表述**（引自对应 MS）
- 「White space and comments are removed」⟦9618_s25_32:8⟧
- 「It takes modified source code and breaks it into a series of tokens」⟦9618_s25_32:8⟧
- 「Identifiers are stored in a symbol table」⟦9618_s25_32:8⟧
- 「The source code is analysed / parsed against the rules of the language to detect any errors in the code」⟦9618_s25_33:8⟧
- 「The output from this phase is a parse tree」⟦9618_s25_33:8⟧
- 「To identify and remove redundant code / To simplify expressions / To reorder the code」⟦9618_w25_33:7(a)⟧

**易错与失分**
- 考官报告指出，语法分析题里常见的错误是写成了词法分析，或写成了解释器的执行过程（⟦9618_s25_33:8⟧）。词法分析不管语法对不对，只管“切成合法的记号”。
- 语法分析只写一句“checks syntax”：考官报告指出完全正确的答案不多（⟦9618_w22_32:2(b)⟧）；要写“按语言规则检查记号”“报告语法错误”“产生语法树”三件事。
- 优化只写“makes the program better”：要写出减少的是什么资源（内存、存储、CPU 时间、执行时间）。
- “另外两个阶段”又写了词法或语法分析：题干已经给出，MS 只给 code generation 和 optimisation。

#### 代表题精讲　⟦9618_s25_32:8⟧

**在考什么**　Explain what is meant by lexical analysis during program compilation. 4 分，MS 七点中任四点。

**完整作答**
1. 词法分析是编译的第一个阶段。
2. 去掉空白和注释。
3. 把（修改后的）源代码切分成一串记号（tokens）。
4. 每个记号被分类、指定类型。
5. 标识符存入符号表。
6. 发现非法记号就报错；合格的结果交给语法分析器。

**与 MS 对齐**　1 ← MP1 “It is the first stage of compilation”；2 ← MP2；3 ← MP3；4 ← MP4 “Each token is categorised and assigned types”；5 ← MP5；6 ← MP6、MP7。各点独立，写满四点即满分。

**英文作答句**　Lexical analysis is the first stage of compilation. White space and comments are removed, then the modified source code is broken into a series of tokens. Each token is categorised and assigned a type, and identifiers are stored in a symbol table. If the lexical analyser finds invalid tokens it generates an error; acceptable data passes to the syntax analyser.

**直观**　批改英文作文的第一遍：先把句子拆成一个个单词，查每个词是不是真的英文单词（词法）；第二遍才看单词排成的句子合不合语法（语法分析）。

**下一道变式**　⟦9618_s25_33:8⟧　（换成第二阶段：语法分析的过程，输入是记号流、输出是语法树。）

<!-- auto:drills P3-SY-06 -->

### P3-SY-07　按语法图或 BNF 判断字符串是否合法　{#P3-SY-07}

<!-- auto:stats P3-SY-07 -->

**考法**　给出几个语法图（偶尔是 BNF），①说明给定字符串为什么不合法（每个 1 分）；②判断每个字符串合法或不合法并给理由（“判断 + 理由”组合 1 分）；③写出一个合法的例子，可能另加长度等约束（1 分）。

**识别信号**　Several syntax diagrams are shown；State whether each … is valid or invalid and give a reason；State why … is not a valid …；State an example of a valid …。

**解题思路（逐步作答模板）**
1. **读懂图例**：圆圈（圆角）里是终结符——真正出现在字符串里的字符；方框里是另一个语法图的名字；箭头方向是先后顺序；分叉是“多选一”；从方框后面绕回前面的线是“可重复（至少一次）”；绕过方框的线是“可以没有”。
2. **把规则翻成一句话**，例如 ⟦9618_s23_31:6(a)⟧ 的 password：一个或多个 letter，接一个或多个 digit，接一个或多个 symbol。
3. **逐个字符对照**：给每个字符标上它属于哪个组；找到**第一个**不符合规则的位置。
4. **理由写“位置 + 规则”**：“必须以 … 开头”“第 n 个字符不能是 …”“只能有一位或两位”“? 不是合法的 symbol”。不要只写“does not follow the syntax diagram”。
5. **写合法例子**：只用图里列出的字符（字母表常故意缺几个字母），满足题目附加的长度要求；写完按第 3 步自查一遍。

**得分表述**（引自对应 MS）
- 「must begin with a member of the group uppercase // cannot begin with a symbol」⟦9618_s25_31:7(a)⟧
- 「the fourth character cannot be a member of the group uppercase」⟦9618_s25_31:7(a)⟧
- 「The symbol comes before the digits – it should be after」⟦9618_s23_31:6(a)⟧
- 「The ? is not a valid symbol」⟦9618_s23_31:6(a)⟧
- 「a number can only be one or two digits in length not three」⟦9618_w24_32:7(a)⟧
- 「Variables must begin with a letter / not a digit」⟦9618_s25_32:9(a)⟧

**易错与失分**
- 判断题只写 valid / invalid、不写理由：MS 按“判断与理由的组合”给分，缺一样这一分就没有。
- 理由太笼统：要指出具体哪个字符、违反哪条规则。考官报告指出，能给出“明确理由”的才得分（⟦9618_s25_31:7(a)⟧）。
- 合法例子用了图里没有的字符：考官报告专门列出了该题可用的字母与数字（字母表里没有 I），超出的不给分（⟦9618_s25_32:9(d)⟧）。
- 看漏回环（以为只能出现一次）或看漏旁路（以为必须出现）。

#### 代表题精讲　⟦9618_s23_31:6(a)⟧

**在考什么**　讲解时请对照原卷 QP p.6（语法图）与 p.7（作答区）。password 的语法图：letter（带回环）→ digit（带回环）→ symbol（带回环）；letter 只有 A、D、P、R、Y，symbol 只有 $ % & @ #，digit 是 0–9。判断 DPAD99$、DAD#95、ADY123? 是否合法并给理由，3 分，每个“判断 + 理由”1 分。

**完整作答**

| 字符串 | 判断 | 理由 |
|:--|:--|:--|
| DPAD99$ | 合法 | 4 个字母（都在 letter 里）后接 2 个数字，再接一个 symbol，顺序正确 |
| DAD#95 | 不合法 | symbol（#）出现在数字前面，按规则它应该在数字后面 |
| ADY123? | 不合法 | ? 不是合法的 symbol |

**与 MS 对齐**　三行分别对应 MS 的 “DPAD99$ – Valid / Reason – 4/multiple letters followed by 2/multiple digits followed by a symbol.”、“DAD#95 – Invalid / Reason – The symbol comes before the digits – it should be after.”、“ADY123? – Invalid / Reason – The ? is not a valid symbol.”。每行判断和理由都对才得 1 分。

**英文作答句**　DPAD99$ is valid: it has four letters followed by two digits followed by a symbol. DAD#95 is invalid: the symbol comes before the digits; it should be after them. ADY123? is invalid: ? is not a valid symbol.

**直观**　语法图是一张单行道地图：顺着箭头只能先过“字母街”，再过“数字街”，最后到“符号街”；可以在一条街上绕圈多走几遍，但不能倒着开，也不能走地图上没有的路。

**下一道变式**　⟦9618_w24_32:7(a)⟧　（number 只能是一位奇数，或一位奇数接一位奇数或偶数：21、123 为什么不合法。）

<!-- auto:drills P3-SY-07 -->

### P3-SY-08　写或补全 BNF　{#P3-SY-08}

<!-- auto:stats P3-SY-08 -->

**考法**　①把只含终结符的语法图写成 BNF：列出全部字符（常 1 分）；②把由方框组成的语法图写成 BNF（2–4 分）；③“一个或多个”要用递归写（常有一分专给递归）；④按一条新的文字规则写 BNF（2–3 分），可以引入中间非终结符。不拆得分点，但 MS 往往按“每行 / 每组选项”给分。

**识别信号**　Complete the Backus-Naur Form (BNF) for …；Write the BNF for …；`<name> ::=` 后面留空；<word> contains one or more letters。

**解题思路（逐步作答模板）**
1. **记号**：`::=` 读作“定义为”；`|` 读作“或”，只放在两个选项**之间**；`<…>` 是非终结符；终结符（具体字符）直接写。
2. **终结符列表**（只含圆圈的图）：`<symbol> ::= % | £ | # | @ | $`。一个不漏、一个不多；开头和结尾都不加 `|`。
3. **顺序**（方框串联）：直接相邻写，`<letter><digit><digit>`，中间不加 `|`。
4. **有限次数的选择**（“一或两个”“第三个字符可以是 A 或 B”）：要么把所有组合用 `|` 全部列出，要么先定义一个中间非终结符再引用，如 `<digits> ::= <number>|<number><number>`。两种写法 MS 都给。
5. **一个或多个**（图里有回环）：用递归，`<word> ::= <letter>|<word><letter>`（或 `<letter><word>|<letter>`）。必须有一个不递归的选项作出口，否则永远写不完。
6. **名称照抄**题目里的写法，包括下划线：`<unsigned_integer>`、`<assignment_statement>`。
7. **自查**：拿一个合法串和一个不合法串按你的 BNF 推一遍。

**得分表述**（引自对应 MS）
- 「<uppercase> ::= A | C | E | G | J」⟦9618_s25_31:7(b)⟧
- 「<passcode> ::= <uppercase><code>」⟦9618_s25_31:7(b)⟧
- 「<word> ::= <letter>|<word><letter>」⟦9618_s23_32:3(b)⟧
- 「<number> ::= <odd>|<odd><even>|<odd><odd>」⟦9618_w24_32:7(b)⟧
- 「<label> ::= <letter><digit>|<letter><digit><digit>」⟦9618_w24_31:10(a)⟧
- 「<middle> ::= <lower>|<digit>」⟦9618_s25_33:9(b)⟧

**易错与失分**
- 考官报告指出两种常见的 `|` 错误：在列表首尾多加 `|`（如 `| + | - | * | / |`），以及在一个序列的每两项之间都加 `|`（如 `<letter>|<digit>|<letter>|<digit>|<digit>`）（⟦9618_w24_31:10(a)⟧）。
- 考官报告指出，常见错误是 `<unsigned_integer>` 漏了下划线（⟦9618_s22_32:4(b)⟧）。
- 回环写成固定次数：“一个或多个”不能只列一个、两个、三个——要递归。考官报告指出该题拿满分必须写出递归（⟦9618_s25_31:7(b)⟧）。
- 新规则题没有逐条照文字写：考官报告指出，严格按照题目开头对新规则的描述来构造 BNF 的考生才得分（⟦9618_w24_31:10(b)(ii)⟧）。

#### 代表题精讲　⟦9618_s25_31:7(b)⟧

**在考什么**　讲解时请对照原卷 QP p.8（语法图）与 p.9（作答区）。uppercase 只有 A、C、E、G、J；passcode 的图：一个 uppercase，后面是 lowercase / symbol / digit 三选一，并有一条回环回到三选一之前——即“一个大写字母，后接一个或多个（小写字母或符号或数字）”。Complete the BNF for `<uppercase>` and `<passcode>`. 4 分。

**完整作答**

```
<uppercase> ::= A | C | E | G | J
<passcode>  ::= <uppercase><code>
<code>      ::= <lowercase>|<symbol>|<digit>
                |<lowercase><code>|<symbol><code>|<digit><code>
```

做法：uppercase 是纯终结符列表；passcode 后半段“一个或多个”，所以先引入中间非终结符 `<code>`，用“三个不递归的出口 + 三个递归选项”写出“至少一个、可以更多”。

**与 MS 对齐**　MS 写 “One mark per mark point”、共 4 分，范答印成四行：`<uppercase>` 一行、`<passcode>` 一行、`<code>` 的三个非递归选项一行、三个递归选项一行，与上面四行逐行对应（MS 没有给这四行编号，这里按“四行对四分”对应）。考官报告指出拿满分必须写出递归，所以递归选项那一行不能省。

**规范写法**　见上方代码块；`<code>` 可以写在一行里，只要 `|` 只出现在选项之间。

**直观**　递归定义像“排队”：一队人 = 一个人，或者“一队人后面再站一个人”。最短的队是一个人（出口），任意长的队都能这样一个一个接出来。

**下一道变式**　⟦9618_s23_32:3(b)⟧　（先写 `<word>`“一个或多个字母”的递归，再用它写 `<variable>`，3 分。）

<!-- auto:drills P3-SY-08 -->

### P3-SY-09　画或补全语法图　{#P3-SY-09}

<!-- auto:stats P3-SY-09 -->

**考法**　①按文字规则画一个新的语法图（3–4 分）；②在给定语法图上按修改后的规则补全（2–3 分）。常和 SY-08 连在一起：先画图，下一小问把同一规则写成 BNF。

**识别信号**　Draw a syntax diagram for …；Complete the syntax diagram for … to show these changes；作答区是空白或画了一半的图。

**解题思路（逐步作答模板）**
1. **把规则切成槽位**：每个槽位写清“哪些组成部分可选”和“出现几次”（恰好一次 / 一或两次 / 零或多次 / 一或多次）。
2. **按槽位选画法**：

| 要表达 | 画法 |
|:--|:--|
| 恰好一次 | 方框画在主线上 |
| 多选一 | 几个方框并联：主线分叉、各过一个方框、再汇合 |
| 一次或多次 | 方框 + 从方框出口绕回方框入口的回环箭头 |
| 零次或多次 | 回环 + 一条从方框入口直通出口的旁路 |
| 一次或两次 | 两个方框串联，第二个方框加旁路 |

3. **画完整**：左边写图名，入口一个箭头，出口一个箭头；每段线都有箭头；方框里的名字照抄题目（number 不要写成 numbers）。
4. **自查**：沿箭头走最短的一条路和最长的路，看是否正好满足规则；再找有没有规则不允许的路（多余的方框、多余的回环）。
5. **补全题**只改题目要求的地方，别的槽位不要加东西。

**得分表述**（引自对应 MS）
- 「letter can repeat and digit present」⟦9618_s23_31:6(c)⟧
- 「digit can repeat or can be bypassed」⟦9618_s23_31:6(c)⟧
- 「correct structure – name, boxes and arrows (in and out)」⟦9618_s23_31:6(c)⟧
- 「end with either one or two symbols」⟦9618_w24_31:10(b)(i)⟧
- 「provision for one or two numbers including relevant connectors」⟦9618_w24_32:7(c)(i)⟧
- 「Correct repetition arrow for final digit」⟦9618_s25_33:9(c)⟧

**易错与失分**
- 考官报告指出：最后两个方框应一起重复，却给每个方框各画了一个回环；漏了最后的出口箭头（⟦9618_s25_32:9(c)⟧）。
- 考官报告指出：补全题在其他位置也加了 upper 等多余方框（⟦9618_s25_33:9(c)⟧）。
- 考官报告指出：把 number 写成 numbers、漏箭头、没保证 number 只出现一次或两次（⟦9618_w24_32:7(c)(i)⟧）；考官还提醒用铅笔画，便于擦改。
- “零个或多个 digit”只画了回环没画旁路：那表示至少一个。

#### 代表题精讲　⟦9618_s23_31:6(c)⟧

**在考什么**　讲解时请对照原卷 QP p.6（letter、digit 语法图）与 p.7（作答区）、MS p.6（两种范图）。An identifier begins with one or more letters, followed by zero digits or one digit or more digits. Draw a syntax diagram for an identifier. 4 分。

**完整作答**　槽位：①letter，一次或多次；②digit，零次或多次。画法：letter 方框加回环；digit 方框加回环，再加一条绕过 digit 的旁路。

```
                 ┌────◄─────┐        ┌────◄────┐
                 │          │        │         │
identifier ──►───┴─[letter]─┴──►──┬──┴─[digit]─┴──┬──►
                                  │               │
                                  └───────►───────┘
```

（上方两条线是回环：从方框出口绕回方框入口；下方一条是旁路：不经过 digit 直接到出口。）

**与 MS 对齐**　MS 四点各 1 分：“begins with a letter”；“letter can repeat and digit present”；“digit can repeat or can be bypassed”；“correct structure – name, boxes and arrows (in and out)”。MS 给了两种范图：上面这种，和“一个 letter 接一个带回环的 letter、再接带回环和旁路的 digit”。两者走出来的字符串完全一样，都给分。

**规范画法要点**　图名 identifier 写在入口线左上方；回环箭头指向方框入口；旁路从 digit 前分出、在 digit 后汇合；出口箭头一个。

**直观**　回环是“还可以再来一次”，旁路是“这一项可以跳过”。“一个或多个”= 先必须走一次再可以绕圈；“零个或多个”= 可以绕圈也可以整段跳过。

**下一道变式**　⟦9618_w24_31:10(b)(i)⟧　（password：开头 letter 或 symbol 二选一，中间一个 digit，结尾一或两个 symbol，3 分。）

<!-- auto:drills P3-SY-09 -->

### P3-SY-10　RPN 的用途与用栈求值的方法　{#P3-SY-10}

<!-- auto:stats P3-SY-10 -->

**考法**　①解释为什么用逆波兰表示法（RPN）求表达式的值（2 分）；②说出求 RPN 用的数据结构并给理由（2 分）；③用文字解释怎样用栈求 RPN 的值（3 分）；④针对前一小问的具体表达式描述求值的主要步骤（4 分，只写通用步骤最多 3 分）。

**识别信号**　Explain why Reverse Polish Notation (RPN) is used；Identify … a data structure；Explain how a stack can be used to evaluate RPN expressions；Describe the main steps in the evaluation of this RPN expression using a stack。

**解题思路（逐步作答模板）**
1. 从左到右，每次读一项。
2. 判断这一项是数值还是运算符。
3. 是数值：压入栈（push）。
4. 是运算符：弹出（pop）栈顶两个值，对它们做这个运算，把结果压回栈。**先弹出的是右边的操作数**（对 − 和 ÷ 很重要）。
5. 重复直到整个表达式读完；栈里剩下的唯一一个值就是结果。

为什么用 RPN：表示没有歧义；从左到右一次读完；不需要括号；不需要运算优先级规则（BODMAS）。为什么用栈：后进先出正好让“最近的两个操作数”先被取出。

具体表达式题（④）：把上面五步里的“数值”“运算符”换成该表达式的真实内容，如“先把 10、10、3、2 依次压栈；遇到第一个运算符 * 时弹出 2 和 3 …”。

**得分表述**（引自对应 MS）
- 「Evaluate the RPN expression from left to right」⟦9618_w23_31:9(b)⟧
- 「Push each element of the RPN expression onto the stack in order until an operator is reached」⟦9618_w23_31:9(b)⟧
- 「Pop the last two elements from the stack and apply the operator」⟦9618_w23_31:9(b)⟧
- 「Push the result of the operation onto the stack」⟦9618_w23_31:9(b)⟧
- 「This repeats until a single value remains, which is the solution」⟦9618_w23_32:6(b)⟧
- 「Reverse Polish Notation provides an unambiguous method of representing an expression」⟦9618_s21_31:4(a)(i)⟧

**易错与失分**
- 考官报告指出，最好的答案用一种能套用到任何 RPN 表达式的通用方式描述过程（⟦9618_w23_31:9(b)⟧、⟦9618_w23_32:6(b)⟧）。通用题不要拿某个具体表达式代替步骤。
- 反过来，题目给了具体表达式时（⟦9618_s22_31:5(b)(ii)⟧），MS 写明 “Max 3 generic answer only”：要拿满 4 分必须带上这个表达式的具体数值和运算符。
- 把运算符也压进栈：栈里只放数值。
- “Push each element … until an operator is reached”指的是操作数入栈，不是运算符入栈。

#### 代表题精讲　⟦9618_w23_31:9(b)⟧

**在考什么**　Explain how a stack can be used to evaluate RPN expressions. 3 分，MS 五点中任三点。

**完整作答**
1. 从左到右处理 RPN 表达式。
2. 按顺序把每个元素压入栈，直到遇到运算符。
3. 遇到运算符时，弹出栈顶的两个元素，对它们做这个运算。
4. 把运算结果压回栈。
5. 重复以上过程直到整个表达式求值完毕。

**与 MS 对齐**　1–5 依次对应 MP1–MP5，五点独立；写满三点即得 3 分，写五点最稳。

**英文作答句**　The RPN expression is evaluated from left to right. Each element is pushed onto the stack in order until an operator is reached. The last two elements are then popped from the stack and the operator is applied to them, and the result of the operation is pushed onto the stack. This process repeats until the whole expression is evaluated, leaving the result on the stack.

**直观**　像叠盘子算账：数字一张张叠上去；来了一个运算符，就拿走最上面两张，算完把结果写成一张新盘子放回去。最后只剩一张，就是答案。

**下一道变式**　⟦9618_s22_31:5(b)(ii)⟧　（针对 `m m j k * - *` 描述主要步骤，4 分；必须写出具体数值，通用描述最多 3 分。）

<!-- auto:drills P3-SY-10 -->

### P3-SY-11　中缀表达式与 RPN 互相转换　{#P3-SY-11}

<!-- auto:stats P3-SY-11 -->

**考法**　①把中缀表达式写成 RPN（1–3 分）；②把 RPN 写回中缀（1–3 分，括号是关键）；③把转回的中缀代入给定数值求值（1 分）。MS 常按片段给分（如前半段一分、后半段一分）。

**识别信号**　Write the infix expression in RPN；Write this RPN expression in infix form；Convert this Reverse Polish Notation (RPN) back to its original infix form；Evaluate your infix expression … when a = …。

**解题思路（逐步作答模板）**

**中缀 → RPN（加括号法）**
1. 按运算顺序给每一个运算加上括号（括号内先算；同级运算从左到右；× ÷ 先于 + −）。
2. 从最内层括号开始，把每个 `(x op y)` 改写成 `x y op`。
3. 去掉所有括号，项与项之间留空格。
4. 自查：操作数的先后顺序与原式完全相同，只有运算符的位置变了。

例：`(2 – 6) * (13 + 7) / 5` → `(((2 – 6) * (13 + 7)) / 5)` → `2 6 –` 与 `13 7 +` → `2 6 – 13 7 + *` → `2 6 – 13 7 + * 5 /`。

**RPN → 中缀（栈法）**
1. 从左到右读；操作数照写（压栈）。
2. 遇到运算符，取最近的两个“项” x、y（x 在前），合成 `(x op y)` 当作一个新项。
3. 读完后只剩一项，就是中缀式。
4. 去掉最外层和不影响运算顺序的括号；**凡是去掉后会改变运算顺序的括号一律保留**。

**得分表述**（引自对应 MS）
- 「((5 + 2) / (9 - 3)) * 3」⟦9618_s24_31:5(a)⟧
- 「7 3 + 2 8 * - 6 /」⟦9618_s24_31:5(b)⟧
- 「2 6 – 13 7 + * 5 /」⟦9618_w25_31:8(b)⟧
- 「(a – b + c) * (c - a) / d」⟦9618_w25_32:8(b)⟧
- 「(5 – 2) * (5 + 4) / 9」⟦9618_w23_31:9(a)(i)⟧
- 「a b * b + d - 15 +」⟦9618_w22_31:5(a)⟧

**易错与失分**
- 考官报告指出，RPN 转中缀时常见错误是漏括号，使答案的运算顺序变了（⟦9618_w23_31:9(a)(i)⟧）；还有漏了包住 a、b、c 那整项的括号，或漏了第二个 c、a 那项的括号（⟦9618_w25_32:8(b)⟧）。
- − 和 ÷ 的操作数顺序写反：`9 3 -` 是 9 − 3，不是 3 − 9。
- 中缀转 RPN 时打乱了操作数顺序：RPN 里操作数的先后与原式一样。
- 同级运算没按从左到右：`a * b + b - d + 15` 的 RPN 是 `a b * b + d - 15 +`，每做完一步就跟一个运算符。

#### 代表题精讲　⟦9618_s24_31:5(a)⟧

**在考什么**　Write this Reverse Polish Notation (RPN) in infix form: `5 2 + 9 3 - / 3 *`。3 分，MS 按三个片段各 1 分。

**完整作答**

| 读到 | 动作 | 当前的项（左 → 右） |
|:--|:--|:--|
| 5、2 | 照写 | 5，2 |
| + | 合成 | (5 + 2) |
| 9、3 | 照写 | (5 + 2)，9，3 |
| - | 合成 | (5 + 2)，(9 - 3) |
| / | 合成 | ((5 + 2) / (9 - 3)) |
| 3 | 照写 | ((5 + 2) / (9 - 3))，3 |
| * | 合成 | ((5 + 2) / (9 - 3)) * 3 |

答案：`((5 + 2) / (9 - 3)) * 3`（最外层那对括号可以去掉，但 (5 + 2)、(9 − 3) 两对必须保留）。

**与 MS 对齐**　MS “One mark per correct term (Max 3)”：`(5 + 2)` 1 分，`/ (9 – 3)` 1 分，`* 3` 1 分；完整答案 `((5 + 2) / (9 - 3)) * 3`。三个片段是三个独立得分点。

**直观**　RPN 是“先报材料、后报做法”：`5 2 +` 就是“拿 5 和 2，加起来”。转回中缀，就是每听到一个做法，把前面最近的两份材料用括号包起来。

**下一道变式**　⟦9618_w25_31:8(b)⟧　（反方向：`(2 – 6) * (13 + 7) / 5` 写成 RPN，2 分。）

<!-- auto:drills P3-SY-11 -->

### P3-SY-12　RPN 求值与栈内容变化　{#P3-SY-12}

<!-- auto:stats P3-SY-12 -->

**考法**　给一个 RPN 表达式和变量取值，在一排空栈格里画出求值过程中栈内容的变化（4 分）。MS 在范答上画“圈”，“One mark per ring”：要么四个圈各 1 分，要么三个圈 + “中间值与最终值” 1 分。偶有直接求值并写过程的 2 分题（2021）。

**识别信号**　Show the changing contents of the stack as the RPN expression is evaluated；一排竖着的空格子（每列一个栈）；where a = …, b = …。

**解题思路（逐步作答模板）**
1. 先把变量换成数值，写在表达式下面（`c a / b d – * b +` → `9 3 / 16 6 – * 16 +`）。
2. **一个记号占一列**：表达式有几个记号（数值 + 运算符），就画几列。QP 给的格子列数通常正好等于记号数。
3. 读到数值：新的一列 = 上一列 + 顶上多一个数。
4. 读到运算符：新的一列 = 上一列弹出顶上两个数、放回运算结果（比上一列少一格）。**下面那个数在运算符左边**：栈底 9、栈顶 3，遇到 / 得 9 / 3 = 3。
5. 栈底写在最下面一格，每列从底往上填；**格子里只写数字，不写运算符**。
6. 最后一列只剩一个数，就是结果。

**得分表述**（引自对应 MS）
- 「One mark per ring (Max 4)」⟦9618_w25_32:8(c)⟧
- 「One mark for the interim total (360) and the final total (10)」⟦9618_w25_33:7(c)⟧
- 「Do not allow operators in stacks」⟦9618_s22_31:5(b)(i)⟧
- 「One mark per ring (Max 4)」⟦9618_s24_31:5(c)⟧

**易错与失分**
- 考官报告指出，有考生在表示栈的列里写了运算符号；运算符不入栈，不应出现在图里（⟦9618_w25_31:8(c)⟧、⟦9618_w25_32:8(c)⟧）。
- 考官报告指出，得高分的是“一步不漏”地画出每一列的考生（⟦9618_s24_32:5(b)⟧）。合并两步（读入数值后直接画运算结果）会让某个圈对不上。
- − 与 ÷ 方向算反：总是“下面的数 op 上面的数”。
- 变量代错值：先在表达式下写好代入后的数字再画。

#### 代表题精讲　⟦9618_w25_32:8(c)⟧

**在考什么**　讲解时请对照原卷 QP p.8（9 列空栈）与 MS p.14（圈的位置）。The RPN expression `c a / b d – * b +` is to be evaluated, where a = 3, b = 16, c = 9 and d = 6. Show the changing contents of the stack. 4 分。

**完整作答**　代入：`9 3 / 16 6 – * 16 +`，共 9 个记号 → 9 列（下表最上一行是栈顶方向，最下一行是栈底）：

| 读到 | 9 | 3 | / | 16 | 6 | – | * | 16 | + |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| 第 3 格 |  |  |  |  | 6 |  |  |  |  |
| 第 2 格 |  | 3 |  | 16 | 16 | 10 |  | 16 |  |
| 第 1 格（栈底） | 9 | 9 | 3 | 3 | 3 | 3 | 30 | 30 | 46 |

（“读到”一行是给你看的提示，答卷的栈格里只写数字。）

**与 MS 对齐**　MS 的四个圈：第 1–3 列（9 / 9、3 / 3）一圈；第 4–6 列（3、16 / 3、16、6 / 3、10）一圈；第 7 列（30）一圈；第 8–9 列（30、16 / 46）一圈。每圈内各列全对得 1 分，共 4 分。结果 46 = (9 / 3) × (16 − 6) + 16。

**直观**　栈图就是“每读一个记号拍一张快照”：数值让盘子叠高一层，运算符让盘子少一层。快照的张数就是记号的个数。

**下一道变式**　⟦9618_s24_31:5(c)⟧　（`a b - c d + * e /`，a = 17、b = 5、c = 7、d = 3、e = 10；同样 9 列、4 个圈。）

<!-- auto:drills P3-SY-12 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| SY-01 vs P1-SS-01 | 用户界面、驱动怎样“隐藏复杂性”/ 最大化资源 → SY-01；列举 OS 的管理任务 → P1 | hidden from the user · maximise |
| SY-02 vs SY-03 | 多任务、进程状态及转换 → SY-02；为什么要调度、具体调度算法、内核处理中断 → SY-03 | state · ready · blocked 还是 scheduling routine · kernel |
| Ready vs blocked | 能运行、只差 CPU / 在等 I/O 或事件，给 CPU 也不能运行 | waiting for CPU time 还是 waiting for I/O |
| SJF vs SRT | 非抢占，选总时间最短 / 抢占，选剩余时间最短，更短的新进程会替下当前进程 | non-pre-emptive 还是 replaced by the shorter process |
| SY-03 中断 vs HV-02 中断 | 内核、优先级、IDT、保存恢复进程状态 / 处理器流水线、RISC 与 CISC 怎样处理中断 | kernel · low-level scheduling 还是 pipeline · processor |
| Paging vs segmentation | 固定大小的块，由 OS 划分 / 可变大小的块，由编译器算段大小 | fixed 还是 variable |
| Virtual memory vs virtual machine | 磁盘扩展 RAM（SY-04）/ 在一台机器上模拟另一台机器（HV-05） | memory 还是 machine |
| Disk thrashing vs fragmentation | 换页太频繁、磁头忙于换页 / 文件不连续存放 | swapping pages 还是 file blocks |
| SY-05 vs SY-06 | 解释器逐行翻译并执行 / 编译器分阶段生成目标代码 | interpreter 还是 compilation · stage |
| Lexical vs syntax analysis | 切成记号、去空白注释、建符号表 / 按文法检查记号流、产生语法树 | tokens · symbol table 还是 grammar · parse tree |
| SY-07 vs SY-08 vs SY-09 | 判断合法与举例 / 写 BNF / 画语法图 | valid / BNF / draw |
| BNF 的竖线（或）vs 序列 | 竖线只分隔可选项；串联的组成部分直接相邻写 | 选其一还是依次出现 |
| 回环 vs 旁路 | 可以重复（至少一次）/ 可以没有 | one or more 还是 zero or more |
| SY-10 vs SY-11 vs SY-12 | 用文字说为什么、怎样用栈 / 中缀与 RPN 互转 / 画栈或求值 | explain · stack / write in RPN · infix / show the changing contents |
| SY-10 vs CT-05 | 栈怎样求 RPN → SY-10；栈的一般用途、ADT 比较 → CT-05 | RPN 是否出现 |
