# 猜随机整数

来源：9618_s25_21:3；QP p7，MS p8，8 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A student has been asked to create a simple guessing game program. This program will generate
    a random integer value between 1 and 100. It will then repeatedly prompt the user to input an
    integer value until they input the randomly generated value.
    The student has written a structured English description:
    step 1 – randomly generate an integer value between 1 and 100 inclusive
    step 2 – prompt the user to input an integer value
    step 3 – output an appropriate message if the value input was too high; then repeat from step 2
    step 4 – output an appropriate message if the value input was too low; then repeat from step 2
    step 5 – output an appropriate message if the value input was the same value that was randomly
            generated; then end the program.
    Write a pseudocode algorithm from this structured English description.
    Assume no input validation is needed.
```

## Python 接口

入口：`main()`。使用 random；输出每次比较结果各一行（英文 high/large/big、low/small、correct/success/found/right 之一表达相应含义），提示放 input() 内。测试依反馈检查终止于目标，不依赖某个固定随机答案。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 8 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Declare all variables used
- [ ] MP2：Uses RAND() function
- [ ] MP3：Uses INT() function
- [ ] MP4：Correct syntax for random number between 1 and 100
- [ ] MP5：Conditional loop until correct number guessed
- [ ] MP6：Prompt and input a guess in a loop
- [ ] MP7：Check if guess is too high in a loop
- [ ] MP8：Check if guess is too low in a loop
- [ ] MP9：Output appropriate message (x2) when the number is not guessed correctly (in the loop) and output correct guess message
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
