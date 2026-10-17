# 添加错误条目并维持有序

来源：9618_w22_23:7(b)(i)；QP p16，MS p9，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

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
Two additional modules are defined:
             Module                              Description
       SortArrays()      • Sorts the arrays into ascending order of ErrCode
                           • Takes two parameters:
                             •  an error number as an integer
                             •  an error description as a string
                           • Writes the error number and error description to the first
       AddError()          unused element of the two arrays. Ensures the ErrCode
                             array is still in ascending order
                           • Returns the number of unused elements after the new error
                             number has been added
                           • Returns −1 if the new error number could not be added
            Write pseudocode for the module AddError(). Assume that the error code is not
            already in the ErrCode array.
```

## Python 接口

入口：`AddError(ErrNum,ErrMess)`。ErrNum 是合法且尚不存在的错误号。写入第一个 999 位置，然后使用 provided SortArrays，返回剩余空位数；满表返回 -1 且不改表。不输出。初始少于 500 是 QP 主背景；本模块明确包含无法加入的返回值，因此额外测试满表这一明示分支。Python 下标=QP−1。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：(Conditional) loop terminating when item added OR end of array reached
- [ ] MP2：Test for unused element in a loop
- [ ] MP3：Assignment of values to arrays // save index of first blank location and assign after loop
- [ ] MP4：Set loop termination if empty element found in a loop
- [ ] MP5：Call SortArrays() once
- [ ] MP6：Calculation of remaining unused elements and return Integer value (for both cases)
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
