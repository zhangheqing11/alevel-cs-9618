## HV　处理器、并行处理与虚拟机 {#ch-HV}

<!-- auto:chapter-stats -->

### 核心思想

HV 对应考纲 15.1，是一章纯“描述题”：没有计算，只有一张流水线时钟图要填。五个题型围绕一个问题——**怎样让计算机更快、更灵活**：

1. **处理器设计**（HV-01、HV-02）：RISC 用少而简单、定长、单周期的指令，硬连线控制器，寄存器多，所以特别适合**流水线**；CISC 指令多而复杂、变长、多周期，微程序控制器。流水线把每条指令分成五个阶段，不同指令的不同阶段在同一时钟周期并行；它也让**中断处理**变复杂（流水线里还有半截的指令）。
2. **并行**（HV-03、HV-04）：Flynn 分类按“指令流 × 数据流”的单 / 多分成 SISD、SIMD、MISD、MIMD；大规模并行计算机是大量处理器 / 计算机联网、同时协同解决同一个问题。
3. **虚拟机**（HV-05）：在宿主机上用软件仿真另一套硬件 / 系统，运行客户操作系统；答好处与局限。注意 virtual machine 与 virtual memory（SY-04）无关。

整章最大的失分点是**拿另一种东西来比**：只问 RISC 特征时写“RISC 比 CISC 快”、写“RISC 没有 …”都不给分（考官报告每年都提）。只问一样就只描述这一样；问区别时才成对写。

| 速查 | RISC | CISC |
|:--|:--|:--|
| 指令集 | 少、简单 | 多、复杂 |
| 指令格式 / 长度 | 格式少、定长 | 格式多、变长 |
| 每条指令的时钟周期 | 一个 | 多个 |
| 寻址方式 | 少 | 多 |
| 寄存器 | 多（通用寄存器） | 少 |
| 控制器 | 硬连线 | 可编程 / 微程序 |
| 流水线 | 容易 | 困难 |
| 设计重心 | 软件（编译器） | 硬件 |

### 题型树
<!-- auto:type-tree -->

### P3-HV-01　RISC 与 CISC 处理器　{#P3-HV-01}

<!-- auto:stats P3-HV-01 -->

**考法**　①描述 RISC 与 CISC 是什么（各 Max 2，共 4 分）；②写出两者的区别（2 分）；③列出 RISC 或 CISC 的四个 / 两个特征（2–4 分）；④勾选表：每行说法属于 RISC 还是 CISC（2 分，全对 2 分、对四行 1 分）。

**识别信号**　Describe what is meant by RISC and CISC processors；Identify two differences between RISC and CISC processors；Identify four features of a RISC / CISC processor；State two features of RISC processors；Tick (✓) one box in each row to show if the statement applies to RISC or CISC processors。

**解题思路**
1. 背熟章首速查表的八行。每行就是一个得分点。
2. **只问一种**（“features of a RISC processor”）：每条只写这一种处理器**有什么**，正面陈述：“uses fixed length instructions”。不写“RISC has fewer … than CISC”，也不写“RISC does not …”。
3. **问区别**：同一行的两端成对写：“RISC has fewer instructions, whereas CISC has more instructions.”每个区别取速查表里不同的一行。
4. **勾选表**：按速查表逐行判断。陷阱句：“uses fewer general-purpose registers”是 CISC；“cache split between data and instructions”按该题 MS 是 RISC。

**得分表述**（引自对应 MS）
- 「uses single-clock cycle instructions」⟦9618_w24_31:2⟧
- 「uses fixed length instructions」⟦9618_w24_31:2⟧
- 「uses many general-purpose registers」⟦9618_w24_31:2⟧
- 「hard-wired control unit」⟦9618_w24_31:2⟧
- 「uses variable length/multi-operation instructions」⟦9618_w24_32:8⟧
- 「RISC has fewer instructions // CISC has more instructions」⟦9618_s22_31:4(b)⟧

**易错与失分**
- 只问一种时拿另一种来比，或写这种处理器“没有什么 / 不擅长什么”：考官报告指出只正面列出该处理器特征的考生才拿分（⟦9618_w24_31:2⟧、⟦9618_w24_32:8⟧、⟦9618_s24_31:11(a)⟧ 的考官报告）。
- “描述 RISC 和 CISC”写成比较：考官报告指出常见错误是去比较两种处理器（⟦9618_s22_31:4(a)⟧ 的考官报告），每边各写自己的两个特征。
- 勾选表靠猜：考官报告指出很多考生错得太多拿不到分（⟦9618_w22_31:10(a)⟧ 的考官报告），全对 2 分、对四行才 1 分。
- 控制器：RISC 硬连线；CISC 写 programmable / micro-programmed（⟦9618_w24_32:8⟧ 的 MS 对 CISC 也列了 hardwired，但最稳的写法是微程序）。

#### 代表题精讲　⟦9618_s22_31:4(a)⟧

**在考什么**　Describe what is meant by RISC and CISC processors. 4 分：RISC max 2（六点任二）、CISC max 2（九点任二）。

**完整作答**
- RISC：使用简单的指令；指令定长；每条指令只需一个时钟周期；使用很多寄存器。
- CISC：指令集很大；使用很多种指令格式、指令变长；指令（转换成子指令后）可能需要多个时钟周期；使用可编程控制器。

**与 MS 对齐**　RISC 四句对应 “Uses simple instructions / Uses fixed length instructions / Instructions only require one clock cycle / Uses many registers”，任二；CISC 四句对应 “Has a large instruction set / Uses many instruction formats / Uses variable length instructions / Instructions (converted to sub-instructions that) may require many clock cycles / Programmable CU”，任二。每边写三四点作保险，每句都只说本处理器自己。

**英文作答句**　RISC: it uses simple instructions of fixed length; each instruction only requires one clock cycle; it uses many registers and a hardwired control unit. CISC: it has a large instruction set and uses many instruction formats with variable length instructions; instructions may require many clock cycles; it uses a programmable control unit.

**直观**　RISC 是一套只有几种简单刀法的厨师：每一刀都一样快，所以几个人可以流水作业；CISC 是会很多复杂招式的厨师：一招顶几刀，但每招用时不同，很难排流水线。

**下一道变式**　⟦9618_w24_31:2⟧　（只问 RISC 的四个特征：四句都正面陈述，不提 CISC。）

<!-- auto:drills P3-HV-01 -->

### P3-HV-02　流水线与中断处理　{#P3-HV-02}

<!-- auto:stats P3-HV-02 -->

**考法**　①描述 RISC 中流水线的用途 / 过程（2–4 分）；②补全流水线时钟周期表：五个阶段 × 若干条指令（4 分）；③概述 RISC 或 CISC 的中断处理过程（3 分）；④解释流水线怎样影响 RISC 的中断处理（3 分）。

**识别信号**　Describe the use of pipelining in Reduced Instruction Set Computers (RISC)；Describe the process of pipelining during the fetch-execute cycle in RISC processors；The processing of instructions is divided into five stages … Complete the table；Outline the process of interrupt handling as it could be applied to RISC or CISC processors；Explain how pipelining affects interrupt handling for RISC processors。

**解题思路**
1. **流水线是什么**：指令被分成五个子任务 / 阶段：取指 IF、译码 ID、取操作数 OF、执行 IE、写回 WB；每个阶段在**一个时钟周期**内完成；不同指令的**不同**阶段可以在同一时钟周期同时进行（同一阶段同一周期只能有一条指令）→ 多条指令同时处理，单位时间完成的指令数（吞吐量）提高。
2. **填时钟周期表**：第 n 条指令的第 k 个阶段放在第 n + k − 1 个周期。整张表是一条斜带：第 1 条指令在周期 1–5、第 2 条在 2–6……第 6 条在 6–10。每格写清是哪条指令（1、2 … 或 A、B …）。
3. **一般中断处理**：处理器在取指—执行周期开始 / 结束时检测中断 → 当前程序暂停，各寄存器内容保存到栈 → 执行中断服务程序 ISR → 从栈恢复寄存器，继续原程序。
4. **流水线对中断的影响**：收到中断时流水线里还有几条做了一半的指令，增加了复杂性 → 通常把正在进行的指令丢弃，只保留最后一条（已在写回阶段的那条）→ 对剩下这条指令应用中断处理程序 → 中断处理完后处理器从顺序里的下一条指令重新开始。

**得分表述**（引自对应 MS）
- 「Pipelining allows several instructions to be processed simultaneously / concurrently」⟦9618_s23_32:8(a)⟧
- 「Each subtask is completed during one clock cycle」⟦9618_w22_31:10(b)⟧
- 「No two instructions can execute their same stage at the same clock cycle」⟦9618_w22_31:10(b)⟧
- 「First instruction successfully completed over five clock cycles」⟦9618_s23_32:8(b)⟧
- 「… the current program is temporarily stopped and the status of each register stored on the stack」⟦9618_s24_31:11(b)⟧
- 「All the instructions currently in operation are usually discarded except for the last one/the one at write back」⟦9618_s24_31:11(c)⟧

**易错与失分**
- 流水线描述只写“几条指令同时处理”：考官报告指出要在此基础上展开（⟦9618_s23_32:8(a)⟧ 的考官报告）——加上“因此吞吐量提高”“每阶段一个时钟周期”“例如一条在译码时下一条在取指”。
- 填表时没标清每格是哪条指令，或在某一行多填了格：考官报告指出答案必须清楚标出六条指令各自经过五个阶段（⟦9618_s23_32:8(b)⟧ 的考官报告）；MS 有一分专给“no extra instruction sections added on any row”。
- 中断处理只要求一般过程（⟦9618_s24_31:11(b)⟧ 的考官报告），不必扯 RISC / CISC 的区别；“流水线怎样影响中断”考官报告指出高分少见（⟦9618_s24_31:11(c)⟧ 的考官报告），记住“丢弃、保留写回那条、处理、从下一条重启”四步。

#### 代表题精讲　⟦9618_s23_32:8(b)⟧

**在考什么**　指令分五个阶段 IF、ID、OF、IE、WB，每个阶段用不同的寄存器。Complete the table to show how a program consisting of six instructions would be completed using pipelining. 4 分。讲解时请对照原卷 QP p.9 的表格（行 = 五个处理器阶段，列 = 时钟周期 1–12）。

**完整作答**　第 n 条指令的第 k 阶段填在周期 n + k − 1：

| 阶段 \ 周期 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| IF | 1 | 2 | 3 | 4 | 5 | 6 | | | | | | |
| ID | | 1 | 2 | 3 | 4 | 5 | 6 | | | | | |
| OF | | | 1 | 2 | 3 | 4 | 5 | 6 | | | | |
| IE | | | | 1 | 2 | 3 | 4 | 5 | 6 | | | |
| WB | | | | | 1 | 2 | 3 | 4 | 5 | 6 | | |

六条指令在第 10 个周期全部完成，周期 11、12 空着。

**与 MS 对齐**　四点：「First stage of first instruction in first clock cycle」⟦9618_s23_32:8(b)⟧（IF 行周期 1 填 1）；“First instruction successfully completed over five clock cycles”（指令 1 占周期 1–5 的斜线）；“Remaining instructions completed over ten clock cycles …”（最后一条在周期 10 写回）；“… with no extra instruction sections added on any row”（每行恰好六格）。MS 的范例用 1.1、1.2 … 或 A、B …标记，只要能分清六条指令即可。

**直观**　洗衣房有洗、甩、烘、叠、装五个工位：第一筐衣服洗完去甩干时，第二筐就进洗衣机。每个工位每一轮只处理一筐，但五个工位同时在忙。

**下一道变式**　⟦9618_s24_31:11(b)⟧　（中断处理的一般过程：检测 → 寄存器入栈 → 执行 ISR → 恢复寄存器，3 分。）

<!-- auto:drills P3-HV-02 -->

### P3-HV-03　四种基本计算机体系结构　{#P3-HV-03}

<!-- auto:stats P3-HV-03 -->

**考法**　①题目给出 SISD，说出并描述其余三种（每种名称 1 分 + 描述 1 分，6 分）；②描述其中两种的特征（各 Max 2，4 分）；③说出两种之间的一个区别、一个相同点（2 分）。

**识别信号**　There are four basic categories of computer architecture … Identify the three other categories … Describe each category；Describe the features of SISD and MIMD / SIMD and MISD computer architectures；State one difference and one similarity between …。

**解题思路**
1. **名字就是定义**：S = single、M = multiple，I = instruction、D = data。
   - **SISD**：单指令流、单数据流；一个处理器（加一个控制器、一个存储单元），按顺序执行指令。
   - **SIMD**：单指令、多数据；许多（阵列）处理器对**不同**数据集同时执行**同一条**指令；属多处理器并行计算机，可利用流水线。
   - **MISD**：多指令、单数据；许多处理器对**同一个**数据流各自执行**不同**指令。
   - **MIMD**：多指令、多数据；许多处理器各自独立（异步）地对不同数据执行不同指令。
2. 描述题每种写两点：**全称展开 + 说明（几个处理器、做什么）**，再加一个特点（SISD 顺序执行；SIMD 并行 / 流水线；MIMD 处理器独立异步运行）。
3. 相同点：SIMD、MISD 都是并行系统、都用多个处理器；区别：同一指令 vs 不同指令、多数据流 vs 同一数据流。

**得分表述**（引自对应 MS）
- 「SIMD (1) many/array processors execute the same instruction using different data sets」⟦9618_s22_32:5⟧
- 「MISD (1) many processors (using different instructions) use the same data set」⟦9618_s22_32:5⟧
- 「MIMD (1) many processors (using different instructions) using different data sets」⟦9618_s22_32:5⟧
- 「Contains one processor, a control unit and a memory unit」⟦9618_w23_31:5⟧
- 「…that operate asynchronously / independently」⟦9618_w23_31:5⟧

**易错与失分**
- 只把缩写展开、不描述：考官报告指出能说出类别的人多，能给出合格描述的人少（⟦9618_s22_32:5⟧ 的考官报告）。展开之后要说“几个处理器、同一 / 不同指令、同一 / 不同数据”。
- MIMD 只写“multiple instruction multiple data”：考官报告指出很少有人补上“包含许多独立运行的处理器”（⟦9618_w23_31:5⟧ 的考官报告）。
- SIMD / MISD 写不到第二分：考官报告指出很少有人写出“都是多处理器的并行计算机”或“SIMD 可利用流水线”（⟦9618_w23_32:10⟧ 的考官报告）。
- 把 SIMD 与 MISD 的“同一 / 不同”弄反：SIMD 是同一指令、不同数据；MISD 是不同指令、同一数据。

#### 代表题精讲　⟦9618_s22_32:5⟧

**在考什么**　There are four basic categories of computer architecture. Single Instruction Single Data (SISD) is one architecture. Identify the three other categories of computer architecture. Describe each category that you identify. 6 分：每种名称 1 分 + 描述 1 分。

**完整作答**
1. SIMD（Single Instruction Multiple Data）：许多（阵列）处理器用不同的数据集执行同一条指令。
2. MISD（Multiple Instruction Single Data）：许多处理器各自执行不同的指令，作用于同一个数据集。
3. MIMD（Multiple Instruction Multiple Data）：许多处理器各自执行不同的指令，作用于不同的数据集。

**与 MS 对齐**　MS 每行“名称 (1) + 描述 (1)”：SIMD「many/array processors execute the same instruction using different data sets」⟦9618_s22_32:5⟧、MISD「many processors (using different instructions) use the same data set」⟦9618_s22_32:5⟧、MIMD「many processors (using different instructions) using different data sets」⟦9618_s22_32:5⟧——三行各 2 分。描述必须同时说清“指令同 / 异”和“数据同 / 异”，并说出是“many processors”。

**英文作答句**　SIMD (Single Instruction Multiple Data): many / array processors execute the same instruction using different data sets. MISD (Multiple Instruction Single Data): many processors, using different instructions, use the same data set. MIMD (Multiple Instruction Multiple Data): many processors, using different instructions, use different data sets.

**直观**　SIMD 像全班听同一个口令、各做各的题（同一指令、不同数据）；MISD 像几个老师用不同方法批同一份卷子；MIMD 像几个小组各做各的项目。

**下一道变式**　⟦9618_w23_32:10⟧　（描述 SIMD 与 MISD 的特征，各 Max 2：展开 + “多处理器并行计算机”，SIMD 还可写流水线。）

<!-- auto:drills P3-HV-03 -->

### P3-HV-04　大规模并行计算机　{#P3-HV-04}

<!-- auto:stats P3-HV-04 -->

**考法**　概述 / 描述大规模并行计算机的特征，3 分。核验语料只有 2 次（另一次在 s26），考纲 15.1 单独列出，写法固定。

**识别信号**　Outline / Describe the characteristics of massively parallel computers。

**解题思路**　三四句，每句一个特征：
1. **大量**处理器或独立的计算机连在一起（形成一台更强大的“单一机器”）。
2. 它们**同时**进行一组协调的计算——协同处理同一个问题，每个处理器负责问题的一部分。
3. 通过**网络基础设施**（互连的数据通路）连接。
4. 处理器之间用**消息接口**、发消息的方式通信（或通过共享的内存池）。

**得分表述**（引自对应 MS）
- 「A large number of computer processors / separate computers connected together」⟦9618_s23_31:8⟧
- 「… simultaneously performing a set of coordinated computations // collaborative processing」⟦9618_s23_31:8⟧
- 「network infrastructure」⟦9618_s23_31:8⟧
- 「communicate using a message interface / by sending messages」⟦9618_s23_31:8⟧

**易错与失分**
- 只写“many processors”就停：考官报告指出拿满分的答案写出了“大量处理器协同工作、用网络基础设施连接”（⟦9618_s23_31:8⟧ 的考官报告）。
- 与 MIMD 混写：MIMD 是 Flynn 分类里的一类，题目问大规模并行计算机时不要改答 Flynn 分类。

#### 代表题精讲　⟦9618_s23_31:8⟧

**在考什么**　Outline the characteristics of massively parallel computers. 3 分，MS 四点 Max 3。

**完整作答**
1. 大量的计算机处理器或独立的计算机连接在一起。
2. 它们同时进行一组协调的计算（协同处理）。
3. 依靠网络基础设施连接。
4. 处理器之间通过消息接口、发送消息来通信。

**与 MS 对齐**　1–4 依次对应 MP1–MP4，任 3 点满分。

**英文作答句**　A massively parallel computer has a large number of computer processors or separate computers connected together, simultaneously performing a set of coordinated computations. They are connected by a network infrastructure and communicate using a message interface, by sending messages.

**直观**　像一千个工人同时盖一座楼：每人负责一小块，靠对讲机（网络、消息）互相协调。

**下一道变式**　核验语料里另一道同型题在 s26（⟦9618_s26_33:4(a)⟧，留作考前模考，专项练习时不做）；2022–25 没有第二道。可用 ⟦9618_w23_31:5⟧ 的 MIMD 描述作对比练习：说清 MIMD 与大规模并行计算机各强调什么。

<!-- auto:drills P3-HV-04 -->

### P3-HV-05　虚拟机　{#P3-HV-05}

<!-- auto:stats P3-HV-05 -->

**考法**　①解释 / 描述虚拟机是什么（2–4 分）；②给出好处与局限（两个好处 + 一两个局限，每点 1 分；s22 那道每点“说明 + 展开”2 分）；③说明宿主操作系统与客户操作系统的角色（3 分）。常组合成 6 分题：描述 + 两好处 + 两缺点。

**识别信号**　Explain / Describe what is meant by (the term) virtual machine；Describe two benefits and one limitation of using a virtual machine；Outline two benefits and two limitations of a virtual machine；Explain the roles of the host operating system and the guest operating system。

**解题思路**
1. **是什么**：在一台宿主计算机上用软件**仿真**另一套计算机系统（硬件和 / 或软件）；被仿真的系统上运行**客户操作系统**。
2. **好处**（每条写成“能做什么 + 为什么有用”）：
   - 兼容：同一台计算机上可以有多个客户 OS / 多台虚拟机；能运行与宿主不兼容的旧软件（legacy）；能仿真不同的指令集。
   - 保护：虚拟机崩溃不影响宿主；可疑软件只会感染虚拟机。
   - 成本：不用另买硬件来测试新系统 / 应用。
3. **局限**：性能下降（多了一层代码，间接访问硬件，资源与宿主共享）；性能 / 响应时间无法准确测量；受宿主机的能力和弱点限制；有些硬件无法仿真；建立和维护复杂、费钱。
4. **宿主 OS 与客户 OS**：宿主 OS 是宿主机本来的操作系统，控制宿主机的全部（物理）资源，提供操作虚拟机软件的界面并运行虚拟机软件；客户 OS 在虚拟机里运行，控制被仿真的虚拟硬件 / 软件，经虚拟机和宿主 OS 间接访问真实硬件，受宿主 OS 控制。

**得分表述**（引自对应 MS）
- 「The emulation of a computer system / hardware and/or software」⟦9618_w22_32:5⟧
- 「… using a host computer system」⟦9618_w22_32:5⟧
- 「A virtual machine can crash without affecting the host machine」⟦9618_w22_32:5⟧
- 「Cost savings due to not needing to purchase extra hardware」⟦9618_w22_32:5⟧
- 「Performance of the guest system cannot be adequately measured」⟦9618_w22_32:5⟧
- 「The guest operating system runs under the control of the host operating system」⟦9618_s24_32:9(b)⟧

**易错与失分**
- 把虚拟机当成虚拟内存来答：考官报告每次都点到这一错误（⟦9618_w22_32:5⟧、⟦9618_s24_32:9(a)⟧ 的考官报告）。
- 两个好处其实是一件事：考官报告指出写出两个**不同**好处、两个**不同**局限的考生得分最多（⟦9618_s24_32:9(a)⟧ 的考官报告）。可按 MS 的分类（兼容 / 保护 / 成本；性能 / 复杂 / 软硬件问题）各取一类。
- 每点 2 分的题（⟦9618_s22_31:6⟧）只写半句：那道 MS 是“说明 (1) + 展开 (1)”，例如“新系统可在不同的虚拟硬件上试用 (1)，不必购买这些硬件 (1)”。

#### 代表题精讲　⟦9618_w22_32:5⟧

**在考什么**　Describe what is meant by a virtual machine. Include in your answer two benefits and two drawbacks of using a virtual machine. 6 分：描述 Max 2、好处 Max 2、缺点 Max 2。

**完整作答**
- Description：虚拟机是用宿主计算机系统对另一个计算机系统（硬件和 / 或软件）的仿真；仿真中使用客户操作系统。
- Benefit 1：同一台计算机上可以使用多个客户操作系统 / 多台虚拟机。
- Benefit 2：虚拟机崩溃时不会影响宿主机。
- Drawback 1：由于给宿主机增加了额外负担，虚拟机比真实机器效率低、性能差。
- Drawback 2：客户系统的性能无法被准确测量。

**与 MS 对齐**　描述两句对应「The emulation of a computer system / hardware and/or software」⟦9618_w22_32:5⟧ 与「… using a host computer system」⟦9618_w22_32:5⟧（第三点 “Using guest operating system(s) for emulation” 是保险）；两个好处、两个缺点各对应 MS 列表里不同的一条。三组各封顶 2 分。

**英文作答句**　A virtual machine is the emulation of a computer system (hardware and / or software) using a host computer system, with guest operating systems used for the emulation. Benefits: multiple guest operating systems can be used on the same computer; a virtual machine can crash without affecting the host machine. Drawbacks: a virtual machine has poorer performance than a real machine because of the extra load on the host computer; the performance of the guest system cannot be adequately measured.

**直观**　虚拟机像在自己家（宿主）里搭了一间“样板房”：可以在里面试装各种家具（客户 OS），砸坏了也不伤到真房子；但样板房的水电都从真房子接，用起来没有真房子那么快。

**下一道变式**　⟦9618_s24_32:9(b)⟧　（换成宿主 OS 与客户 OS 的角色，各 Max 2：谁控制真实资源、谁运行在虚拟机里。）

<!-- auto:drills P3-HV-05 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| HV-01 vs HV-02 | 只问 RISC / CISC 的特征与区别 → HV-01；问流水线、中断处理 → HV-02 | 题干有没有 pipelining / interrupt |
| “features of RISC” vs “differences” | 特征题只正面写一种；区别题成对写两种 | features / describe 还是 differences / compare |
| HV-02 中断 vs SY-03 中断 | 处理器层面（取指—执行周期、流水线里的指令）→ HV-02；OS 内核作为中断处理程序、调度 → SY-03 | 题干提 RISC / CISC / pipelining 还是 OS / kernel / scheduling |
| SIMD vs MISD | SIMD：同一指令、不同数据；MISD：不同指令、同一数据 | 看 I 和 D 前面是 S 还是 M |
| HV-03 MIMD vs HV-04 大规模并行 | MIMD 是 Flynn 分类的一类；大规模并行计算机讲大量处理器联网协同、发消息通信 | 题干是 “categories of computer architecture” 还是 “massively parallel computers” |
| Virtual machine vs virtual memory | 虚拟机（HV-05）仿真另一套系统；虚拟内存（SY-04）用辅存扩充主存 | machine 还是 memory |
| 宿主 OS vs 客户 OS | 宿主 OS 控制真实硬件并运行虚拟机软件；客户 OS 在虚拟机里运行、控制虚拟硬件 | host 还是 guest |
