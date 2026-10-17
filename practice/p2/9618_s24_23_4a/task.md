# 两段输入的合计平均值

来源：9618_s24_23:4(a)；QP p8，MS p7，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A procedure TwoParts() will input a sequence of real values, one at a time.
    The procedure will:
    •   process the sequence in two parts
    •   form a first total by adding the values until the first zero
    •   form a second total by adding the values after the first zero until the second zero
    •   output the average of the two totals, together with a suitable message.
    Values input in the first part are totalled using global variable TotalA and those input in the
    second part are totalled using global variable TotalB.
Write pseudocode for the procedure TwoParts().
```

## Python 接口

入口：`TwoParts()`。输出平均数并附文字消息，不限定措辞。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Procedure heading and ending
- [ ] MP2：Declare all local variables
- [ ] MP3：Initialise TotalA and TotalB
- [ ] MP4：First conditional loop until zero entered, summing TotalA // Loop until both parts (sequences) have been entered
- [ ] MP5：Second conditional loop until zero entered, summing TotalB // Loop summing appropriate Totals
- [ ] MP6：Calculation of average and output with a message // Calculation of the average for the values making up the two totals and both output with a suitable message
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
