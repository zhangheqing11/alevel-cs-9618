# 声明并清空合法分数查表

来源：9618_w25_22:4(a)；QP p6，MS p9，4 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A quiz has nine questions. There are:
    •   five easy questions each worth 3 points
    •   four hard questions each worth 5 points.
    At the end of the quiz the points for each correctly answered question are added to give a total
    score.
    A check is made to test that the total score is valid using a 1D array CheckTotal of type BOOLEAN.
    Each index value of the array represents a possible total score. The corresponding element value
    is TRUE if the index value represents a valid total score and FALSE otherwise.
    The first nine rows of the array are:
      Index    Element
                                                     Comment
      value     value
        0     TRUE        valid total score (no correct answers)
        1     FALSE      invalid total score
        2     FALSE      invalid total score
        3     TRUE        valid total score (one 3-point question correct)
        4     FALSE      invalid total score
        5     TRUE        valid total score (one 5-point question correct)
        6     TRUE        valid total score (two 3-point questions correct)
        7     FALSE      invalid total score
        8     TRUE        valid total score (one 3-point question and one 5-point question correct)
    For example, a total score of 6 points is valid; the value of the array element at index value 6 is TRUE
Write pseudocode to declare CheckTotal and to set all elements of the array to FALSE
        All variables used must be declared.
```

## Python 接口

入口：`main()`。原题是声明加初始化，Python main 执行后提供全局 CheckTotal 真实 list，下标 0–35（最高分 5×3+4×5）。本问全部设 False，尚未计算合法总分，不能按前文示例提前设 True。不输出。声明本身是作答内容，不放进 provided 骨架。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Declaration of CheckTotal array
- [ ] MP2：Declaration of a loop counter
- [ ] MP3：Loop – with correct syntax and number of iterations
- [ ] MP4：Assignment of array element to FALSE
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
