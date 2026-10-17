# 删除项目注释并生成第一阶段文件

来源：9618_s24_21:8(b)；QP p20，MS p12，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A teacher is designing a program to process pseudocode projects written by her students.
    Each student project is stored in a text file.
    The process is split into a number of stages. Each stage performs a different task and creates a
    new file named as shown:
            File name                              Comment
     MichaelAday_src.txt   student project file produced by student Michael Aday
     MichaelAday_S1.txt    file produced by stage 1
     MichaelAday_S2.txt    file produced by stage 2
    The teacher has defined the first program module as follows:
           Module                                  Description
     DeleteComment()  • called with a parameter of type string representing a line of
                           pseudocode from a student’s project file
                         • returns the line after removing any comments
                         Note on comments:
                         A comment starts with two forward slash characters and includes all the
                         remaining characters on the line.
                         The following example shows a string before and after the comment has
                         been removed:
                         Before: IF X2 > 13 THEN    //check if limit exceeded
                         After:  IF X2 > 13 THEN
A second module is defined:
             Module                                Description
         Stage_1()      • called with a parameter of type string representing a student name
                          • creates a new stage 1 file
                          • copies each line from the student’s project file to the stage 1 file after
                           removing any comment from each line
                          • does not write blank lines to the stage 1 file
                          • returns the number of lines written to the stage 1 file
        Write pseudocode for module Stage_1().
        Module DeleteComment() must be used in your solution.
```

## Python 接口

入口：`Stage_1(StudentName)`。使用给定 DeleteComment：仅删除从 // 起的内容，保留前面的空格。没有额外删首空格的要求；这里 blank 指处理后空串，纯空格行是否 blank 未定义，不用它作额外判分边界。生成 <StudentName>_S1.txt 并覆盖旧内容，每条写入行含 LF；返回写入行数，不 print。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `MichaelAday_src.txt`：51 字节；最后一行无换行。


## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Generate filenames condone missing “_”
- [ ] MP2：Open both files in correct modes and subsequently close
- [ ] MP3：Loop to EOF(OldFile)
- [ ] MP4：Read a line from OldFile and execute DeleteComment()in a loop
- [ ] MP5：Skip blank lines after DeleteComment()in a loop
- [ ] MP6：Write Line to stage 1 file and increment Count
- [ ] MP7：Return the number of lines after a reasonable attempt at counting
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
