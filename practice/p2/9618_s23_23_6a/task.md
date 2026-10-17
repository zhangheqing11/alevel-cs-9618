# 筛选末两位数字之和为 6 的整数

来源：9618_s23_23:6(a)；QP p10，MS p6，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A procedure Select() will:
    1.  take two integer values as parameters representing start and end values where both values
        are greater than 9 and the end value is greater than the start value
    2.  output each integer value between the start and the end value (not including the start and
        end values), where the sum of the last two digits is 6, for example, 142.
Write pseudocode for procedure Select().
        Parameter validation is not required.
```

## Python 接口

入口：`Select(Start, End)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 7 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Procedure heading and ending
- [ ] MP2：(Count-controlled) Loop
- [ ] MP3：…. with correct range from Start+1 to End-1
- [ ] MP4：Convert ThisNum (loop counter) to a string
- [ ] MP5：Extract the last two/first/second ’character digit(s)’ required in a loop
- [ ] MP6：Extract the second individual ‘character digit’ required in a loop
- [ ] MP7：Calculate the sum of the last two digits
- [ ] MP8：If sum = 6 then OUTPUT the number (either string or integer) in a loop
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
