# 查找客户积分

来源：9618_s25_22:7(a)；QP p15，MS p16，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

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
Write efficient pseudocode for module FindCustomer()
```

## Python 接口

入口：`FindCustomer(CustomerID)`。Python 行列=QP下标−1，未使用行第一列 99999；未使用行第二列不可用于统计。找到返回积分（可以为 0），不存在/超范围返回 -1，不输出、不改表。行为测兼容本题 MS 明确认可的顺序查找、二分查找与按连续 ID 直接定位，人工清单下列为条件循环主方案；其他方案按同题 MS 相应条目批改。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Create function header and ending with correct parameter and return type
- [ ] MP2：Check CustomerID is in range and if not return −1
- [ ] MP3：(Conditional) loop iterating through each element in array
- [ ] MP4：Check for current element in array contains required customer ID in a loop
- [ ] MP5：… If found set value to terminate loop
- [ ] MP6：Terminating loop when customer ID found
- [ ] MP7：Terminating loop when current customer ID is 99999
- [ ] MP8：Return either loyalty points for the customer found or –1 if not found
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
