# 存入严格递增的实时输入

来源：9618_w25_21:4(a)；QP p6，MS p10，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program contains a global 1D array Number consisting of 20 elements of type REAL
    A procedure Store() will input a sequence of up to 20 real values, one value at a time. These
    values will be assigned to elements of the array using four steps:
    Step 1:  store the first value in the sequence in the first element of the array
    Step 2:  check each subsequent value input. If this value is larger than the previous value input,
            then assign the value to the next array element, otherwise go to step 4
    Step 3:  repeat from step 2 unless the array is full
    Step 4:  output the count of the number of values stored in the array together with a suitable
            message.
Complete the pseudocode for Store()
        All variables used in the algorithm must be declared.
        PROCEDURE Store()
        ENDPROCEDURE
```

## Python 接口

入口：`Store()`。使用 input(prompt) 每次读一实数；不递增的输入不存入，满 20 后不得再读第 21 个。测试均提供足够值到这两个明示终止条件之一，不测试无输入或提早 EOF。只 print 一行 <数量> values were stored in the array；未使用单元原值 QP 未定义，测试不限制。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Declare local variables Index as integer, ThisNum and LastNum as real
- [ ] MP2：Input value and assign to first element
- [ ] MP3：Attempt at conditional loop including both tests
- [ ] MP4：Completely correct conditional loop including both tests
- [ ] MP5：Assign input value to current element if greater than previous element and input next value in a loop
- [ ] MP6：Final output giving attempted count of elements stored plus message after a loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
