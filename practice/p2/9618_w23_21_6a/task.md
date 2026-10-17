# 带长度限制的行输出缓冲

来源：9618_w23_21:6(a)；QP p10，MS p7，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
The pseudocode OUTPUT command starts each output on a new line.
A new procedure MyOutput() will take a string and a Boolean parameter.
        MyOutput() may be called repeatedly and will use concatenation to build a string using a
        global variable MyString, up to a maximum length of 255 characters.
        MyString will be output in either of these two cases:
        1.  The Boolean parameter value is TRUE
        2.  The resulting string (after concatenation) would be longer than 255 characters.
        If MyString is not output, the string is concatenated with MyString.
        For example, the calls to MyOutput() given below would result in the output as shown:
            MyOutput("Hello ", FALSE)
            MyOutput("ginger ", FALSE)
            MyOutput("cat", TRUE)
            MyOutput("How are you?", TRUE)
        Resulting output:
            Hello ginger cat
            How are you?
        Notes:
        •   MyString is initialised to an empty string before MyOutput() is called for the first time.
        •   No string passed to MyOutput() will be longer than 255 characters.
        Write pseudocode for MyOutput().
```

## Python 接口

入口：`MyOutput(NewString,EOL)`。溢出分支按本题 MS：先输出旧缓冲，保存 NewString；这一分支不再处理 EOL。非溢出时追加后按 EOL 决定输出并清空。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Procedure heading, including parameters, and ending
- [ ] MP2：Produce concatenated string
- [ ] MP3：… Check whether resulting string would be too long
- [ ] MP4：If so, then output old MyString
- [ ] MP5：… and assign NewString to MyString
- [ ] MP6：Else concatenate NewString to MyString
- [ ] MP7：(test for length < 255) Test EOL – If TRUE then Output
- [ ] MP8：… and reset MyString to empty string
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
