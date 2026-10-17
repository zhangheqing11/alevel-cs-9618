# 生成十进制校验位

来源：9618_w25_21:6(b)；QP p11，MS p13，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
Students are learning about a simple check digit method for data validation. In this method, a
    single check digit is appended to the end of an original number to give a new number.
    The students are studying a method which:
    •   calculates the sum of all the digits in the original number
    •   uses integer division to calculate the remainder when the sum is divided by 10
    •   uses the remainder as the check digit
    •   appends the check digit to the original number, creating the new number.
    For example:
     original number                                            4162
     sum of all digits                                            4 + 1 + 6 + 2 = 13
     remainder when the sum is divided by 10 using integer division  3
     new number                                               41623
    The method described can be used to detect single-digit errors. For example, if the new number
    is incorrectly input as 41633, then the check digit does not match and the input will be rejected.
A module Generate() will take an integer value representing an original number and return
        an integer value representing a new number which includes the check digit.
        The original number is always at least three digits in length.
        Write pseudocode for the module Generate()
        Assume that the parameter is valid.
```

## Python 接口

入口：`Generate(Number)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading, parameters return type and ending
- [ ] MP2：Initialise Total
- [ ] MP3：Convert Number to a string and loop for length of converted Number
- [ ] MP4：attempt to form sum of digits in a loop
- [ ] MP5：completely correct sum of digits in a loop
- [ ] MP6：Calculate CheckDigit
- [ ] MP7：Add CheckDigit to original number multiplied by 10 and return number // Convert CheckDigit to a character and appended to NumString and then convert to a number and return
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
