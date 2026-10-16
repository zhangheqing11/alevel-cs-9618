## PF　处理器基础 {#ch-PF}

<!-- auto:chapter-stats -->

### 核心思想

这一章回答：**一条指令是怎样被处理器取来、看懂、执行的，以及我们怎样用最底层的指令直接摆弄寄存器里的位**。题型分三段：

1. **硬件结构**（PF-01 至 PF-06）：冯·诺依曼模型——程序和数据放在同一个存储器里（PF-01）；CPU 里的寄存器各管一件事（PF-02）；它们按固定顺序配合完成取指-执行周期（PF-03）；周期之间插空处理中断（PF-04）；什么能让这一切更快（PF-05）；外设从哪里接进来（PF-06）。
2. **汇编语言**（PF-07 至 PF-10）：汇编器怎样把助记符变成机器码、指令分几组（PF-07）；操作数怎样找到真正的数据——寻址方式（PF-08）；按寻址方式算单条/几条指令后的 ACC（PF-09）；带跳转与循环的完整程序跟踪（PF-10）。
3. **位操作**（PF-11 至 PF-13）：整体移位（PF-11）；与掩码逐位 AND/OR/XOR（PF-12）；反过来，为了测试/置位/清零某一位而选择掩码（PF-13）。

**汇编题的共同底稿**——题目每次都会印出指令表，但读表的规则不变，必须熟到不用想：

| 记号 | 含义 | 例 |
|:--|:--|:--|
| `#n` | 十进制数本身（立即数） | `LDM #12`：ACC ← 12 |
| `Bn` | 二进制数本身 | `AND B00001111` |
| `&n` | 十六进制数本身 | `XOR &F1` |
| `<address>`（不带记号的数） | **地址**，要去内存表里取它的内容 | `ADD 54`：ACC ← ACC + [54] |

| 指令 | 作用 | 寻址 |
|:--|:--|:--|
| `LDM #n` | ACC ← n | 立即 |
| `LDD a` | ACC ← [a] | 直接 |
| `LDI a` | ACC ← [[a]]（先取 a 里的地址，再取那个地址的内容） | 间接 |
| `LDX a` | ACC ← [a + IX] | 变址 |
| `LDR #n` | IX ← n | 立即 |
| `STO a` | [a] ← ACC（**ACC 不变**，改的是内存） | 直接 |
| `ADD`/`SUB #n`、`ADD`/`SUB a` | ACC ← ACC ± n 或 ACC ± [a] | 立即 / 直接 |
| `INC`/`DEC ACC` 或 `IX` | 该寄存器 ± 1 | — |
| `CMP #n` / `CMP a` / `CMI a` | 比较 ACC 与 n / [a] / [[a]]，**ACC 不变** | 立即 / 直接 / 间接 |
| `JPE a` / `JPN a` / `JMP a` | 比较为真时跳 / 比较为假时跳 / 无条件跳 | — |
| `IN` / `OUT` | 输入一个字符，把其 ASCII 码放进 ACC / 输出 ACC 中 ASCII 码对应的字符 | — |
| `AND`/`OR`/`XOR`、`LSL`/`LSR #n` | 按位运算 / 逻辑移位，结果放回 ACC | 立即 / 直接 |

记号 `[a]` 读作“地址 a 里的内容”。这是 PF-03 的寄存器传送记法和 PF-08～PF-10 的追踪共用的语言。

### 题型树
<!-- auto:type-tree -->

### P1-PF-01　冯·诺依曼模型、CPU 部件与总线　{#P1-PF-01}

<!-- auto:stats P1-PF-01 -->

**考法**　①存储程序概念是什么；②CU、系统时钟、ALU、IAS 的作用，或 CU 与时钟/控制总线怎样协作（2–4 分）；③除寄存器和总线外，冯·诺依曼模型的其他部件；④地址总线、数据总线、控制总线各传什么（常放在“向外设写数据”的情境里）；⑤控制总线能传的信号；⑥勾选每个部件用哪条总线。

**识别信号**　stored program concept；Von Neumann model；purpose of the Control Unit (CU) / system clock / Immediate Access Store (IAS)；Explain how the CU, system clock and control bus operate；address bus / data bus / control bus；types of signal that a control bus can transfer。

**解题思路**
1. **存储程序概念**一句话：指令和数据存在同一个（主）存储器里。
2. **部件分工**：
   - CU：取指、译码、管理指令的执行顺序；通过控制总线发出/接收控制信号；协调 CPU 内其他部件。
   - 系统时钟：产生定时信号（经控制总线）→ 使各部件的操作同步。
   - ALU：做算术运算与逻辑运算（含比较）。
   - IAS（立即存取存储器，即主存）：存放当前正在使用的程序与数据；易失；访问快。
3. **CU + 时钟 + 控制总线**协作题按“时钟发定时信号 → 经控制总线 → 使部件同步；CU 发起数据传送 → 在控制总线上发信号给其他部件”四步写。
4. **三条总线**：地址总线传**地址**（单向，CPU → 内存/设备）；数据总线传**数据/指令**（双向）；控制总线传**控制信号**（双向）：读、写、中断、时钟信号。
5. 勾选题：系统时钟 → 控制总线；MAR → 地址总线；MDR → 数据总线。

**得分表述**（引自对应 MS）
- 「Instructions and data are stored in the same memory space / in main memory」⟦9618_w22_11:5(a)⟧
- 「The system clock gives out timing signals」⟦9618_s23_13:7(b)⟧
- 「to synchronise the other system components」⟦9618_s23_13:7(b)⟧
- 「The Control Unit initiates data transfer」⟦9618_s23_13:7(b)⟧
- 「to manage the execution of instructions (in sequence)」⟦9618_w22_11:5(b)(iii)⟧
- 「The address of the data to be written to the device (in RAM) is carried on the address bus」⟦9618_w23_12:8(c)(ii)⟧

**易错与失分**
- “The CU sends signals on the **data** bus”：控制信号走**控制总线**（⟦9618_s25_12:1(a)⟧ 正是要你改正这句话）。
- “system clock keeps the time”只是附带点；核心是“产生定时信号、使操作同步”。
- 列冯·诺依曼部件时又写了寄存器或总线：题目说了 Do not include。
- 数据总线写成“carries addresses”或地址总线写成“carries data”：分不清就记“MAR 接地址总线、MDR 接数据总线”。

#### 代表题精讲　⟦9618_s23_13:7(b)⟧

**在考什么**　Explain how the CU, system clock and control bus operate to transfer data between the components of the computer system. 4 分，MS 5 点取 4。考你能否把三个部件串成一条因果链。

**完整作答**　系统时钟发出定时信号；这些信号经控制总线传给各部件，使系统中其他部件的操作同步。控制单元负责发起数据传送：它产生控制信号（如读、写），经控制总线发给其他部件，告诉它们何时、怎样传送数据。

**与 MS 对齐**　“The system clock gives out timing signals”→“… which are sent on the control bus”→“…to synchronise the other system components”→“The Control Unit initiates data transfer”→“…by generating signals that are sent on the control bus to other components”，任取 4 点。

**英文作答句**　The system clock gives out timing signals, which are sent on the control bus to synchronise the other system components. The Control Unit initiates data transfer by generating signals that are sent on the control bus to other components.

**直观**　时钟是乐队的节拍器，CU 是指挥，控制总线是指挥手里的指挥棒——节拍器定拍子，指挥按拍子示意谁该动。

**下一道变式**　⟦9618_w23_12:8(c)(ii)⟧　（换成地址总线、数据总线与缓冲区在写光盘时的作用。）

<!-- auto:drills P1-PF-01 -->

### P1-PF-02　寄存器的作用　{#P1-PF-02}

<!-- auto:stats P1-PF-02 -->

**考法**　①写出给定寄存器（PC、MAR、MDR、IX、ACC、CIR、SR）的作用，常为填表；②已给几个寄存器，再说出另外两个专用寄存器及作用；③通用寄存器与专用寄存器的两个区别；④六句陈述中找出三句错的并改正。

**识别信号**　State / Describe the role / purpose of the following registers；Identify two other special purpose registers；differences between general purpose registers and special purpose registers；Three of the statements are incorrect。

**解题思路**
1. 背熟“一个寄存器 = 一句话”，注意装的是**地址**还是**数据/指令**：

| 寄存器 | 装什么 |
|:--|:--|
| PC 程序计数器 | **下一条**要取的指令的**地址** |
| MAR 存储器地址寄存器 | 将要读/写的内存单元的**地址** |
| MDR 存储器数据寄存器 | 刚从 MAR 所指地址读出的、或将要写入那里的**数据/指令** |
| CIR 当前指令寄存器 | **当前**正在译码/执行的**指令** |
| ACC 累加器 | 算术与逻辑运算的（中间）结果 |
| IX 变址寄存器 | 一个数，加到操作数上得到实际地址 |
| SR 状态寄存器 | 各个标志位（进位、溢出、零、负、中断等），运算后被置位/清零 |

2. 通用 vs 专用：专用寄存器各有指定的用途、保存程序执行的状态；通用寄存器可用于程序员定义的任何用途、在运算中暂存数据。
3. 改错题：逐句对照上表，错处常在“地址 vs 内容”（PC 存的是下一条指令的**地址**，不是指令）、“哪条总线”（CU 用控制总线）、“方向”（MDR 存要写入 MAR 所指地址的数据，不是“把数据传到 MAR”）。

**得分表述**（引自对应 MS）
- 「to store the address / location / memory location of the next instruction to be fetched」⟦9618_w22_11:5(b)(i)⟧
- 「holds address in memory from which data will be read / to which data will be written」⟦9618_w22_13:4(a)(i)⟧
- 「holds the data/instructions which has been read from or is to be written to the address in the MAR」⟦9618_w22_13:4(a)(i)⟧
- 「holds the instruction currently being decoded and/or executed」⟦9618_w23_11:5(a)⟧
- 「to store a value that is added to an address to give another address」⟦9618_w22_11:5(b)(i)⟧
- 「Special purpose registers are specialised for a specific use, whereas general purpose registers are used for any purpose」⟦9618_w23_13:9(a)(ii)⟧

**易错与失分**
- “PC stores the next instruction”：错，是下一条指令的**地址**。这是改错题的常客。
- “MAR stores data”：MAR 只放地址。
- 已给的寄存器（如 MDR、IX、ACC）又写一遍：不得分。
- SR 只写“stores the status”：要具体到“存放标志位，标志在算术/逻辑运算后被置位或清零，可被检查以决定是否改变执行顺序”。

#### 代表题精讲　⟦9618_w24_12:3(a)⟧

**在考什么**　Complete the table by describing the purpose of each of the given registers：PC、MAR、MDR、IX。4 分，每个 1 分（讲解时请对照原卷 QP p.4 的表格）。

**完整作答**

| Register | Purpose |
|:--|:--|
| PC | 存放下一条要取（执行）的指令的地址 |
| MAR | 存放将要读出或写入数据的那个内存单元的地址 |
| MDR | 存放从 MAR 所指地址读出的数据，或将要写入 MAR 所指地址的数据 |
| IX | 存放一个数，它加到操作数上，形成数据的地址 |

**与 MS 对齐**　四格分别对应 MS 的“Stores the address of the next instruction to be fetched/executed”“Stores the address of the memory location where data will be read from/written to”“Stores the data read from the address in the MAR // stores the data to be written to the address in the MAR”“Stores a number that will be added to the operand, to form the address of the data”。

**英文作答句**　PC: stores the address of the next instruction to be fetched. MAR: stores the address of the memory location where data will be read from or written to. MDR: stores the data read from, or to be written to, the address in the MAR. IX: stores a number that is added to the operand to form the address of the data.

**直观**　去图书馆借书：PC 是“下一本要借的书的索书号”，MAR 是“正在找的书架号”，MDR 是“刚从书架上拿下来的书”，CIR 是“正在读的那本”。

**下一道变式**　⟦9618_s25_12:1(a)⟧　（改错题：六句里找出三句错的并改正。）

<!-- auto:drills P1-PF-02 -->

### P1-PF-03　取指-执行周期　{#P1-PF-03}

<!-- auto:stats P1-PF-03 -->

**考法**　①用文字描述各寄存器在 F-E 周期中的作用（4–5 分）；②用寄存器传送记法（RTN）写出取指阶段的全部步骤；③给 RTN 写描述，或给描述写 RTN（填表）；④找出 RTN 里的错误；⑤只问 MAR/MDR 在周期中的作用。

**识别信号**　Fetch-Execute (F-E) cycle；register transfer notation；MAR ← [PC]、MDR ← [[MAR]]；Describe the role of the registers in the F-E cycle；Complete the table by writing the missing steps。

**解题思路**
1. 取指阶段只有四步，顺序固定，**背下 RTN 和对应的英文句**：

| 步 | RTN | 含义 |
|:--|:--|:--|
| 1 | `MAR ← [PC]` | 把 PC 的内容（下一条指令的地址）复制到 MAR |
| 2 | `PC ← [PC] + 1` | PC 加 1，指向再下一条指令 |
| 3 | `MDR ← [[MAR]]` | 把 MAR 所指地址里的内容（指令）复制到 MDR |
| 4 | `CIR ← [MDR]` | 把 MDR 的内容复制到 CIR，随后译码、执行 |

   第 2 步可以与第 1 步同时（MS 常写成“MAR ← [PC] and PC ← [PC] + 1”同一分），但必须在第 1 步**之后**或同时，不能在之前。
2. 读 RTN：`[X]` = X 的内容；`[[MAR]]` = 以 MAR 的内容为地址的那个内存单元的内容（双层括号 = 间接一次）。
3. 文字描述题：按上面四步各写一句，再补“CIR 中的指令被 CU 译码并执行”；5 分题还要写“PC 每个周期递增/改变”。
4. 改错题：逐行检查箭头左边是否是正确的目标寄存器、右边括号层数是否正确（MDR 一行必须是两层括号）。

**得分表述**（引自对应 MS）
- 「The contents of the PC are copied to the MAR」⟦9618_s22_13:2(a)⟧
- 「Address in PC is incremented」⟦9618_s22_13:2(a)⟧
- 「The data in the address held in the MAR is copied to the MDR」⟦9618_s22_13:2(a)⟧
- 「The contents of MDR are copied into CIR」⟦9618_w23_13:9(b)⟧
- 「The address is received from the Program Counter (PC)」⟦9618_w25_13:6(b)⟧
- 「The instruction passes to the CIR for decoding and executing」⟦9618_w25_13:6(b)⟧

**易错与失分**
- `MDR ← [MAR]`（少一层括号）：那是把地址本身放进 MDR，错。
- `PC ← PC + 1`（右边没括号）：RTN 要写 `[PC] + 1`。
- 顺序题把“PC 加 1”放在“MAR ← [PC]”之前：会取到错误的指令。⟦9618_s25_13:2(a)(ii)⟧ 有一分专给“Correct order”。
- 文字题写“PC holds the next instruction”：仍是 PF-02 那个坑，PC 存地址。

#### 代表题精讲　⟦9618_w23_13:9(b)⟧

**在考什么**　一张不完整的表列出 F-E 周期的步骤（RTN）和描述，补全缺的两个 RTN 和两个描述，4 分（讲解时请对照原卷 QP p.14 的表格；表中各行的排列不是周期顺序）。

**完整作答**

| Step | Description |
|:--|:--|
| `PC ← [PC] + 1` | The address in PC is incremented.（已给） |
| `MDR ← [[MAR]]`（已给） | MAR 所指地址中的数据被复制到 MDR |
| `MAR ← [PC]`（已给） | PC 的内容被复制到 MAR |
| `CIR ← [MDR]` | The contents of MDR are copied into CIR.（已给） |

**与 MS 对齐**　四个空格各 1 分：补的 RTN 是 `PC ← [PC] + 1` 与 `CIR ← [MDR]`；补的描述是“The data in the location pointed to by the MAR is copied to the MDR”与“The contents of PC are copied to the MAR”。

**英文作答句**　The data in the location pointed to by the MAR is copied to the MDR. The contents of the PC are copied to the MAR.

**直观**　PC 报出地址 → MAR 拿着地址去内存 → 内存把东西交给 MDR → MDR 转交给 CIR 去执行。四个人传一封信，每人只做一件事。

**下一道变式**　⟦9618_s25_13:2(a)(ii)⟧　（不给任何提示，用 RTN 按顺序写出全部取指步骤，4 分里有 1 分专给顺序。）

<!-- auto:drills P1-PF-03 -->

### P1-PF-04　中断　{#P1-PF-04}

<!-- auto:stats P1-PF-04 -->

**考法**　①中断的目的；②软件中断/硬件中断的原因举例；③在 F-E 周期的什么时候检测中断；④解释中断怎样被检测和处理（4–5 分，最常见，有时放在“按下键盘”这样的具体情境里）；⑤给出步骤表，把缺的步骤（字母）填到正确位置。

**识别信号**　interrupt；Interrupt Service Routine (ISR)；Explain how the computer handles this interrupt；State when interrupts are detected during the F-E cycle；causes of a software interrupt。

**解题思路**
1. **目的**：设备或进程发出信号，请求处理器的注意。
2. **原因**：硬件——按键、鼠标移动、打印机缺纸、设备传输完成、电源故障；软件——除以零、运行时错误、访问非法内存位置、数组越界、栈溢出、程序请求外部设备输入。
3. **何时检测**：每个 F-E 周期**结束时**（下一个周期开始前），检查中断寄存器。
4. **处理流程**（背成一条链，按分值写够点数）：
   1. 中断标志在中断寄存器中被置位；
   2. 在当前 F-E 周期结束时检查中断寄存器；
   3. 比较优先级：若低于当前进程，继续执行当前进程；
   4. 若更高：把当前寄存器内容（进程状态）保存到栈上；
   5. 识别中断源，把对应 ISR 的地址装入 PC，调用 ISR 处理中断（情境题写具体：处理键盘输入的数据）；
   6. ISR 结束后再检查是否有更高优先级的中断；
   7. 没有则从栈中恢复寄存器内容，继续原进程的下一个 F-E 周期。

**得分表述**（引自对应 MS）
- 「to send a signal from a device or process」⟦9618_w22_11:5(c)⟧
- 「seeking the attention of the processor」⟦9618_w22_11:5(c)⟧
- 「At the start / end of FE cycle the interrupt register is checked」⟦9618_s25_12:1(c)⟧
- 「The priority of any interrupts waiting is checked」⟦9618_s25_12:1(c)⟧
- 「the contents of the registers are stored on the stack」⟦9618_s25_12:1(c)⟧
- 「if no more interrupts of higher priority, the register contents are restored and the next FE cycle continues」⟦9618_s25_12:1(c)⟧

**易错与失分**
- 写“the CPU stops immediately”：中断要等当前 F-E 周期**执行完**才检测。
- 漏掉“比较优先级”：这是处理流程里最容易丢的一分；而且要写低优先级时怎么办。
- 只写“the registers are saved”不写去哪：写“on the stack”。
- 情境题不扣情境：⟦9618_s23_11:6⟧ 的 MS 有“The appropriate interrupt service routine (ISR) for the key press is called”“The input data from the keyboard is processed”。
- 软件中断举成“keyboard key pressed”：那是硬件中断。

#### 代表题精讲　⟦9618_s23_11:6⟧

**在考什么**　An interrupt is generated when a key is pressed on a computer keyboard. Explain how the computer handles this interrupt. 5 分，MS 8 点取 5。

**完整作答**
1. 按键使中断寄存器中的中断标志被置位。
2. 在当前 F-E 周期结束时（下一个周期开始前），系统检查中断寄存器。
3. 检查是否有比当前进程优先级更高的中断。
4. 如果有，把当前寄存器的内容保存到栈上。
5. 调用处理按键的中断服务程序 ISR，处理来自键盘的输入数据。
6. ISR 完成后，从栈中恢复寄存器内容，控制权交回原来的进程。

**与 MS 对齐**　“An interrupt flag is raised in the (interrupt) register”→“At the end of the current FE cycle”→“The system checks the interrupt register for higher priority interrupts than current process”→“If true, it stores the current contents of the registers on the stack”→“The appropriate interrupt service routine (ISR) for the key press is called”→“The input data from the keyboard is processed”→“The contents of the registers are restored from the stack”→“... and control is passed back to previous process”。写满 6 点保险。

**英文作答句**　An interrupt flag is raised in the interrupt register. At the end of the current F-E cycle, the system checks the interrupt register for interrupts with a higher priority than the current process. If true, it stores the current contents of the registers on the stack. The appropriate ISR for the key press is called and the input data from the keyboard is processed. The contents of the registers are restored from the stack and control is passed back to the previous process.

**直观**　你在写作业（当前进程），手机响了（中断）。你先把这一句写完（周期结束），看看是谁打来的、要不要接（优先级）；要接，就在书里夹个书签（寄存器存栈），接完电话再翻到书签处接着写（恢复寄存器）。

**下一道变式**　⟦9618_w23_13:9(d)⟧　（排序题：从字母选项里挑出缺的三个步骤放到正确位置。）

<!-- auto:drills P1-PF-04 -->

### P1-PF-05　影响计算机性能的因素　{#P1-PF-05}

<!-- auto:stats P1-PF-05 -->

**考法**　①说出一个影响性能的因素并说明原因（“因素 + 原因”成对给分）；②描述两种硬件升级及各自如何提高性能；③解释提高时钟速度、增大缓存各自为何提高性能；④为什么双核不一定快一倍 / 增加核数的缺点；⑤RAM 容量、总线宽度不同怎样影响性能（常给两台电脑的配置对比）。

**识别信号**　clock speed / number of cores / cache memory / bus width / RAM；Identify one factor … and state why；Describe two ways the hardware … can be upgraded；does not always run twice as fast；drawbacks of increasing the number of cores。

**解题思路**
1. 每个因素背一条“因为 → 所以”：

| 因素 | 为什么更快 |
|:--|:--|
| 时钟速度 ↑ | 每秒执行更多 F-E 周期 → 每秒处理更多指令 |
| 核数 ↑ | 每个核可独立处理，多条指令/多个进程并行执行 |
| 缓存 ↑ | 缓存是靠近 CPU 的高速存储，存最常用的指令/数据；更大 → 能存更多 → 少去访问较慢的 RAM，CPU 少空等 |
| 数据总线宽度 ↑ | 每次能传更多位的数据 |
| 地址总线宽度 ↑ | 能寻址更多内存单元 |
| RAM ↑ | 更多正在运行的程序和数据能同时放在内存里，少用虚拟内存、少从较慢的辅存读取 |

2. “不一定快一倍”/多核缺点：核之间要通信 → 额外开销与延迟；软件不一定为多核设计 → 有的核闲置；内存访问速度可能跟不上；（比较两台电脑时）其他配置也可能不同。
3. 升级题：“升级什么”1 分 +“为什么提高性能”1 分，**两句要配对**。

**得分表述**（引自对应 MS）
- 「Processor can perform more F-E cycles per second」⟦9618_w25_12:3(c)⟧
- 「so more instructions / data can be processed each second」⟦9618_w25_12:3(c)⟧
- 「Can store more of the most frequently used instructions」⟦9618_w25_12:3(c)⟧
- 「which reduces the need to access slower RAM」⟦9618_w25_12:3(c)⟧
- 「Multiple cores introduce additional overheads」⟦9618_w23_11:5(c)(ii)⟧
- 「Wider data bus means more data can be transferred between components at a time」⟦9618_s25_11:6(a)(iii)⟧

**易错与失分**
- 只写“faster”：要写到 F-E 周期每秒更多、少访问 RAM 这一层机制。
- 题目说了“other”而又写了题干已给的因素（如已给核数又写核数）。
- 把 SSD 当作处理器的因素：问 processor feature 时答时钟、核数、缓存、总线宽度。
- 缓存写成“stores all data”：缓存存的是**常用**的指令和数据。

#### 代表题精讲　⟦9618_w25_12:3(c)⟧

**在考什么**　新旧两台电脑：1.8 GHz → 2.3 GHz、16 MB → 32 MB 缓存。Explain why increasing the clock speed and increasing the cache memory will improve the performance of the computer. 4 分，每项 2 分（讲解时请对照原卷 QP p.5 的配置表）。

**完整作答**
- 时钟速度：处理器每秒能执行更多的 F-E 周期，所以每秒能处理更多指令/数据。
- 缓存：更大的缓存能存更多最常用的指令，从而减少访问较慢的 RAM 的次数。

**与 MS 对齐**　Clock speed：“Processor can perform more F-E cycles per second”+“... so more instructions / data can be processed each second”；Cache memory：“Can store more of the most frequently used instructions”+“… which reduces the need to access slower RAM”。

**英文作答句**　Clock speed: the processor can perform more F-E cycles per second, so more instructions can be processed each second. Cache memory: it can store more of the most frequently used instructions, which reduces the need to access the slower RAM.

**下一道变式**　⟦9618_w23_11:5(c)(ii)⟧　（反面：为什么两个 2.1 GHz 核不一定比一个 2.1 GHz 快一倍，5 分。）

<!-- auto:drills P1-PF-05 -->

### P1-PF-06　端口　{#P1-PF-06}

<!-- auto:stats P1-PF-06 -->

**考法**　①为某个外设（打印机、显示器、VR 头显、光驱、U 盘）选一个端口并论证；②HDMI 相对 VGA 的好处；③数据怎样经 USB 传输；④HDMI 怎样连接外设；⑤U 盘插入后怎样被自动识别。

**识别信号**　Universal Serial Bus (USB)；High Definition Multimedia Interface (HDMI)；Video Graphics Array (VGA)；Identify one port … Justify your choice；Explain how this port provides an automatic connection。

**解题思路**
1. **USB**：串行，一次传 1 位；通用标准，几乎所有外设都能用；传输快；插入时电压变化 → 计算机检测到 → 设备把自己的识别码发给计算机 → OS 在设备列表里找到它 → 加载对应的驱动程序（自动连接）。
2. **HDMI**：数字接口；一根线同时传**音频和视频**；带宽高、传输快，支持高分辨率；传的是未压缩的数字信号流；抗干扰。
3. **VGA**：模拟视频接口，只传视频，不传声音。
4. 论证题：“端口名 1 分 + 与设备匹配的理由 2 分”。理由要扣设备（显示器有扬声器 → HDMI 传声音；高分辨率 → HDMI 带宽高）。

**得分表述**（引自对应 MS）
- 「HDMI transfers both audio and video using a single cable」⟦9618_s25_13:2(c)⟧
- 「HDMI has faster transfer rates than VGA」⟦9618_w24_12:3(b)⟧
- 「HDMI is digital interface therefore no data is lost in transfer to analogue and back」⟦9618_w24_12:3(b)⟧
- 「A voltage change occurs when the drive is plugged in」⟦9618_w24_11:3(b)(ii)⟧
- 「and loads the appropriate device driver」⟦9618_w24_11:3(b)(ii)⟧
- 「1 bit is transferred at a time」⟦9618_s23_12:5(c)(i)⟧

**易错与失分**
- 给 U 盘选 HDMI，给打印机选 VGA：端口要与设备用途匹配。
- HDMI 的好处只写“better quality”：要写出原因（数字信号、带宽高、支持高分辨率、同时传音频）。
- 自动识别只写“the computer recognises it”：要写出“电压变化 → 检测 → 设备码 → OS 加载驱动”这条链（驱动那一点与 SS-01 相连）。

#### 代表题精讲　⟦9618_w24_12:3(b)⟧

**在考什么**　显示器分辨率 2560 × 1600，并内置扬声器；电脑有 VGA 和 HDMI 两个口。Explain the benefits of connecting the monitor to the computer using the HDMI port instead of the VGA port. 4 分，MS 6 点取 4。

**完整作答**
1. HDMI 的传输速率比 VGA 快，这正是这台高分辨率（像素多）显示器所需要的。
2. HDMI 能同时传视频和音频到显示器的扬声器，所以不需要像 VGA 那样另接一根音频线。
3. HDMI 是数字接口，不需要先转成模拟信号再转回来，数据不会在转换中丢失。

**与 MS 对齐**　“HDMI has faster transfer rates than VGA”+“… needed due to high resolution / large number of pixels of monitor”；“HDMI supports video and audio transfer between computer and monitor speakers”+“… so no separate sound cable is needed unlike VGA”；“HDMI is digital interface therefore no data is lost in transfer to analogue and back”。

**英文作答句**　HDMI has faster transfer rates than VGA, which is needed due to the high resolution of the monitor. HDMI supports video and audio transfer to the monitor speakers, so no separate sound cable is needed, unlike VGA. HDMI is a digital interface, so no data is lost in conversion to analogue and back.

**下一道变式**　⟦9618_w24_11:3(b)(ii)⟧　（U 盘插入后被自动识别：端口 + 自动连接的过程。）

<!-- auto:drills P1-PF-06 -->

### P1-PF-07　汇编语言：机器码、两遍汇编与指令分组　{#P1-PF-07}

<!-- auto:stats P1-PF-07 -->

**考法**　①两遍汇编器第一遍的目的；②连线/勾选：每个动作在第一遍、第二遍还是两遍都做；③写出某些操作码所属的指令组；④给出指令组，从指令表里各举一条带合适操作数的指令；⑤描述两个指令组。

**识别信号**　two-pass assembler；first pass / second pass；symbol table；instruction group(s)；data movement / input and output of data / arithmetic operations / unconditional and conditional instructions / compare instructions。

**解题思路**
1. **两遍汇编**：汇编语言里可以用**标签**（label）代替地址，而标签可能在定义之前就被使用（向前跳转），所以要读两遍：
   - 第一遍：逐行读源代码；去掉注释和空白；把标签及其地址加入**符号表**（目的就是建立符号表）。
   - 第二遍：再次逐行读源代码；用符号表把标签换成地址；生成**目标码**（object code，即机器码）。
   - “逐行读源代码”两遍都做。
2. **五个指令组**与例子（以题目给的指令表为准）：

| 组 | 指令 |
|:--|:--|
| Data movement 数据移动 | LDM、LDD、LDI、LDX、LDR、STO、MOV |
| Input and output of data 输入输出 | IN、OUT |
| Arithmetic operations 算术运算 | ADD、SUB、INC、DEC |
| Unconditional and conditional instructions 无条件/条件跳转 | JMP、JPE、JPN |
| Compare instructions 比较 | CMP、CMI |

3. 举例题“Each instruction must have a suitable operand”：写全，如 `LDR #50`、`STO 201`、`ADD 100`、`INC IX`、`JPE 96`。

**得分表述**（引自对应 MS）
- 「To create a symbol table」⟦9618_w23_11:8(a)⟧
- 「1 mark for generates object code to second pass」⟦9618_s23_12:3(a)⟧
- 「1 mark for reads source code one line at a time to both boxes」⟦9618_s23_12:3(a)⟧
- 「1 mark for removes white space and adds labels to first pass」⟦9618_s23_12:3(a)⟧
- 「IN - Input and output of data」⟦9618_w23_12:9(a)⟧
- 「JPE - Unconditional and conditional instructions」⟦9618_w23_12:9(a)⟧

**易错与失分**
- 组名写得太随意（“loading group”“jump group”）：用标准组名，MS 认的就是表里那五个。
- “INC”归到数据移动：INC/DEC 是算术运算。
- 举例不带操作数（只写 `LDR`），或用了指令表里没有的指令：题目要求 “Only use the instructions given in the table”。
- 两遍汇编的勾选题里，“检查操作码是否在指令集中”这一行在抽取文本里看不出勾在哪一栏（⟦9618_w22_11:6(c)⟧），以该题 MS p.9 原页为准，讲解时请对照。

#### 代表题精讲　⟦9618_w23_12:9(a)⟧

**在考什么**　Identify the instruction group for each of the following opcodes：IN、ADD、JPE、CMI。4 分，每个 1 分。

**完整作答**
- IN：输入输出（Input and output of data）。
- ADD：算术运算（Arithmetic operations）。
- JPE：无条件与条件跳转（Unconditional and conditional instructions）——JPE 是比较后条件为真时跳转。
- CMI：比较（Compare instructions）——用间接寻址取比较对象，但它的作用仍是比较。

**与 MS 对齐**　“IN - Input and output of data”“ADD - Arithmetic operations”“JPE - Unconditional and conditional instructions”“CMI - Compare instructions”。

**英文作答句**　IN: input and output of data. ADD: arithmetic operations. JPE: unconditional and conditional instructions. CMI: compare instructions.

**下一道变式**　⟦9618_s23_12:3(a)⟧　（两遍汇编：每个动作连到第一遍、第二遍或两遍。）

<!-- auto:drills P1-PF-07 -->

### P1-PF-08　寻址方式　{#P1-PF-08}

<!-- auto:stats P1-PF-08 -->

**考法**　①填空/填表：按描述写出寻址方式名称；②说出并描述一种（题目指令表里没出现的）寻址方式，有时还要举一条指令为例；③直接寻址与变址寻址的一个相同点和一个不同点；④相对寻址是什么、有什么用。

**识别信号**　mode(s) of addressing；immediate / direct / indirect / indexed / relative addressing；Identify and describe one (additional) mode of addressing；Explain the purpose of relative addressing。

**解题思路**
1. 五种方式，每种一句话 + 一条例子：

| 方式 | 操作数是什么 | 例 | ACC 得到 |
|:--|:--|:--|:--|
| Immediate 立即 | 数据本身 | `LDM #20` | 20 |
| Direct 直接 | 数据所在的地址 | `LDD 20` | [20] |
| Indirect 间接 | 一个地址，那里存着数据所在的地址 | `LDI 20` | [[20]] |
| Indexed 变址 | 一个地址，加上 IX 的内容才是数据所在地址 | `LDX 20` | [20 + IX] |
| Relative 相对 | 相对某个基地址的偏移量 | — | [基地址 + 偏移] |

2. **相对寻址的用途**：所有地址都写成“基地址 + 偏移”，程序被装进内存的任何位置都能正确运行 → 可重定位代码（relocatable code）。
3. “没出现的方式”：先看题目指令表与程序里已用了哪些（装入类指令的说明会写明 Immediate / Direct / Indirect / Indexed addressing），再从五种里挑剩下的；拿不准时选间接或变址最稳。
4. 直接 vs 变址：相同——都把某个地址里的内容装入 ACC；不同——直接用操作数本身做地址，变址要先把 IX 的内容加到操作数上。

**得分表述**（引自对应 MS）
- 「Direct addressing is when the operand holds the memory address of the data」⟦9618_s23_12:3(b)⟧
- 「Indirect addressing is when the operand holds a memory address that stores the memory address of the data」⟦9618_s23_12:3(b)⟧
- 「Immediate addressing is when the operand is the data」⟦9618_s23_12:3(b)⟧
- 「The address of the data is formed by adding the contents of the Index Register (IX) to the operand」⟦9618_s25_13:5(a)(ii)⟧
- 「To allow for re-locatable code」⟦9618_w22_13:6(a)(ii)⟧
- 「because all (target) addresses can be specified by the base address + offset」⟦9618_w22_13:6(a)(ii)⟧

**易错与失分**
- 间接寻址写成“the operand is the address of the data”：那是直接寻址。间接要多一层——“存着数据地址的地址”。
- 变址写成“adds the operand to the ACC”：加的是 **IX**，得到的是**地址**。
- 题目要“not used in the program”时写了程序里已有的方式：先核对指令表。
- 描述与名称不配对：“名称 1 分 + 对应描述 1 分”，名称错了描述也不给。

#### 代表题精讲　⟦9618_s25_13:5(a)(ii)⟧

**在考什么**　Complete the table by identifying and describing two modes of addressing that are not used in the program in part (a). 4 分：每种“名称 1 + 对应描述 1”。MS 接受 Direct、Indirect、Indexed 中的任意两种（讲解时请对照原卷 QP p.11–12 的指令表与 part (a) 的程序，确认程序里用了哪些方式）。

**完整作答**

| Mode of addressing | Description |
|:--|:--|
| Indirect | 操作数指向一个内存单元，该单元里存的是数据的地址 |
| Indexed | 把变址寄存器 IX 的内容加到操作数上，形成数据的地址 |

**与 MS 对齐**　“Indirect”+“The operand points to the memory location which is the address of the data”；“Indexed”+“The address of the data is formed by adding the contents of the Index Register (IX) to the operand”。

**英文作答句**　Indirect: the operand points to the memory location which holds the address of the data. Indexed: the address of the data is formed by adding the contents of the Index Register (IX) to the operand.

**直观**　立即 = 直接把东西递给你；直接 = 告诉你“东西在 20 号柜”；间接 = 告诉你“20 号柜里有张纸条，写着东西在几号柜”；变址 = “从 20 号柜往后数 IX 个”。

**下一道变式**　⟦9618_w22_13:6(a)(ii)⟧　（相对寻址的目的：可重定位代码。）

<!-- auto:drills P1-PF-08 -->

### P1-PF-09　执行指令后的寄存器内容　{#P1-PF-09}

<!-- auto:stats P1-PF-09 -->

**考法**　给一张小内存表（地址 → 数据）和 ACC、IX 的初值，再给 3–4 组互相独立的指令（每组 1–3 条），写出每组执行后 ACC（有时还要 IX）的值。每组 1 分，共 3–5 分。也有单条指令一行一问的形式。

**识别信号**　The current contents of memory are shown；The current contents of the ACC and IX are shown；Complete the table by writing the content of the ACC (and the IX) after each program / set of instructions；LDM / LDD / LDI / LDX / LDR / ADD / SUB / INC / DEC。

**解题思路**
1. **每组都从题目给的初值开始**（ACC、IX 都回到初值），组与组之间不传递。
2. 每条指令先认**寻址方式**，再按章首的指令表计算：
   - `#` 开头 → 数字本身；不带记号 → 地址，去内存表查。
   - `LDI a`：查两次——先查 a 得到一个地址，再查那个地址。
   - `LDX a`：先算 a + IX，再查。
   - `LDR #n` 改的是 IX，不是 ACC；后面的 `LDX` 要用新的 IX。
3. 在草稿上写成链式：`LDI 15 → [15] = 16 → [16] = 12 → ACC = 12 → SUB #1 → 11`。
4. 有 IX 列时：没碰 IX 的组，IX 就是初值。
5. 如果表里混有 AND/OR/XOR 位运算：按裁决 B2，位运算行占一半或以上时这类题归 PF-12，算法相同（见 PF-12 卡）；另外记住 `CMP` 只比较、不改 ACC。

**得分表述**（引自对应 MS）
- 「1 mark for each correct content of the ACC (4)」⟦9618_w24_12:8(a)⟧
- 「1 mark for correct IX column」⟦9618_w24_12:8(a)⟧
- 「LDM #98 98」⟦9618_w25_12:3(b)⟧
- 「LDI 101 8」⟦9618_w25_12:3(b)⟧
- 「LDX 100 32」⟦9618_w25_12:3(b)⟧

**易错与失分**
- `ADD 11` 当成加 11：不带 `#` 就是地址，要加的是 [11]。
- `LDI` 只查一次：得到的是地址不是数据。
- 上一组的结果带进下一组：每组都从初值开始。
- `LDX` 忘了加 IX，或用了 IX 的旧值（同组里前面有 `LDR`）。
- `STO` 以为会改 ACC：STO 只把 ACC 写进内存。

#### 代表题精讲　⟦9618_s24_12:5(a)⟧

**在考什么**　内存：10→1、11→3、12→5、13→11、14→10、15→16、16→12；ACC = 10，IX = 0。四个程序各写执行后的 ACC，4 分，每个 1 分（讲解时请对照原卷 QP p.11 的表格）。四个程序正好覆盖间接、直接、立即、变址四种寻址。

**完整作答**

| 程序 | 追踪 | ACC |
|:--|:--|:--|
| 1 `LDI 15` / `SUB #1` | [15] = 16 → [16] = 12 → ACC = 12；12 − 1 | **11** |
| 2 `LDD 14` / `ADD 11` | ACC = [14] = 10；+ [11] = 3 | **13** |
| 3 `LDM #11` / `ADD #3` / `SUB 16` | ACC = 11；+ 3 = 14；− [16] = 12 | **2** |
| 4 `LDR #2` / `LDX 14` / `ADD #2` | IX = 2；[14 + 2] = [16] = 12；+ 2 | **14** |

**与 MS 对齐**　MS 的四个答案依次是 11、13、2、14，每个 1 分。

**英文作答句**　（填表题无文字作答。）

**直观**　把内存表当成一排带编号的抽屉。`#` 是“直接给你这个数”；没有 `#` 是“去这个编号的抽屉拿”；`LDI` 是“抽屉里放着另一张抽屉号”；`LDX` 是“编号再往后挪 IX 格”。

**下一道变式**　⟦9618_w24_12:8(a)⟧　（多了 IX 列：第 4 组先 `LDR #21` 改 IX，再 `LDX 2`。）

<!-- auto:drills P1-PF-09 -->

### P1-PF-10　汇编程序跟踪　{#P1-PF-10}

<!-- auto:stats P1-PF-10 -->

**考法**　内存里有一段程序（含 CMP/CMI、JPE/JPN、JMP，常有循环和 IN/OUT）和数据，用跟踪表逐条执行，记录每条指令执行后的 ACC、IX、相关内存单元和输出。3–5 分，按“阴影行组”给分。附带小问：说明程序（或一段代码）的作用；把某条指令改掉会有什么影响。

**识别信号**　Trace the program currently in memory using the (following) trace table；表头 Instruction address / ACC / IX / Memory address … / Output；stopping when line … is executed for a second time；State the purpose of this part of an assembly language program；State the effect of changing instruction …。

**解题思路**
1. **准备**：在跟踪表第一行（题目通常已给）确认各内存单元的初值；把 ASCII 对照表（若给）放在手边。
2. **一条指令一行**：第一列写**执行的这条指令的地址**；只在某一栏的值**改变**时才写新值（MS 的空格就是“不变”）。
3. **每类指令改哪一栏**：
   - LDM/LDD/LDI/LDX、ADD/SUB、INC/DEC ACC、IN → 改 ACC；
   - LDR、INC/DEC IX → 改 IX；
   - STO a → 改内存 a 那一栏（ACC 不变）；
   - CMP/CMI、JPE/JPN/JMP → 什么都不改，只决定**下一行的指令地址**；
   - OUT → 在 Output 栏写 ACC 中 ASCII 码对应的字符。
4. **跳转**：CMP 比较后，JPE 在“相等”时跳，JPN 在“不相等”时跳；跳了，下一行写目标地址；没跳，写下一条地址。JMP 无条件跳。
5. **停止条件**：执行到 END，或题目给的停止条件（“stopping when line 90 is executed for a second time”）就停。
6. “程序的作用”：看循环在做什么（数某个字符的个数、交换两个单元的内容……），用一句话说出结果；“改一条指令的影响”：把改后的那条重新算一遍，看结果和后续比较/循环怎样变。

**得分表述**（引自对应 MS）
- 「1 mark for each shaded section」⟦9618_s25_11:8(a)⟧
- 「1 mark for each set of highlighted rows」⟦9618_w22_11:6(a)(i)⟧
- 「swaps the contents of memory address 100 and 101」⟦9618_w22_11:6(a)(ii)⟧
- 「The number 10 will be loaded into the ACC instead of 12 / contents of address 10」⟦9618_s25_12:7(a)(ii)⟧
- 「The addition will give 20 not 22 so the comparison will fail and result in an infinite loop」⟦9618_s25_12:7(a)(ii)⟧

**易错与失分**
- 每行都把 ACC 抄一遍：多数情况不扣分，但会让你看漏真正改变的地方；MS 的写法是只写变化。
- STO 之后忘了更新内存栏，导致后面 LDD 读到旧值——连锁错一整组。
- 跳转后仍写下一条地址：JPE/JPN 成立时下一行一定是目标地址。
- IN 之后 ACC 写成字符本身：ACC 里是 **ASCII 码**（输入 ‘1’ → 49）；OUT 写的才是字符。
- 停止条件读错，多跟或少跟一圈。
- 跟踪表的阴影分组只在原卷 MS 上看得到，**本型每题都要对照原卷 QP 的程序与跟踪表**。

#### 代表题精讲　⟦9618_s25_11:8(a)⟧

**在考什么**　内存 80→10、81→8、82→80、83→81；程序从地址 200 开始（`LDD 81`、`INC ACC`、`STO 83`、`LDI 82`、`CMP 83`、`JPE 209`、`LDD 83`、`ADD #10`、`JMP 210`、`DEC ACC`、`STO 81`、`END`）。用跟踪表跟踪，4 分（讲解时请对照原卷 QP p.14–15 的程序与跟踪表）。

**完整作答**

| 指令地址 | 指令 | ACC | [80] | [81] | [82] | [83] | 说明 |
|:-:|:--|:-:|:-:|:-:|:-:|:-:|:--|
| （初值） | | | 10 | 8 | 80 | 81 | |
| 200 | LDD 81 | 8 | | | | | ACC ← [81] |
| 201 | INC ACC | 9 | | | | | |
| 202 | STO 83 | | | | | 9 | [83] ← 9 |
| 203 | LDI 82 | 10 | | | | | [82] = 80 → [80] = 10 |
| 204 | CMP 83 | | | | | | 10 与 [83] = 9 比较：不相等 |
| 205 | JPE 209 | | | | | | 比较为假，不跳 |
| 206 | LDD 83 | 9 | | | | | |
| 207 | ADD #10 | 19 | | | | | |
| 208 | JMP 210 | | | | | | 无条件跳到 210 |
| 210 | STO 81 | | | 19 | | | [81] ← 19 |
| 211 | END | | | | | | |

注意 209（`DEC ACC`）从未执行，所以表里没有 209 这一行。

**与 MS 对齐**　MS 的行与上表一致：200 → 8，201 → 9，202 → [83] = 9，203 → 10，204，206 → 9，207 → 19，208，210 → [81] = 19；按阴影分 4 段各 1 分。

**英文作答句**　（跟踪题无文字作答。）

**直观**　跟踪就是当一回 CPU：手里一张纸（ACC），桌上一排抽屉（内存），一次只执行一条指令，执行完才看下一条去哪。

**下一道变式**　⟦9618_w22_11:6(a)(i)⟧　（带循环和 IX、用 CMP #35 判断结束、最后 OUT 一个字符；讲解时请对照原卷 QP p.13 的 ASCII 表。）

<!-- auto:drills P1-PF-10 -->

### P1-PF-11　移位　{#P1-PF-11}

<!-- auto:stats P1-PF-11 -->

**考法**　①对给定 8 位数做 n 位的逻辑左移/右移、算术右移、循环移位，写出结果（每题 1 分，最常见）；②执行 `LSL #n` / `LSR #n` 后的 ACC；③写出能把 ACC 从某值变到另一值的移位指令；④逻辑右移与算术右移的相同点、不同点；⑤移位的数学含义。

**识别信号**　logical shift / arithmetic shift / cyclic shift；Show the result of a n-place … shift；LSL #n / LSR #n；Write a bit manipulation instruction that uses a binary shift to change the contents of the ACC to；difference between a right logical shift and a right arithmetic shift。

**解题思路**
1. **逻辑移位**：所有位整体移动，移出的位丢掉，空出的一端补 **0**。`LSL` 往左（右端补 0），`LSR` 往右（左端补 0）。
2. **算术右移**：所有位右移，移出的位丢掉，左端空位**复制原来的符号位（MSB）**——保持补码数的正负。算术左移与逻辑左移结果相同（右端补 0）。
3. **循环移位**：移出一端的位从另一端补回去，一位不丢。
4. **数学含义**（无符号数，未溢出时）：左移 n 位 = ×2ⁿ；右移 n 位 = ÷2ⁿ（丢掉余数）。
5. **写法**：先把原数按 4 位一组写开，数着位数移；结果也写成 8 位（MS 用 `xxxx xxxx`）。
6. **反推指令**：对比前后两个数，看是整体左移还是右移了几位：`0001 1110 → 0111 1000` 是左移 2 位 → `LSL #2`。

**得分表述**（引自对应 MS）
- 「A logical shift moves all bits to the right and inserts zeros in the appropriate leftmost bits」⟦9618_w24_13:8(c)⟧
- 「An arithmetic shift moves all bits to the right but copies the sign bit into the Most Significant Bit (MSB)」⟦9618_w24_13:8(c)⟧
- 「Arithmetic retains sign/MSB while logical does not retain sign/MSB」⟦9618_s26_13:7(c)⟧
- 「Both lose the Least Significant Bit(s) (LSB)」⟦9618_s26_13:7(c)⟧

**易错与失分**
- 算术右移左边补 0：只有符号位为 0 时才补 0；负数（MSB = 1）要补 1。⟦9618_s25_13:7(a)(ii)⟧：`1001 1110` 算术右移 3 位 → `1111 0011`。
- 位数数错：结果必须仍是 8 位。写成 4 位一组再移最不容易错。
- 题目给的是补码负数却做逻辑左移（⟦9618_s25_13:7(a)(i)⟧）：照做逻辑移位，不必管符号，`1100 1010` → `0010 1000`。
- 循环移位当成逻辑移位，把移出的位丢了。

#### 代表题精讲　⟦9618_w24_13:8(c)⟧

**在考什么**　Describe the difference between a right logical binary shift and a right arithmetic binary shift. 2 分：两种移位各 1 句。

**完整作答**　逻辑右移：所有位向右移动，在左端空出的位上补 0。算术右移：所有位向右移动，但把符号位复制到最高位（MSB），因此补码数的正负不变。
例：`1001 0011` 右移 3 位——逻辑：`0001 0010`；算术：`1111 0010`（与 ⟦9618_w25_13:2(c)⟧ 的 MS 答案一致）。

**与 MS 对齐**　“A logical shift moves all bits to the right and inserts zeros in the appropriate leftmost bits”+“An arithmetic shift moves all bits to the right but copies the sign bit into the Most Significant Bit (MSB)”。

**英文作答句**　A logical shift moves all bits to the right and inserts zeros in the leftmost bits, whereas an arithmetic shift moves all bits to the right but copies the sign bit into the Most Significant Bit (MSB).

**直观**　一排人往右挪座位：逻辑右移时，左边空出的座位一律坐“0”；算术右移时，左边空座由最左边那个人的“分身”补上——队伍的“正负号”保持不变。

**下一道变式**　⟦9618_s25_13:7(a)(ii)⟧　（动手算：补码负数 `10011110` 算术右移 3 位。）

<!-- auto:drills P1-PF-11 -->

### P1-PF-12　按位运算求结果　{#P1-PF-12}

<!-- auto:stats P1-PF-12 -->

**考法**　给 ACC 的当前值（8 位二进制）和一条 AND / OR / XOR 指令，写出执行后的 ACC。操作数可能是二进制 `B…`、十进制 `#…`、十六进制 `&…` 或内存地址（去内存表取）。单问每题 1 分，或一张 3–4 行的表（每次执行前把 ACC 重置为同一个值）。有时与 LSL、LDM、CMP 混在一张表里。

**识别信号**　Show / Write the contents of the ACC after the execution of the following instruction: AND / OR / XOR …；Complete the table by writing the content of the ACC；The binary number … is reloaded into the ACC before each … is run。

**解题思路**
1. **把操作数换成 8 位二进制**：`#30` → `0001 1110`；`&F1` → `1111 0001`；`B01001111` 直接用；地址 → 去内存表取那一格的二进制。
2. ACC 与操作数**上下对齐**，逐位运算：
   - AND：两位都 1 才得 1（与 0 的位被**清零**，与 1 的位**保留**）；
   - OR：有一个 1 就得 1（与 1 的位被**置 1**，与 0 的位保留）；
   - XOR：两位不同得 1（与 1 的位被**取反**，与 0 的位保留）。
3. 结果写成 8 位，4 位一组。
4. 表里混有其他指令：`LDM #n` 直接把 n 的二进制放进 ACC；`CMP` 只比较、ACC 不变；`LSL/LSR` 按 PF-11 移位；`ADD`/`INC` 做二进制加法。
5. 表格题每行都从题目说的“reloaded”值开始，不要把上一行的结果带下来。

**得分表述**（引自对应 MS）
- 「AND 31 1001 1010」⟦9618_s24_11:4(b)⟧
- 「XOR B01001111 1101 0101」⟦9618_s24_11:4(b)⟧
- 「OR #30 1001 1110」⟦9618_s24_11:4(b)⟧
- 「AND #29 0000 0100」⟦9618_s24_12:5(b)⟧
- 「XOR &F1 1111 0000」⟦9618_w25_13:6(a)⟧

**易错与失分**
- `#29` 当成二进制或十六进制：`#` 是十进制，29 = `0001 1101`。
- 地址操作数（`AND 31`、`OR 100`）直接拿地址号去运算：要先取那个地址里的数据。
- `&F1` 换错：F = 1111，1 = 0001。
- CMP 行写出了比较结果：CMP 不改 ACC，原样抄写当前值（⟦9618_w25_13:6(a)⟧ 的 CMP 行答案就是原值 `0001 0001`）。
- 数位没对齐，错一位整行丢分。

#### 代表题精讲　⟦9618_s24_11:4(b)⟧

**在考什么**　内存：30 → 0111 0101、31 → 1111 1111、32 → 0000 0000、33 → 1100 1100、34 → 1010 1010；每个程序运行前 ACC 都重置为 `1001 1010`。三个程序 `AND 31`、`XOR B01001111`、`OR #30`，各写结果，3 分（讲解时请对照原卷 QP p.10 的表格）。三行正好用到地址、二进制、十进制三种操作数。

**完整作答**

```
1) AND 31：操作数 = [31] = 1111 1111
   ACC   1001 1010
   AND   1111 1111
   =     1001 1010        （与全 1 相与，保持不变）

2) XOR B01001111
   ACC   1001 1010
   XOR   0100 1111
   =     1101 0101

3) OR #30：30 = 0001 1110
   ACC   1001 1010
   OR    0001 1110
   =     1001 1110
```

**与 MS 对齐**　MS 三行：`1001 1010`、`1101 0101`、`1001 1110`，每行 1 分。

**英文作答句**　（填表题无文字作答。）

**直观**　掩码像一张镂空模板盖在 ACC 上：AND 的 0 把底下的位涂黑，OR 的 1 把底下的位点亮，XOR 的 1 把底下的位翻面。

**下一道变式**　⟦9618_s24_12:5(b)⟧　（同样三种操作数，`AND #29` 要先把 29 换成二进制。）

<!-- auto:drills P1-PF-12 -->

### P1-PF-13　位掩码与设备监控　{#P1-PF-13}

<!-- auto:stats P1-PF-13 -->

**考法**　①写一条（或两条）位操作指令，实现指定效果：把 ACC 清零、只把最低位置 1、只把最高位置 1、把 ACC 从某值变到另一值；②解释怎样用位操作测试 ACC 中的数是否为奇数，或怎样清空寄存器，并写出指令；③解释位操作怎样用于监测或控制设备。

**识别信号**　Write the bit manipulation instruction(s) that will / can be used to …；set the ACC to &0；set the least / most significant bit to 1；test whether … represents an odd denary number；Explain how bit manipulation can be used to monitor or control a device。

**解题思路**
1. **先选运算**：

| 想要的效果 | 运算 | 掩码 |
|:--|:--|:--|
| 把某些位清零 / 只保留某些位（测试） | AND | 要清零的位放 0，要保留的位放 1 |
| 把某些位置 1 | OR | 要置 1 的位放 1，其余放 0 |
| 把某些位取反 | XOR | 要取反的位放 1，其余放 0 |
| 整个寄存器清零 | AND | 全 0：`AND #0` |

2. **再写掩码**：写成 `B…`、`#…` 或 `&…` 都行（MS 通常三种都列）。“All other bits must remain unchanged”就是在提示：其他位的掩码要选“不改变”的那种（AND 用 1，OR/XOR 用 0）。
3. **两步题**：“只把 MSB 置 1、其他位全 0，且对任何 8 位数都成立” → 先 `AND #0` 清零，再 `OR #128`。
4. **测试某一位**：用 AND 把其他位清掉、只留下要测的那一位，再把结果与只含那一位的值比较（奇数测试：`AND #1`，结果与 1 比较，相等则为奇数）。
5. **监测/控制设备**：每一位代表一个设备的状态（开/关）；监测 = 用掩码测试单独某一位，读出设备状态；控制 = 用掩码置位/清零/取反单独某一位，改变设备状态，不影响其他位。

**得分表述**（引自对应 MS）
- 「An odd binary number will have a 1 in the Least Significant Bit (LSB)」⟦9618_w24_12:8(b)(ii)⟧
- 「A bit manipulation operation is required to access/mask only the LSB and clear all the others」⟦9618_w24_12:8(b)(ii)⟧
- 「Compare the result of the masking with denary 1」⟦9618_w24_12:8(b)(ii)⟧
- 「AND B00000001 // AND #1 // AND &01」⟦9618_w24_12:8(b)(ii)⟧
- 「OR B0000 0001 // OR #1 // OR &1」⟦9618_s25_11:8(b)(i)⟧
- 「by setting/clearing/toggling a single bit」⟦9618_s26_13:7(b)⟧

**易错与失分**
- 用 OR 去清零、用 AND 去置 1：方向反了。记“AND 管 0，OR 管 1，XOR 管翻”。
- 置最低位写成 `OR #255`：会把其他位也变成 1，违反“其他位不变”。
- 两步题只写 `OR #128`：如果原来其他位有 1，就做不到“只有 MSB 为 1”。
- 解释题只写指令不写解释：MS 是“解释 2 分 + 指令 1 分”。

#### 代表题精讲　⟦9618_w24_12:8(b)(ii)⟧

**在考什么**　Explain how bit manipulation can be used to test whether the binary number stored in the ACC represents an odd denary number. Write the bit manipulation instruction that will be used. 3 分：解释最多 2 分 + 指令 1 分。

**完整作答**
- 解释：奇数的二进制最低位（LSB）一定是 1。用位操作屏蔽出 LSB、把其他位全部清零；再把屏蔽后的结果与十进制 1 比较——相等就说明是奇数。
- 指令：`AND B00000001`（或 `AND #1`、`AND &01`）。

**与 MS 对齐**　解释 ←“An odd binary number will have a 1 in the Least Significant Bit (LSB)”“A bit manipulation operation is required to access/mask only the LSB and clear all the others”“Compare the result of the masking with denary 1”（任 2 点）；指令 ←“AND B00000001 // AND #1 // AND &01”。

**英文作答句**　An odd binary number will have a 1 in the Least Significant Bit (LSB). A bit manipulation operation is used to mask only the LSB and clear all the other bits. The result of the masking is compared with denary 1; the comparison is true if the number is odd. Instruction: AND B00000001

**直观**　判断奇偶只需看个位上的那一位：AND #1 就是用手把其他七位都捂住，只露出最后一位。

**下一道变式**　⟦9618_s25_13:5(b)⟧　（两条指令：对任意 8 位数只把 MSB 置 1。）

<!-- auto:drills P1-PF-13 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| PF-02 vs PF-03 | 单问某个寄存器存什么 → PF-02；放进取指-执行周期的顺序里、或用 RTN → PF-03 | 有没有 F-E cycle / register transfer notation |
| PF-03 vs PF-04 | 周期本身 → PF-03；周期结束时检查中断、怎样处理 → PF-04 | 有没有 interrupt / ISR |
| PF-01 vs PF-05 | 时钟、总线是什么/做什么 → PF-01；它们变快/变宽为什么提高性能 → PF-05 | 有没有 performance / upgrade / increase |
| PF-08 vs PF-09 | 说出/描述寻址方式 → PF-08；按寻址方式算 ACC → PF-09 | 有没有内存表要你算数 |
| PF-09 vs PF-10 | 各组指令互相独立、无跳转 → PF-09；一段有跳转/循环/输出的程序逐行跟踪 → PF-10 | Trace … using the trace table；有 CMP/JPE/JMP |
| PF-09 vs PF-12 | 装入/算术为主 → PF-09；AND/OR/XOR 占一半或以上 → PF-12（裁决 B2，例 ⟦9618_w25_13:6(a)⟧） | 数表里位运算行占几成 |
| PF-11 vs PF-12 | 整体挪位 → PF-11；与掩码逐位运算 → PF-12；一张表都有时按得分点多数定主题型 | LSL/LSR 还是 AND/OR/XOR |
| PF-12 vs PF-13 | 指令已给、求结果 → PF-12；效果已给、求指令或解释 → PF-13 | “Write the contents of the ACC” 还是 “Write the bit manipulation instruction that will …” |
| 直接 vs 间接 vs 变址 | 操作数是数据的地址 / 是“存着数据地址”的地址 / 要加上 IX 才是数据地址 | LDD / LDI / LDX |
| 逻辑右移 vs 算术右移 | 左端补 0 / 左端复制符号位 | 题目说 logical 还是 arithmetic；是否补码负数 |
