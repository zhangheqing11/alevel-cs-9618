# 24 小时制时钟进位

来源：9618_w24_21:2；QP p4，MS p5，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A program uses three global integer variables HH, MM and SS to represent the current time in
    hours, minutes and seconds using the 24-hour clock notation.
    Midnight would be represented as 00:00:00 (HH:MM:SS). If the variables HH, MM and SS contained
    the values 16, 30 and 10 respectively, then the time would be 16:30:10 or just after 4.30 in the
    afternoon.
    A procedure Tick() will be called every second.
    The procedure Tick() will:
    •   update the value in SS each time it is called
    •   update the values in HH and MM as appropriate
    •   call a procedure CheckAlarm() at the start of each minute
    •   call a procedure NewDay() whenever the time reaches midnight.
    Complete the pseudocode for procedure Tick().
    PROCEDURE Tick()
    ENDPROCEDURE
```

## Python 接口

入口：`Tick()`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 6 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Increment SS anywhere in the code
- [ ] MP2：Call CheckAlarm() when SS is set to zero
- [ ] MP3：Test if SS = 60 anywhere in the code … if so:
- [ ] MP4：set SS to 0
- [ ] MP5：increment MM
- [ ] MP6：When MM is set to 60 set MM to 0 and increment HH
- [ ] MP7：When HH is set to 24 set HH to 0 and call NewDay()
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
