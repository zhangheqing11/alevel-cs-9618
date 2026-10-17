# 初始化链表节点的后继指针

来源：9618_w24_23:3(b)；QP p5，MS p6，4 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
The implementation of a linked list uses an integer variable and a 1D array List of type Node.
    Record type Node is declared in pseudocode as follows:
    TYPE Node
        DECLARE Data : STRING
        DECLARE Pointer : INTEGER
    ENDTYPE
    The array List is declared in pseudocode as follows:
    DECLARE List : ARRAY[1:200] OF Node
    The linked list will operate as follows:
    •   Integer variable HeadPointer will store the array index for the first node in the linked list.
    •   The Pointer field of a node contains the index value of the next array element (the next
        node) in the linked list.
    •   The value 0 is used as a null pointer.
The array List will be initialised so that each node points to the following node.
        The last node will contain a null pointer.
        Complete the program flowchart to represent the algorithm for this operation.
            START
             END
```

## Python 接口

入口：`main()`。原题要求补流程图：先画含循环的流程图，answer.pseudo 是同算法转写辅助，Python main 是测试包装。List[0] 为占位，1–200 原样对应 QP，指针 0 是 null，不减一。本小问只初始化 Pointer，不改 Data 或 HeadPointer（QP 没要求后两者初始化）。没有给空闲表变量，不自行新增。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Use of variable as array index and initialisation to 1 / to first element of array
- [ ] MP2：Loop for 199 / 200 iterations
- [ ] MP3：Assign Index+1 to each pointer field in a loop
- [ ] MP4：Assign 0 to 200th pointer field
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
