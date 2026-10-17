# 从项目文件提取模块信息

来源：9618_s24_23:8(b)；QP p20，MS p13，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A teacher is designing a program to process pseudocode projects written by her students.
    The program analyses a student project and extracts information about each module that is
    defined (each procedure or function). This information is stored in a global 2D array ModInfo of
    type string.
    A module header is the first line of a module definition and starts with either of the keywords
    PROCEDURE or FUNCTION.
    An example of part of the array is given below. Row 10 of the array shows that a procedure header
    occurs on line 27 and row 11 shows that a function header occurs on line 35. "P" represents a
    procedure and "F" represents a function:
                         x = 1  x = 2                   x = 3
    ModInfo[10, x]    "27"    "P"     "MyProc(Z : CHAR)"
    ModInfo[11, x]    "35"    "F"     "MyFun(Y : CHAR) RETURNS BOOLEAN"
    The string stored in column 3 is called the module description. This is the module header without
    the keyword.
    A valid module header will:
    •   be at least 13 characters long
    •   start with the keyword PROCEDURE or FUNCTION. The keyword may appear in either upper or
        lower case (or a mix of both) and must be followed by a space character.
    The teacher has defined the first program module as follows:
          Module                                Description
     Header()         •   called with a parameter of type string representing a line of
                            pseudocode
                        •   if the line is a valid procedure header, returns a string:
                               "P<Module description>"
                        •   if the line is a valid function header, returns a string:
                               "F<Module description>"
                        •   otherwise, returns an empty string
                            For example, given the string:
                            "FUNCTION Zap(X : INTEGER) RETURNS CHAR"
                            Header()returns the string:
                            "FZap(X : INTEGER) RETURNS CHAR"
A new module is required:
                Module                                Description
         FindModules()      •   called with a parameter of type string representing a student
                                   project file name
                               •   uses module Header() to check each line of the project
                               •   assigns values to the ModInfo array for each module
                                   declaration in the student project
        As a reminder, the previous example of part of the array is repeated below:
                             x = 1  x = 2                   x = 3
        ModInfo[10, x]    "27"    "P"     "MyProc(Z : CHAR)"
        ModInfo[11, x]    "35"    "F"     "MyFun(Y : CHAR) RETURNS BOOLEAN"
        Write pseudocode for module FindModules().
        Assume that the array contains enough rows for the number of modules in each project.
```

## Python 接口

入口：`FindModules(FileName)`。ModInfo 三列全部 STRING；Python 行列=QP下标−1，文件行号从 1 起。QP 未给行数，骨架提供足够的 100 行示例容量，测试也会换为足够容量的 list。每次从首行填充；未使用行的内容 QP 未规定，因此测试不要求清零。必须使用 Header 返回值；不输出。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `project.txt`：89 字节；最后一行无换行。


## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Open file in READ mode and subsequently close
- [ ] MP2：Loop to EOF(FileName)
- [ ] MP3：Read a line from the file and maintain LineNum in a loop
- [ ] MP4：Call Header() and use return value in a loop
- [ ] MP5：Test return value for "" in a loop
- [ ] MP6：Attempt at all three-array assignment for all columns in correct row
- [ ] MP7：Correct values assigned to all columns of array
- [ ] MP8：Maintain correct array row index
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
