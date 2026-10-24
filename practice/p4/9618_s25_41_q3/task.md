# 9618_s25_41 第 3 题 · Node / Tree：对象引用与递归中序遍历

标识符及文件名照 QP；数组建成真实 list，并用英文注释注明类型与大小（D10）。从空文件完成，主程序放在 `if __name__ == "__main__":` 下，提示写在 `input("…")` 中。按 `make try EX=practice/p4/9618_s25_41_q3 K=3b` 可分问测试。QP 要求私有属性时使用 `self.__Name`；未要求时可按 MS 使用公有属性；测试允许正确的循环实现，不靠指定变量名或固定提示语判分。
来源：QP pp.6–9；MS pp.30–43。已看 QP 全题原页、MS Python 范例原页；证据格与官方 evidence.doc 逐格核对。

## 英文原题（对照 QP 原页转写）

```text
6

3   A program stores data in a binary tree that is designed using Object‑Oriented Programming
    (OOP).

    The tree stores data in ascending numerical order, for example:




                           20                                         45


                 1                   21                      33                  63

    The class Node stores data about the nodes.

                                               Node
 NodeData : Integer                       stores the node’s integer data

 LeftNode : Node                          stores the node that is stored to the left of the current
                                          node, or a null value if there is no node to the left

 RightNode : Node                         stores the node that is stored to the right of the current
                                          node, or a null value if there is no node to the right
 Constructor()                            initialises NodeData to its parameter value; initialises
                                          LeftNode and RightNode to a null value

 GetLeft()                                returns LeftNode

 GetRight()                               returns RightNode

 GetData()                                returns NodeData

 SetLeft()                                takes an object of type Node as a parameter and stores
                                          it in LeftNode

 SetRight()                               takes an object of type Node as a parameter and stores
                                          it in RightNode






    (a) (i)     Write program code to declare the class Node and its constructor.

                Do not declare the other methods.

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program as Question3_J25.

 Copy and paste the program code into part 3(a)(i) in the evidence document.
                                                                                                      [4]

         (ii)   Write program code for the three get methods.

 Save your program.

 Copy and paste the program code into part 3(a)(ii) in the evidence document.
                                                                                                      [3]

        (iii)   The method SetLeft() takes an object of type Node as a parameter. The method
                stores the parameter in the attribute LeftNode

                The method SetRight() takes an object of type Node as a parameter. The method
                stores the parameter in the attribute RightNode

                Write program code for SetLeft() and SetRight()

 Save your program.

 Copy and paste the program code into part 3(a)(iii) in the evidence document.
                                                                                                      [3]

    (b) Write the main program to declare five objects of type Node :

         •      Node 1 with the data 10
         •      Node 2 with the data 20
         •      Node 3 with the data 5
         •      Node 4 with the data 15
         •      Node 5 with the data 7

 Save your program.

 Copy and paste the program code into part 3(b) in the evidence document.
                                                                                                      [2]






    (c) The class Tree stores the tree.

                                                   Tree
 FirstNode : Node                             stores the root node in the tree
 Constructor()                                initialises FirstNode to its parameter value

 GetRootNode()                                returns the node stored in FirstNode

 Insert()                                     stores its parameter node in the correct position in the
                                              tree


          (i)   Write program code to declare the class Tree and its constructor.

                Do not declare the other methods.

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 3(c)(i) in the evidence document.
                                                                                                         [2]

         (ii)   Write program code for GetRootNode()

 Save your program.

 Copy and paste the program code into part 3(c)(ii) in the evidence document.
                                                                                                         [1]

        (iii)   The method Insert() takes a node as a parameter and then searches the tree to find
                the position to insert the new node by:

                •   checking whether the node’s data is less than or greater than the root node’s data
                •   moving to the left node if the data is less than the root node’s data
                •   moving to the right node if the data is greater than or equal to the root node’s data
                •   repeating until the final position of the node is found and stores the node in that
                    position.

                Write program code for Insert()

 Save your program.

 Copy and paste the program code into part 3(c)(iii) in the evidence document.
                                                                                                         [6]






    (d) The recursive procedure OutputInOrder() outputs the data stored in the binary tree in
        ascending numerical order.

         The procedure takes a Node object as a parameter and then:

         •      checks if the left node is null. If there is a left node, the function calls itself with the left
                node
         •      outputs the data of the current node
         •      checks if the right node is null. If there is a right node, the function calls itself with the
                right node.

         Write program code for OutputInOrder()

 Save your program.

 Copy and paste the program code into part 3(d) in the evidence document.
                                                                                                              [5]

    (e) (i)     Write program code to extend the main program to:

                •    create a new object of type Tree with the node containing the data 10 as the first
                     node
                •    insert the nodes with the values 20, 5, 15 and 7 into the tree in the order given
                •    call OutputInOrder() with the tree’s root node as a parameter.

 Save your program.

 Copy and paste the program code into part 3(e)(i) in the evidence document.
                                                                                                              [3]

         (ii)   Test your program.

                Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot into part 3(e)(ii) in the evidence document.
                                                                                                              [1]
```

## Python 接口与 QP / MS 差异

接口照 QP 的 Node / Tree、get/set、Insert、全局递归过程 `OutputInOrder(RootNode)`；null 用 None，不用整数下标。构造 Tree 时已有根对象，不额外规定空树构造。QP 明确相等值走右，所以包含重复值插入测试。Insert 可迭代或递归；OutputInOrder 必须递归，测试包装全局过程统计非空结点调用次数。MS p.31 的属性及 __init__ 下划线在抽文本中丢失，已看原页后照正确 Python 写法转写；没有据抽取乱码认定官方笔误。无数据文件。

## 证据文档对照表

| 证据格 | 行 id | 分 | 内容 | 自动测（测试名 · 语料得分点） | 人工核对 |
|:--|:--|--:|:--|:--|:--|
| Part 3(a)(i) | 9618_s25_41:3(a)(i) | 4 | 代码 | `test_3a_i_ii_iii_node_references` · MP4 | MP1, MP2, MP3 |
| Part 3(a)(ii) | 9618_s25_41:3(a)(ii) | 3 | 代码 | `test_3a_i_ii_iii_node_references` · MP2, MP3 | MP1 |
| Part 3(a)(iii) | 9618_s25_41:3(a)(iii) | 3 | 代码 | `test_3a_i_ii_iii_node_references` · MP2, MP3 | MP1 |
| Part 3(b) | 9618_s25_41:3(b) | 2 | 代码 | `test_3b_and_3e_i_main_objects` · MP1, MP2 | — |
| Part 3(c)(i) | 9618_s25_41:3(c)(i) | 2 | 代码 | `test_3c_i_ii_root_is_original_node` · MP2 | MP1 |
| Part 3(c)(ii) | 9618_s25_41:3(c)(ii) | 1 | 代码 | `test_3c_i_ii_root_is_original_node` · 整行 | — |
| Part 3(c)(iii) | 9618_s25_41:3(c)(iii) | 6 | 代码 | `test_3c_iii_insert_identity_and_duplicate_right` · MP2, MP3, MP4, MP5, MP6 | MP1 |
| Part 3(d) | 9618_s25_41:3(d) | 5 | 代码 | `test_3d_recursive_inorder` · MP1, MP2, MP3, MP4, MP5 | — |
| Part 3(e)(i) | 9618_s25_41:3(e)(i) | 3 | 代码 | `test_3ei_main_call_chain` / `test_3b_and_3e_i_main_objects` / `test_3e_ii_screenshot` · MP1, MP2, MP3 | — |
| Part 3(e)(ii) | 9618_s25_41:3(e)(ii) | 1 | 截图 | `test_3e_ii_screenshot` · 整行 | — |

自动覆盖表示行为得到验证；混合点里的函数头、注释、调用结构仍须补核，不能凭测试自动授予考试分数。可选得分点多于该行满分时，按 markpoints[].marks 加权后按该行满分比例折算。

## 人工核对清单

- [ ] 3(a)(i) MP1：Class header (and end where appropriate)
- [ ] 3(a)(i) MP2：Constructor header (and end where appropriate) with (min) one parameter (integer) within class
- [ ] 3(a)(i) MP3：3 attributes with correct data types
- [ ] 3(a)(ii) MP1：1 get method with no parameter …
- [ ] 3(a)(iii) MP1：1 set method taking parameter of type Node …
- [ ] 3(c)(i) MP1：Class Tree header (and end) no inheritance and constructor header (and end) taking 1 node parameter within class …
- [ ] 3(c)(iii) MP1：Insert method header (and end) taking 1 node parameter
- [ ] 所有方法头、主程序的调用顺序、返回值接收与题给标识符符合该题 MS；属性注释写明类型，QP 要求私有的属性不改成公有属性。
- [ ] 题目指定算法自行实现，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳（D10 ③；本项人工核对）。
- [ ] 截图清晰，输入、输出及要求的文件名可见；appropriate message 的语义与状态一致（措辞不限）。

## 得分点编号（D37 ②）

编号采用语料 markpoints[].n；1 分且未拆分的行记“整行”。本题 MS 圆点顺序与语料一致；若 MS 给可选点上限，按该行上限计分。

## QP p.6 示例二叉树图的文字对照

| 结点 | 左孩子 | 右孩子 |
|:--|:--|:--|
| 30（根） | 20 | 45 |
| 20 | 1 | 21 |
| 45 | 33 | 63 |
| 1、21、33、63 | 无 | 无 |
