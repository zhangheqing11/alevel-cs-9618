# 9618_w24_41 第 3 题 · 数组链表的头插与删除、空闲链回收

覆盖 8 行，共 19 分。QP 原页：[12, 13, 14, 15]；MS 原页：[26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]，已逐页渲染核对。证据格另对照官方 evidence.doc。

## 导读

从 starter.py 的空白分节开始写；标识符、文件名照题目。数组必须建出真实 list，并以英文注释注明类型与大小（D10 ①）；指针初值照题目（D10 ②）。排序、查找及 ADT 操作自己写循环，不用 `sort()`、`sorted()`、`index()`、`max()`、`min()` 或成员测试 `in` 代劳（D10 ③）。主程序置于 `if __name__ == "__main__":` 下，以便测试导入；提示语写在 `input("…")` 中。

## 英文原题（QP 原页转写）

```text
3      A linked list stores positive integer data in a 2D array. The first dimension of the array stores the
       integer data. The second dimension of the array stores the pointer to the next node in the linked
       list.

       A linked list node with no data is initialised with the integer –1. These nodes are linked together as
       an empty list. A pointer of –1 identifies that node as the last node.

       The linked list can store 20 nodes.

       The global 2D array LinkedList stores the linked list.

       LinkedList is initialised as an empty list. The data in each node is initialised to –1. Each node’s
       pointer stores the index of the next node. The last node stores the pointer value –1, which indicates
       it is the last node.

       The global variable FirstEmpty stores the index of the first element in the empty list. This is the
       first node in the empty linked list when it is initialised, which is index 0.

       The global variable FirstNode stores the index of the first element in the linked list. There is no
       data in the linked list when it is initialised, so FirstNode is initialised to –1.

       This diagram shows the content of the initialised array.

       FirstEmpty = 0

       FirstNode = –1

           Index           Data         Pointer

               0            -1               1

               1            -1               2

               2            -1               3

               3            -1               4

               4            -1               5



             19             -1               -1

       (a) Write program code for the main program to declare and initialise LinkedList, FirstNode
           and FirstEmpty.

    Save your program as Question3_N24.

    Copy and paste the program code into part 3(a) in the evidence document.
                                                                                                          [2]






    (b) The procedure InsertData() takes five positive integers as input from the user and inserts
        these into the linked list.

         Each data item is inserted at the front of the linked list.

         The table shows the steps to follow depending on the state of the linked list:

               Linked list state                                       Steps
                                      insert the data in the index pointed to by FirstEmpty

                    not full          change the pointer to the index pointed to by FirstNode

                                      change the values of FirstNode and FirstEmpty
                      full            end the procedure

         Any node that is at the end of the linked list has a pointer of –1.

         Write program code for InsertData().

 Save your program.

 Copy and paste the program code into part 3(b) in the evidence document.
                                                                                                 [6]






    (c) The procedure OutputLinkedList() outputs the data in the linked list in order by following
        the pointers from FirstNode.

          (i)   Write program code for OutputLinkedList().

 Save your program.

 Copy and paste the program code into part 3(c)(i) in the evidence document.
                                                                                               [2]

         (ii)   Amend the main program to call InsertData() and then OutputLinkedList().

 Save your program.

 Copy and paste the program code into part 3(c)(ii) in the evidence document.
                                                                                               [1]

        (iii)   Test your program with the test data:

                5       1       2       3       8

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 3(c)(iii) in the evidence document.
                                                                                               [1]






    (d) The procedure RemoveData() removes a node from the linked list.

         The procedure takes the data item to be removed from the linked list as a parameter.

         The procedure checks each node in the linked list, starting with the node FirstNode, until it
         finds the node to be removed. This node is added to the empty list, and pointers are changed
         as appropriate. The procedure only removes the first occurrence of the parameter.

         Assume that the data item being removed is in the linked list.

          (i)   Write program code for RemoveData().

 Save your program.

 Copy and paste the program code into part 3(d)(i) in the evidence document.
                                                                                                   [5]

         (ii)   Amend the main program to:

                •   call RemoveData() with the parameter 5
                •   output the word "After"
                •   call OutputLinkedList().

 Save your program.

 Copy and paste the program code into part 3(d)(ii) in the evidence document.
                                                                                                   [1]
        (iii)   Test your program with both sets of given test data:

                Test data set 1:   5   6   8 9     5

                Test data set 2: 10    7   8 5     6

                Take a screenshot of each output.

 Save your program.

 Copy and paste the screenshot(s) into part 3(d)(iii) in the evidence document.
                                                                                                   [1]
```

## Python 接口与测试约定

- 全局 `LinkedList` 为 20×2 整数 list，列 0 是数据，列 1 是下一指针；`FirstNode=-1`，`FirstEmpty=0`。`InsertData()`、`OutputLinkedList()`、`RemoveData(ItemToRemove)` 使用题给名字。
- InsertData 每次最多插入五个正整数，满时结束；测试不添加 QP 未要求的正整数输入校验。
- 删除参数保证存在（QP 明示），不测找不到的情况。回收结点可接在空闲链头或尾；测试按链遍历核对两条链恰好覆盖 20 格，不强迫某一种合法的回收顺序。是否把回收结点数据清成 -1 不作限制（MS 头删除范例不清数据）。
- 输出数据的换行/空格不限；主程序 After 前后应是链顺序，提示语不应自行输出额外数字。无数据文件。

## 证据文档对照表

表内 MP 号取语料 markpoints[].n。每行列出自动与人工主归属；类型注释、函数头和截图可读性仍须人工核对。自动占比只统计可观察行为，并非自动给出考试分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_w24_41:3(a) | 2 | 代码 | `test_3a_initial_free_list` · MP1、MP2 | — |
| Part 3(b) | 9618_w24_41:3(b) | 6 | 代码 | `test_3b_insert_five_at_front`；`test_3b_full_and_recycled_nodes` · MP1、MP2、MP3、MP4、MP5、MP6、MP7 | — |
| Part 3(c)(i) | 9618_w24_41:3(c)(i) | 2 | 代码 | `test_3c_i_output_follows_nonsequential_pointers` · MP1、MP2 | — |
| Part 3(c)(ii) | 9618_w24_41:3(c)(ii) | 1 | 代码 | `test_3c_iii_screenshot_reverse` · MPwhole | — |
| Part 3(c)(iii) | 9618_w24_41:3(c)(iii) | 1 | 截图 | `test_3c_iii_screenshot_reverse` · MPwhole | — |
| Part 3(d)(i) | 9618_w24_41:3(d)(i) | 5 | 代码 | `test_3d_i_remove_head_middle_tail`；`test_3d_i_duplicate_only_first_removed`；`test_3b_full_and_recycled_nodes` · MP2、MP3、MP4、MP5、MP6、MP7、MP8 | MP1 Procedure header (and end) with parameter |
| Part 3(d)(ii) | 9618_w24_41:3(d)(ii) | 1 | 代码 | `test_3d_iii_screenshot_after` · MPwhole | — |
| Part 3(d)(iii) | 9618_w24_41:3(d)(iii) | 1 | 截图 | `test_3d_iii_screenshot_after` · MPwhole | — |

## 人工核对清单

- [ ] 3(d)(i) MP1：Procedure header (and end) with parameter
- [ ] 数组、指针与记录字段的英文类型注释及作用域正确，数组大小与 QP 一致。
- [ ] 按 QP 写指定算法；没有以内置容器操作代替数组 ADT 或查找、排序步骤。
- [ ] 所有截图清晰；输入、输出和要求的文件名可见；截图不能仅由 pytest 成功代替。
- [ ] 3(b) MP1 同时包含过程头和五次输入；行为自动检查，过程头人工复核。3(c)(i) MP1 同理。

## QP / MS 差异与点号对照

- MS p.27 Python 初始化仅 append 19 行，随后访问 LinkedList[19] 越界；参考解依 QP p.12 创建全部 20 行，最后指针 -1。
- MS p.36 Python 主程序同样缺最后一行；VB/Java 在该处把最后指针留成 20；参考解沿用正确的 20 节点初始化。
- MS p.31 OutputLinkedList 在空表时会访问下标 -1；参考解在遍历前检查终止值。不额外要求 QP 未涉及的空表截图。
- 同季 9618_w24_43 第 3 题与本题相同，不另建练习。

3(b) 有 7 个候选点，最多 6 分；3(d)(i) 有 8 个候选点，最多 5 分；按候选点权重比例折算。MS 圆点未印数字，语料 MP 顺序与圆点一致。
