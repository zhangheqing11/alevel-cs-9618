## HW　硬件：核心概念 {#core-HW}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Primary memory | 「Random Access Memory (RAM) and Read Only Memory (ROM) are both examples of primary memory」⟦9618_s22_11:2(a)(i)⟧ | 处理器可直接访问的存储器，包括 RAM 与 ROM | 书桌：手边正在用的东西 | P1-HW-01 |
| Secondary storage | Non-volatile storage that keeps data and programs when the power is off.（非 MS 原句） | 断电后仍保存数据与程序的非易失存储（硬盘、固态、光盘） | 书柜：关机后东西还在 | P1-HW-01、P1-HW-04 |
| RAM | 「One item that is stored in RAM is currently running software/data/part of OS」⟦9618_s22_11:2(a)(i)⟧ | 可读可写、易失的主存，存放当前正在运行的程序与数据 | 草稿纸：随写随擦，断电就清空 | P1-HW-01 |
| ROM | 「to store boot up instructions / system software / firmware / BIOS」⟦9618_w22_12:3(c)⟧ | 只读、非易失的主存，存放启动指令、固件、BIOS | 刻在石头上的开机说明书 | P1-HW-01 |
| Volatile vs non-volatile | 「RAM is volatile, ROM is non-volatile」⟦9618_s26_12:6(c)⟧ | 易失：断电后内容丢失；非易失：断电后内容保留 | 白板与刻字 | P1-HW-01 |
| SRAM | 「SRAM uses transistors arranged as flip-flops/latches」⟦9618_s22_11:2(a)(i)⟧ | 用触发器存储每一位的 RAM：不需刷新、访问快、贵、密度低，用作缓存 | 拨好的开关，拨在哪停在哪 | P1-HW-02 |
| DRAM | 「DRAM uses transistors and capacitors」⟦9618_s22_11:2(a)(i)⟧；「DRAM requires constant refresh cycles unlike SRAM」⟦9618_w24_11:3(c)⟧ | 用晶体管和电容以电荷存储每一位的 RAM：需不断刷新、较慢、便宜、密度高，用作主存 | 漏水的小水桶，要不停加水 | P1-HW-02 |
| PROM | 「PROM can be set once, EPROM and EEPROM can be overwritten multiple times」⟦9618_s22_11:2(a)(ii)⟧ | 出厂后只能写入一次的可编程 ROM | 一次性刻录 | P1-HW-03 |
| EPROM | 「EPROM uses ultraviolet light to erase data whilst EEPROM uses an electrical signal to do this」⟦9618_w24_12:2(c)⟧ | 可用紫外线擦除、须从电路板取下、整片擦除后重写的 ROM | 要拆下来放进“紫外线烤箱”才能重写 | P1-HW-03 |
| EEPROM | 「EPROM needs to be removed from device EEPROM can be erased in situ」⟦9618_s22_11:2(a)(ii)⟧ | 用电信号原位擦写、可部分擦除、可多次重写的 ROM | 不拆机就能“在线升级固件” | P1-HW-03 |
| Magnetic hard disk | 「When reading from disk, a variation in magnetic field produces a variation in current through the head」⟦9618_s22_11:2(b)⟧ | 数据以磁化图案存在高速旋转的盘片上，由臂上的读写磁头读写 | 唱片机：唱片转，唱针移 | P1-HW-04 |
| Optical disc | 「When reading the laser reflects from pits and lands」⟦9618_w24_11:3(d)(i)⟧ | 激光在旋转的盘面上烧出凹坑写入数据；读取时凹坑与平面反射不同，解释为 1 或 0 | 用光“读盲文” | P1-HW-04 |
| Solid state (flash) memory | Data is stored by trapping electrons in floating gates of NAND or NOR flash cells; there are no moving parts.（非 MS 原句） | 由 NAND/NOR 闪存单元构成，浮栅在断电时保留电子、控制栅控制电流通过；无活动部件 | 一排排能把电子“关起来”的小格子 | P1-HW-04 |
| Resistive touchscreen | 「Resistive: The space between the conductive layers is removed/the layers touch and a circuit is completed」⟦9618_s24_13:7(d)⟧ | 两层导电层，按压使其接触、接通电路，处理器算出触点坐标 | 按下去才算数，戴手套也能用 | P1-HW-05 |
| Capacitive touchscreen | 「Capacitive: The electrical charge changes where the user pressed」⟦9618_s24_13:7(d)⟧ | 触碰改变该处电荷/电场，由变化位置算出坐标 | 手指带走一点电荷，屏幕就知道你点了哪 | P1-HW-05 |
| 3D printer | 「Builds up the model one layer at a time」⟦9618_w23_11:7(a)⟧ | 增材制造：按 CAD 文件从底部开始一层一层堆积材料并固化 | 用挤牙膏的方式一层层垒出模型 | P1-HW-05 |
| Microphone | 「The incoming sound waves cause vibrations of the diaphragm」⟦9618_w21_12:3(a)⟧ | 声波使振膜振动，带动线圈与磁铁相对运动（或改变电容），产生电信号 | 把空气的振动变成电流的振动 | P1-HW-05 |
| Buffer | 「The buffer is used for temporary storage」⟦9618_w24_13:2(b)⟧；「to allow processes / devices to operate at different speeds」⟦9618_w22_13:1(c)⟧ | 在速度不同的设备/进程之间临时存放数据的存储区，使处理器不必等待慢速设备 | 餐厅的出菜台：厨房快速出菜，服务员按自己的节奏取 | P1-HW-06、P1-CM-12 |
| Embedded system | 「combination of hardware and software designed for a specific function」⟦9618_w22_13:10(b)(ii)⟧；「the embedded system is built into / integrated (into the car alarm)」⟦9618_w22_13:10(b)(ii)⟧ | 内置于更大系统、为一项特定功能设计的软硬件组合（有处理器、存储器、I/O），固件不易被用户修改 | 洗衣机里那块只会管洗衣程序的小电脑 | P1-HW-07 |
| Firmware | Software stored permanently in ROM / EEPROM that controls the hardware of a device.（非 MS 原句） | 固化在 ROM/EEPROM 中、控制设备硬件的软件 | 出厂时“焊”进设备的程序 | P1-HW-01、P1-HW-03、P1-HW-07 |
| Monitoring system | 「Monitoring systems do not take any action」⟦9618_w25_11:9⟧ | 只用传感器采集、记录或显示数据，不采取行动改变环境的系统 | 体温计：只量不治 | P1-HW-08 |
| Control system | 「control systems act autonomously to change the environment if the values are out of a prescribed range」⟦9618_w25_11:9⟧ | 当读数超出设定范围时，自主用执行器改变环境、并利用反馈的系统 | 恒温空调：量了还会动手调 | P1-HW-08 |
| Feedback | 「Feedback ensures that a system operates within set criteria / constraints」⟦9618_w23_11:9(a)⟧；「by enabling system output to affect (subsequent) system input」⟦9618_w23_11:9(a)⟧ | 系统的输出影响后续输入，使系统能自动调整、保持在设定条件内 | 开车时看路调方向盘：动作的结果又成了下一步的依据 | P1-HW-08 |
| Sensor | An input device that measures a physical quantity and sends the data to the processor.（非 MS 原句） | 测量物理量（温度、压力、光、红外、声音等）并把数据送给处理器的输入设备 | 系统的“眼睛和耳朵” | P1-HW-09 |
| Actuator | 「Actuator generates a signal / causes an action / converts electrical energy into a mechanical force」⟦9618_w23_12:1(b)⟧ | 接收控制信号、把电能转换成机械动作的输出设备 | 系统的“手” | P1-HW-08、P1-HW-09 |
