# 创建三位序号文件

来源：9618_w23_22:6(a)；QP p12，MS p9，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A procedure CreateFiles() will take two parameters:
        •   a string representing a file name
        •   an integer representing the number of files to be created.
        The procedure will create the number of text files specified.
        Each file is given a different name. Each file name is formed by concatenating the file name
        with a suffix based on the file number. The suffix is always three characters.
        For example, the call CreateFiles("TestData", 3) would result in the creation of the
        three files, TestData.001, TestData.002 and TestData.003.
        Each file will contain a single line. For example, file TestData.002 would contain the string:
            This is File TestData.002
        Write pseudocode for CreateFiles().
        Assume both parameters are valid and that the integer value is between 1 and 999, inclusive.
```

## Python 接口

入口：`CreateFiles(NameRoot,NumFiles)`。NumFiles 在 1–999，按 QP 不测 0。文件名 <NameRoot>.<三位补零序号>。WRITEFILE 对应内容 This is File <完整文件名> 加 LF，覆盖同名旧文件。不 print。只创建输出文件，故 files/ 无输入数据。所有操作在临时目录。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading, including parameters, and ending
- [ ] MP2：Loop for NumFiles iterations
- [ ] MP3：Attempt to create filename suffix using NUM_TO_STR() in a loop
- [ ] MP4：Completely correct filename
- [ ] MP5：OPENFILE in WRITE mode and subsequent CLOSE in a loop
- [ ] MP6：WRITE initial first line to the file in a loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
