# 按供应商输出库存报表

来源：9618_s23_23:8(b)；QP p16，MS p9，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A computer shop assembles desktop computers, using items bought from several suppliers. A text
    file Stock.txt contains information about each item.
    Information for each item is stored as a single line in the Stock.txt file in the format:
        <ItemNum><SupplierCode><Description>
    Item information is as follows:
                             Format                           Comment
                                            unique number for each item in the range “0001”
     ItemNum        4 numeric characters
                                            to “5999” inclusive
     SupplierCode  3 alphabetic characters  code to identify the supplier of the item
     Description   a string                a minimum of 12 characters
    The file is organised in ascending order of ItemNum and does not contain all possible values in
    the range.
    The programmer has defined the first program module as follows:
         Module                                  Description
     ChangeSupp()  • called with two parameters Code1 and Code2 of type string that represent
                       valid supplier codes
                      • creates a new file NewStock.txt from the contents of the
                       file Stock.txt where any reference to Code1 is replaced by Code2
                      • returns a count of the number of items that have had their supplier code
                       changed
A new module is required:
              Module                                Description
         Report_1()       • takes a parameter of type string that represents a SupplierCode
                            • searches the Stock.txt file for each line of item information that
                              contains the given SupplierCode
                            • produces a formatted report of items for the given SupplierCode,
                              for example, for supplier DRG, the output could be:
                                  Report for Supplier: DRG
                                  Item          Description
                                  1234          USB Printer Cable 3 m
                                  1273          32GB USB Flash Drive
                                  1350          Mouse Mat 320 x 240 mm
                                  Number of items listed: 3
        Write pseudocode for module Report_1().
```

## Python 接口

入口：`Report_1(Supp)`。输出 QP 示例的 Report for Supplier: <Supp>、Item / Description 两列、匹配的货号和完整描述、Number of items listed: <数量>。空行可选，列间一个或多个空白均接受；描述内部空格保留。没有匹配也输出两行标题和数量 0。文件不变并关闭。QP 例中 Cable 3m 按原页转写。MS 范例 OUTPUT 的 ThisItem 拼写不作为新变量要求，按 QP 输出货号。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `Stock.txt`：86 字节；最后一行有换行。


## 人工核对清单

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Output report header (blank lines optional) – Must contain the parameter code
- [ ] MP2：Conditional loop until EOF("Stock.txt")
- [ ] MP3：Read a line from Stock.txt AND extract SupplierCode in a loop
- [ ] MP4：Test if SupplierCode = Supp then increment count (must have been Initialised)
- [ ] MP5：Extract AND output item and description in a loop
- [ ] MP6：Output the final line with count
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
