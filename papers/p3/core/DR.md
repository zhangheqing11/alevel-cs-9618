## DR　数据表示：核心概念 {#core-DR}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。伪代码写法见 2027–29 伪代码指南 “User-defined data types” 一节（p.12–14）。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| User-defined data type | 「To allow data types not available in a programming language to be constructed // To extend the flexibility of the programming language」⟦9618_s21_31:2(a)⟧ | 程序员在语言内置类型之外自己定义的类型 | 语言没有现成的“零件”，就自己拼一个 | P3-DR-01 |
| Non-composite data type | 「A data type that is defined without referencing another data type」⟦9618_s24_32:3(a)⟧ | 定义时不引用其他数据类型的类型；可以是内置的或用户定义的（枚举、指针） | 一块整砖，不由别的砖拼成 | P3-DR-01 |
| Composite data type | 「Composite data types refer to other data types in their definition/contain more than one data type in their definition」⟦9618_s24_31:3(a)⟧ | 定义里引用其他数据类型、由多个元素组成并放在一个标识符下的类型（记录、集合、类 / 对象） | 一个收纳盒，里面放着各种类型的格子 | P3-DR-01 |
| Enumerated data type | 「A (user-defined non-composite) data type with an ordered list of possible values」⟦9618_w22_31:3(a)⟧ | 列出全部可能取值、且这些值有序的非组合类型；声明 `TYPE 名 = (值1, 值2, …)` | 下拉菜单：只能选列出的几项，且有先后 | P3-DR-01、P3-DR-02 |
| Pointer data type | 「A user-defined non-composite data type used to reference a memory location」⟦9618_w22_31:3(b)⟧ | 存放内存地址并指明该地址里数据类型的非组合类型；声明 `TYPE 名 = ^类型` | 写着门牌号、并注明“屋里放什么”的纸条 | P3-DR-01、P3-DR-02 |
| Record | 「It uses other data types in its definition to form a single new data type」⟦9618_w24_32:3(a)⟧ | 把固定数量的相关数据项（各有类型）组合成一个新类型的组合类型；`TYPE … ENDTYPE` | 一张表格的表头：每栏有名字、有规定的类型 | P3-DR-01、P3-DR-03、P3-DR-04 |
| Set | 「… which includes a list of unordered elements」⟦9618_w24_31:6(a)⟧ | 元素无序、元素同类型、可做交集并集等集合运算的组合类型；`TYPE 名 = SET OF 类型` + `DEFINE …` | 一个袋子：东西放进去没有先后，可以和别的袋子比较“共同有的” | P3-DR-01、P3-DR-05 |
| Dot notation | 「LibraryBook.Fiction ← FALSE」⟦9618_s22_31:1(a)⟧ | 用“变量名.字段名”访问记录的某个字段 | 表格的“第几张.哪一栏” | P3-DR-04 |
| Serial file organisation | 「Records are stored one after the other as they are collected // records are stored in chronological order」⟦9618_w24_32:2(a)⟧ | 记录按到达先后一条接一条存放，新记录追加到末尾 | 排队登记簿 | P3-DR-06 |
| Sequential file organisation | 「records are stored in a particular order」⟦9618_s23_32:2(a)⟧ | 记录按键字段的顺序存放；更新要生成新版本文件 | 按学号排好的花名册 | P3-DR-06 |
| Random file organisation | 「There is a relationship between the key of the record and its location within the file // a hashing algorithm is used to find the location of the record」⟦9618_w23_31:4(a)⟧ | 记录不按任何顺序存放，位置由键经散列算法决定，可以直接更新 | 寄存柜：柜号由号码牌算出 | P3-DR-06 |
| Sequential access | 「Sequential access method searches for records one after the other」⟦9618_s24_31:4(a)⟧ | 从文件开头逐条读记录比较，直到找到或到文件尾（顺序文件可在键超过目标时停） | 一页页翻 | P3-DR-07 |
| Direct access | 「Direct access allows a record to be found in a file without other records being read」⟦9618_s24_32:7(a)⟧ | 不读其他记录就能找到目标记录：顺序文件用索引，随机文件用散列 | 直接翻到目录给出的那一页 | P3-DR-07 |
| Index (sequential file) | 「In sequential files, an index of all key fields is kept」⟦9618_s24_32:7(b)(i)⟧ | 顺序文件里保存所有键字段及其记录地址的表，用于直接存取 | 书后的索引页 | P3-DR-07 |
| Hashing algorithm | 「The result of the calculation gives the address where the record should be found / stored」⟦9618_w24_31:5(a)⟧ | 作用于记录键字段的数学公式，结果是记录应存 / 应在的地址 | 由号码牌算柜号的规则 | P3-DR-08、P3-DR-07 |
| Collision | 「A collision is when the two values / data items in the key field for two records (pass through a hashing algorithm and) result in the same hash value」⟦9618_w23_32:3(a)⟧ | 两个不同的键经散列算法得到同一个散列值，算出的位置可能已被占用 | 两张号码牌算出同一个柜号 | P3-DR-08 |
| Overflow area | 「An overflow area is set up and the record is stored in the next free memory space in the overflow area」⟦9618_w24_31:5(b)⟧ | 处理冲突的一种办法：冲突的记录存进另设的溢出区的下一个空位 | 主柜满了就放到旁边的备用柜 | P3-DR-08 |
| Linear probing | 「The record is stored in the next free memory space after the one identified by the hashing algorithm」⟦9618_w24_31:5(b)⟧ | 处理冲突的一种办法：从散列位置起往后找第一个空位 | 本柜有人就看下一个 | P3-DR-08 |
| Mantissa / exponent | Floating-point value = mantissa × 2^exponent; both are stored in two’s complement.（非 MS 原句） | 尾数给出有效数字（小数点在符号位后），阶码给出小数点移动的位数；两者都用补码 | 科学记数法的“系数”和“10 的几次方”，只是换成二进制 | P3-DR-09、P3-DR-10 |
| Normalised floating point | The two most significant bits of the mantissa are different: 01 for a positive number, 10 for a negative number.（非 MS 原句） | 尾数最高两位不同（正数 01、负数 10）的浮点表示 | 把前导的 0（或 1）全推掉，不浪费位 | P3-DR-10、P3-DR-11 |
| Not normalised（判断理由） | 「The mantissa does not begin with 01/10 (as its most significant bits)」⟦9618_w22_31:1(c)(i)⟧ | 判断一个位串“未规格化”的理由：尾数前两位相同（00 或 11） | 前面还有可以推掉的位 | P3-DR-11 |
| Reason for normalisation | 「Maximising the number of significant bits // maximising the (potential) precision / accuracy of the number for the given number of bits」⟦9618_w21_31:1(b)⟧ | 规格化使有效位最多、精度最高，并使每个数只有一种表示 | 屏幕上每一位都显示有效数字 | P3-DR-11 |
| Precision vs range | 「When the range increases the accuracy decreases // When the range decreases the accuracy increases」⟦9618_s24_32:1(a)⟧ | 总位数固定时，尾数位多 → 精度高；阶码位多 → 范围大；二者此消彼长 | 屏幕位数与“能显示多大的数”二选一 | P3-DR-12 |
| Truncation / rounding error | 「therefore, there will be a loss of precision due to a rounding error/truncation」⟦9618_w23_31:1(b)⟧ | 尾数位数不够或小数无法用 2 的负幂精确表示时，只能存近似值 | 0.2 写成二进制像 1/3 写成小数，永远写不完 | P3-DR-10、P3-DR-12 |
| Overflow | 「the result might be outside of the range of values possible to store in the given system」⟦9618_w25_33:2(b)⟧ | 运算结果大于系统能表示的最大值，最高位丢失 | 里程表转过了头 | P3-DR-12 |
| Underflow | 「… the result is too small to be precisely represented in the available system」⟦9618_w22_32:1(c)⟧ | 运算结果太接近 0，阶码不够负，无法表示（常变成 0） | 小到秤上显示不出来 | P3-DR-12 |
