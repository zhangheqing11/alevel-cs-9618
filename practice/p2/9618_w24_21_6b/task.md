# 计算不考虑闰年的使用期限

来源：9618_w24_21:6(b)；QP p13，MS p10，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A factory produces food items. The items must be used within a certain number of days after their
    production date. The number of days is known as the shelf life. It is different for each type of item
    but is always a whole number in the range 1 to 21 (inclusive).
    The latest date that an item can be used is called the ‘use-by’ date.
    A program is needed to produce labels which show the ‘use-by’ date.
    Part of the program is a function GetDate() which will:
    •   take two parameters: a production date and a value representing the shelf life
    •   return the corresponding ‘use-by’ date.
    The program contains a global 1D array DaysInMonth of type integer which stores the number of
    days in each month (index 1 is January):
       Index     Value
         1        31
         2        28    Note: Leap years are not considered
         3        31
         4        30
         11        30
        12        31
Complete the pseudocode for the function GetDate().
        Date functions from the insert should be used in your solution.
    FUNCTION GetDate(ProductionDate : DATE, ShelfLife : INTEGER) RETURNS DATE
    ENDFUNCTION
```

## Python 接口

入口：`GetDate(ProductionDate,ShelfLife)`。日期参数/返回均 datetime.date；ShelfLife 在 1–21。QP 明确忽略闰年，测试使用非闰年；下标 month−1。不输出。Python 属性读日月年、date 构造对应插页 DAY/MONTH/YEAR/SETDATE；伪代码仍按插页写。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 7 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Declare three variables of TYPE INTEGER to store DD, MM and YY
- [ ] MP2：Correct use of date functions from Insert to extract three integer values representing DD, MM and YY and use/assign to a variable
- [ ] MP3：Add parameter ShelfLife to DD and use / assign result to a variable
- [ ] MP4：Extract LastDay from DaysInMonth using MM as Index
- [ ] MP5：Test for new DD after end of month / DaysInMonth[MM] … and if DD > DaysInMonth[MM]:
- [ ] MP6：MM is incremented by 1 and DD is set to DD – DaysInMonth[MM]
- [ ] MP7：If MM = 13 / MM > 12 then increment YY and set MM to 1
- [ ] MP8：Use of SETDATE to assign value to NewDate, NewDate must have been delared as a type DATE
- [ ] MP9：Return date
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
