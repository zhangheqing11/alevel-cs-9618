# 识别伪代码模块头

来源：9618_s24_23:8(a)；QP p19，MS p12，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

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
Write pseudocode for module Header().
```

## Python 接口

入口：`Header(Line)`。ModInfo 仅为原题上下文，本小问不访问；骨架用 11 行容纳题给示例，完整数组容量未在本小问规定。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading, parameter, return type and ending
- [ ] MP2：Check that the line is at least 13 characters long before attempting to extract and return empty string
- [ ] MP3：Attempt at: Extract characters, 9 or 10 characters, corresponding to keyword plus space and compare with appropriate keyword plus space
- [ ] MP4：Completely correct MP3
- [ ] MP5：Use of type case conversion to allow for 'any case'
- [ ] MP6：Calculation of 'rest of line' and concatenation with 'P or 'F'
- [ ] MP7：Return string
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
