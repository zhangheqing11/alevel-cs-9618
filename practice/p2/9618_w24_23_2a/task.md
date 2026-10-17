# 输入 100 个整数并累加正数

来源：9618_w24_23:2(a)；QP p3，MS p5，5 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
An algorithm will:
    1.  prompt and input a sequence of 100 integer values, one at a time
    2.  sum the positive integers
    3.  output the result of the sum.
Write pseudocode for the algorithm.
        Assume the value zero is neither positive nor negative.
        You must declare all variables used in the algorithm.
```

## Python 接口

入口：`main()`。每次提示放入 input()；最终一行输出正数总和，不计零和负数。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 5 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Declarations of all variables used
- [ ] MP2：Loop for 100 iterations
- [ ] MP3：Prompt and input a value in a loop and
- [ ] MP4：Test for value > 0 // >=1 in a loop
- [ ] MP5：Sum the Total in a loop
- [ ] MP6：Output of Total after the loop
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
