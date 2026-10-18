## HV　处理器、并行处理与虚拟机：核心概念 {#core-HV}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| RISC | 「Uses relatively few instructions / simple instructions」⟦9618_s24_31:11(a)⟧ | 精简指令集计算机：指令少而简单、定长、单周期，寄存器多，硬连线控制器，易于流水线 | 只会几种简单刀法、但刀刀一样快的厨师 | P3-HV-01 |
| CISC | 「large instruction set」⟦9618_w24_32:8⟧ | 复杂指令集计算机：指令多而复杂、变长、多周期，寻址方式多，微程序（可编程）控制器 | 会很多复杂招式的厨师 | P3-HV-01 |
| Single-cycle instruction | 「uses single-clock cycle instructions」⟦9618_w24_31:2⟧ | 每条指令在一个时钟周期内完成（RISC 的特征） | 一拍一个动作 | P3-HV-01、P3-HV-02 |
| Hard-wired control unit | 「hard-wired control unit」⟦9618_w24_31:2⟧ | 用固定逻辑电路产生控制信号的控制器（RISC） | 写死在电路里的指挥 | P3-HV-01 |
| Micro-programmed control unit | 「uses programmable control unit // uses micro-programmed control unit」⟦9618_w24_32:8⟧ | 用存储的微程序产生控制信号的控制器（CISC），复杂指令被转换成子指令执行 | 照着说明书一步步指挥 | P3-HV-01 |
| Pipelining | 「Pipelining allows several instructions to be processed simultaneously / concurrently」⟦9618_s23_32:8(a)⟧ | 指令分成若干阶段，不同指令的不同阶段在同一时钟周期并行，提高吞吐量 | 洗衣房流水作业 | P3-HV-02 |
| Pipeline stages | 「… Instruction fetch / IF, Instruction decode / ID, operand fetch / OF, opcode/instruction execute IE, result store / write back result / WB」⟦9618_w22_31:10(b)⟧ | 五个阶段：取指、译码、取操作数、执行、写回，每个阶段一个时钟周期 | 洗、甩、烘、叠、装五个工位 | P3-HV-02 |
| Instruction throughput | 「… therefore, increasing the CPU instruction throughput / the number of instructions completed per unit of time」⟦9618_s23_32:8(a)⟧ | 单位时间内完成的指令条数 | 每小时洗完几筐 | P3-HV-02 |
| Interrupt handling | 「… the current program is temporarily stopped and the status of each register stored on the stack」⟦9618_s24_31:11(b)⟧ | 周期开始 / 结束时检测中断 → 暂停当前程序、寄存器入栈 → 执行 ISR → 恢复寄存器继续 | 接电话前先在书里夹好书签 | P3-HV-02 |
| Pipelining and interrupts | 「All the instructions currently in operation are usually discarded except for the last one/the one at write back」⟦9618_s24_31:11(c)⟧ | 中断到来时流水线里有半截指令：通常丢弃，只保留写回阶段那条，处理完从下一条指令重新开始 | 流水线急停：已装箱的发走，半成品回炉 | P3-HV-02 |
| SISD | 「Single Instruction, Single Data (architecture). // Data is taken from a single source and a single instruction is performed on the data」⟦9618_w23_31:5⟧ | 单指令流、单数据流：一个处理器顺序执行指令 | 一个人一道题一道题做 | P3-HV-03 |
| SIMD | 「Single Instruction, Multiple Data (architecture) // Performs the same operation on multiple different data streams simultaneously」⟦9618_w23_32:10⟧ | 单指令、多数据：多个处理器对不同数据同时执行同一条指令 | 全班听同一口令各做各的题 | P3-HV-03 |
| MISD | 「Multiple Instruction, Single Data (architecture) // Performs different operations on the same data stream」⟦9618_w23_32:10⟧ | 多指令、单数据：多个处理器对同一数据流执行不同指令 | 几个老师用不同方法批同一份卷 | P3-HV-03 |
| MIMD | 「Multiple Instruction, Multiple Data (architecture). // At any time, any processor can execute different instructions on different sets of data」⟦9618_w23_31:5⟧ | 多指令、多数据：多个处理器独立（异步）地对不同数据执行不同指令 | 几个小组各做各的项目 | P3-HV-03 |
| Massively parallel computer | 「A large number of computer processors / separate computers connected together」⟦9618_s23_31:8⟧ | 大量处理器 / 计算机通过网络连接，同时协同处理同一问题，以发送消息方式通信 | 一千个工人用对讲机协同盖一座楼 | P3-HV-04 |
| Virtual machine | 「The emulation of a computer system / hardware and/or software」⟦9618_w22_32:5⟧ | 在宿主计算机上用软件仿真另一套计算机系统，在其中运行客户操作系统 | 家里搭的样板房 | P3-HV-05 |
| Host operating system | 「The host operating system is the normal operating system for the host computer / machine」⟦9618_s24_32:9(b)⟧ | 宿主机本来的 OS，控制全部物理资源并运行虚拟机软件 | 真房子的物业 | P3-HV-05 |
| Guest operating system | 「The guest operating system runs within the virtual machine」⟦9618_s24_32:9(b)⟧ | 在虚拟机里运行的 OS，控制虚拟硬件，经宿主 OS 间接访问真实硬件 | 样板房里的住户 | P3-HV-05 |
