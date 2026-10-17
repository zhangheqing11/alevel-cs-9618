# 输出严格递增的随机整数

来源：9618_w23_23:4(a)；QP p8，MS p7，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A procedure RandList() will output a sequence of 25 random integers, where each integer is
    larger than the previous one.
Write pseudocode for procedure RandList().
```

## Python 接口

输出约定：只输出 25 行，每行只有一个整数，不附说明文字。

入口：`RandList()`。题目未给数值上下界；测试只要求 25 个整数严格递增，不限定 MS 的分段范围或某个随机序列。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Procedure heading and ending
- [ ] MP2：Local loop counter Count as integer
- [ ] MP3：Loop to iterate 25 times or more for each unique number
- [ ] MP4：‘Attempt’ to generate a random number including use of INT() in a loop
- [ ] MP5：Ensure that number generated is greater than previous and change ‘previous’
- [ ] MP6：Output random number after an attempt at MP5 in a loop
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
