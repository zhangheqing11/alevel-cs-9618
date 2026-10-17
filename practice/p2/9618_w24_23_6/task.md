# 找三月第三个星期日

来源：9618_w24_23:6；QP p11，MS p10，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
In some countries, on the third Sunday in March, daylight saving time begins when clocks move
    forward by one hour.
    A module AdjustClock() will take an integer parameter representing a year. The module will
    return an integer value representing the number of the day in March on which the clocks move
    forward.
    For example, the following line of pseudocode would assign DayNumber the value 20:
    DayNumber ← AdjustClock(2022)
    Write pseudocode for the function AdjustClock().
    Date functions from the insert should be used in your solution.
```

## Python 接口

入口：`AdjustClock(ThisYear)`。Python datetime.date 的 weekday() 以周一为 0；伪代码用插页 SETDATE 与 DAYINDEX（周日为 1）。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 7 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading, parameter, ending and return type
- [ ] MP2：Declare local integer variable that is used to create a date
- [ ] MP3：Loop until 3rd Sunday found
- [ ] MP4：Attempt to use both SETDATE() and DAYINDEX() in a loop
- [ ] MP5：Correctly generate value of type DATE using SETDATE() in a loop
- [ ] MP6：Test if value represents a Sunday using DAYINDEX() in a loop
- [ ] MP7：Increment Sunday count in a loop and initialised correctly before loop
- [ ] MP8：Return day number of third Sunday
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
