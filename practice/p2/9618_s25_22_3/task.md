# 不重复随机数与条件第三数

来源：9618_s25_22:3；QP p6，MS p9，8 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
An algorithm is designed to generate and output two unique random integers. Each integer value
    is between –10 and 10 inclusive.
    If both integers output are negative, a third random integer between 30 and 35 inclusive will be
    generated and output.
    Write pseudocode for this algorithm.
```

## Python 接口

入口：`main()`。每个随机整数输出一行，使用标准库 random。测试检查范围、不重复与第三数条件，不限定随机序列。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Declare all variables used
- [ ] MP2：Use RAND() function with any integer parameter
- [ ] MP3：Use INT() function with any numeric parameter
- [ ] MP4：Conditional loop until two different random numbers are generated
- [ ] MP5：Use INT() function using random number generated between −10 and 10 inclusive in a loop
- [ ] MP6：Output two different random integers / numbers
- [ ] MP7：Check if both random integers / numbers are negative
- [ ] MP8：then output a (third) random integer / number between 30 and 35 inclusive
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
