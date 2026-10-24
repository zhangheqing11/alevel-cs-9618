# 9618_s24_42 第 2 题 · Node / TreeClass：对象数组二叉树

标识符及文件名照 QP；数组建成真实 list，并用英文注释注明类型与大小（D10）。从空文件完成，主程序放在 `if __name__ == "__main__":` 下，提示写在 `input("…")` 中。按 `make try EX=practice/p4/9618_s24_42_q2 K=2b` 可分问测试。QP 要求私有属性时使用 `self.__Name`；未要求时可按 MS 使用公有属性；测试允许正确的循环实现，不靠指定变量名或固定提示语判分。
来源：QP pp.6–9；MS pp.15–27。已看 QP 全题原页、MS Python 范例原页；证据格与官方 evidence.doc 逐格核对。

## 英文原题（对照 QP 原页转写）

```text
6

2   A binary tree stores data in ascending order. For example:



                                       8                                19

                               3               10
    A computer program stores integers in a binary tree in ascending order. The program uses
    Object‑Oriented Programming (OOP).

    The binary tree is stored as a 1D array of nodes. Each node contains a left pointer, a data value
    and a right pointer.

    The class Node stores the data about a node.

                                                     Node
      LeftPointer : INTEGER                stores the index of the node to the left in the binary tree

      Data : INTEGER                       stores the node’s data

      RightPointer : INTEGER               stores the index of the node to the right in the binary tree
      Constructor()                        initialises Data to its parameter value
                                           initialises LeftPointer and RightPointer to −1

      GetLeft()                            returns the left pointer

      GetRight()                           returns the right pointer

      GetData()                            returns the data value

      SetLeft()                            assigns the parameter to the left pointer

      SetRight()                           assigns the parameter to the right pointer

      SetData()                            assigns the parameter to the data

    (a) (i)    Write program code to declare the class Node and its constructor.

               Do not declare the other methods.

               Use the appropriate constructor for your programming language.

               If you are writing in Python, include attribute declarations using comments.

 Save your program as Question2_J24.

 Copy and paste the program code into part 2(a)(i) in the evidence document.
                                                                                                          [4]


         (ii)   The get methods GetLeft(), GetRight()and GetData()each return the relevant
                attribute.

                Write program code for the three get methods.

 Save your program.

 Copy and paste the program code into part 2(a)(ii) in the evidence document.
                                                                                                        [3]

        (iii)   The set methods SetLeft(), SetRight()and SetData()each take a parameter and
                then store this in the relevant attribute.

                Write program code for the three set methods.

 Save your program.

 Copy and paste the program code into part 2(a)(iii) in the evidence document.
                                                                                                        [3]

    (b) The class TreeClass stores the data about the binary tree.

                                                     TreeClass
           Tree[0:19] : Node                 an array of 20 elements of type Node

           FirstNode : INTEGER               stores the index of the first node in the tree

           NumberNodes : INTEGER             stores the quantity of nodes in the tree
           Constructor()                     initialises FirstNode to −1 and NumberNodes to 0
                                             initialises each element in Tree to a Node object with the
                                             data value of −1

           InsertNode()                      takes a Node object as a parameter, inserts it in the array
                                             and updates the pointer for its parent node

           OutputTree()                      outputs the left pointer, data and right pointer of each
                                             node in Tree


         Nodes cannot be deleted from this tree.

          (i)   Write program code to declare the class TreeClass and its constructor.

                Do not declare the other methods.

                Use the appropriate constructor for your programming language.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 2(b)(i) in the evidence document.
                                                                                                        [4]


         (ii)   The method InsertNode()takes a Node object, NewNode, as a parameter and inserts
                it into the array Tree.

                InsertNode()first checks if the tree is empty.

                If the tree is empty, InsertNode():

                •   stores NewNode in the array Tree at index NumberNodes
                •   increments NumberNodes
                •   stores 0 in FirstNode.

                If the tree is not empty, InsertNode():

                •   stores NewNode in the array Tree at index NumberNodes
                •   accesses the data in the array Tree at index FirstNode and compares it to the
                    data in NewNode
                •   repeatedly follows the pointers until the correct position for NewNode is found
                •   once the position is found, InsertNode()sets the left or right pointer of its parent
                    node
                •   increments NumberNodes.

                Write program code for InsertNode().

 Save your program.

 Copy and paste the program code into part 2(b)(ii) in the evidence document.
                                                                                                     [6]

        (iii)   The method OutputTree()outputs the left pointer, the data and the right pointer for
                each node that has been inserted into the tree. The outputs are in the order they are
                saved in the array.

                If there are no nodes in the array, the procedure outputs ‘No nodes’.

                Write program code for OutputTree().

 Save your program.

 Copy and paste the program code into part 2(b)(iii) in the evidence document.
                                                                                                     [4]






    (c) (i)     The main program declares an instance of TreeClass with the identifier TheTree.

                Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 2(c)(i) in the evidence document.
                                                                                                       [1]

         (ii)   The main program inserts the following integers into the binary tree in the order given:

                    10

                    11

                    5

                    1

                    20

                    7

                    15

                The main program then calls the method OutputTree().

                Write program code to amend the main program.

 Save your program.

 Copy and paste the program code into part 2(c)(ii) in the evidence document.
                                                                                                       [4]

        (iii)   Test your program.

                Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot into part 2(c)(iii) in the evidence document.
                                                                                                       [1]
```

## Python 接口与 QP / MS 差异

接口照 QP 的 `Node(Data)`、`TreeClass()` 及 get/set/InsertNode/OutputTree 名称。MS 2(a)(i) 得分点称属性 public，但 Python 范例为私有；测试接受公有或私有，只按 getter/setter 行为与题给指针约定核对。MS p.23 原页的 NumberNodes 增量实际在左右分支之外（抽文本会丢缩进），参考解保持。该算法对重复值 / 满树行为 QP 未定义，测试只插入不同整数且不超过 20 个，不额外规定溢出返回值。2(b)(ii) 7 个可选点最多 6 分。无数据文件，不复制本卷其他题的文件。

## 证据文档对照表

| 证据格 | 行 id | 分 | 内容 | 自动测（测试名 · 语料得分点） | 人工核对 |
|:--|:--|--:|:--|:--|:--|
| Part 2(a)(i) | 9618_s24_42:2(a)(i) | 4 | 代码 | `test_2a_node_getters_setters` · MP4 | MP1, MP2, MP3 |
| Part 2(a)(ii) | 9618_s24_42:2(a)(ii) | 3 | 代码 | `test_2a_node_getters_setters` · MP2, MP3 | MP1 |
| Part 2(a)(iii) | 9618_s24_42:2(a)(iii) | 3 | 代码 | `test_2a_node_getters_setters` · MP2, MP3 | MP1 |
| Part 2(b)(i) | 9618_s24_42:2(b)(i) | 4 | 代码 | `test_2b_i_constructor_twenty_independent_nodes` · MP2, MP3, MP4 | MP1 |
| Part 2(b)(ii) | 9618_s24_42:2(b)(ii) | 6 | 代码 | `test_2b_ii_insert_left_right_and_count` / `test_2b_ii_deep_tree_twenty_nodes` · MP2, MP3, MP4, MP5, MP6, MP7 | MP1 |
| Part 2(b)(iii) | 9618_s24_42:2(b)(iii) | 4 | 代码 | `test_2b_iii_empty_and_populated_output` · MP1, MP2, MP3, MP4 | — |
| Part 2(c)(i) | 9618_s24_42:2(c)(i) | 1 | 代码 | `test_2c_i_main_identifier` · 整行 | — |
| Part 2(c)(ii) | 9618_s24_42:2(c)(ii) | 4 | 代码 | `test_2c_iii_screenshot` · MP1, MP2, MP3, MP4 | — |
| Part 2(c)(iii) | 9618_s24_42:2(c)(iii) | 1 | 截图 | `test_2c_iii_screenshot` · 整行 | — |

自动覆盖表示行为得到验证；混合点里的函数头、注释、调用结构仍须补核，不能凭测试自动授予考试分数。可选得分点多于该行满分时，按 markpoints[].marks 加权后按该行满分比例折算。

## 人工核对清单

- [ ] 2(a)(i) MP1：Class Node declaration (and end where appropriate)
- [ ] 2(a)(i) MP2：LeftPointer, Data and RightPointer declared as (public) integer
- [ ] 2(a)(i) MP3：Constructor header (and end) taking one parameter within class …
- [ ] 2(a)(ii) MP1：1 get method with no parameter …
- [ ] 2(a)(iii) MP1：1 set method header (and end) with parameter …
- [ ] 2(b)(i) MP1：Class TreeClass header (and end)
- [ ] 2(b)(ii) MP1：Method header and end, taking a Node as parameter
- [ ] 所有方法头、主程序的调用顺序、返回值接收与题给标识符符合该题 MS；属性注释写明类型，QP 要求私有的属性不改成公有属性。
- [ ] 题目指定算法自行实现，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳（D10 ③；本项人工核对）。
- [ ] 截图清晰，输入、输出及要求的文件名可见；appropriate message 的语义与状态一致（措辞不限）。

## 得分点编号（D37 ②）

编号采用语料 markpoints[].n；1 分且未拆分的行记“整行”。本题 MS 圆点顺序与语料一致；若 MS 给可选点上限，按该行上限计分。

## QP p.6 示例二叉树图的文字对照

| 结点 | 左孩子 | 右孩子 |
|:--|:--|:--|
| 15（根） | 8 | 19 |
| 8 | 3 | 10 |
| 19 | 无 | 无 |
| 3 | 无 | 无 |
| 10 | 无 | 无 |
