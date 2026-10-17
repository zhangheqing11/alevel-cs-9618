# 比较奇偶下标元素总和

来源：9618_s24_21:4；QP p8，MS p7，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A global 1D array Data contains 100 elements of type integer.
    A function Check() will:
    •   total the element values in odd index locations (1, 3, 5 ... 97, 99)
    •   total the element values in even index locations (2, 4, 6 ... 98, 100)
    •   return one of three strings ‘Odd’, ‘Even’ or ‘Same’ to indicate which total is the greater, or
        whether the totals are the same.
    Write pseudocode for the function Check().
```

## Python 接口

入口：`Check()`。Data[0] 对应 QP Data[1]，奇偶按 QP 下标判断。返回字符串 Odd / Even / Same，不输出，不修改数组。MS 范例遗漏 RETURN 比较段，但 MP6 明确要求，参考解按 QP 与该得分点补齐。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Function heading, ending and return type
- [ ] MP2：Declare local variables Odd, Even and Index as integers
- [ ] MP3：Initialise Odd and Even
- [ ] MP4：Loop for 100 iterations // through array
- [ ] MP5：Sum Odd and Even element values in a loop
- [ ] MP6：Compare Odd and Even after the loop and Return appropriate string
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
