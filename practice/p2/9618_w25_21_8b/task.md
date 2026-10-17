# 归还指定学生的指定图书

来源：9618_w25_21:8(b)；QP p16，MS p18，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program is being developed to manage student book loans from a college library. Students may
    borrow up to five books at a time from the library.
    The programmer has defined a record type to define each loan.
    The record data items are:
       Data item     Data type                         Comment
     StudentID    STRING      the unique ID of the student who has borrowed the book
     BookID       STRING      the unique ID of the book being borrowed
     OnLoan       BOOLEAN     TRUE if the book has not been returned
    The programmer has defined a global array Loan to store 5000 loan records.
    There are more elements in the array than books in the library. Unused elements have the
    StudentID set to an empty string. These may occur anywhere in the array.
    The programmer has defined the first program module:
          Module                                Description
                        •   called  with  a  parameter  of  type  STRING  representing  a
                            StudentID
     OKToBorrow()    •   search the array for loan records for the specified student
                        •   output a suitable message to say whether the student may, or
                            may not, borrow another book
A second module is defined:
             Module                            Description
                          •   called with two parameters of type STRING representing a
                              StudentID and a BookID
                          •   searches the array for the relevant loan record
         ReturnBook()
                          •   when found, sets OnLoan to FALSE and returns TRUE
                          •   if a loan record is not found, or the book has already been
                              returned, then returns FALSE
        Write efficient pseudocode for the module ReturnBook()
        Assume that each student is only allowed to borrow each book only once. That means that
        there will be no more than one loan record for a given combination of student and book.
```

## Python 接口

入口：`ReturnBook(ThisStudentID,ThisBookID)`。参数顺序 StudentID、BookID；两者组合唯一。找到在借者只把该记录 OnLoan 改 False，返回 True；已归还或找不到返回 False，其余记录不变。不输出。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Loop through all elements in Loan array
- [ ] MP2：...and book loan not found
- [ ] MP3：Attempt to reference an individual data item in a loop
- [ ] MP4：Correct test for StudentID and correct BookID in a loop
- [ ] MP5：… If book not returned yet, then set OnLoan field to FALSE
- [ ] MP6：RETURN TRUE if book loan Found and not already returned
- [ ] MP7：RETURN FALSE if book loan Found and loan already returned
- [ ] MP8：RETURN FALSE if book loan not found
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
