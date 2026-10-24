# 9618_w22_41 第 3 题 · 二叉树递归查找与后序遍历

## 导读

本练习覆盖 6 个小问，共 21 分。从空白程序完成整道大题；可用 `make try EX=practice/p4/9618_w22_41_q3 K=3b` 按小问测试。标识符、指针初值与文件名照抄 QP（D10）；数组必须建立固定长度的真实 list，并用英文注释写明大小与类型。算法自行编写循环与指针操作，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳。

主程序放在 `if __name__ == "__main__":` 下，避免导入时运行输入；提示写在 `input("…")` 里（D13）。测试通过与人工清单通过之后才能记录掌握（D3）。

## Python 接口

`ArrayNodes` 固定20×3，先按3(a)全部初始化-1，再按3(b)修改前六行；导入后的状态是3(b)最终树。`FreeNode=6`、`RootPointer=0`。`SearchValue(Root, ValueToFind)` 的 Root 是下标；`PostOrder(RootNode)` 采用 MS Python 节点行参数（例如 ArrayNodes[RootPointer]），输出数据而非下标。SearchValue 用递归实现，测试统计递归访问路径；PostOrder 也检查递归调用与左、右、根顺序。3(a)初始化遍历及覆盖前六行之前的状态须人工核对，自动测试验证最终形状与未用节点；不因最终树非全-1判错。

## 英文原题（QP 原页转写）

```text
3   A binary tree consists of nodes. Each node has 3 integer values: a left pointer, data and a right
    pointer.

    The binary tree is stored using a global 2D array.

    The pseudocode declaration for the array is:

    DECLARE ArrayNodes : ARRAY[0:19, 0:2] OF INTEGER

    For example:

    •    ArrayNodes[0, 0] stores the left pointer for the first node.
    •    ArrayNodes[0, 1] stores the data for the first node.
    •    ArrayNodes[0, 2] stores the right pointer for the first node.

    –1 indicates a null pointer, or null data.

    (a) Write program code to:

         •     declare the global 2D array ArrayNodes
         •     initialise all 3 integer values to –1 for each node.

 Save your program as Question3_N22.

 Copy and paste the program code into part 3(a) in the evidence document.
                                                                                                  [3]

    (b) The binary tree stores the following values:

                  Index        Left pointer                Data         Right pointer

                     0               1                      20                5

                     1               2                      15                –1

                     2              –1                      3                 3

                     3              –1                      9                 4

                     4              –1                      10                –1

                     5              –1                      58                –1

                     6              –1                      –1                –1

         FreeNode stores the index of the first free element in the array, initialised to 6.

         RootPointer stores the index of the first node in the tree, initialised to 0.

         Amend your program by writing program code to store the given data in ArrayNodes and
         initialise the free node and root node pointers.

 Save your program.

 Copy and paste the program code into part 3(b) in the evidence document.
                                                                                                  [2]

(c) The following recursive pseudocode function searches the binary tree for a given value. If the
        value is found, the function must return the index of the value. If the value is not found, the
        function must return –1.

         The function is incomplete. There are four incomplete statements.

         FUNCTION SearchValue(Root : INTEGER,
                              ValueToFind : INTEGER) RETURNS INTEGER

               IF Root = –1 THEN

                   RETURN –1

               ELSE

                 IF ArrayNodes[Root, 1] = ValueToFind THEN

                       RETURN .......................................

                 ELSE

                       IF ArrayNodes[Root, 1] = –1 THEN

                            RETURN –1

                       ENDIF

                 ENDIF

               ENDIF

               IF ArrayNodes[Root, 1] ....................................... ValueToFind THEN

                   RETURN SearchValue(ArrayNodes[............, 0], ValueToFind)

               ENDIF

               IF ArrayNodes[Root, ............] < ValueToFind THEN

                   RETURN SearchValue(ArrayNodes[Root, 2], ValueToFind)

               ENDIF

         ENDFUNCTION

         Write program code for the function SearchValue().

 Save your program.

 Copy and paste the program code into part 3(c) in the evidence document.
                                                                                                    [5]

(d) A post order traversal performs the following operation:

         •     visit the left node
         •     visit the right node
         •     output the root.

         For example, in the following tree, the output would be: 3     9   25   60   50



                                            25                     60
                                      3                   9
         An outline of the PostOrder() procedure is:

         •     If left node is not empty, make a recursive call with the left node as the root.
         •     If right node is not empty, make a recursive call with the right node as the root.
         •     Output the current root node.

         The procedure PostOrder() takes the root node as a parameter.

         Write program code for the procedure PostOrder().

 Save your program.

 Copy and paste the program code into part 3(d) in the evidence document.
                                                                                                    [7]

(e) (i)     Amend the main program by writing program code to:

                •   call the function SearchValue() to find the position of the number 15 in the tree
                •   use the result from SearchValue() to output either the index of the value if found,
                    or an appropriate message to state that the value was not found
                •   call the procedure PostOrder().

 Save your program.

 Copy and paste the program code into part 3(e)(i) in the evidence document.
                                                                                                    [3]

         (ii)   Test your program.

                Take a screenshot to show the output.

 Copy and paste the screenshot into part 3(e)(ii) in the evidence document.

                                                                                                    [1]
```

## 证据文档对照表

已逐格核对官方 evidence.doc；一格一行。MP 编号均为语料 `markpoints[].n`（D37 ②）。一个 MP 同时含函数头与行为时，行为列自动，函数头仍须人工核对；只考结构的 MP 全部列人工。可选点超过行分时，按 `行分 × 自动点分 / 全部点分` 折算，不表示真实考试逐点授分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_w22_41:3(a) | 3 | 代码 | `test_3a_array_shape_and_unused_nodes` · MP1、MP3 | MP2 |
| Part 3(b) | 9618_w22_41:3(b) | 2 | 代码 | `test_3b_preset_and_pointers` · MP1、MP2 | — |
| Part 3(c) | 9618_w22_41:3(c) | 5 | 代码 | `test_3c_search_both_branches`、`test_3c_search_recursive_and_null_data` · MP1 | MP2 |
| Part 3(d) | 9618_w22_41:3(d) | 7 | 代码 | `test_3d_postorder_recursive`、`test_3d_postorder_different_tree` · MP1、MP2、MP3、MP4、MP5、MP6、MP7 | — |
| Part 3(e)(i) | 9618_w22_41:3(e)(i) | 3 | 代码 | `test_3e_screenshot` · MP1、MP2、MP3 | — |
| Part 3(e)(ii) | 9618_w22_41:3(e)(ii) | 1 | 截图 | `test_3e_screenshot` · 整行 | — |

自动测分值 19.000000，人工核对分值 2.000000，自动占比 90.48%。这是验证覆盖口径，自动测试不为未实际核对的写法授分。

## 人工核对清单

- [ ] 9618_w22_41:3(a) MP2：looping through all 20 × 3 elements of array …（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_w22_41:3(c) MP2：1 mark for remainder of function correct（1 分；人工核对代码结构 / 声明）。
- [ ] 所有模块头、参数个数与顺序、全局 / 局部作用域符合 QP；所有 list 的类型与大小有英文注释；没有用内置函数替代题目要求的算法（D10 ③）。
- [ ] 给定伪代码的整体流程、没有多余代码、打开与关闭文件位置，由导师按本题 MS 看代码核对。行为正确不替代这些检查。
- [ ] 截图清晰、输入与规定的输出可见；自动测试只验证输出内容，不验证图片本身。

## 原页、编号与差异记录

已看 QP pp.8–11、MS pp.16–23 全部渲染图，核对 evidence.doc 6 格。MS p.17 Python 把 ArrayNodes 重建为仅6行，且写 FreeNodes（多s），参考解保留20行并用 QP FreeNode。MS p.23 截图为 Found at 1，然后10、9、3、15、58、20。3(c)语料MP1合并四处填空（4分），MP2整体余下逻辑（1分）人工；不自造四个点号。3(e)(i) MP2 的成功分支自动测，找不到分支固定示例不会经过，归于人工补核，不据此声称整个分支均自动覆盖。PostOrder采用节点参数，MS也允许下标参数但本练习接口已约定节点形式。与 w22_43 第3题相同；无本题源文件。
