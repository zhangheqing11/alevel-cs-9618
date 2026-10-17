# 输出可兑换客户及平均积分

来源：9618_s25_22:7(b)；QP p16，MS p19，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program is being developed to implement a customer loyalty scheme for a coffee shop.
    Each customer has a unique customer ID starting at 10001 with this value increasing by one each
    time a new customer joins the loyalty scheme.
    For example, the third customer who joins the loyalty scheme is given the customer ID 10003
    The loyalty scheme is limited to 1000 customers.
    A customer is awarded a loyalty point every time they buy a coffee.
    The programmer has decided to use a global 2D array Loyalty of type INTEGER. The array
    Loyalty is made up of 1000 rows and 2 columns. Each row relates to one customer; column 1
    contains the unique customer ID and column 2 contains the number of customer loyalty points.
    Rows in the array Loyalty that are not currently being used have the value of Column 1 set to
    99999
    The array is sorted in ascending order by customer ID.
    The programmer has defined a program module:
           Module                                  Description
                         •   called with parameter of type INTEGER representing a customer ID
                         •   searches the Loyalty array for this customer ID
                         •   the search will stop as soon as the customer ID is found
     FindCustomer()
                         •   the search should efficiently deal with the situation when the
                             customer ID is not stored in the Loyalty array
                         •   if the customer ID is found, return an integer value representing the
                             loyalty points, otherwise return -1
A customer can claim a free coffee for every 11 loyalty points.
        The programmer has defined a second program module:
                 Module                                Description
                                 •   output the customer ID for each customer who has 11 or
                                     more loyalty points
         PointsReport()
                                 •   output the average loyalty points for all customers in the
                                     Loyalty array along with an appropriate message
        Write efficient pseudocode for module PointsReport()
        Assume the array contains the data for at least one customer.
```

## Python 接口

入口：`PointsReport()`。至少一位客户（QP 明确前提，不测空表），Python 行列=QP下标−1。符合者按数组顺序每个 print 一行，只含客户 ID；最后 print 一行 The average points of all the customers is <平均值>，数值接受等值浮点表示。不统计 99999 行。满表也须安全结束，不依赖越界读取后的 AND 短路。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 7 分，候选得分点不能简单相加超过此上限。

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Create procedure header and ending
- [ ] MP2：Declare and initialise Index, Sum and Count
- [ ] MP3：Loop through all elements in Loyalty array
- [ ] MP4：… or terminates when column1 of Loyalty array equals 99999 in a loop
- [ ] MP5：Check if loyalty points greater than or equal to 11 in a loop
- [ ] MP6：If true output customer ID
- [ ] MP7：Sum points and Increment Count in a loop
- [ ] MP8：Calculate and output average with an appropriate message
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
