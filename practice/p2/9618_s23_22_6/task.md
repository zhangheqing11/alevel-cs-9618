# 输出空心数字方阵

来源：9618_s23_22:6；QP p10，MS p7，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A procedure Square() will take an integer value in the range 1 to 9 as a parameter and output a
    number square.
    The boundary of a number square is made up of the character representing the parameter value.
    The inside of the number square is made up of the asterisk character (*).
          Parameter value 1 — Output:
1

Parameter value 2 — Output:
22
22

Parameter value 3 — Output:
333
3*3
333

Parameter value 4 — Output:
4444
4**4
4**4
4444

Parameter value 9 — Output:
999999999
9*******9
9*******9
9*******9
9*******9
9*******9
9*******9
9*******9
999999999

The pseudocode OUTPUT command starts each output on a new line. For example, the following
    three OUTPUT statements would result in the outputs as shown:
        OUTPUT "Hello"
        OUTPUT "ginger"
        OUTPUT "cat"
    Resulting output:
        Hello
        ginger
        cat
    Write pseudocode for procedure Square().
    Parameter validation is not required.
```

## Python 接口

输出约定：只输出题给的数字方阵，每个方阵行占一行，不加标题或说明文字。

入口：`Square(Dim)`。每行使用 print 一次；无字符间隔空格。QP 表格改用逐个参数的等宽输出块转写，保留原示例内容。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 6 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Procedure heading and ending including parameter
- [ ] MP2：Loop using parameter, containing attempt to construct first line / last line
- [ ] MP3：Construct first line / last line
- [ ] MP4：Attempt at loop to construct intermediate line
- [ ] MP5：Output first / last line of square when Dim > 2
- [ ] MP6：Output all intermediate lines in a loop
- [ ] MP7：Correct output of first two squares
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
