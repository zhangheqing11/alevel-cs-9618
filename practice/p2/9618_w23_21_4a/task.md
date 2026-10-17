# 判断精确匹配次数是否超限

来源：9618_w23_21:4(a)；QP p6，MS p6，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A global array is declared in pseudocode as follows:
        DECLARE Data : ARRAY[1:150] OF STRING
    A function TooMany() will:
        1.  take two parameters:
            •   a string (the search string)
            •   an integer (the maximum value)
        2.  count the number of strings in the array that exactly match the search string
        3.  return TRUE if the count is greater than the maximum value, otherwise will return FALSE
Write pseudocode for the function TooMany().
```

## Python 接口

入口：`TooMany(Search,Max)`。Data 真实 150 项，Python 下标=QP下标−1，精确、区分大小写匹配；返回 bool，不输出，不改数组，不能用内置查找计数替代循环。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Function heading, ending and return type
- [ ] MP2：Declare Count and Index as integers
- [ ] MP3：Initialise Count
- [ ] MP4：Loop (any type) for 150 iterations
- [ ] MP5：Compare Data element with parameter - if equal, increment Count in a loop
- [ ] MP6：Compare Count with Max and return Boolean in both cases outside the loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
