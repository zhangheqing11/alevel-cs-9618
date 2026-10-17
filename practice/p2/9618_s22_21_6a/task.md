# 输出末位为 7 的整数

来源：9618_s22_21:6(a)；QP p9，MS p6，5 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
An algorithm will:
        •   output each integer value between 100 and 200 that ends with the digit 7, for example,
            107
        •   output a final count of the number of values that are output.
        Write pseudocode for this algorithm.
        Any variables used must be declared.
```

## Python 接口

输出约定：输出的每一行只含一个整数，不加说明文字：先按递增顺序输出符合条件的数，最后一行只输出计数。

入口：`main()`。输出每个整数各占一行，最后一行仅输出计数。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Declare loop variable and counter as integers, counter initialised
- [ ] MP2：Loop 100 to 200, no step defined
- [ ] MP3：Test value in a loop
- [ ] MP4：Output selected value and incrementing a counter in a loop
- [ ] MP5：Output the counter, following a reasonable attempt, after the loop
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
