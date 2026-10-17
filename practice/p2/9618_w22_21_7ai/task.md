# 计算单运算符表达式

来源：9618_w22_21:7(a)(i)；QP p12，MS p8，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A simple arithmetic expression is stored as a string in the format:
        <Value1><Operator><Value2>
    An operator character is one of the following:  ' + '    ' − '    ' * '    ' / '
    Example arithmetic expression strings:
        "803+1904"
        "34/7"

A procedure Calculate() will:
        •   take an arithmetic expression string as a parameter
        •   evaluate the expression
        •   output the result.
        Assume:
        •   the string contains only numeric digits and a single operator character
        •   Value1 and Value2 represent integer values
        •   Value1 and Value2 are unsigned (they will not be preceded by ' + ' or ' − ').
Write pseudocode for the procedure Calculate().
```

## Python 接口

入口：`Calculate(Expression)`。测试使用 ASCII 运算符 + - * /，除数非零；输出计算结果，不把题目未规定的错误处理作为要求。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 7 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Declaration of local variables for Par1 Par2 and Par3
- [ ] MP2：Loop to end of (parameter) string // until operator is found
- [ ] MP3：Extract a character in a loop...
- [ ] MP4：Attempt at extraction of three parts of expression using substring functions
- [ ] MP5：Completely correct extraction of all three parts of expression
- [ ] MP6：Convert string to Integer using STR_TO_NUM(<something sensible>)
- [ ] MP7：Attempt to interpret at least two operators (Par2): + - * /
- [ ] MP8：Corresponding correct calculation (all operators) and final Output of result
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
