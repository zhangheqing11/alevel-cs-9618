# 建立等级复核布尔查表数组

来源：9618_w24_23:4(b)(ii)；QP p9，MS p8，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
An examination paper has a maximum of 75 marks. One of five pass grades (A to E) is assigned,
    depending on the mark obtained. The lowest mark for a given grade is known as the grade boundary.
    A program is being written to process examination marks.
    The five grade boundaries are stored in a global 1D array GB of type INTEGER, for example:
               Index        Value                    Comment
                 1           65      The minimum mark for an A grade.
                 2           57      The minimum mark for a B grade.
                 3           43      The minimum mark for a C grade.
                 4           35      The minimum mark for a D grade.
                 5           27      The minimum mark for an E grade.
    Any paper that achieves a mark within 2 marks of a grade boundary must be checked. Using the
    given table, a paper with 45 marks would need to be checked.

An alternative algorithm to determine if a paper needs to be checked uses a global 1D array
        Check, containing 76 elements of type BOOLEAN. The indices of the array are from 0 to 75
        (inclusive), corresponding to the range of possible marks.
        An element value in Check is TRUE if the index is within 2 marks of a grade boundary. For
        example, in the case where the C grade boundary is 43 the corresponding part of the Check
        array would be as follows:
            Index        Value
              40         FALSE
              41          TRUE
              42          TRUE
                                     ←
              43          TRUE         The grade boundary for a C grade
              44          TRUE
              45          TRUE
              46         FALSE
A procedure GBInitialise() will initialise the Check array using values from the GB
            array.
            Note it can be assumed that the maximum grade boundary value for A is 70 and the
            minimum value for E is 15.
            Write pseudocode for the procedure.
```

## Python 接口

入口：`GBInitialise()`。GB 下标−1，Check 按 QP 本来就从 0 起；真实 list。A 不超过 70、E 不低于 15。每次重新初始化全部 76 项，不输出。重叠范围只需任一边界命中即 True；MS 选择方案 Version 2 范例会反复覆盖早先 True，按 QP 与 MP6 保留任一命中（D31），正确选择方案同样接受。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading and ending
- [ ] MP2：Initialise Check array to FALSE
- [ ] MP3：Loop through GB array
- [ ] MP4：Extract the GB mark
- [ ] MP5：Loop for 5 elements across GBMark ± 2 // Check if within GBMark ± 2
- [ ] MP6：Assign each element of Check array to TRUE
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
