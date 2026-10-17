# 统计每小时拍摄次数

来源：9618_s25_22:5(b)；QP p10，MS p12，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
An automated digital camera system is used to take a sequence of pictures of animals in a garden.
    During the design of the system, a state‑transition diagram is produced.
    The table details the states in the automated digital camera system along with the events which
    cause the states to change.
    The system starts in standby mode. The sequence of pictures is taken when in active mode.
           Current state                 Event                  Next state
     standby mode             turn on                   detect mode
     detect mode               turn off                   standby mode
     detect mode               movement detected        active mode
     active mode               20 seconds elapsed        sequence complete
     active mode               turn off                   standby mode
     sequence complete        time saved                detect mode
At the end of each sequence of pictures, the time is saved as a string in the format
        <HH><MM><SS> where:
        •   HH represents the hours using two digits
        •   MM represents the minutes using two digits
        •   SS represents the seconds using two digits.
        For example:
        •   "081230" is stored to represent the time 8:12:30, in the morning
        •   "152235" is stored to represent the time 15:22:35, in the afternoon.
        Each string is stored on a new line in the text file TimeTaken.txt
        An algorithm is required to process the content of the text file TimeTaken.txt once it has
        been transferred to the computer.
        For each hour when pictures are taken, output a suitable message showing the hour and the
        total number of sequences of pictures taken within that hour.
        Example outputs:
        Hour : 15  Total : 32
        Hour : 18  Total : 1
        Write pseudocode for this algorithm.
        Assume the text file TimeTaken.txt contains at least one line.
```

## Python 接口

入口：`main()`。Python main 包装无命名算法；每个有记录小时只 print 一行 Hour : <小时>  Total : <次数>，小时可补零，空白数量可变，不要求输出顺序。QP 保证至少一行，不测空文件；为兼容 MS 两种认可算法，行为测试使用按时间记录、同一小时相邻的数据。人工清单下列是条件循环方案；MS 同页数组计数替代方案也可按其得分点逐项检查，不强制用上一个小时比较。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `TimeTaken.txt`：27 字节；最后一行无换行。


## 人工核对清单

本题 MS 总分上限 8 分，候选得分点不能简单相加超过此上限。

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Any Initialisation of count for number of pictures taken each hour
- [ ] MP2：Open "TimeTaken.txt" for read and subsequently close
- [ ] MP3：Conditional loop until EOF
- [ ] MP4：Read a line from "TimeTaken.txt" in a loop
- [ ] MP5：Extract Hour from line read in a loop
- [ ] MP6：A mechanism to compare current hour extracted from file with last one read from file in a loop
- [ ] MP7：If hours same increment count in a loop
- [ ] MP8：If not same output count (with a suitable message) and update Hour ← NextHour and set Count to 1 in a loop
- [ ] MP9：Output final Count and Hour (with a suitable message) once only
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
