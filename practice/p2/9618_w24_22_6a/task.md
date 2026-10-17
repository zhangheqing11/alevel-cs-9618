# 随机选择两种馅料与面包

来源：9618_w24_22:6(a)；QP p13，MS p9，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A shop sells sandwiches and snacks. The owner chooses a ‘daily special’ sandwich which is
    displayed on a board outside the shop. Each ‘daily special’ has two different fillings and is made
    with one type of bread.
    The owner wants a program to randomly choose the ‘daily special’ sandwich.
    The program designer decides to store the possible sandwich fillings in a 1D array of type string.
    The array is declared in pseudocode as follows:
        DECLARE Filling : ARRAY [1:35] OF STRING
    Each element contains the name of one filling.
    An example of the first five elements is as follows:
     Index     Element value
       1    "Cheese"
       2    "Onion"
       3    "Salmon"
       4    "Anchovies"
       5    "Peanut Butter"
    A second 1D array stores the possible bread used:
        DECLARE Bread : ARRAY [1:10] OF STRING
    Each element contains the name of one type of bread.
    An example of the first three elements is as follows:
     Index    Element value
       1    "White"
       2    "Brown"
       3    "Pitta"
    Both arrays may contain unused elements. The value of these will be an empty string and they
    may occur anywhere in each array.
    A procedure Special() will output a message giving the ‘daily special’ sandwich made from two
    randomly selected different fillings and one randomly selected bread.
    Unused array elements must not be used when creating the ‘daily special’ sandwich.
    Using the above examples, the output could be:
        "The daily special is Cheese and Onion on Brown bread."
Complete the pseudocode for the procedure Special().
        Assume that both arrays are global.
        PROCEDURE Special()
        ENDPROCEDURE
```

## Python 接口

入口：`Special()`。使用 provided RAND(Limit) 返回 0≤实数<Limit；Python 下标无需 +1（伪代码仍 INT(RAND(n))+1）。至少两种不同有效馅料、一种有效面包；不测无法终止的无可选值情况。按 QP 只 print 一行 The daily special is <馅料1> and <馅料2> on <面包> bread.。测试给 RAND 注入固定种子的随机源，只检查选项与输出性质，不强制抽取次数或次序。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Loop for Filling 1, avoiding unused elements
- [ ] MP2：Loop for Filling 2 avoiding unused elements
- [ ] MP3：Check Filling 2 is different from Filling 1 – could correctly compare either the indices or the array contents
- [ ] MP4：Loop for Bread, avoiding unused elements
- [ ] MP5：Using RAND(10) / RAND(35)
- [ ] MP6：Completely correct use of RAND() - including INT()and +1 in all cases
- [ ] MP7：Correct output - once only – following a reasonable attempt at selection of filings and bread
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
