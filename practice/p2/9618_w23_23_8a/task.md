# 接收文本数据并写入文件

来源：9618_w23_23:8(a)；QP p17，MS p10，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

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
    Messages are sent between computers as a string of characters organised into fields as shown:
        <STX><DestinationID><SourceID><Data><ETX>
          Field name                            Description
                         a single character marking the start of the message
       STX
                         (ASCII value 02)
       DestinationID  three numeric characters identifying the destination computer
       SourceID        three numeric characters identifying the source computer
                         a variable length string containing the data being sent
       Data
                         (Minimum length is 1 character)
                         a single character marking the end of the message
       ETX
                         (ASCII value 03)
    For example, the following message contains the data "Hello Jack" being sent from computer
    "202" to computer "454":
    <STX>"454202Hello Jack"<ETX>
    Each computer will run a copy of the same program. Each program will contain a global variable
    MyID of type string which contains the unique ID of the computer in which the program is running.
    The first two program modules are defined as follows:
          Module                                Description
                        •   returns the data field from a message that has been received
     GetData()
                        •   If no message is available, the module waits until one has been
     (already written)
                            received.
                        •   takes a file name as a parameter of type string
                        •   creates a text file with the given file name (no checking required)
                        •   writes the data field returned by GetData() to the file
     ReceiveFile()
                        •   repeats until the data field is "****", which is not written to the file
                        •   outputs a final message giving the total number of characters
                            written to the file, for example:
                            132456 characters were written to newfile.txt
Write pseudocode for module ReceiveFile().
        Module GetData() has already been written and must be used.
```

## Python 接口

入口：`ReceiveFile(FileName)`。GetData 是已给定接收模块；写每个数据字段为一行（LF），完整等于 **** 才终止且不写入。字符总数按本题 MS LENGTH(FileData) 累计，不含 WRITEFILE 添加的行分隔符。只 print 一行 <总数> characters were written to <FileName>。立即终止创建空文件并输出 0；不加无效空消息，因为 QP Data 最短 1 字符。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：OPEN file in WRITE mode and subsequently CLOSE
- [ ] MP2：Conditional loop until terminator received
- [ ] MP3：‘Attempted’ use of GetData() – Ignore CALL …
- [ ] MP4：Fully correct use GetData()to return the data in a loop
- [ ] MP5：Maintain CharCount in a loop
- [ ] MP6：Write each line to the file - except the terminator in a loop
- [ ] MP7：Final output of message giving number of characters written outside loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
