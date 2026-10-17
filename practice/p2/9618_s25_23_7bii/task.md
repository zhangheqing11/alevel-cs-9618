# 把 DDMMYYYY 转为日期

来源：9618_s25_23:7(b)(ii)；QP p18，MS p14，4 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A program is being developed to implement a customer loyalty scheme for a coffee shop.
    The programmer has decided that the following data items need to be stored for each customer:
       Data item                                 Description
     customer ID     a unique six-digit string
     loyalty points    an integer value that depends on how often the customer visits the coffee shop
     last visit date    the date the customer last visited the coffee shop
    The programmer has defined a program module:
          Module                                  Description
                       •  called with two parameters:
                          1.  loyalty points of type INTEGER
                          2.  last visit date of type DATE
                       •  change the loyalty points:
                          ○  increase by four if the last visit date and the current date are in the
     UpdateVisit()
                              same month
                          ○  otherwise increase by one
                       •  change the last visit date to the current date
                       •  the changed values must be available to the code that follows the call
                          to UpdateVisit()

A text file Loyalty.txt will be used to store the data items for the loyalty scheme.
        The text file Loyalty.txt contains only one line of data for each customer.
        Each data item is separated by a comma:
        <CustomerID>,<LoyaltyPointsString>,<LastVisitDateString>
        LastVisitDateString is always eight characters in length in the format: DDMMYYYY.
        An example of how a line of data will be stored in the text file Loyalty.txt is:
          "100123,132,05032025"
        This example shows that the customer with an ID of 100123 had 132 loyalty points following
        their last visit to the coffee shop on 05/03/2025.
        If a customer visits the coffee shop on a Monday, the value of their loyalty points is increased
        by 10.
        The programmer has defined two more program modules:
              Module                                Description
                            •  called with a parameter of type STRING that represents a
         FindCustomer()
                               customer ID
                            •  returns the line of data read from the text file Loyalty.txt
         (is already written)
                               containing the data items for that customer
         MondayCheck()   •  called with a parameter of type STRING that represents the
                               customer ID of a customer
                            •  calls FindCustomer()
                            •  extracts the loyalty points from the string returned by
                               FindCustomer()
                            •  increases the loyalty points for the current customer by 10 if the
                               day visited is a Monday
                            •  returns an integer value representing the loyalty points
A date is stored in LastVisitDateString in the format:
            DDMMYYYY
            DD is a 2-digit string
            MM is a 2-digit string
            YYYY is a 4-digit string.
            For example, the date 03/09/2024 is stored as "03092024"
            An algorithm is needed to convert the string stored in LastVisitDateString to data
            type DATE which is then stored in the variable LastVisitDate.
            Complete the pseudocode for this algorithm:
            Assume that LastVisitDateString has been declared and contains valid data.
            DECLARE DayInt, MonthInt, YearInt : INTEGER
            DECLARE LastVisitDate : DATE
```

## Python 接口

入口：`main()`。测试设置全局 LastVisitDateString，调用 main() 后核对全局 LastVisitDate。Python date 按年、月、日构造；指南 SETDATE 按日、月、年。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Use of one substring function
- [ ] MP2：DayInt, MonthInt and YearInt all correctly extracted
- [ ] MP3：Use of STR_TO_NUM x 3
- [ ] MP4：SETDATE() function used to convert to a date type and assigned to LastVisitDate
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
