# 向第一个空借阅记录登记

来源：9618_w25_22:8(b)；QP p16，MS p14，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

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
As a reminder, a global array Loan stores 7000 loan records with data items for each loan
        record:
           Data item      Data type                         Comment
         StudentID    STRING       the unique ID of the student who has borrowed the book
         BookID       STRING       the unique ID of the book being borrowed
         OnLoan       BOOLEAN      TRUE if the book has not been returned
        A new module is defined:
             Module                                Description
                          •   called  with  two  parameters  of  type  STRING  representing  a
                              StudentID and a BookID
         NewLoan()      •   searches the array for an unused loan record
                          •   if found, updates the loan record and returns TRUE, otherwise
                              returns FALSE
        Write efficient pseudocode for NewLoan()
```

## Python 接口

入口：`NewLoan(ThisStudentID,ThisBookID)`。参数为非空 ID；未用只以 StudentID=="" 判断，已归还记录不代表未用。按 MS MP2 第一个未用记录插入；同时写两 ID 和 OnLoan=True。成功 True，满表 False 且不改记录，不输出。不增加 QP 未要求的重复借阅验证。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Loop through 7000 elements in Loan array – correct loop structure
- [ ] MP2：or until the first unused element is found // Correct RETURN inside a FOR loop
- [ ] MP3：Correct use of the indexed dot notation
- [ ] MP4：Test if record is unused (.StudentID = "")in a loop
- [ ] MP5：Two item assignment statements correct
- [ ] MP6：Loan[Index].OnLoan assigned TRUE
- [ ] MP7：Correct logic to return BOOLEAN in both cases (position found / no position available)
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
