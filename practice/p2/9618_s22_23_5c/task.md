# 输出出勤不足的员工

来源：9618_s22_23:5(c)；QP p7，MS p6，4 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program will store attendance data about each employee of a company.
    The data will be held in a record structure of type Employee. The fields that will be needed are as
    shown:
               Field                  Typical value                   Comment
     EmployeeNumber         123                       A numeric value starting from 1
     Name                     "Smith,Eric"            Format: <last name>','<first name>
     Department              "1B"                     May contain letters and numbers
     Born                     13/02/2006              Must not be before 04/02/1957
     Attendance              97.40                    Represents a percentage

A 1D array Staff containing 500 elements will be used to store the employee records.
A procedure Absentees() will output the EmployeeNumber and the Name of all employees
        who have an Attendance value of 90.00 or less.
        Write pseudocode for the procedure Absentees().
        Assume that the Staff array is global.
```

## Python 接口

入口：`Absentees()`。Staff 真实存放 500 个独立 Employee，Python 下标=QP下标−1。沿用本题 MS 的可接受未使用标记 EmployeeNumber=-1（QP 前问让考生选择标记）；其余字段对未使用项不作要求。按数组顺序，每位符合条件员工先 print 编号一行，再 print 姓名一行，不加说明；没有符合者不输出。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 4 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading and ending and declaration of loop counter
- [ ] MP2：loop through 500 elements
- [ ] MP3：attempt to skip unused element
- [ ] MP4：test Staff[Index].Attendance <= 90 in a loop
- [ ] MP5：if so, output EmployeeNumber and Name fields in a loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
