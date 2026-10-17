## PF　处理器基础：核心概念 {#core-PF}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Stored program concept | 「Instructions and data are stored in the same memory space / in main memory」⟦9618_w22_11:5(a)⟧ | 程序的指令与数据存放在同一个（主）存储器中 | 菜谱和食材放在同一个冰箱里 | P1-PF-01 |
| Control Unit (CU) | 「to manage the execution of instructions (in sequence)」⟦9618_w22_11:5(b)(iii)⟧ | 取指、译码、管理指令按顺序执行，经控制总线发出/接收控制信号，协调 CPU 各部件 | 乐队指挥 | P1-PF-01 |
| System clock | 「The system clock gives out timing signals」⟦9618_s23_13:7(b)⟧ | 产生定时信号，经控制总线使各部件的操作同步 | 节拍器 | P1-PF-01、P1-PF-05 |
| ALU | Performs arithmetic and logical operations (including comparisons).（非 MS 原句） | 算术逻辑单元：做加减等算术运算与 AND/OR、比较等逻辑运算 | 计算器 | P1-PF-01 |
| Immediate Access Store (IAS) | 「Immediate Access Store holds all the data / instructions / programs currently in use」⟦9618_w23_11:5(b)⟧ | 处理器可直接访问的主存，存放当前正在使用的程序与数据；易失、访问快 | 手边的书桌 | P1-PF-01 |
| Address bus | 「The address of the data to be written to the device (in RAM) is carried on the address bus」⟦9618_w23_12:8(c)(ii)⟧ | 传送地址的总线，单向（从 CPU 发出） | 寄信时信封上的地址 | P1-PF-01、P1-PF-05 |
| Data bus | 「All data to be written to the device / buffer is carried on the data bus」⟦9618_w23_12:8(c)(ii)⟧ | 在 CPU、内存与设备之间双向传送数据与指令的总线 | 信封里的信 | P1-PF-01、P1-PF-05 |
| Control bus | 「which are sent on the control bus」⟦9618_s23_13:7(b)⟧ | 传送控制信号（读、写、中断、时钟）的双向总线 | 指挥棒 | P1-PF-01 |
| Program Counter (PC) | 「to store the address / location / memory location of the next instruction to be fetched」⟦9618_w22_11:5(b)(i)⟧ | 存放下一条要取的指令的地址 | 书签：下一页在哪 | P1-PF-02、P1-PF-03 |
| Memory Address Register (MAR) | 「holds address in memory from which data will be read / to which data will be written」⟦9618_w22_13:4(a)(i)⟧ | 存放将要读/写的内存单元的地址 | 正要去的柜子号 | P1-PF-02、P1-PF-03 |
| Memory Data Register (MDR) | 「holds the data/instructions which has been read from or is to be written to the address in the MAR」⟦9618_w22_13:4(a)(i)⟧ | 存放从 MAR 所指地址读出、或将写入该地址的数据/指令 | 刚从柜子里取出（或要放进去）的东西 | P1-PF-02、P1-PF-03 |
| Current Instruction Register (CIR) | 「holds the instruction currently being decoded and/or executed」⟦9618_w23_11:5(a)⟧ | 存放当前正在译码/执行的指令 | 正在读的那一页 | P1-PF-02、P1-PF-03 |
| Accumulator (ACC) | 「holds the result of a calculation」⟦9618_w25_11:6(a)⟧ | 存放算术与逻辑运算（中间）结果的专用寄存器 | 计算器的显示屏 | P1-PF-02、P1-PF-09 |
| Index Register (IX) | 「to store a value that is added to an address to give another address」⟦9618_w22_11:5(b)(i)⟧ | 存放一个数，与操作数相加形成实际地址（变址寻址） | “从这里往后数几格” | P1-PF-02、P1-PF-08 |
| Status Register (SR) | 「To store the value of flags/bits」⟦9618_w24_11:8(a)⟧ | 存放标志位（进位、溢出、零、负、中断等），运算后被置位/清零，可被检查以改变执行顺序 | 仪表盘上的指示灯 | P1-PF-02 |
| General vs special purpose register | 「Special purpose registers are specialised for a specific use, whereas general purpose registers are used for any purpose」⟦9618_w23_13:9(a)(ii)⟧ | 专用寄存器各有指定用途、保存程序执行状态；通用寄存器可由程序员用于任何用途 | 专用工具与万用托盘 | P1-PF-02 |
| Register transfer notation | MAR ← [PC] means the contents of the PC are copied into the MAR; [[MAR]] means the contents of the address held in the MAR.（非 MS 原句） | 用“目标 ← [来源]”表示寄存器间的数据传送；[X] 表示 X 的内容 | 箭头指向谁就改谁 | P1-PF-03 |
| Fetch-execute cycle | 「The contents of the PC are copied to the MAR」⟦9618_s22_13:2(a)⟧ | 取指：MAR ← [PC]，PC ← [PC] + 1，MDR ← [[MAR]]，CIR ← [MDR]；随后译码、执行 | 四人传信 | P1-PF-03 |
| Interrupt | 「to send a signal from a device or process」⟦9618_w22_11:5(c)⟧ | 设备或进程发给处理器、请求其注意的信号 | 手机来电 | P1-PF-04 |
| Interrupt Service Routine (ISR) | 「The relevant Interrupt Service Routine (ISR) / interrupt handler is called to process the interrupt」⟦9618_s25_12:1(c)⟧ | 处理某类中断的专用程序 | 接电话的那段对话 | P1-PF-04 |
| Interrupt priority | 「The priority of any interrupts waiting is checked」⟦9618_s25_12:1(c)⟧ | 只有优先级高于当前进程的中断才会打断它 | 老板的电话要接，推销电话不接 | P1-PF-04 |
| Stack (in interrupts) | 「the contents of the registers are stored on the stack」⟦9618_s25_12:1(c)⟧ | 中断前保存寄存器内容、处理完后恢复的内存区 | 书签：接完电话从哪接着读 | P1-PF-04 |
| Clock speed | 「Processor can perform more F-E cycles per second」⟦9618_w25_12:3(c)⟧ | 每秒的时钟周期数；越高每秒执行的 F-E 周期越多 | 心跳越快干活越快 | P1-PF-05 |
| Cache memory | 「Can store more of the most frequently used instructions」⟦9618_w25_12:3(c)⟧ | 靠近 CPU 的高速存储，存最常用的指令和数据，减少访问较慢的 RAM | 抽屉里放最常用的笔 | P1-PF-05 |
| Multi-core overhead | 「Multiple cores introduce additional overheads」⟦9618_w23_11:5(c)(ii)⟧ | 多核之间要通信协调，软件也未必能用满所有核，所以速度不会按核数成倍增长 | 两个人抬一张桌子要先商量 | P1-PF-05 |
| USB | 「1 bit is transferred at a time」⟦9618_s23_12:5(c)(i)⟧ | 通用串行总线：串行传输、通用标准，插入后可自动识别并加载驱动 | 万能插头 | P1-PF-06 |
| HDMI | 「HDMI transfers both audio and video using a single cable」⟦9618_s25_13:2(c)⟧ | 高清多媒体数字接口：一根线传音频与视频，带宽高 | 一根线搞定画面和声音 | P1-PF-06 |
| Two-pass assembler | 「To create a symbol table」⟦9618_w23_11:8(a)⟧ | 第一遍去注释、建立符号表（标签与地址）；第二遍用符号表生成目标码 | 先编目录，再按目录翻译 | P1-PF-07 |
| Symbol table | 「1 mark for removes white space and adds labels to first pass」⟦9618_s23_12:3(a)⟧ | 记录每个标签对应地址的表，在第一遍建立 | 通讯录 | P1-PF-07 |
| Instruction groups | 「IN - Input and output of data」⟦9618_w23_12:9(a)⟧ | 数据移动、输入输出、算术运算、无条件/条件跳转、比较 | 指令的五个抽屉 | P1-PF-07 |
| Immediate addressing | 「Immediate addressing is when the operand is the data」⟦9618_s23_12:3(b)⟧ | 操作数就是数据本身（`#n`） | 直接把东西递给你 | P1-PF-08、P1-PF-09 |
| Direct addressing | 「Direct addressing is when the operand holds the memory address of the data」⟦9618_s23_12:3(b)⟧ | 操作数是数据所在的地址 | “东西在 20 号柜” | P1-PF-08、P1-PF-09 |
| Indirect addressing | 「Indirect addressing is when the operand holds a memory address that stores the memory address of the data」⟦9618_s23_12:3(b)⟧ | 操作数指向的单元里存着数据的地址 | “20 号柜里有张纸条写着柜号” | P1-PF-08、P1-PF-09 |
| Indexed addressing | 「The address of the data is formed by adding the contents of the Index Register (IX) to the operand」⟦9618_s25_13:5(a)(ii)⟧ | 操作数加上 IX 的内容才是数据的地址 | “从 20 号柜往后数 IX 格” | P1-PF-08、P1-PF-09 |
| Relative addressing | 「because all (target) addresses can be specified by the base address + offset」⟦9618_w22_13:6(a)(ii)⟧ | 地址写成“基地址 + 偏移量”，使代码可以装到内存任何位置（可重定位） | “从我站的地方往前走 3 步” | P1-PF-08 |
| Trace table | 「1 mark for each set of highlighted rows」⟦9618_w22_11:6(a)(i)⟧ | 逐条记录指令执行后 ACC、IX、内存与输出变化的表，只写变化的值 | 给 CPU 写日记 | P1-PF-10 |
| Logical shift | 「A logical shift moves all bits to the right and inserts zeros in the appropriate leftmost bits」⟦9618_w24_13:8(c)⟧ | 所有位整体移动，移出的丢弃，空位补 0；对无符号数，左移 n 位仅在未丢失有效位时等于 ×2ⁿ，右移 n 位等于 ÷2ⁿ 后向下取整 | 队伍挪座位，空座坐“0” | P1-PF-11 |
| Arithmetic shift | 「An arithmetic shift moves all bits to the right but copies the sign bit into the Most Significant Bit (MSB)」⟦9618_w24_13:8(c)⟧ | 右移时左端复制符号位，保持补码数的正负 | 空座由排头的分身补上 | P1-PF-11 |
| Cyclic shift | Bits shifted out of one end are inserted at the other end.（非 MS 原句） | 循环移位：移出一端的位从另一端补回，不丢位 | 转盘 | P1-PF-11 |
| Bit masking | 「A bit manipulation operation is required to access/mask only the LSB and clear all the others」⟦9618_w24_12:8(b)(ii)⟧ | 用掩码与 AND（清零/测试）、OR（置 1）、XOR（取反）只改变或只读取指定的位 | 镂空模板 | P1-PF-12、P1-PF-13 |
| Monitoring / control by bit manipulation | 「by testing/observing the state of an individual bit」⟦9618_s26_13:7(b)⟧ | 每一位代表一个设备的开关状态：测试某一位来监测，置位/清零/取反某一位来控制 | 一排开关，每个管一盏灯 | P1-PF-13 |
