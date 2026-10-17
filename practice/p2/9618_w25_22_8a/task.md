# 分别统计在借和已还图书

来源：9618_w25_22:8(a)；QP p15，MS p13，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program is being developed to manage student book loans from a college library.
    The programmer has defined a record type to define each loan.
    The data items are:
        Data item       Data type                          Comment
     StudentID     STRING         the unique ID of the student who has borrowed the book
     BookID         STRING         the unique ID of the book being borrowed
     OnLoan         BOOLEAN        TRUE if the book has not been returned
    The programmer has defined a global array Loan to store 7000 loan records.
    There are more elements in the array than books in the library. Unused elements have the
    StudentID set to an empty string. These may occur anywhere in the array.
    The programmer has defined a program module:
            Module                               Description
                             •   called with a parameter of type STRING representing a
                                 StudentID
                             •   counts the number of books currently on loan to the
                                 specified student
     CountLoans()
                             •   counts the number of books that the student has already
                                 returned
                             •   output both counts together with a suitable message
Write pseudocode for module CountLoans()
```

## Python 接口

入口：`CountLoans(ThisStudentID)`。StudentID 非空；只统计该学生，未用项可在任意位置。只 print 两行 Student has <在借数> books on loan 和 and has returned <已还数> books，使用 MS 示例固定语句（不因单复数改字），不改记录。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Declaration of Index and two count variables
- [ ] MP2：Loop for 7000 iterations
- [ ] MP3：Index references an indexed data item with correct .dot notation
- [ ] MP4：Attempt to compare the StudentID field = parameter in a loop
- [ ] MP5：Test of the OnLoan field and correct logic for both outcomes
- [ ] MP6：Both count variables initialised and increment appropriate count in a loop
- [ ] MP7：Output includes both counts with a suitable message
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
