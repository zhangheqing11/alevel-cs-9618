# 将每组三个采样压缩成平均值

来源：9618_w22_21:5；QP p8，MS p6，5 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program uses two 1D arrays of type integer. Array1 contains 600 elements and Array2
    contains 200 elements.
    Array1 contains sample values read from a sensor. The sensor always takes three consecutive
    samples and all of these values are stored in Array1.
    A procedure Summarise() will calculate the average of three consecutive values from Array1
    and write the result to Array2. This will be repeated for all values in Array1.
    The diagram below illustrates the process for the first six entries in Array1.
       Array1    }                           Array2
                                                                  Comment
         10                                      15       average of first three values
         20                                      41      average of next three values
                  }
         15
         40
         41
         42
    Write pseudocode for the procedure Summarise().
```

## Python 接口

入口：`Summarise()`。两组真实 list，QP 下标−1；原位填 Array2，Array1 保持原值，不输出。INTEGER 输出采用 INT 截断，按 MS MP4 检查；不以 round 替代。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 5 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading and ending and declaration of both indexes
- [ ] MP2：Loop to process all elements from Array1
- [ ] MP3：Sum (any) three consecutive values from Array1 and divide by 3 in a loop
- [ ] MP4：Convert result to Integer
- [ ] MP5：Assign value to correct element of Array2 in a loop
- [ ] MP6：Increment Array2 index in a loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
