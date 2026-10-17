# 检查并计算字符串商

来源：9618_w24_21:4(c)；QP p9，MS p8，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A program includes the following assignment statement:
    Result ← STR_TO_NUM(x) / STR_TO_NUM(y)
    When the program evaluates the expression in the statement, it performs a calculation.
    Variable Result is of type real and variables x and y are of type string.
    Two checks are required before the calculation is performed:
    1.  The two strings represent valid numeric values.
    2.  The numeric value of string y is not zero.
The module to perform the checks and calculation will be implemented as a function. The
        function will need to return both a real and a Boolean value. To achieve this a record type is
        defined in pseudocode as follows:
        TYPE Result
            DECLARE Done : BOOLEAN
            DECLARE Value : REAL
        ENDTYPE
        The function Evaluate() will:
        •   take two parameters of type string representing the two numeric values
        •   return a variable of type Result with the Done field set to FALSE if either of the following
            applies:
            ◦   at least one of the strings does not represent a valid numeric value
            ◦   the numeric value of the string representing value y is zero
        •   otherwise return a variable of type Result with the Done field set to TRUE and the
            Value field assigned the result of the formula (based on the numeric value of the two
            parameters).
        Write pseudocode for the function Evaluate().
```

## Python 接口

入口：`Evaluate(NumStr1,NumStr2)`。两个位置参数依题给 x / y 公式：第一个为分子，第二个为分母。返回有 Done、Value 字段的记录对象；Done 为 False 时不检查 Value。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 6 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading, parameters, ending
- [ ] MP2：... Correct return type of Result
- [ ] MP3：Local declaration of type Result
- [ ] MP4：Attempt at using IS_NUM() to check both parameters/strings
- [ ] MP5：Attempt at using of STR_TO_NUM() to convert both parameters/strings
- [ ] MP6：Check if the divisor, is non-zero ...
- [ ] MP7：… and if so correct calculation and assignment to Value field
- [ ] MP8：Return variable of type Result having assigned both fields
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
