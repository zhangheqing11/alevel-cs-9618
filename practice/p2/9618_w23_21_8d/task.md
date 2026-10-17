# 提取带 STX/ETX 消息字段

来源：9618_w23_21:8(d)；QP p18，MS p10，6 分。已对照 QP 原页核对下列题干、表格与示例。

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
A new module has been defined:
           Module                                Description
                           • takes two parameters:
                             o a string containing a message
                             o an integer containing a field number
     GetField()
                           • If the field number is valid (in the range 1 to 3, inclusive), it
                            returns a string containing the required field, otherwise it returns
                            an empty string.
        As a reminder, a message is defined as follows:
            <STX><DestinationID><SourceID><Data><ETX>
     Field
                  Field name                           Description
   number
                                 a single character marking the start of the message
 Not applicable  STX
                                 (ASCII value 02)
      1       DestinationID  three numeric characters that identify the destination computer
      2       SourceID        three numeric characters that identify the source computer
                                 a variable length string containing the data being sent
      3       Data
                                 (Minimum length is 1 character)
                                 a single character marking the end of the message
 Not applicable  ETX
                                 (ASCII value 03)
    Write pseudocode for module GetField().
```

## Python 接口

入口：`GetField(Msg,FieldNo)`。消息包含真实 chr(2)/chr(3)，示例中的引号不属于消息数据。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Use of CASE ... ENDCASE or IF ... THEN ... ENDIF
- [ ] MP2：Field 1 and Field 2 extracted correctly
- [ ] MP3：Calculate a length of field 3
- [ ] MP4：Field 3 extracted correctly
- [ ] MP5：Return empty string in case of invalid parameter (via OTHERWISE or initialisation)
- [ ] MP6：Final RETURN, after a reasonable attempt
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
