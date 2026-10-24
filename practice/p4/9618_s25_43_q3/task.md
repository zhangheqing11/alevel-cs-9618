# 9618_s25_43 第 3 题 · LinkedList object references and removal

标识符及文件名照 QP；数组建成真实 list，并用英文注释注明类型与大小（D10）。从空文件完成，主程序放在 `if __name__ == "__main__":` 下，提示写在 `input("…")` 中。按 `make try EX=practice/p4/9618_s25_43_q3 K=3b` 可分问测试。对象私有属性使用 `self.__Name`；测试允许正确的循环实现，不靠指定变量名或固定提示语判分。
来源：QP pp.7–10；MS pp.33–45。已看 QP 全题原页、MS Python 范例原页；证据格与官方 evidence.doc 逐格核对。

## 英文原题（对照 QP 原页转写）

```text
7

3   A program stores data in a linked list that is designed using Object‑Oriented Programming (OOP).

    The class Node stores data about the nodes.

                                                   Node
      TheData : Integer          stores the integer data

      NextNode : Node            stores the next node in the linked list

      Constructor()              initialises TheData to its parameter value, initialises NextNode
                                 to a null value

      GetData()                  returns TheData

      GetNextNode()              returns NextNode

      SetNextNode()              takes an object of type Node as a parameter and stores it in
                                 NextNode

    (a) (i)     Write program code to declare the class Node and its constructor.

                Do not declare the other methods.

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program as Question3_J25.

 Copy and paste the program code into part 3(a)(i) in the evidence document.
                                                                                                      [4]

         (ii)   Write program code for the two get methods.

 Save your program.

 Copy and paste the program code into part 3(a)(ii) in the evidence document.
                                                                                                      [3]

        (iii)   The method SetNextNode() takes an object of type Node as a parameter. The method
                stores the parameter in the attribute NextNode

                Write program code for SetNextNode()

 Save your program.

 Copy and paste the program code into part 3(a)(iii) in the evidence document.
                                                                                                      [2]





                                                      8

    (b) The class LinkedList stores the linked list.

                                               LinkedList
           HeadNode : Node         stores the first node in the linked list

           Constructor()           initialises HeadNode to a null value

           InsertNode()            creates a new node using its integer parameter. Sets this
                                   node as the new head node and updates NextNode

           RemoveNode()            finds the first node that contains its integer parameter and
                                   removes this node from the linked list

           Traverse()              concatenates and returns the integer data in each node in
                                   the linked list


          (i)   Write program code to declare the class LinkedList and its constructor.

                Do not declare the other methods.

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 3(b)(i) in the evidence document.
                                                                                                  [2]

         (ii)   The method InsertNode():

                •   takes an integer as a parameter
                •   creates a new node with the parameter as the integer data
                •   uses the new node’s method SetNextNode() to store the current HeadNode as
                    the next node
                •   replaces HeadNode with the current node.

                Write program code for InsertNode()

 Save your program.

 Copy and paste the program code into part 3(b)(ii) in the evidence document.
                                                                                                  [4]





                                                          9

        (iii)       The method Traverse() concatenates the integer data from the nodes in the linked
                    list, starting with the node stored in HeadNode. The method returns the final string with
                    each integer data separated with a space.

                    Write program code for Traverse()

 Save your program.

 Copy and paste the program code into part 3(b)(iii) in the evidence document.
                                                                                                            [3]

        (iv)        The method RemoveNode() takes an integer parameter to search for and remove from
                    the linked list.

                    The method first checks if the linked list is empty. If the linked list is empty the method
                    returns FALSE

                    If the linked list is not empty, the integer data in HeadNode is compared to the parameter.
                    If it matches the parameter, HeadNode is changed to store the next node.

                    If the parameter does not match, the nodes are followed until either:

                •       the node with matching integer data is found. This node is removed, the appropriate
                        nodes updated and TRUE returned
                       or
                •       none of the nodes contain matching integer data to the parameter. No nodes are
                        removed and FALSE is returned.

                    Write program code for RemoveNode()

 Save your program.

 Copy and paste the program code into part 3(b)(iv) in the evidence document.
                                                                                                            [6]





                                                      10

    (c) (i)     The main program creates a new LinkedList object and uses the appropriate method
                to insert five nodes with the following integer data values in the order given:

                                10        20          30        40   50

                The main program then:

                •   calls Traverse()
                •   removes the node containing the integer data 30 using RemoveNode()
                •   calls Traverse()

                Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 3(c)(i) in the evidence document.
                                                                                             [3]

         (ii)   Test your program.

                Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot into part 3(c)(ii) in the evidence document.
                                                                                             [2]
```

## Python 接口与 QP / MS 差异

接口照 QP：`Node(Data)`、`LinkedList()`、`InsertNode(integer)`、`Traverse()` 返回空格分隔字符串、`RemoveNode(integer)` 返回真正的 BOOLEAN。末尾多一个空格按 MS 范例接受，内部整数间一个空格。MS p.41 Python 在尾结点访问 NextNode.GetData 会遇 None，且非头删除与找不到时没有返回 BOOLEAN；按 QP 修正为先查下一结点是否非空，再分别返回 True / False。MS p.44 只保存两次 Traverse 返回值，没有 print；QP 截图格与 MS p.45 要求输出两组列表，所以参考解补输出。3(b)(iv) 7 个可选点最多 6 分。

## 证据文档对照表

| 证据格 | 行 id | 分 | 内容 | 自动测（测试名 · 语料得分点） | 人工核对 |
|:--|:--|--:|:--|:--|:--|
| Part 3(a)(i) | 9618_s25_43:3(a)(i) | 4 | 代码 | `test_3a_node_references` · MP4 | MP1, MP2, MP3 |
| Part 3(a)(ii) | 9618_s25_43:3(a)(ii) | 3 | 代码 | `test_3a_node_references` · MP2, MP3 | MP1 |
| Part 3(a)(iii) | 9618_s25_43:3(a)(iii) | 2 | 代码 | `test_3a_node_references` · MP2 | MP1 |
| Part 3(b)(i) | 9618_s25_43:3(b)(i) | 2 | 代码 | `test_3b_i_ii_iii_empty_and_head_insertion` · MP2 | MP1 |
| Part 3(b)(ii) | 9618_s25_43:3(b)(ii) | 4 | 代码 | `test_3b_i_ii_iii_empty_and_head_insertion` · MP2, MP3, MP4 | MP1 |
| Part 3(b)(iii) | 9618_s25_43:3(b)(iii) | 3 | 代码 | `test_3b_i_ii_iii_empty_and_head_insertion` · MP1, MP2, MP3 | — |
| Part 3(b)(iv) | 9618_s25_43:3(b)(iv) | 6 | 代码 | `test_3b_iv_empty_and_singleton` / `test_3b_iv_head_middle_tail_missing` / `test_3b_iv_removes_only_first_match` · MP1, MP2, MP3, MP4, MP5, MP6, MP7 | — |
| Part 3(c)(i) | 9618_s25_43:3(c)(i) | 3 | 代码 | `test_3c_ii_screenshots_before_after` · MP1, MP2, MP3 | — |
| Part 3(c)(ii) | 9618_s25_43:3(c)(ii) | 2 | 截图 | `test_3c_ii_screenshots_before_after` · MP1, MP2 | — |

自动覆盖表示行为得到验证；混合点里的函数头、注释、调用结构仍须补核，不能凭测试自动授予考试分数。可选得分点多于该行满分时，按 markpoints[].marks 加权后按该行满分比例折算。

## 人工核对清单

- [ ] 3(a)(i) MP1：Class Node header (and end)
- [ ] 3(a)(i) MP2：TheData declared as Integer, NextNode declared as Node
- [ ] 3(a)(i) MP3：Constructor header (and end) taking (min) 1 parameter …
- [ ] 3(a)(ii) MP1：1 get method header (and close) taking no parameters …
- [ ] 3(a)(iii) MP1：SetNextNode() method header (and close) taking 1 parameter (of type Node) …
- [ ] 3(b)(i) MP1：Class LinkedList header (and close) and constructor header with no parameter (and close) …
- [ ] 3(b)(ii) MP1：InsertNode()method header (and close) taking one (integer) parameter
- [ ] 所有方法头、主程序的调用顺序、返回值接收与题给标识符符合该题 MS；属性注释写明类型，私有属性不改成公有属性。
- [ ] 题目指定算法自行实现，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳（D10 ③；本项人工核对）。
- [ ] 截图清晰，输入、输出及要求的文件名可见；appropriate message 的语义与状态一致（措辞不限）。

## 得分点编号（D37 ②）

编号采用语料 markpoints[].n；1 分且未拆分的行记“整行”。本题 MS 圆点顺序与语料一致；若 MS 给可选点上限，按该行上限计分。
