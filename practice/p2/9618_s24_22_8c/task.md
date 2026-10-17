# 清理项目并追加到第二阶段文件

来源：9618_s24_22:8(c)；QP p20，MS p12，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A teacher is designing a program to process pseudocode projects written by her students.
    Each student project is stored in a text file.
    The process is split into a number of stages. Each stage performs a different task and creates a
    new file.
    For example:
            File name                              Comment
     MichaelAday_src.txt  Student project file produced by student Michael Aday
     MichaelAday_S1.txt    File produced by stage 1
     MichaelAday_S2.txt    File produced by stage 2
Two modules are defined:
               Module                                Description
         DeleteComment()  • called with a parameter of type string representing a line of
         (already written)        pseudocode from a student’s project file
                              • returns the line after removing any comment
         Stage_2()          • called with two parameters:
                                ○ a string representing an input file name
                                ○ a string representing an output file name
                              • copies each line from the input file to the existing output file having
                               first removed all leading spaces and comments from that line
                              • does not write blank lines to the output file
                              • outputs a final message giving the number of blank lines removed
        Write pseudocode for module Stage_2().
        Modules DeleteComment() and DeleteSpaces() must be used in your solution.
```

## Python 接口

入口：`Stage_2(F1,F2)`。F2 是已存在输出文件，必须追加并保留已有内容。提供 DeleteSpaces / DeleteComment（见骨架），必须使用两者；每条新增行用 LF 结束。执行后只 print 一行 <数量> blank lines were removed，不加其它输出。按 QP 删除空白行；全空格行经 DeleteSpaces 变空串，照 D31 计入删除数。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `input.txt`：45 字节；最后一行有换行。
- `output.txt`：14 字节；最后一行有换行。


## 人工核对清单

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading, parameters, ending
- [ ] MP2：Open both files in correct modes and subsequently close
- [ ] MP3：Loop to EOF(F1)
- [ ] MP4：Read a line from F1 in a loop
- [ ] MP5：Assign return values from DeleteComment() and DeleteSpaces() in a loop
- [ ] MP6：Check return value following both MP5 function calls is not an empty string and if so write to F2 in a loop
- [ ] MP7：Count the blank lines in a loop
- [ ] MP8：Output number of blank lines removed following a reasonable attempt after the loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
