## IR　信息表示：核心概念 {#core-IR}

英文列是可以直接写进答卷的得分句：带 ⟦⟧ 的是该题 MS 原文；标「非 MS 原句」的是标准定义，用于理解与默写，真正作答时仍以所答那题的 MS 为准。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Binary prefix / denary prefix | 「Kibibyte is binary prefix and kilobyte is denary prefix」⟦9618_s23_11:3(d)(i)⟧ | 二进制前缀（kibi、mebi、gibi、tebi）按 2¹⁰ = 1024 的幂计；十进制前缀（kilo、mega、giga、tera）按 10³ = 1000 的幂计 | 同叫“千”，一个是 1024，一个是 1000；存储厂商用 1000，内存天然按 1024 | P1-IR-01、P1-IR-12 |
| Kibibyte vs kilobyte | 「Kibibyte is 1024 bytes and kilobyte is 1000 bytes」⟦9618_s23_11:3(d)(i)⟧ | 1 KiB = 1024 字节；1 kB = 1000 字节 | 每升一级都多乘 1024（或 1000），级数越高差得越多 | P1-IR-01 |
| Binary Coded Decimal (BCD) | Each denary digit is represented by its own 4-bit binary code.（非 MS 原句） | 把十进制数的每一位数字分别用 4 位二进制表示 | 不换算整个数，而是“逐个数字翻译”；所以每 4 位不会超过 1001（9） | P1-IR-02、P1-IR-04 |
| Invalid BCD | 「The denary value in each group of 4 bits is greater than 9」⟦9618_w21_12:4(d)⟧ | 任一 4 位组的值大于 9，就不是合法 BCD | 一个十进制数字最大是 9，4 位却能到 15，多出来的 1010–1111 在 BCD 里没有意义 | P1-IR-02 |
| Two's complement | 「Most significant 1 bit is treated as the corresponding negative denary value」⟦9618_w24_13:8(b)⟧ | 最高位取负位权（8 位为 −128）的有符号整数表示法；负数 = 正数取反加一 | 256 个位模式绕成一圈，−x 放在“再走 x 步回到 0”的位置，所以减法可以用加法做 | P1-IR-03、P1-IR-05 |
| One's complement | A negative number is formed by inverting every bit of the positive number.（非 MS 原句） | 负数 = 对应正数的每一位取反（不加 1） | 比补码少一步“加 1”，代价是 0 有 +0、−0 两种写法 | P1-IR-03 |
| Range of n-bit two's complement | 「Smallest: 1000 0000」⟦9618_s25_12:2(b)(ii)⟧；「Largest: 0111 1111」⟦9618_s25_12:2(b)(ii)⟧ | n 位补码最小 −2ⁿ⁻¹（1 后跟 0），最大 2ⁿ⁻¹ − 1（0 后跟 1） | 负数比正数多一个，因为 0 占了“非负”那一半的一个位置 | P1-IR-03 |
| Overflow | 「The answer cannot be represented in the number of bits available」⟦9618_w24_11:1(d)⟧ | 运算结果超出寄存器位数所能表示的范围 | 三位数里程表 999 再走 1 变 000：不是机器坏了，是格子不够 | P1-IR-05 |
| Character set | 「All of the characters/symbols that the computer can use/represent」⟦9618_s22_13:1(a)(i)⟧ | 计算机能识别、表示的全部字符，每个字符对应唯一编码 | 一本“字符 ↔ 号码”的对照字典，收发双方用同一本才能读懂 | P1-IR-06 |
| Text representation | 「Each character has a unique binary code」⟦9618_s24_13:1(d)(ii)⟧；「The binary code for each character is stored in sequence」⟦9618_s24_13:1(d)(ii)⟧ | 每个字符有唯一二进制码，文本中各字符的码按顺序存储 | 查字典把每个字换成号码，再按原来的顺序排好 | P1-IR-06 |
| ASCII / extended ASCII | 「ASCII has 7 bits whereas extended ASCII has 8 bits」⟦9618_s22_13:1(a)(ii)⟧ | ASCII 每字符 7 位、128 个字符；扩展 ASCII 8 位、256 个字符 | 够写英文，不够写中文 | P1-IR-06 |
| Unicode | 「represents all characters in all languages」⟦9618_w24_13:6(a)⟧ | 每字符可用 16 或 32 位，能表示所有语言的字符及 emoji；包含 ASCII 的全部字符 | 一本全世界通用的大字典，ASCII 是它的前 128 页 | P1-IR-06 |
| Pixel | 「The smallest part of the image」⟦9618_s23_11:1(a)⟧ | 位图中能单独取一种颜色的最小单元 | 十字绣图纸上的一格 | P1-IR-07 |
| Colour depth / bit depth | 「the number of bits used to represent a colour」⟦9618_w24_12:7(a)(i)⟧ | 表示每个像素颜色所用的位数；决定能表示的颜色数（2ⁿ） | 调色盘上颜料的种数由它决定：8 位 256 种，24 位约 1600 万种 | P1-IR-07、P1-IR-08、P1-IR-12 |
| Image resolution | 「Image resolution is the number of pixels wide by pixels high that form the image」⟦9618_s26_12:1(b)⟧ | 组成图像的像素数（宽 × 高） | 图纸有多少格 | P1-IR-07、P1-IR-08 |
| Screen resolution | 「screen resolution is the number of pixels wide by pixels high that can be displayed on a screen」⟦9618_s26_12:1(b)⟧ | 屏幕能显示的像素数（宽 × 高） | 屏幕有多少格；改它不改图像文件 | P1-IR-07 |
| File header | 「stores data about the image file / metadata」⟦9618_w24_12:7(a)(i)⟧ | 文件开头存放关于图像本身的数据（类型、尺寸、色深、压缩方式等） | 包裹上的快递单：不是货物，但告诉你怎么拆 | P1-IR-07 |
| Vector graphic | 「Vector graphic store a set of instructions about how to draw the shape」⟦9618_w21_12:5(b)(i)⟧ | 用绘图对象及其属性（数学描述）存储图像，显示时按指令计算绘制 | 存的是“画法”而不是“画好的格子”，放大时重新画，所以不糊 | P1-IR-09 |
| Drawing object | 「A drawing object is an individual element of an image, for example: a line, a square」⟦9618_s26_11:5(b)⟧ | 矢量图中的单个元素，如一条线、一个矩形 | 积木里的一块 | P1-IR-09 |
| Property | 「an attribute of a drawing object」⟦9618_w24_12:7(b)⟧ | 绘图对象的一项属性，定义其外观的一个方面（颜色、线宽、坐标等） | 这块积木的颜色和尺寸 | P1-IR-09 |
| Drawing list | 「all the drawing objects/shapes in an image」⟦9618_w24_12:7(b)⟧ | 图中全部绘图对象及画出它们所需命令的清单 | 整套积木的拼装说明书 | P1-IR-09 |
| Analogue data | 「data values that are continuously changing」⟦9618_w23_13:1(a)⟧ | 连续变化、可取任意值的数据 | 坡道（模拟）对台阶（数字） | P1-IR-10 |
| Sampling | Taking measurements of the amplitude of a sound wave at regular intervals and storing the values.（非 MS 原句） | 按固定时间间隔测量声波振幅并存储测得的值 | 每隔一小段时间给声波拍一张“高度照片” | P1-IR-10 |
| Sampling rate | 「the number of samples taken per unit time / per second」⟦9618_w22_11:1(d)(i)⟧ | 单位时间（每秒）取样的次数 | 拍照的频率；44.1 kHz = 每秒 44 100 张 | P1-IR-10、P1-IR-11、P1-IR-12 |
| Sampling resolution | The number of bits used to store each sample.（非 MS 原句） | 存储每个样本所用的位数 | 量高度的尺子刻度有多细：16 位有 65 536 个刻度 | P1-IR-10、P1-IR-11、P1-IR-12 |
| Quantisation error | 「The quantisation errors are smaller」⟦9618_s23_13:3(c)(ii)⟧ | 样本的真实振幅与最接近的可表示值之间的差 | 用整厘米尺量 3.4 cm 只能记 3 cm，差的 0.4 就是量化误差 | P1-IR-11 |
| Lossy compression | Some data is permanently removed, so the original file cannot be recreated exactly.（非 MS 原句） | 永久删除部分数据，不能完全还原原文件，但压缩率高 | 删掉人眼人耳察觉不到的细节 | P1-IR-14、P1-IR-15 |
| Lossless compression | No data is lost, so the original file can be recreated exactly.（非 MS 原句） | 不丢失任何数据，可以完全还原原文件 | 把衣服叠紧放进箱子，拿出来一件不少 | P1-IR-14、P1-IR-15 |
| Run-length encoding (RLE) | 「A series of consecutive pixels of the same colour // a sequence of the same colour pixel is stored as a single copy of the colour and the number of consecutive occurrences」⟦9618_s26_12:1(d)(ii)⟧ | 把连续重复的相同值存成“一个副本 + 重复次数”的无损压缩方法 | “白白白白白”记成“5 白”；没有连续重复时反而更长 | P1-IR-15 |
