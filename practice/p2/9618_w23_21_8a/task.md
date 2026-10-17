# 逐行封装消息发送文件

来源：9618_w23_21:8(a)；QP p15，MS p9，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

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
       Field
                  Field name                           Description
      number
                                 a single character marking the start of the message
        n/a    STX
                                 (ASCII value 02)
         1     DestinationID  three numeric characters that identify the destination computer
         2     SourceID        three numeric characters that identify the source computer
                                 a variable length string containing the data being sent
         3     Data
                                 (Minimum length is 1 character)
                                 a single character marking the end of the message
        n/a    ETX
                                 (ASCII value 03)
    For example, the following message contains the data "Hello Kevin" being sent from computer
    "101" to computer "232":
        <STX>"232101Hello Kevin"<ETX>
    Each computer will run a copy of the same program. Each program will contain a global variable,
    MyID of type string, that contains the unique ID of the computer in which the program is running.
    The programmer has defined the first two program modules as follows:
            Module                               Description
                           • takes two parameters:
     Transmit()            o a string containing a message
     (already written)          o an integer containing a port number
                           • transmits the message using the given port
                           • takes three parameters:
                             o a string containing a text file name
     SendFile()            o a string containing a Destination ID
                             o an integer containing a Port number
                           • transmits the file one line at a time
                           • transmits a final message with data string "****"
Write pseudocode for module SendFile().
        Assume:
        •   module Transmit() has already been written and is used to transmit a message
        •   the value of MyID may be used as SourceID
        •   the file specified contains no blank lines
        •   the file specified does not contain the line "****"
```

## Python 接口

入口：`SendFile(FileName,DestID,Port)`。MyID 为真实全局 STRING，Transmit 是给定传输模块，测试替换记录参数，不接触网络。STX/ETX 必须是 ASCII 2/3 单字符，不能文字标记。每个文件行不含行分隔符，保留行内空格；最后只发送一次 **** 封包，不 print。QP 禁止空行与数据行 ****，不测试这些输入；空文件没有空行，仍发送结束封包。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `message.txt`：21 字节；最后一行无换行。


## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：OPEN file in READ mode – using parameter - and subsequently CLOSE
- [ ] MP2：Conditional loop to EOF()
- [ ] MP3：Use of READFILE to get a line from the file
- [ ] MP4：‘Attempt’ to form a message (minimum is DestID, MyID, FileData)
- [ ] MP5：Message formed is completely correct
- [ ] MP6：Call Transmit() with correct MP4 string in a loop
- [ ] MP7：Transmit the "****" message (all parts present) after the loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
