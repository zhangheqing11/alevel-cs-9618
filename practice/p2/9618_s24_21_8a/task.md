# 删除双斜线注释

来源：9618_s24_21:8(a)；QP p19，MS p11，8 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

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
Complete the pseudocode for module DeleteComment().
        FUNCTION DeleteComment(Line : STRING) RETURNS STRING
        ENDFUNCTION
```

## Python 接口

入口：`DeleteComment(Line)`。不额外删除注释前的空格；原题未定义字符串字面量中的 // 特殊规则，因此所有首个 // 都视作注释开始。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Loop to length of Line (parameter) // length of Line -1
- [ ] MP2：Terminate loop on first double slash
- [ ] MP3：Attempt to extract one/two characters in a loop
- [ ] MP4：Check for "//" after attempt at extraction in a loop
- [ ] MP5：Record start position of comment // Calculate amount of trim required
- [ ] MP6：Attempt to trim Line from start of comment
- [ ] MP7：Completely correct trimmed Line from start of comment
- [ ] MP8：Return Line after a reasonable overall attempt
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
