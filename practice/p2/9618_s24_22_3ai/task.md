# 声明生产组件记录

来源：9618_s24_22:3(a)(i)；QP p7，MS p6，4 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A factory needs a program to help manage its production of items.
    Data will be stored about each item.
    The data for each item will be held in a record structure of type Component.
    The programmer has started to define the fields that will be needed as shown in the table.
          Field       Example value                 Comment
     Item_Num      123478         a numeric value used as an array index
     Reject         FALSE          TRUE if this item has been rejected
     Stage          'B'            a letter to indicate the stage of production
     Limit_1        13.5           any value in the range 0 to 100 inclusive
     Limit_2        26.4           any value in the range 0 to 100 inclusive
Write pseudocode to declare the record structure for type Component.
```

## Python 接口

入口：`Component`。TYPE 适配为 Component 类；构造参数按字段表顺序，参数类型已正确，同名公开字段。CHAR 在 Python 为单字符 str；无需无参默认构造或输入验证，类型声明仍人工逐点检查。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：One mark for TYPE and ENDTYPE statements
- [ ] MP2：One mark for Item_Num and Reject fields
- [ ] MP3：One mark for Stage field
- [ ] MP4：One mark for Limit fields as REAL
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
