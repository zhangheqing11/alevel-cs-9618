# 遮盖卡号并保留末四位

来源：9618_w24_22:2(a)；QP p4，MS p5，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A program is being developed to process bank card information.
    When a card number is displayed, all the characters except the last four are replaced with the
    asterisk character '*'.
    Card numbers are stored as strings. The strings are between 10 and 20 characters in length.
    The function Conceal() will take a string representing a card number and return a modified
    string.
    Example strings:
         Original string         Modified string
     "1234567890"         "******7890"
     "1234567897652"     "*********7652"
     "1234567890123456"  "************3456"
The function Conceal() will:
        •   take a numeric string as a parameter representing the card number
        •   return a string in which the asterisk character replaces all except the last four characters
            of the card number parameter.
        Write pseudocode for the function Conceal().
```

## Python 接口

入口：`Conceal(CardNumber)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading and parameter and ending and return type
- [ ] MP2：Declaration of all local variables used - including the loop counter
- [ ] MP3：Calculate number of digits to mask / number of asterisks required
- [ ] MP4：use of a ‘relevant’ Loop
- [ ] MP5：Correct number of iterations
- [ ] MP6：Concatenate asterisk to start/end of MaskedString in a loop
- [ ] MP7：Assign last four characters to MaskedString // Concatenate the retained original last four digits
- [ ] MP8：Return masked string
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
