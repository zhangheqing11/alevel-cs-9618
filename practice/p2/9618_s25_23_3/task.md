# 投骰子的输出与平均数

来源：9618_s25_23:3；QP p7，MS p9，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A programmer has been asked to create a module RollDice() to simulate multiple rolls of a
    dice. This module will be used as part of a program for a game.
    The module will:
    step 1 – take a positive integer parameter representing the number of times the dice will be rolled
    step 2 – simulate one roll of the dice by generating a random integer between 1 and 6 inclusive
    step 3 – output the integer generated
    step 4 – repeat, as required from step 2
    step 5 – calculate the average value of the random integers generated
    step 6 – return the average value.
    Write pseudocode for the module RollDice()
```

## Python 接口

入口：`RollDice(NoOfTimes)`。每次点数各输出一行，返回 REAL 对应 Python float；不要求特定随机序列。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Declare all variables used and initialise Sum to 0
- [ ] MP2：Loop for ‘number of times’ parameter
- [ ] MP3：Use RAND() function with Integer parameter in a loop
- [ ] MP4：Use INT() function in a loop
- [ ] MP5：Generate a random integer between 1 and 6 in a loop
- [ ] MP6：Output each value generated in a loop
- [ ] MP7：Calculate Sum and if Average used check declared as REAL and return Average and check function header returns REAL
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
