# 解析逗号分隔整数

来源：9618_s22_22:6；QP p10，MS p10，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A string represents a series of whole numbers, separated by commas.
    For example:
        "12,13,451,22"
    Assume that:
    •   the comma character ',' is used as a separator
    •   the string contains only the characters '0' to '9' and the comma character ','.
    A procedure Parse will:
    •   take the string as a parameter
    •   extract each number in turn
    •   calculate the total value and average value of all the numbers
    •   output the total and average values with a suitable message.
    Write pseudocode for the procedure.
    PROCEDURE Parse(InString : STRING)
    ENDPROCEDURE
```

## Python 接口

入口：`Parse(InString)`。题目仅要求 suitable message，测试提取总数和平均数并要求有文字提示，不限定消息措辞。输入至少一个有效整数，无首尾逗号。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Declare and initialise Count, Total and NumString
- [ ] MP2：Loop for number of characters in InString
- [ ] MP3：Extract a character and test for comma in a loop
- [ ] MP4：If comma, convert NumString to integer and update Total and Count
- [ ] MP5：and reset NumString
- [ ] MP6：Otherwise append character to NumString
- [ ] MP7：Calculate average AND final output statement(s) outside the loop
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
