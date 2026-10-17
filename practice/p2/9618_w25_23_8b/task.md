# 统计导师学生当前借阅总数

来源：9618_w25_23:8(b)；QP p20，MS p17，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program is being developed to manage student book loans from a college library.
    The programmer has defined a record type to define each loan.
    The data items are:
     Data item         Data type                       Comment
                                       the unique ID of the student who has borrowed
                                       the book
     StudentID   STRING
                                       The first three characters of a StudentID
                                       represent a tutor ID. Each student has one tutor.
     BookID       STRING            the unique ID of the book being borrowed
     OnLoan       BOOLEAN           TRUE if the book has not been returned
    The programmer has defined a global array Loan to store 8000 loan records.
    There are more elements in the array than books in the library. Unused elements have the
    StudentID set to an empty string. These may occur anywhere in the array.
    The programmer has defined a program module:
          Module                               Description
                        •   called with two parameters of type STRING representing a
                            StudentID and a BookID
                        •   outputs a message saying whether a given loan has been
     LoanStatus()
                            returned or not
                        •   outputs a warning message if a record of the given loan is
                            not found
A second module is defined:
                Module                            Description
                               •   called with a parameter of type STRING representing
                                   a tutor ID (as a reminder, the first three characters of
                                   a StudentID represent a tutor ID)
         LoansPerTutor()
                               •   returns an integer value representing the number of
                                   books currently on loan to students who have the
                                   given tutor
        Reminder: unused elements have the StudentID set to an empty string. These may occur
        anywhere in the array.
        Write pseudocode for the module LoansPerTutor()
```

## Python 接口

入口：`LoansPerTutor(TutorID)`。TutorID 是三字符导师 ID，取 StudentID 前三字符精确匹配；空 StudentID 必须跳过，只数 OnLoan=True。返回 int，不输出，不改记录；不做子串包含查找。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Initialise local integer for Count
- [ ] MP2：Loop through all elements in the Loan array
- [ ] MP3：Attempt at referencing a data item in a loop
- [ ] MP4：Extract TutorID from Loan[Index].StudentID in a loop
- [ ] MP5：Test for Matching Tutor AND test if the book has been returned using correct dot notation in a loop
- [ ] MP6：... if true then increment Count in a loop
- [ ] MP7：Return count
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
