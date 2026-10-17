# 按访问月份更新积分和日期

来源：9618_s25_23:7(a)(i)；QP p14，MS p12，5 分。已对照 QP 原页核对下列题干、表格与示例。

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
Write pseudocode for module UpdateVisit()
            Assume the customer has made at least one previous visit.
```

## Python 接口

入口：`UpdateVisit(LoyaltyPoints,LastVisitDate)`。参数顺序按 QP 模块表：积分、日期（MS 范例顺序相反）。两个 BYREF 参数用单元素 list 表示；修改 [0] 使调用者可见。日期用 datetime.date，TODAY 可由测试替换。测试只覆盖同一年内的同月与不同月；跨年同月是否加四分在 QP 未定义，依 D31 不测。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 5 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Procedure heading and ending and two parameters of correct type
- [ ] MP2：… both passed BYREF
- [ ] MP3：Use of TODAY() function to obtain current date
- [ ] MP4：Use MONTH function (×2) and one parameter is the header parameter and 2nd parameter is TODAY() / assigned variable
- [ ] MP5：If visit is same month, increase LoyaltyPoints by 4 otherwise increase by 1
- [ ] MP6：LastVisitDate set to TODAY() / ‘current date’ variable (assigned or unassigned)
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
