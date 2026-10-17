# 删除行首空格

来源：9618_s24_22:8(b)；QP p18，MS p11，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

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
The teacher has defined the first program module as follows:
              Module                                Description
         DeleteSpaces()  • called with a parameter of type string representing a line of
                              pseudocode from a student’s project file
                            • returns the line after removing any leading space characters
                            The following example shows a string before and after the leading
                            spaces have been removed:
                              Before: "   IF X2 > 13 THEN"
                              After:   "IF X2 > 13 THEN"
        Complete the pseudocode for module DeleteSpaces().
        FUNCTION DeleteSpaces(Line : STRING) RETURNS STRING
        ENDFUNCTION
```

## Python 接口

入口：`DeleteSpaces(Line)`。保留中间与结尾空格；全空格行的结果为空字符串，按 QP 的“移除所有行首空格”补测此边界。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Loop to length of parameter // Loop until first non-space character in Line
- [ ] MP2：Extract a character in a loop
- [ ] MP3：Identify first non-space character in a loop
- [ ] MP4：Attempt at removing leading spaces in Line
- [ ] MP5：Leading spaces removed from Line / / Create new string without leading space
- [ ] MP6：Return a string following a reasonable attempt at removing leading spaces in Line
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
