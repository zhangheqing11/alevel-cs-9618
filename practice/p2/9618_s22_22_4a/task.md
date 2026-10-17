# 输出文件最后三行

来源：9618_s22_22:4(a)；QP p6，MS p6，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A procedure LastLines() will:
        •   take the name of a text file as a parameter
        •   output the last three lines from that file, in the same order as they appear in the file.
        Note:
        •   Use local variables LineX, LineY and LineZ to store the three lines from the file.
        •   You may assume the file exists and contains at least three lines.
        Write pseudocode for the procedure LastLines().
```

## Python 接口

入口：`LastLines(ThisFile)`。每个原文件行原样 print 为一行，保留空行及行内空格，不加标题。文件至少三行是 QP 的明确前提，因此不测空文件或一行文件。文件题通过 candidate_path 在样例副本临时目录运行；测试检查文件已关闭。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `sample.txt`：25 字节；最后一行无换行。


## 人工核对清单

本题 MS 总分上限 6 分，候选得分点不能简单相加超过此上限。

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading (including parameter) and ending
- [ ] MP2：Declaration of local variables for three lines AND File OPEN in READ mode AND CLOSE
- [ ] MP3：Loop until EOF(ThisFile)
- [ ] MP4：Read line from file... in a loop
- [ ] MP5：Attempt at a shuffle… in a loop
- [ ] MP6：Correctly shuffle LineX, LineY and LineZ in a loop
- [ ] MP7：OUTPUT the three lines in correct sequence, following reasonable attempt
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
