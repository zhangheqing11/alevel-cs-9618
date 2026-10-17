# 把收到的消息放入正确栈

来源：9618_w23_22:8(b)；QP p18，MS p13，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

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
Copies of the same program will run on each computer. The program contains a global
        variable MyID of type string, which contains the unique ID of the computer in which the
        program is running.
        When messages are received, they are placed on one of two stacks. Stack 1 is used for
        messages that have reached their destination and stack 2 is used for messages that will be
        forwarded on to another computer.
        Additional modules are defined:
             Module                                Description
                             •   takes two parameters:
                                 ○   a string representing a message
     StackMsg()                 ○   an integer representing the stack number
     (already written)          •   adds the message to the required stack
                             •   returns TRUE if the message is added to the required stack,
                                 otherwise returns FALSE
                             •   takes a message as a parameter of type string
                             •   ignores any message with a zero-length data field
                             •   extract the DestinationID from the message
                             •   checks whether the DestinationID is this computer or
     ProcessMsg()              whether the message is to be forwarded
                             •   uses StackMsg() to add the message to the appropriate
                                 stack
                             •   outputs an error if the message could not be added to the
                                 stack
        Write pseudocode for module ProcessMsg().
        Module StackMsg() must be used.
```

## Python 接口

入口：`ProcessMsg(ThisMsg)`。StackMsg 是题给服务，测试替换其成功/失败结果；本小问不实现栈或 GetPort。RouteTable 中未定义单元以 0 占位，未使用该行时不可读其路由。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Ignore message if data field is empty
- [ ] MP2：Extract ThisDest from ThisMsg
- [ ] MP3：Test if destination is this computer
- [ ] MP4：Attempt to use StackMsg()
- [ ] MP5：Fully correct use of StackMsg()for both cases / stacks
- [ ] MP6：Test StackMsg() return value for both cases
- [ ] MP7：Following a reasonable attempt at MP6 output warning if StackMsg() returns FALSE
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
