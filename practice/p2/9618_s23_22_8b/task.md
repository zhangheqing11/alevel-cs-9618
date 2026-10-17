# 按货号顺序生成新库存文件

来源：9618_s23_22:8(b)；QP p18，MS p12，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

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
A new module is defined as follows:
             Module                                Description
         AddItem()     •   called with a parameter of type string representing valid information
                             for a new item that is not currently in the Stock.txt file
                         •   creates a new file NewStock.txt from the contents of the file
                             Stock.txt and adds the new item information at the appropriate
                             place in the NewStock.txt file
        As a reminder, the file Stock.txt is organised in ascending order of ItemNum and does not
        contain all possible values in the range.
        Write pseudocode for module AddItem().
```

## Python 接口

入口：`AddItem(NewLine)`。NewLine 已合法且货号不在源文件中；不测试重复或非法货号。源文件不变，覆盖创建 NewStock.txt，保持升序；每个记录用 LF 结束（包括最后一条），对应 WRITEFILE 逐行输出，不 print。空源文件也写入新记录。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `Stock.txt`：48 字节；最后一行无换行。


## 人工核对清单

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Open both files, in correct modes, and subsequently close
- [ ] MP2：Conditional loop until end of file Stock.txt
- [ ] MP3：Read a line from Stock.txt AND extract ThisItemNum in a loop
- [ ] MP4：Test ThisItemNum > NewItemNum then write NewLine to NewStock.txt
- [ ] MP5：...including mechanism to only do this once only
- [ ] MP6：Write line read from Stock to NewStock
- [ ] MP7：Deal with the case where NewLine is the new last line
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
