# 输出错误号范围及缺失描述警告

来源：9618_w22_23:7(a)；QP p13，MS p8，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A teacher is designing a program to perform simple syntax checks on programs written by
    students.
    Two global 1D arrays are used to store the syntax error data. Both arrays contain 500 elements.
    •   Array ErrCode contains integer values that represent an error number in the range 1 to 800.
    •   Array ErrText contains string values that represent an error description.
    The following diagram shows an example of the arrays.
           Index      ErrCode                       ErrText
             1           10         "Invalid identifier name"
             2           20         "Bracket mismatch"
             3           50         ""
             4           60         "Type mismatch in assignment"
             ...
            500         999        <Undefined>
    Note:
    •   There are less than 500 error codes so corresponding elements in both arrays may be
        unused. Unused elements in ErrCode have the value 999. These will occur at the end of the
        array. The value of unused elements in ErrText is undefined.
    •   Values in the ErrCode array are stored in ascending order but not all values may be present.
        For example, there may be no error code 31.
    •   Some error numbers are undefined. In these instances, the ErrCode array will contain a
        valid error number but the corresponding ErrText element will contain an empty string.
    The teacher has defined one program module as follows:
             Module                                Description
                             • Prompts for input of two error numbers
                             • Outputs a list of error numbers between the two numbers input
                               (inclusive) together with the corresponding error description
                             • Outputs a warning message when the error description is
                               missing as for error number 50 in the example
                             • Outputs a suitable header and a final count of error numbers
                               found
     OutputRange()
                             Output based on the example array data above:
                                 List of error numbers from 1 to 60
                                 10 : Invalid identifier name
                                 20 : Bracket mismatch
                                 50 : Error Text Missing
                                 60 : Type mismatch in assignment
                                 4 error numbers output
Write pseudocode for module OutputRange(). Assume that the two numbers input
        represent a valid error number range.
```

## Python 接口

入口：`OutputRange()`。用 input(prompt) 按先 First 后 Last 读合法的闭区间，提示不另 print（D13）。输出逐行遵循 QP 示例：标题 List of error numbers from <First> to <Last>；每项 <错误号> : <描述>，空描述用 Error Text Missing；末行 <数量> error numbers output。空行可选。数组少于 500 个有效错误号，999 在尾部，未使用描述不检查。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 8 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Declaration and initialisation of local integer for Count
- [ ] MP2：Appropriate prompt and two inputs
- [ ] MP3：(Conditional) loop while error number input is in range // error code 999 reached
- [ ] MP4：…and not end of array
- [ ] MP5：Check if this ErrCode needs to be output in a loop
- [ ] MP6：if so check for blank error text in a loop
- [ ] MP7：Output in both cases
- [ ] MP8：….and increment count in a loop
- [ ] MP9：OUTPUT of header and summary including count
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
