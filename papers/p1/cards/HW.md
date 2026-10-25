## HW　硬件 {#ch-HW}

<!-- auto:chapter-stats -->

### 核心思想

这一章讲计算机系统里**处理器以外的硬件**：数据存在哪、从哪进来、往哪出去，以及专用的小系统怎样感知和控制外部世界。

1. **存储器**（HW-01 至 HW-04）：主存里 RAM 放“正在用的”、ROM 放“开机就要、永远不变的”（HW-01）；RAM 又分 SRAM 与 DRAM（HW-02）；ROM 又分 PROM、EPROM、EEPROM（HW-03）；辅存有磁盘、固态、光盘三种原理（HW-04）。
2. **外设与速度差**（HW-05、HW-06）：触摸屏、麦克风、3D 打印机、VR 头显怎样工作（HW-05）；处理器比外设快得多，所以中间要放缓冲区（HW-06）。
3. **专用系统**（HW-07 至 HW-09）：嵌在更大设备里、只做一件事的嵌入式系统（HW-07）；它们常常是监测系统或控制系统，区别在于有没有执行器和反馈（HW-08）；系统的“眼睛”是传感器，“手”是执行器（HW-09）。

这一章的题多是“对比 + 理由”：SRAM 对 DRAM、EPROM 对 EEPROM、磁盘对固态、监测对控制。答题时**两边成对写**，并把理由落到题目的设备上（“the CCTV computer is working all the time, so …”）。

**心智模型**　整章可以从两幅图推出来。①**速度阶梯**：处理器最快，寄存器与缓存次之，RAM 再慢（SRAM 比 DRAM 快但贵、密度低，所以 SRAM 做缓存、DRAM 做主存），辅存慢几个数量级（固态快于磁盘，磁盘快于光盘），外设最慢。阶梯上每相邻两级之间的速度差就是一道题：为什么要有 RAM（辅存太慢）、为什么 ROM 放固件（开机时 RAM 还是空的）、为什么要缓冲区（HW-06：两级速度不同，中间放一块临时存放区）、选固态还是磁盘（HW-04：速度、容量、价格、抗震，落到题目的设备上）。②**感知—判断—执行环**：传感器把物理量变成数字量送给处理器（常经 ADC），处理器按程序比较、判断，执行器把数字信号变回动作（常经 DAC）。只走前半环（传感器 → 处理器 → 显示或记录）是监测系统；环闭合（处理器 → 执行器改变环境 → 传感器再读到变化）才是控制系统（HW-08、HW-09）；嵌入式系统是把这个环装进一台专用设备（HW-07）。看到一道 HW 题，先问“它在阶梯的哪两级之间”或“它在环的哪一段”，答案的骨架就有了。

### 题型树
<!-- auto:type-tree -->

### P1-HW-01　主存：RAM 与 ROM　{#P1-HW-01}

<!-- auto:stats P1-HW-01 -->

**考法**　①RAM 与 ROM 的区别；②在某个设备（嵌入式系统、监控主机、洗衣机）里 RAM、ROM 各存什么或各自的用途；③为什么嵌入式系统要用 ROM；④情境中哪些数据放主存、哪些放辅存。

**识别信号**　Random Access Memory (RAM) … Read Only Memory (ROM)；Describe two differences between RAM and ROM；Describe the contents of the ROM；Explain the reasons why ROM is used in an embedded system；Identify … data … stored in primary memory。

**解题思路**
1. 对比三根轴：**可写性**（RAM 可读可写，ROM 只读/内容不能改）；**易失性**（RAM 断电丢失，ROM 断电保留）；**内容**（RAM 放正在运行的程序和数据，ROM 放启动指令/固件/BIOS）。
2. 情境题落到设备：RAM 里是“当前正在用的”——当前传感器读数、刚录的视频、用户选的洗衣程序、剩余时间、正在执行的指令；ROM 里是“开机就要、不变的”——启动程序、固件、操作系统内核。
3. “为什么用 ROM”：内容不需要改；断电后必须保留；用来存启动指令/固件。
4. 主存 vs 辅存：只在本次运行期间需要 → 主存；关机后还要保留 → 辅存（例：本次行程里程 → 主存；累计总里程 → 辅存）。

**得分表述**（引自对应 MS）
- 「RAM is volatile, ROM is non-volatile」⟦9618_s26_12:6(c)⟧
- 「to store data that does not change」⟦9618_w22_12:3(c)⟧
- 「data must be stored even when device is without power」⟦9618_w22_12:3(c)⟧
- 「to store boot up instructions / system software / firmware / BIOS」⟦9618_w22_12:3(c)⟧
- 「One item that is stored in RAM is currently running software/data/part of OS」⟦9618_s22_11:2(a)(i)⟧
- 「Instructions being executed」⟦9618_s24_11:2(c)(i)⟧

**易错与失分**
- 写“ROM stores the operating system”：MS 接受的是启动指令、BIOS、OS 的**内核/部分**，不是整个 OS。
- RAM 用途写成“stores files”：长期保存文件是辅存的事。
- 情境题写一般答案（“stores data”）：要写出这台设备的具体数据（“the current reading from the motion sensor”）。

#### 代表题精讲　⟦9618_w22_12:3(c)⟧

**在考什么**　嵌入式系统里有 ROM 和 RAM。Explain the reasons why ROM is used in an embedded system. 2 分，MS 3 点取 2。

**完整作答**　嵌入式系统的启动指令和固件是固定的，不需要改动，正适合放在只读存储器里；而且这些指令在设备断电后必须仍然保存，下次通电才能立即启动——ROM 是非易失的，正好满足。

**与 MS 对齐**　“to store data that does not change”“data must be stored even when device is without power”“to store boot up instructions / system software / firmware / BIOS”，三点任写两点。

**英文作答句**　ROM is used to store the boot-up instructions / firmware, which is data that does not change. The data must be stored even when the device is without power, and ROM is non-volatile.

**下一道变式**　⟦9618_s24_11:2(c)(i)⟧　（视频门铃：写出两项存放在主存里的数据。）

<!-- auto:drills P1-HW-01 -->

### P1-HW-02　SRAM 与 DRAM　{#P1-HW-02}

<!-- auto:stats P1-HW-02 -->

**考法**　①列出 SRAM 与 DRAM 的两三个区别；②在某设备里用 DRAM（而不是 SRAM）的优点或缺点；③解释为什么某处用 SRAM；④填空：SRAM 由触发器构成、DRAM 由晶体管和电容构成。

**识别信号**　Dynamic RAM (DRAM) … Static RAM (SRAM)；advantages / disadvantages of using DRAM instead of SRAM；Explain why Static RAM is used in … instead of Dynamic RAM；State three differences。

**解题思路**
1. 从**结构**推出一切：SRAM 每位用一个**触发器**（flip-flop）保存，不会漏电 → **不需要刷新** → 访问**更快**，但每位用的晶体管多 → **贵**、**密度低** → 用在**缓存**。DRAM 每位用一个晶体管 + 一个**电容**保存电荷，电荷会漏 → **需要不断刷新** → 访问**较慢**，但结构简单 → **便宜**、**密度高**（每片容量大）→ 用在**主存**。
2. 区别题每点写成一对：“DRAM … whereas SRAM …”。
3. 优缺点题看问的是谁“instead of”谁：DRAM 的优点 = 便宜、密度高；DRAM 的缺点 = 要刷新、慢。
4. 设备情境：存大量数据又不要求极快（打印机存打印数据）→ DRAM；要快（CPU 缓存）→ SRAM。

**得分表述**（引自对应 MS）
- 「DRAM stores each bit as charge SRAM uses flip-flop to store each bit」⟦9618_w25_11:6(c)⟧
- 「DRAM is less expensive to manufacture SRAM is more expensive to manufacture」⟦9618_w25_11:6(c)⟧
- 「DRAM has slower access speeds SRAM has faster access times」⟦9618_w25_11:6(c)⟧
- 「DRAM is used in main memory SRAM is used in cache」⟦9618_w25_11:6(c)⟧
- 「Static RAM has faster access time」⟦9618_w23_13:7(a)⟧
- 「because it does not need to be refreshed」⟦9618_w23_13:7(a)⟧

**易错与失分**
- 把“refresh”说反：需要刷新的是 **DRAM**（Dynamic，电荷会漏）。
- “DRAM is cheaper”与“DRAM costs less per unit”是同一个点，算一分。
- 优点/缺点题答反方向：“disadvantages of using DRAM instead of SRAM”要写 DRAM 的缺点（刷新、慢），不是 SRAM 的缺点。

#### 代表题精讲　⟦9618_w25_11:6(c)⟧

**在考什么**　State three differences between DRAM and SRAM. 3 分，MS 6 点取 3。

**完整作答**
1. DRAM 需要不断刷新，SRAM 不需要刷新。
2. DRAM 用电容以电荷形式存每一位，SRAM 用触发器存每一位。
3. DRAM 访问速度较慢，SRAM 访问更快。
（还可写：DRAM 制造更便宜；DRAM 存储密度更高；DRAM 用作主存、SRAM 用作缓存。）

**与 MS 对齐**　①“DRAM requires to be refreshed/charged SRAM does not request a refresh”；②“DRAM stores each bit as charge SRAM uses flip-flop to store each bit”；③“DRAM has slower access speeds SRAM has faster access times”。

**英文作答句**　1. DRAM needs to be refreshed, whereas SRAM does not. 2. DRAM stores each bit as charge in a capacitor, whereas SRAM uses a flip-flop to store each bit. 3. DRAM has slower access speeds, whereas SRAM has faster access times.

**直观**　DRAM 像漏水的小水桶，得不停加水（刷新）；SRAM 像拨好的开关，拨在哪就停在哪，所以读起来快，但每个开关零件多、贵。

**下一道变式**　⟦9618_w23_13:7(a)⟧　（解释为什么笔记本电脑用 SRAM 而不用 DRAM。）

<!-- auto:drills P1-HW-02 -->

### P1-HW-03　PROM、EPROM 与 EEPROM　{#P1-HW-03}

<!-- auto:stats P1-HW-03 -->

**考法**　①解释三者的区别；②EPROM 与 EEPROM 的两个区别；③按描述写出存储器名称（填表）；④在设备（VR 头显、嵌入式系统）里用 EEPROM 的好处/理由；⑤已给 PROM，命名并描述另外两种 ROM。

**识别信号**　Programmable ROM (PROM) / Erasable Programmable ROM (EPROM) / Electrically Erasable Programmable ROM (EEPROM)；Explain the benefits of using EEPROM instead of other types of ROM；the type of memory technology for each description。

**解题思路**
1. 三者沿“能不能改、怎么改”排开：
   - **PROM**：出厂后只能写**一次**。
   - **EPROM**：用**紫外线**擦除，必须从电路板上**取下**，擦除时**整片**全擦，之后可重写多次。
   - **EEPROM**：用**电信号**擦除，**原位**（in situ）擦写，可以只擦**部分**（某个字节），可多次擦写。
2. EEPROM 的好处落到设备：固件可以频繁更新以获得新功能；不需要取出芯片；不需要先把固件全部擦掉；普通用户无需专门设备就能升级。
3. 区别题成对写：“EPROM … whilst EEPROM …”。

**得分表述**（引自对应 MS）
- 「PROM can be set once, EPROM and EEPROM can be overwritten multiple times」⟦9618_s22_11:2(a)(ii)⟧
- 「EPROM needs to be removed from device EEPROM can be erased in situ」⟦9618_s22_11:2(a)(ii)⟧
- 「EPROM uses ultraviolet light to erase data whilst EEPROM uses an electrical signal to do this」⟦9618_w24_12:2(c)⟧
- 「EPROM erases all the data, EEPROM can erase parts of the data」⟦9618_w24_12:2(c)⟧
- 「EEPROM allows frequent/multiple read/write/erase operations」⟦9618_s24_12:2(c)⟧
- 「without removing the chip(s)/firmware from the headset」⟦9618_s24_12:2(c)⟧

**易错与失分**
- 把 EPROM 的擦除方式写成“electrically”：E**E**PROM 多出来的那个 E 才是 Electrically。
- “EEPROM can be changed”太泛：要说**怎样**改（电信号、原位、可部分擦除）或**改了有什么用**（更新固件、获得新功能）。
- 已给 PROM 时再写 PROM 不得分（⟦9618_s26_13:8(a)⟧ 要的是另外两种）。

#### 代表题精讲　⟦9618_s22_11:2(a)(ii)⟧

**在考什么**　Explain the difference between PROM, EPROM and EEPROM. 3 分，MS 4 点取 3。

**完整作答**　PROM 只能写入一次，EPROM 和 EEPROM 可以反复改写多次。EPROM 要从设备中取下才能擦除，EEPROM 可以在设备里原位擦除。EPROM 用紫外线擦除，EEPROM 用电压擦除。（还可写：EPROM 改写前必须整片擦除，EEPROM 不必。）

**与 MS 对齐**　“PROM can be set once, EPROM and EEPROM can be overwritten multiple times”→“EPROM needs to be removed from device EEPROM can be erased in situ”→“EPROM and can be erased using UV light, EEPROM can be erased using voltage”→“EPROM must be entirely erased before rewriting, EEPROM does not have to be entirely erased before rewriting”。

**英文作答句**　PROM can be set once, whereas EPROM and EEPROM can be overwritten multiple times. EPROM needs to be removed from the device to be erased, whereas EEPROM can be erased in situ. EPROM is erased using UV light, whereas EEPROM is erased using a voltage.

**下一道变式**　⟦9618_s24_12:2(c)⟧　（VR 头显里用 EEPROM 的好处，要扣设备。）

<!-- auto:drills P1-HW-03 -->

### P1-HW-04　存储设备原理与选择　{#P1-HW-04}

<!-- auto:stats P1-HW-04 -->

**考法**　①描述磁性硬盘的工作原理（常 4–5 分，或填空）；②描述光盘读写器的原理；③固态（闪存）存储的原理（NAND/NOR、浮栅、控制栅，填表）；④为情境论证“磁盘比固态更合适”（“理由 + 情境展开”成对给分）。

**识别信号**　Describe the principal operation(s) of a magnetic hard disk / optical disc reader/writer / solid state (flash) memory；platters / read/write head / laser / pits and lands；NAND / NOR / floating gate；reasons why magnetic storage is more appropriate than solid state storage。

**解题思路**
1. **磁盘**：一个或多个可磁化的**盘片**装在**主轴**上高速旋转 → **读写磁头**装在臂上移到盘面上方 → 盘面分成同心**磁道**和**扇区** → 写入时磁头中的电流变化产生磁场变化，把数据存成磁化图案；读取时磁场变化在磁头中产生电流变化。
2. **光盘**：光盘高速旋转 → 激光照射盘面，光学头移到位置，沿螺旋轨道由内向外 → 写入时激光烧出**凹坑**（pits）→ 读取时凹坑与平面（lands）反射不同 → 差异解释为 1 或 0。
3. **固态**：由 NAND 或 NOR 门构成；每个存储单元 1 或 2 个晶体管；**浮栅**在断电时保留电子，**控制栅**控制电流是否通过。没有活动部件。
4. **磁盘 vs 固态**（选磁盘时）：每单位存储成本更低 → 大量视频需要大容量，花费更少；频繁不断的读写 → 磁盘寿命更长。每个理由都要接一句情境展开。

**得分表述**（引自对应 MS）
- 「The computer will have a large number of read/write operations because it is working all the time」⟦9618_s23_11:4(b)⟧
- 「magnetic storage has more longevity」⟦9618_s23_11:4(b)⟧
- 「Magnetic storage costs less per storage unit」⟦9618_s23_11:4(b)⟧
- 「videos are large files and therefore very large storage capacity is required」⟦9618_s23_11:4(b)⟧
- 「When reading the laser reflects from pits and lands」⟦9618_w24_11:3(d)(i)⟧
- 「When reading from disk, a variation in magnetic field produces a variation in current through the head」⟦9618_s22_11:2(b)⟧

**易错与失分**
- 论证题只写“cheaper”“lasts longer”不展开：MS 是“理由 1 分 + 对应情境 1 分”，没有情境只得一半。
- 写“magnetic disks are faster”：恰恰相反，固态更快；选磁盘的理由是成本与寿命。
- 光盘写成“laser reads magnetic patterns”，或磁盘写成“laser”：两种原理别串。
- 固态填表：“能在断电时保留电子”的是 floating gate，“控制电流通过”的是 control gate（⟦9618_s24_11:2(c)(ii)⟧，讲解时请对照原卷 QP p.4）。

#### 代表题精讲　⟦9618_s23_11:4(b)⟧

**在考什么**　联网 CCTV 系统的中央计算机把视频文件存到辅存。Describe two reasons why magnetic storage is more appropriate than solid state storage for this computer. 4 分：每个理由 1 + 对应展开 1（讲解时请对照原卷 QP p.10）。

**完整作答**
1. 这台计算机一直在工作，读写操作次数非常多；磁性存储在大量读写下寿命更长。
2. 磁性存储每单位容量的成本更低；视频文件很大，需要非常大的存储容量，用磁盘便宜得多。

**与 MS 对齐**　理由 1 ←“The computer will have a large number of read/write operations because it is working all the time”+“.. magnetic storage has more longevity”；理由 2 ←“Magnetic storage costs less per storage unit”+“… videos are large files and therefore very large storage capacity is required”。

**英文作答句**　1. The computer will have a large number of read/write operations because it is working all the time, and magnetic storage has more longevity. 2. Magnetic storage costs less per storage unit, and the videos are large files, so a very large storage capacity is required.

**下一道变式**　⟦9618_w24_11:3(d)(i)⟧　（转到原理题：光盘读写器怎样工作。）

<!-- auto:drills P1-HW-04 -->

### P1-HW-05　输入输出设备原理　{#P1-HW-05}

<!-- auto:stats P1-HW-05 -->

**考法**　描述某个设备的工作原理（principal operation），常以填空出现：触摸屏（电阻式/电容式，怎样把触点变成菜单选择）、麦克风、3D 打印机、VR 头显；偶有判断题（电阻式触摸屏的说法真假）。3–5 分。

**识别信号**　Describe the principal operation of a touchscreen / microphone / 3D printer；resistive / capacitive touchscreen；Complete the description of the principal operation of a VR headset；Explain how a touchscreen converts the point of touch to a selection；Explain how the model will be printed using a 3D printer。

**解题思路**
1. **电阻式触摸屏**：两层导电层；按下时两层接触，电路接通 → 处理器算出触点的 x、y 坐标。任何物体按压都能用。
2. **电容式触摸屏**：多层；手指触碰改变该处的电荷/电场（电流变化）→ 由变化位置算出坐标。
3. **触点 → 菜单选择**：确定 x、y 坐标 → 找出该坐标对应的菜单项 → 执行（加入订单）。
4. **麦克风**：振膜 → 声波使振膜振动 → 带动线圈在磁铁旁移动（动圈式；或改变电容 / 使晶体变形）→ 产生电信号。
5. **3D 打印机**：增材制造；用 CAD / 3D 建模软件生成的数字文件；从底部开始**一层一层**堆积，每层重复；材料熔融挤出（FDM）或树脂被紫外激光固化（SLA）等。
6. **VR 头显**：一两个显示屏输出图像；陀螺仪/加速度计检测头部运动，微处理器分析运动方向与速度；有的用摄像头跟踪眼球。

**得分表述**（引自对应 MS）
- 「Resistive: The space between the conductive layers is removed/the layers touch and a circuit is completed」⟦9618_s24_13:7(d)⟧
- 「Capacitive: The electrical charge changes where the user pressed」⟦9618_s24_13:7(d)⟧
- 「The software/microprocessor calculates the coordinates」⟦9618_s24_13:7(d)⟧
- 「The incoming sound waves cause vibrations of the diaphragm」⟦9618_w21_12:3(a)⟧
- 「Builds up the model one layer at a time」⟦9618_w23_11:7(a)⟧
- 「This sensor is a gyroscope/accelerometer」⟦9618_s24_12:2(a)⟧

**易错与失分**
- 触摸屏只写“detects the touch”：要写出**机制**（两层接触 / 电荷变化）和**坐标**两步。
- 3D 打印写成“prints the object”：关键词是 additive、layer by layer、CAD file。
- 填空题按意思填却用了口语词：用 MS 的术语（circuit、coordinates、gyroscope）。

#### 代表题精讲　⟦9618_s24_13:7(d)⟧

**在考什么**　餐厅机器人上有触摸屏供顾客付款。Describe the principal operation of a touchscreen. 4 分，MS 5 点取 4。

**完整作答**　如果是电阻式触摸屏：屏幕有两层导电层，用户按下时两层之间的空隙消失、两层接触，电路接通。如果是电容式：用户触碰的位置电荷发生变化。无论哪种，系统都根据电场的变化确定接触点，再由软件/微处理器计算出触点的坐标。

**与 MS 对齐**　“Resistive: The space between the conductive layers is removed/the layers touch and a circuit is completed”“Capacitive: The electrical charge changes where the user pressed”“The point of contact is identified”“... from the change in electrical field”“The software/microprocessor calculates the coordinates”。

**英文作答句**　In a resistive touchscreen, the space between the conductive layers is removed when the user presses, so the layers touch and a circuit is completed. In a capacitive touchscreen, the electrical charge changes where the user pressed. The point of contact is identified from the change in the electrical field, and the microprocessor calculates the coordinates.

**下一道变式**　⟦9618_w23_11:7(a)⟧　（换成 3D 打印机的工作原理。）

<!-- auto:drills P1-HW-05 -->

### P1-HW-06　缓冲区　{#P1-HW-06}

<!-- auto:stats P1-HW-06 -->

**考法**　①缓冲区的作用/目的，再举一个例子；②描述某个具体传输中怎样使用缓冲区：计算机 → 硬盘/光盘、计算机 → 激光打印机、计算机 → VR 头显、视频门铃；③一句话说明为什么某设备需要缓冲区。3–4 分。

**识别信号**　buffer / memory buffer；Describe how … will use the buffer；Explain the use of a buffer when writing data to …；Describe the purpose of the buffer；State why a 3D printer needs a buffer。

**解题思路**
1. **为什么要**：计算机（处理器）与外设收发数据的**速度不同**。
2. **是什么**：一块**临时存储**区。
3. **怎么用**（按顺序写）：计算机以**高速**把数据送入缓冲区 → 计算机**不必等待**、可以去做别的事 → 外设以**自己较慢的速度**从缓冲区取数据 → 缓冲区**空**（或满）时发**中断**给计算机，请求更多数据（或暂停发送）。
4. 情境题把“外设”换成题目里的设备名，并说清数据流向（门铃：摄像头 → 缓冲区 → 智能手机 / 辅存）。

**得分表述**（引自对应 MS）
- 「The buffer is used for temporary storage」⟦9618_w24_13:2(b)⟧
- 「so that the computer can transfer data to the buffer at the higher speed」⟦9618_w24_13:2(b)⟧
- 「and is not held up waiting for data to transfer」⟦9618_w24_13:2(b)⟧
- 「and so that data is transferred to hard disk drive from the buffer at the slower rate」⟦9618_w24_13:2(b)⟧
- 「When the buffer is empty an interrupt is sent to the laptop」⟦9618_w23_13:7(c)⟧
- 「to allow processes / devices to operate at different speeds」⟦9618_w22_13:1(c)⟧

**易错与失分**
- 只写“stores data temporarily”：那只是一个点，没说**为什么**（速度不同）和**带来什么**（处理器不用等）。
- 把缓冲区说成“speeds up the printer”：外设速度不变，变快的是计算机不再被拖住。
- 中断的方向说反：是**外设一侧**（缓冲区空/满时）向计算机发中断请求更多数据。
- 打印机题只写缓冲区，不提“用户可以继续使用笔记本”这一后果。

#### 代表题精讲　⟦9618_w24_13:2(b)⟧

**在考什么**　Explain how a memory buffer is used when a computer is transferring data to its magnetic hard disk drive. 4 分，MS 5 点取 4。

**完整作答**　计算机发送数据的速度比硬盘接收的速度快，两者速度不同。缓冲区用作临时存储：计算机以较高的速度把数据传进缓冲区，于是不会被拖住、不必等待数据慢慢写完；硬盘再以自己较慢的速度从缓冲区取数据写入。

**与 MS 对齐**　“The computer and the hard disk drive transmit and receive at different speeds // The computer transfers data faster than the HDD can receive”→“The buffer is used for temporary storage”→“… so that the computer can transfer data to the buffer at the higher speed”→“... and is not held up waiting for data to transfer”→“… and so that data is transferred to hard disk drive from the buffer at the slower rate”。

**英文作答句**　The computer transfers data faster than the HDD can receive it. The buffer is used for temporary storage, so the computer can transfer data to the buffer at the higher speed and is not held up waiting for the data to transfer. The data is then transferred to the hard disk drive from the buffer at the slower rate.

**下一道变式**　⟦9618_w23_13:7(c)⟧　（激光打印机：多了“缓冲区空时发中断请求更多数据”。）

<!-- auto:drills P1-HW-06 -->

### P1-HW-07　嵌入式系统　{#P1-HW-07}

<!-- auto:stats P1-HW-07 -->

**考法**　①描述嵌入式系统的特征；②解释某设备（电视、车道检测、视频门铃、健康监测器）为什么是嵌入式系统；③举例并解释；④嵌入式系统的缺点。

**识别信号**　embedded system；Explain why … is an example of an embedded system；Identify two characteristics … that suggest it is an embedded system；Describe the drawbacks of embedded systems。

**解题思路**
1. 四个特征（每个都能落到设备上）：**内置/集成**在一个更大的系统里；软硬件结合、**专用于一项特定功能**；必须有处理器、存储器与输入/输出；**固件**不容易被用户修改/更新。
2. “为什么是嵌入式系统”：把四个特征逐条套到题目设备上（“the lane detection system is built into the car”“it only performs one task”）。
3. 缺点：用户难以更新固件；故障难修、维修是专业活且贵；功能难扩展、难改作他用；坏了常直接丢弃 → 电子垃圾。

**得分表述**（引自对应 MS）
- 「the embedded system is built into / integrated (into the car alarm)」⟦9618_w22_13:10(b)(ii)⟧
- 「combination of hardware and software designed for a specific function」⟦9618_w22_13:10(b)(ii)⟧
- 「must have a processor, memory and input / output」⟦9618_w22_13:10(b)(ii)⟧
- 「The system is not easily changed/updated by the car owner」⟦9618_w22_13:10(b)(ii)⟧
- 「Dedicated to a single task // limited number of functions」⟦9618_w23_12:1(c)(i)⟧
- 「It is difficult to change / update the firmware by the user」⟦9618_w24_12:2(a)⟧

**易错与失分**
- 解释题不扣设备：MS 写“applied to example”，泛泛而谈的特征可能不给分。
- 写“small computer”：大小不是特征，关键是“专用 + 内置于更大系统”。
- 缺点写成“expensive”：MS 的缺点集中在难更新、难维修、难改作他用。

#### 代表题精讲　⟦9618_w22_13:10(b)(ii)⟧

**在考什么**　汽车防盗报警器是嵌入式系统。Describe the characteristics of an embedded system. 3 分，MS 4 点取 3。

**完整作答**　嵌入式系统内置于更大的系统中——这里集成在汽车报警器里；它是为一项特定功能设计的硬件与软件的组合；它必须有处理器、存储器和输入/输出；车主不能轻易修改或更新这个系统。

**与 MS 对齐**　“the embedded system is built into / integrated (into the car alarm)”“combination of hardware and software designed for a specific function”“must have a processor, memory and input / output”“The system is not easily changed/updated by the car owner”。

**英文作答句**　The embedded system is built into the car alarm. It is a combination of hardware and software designed for a specific function. It must have a processor, memory and input/output, and it is not easily changed or updated by the car owner.

**下一道变式**　⟦9618_w24_12:2(a)⟧　（反面：嵌入式系统的缺点。）

<!-- auto:drills P1-HW-07 -->

### P1-HW-08　监测系统与控制系统　{#P1-HW-08}

<!-- auto:stats P1-HW-08 -->

**考法**　①判断情境中的系统是监测还是控制并论证——**判断本身不给分**，分数全在理由；②描述两者的区别；③解释反馈在控制系统中的作用/重要性。2–3 分。

**识别信号**　State / Explain whether … is a monitoring system or a control system. Justify；Describe the differences between a monitoring system and a control system；Explain the importance of feedback in a control system；Describe how feedback is used。

**解题思路**
1. 判断标准一句话：**输出会不会改变下一次的输入**。会 → 控制系统（有执行器、有反馈）；不会 → 监测系统（只记录/报警）。
2. 控制系统的理由：使用**执行器**改变环境（开门、刹车、开制冷）→ 改变后的状态又被传感器读到（**反馈**）→ 系统自主地据此继续调整。
3. 监测系统的理由：只记录或显示/发送数据，灯与警报只是**提示**；输出不影响传感器的下一次输入；**没有执行器**、没有反馈。
4. 反馈的重要性（三点链）：保证系统在设定的条件内运行 → 因为输出能影响后续输入 → 从而能自动调整条件。

**得分表述**（引自对应 MS）
- 「Monitoring systems do not take any action whereas control systems act autonomously to change the environment if the values are out of a prescribed range」⟦9618_w25_11:9⟧
- 「Control systems use actuators monitoring systems do not have any actuators」⟦9618_w25_11:9⟧
- 「Feedback ensures that a system operates within set criteria / constraints」⟦9618_w23_11:9(a)⟧
- 「by enabling system output to affect (subsequent) system input」⟦9618_w23_11:9(a)⟧
- 「thus allowing conditions to be automatically adjusted」⟦9618_w23_11:9(a)⟧
- 「The output of the floodlight or the audio alarm does not affect the input of data from the sensors」⟦9618_w24_11:5(c)⟧

**易错与失分**
- 只写“Control system”不写理由：0 分（No mark for identification）。
- 把“有报警/有灯/会发消息”当成控制：报警和警示牌只是输出提示，不改变被测量的量（⟦9618_w24_12:9(b)⟧、⟦9618_w24_11:5(c)⟧ 都是监测）。
- 理由不扣情境：要写“braking changes the distance to the object, and this new distance is used to decide how hard to brake”，而不是只抄定义。

#### 代表题精讲　⟦9618_w24_13:3⟧

**在考什么**　汽车自动刹车：传感器测前方物体距离，太近或接近太快就刹车，越近刹得越重。Explain the reasons why the automatic braking system of the car is a control system. 3 分，MS 5 点取 3。

**完整作答**　这个系统使用反馈，并且独立自主地行动。传感器输入的距离数据使汽车刹车；刹车又改变了汽车与物体之间的距离；这个新的距离再被传感器读入，用来决定是否需要刹车、刹多重。

**与 MS 对齐**　“The system uses feedback”“The system acts independently”“Input data causes the car to brake”“… braking decreases the/changes the distance to the object”“… this new distance is used to determine whether/how hard the car needs to brake”。

**英文作答句**　The system uses feedback and acts independently. The input data causes the car to brake; braking changes the distance to the object, and this new distance is used to determine whether and how hard the car needs to brake.

**直观**　空调遥控器设 24°C：室温高了制冷，制冷让室温下降，新室温又决定要不要继续制冷——这条“输出 → 改变输入”的回路就是反馈；只看温度计不开空调，就是监测。

**下一道变式**　⟦9618_w24_12:9(b)⟧　（桥梁超限警示系统：结论是监测，理由反过来写。）

<!-- auto:drills P1-HW-08 -->

### P1-HW-09　传感器与执行器　{#P1-HW-09}

<!-- auto:stats P1-HW-09 -->

**考法**　①为情境选一或两种传感器并说明各自用途（“传感器 + 用途”成对给分）；②为几个场景各选最合适的传感器（全对才得分）；③描述执行器在系统中的作用；④描述某传感器在设备中的作用（3D 打印机的温度传感器）。

**识别信号**　Identify one (appropriate) type of sensor … State how / purpose；Complete the table by identifying two sensors … and the purpose of each；Describe the purpose of a temperature sensor within …；Describe the role of an actuator。

**解题思路**
1. 常用传感器与它测的量：**pressure**（重量、有没有东西压上/拿走、碰撞）；**infra-red**（光束被挡断、有人/障碍物在附近、高度检测）；**light**（光照强度）；**temperature**（温度）；**sound**（声音）；**proximity**（距离/接近）。
2. 用途要写成“检测什么 → 在这个系统里用来做什么”：“Pressure sensor — detects when an item is removed from the shelf”。
3. 执行器：接收控制信号，把电能转成**机械动作**（推杆、开门、开活板），完成系统要做的动作。
4. 选择时避免写品牌或“camera”（不是传感器题的常规答案，除非 MS 列出）。

**得分表述**（引自对应 MS）
- 「Detects when the pressure of an item is removed from a shelf / put back on a shelf」⟦9618_s25_11:4(b)⟧
- 「To detect if there is an obstacle in the way」⟦9618_s24_13:7(a)⟧
- 「Measure / check the weight of the vehicle」⟦9618_w24_12:9(a)⟧
- 「To prevent overheating // ensure material is hot enough」⟦9618_w23_11:7(b)⟧
- 「Actuator generates a signal / causes an action / converts electrical energy into a mechanical force」⟦9618_w23_12:1(b)⟧
- 「to push an arm // to open a trap door」⟦9618_w23_12:1(b)⟧

**易错与失分**
- 传感器选对但用途不扣情境：MS 要“sensor and its use **in this system**”。
- “motion sensor”在多数 MS 里不是标准答案；检测人或物体靠近写 infra-red / proximity。
- 执行器写成“detects …”：检测是传感器的事，执行器负责**动作**。

#### 代表题精讲　⟦9618_s24_13:7(a)⟧

**在考什么**　餐厅送餐机器人导航到餐桌。Complete the table by identifying two sensors that can be included in the robot and the purpose of each sensor in the navigation system. 2 分：每行“传感器 + 对应用途”1 分（讲解时请对照原卷 QP p.13 的表格）。

**完整作答**

| Sensor | Purpose in navigation system |
|:--|:--|
| Infra-red | 检测前方路上是否有障碍物 // 指示已到达目标餐桌 |
| Pressure | 检测是否撞到桌子或其他障碍物 // 检测托盘上的食物是否被放上/取走，以便继续移动 |

（MS 还接受 sound：检测有人说话，以便用 AI 识别语音、判断是否需要停下。）

**与 MS 对齐**　每行必须传感器与用途**配对**：Infra-red ←“To detect if there is an obstacle in the way”；Pressure ←“To detect if a table or other obstacle has been hit”。

**英文作答句**　Infra-red sensor: to detect if there is an obstacle in the way. Pressure sensor: to detect if a table or other obstacle has been hit.

**下一道变式**　⟦9618_w23_12:1(b)⟧　（换成执行器：描述执行器在剔除重量不合格巧克力的系统中的作用。）

<!-- auto:drills P1-HW-09 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| HW-01 vs HW-02 vs HW-03 | RAM 对 ROM → HW-01；SRAM 对 DRAM → HW-02；PROM/EPROM/EEPROM → HW-03 | 题干里的缩写 |
| SRAM vs DRAM | SRAM：触发器、不刷新、快、贵、缓存；DRAM：电容、要刷新、慢、便宜、密度高、主存 | refresh / cache / main memory |
| EPROM vs EEPROM | EPROM：紫外线、取下、整片擦；EEPROM：电信号、原位、可部分擦 | UV light / in situ / electrically |
| HW-04 vs HW-05 | 存储设备（磁盘、固态、光盘）→ HW-04；输入输出设备（触摸屏、麦克风、打印机、VR）→ HW-05 | 设备名 |
| HW-06 vs PF-04 | 缓冲区的用途 → HW-06；中断本身的处理过程 → PF-04 | buffer vs interrupt service routine |
| HW-06 vs CM-12 | 只问缓冲区作用 → HW-06；流媒体整体过程 → CM-12 | bit streaming / media server |
| HW-07 vs HW-08 | “为什么是嵌入式” → HW-07；“监测还是控制” → HW-08 | embedded vs monitoring / control |
| HW-08 vs HW-09 | 判断系统类型、反馈 → HW-08；选传感器、执行器作用 → HW-09 | feedback vs sensor / actuator |
| 监测 vs 控制 | 输出不影响下一次输入、无执行器 → 监测；有执行器、输出改变被测量的量 → 控制 | 报警灯、警示牌只是提示 → 监测 |
