# 声明租车记录

来源：9618_w25_21:3(a)(i)；QP p5，MS p9，4 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program is needed to manage individual rentals in a car-hire business.
    The data items for each rental will be held in a record structure of type RentalRecord
    The programmer has started to define the items that will be needed:
         Item      Example value                       Comment
     RentalID   "AB1234"       a unique alpha-numeric value
     CarID       241             a numeric value used as an array index
     DisCode    'S'             a letter indicating the type of discount offered
     Start       13/06/2025    when the rental starts
     Duration   7               the number of days of the rental
     Completed  FALSE          TRUE when the car is returned and the rental charge paid
Write pseudocode to declare the record structure for type RentalRecord
```

## Python 接口

入口：`RentalRecord`。TYPE 题以 RentalRecord 类适配，构造参数依字段表顺序，已是正确类型；公开同名属性。DATE 对应 datetime.date，CHAR 对应单字符 str。QP 未定义默认值，不要求无参构造或参数校验；声明类型仍人工核对。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：One mark for TYPE RentalRecord and ENDTYPE statements
- [ ] MP2：One mark for RentalID and CarID declared correctly
- [ ] MP3：One mark for DisCode and Start declared correctly
- [ ] MP4：One mark for Duration and Completed declared correctly
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
