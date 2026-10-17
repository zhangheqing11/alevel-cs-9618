# 验证新的供应商代码

来源：9618_s23_21:8(a)；QP p15，MS p9，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A computer shop assembles computers using items bought from several suppliers. A text file
    Stock.txt contains information about each item.
    Information for each item is stored as a single line in the Stock.txt file in the format:
        <ItemNum><SupplierCode><Description>
    Item information is as follows:
                              Format                     Comment
                                              unique for each item in the range
     ItemNum          4 numeric characters
                                              "0001" to "5999" inclusive
     SupplierCode    5 alphabetic characters   to identify the supplier of the item
     Description     a string                 a minimum of 12 characters
    The file is organised in ascending order of ItemNum and does not contain all possible values in
    the range.
    A programmer has started to define program modules as follows:
         Module                                  Description
     SuppExists()  •   called with a parameter of type string representing a supplier code
     (already written)
                      •   returns TRUE if the supplier code is already in use, otherwise returns
                          FALSE
     IsNewSupp()   •   called with a parameter of type string representing a new supplier code
                      •   returns TRUE if the string only contains alphabetic characters (either
                          upper or lower case) and the supplier code is not already in use,
                          otherwise returns FALSE
Write pseudocode for module IsNewSupp().
        Module SuppExists() has already been written and should be used as part of your solution.
        Module SuppExists() will generate a run-time error if the given parameter is not
        5 characters in length.
```

## Python 接口

入口：`IsNewSupp(ThisString)`。SuppExists 是题给的已有模块；测试替换其返回值，不要求自行读 Stock.txt。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Check ThisString is exactly 5 characters in length
- [ ] MP2：Use of SuppExists() with a string of 5 characters as a parameter
- [ ] MP3：Loop for 5 iterations // loops for length of string parameter
- [ ] MP4：Extract a character in a loop
- [ ] MP5：Test if char is alphabetic in a loop
- [ ] MP6：…catering for both upper and lower case
- [ ] MP7：Return Boolean following a reasonable attempt
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
