# 检查库存中是否已有货号

来源：9618_s23_21:8(b)；QP p16，MS p10，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

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
A new module has been defined:
               Module                                Description
         CheckNewItem()    •   called with a parameter of type string representing a line of
                                  item information
                              •   checks to see whether an item with the same ItemNum already
                                  exists in the file
                              •   returns TRUE if the ItemNum is not already in the file, otherwise
                                  returns FALSE
        Write efficient pseudocode for module CheckNewItem().
```

## Python 接口

入口：`CheckNewItem(NewLine)`。参数保证符合 QP 格式；Stock.txt 升序、货号唯一。只返回 bool，不输出、不改文件。QP 没有限定文件至少几行，故包括空文件与单行。按升序可以在读到大于目标的货号时停止。MS MP5 原文中的 < 是范例继续循环的比较方向；行为测试按 QP 升序查找，不把范例文字误作提前失败条件。禁止内置查找替代。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `Stock.txt`：77 字节；最后一行无换行。


## 人工核对清单

本题 MS 总分上限 7 分，候选得分点不能简单相加超过此上限。

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Open Stock.txt in READ mode and subsequently close
- [ ] MP2：Extract NewItemNum from parameter
- [ ] MP3：Conditional loop until EOF("Stock.txt")
- [ ] MP4：... OR NewItemNum found
- [ ] MP5：... OR when ThisItemNum < NewItemNum
- [ ] MP6：Read a line from Stock.txt AND extract ThisItemNum in a loop
- [ ] MP7：If ThisItemNum = NewItemNum then terminate loop / set flag in a loop
- [ ] MP8：Return Boolean after reasonable attempt
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
