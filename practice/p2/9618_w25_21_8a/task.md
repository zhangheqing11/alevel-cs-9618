# 检查学生能否再借一本书

来源：9618_w25_21:8(a)；QP p15，MS p17，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

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
Write efficient pseudocode for the module OKToBorrow()
```

## Python 接口

入口：`OKToBorrow(ThisStudentID)`。StudentID 非空；任意位置可有未用记录；只数本学生且 OnLoan 为 True 的记录。只 print 一行 Student may borrow another book 或 Student may not borrow another book，不改数组。五本上限、找到五本提前结束人工核对。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading, parameter and ending
- [ ] MP2：Loop through all elements in Loan array
- [ ] MP3：... terminating if Max reached
- [ ] MP4：Test for correct StudentID field in a loop
- [ ] MP5：... and that OnLoan = TRUE in a loop
- [ ] MP6：... if so, then increment Count in a loop
- [ ] MP7：Output an appropriate message in both cases after the loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。

本题语料将 MS 原页 MP5 的“检查 OnLoan”与下一行“递增 Count”拆成语料 MP5、MP6；语料 MP7 对应原页 MP6 输出。下列清单和测试引用语料点号，人工可据此映射原页；未把两份不同编号当成额外得分。QP/MS 总分均为 7。
