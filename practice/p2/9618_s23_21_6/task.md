# 混合六路采样数据

来源：9618_s23_21:6；QP p10，MS p7，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A video-conferencing program supports up to six users. Speech from each user is sampled and
    digitised (converted from analogue to digital). Digitised values are stored in array Sample.
    The array Sample consists of 6 rows by 128 columns and is of type integer. Each row contains
    128 digitised sound samples from one user.
    The digitised sound samples from each user are to be processed to produce a single value which
    will be stored in a 1D array Result of type integer. This process will be implemented by procedure
    Mix().
    A procedure Mix() will:
    •   calculate the average of each of the 6 sound samples in a column
    •   ignore sound sample values of 10 or less
    •   store the average value in the corresponding position in Result
    •   repeat for each column in array Sample
    The diagram uses example values to illustrate the process:
                              1    2    3            ...           126  127  128
                         1   20   20   20                        30   30   2
                         2   20   20   30                        50   30   3
                         3   20   20   40                        40   40   4
           Sample:
                         4   20   20   50                        40   50   20
                         5   20   3    5                         6   60   4
                         6   20   4    2                         4   70   30
           Result:          20   20   35                        40   46   25
    Write pseudocode for procedure Mix().
    Assume Sample and Result are global.

```

## Python 接口

入口：`Mix()`。Python 行列下标=QP下标−1；原位填写 Result，Sample 不变，不输出。每列至少一个值大于 10；QP 未定义整列均被忽略时的平均数，测试不构造该情况。截断取整数，不能四舍五入。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 6 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Declaration and initialisation before inner loop of Count and Total
- [ ] MP2：Outer Loop for 128 iterations
- [ ] MP3：Inner loop for six iterations
- [ ] MP4：Test for sample > 10 in a loop
- [ ] MP5：and if true sum Total and increment Count
- [ ] MP6：Calculate average value and assign to Result array after inner loop and within outer loop
- [ ] MP7：Use of INT()/ DIV to convert average to integer
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
