# 咖啡积分兑换

来源：9618_s25_21:7(a)；QP p15，MS p12，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

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
Write pseudocode for module CustomerOrder()
```

## Python 接口

入口：`CustomerOrder(Number,Points)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function header and ending and parameters and return type
- [ ] MP2：Number of coffees ordered added to points
- [ ] MP3：Correct calculation of one free coffee
- [ ] MP4：Attempted calculation of multiple free coffees and reduced NewPoints
- [ ] MP5：Output number of free drinks with suitable message
- [ ] MP6：Return of NewPoints
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
