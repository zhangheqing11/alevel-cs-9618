# 9618_w25_42 第 3 题 · 数组二叉搜索树与完整文件导出

覆盖 6 行，共 21 分。QP 原页：[10, 11, 12]；MS 原页：[27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]，已逐页渲染核对。证据格另对照官方 evidence.doc。

## 导读

从 starter.py 的空白分节开始写；标识符、文件名照题目。数组必须建出真实 list，并以英文注释注明类型与大小（D10 ①）；指针初值照题目（D10 ②）。排序、查找及 ADT 操作自己写循环，不用 `sort()`、`sorted()`、`index()`、`max()`、`min()` 或成员测试 `in` 代劳（D10 ③）。主程序置于 `if __name__ == "__main__":` 下，以便测试导入；提示语写在 `input("…")` 中。

## 英文原题（QP 原页转写）

```text
3      A program stores integers in ascending order in an ordered binary tree. The tree is implemented
       as a 2D array.

       Each node is stored with three values:

       •   a pointer to the left node
       •   the data
       •   a pointer to the right node.

       All null values are stored as –1

       The binary tree can store up to 50 nodes.

       Nodes cannot be deleted from the binary tree.

       (a) The binary tree is stored as a global array with the identifier TreeArray. The left pointer, the
           data and the right pointer of each node are initialised to –1

           The global variable RootPointer stores the index of the root node in the tree, initialised to
           –1

           The global variable FreeNode stores the index of the next free node in the array, initialised
           to 0

           Write program code to declare and initialise TreeArray, RootPointer and FreeNode

    Save your program as Question3_N25.

    Copy and paste the program code into part 3(a) in the evidence document.
                                                                                                         [3]

       (b) The procedure AddNode():

           •    takes an integer to store in the binary tree as a parameter
           •    stores the parameter in the next free node in the array
           •    finds the position to store the data in the tree by following the appropriate pointers
           •    updates the pointer of the new node’s parent node.

           The procedure outputs "The tree is full" if the parameter cannot be stored because
           the tree is full.

           Write program code for AddNode()

    Save your program.

    Copy and paste the program code into part 3(b) in the evidence document.
                                                                                                         [7]

(c) The text file TreeData.txt stores 50 integers. Each integer is on a new line in the file.

         The main program reads each integer from the file and stores each integer in the binary tree
         in the order they are read.

         Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 3(c) in the evidence document.
                                                                                                    [4]

    (d) The procedure WriteAllToFile() stores the content of TreeArray in a new text file with
        the filename Tree.txt. The file Tree.txt is not provided.

         Each node in TreeArray is stored on one line with a comma separating each value.

         For example, the current contents of TreeArray are:

               Index        0            1             2

                 0         –1           20             1

                 1         –1           30             –1

                …

                49         -1           -1             -1

         After writing TreeArray to the text file, Tree.txt will contain:

         –1,20,1
         –1,30,–1
         …
         -1,-1,-1

         Write program code for WriteAllToFile()

         Include exception handling when writing to the file.

 Save your program.

 Copy and paste the program code into part 3(d) in the evidence document.
                                                                                                    [5]

(e) (i)       Amend the main program to call WriteAllToFile()

 Save your program.

 Copy and paste the program code into part 3(e)(i) in the evidence document.
                                                                                                                                                         [1]

             (ii)    Test your program.

                     Take a screenshot that shows all of the content stored in the file Tree.txt

                     In this screenshot you need to make sure the filename is visible.

 Save your program.

 Copy and paste the screenshot(s) into part 3(e)(ii) in the evidence document.
                                                                                                                                                         [1]
```

## Python 接口与测试约定

- `TreeArray` 为 50×3 全局 list，列按 QP 的 左指针/数据/右指针；所有格 -1，`RootPointer=-1`，`FreeNode=0`。`AddNode(NodeData)`、`WriteAllToFile()` 按 QP 名字。
- 文件读取属于主程序，不要求额外 ReadData 函数；测试记录 AddNode 调用，检查 50 个整数原顺序。
- Tree.txt 为程序新建，不放进 files；截图测试读取脚本生成的文件，与 MS p.38 图中 50 行逐行比对。文件名可见仍人工核对。
- QP 未规定重复值应走左还是右；附加边界测试用互异值，不自行指定重复值策略。输出文件只测首次新建，不限定再次运行的覆盖或追加行为。

## 证据文档对照表

表内 MP 号取语料 markpoints[].n。每行列出自动与人工主归属；类型注释、函数头和截图可读性仍须人工核对。自动占比只统计可观察行为，并非自动给出考试分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_w25_42:3(a) | 3 | 代码 | `test_3a_globals_and_nulls` · MP1、MP2、MP3 | — |
| Part 3(b) | 9618_w25_42:3(b) | 7 | 代码 | `test_3b_insert_left_right_and_deep`；`test_3b_last_node_and_full` · MP1、MP2、MP3、MP4、MP5、MP6、MP7、MP8、MP9 | — |
| Part 3(c) | 9618_w25_42:3(c) | 4 | 代码 | `test_3c_file_inputs_call_addnode_in_order`；`test_3c_missing_input_file` · MP2、MP3、MP4、MP5 | MP1 Opening the file to read and closing the file in an appropriate place |
| Part 3(d) | 9618_w25_42:3(d) | 5 | 代码 | `test_3d_write_all_nodes_and_format`；`test_3d_write_error_handled` · MP1、MP3、MP4、MP5 | MP2 Opening the file (Tree.txt) to write and closing the file in appropriate place |
| Part 3(e)(i) | 9618_w25_42:3(e)(i) | 1 | 代码 | `test_3e_ii_screenshot_file_content` · MPwhole | — |
| Part 3(e)(ii) | 9618_w25_42:3(e)(ii) | 1 | 截图 | `test_3e_ii_screenshot_file_content` · MPwhole | — |

## 人工核对清单

- [ ] 3(c) MP1：Opening the file to read and closing the file in an appropriate place
- [ ] 3(d) MP2：Opening the file (Tree.txt) to write and closing the file in appropriate place
- [ ] 数组、指针与记录字段的英文类型注释及作用域正确，数组大小与 QP 一致。
- [ ] 按 QP 写指定算法；没有以内置容器操作代替数组 ADT 或查找、排序步骤。
- [ ] 所有截图清晰；输入、输出和要求的文件名可见；截图不能仅由 pytest 成功代替。
- [ ] 3(b) MP1 的过程头、3(d) MP1 的过程头及异常消息含义人工核对；行为部分自动。
- [ ] 3(c) MP1、3(d) MP2：文件打开/关闭的位置；3(e)(ii)：截图包含文件名和全部 50 行。

## QP / MS 差异与点号对照

- Python AddNode 范例与 QP 一致，参考解保留其插入逻辑。
- MS pp.35–36 Java/Python 写文件用追加模式，QP 只要求 new text file 且首次未提供；参考解用 w 创建文件，测试只检查首次写入，不裁决 QP 未要求的重复导出策略。
- 3(d) 异常测试让 Tree.txt 路径成为目录，真实触发打开错误，不要求某种 try/except 写法。

3(b) 有 9 个候选点，最多 7 分；3(c) 有 5 个候选点，最多 4 分，按点分值比例折算。语料编号按 MS 圆点顺序，不能把候选点数当成本题分值。
