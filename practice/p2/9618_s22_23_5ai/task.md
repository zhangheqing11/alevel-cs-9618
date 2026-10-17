# 定义员工记录类型

来源：9618_s22_23:5(a)(i)；QP p6，MS p5，4 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

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
Write pseudocode to declare the record structure for type Employee.
```

## Python 接口

入口：`Employee`。TYPE 题的 Python 对应为 Employee 类，构造参数按 QP 字段表顺序，参数已是正确类型，存入同名公开属性。Born 用 datetime.date。QP 未定义默认值，因此不要求无参构造或自选默认值；类型声明仍由人工核对。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：TYPE Employee and ENDTYPE
- [ ] MP2：Fields: EmployeeNumber and Name and Department
- [ ] MP3：Field: Born
- [ ] MP4：Field: Attendance
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
