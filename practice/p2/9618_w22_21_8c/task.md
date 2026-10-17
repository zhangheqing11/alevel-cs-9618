# 累计语法错误并在超限时停止

来源：9618_w22_21:8(c)；QP p16，MS p10，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A teacher is designing a program to perform simple syntax checks on programs written by
    students. Student programs are submitted as text files, which are known as project files.
    A project file may contain blank lines.
    The teacher has defined the first program module as follows:
              Module                                  Description
                               • takes the name of an existing project file as a parameter of type
                                string
     CheckFile()
                               • returns TRUE if the file is valid (it contains at least 10 non-blank
                                lines), otherwise returns FALSE
Further modules are defined as follows:
CheckLine(): takes a line from a project file as a parameter of type string;
returns zero if the line is blank or contains no syntax error, otherwise returns an error number as an integer.
CountErrors(): takes two parameters: the name of a project file as a string; the maximum number of errors as an integer;
uses CheckFile() to test the project file. Outputs an error message and ends if the project file is not valid;
calls CheckLine() for each line in the project file; counts the number of errors;
outputs the number of errors or a warning message if the maximum number of errors is exceeded.
Write pseudocode for module CountErrors(). Assume CheckFile() and CheckLine()
        have been written and can be used in your solution.
```

## Python 接口

入口：`CountErrors(ThisFile,MaxErrors)`。MaxErrors 非负。CheckFile / CheckLine 为已给定模块，必须使用，不自行重写语法检查器。输出只一行：无效 That program file is not valid；超限 Check terminated - too many errors；否则 There were <数> errors.。严格大于上限才停止；按 QP，最后一行刚超限仍输出超限警告（MS 范例以 EOF 判断该情形时会输出总数，D31 按 QP 测）。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `project.txt`：92 字节；最后一行无换行。


## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading and ending including parameters
- [ ] MP2：Declaration and initialisation of local Integer value for ErrCount
- [ ] MP3：Use of CheckFile(), output message and terminate if it returns FALSE
- [ ] MP4：Conditional loop until EOF()
- [ ] MP5：...or ErrCount > MaxErrors
- [ ] MP6：Read line and use as parameter to CheckLine()in a loop
- [ ] MP7：Test return value and increment ErrCount if non-zero in a loop
- [ ] MP8：Output either message once only as appropriate
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
