# 交换消息并以 Bye 结束

来源：9618_w23_23:8(c)；QP p18，MS p11，7 分。已对照 QP 原页核对下列题干、表格与示例。

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
Two new modules are defined, which will allow two users to exchange messages.
           Module                               Description
                         •   takes two parameters:
      Transmit()           ○   a string representing a message
      (already written)        ○   an integer representing a port number
                         •   transmits the message using the given port
                         •   takes two parameters:
                             ○   a string representing a Destination ID
                             ○   an integer representing a port number
                         •   extracts data from a received message using GetData() and
      Chat()
                             outputs it
                         •   forms a message using data input by the user and sends it
                             using Transmit()
                         •   repeats until either the output string or the sent string is "Bye"
    Reminders:
    •   Each program contains a global variable MyID of type string which contains the unique ID of
        the computer in which the program is running.
    •   Messages are sent between computers as a string of characters organised into fields as
        shown:
            <STX><DestinationID><SourceID><Data><ETX>
    Write pseudocode for module Chat().
    Modules GetData() and Transmit() must be used.
```

## Python 接口

输出约定：每次从 GetData() 收到的数据原样 print 一行（包括收到的 Bye）；不额外输出标签、发送回显或提示行。用户输入提示若有须放 input() 中。

入口：`Chat(Destination,Port)`。GetData 与 Transmit 已给，测试替换为消息队列；数据严格等于大小写敏感的 Bye 才结束。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Conditional loop
- [ ] MP2：Test for terminator in both cases
- [ ] MP3：Use GetData() to get the data from the message
- [ ] MP4：OUTPUT the data in a loop
- [ ] MP5：INPUT the data reply
- [ ] MP6：‘Attempted ‘ use of Transmit to send it in a loop
- [ ] MP7：Correct formation of parameters to Transmit()
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
