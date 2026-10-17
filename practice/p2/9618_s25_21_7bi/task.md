# 为忠诚计划追加新客户

来源：9618_s25_21:7(b)(i)；QP p16，MS p13，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program is being developed to implement a customer loyalty scheme for a coffee shop.
    The programmer has decided that the following data items need to be stored for each customer:
          Data item                              Description
      customer ID        a unique six-digit string
                        an integer value that is increased by one for every cup of coffee the
      points
                        customer orders
    When a customer visits the shop and orders coffee, the scheme operates as follows:
    •   The total number of points is increased by the number of coffees ordered.
    •   If just one cup of coffee is ordered and the number of points goes above 10, then:
        ◦   the cup of coffee they have just ordered is given to them free of charge
        ◦   the number of points is reduced by 11.
    •   If the order is for multiple coffees and the number of points goes above 10, then:
        ◦   they get one coffee free of charge for every 11 points
        ◦   the number of points is reduced by 11 for each free coffee.
    For example, the:
    •   customer currently has 9 points
    •   customer orders 16 cups of coffee
    •   total number of points now becomes 25
    •   customer gets 2 free coffees and now has 3 points left.
    The programmer has defined a program module that is called every time a customer places an
    order:
            Module                                Description
                             •   called with two integer parameters:
                                 ◦   the number of coffees ordered
     CustomerOrder()          ◦   the current number of points
                             •   output a suitable message giving the number of free coffees
                             •   return a value for the new points total.

A text file Loyalty.txt will be used to store the data items for the loyalty scheme. The data
        items for each customer will be stored on a separate line of the text file where each data item
        is separated by a comma:
        <CustomerID>,<Points>
        The contents of the text file Loyalty.txt will always be stored in ascending order by
        customer ID.
        When the data items are read from or written to the text file Loyalty.txt, they may need to
        be converted to the appropriate data type.
        Each customer has a unique customer ID starting at "100001" with this value increasing by
        one each time a new customer joins the loyalty scheme.
        When a customer joins the loyalty scheme, they are assigned the next customer ID and value
        of points is set to 0.
        For example, if the loyalty scheme has 204 customers and a new customer joins the loyalty
        scheme, the following line is added to the text file Loyalty.txt:
        "100205,0"
        You can assume that the number of customers in the loyalty scheme will never be more than
        9000.
        The programmer has defined a program module as follows:
           Module                                Description
                           •   called with an integer parameter representing the number of
                               new customers to be added to the loyalty scheme
                           •   adds a new line, containing the required information, to the
     AddNewCustomers()
                               text file Loyalty.txt for each customer added to the loyalty
                               scheme
                           •   outputs each new customer ID added to the loyalty scheme
Write pseudocode for module AddNewCustomers()
            Assume that there is at least one customer already in the loyalty scheme.
```

## Python 接口

入口：`AddNewCustomers(NumToAdd)`。QP 保证至少一位已有客户，总人数不超过 9000，NumToAdd 非负。空文件不测。每个新 ID 单独 print 一行，只含六位 ID；新文件记录为 <ID>,0，无额外空格，LF 结束。末行无换行时先补记录分隔换行；原记录内容保留。加入 0 位时不改文件、不输出。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `Loyalty.txt`：18 字节；最后一行有换行。


## 人工核对清单

本题 MS 总分上限 8 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：All variables used are declared using the correct type including a string and an integer
- [ ] MP2：Open file in read mode and close (before opening in append mode)
- [ ] MP3：Conditional loop with EOF("Loyalty.txt")
- [ ] MP4：Read Line from file // Count number of records in the file
- [ ] MP5：Open the file in append mode and subsequently close
- [ ] MP6：Extract CustomerID from Line and convert to integer // use count from MP4 to generate last CustomerID stored
- [ ] MP7：A (count controlled) loop for the number of customers to add
- [ ] MP8：Increment CustomerID and output the new CustomerID in loop
- [ ] MP9：Create string for new CustomerID and write to file in loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
