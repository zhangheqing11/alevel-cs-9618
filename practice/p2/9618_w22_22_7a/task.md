# 输出对应的语法错误描述

来源：9618_w22_22:7(a)；QP p17，MS p11，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A teacher is designing a program to perform simple syntax checks on programs written by
    students.
    Two global 1D arrays are used to store the syntax error data. Both arrays contain 500 elements.
    •   Array ErrCode contains integer values that represent an error number in the range 1 to 800.
    •   Array ErrText contains string values that represent an error description.
    The following diagram shows an example of the arrays.
      Index        ErrCode                         ErrText
        1             10          "Invalid identifier name"
        2             20          "Bracket mismatch"
        3             50          "Undeclared variable"
        4             60          "Type mismatch in assignment"
       …
       500           999                  <Undefined>
    Note:
    •   There may be less than 500 error numbers so corresponding elements in both arrays may be
        unused. Unused elements in ErrCode have the value 999. The value of unused elements in
        ErrText is undefined.
    •   Values in the ErrCode array are stored in ascending order but not all values may be present,
        for example, there may be no error code 31.
    The teacher has defined two program modules as follows:
           Module                                  Description
                         •   takes two parameters as integers:
                              ○   a line number in the student’s program
                              ○   an error number
                         •   searches for the error number in the ErrCode array:
     OutputError()
                              ○   if found, outputs the corresponding error description and the
                                  line number, for example:
                                      "Bracket mismatch on line 34"
                              ○   if not found, outputs the line number and a warning, for
                                  example:
                                      "Unknown error on line 34"
     SortArrays()      sorts the arrays into ascending order of ErrCode
Write efficient pseudocode for module OutputError().
```

## Python 接口

入口：`OutputError(LineNum,ErrNum)`。输入错误号在 1–800，QP 下标−1；数组已按错误号升序，未使用项 999。只 print 一行 <描述> on line <LineNum>，找不到时 Unknown error on line <LineNum>；不改数组，禁止内置查找替代。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 6 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading and ending including parameters
- [ ] MP2：Conditional loop containing incrementing Index...
- [ ] MP3：...terminating when ErrNum found
- [ ] MP4：...terminating when ErrCode[Index] > ErrNum (i.e. ErrNum not found)
- [ ] MP5：... OR after element 500 tested
- [ ] MP6：Test if found and OUTPUT 'Found' message
- [ ] MP7：...otherwise OUTPUT 'Not Found' message
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
