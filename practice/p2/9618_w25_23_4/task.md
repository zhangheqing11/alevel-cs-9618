# 将逗号分隔的三位数存入数组

来源：9618_w25_23:4；QP p8，MS p8，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program contains a global 1D array Data containing 20 elements of type INTEGER
    A global string NumString represents a sequence of three-digit numbers, separated by commas.
    For example:
    "101,456,219,754,328"
    The string contains at least four three-digit numbers. The total number of three-digit numbers in
    the string is unknown.
    A procedure Store() will:
    •   extract one three-digit number at a time from NumString
    •   convert each of the three-digit numbers extracted to an integer and assign this to the next
        array element, starting from index 1
    •   end when all three-digit numbers have been stored, or when the array is full.
    Complete the pseudocode for Store()
    All local variables used must be declared.
    PROCEDURE Store()
    ENDPROCEDURE
```

## Python 接口

入口：`Store()`。QP 保证至少四个三位数字，用逗号分隔、无末尾逗号；不测少于四个、空串或非法格式。填入前 20 个或全部（较少时），不输出，不要求清零未用位置。切片在伪代码用 MID/LEFT/RIGHT；其他本题 MS 替代算法也按对应点人工核对。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 6 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Declare all local variables used
- [ ] MP2：Conditional loop while end of string not reached
- [ ] MP3：... and array not full
- [ ] MP4：Attempted use of MID() // Attempted use of Right() and Left()
- [ ] MP5：Correct extraction and use next three letter substring from NumString in a loop
- [ ] MP6：Convert to integer and assign value to array element in a loop
- [ ] MP7：Correct increment of array index by 1 and start position of substring by 4
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
