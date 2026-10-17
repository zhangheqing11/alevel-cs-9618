# 生成需要复核试卷的 ID 文件

来源：9618_w24_21:8(b)；QP p18，MS p13，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
An exam paper has a maximum of 75 marks. One of five pass grades (A to E) is assigned,
    depending on the mark obtained. The lowest mark for a given grade is known as the grade
    boundary. For example, if the grade boundary for an A grade is 65 marks, then any candidate who
    achieves a mark of 65 or above will be awarded an A. A grade of U is awarded for marks below the
    E grade boundary.
    The five grade boundaries are stored in a global 1D array GradeBoundary of type integer.
    For example:
                    Element         Value              Comment
              GradeBoundary[1]  65        The minimum mark for an A grade.
              GradeBoundary[2]  57        The minimum mark for a B grade.
              GradeBoundary[3]  43        The minimum mark for a C grade.
              GradeBoundary[4]  35        The minimum mark for a D grade.
              GradeBoundary[5]  27        The minimum mark for an E grade.
    A global 2D array Result of type integer contains candidate marks for the exam. Each row
    relates to one candidate. Column 1 contains the candidate mark and column 2 contains the unique
    candidate ID.
    For example, for the fourth and fifth candidates:
                   Element       Mark             Element          ID
               Result[4, 1]    56            Result[4, 2]    1074832
               Result[5, 1]    54            Result[5, 2]    2573839
    There are more rows in the array than candidates who sit the exam. Any unused rows will be at
    the end of the array.
    Candidate papers that are given a mark within two marks of any grade boundary must be checked.
    For example, given the values in the example grade boundaries above, any paper that was
    awarded between 41 and 45 marks (inclusive) would need to be checked.
    A program is being written to identify papers that need to be checked.
    The programmer has defined the first program module as follows:
            Module                            Description
                         •   called with a parameter of type integer representing a
                             candidate mark
         CheckMark()
                         •   returns TRUE if the mark is within 2 of any of the five grade
                             boundaries, otherwise returns FALSE
A second module is defined:
            Module                            Description
                         •   called with a parameter of type integer representing the
                             number of candidate marks in the Result array
                         •   uses CheckMark() to check each candidate mark
                         •   for each paper that needs to be checked, write the
         CheckAll()
                             corresponding candidate ID on a separate line in a new file
                             named GRList.txt
                         •   outputs a message with a count of how many papers need
                             to be checked
        Write pseudocode for module CheckAll().
        CheckMark() must be used to check each individual mark.
```

## Python 接口

入口：`CheckAll(CNum)`。Result 行列下标=QP−1；题面未定总容量，骨架给 100 行样例容量，测试替换为足够的真实 list。只检查前 CNum 位，包括 0 位；必须用 provided CheckMark。覆盖 GRList.txt，每个 ID 一行 LF；只 print 一行 There are <数量> papers to check。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 8 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading, parameter and ending.
- [ ] MP2：Open file in write mode and subsequently close
- [ ] MP3：Loop through all CNum candidates
- [ ] MP4：Extract candidate mark from Result array in a loop
- [ ] MP5：Use of CheckMark() with candidate mark as parameter in a loop
- [ ] MP6：Test return value and if TRUE then increment Count in a loop
- [ ] MP7：... write ID to file ...
- [ ] MP8：... after conversion to a string in a loop
- [ ] MP9：Final output of message giving number of papers to check not in a loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
