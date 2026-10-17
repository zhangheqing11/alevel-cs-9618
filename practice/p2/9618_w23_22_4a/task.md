# 以 99 终止并统计奇偶数

来源：9618_w23_22:4(a)；QP p8，MS p7，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A procedure Count() will:
    1.  input a value (all values will be positive integers)
    2.  count the number of odd values and count the number of even values
    3.  repeat from step 1 until the value input is 99
    4.  output the two count values, with a suitable message.
    The value 99 must not be counted.
Write pseudocode for the procedure Count().
```

## Python 接口

入口：`Count()`。输出奇数计数、偶数计数（此顺序）及文字消息；99 不计数。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 6 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Procedure heading and ending
- [ ] MP2：Local COdd, CEven and ThisNum declared as integers
- [ ] MP3：Conditional loop while ThisNum <> 99
- [ ] MP4：Input ThisNum in a loop
- [ ] MP5：Check ThisNum is odd or even in a loop
- [ ] MP6：Increment appropriate count in a loop, both counts must have been initialised before loop
- [ ] MP7：After the loop output COdd and CEven with a suitable message following a reasonable attempt at counting
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
