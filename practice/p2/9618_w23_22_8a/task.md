# 从路由范围表寻找端口

来源：9618_w23_22:8(a)；QP p17，MS p11，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A class of students are developing a program to send data between computers. Many computers
    are connected together to form a wired network. Serial ports are used to connect one computer to
    another.
    Each computer:
    •   is assigned a unique three-digit ID
    •   has three ports, each identified by an integer value
    •   is connected to between one and three other computers.
    Data is sent as individual message strings.
    Each string contains the destination ID (the ID of the computer that is to receive the message)
    followed by the data:
        <DestinationID><Data>
    Messages may pass through several computers on the way to their destination.
    When a message arrives at a computer, that is not the destination, the program needs to forward
    it on to another computer using one of its serial ports.
    The port to use is obtained from information that is stored in an array RouteTable.
    RouteTable is a global 2D array of integers. It is declared in pseudocode as follows:
        DECLARE RouteTable : ARRAY[1:6,1:3] OF INTEGER
    The values in the first two columns of RouteTable define a range of ID values.
    Column 3 gives the corresponding port number to use when forwarding the message to a computer
    with an ID within this range.
    For example, the contents of RouteTable could be:
                        Column 1        Column 2        Column 3
         Row 1            100             199               1
         Row 2            200             259               2
         Row 3            −1         <undefined>    <undefined>
         Row 4            260             399               2
         Row 5            400             599               3
         Row 6            600             999               1
    In this example, a message that arrives with a DestinationID of "283" will be forwarded using
    port 2.
    Row 3 in the example shows an unused row. These may occur anywhere. Unused rows have the
    column 1 element set to −1. The value of unused elements in the other two columns is undefined.
    The programmer has defined the first program module as follows:
           Module                                Description
                         •   takes a DestinationID as a parameter of type string
                         •   searches for the range corresponding to the DestinationID
     GetPort()             in the array
                         •   returns the port number, or returns −1 if no corresponding
                             range is found
Write pseudocode for module GetPort().
        Assume DestinationID contains a valid three-digit string.
```

## Python 接口

入口：`GetPort(ThisDest)`。ThisDest 已是合法三位数字串，闭区间含两端；未用行首列 -1，可在任意位置，其余列无定义，不能拿来匹配。范围重叠时端口选择 QP 未定义，测试不构造重叠；不输出、不改表。MS 同题还认可逐条选择方案，按其对应得分点人工核对；该范例不等号方向错误不覆盖 QP 范围定义（D31）。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 7 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Function heading and ending including parameter and return type
- [ ] MP2：Convert parameter to a number
- [ ] MP3：(Conditional) loop through array
- [ ] MP4：Skip unused element in a loop
- [ ] MP5：Attempt to check one range with destination in a loop
- [ ] MP6：Test all ranges correctly with destination in a loop
- [ ] MP7：Store port value if destination matched in a loop (and exit loop)
- [ ] MP8：Return port value including -1 if no match found
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
