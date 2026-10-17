# 按指针次序输出链表数据

来源：9618_w24_23:3(c)；QP p.6，MS p.7，4 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

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
An algorithm outputs the Data field from all nodes in the array List. The order the Data is
        output should be the same order it is stored in the linked list.
        Describe the algorithm in four steps.
        Do not use pseudocode statements in your answer.
```



## Python 接口

入口：`main()`。原题无模块名，Python `main()`；提供 Node(Data, Pointer) 与全局 List、HeadPointer。List 有200个真实结点另加0号占位；Python下标直接等于题给指针，0为空（沿用批2链表约定）。按链接次序每结点输出一行Data，不输出未链接元素、不重排链表；空链表无输出。不测试损坏指针或环。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Assign HeadPointer to ThisPointer / Current Pointer // Identify first node using headpointer
- [ ] MP2：Loop the following until ThisPointer value is 0 (zero) / null pointer reached
- [ ] MP3：… Output data (field) from array element at index ThisPointer // Output data (field) of the current node / array element
- [ ] MP4：… Assign pointer field from current array element / index / to ThisPointer / Current Pointer // Assign pointer field from current node to ThisPointer / Current Pointer
- [ ] 本小问总分上限 4 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
