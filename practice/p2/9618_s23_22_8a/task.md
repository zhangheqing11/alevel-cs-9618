# 验证库存信息行

来源：9618_s23_22:8(a)；QP p17，MS p11，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A computer shop assembles computers using items bought from several suppliers. A text file
    Stock.txt contains information about each item.
    Information for each item is stored as a single line in the Stock.txt file in the format:
        <ItemNum><SupplierCode><Description>
    Valid item information is as follows:
                                  Format                         Comment
                                                    unique number for each item in the range
     ItemNum            4 numeric characters
                                                    ″0001″ to ″5999″ inclusive
     SupplierCode      3 alphabetic characters     to identify the supplier of the item
     Description       a string                   a minimum of 12 characters
    The file is organised in ascending order of ItemNum and does not contain all possible values in
    the range.
    A programmer has started to define program modules as follows:
           Module                                  Description
     OnlyAlpha()       •   called with a parameter of type string
     (already written)
                          •   returns TRUE if the string contains only alphabetic characters,
                              otherwise returns FALSE
     CheckInfo()       •   called with a parameter of type string representing a line of item
                              information
                          •   checks to see whether the item information in the string is valid
                          •   returns TRUE if the item information is valid, otherwise returns
                              FALSE
Write pseudocode for module CheckInfo().
        Module OnlyAlpha() should be used as part of your solution.
```

## Python 接口

入口：`CheckInfo(NewLine)`。只验证本题规定的行格式，不增加题目没有要求的库存去重检查。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Test length of parameter
- [ ] MP2：Extract first 4 characters of parameter (as ItemNum)
- [ ] MP3：Test first four characters are all numeric
- [ ] MP4：Test ItemNum in range "0001" to "5999"
- [ ] MP5：Extract characters 5 to 7 of parameter (as SupplierCode)
- [ ] MP6：Use of OnlyAlpha()with extracted SupplierCode
- [ ] MP7：Return BOOLEAN value correctly in all cases, must have been declared as local
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
