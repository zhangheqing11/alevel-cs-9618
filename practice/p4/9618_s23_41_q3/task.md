# 9618_s23_41 第 3 题 · 双栈动物与颜色配对

## 导读

本练习覆盖 9 个小问，共 25 分。从空白程序完成整道大题；可用 `make try EX=practice/p4/9618_s23_41_q3 K=3b` 按小问测试。标识符、指针初值与文件名照抄 QP（D10）；数组必须建立固定长度的真实 list，并用英文注释写明大小与类型。算法自行编写循环与指针操作，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳。

主程序放在 `if __name__ == "__main__":` 下，避免导入时运行输入；提示写在 `input("…")` 里（D13）。测试通过与人工清单通过之后才能记录掌握（D3）。

## Python 接口

接口名及参数沿用 QP / MS：`PushAnimal(DataToPush)`、`PopAnimal()`、`PushColour(DataToPush)`、`PopColour()`、`ReadData()`、`OutputItem()`；Push 返回布尔值，Pop 空时返回空串。全局数组与指针名照 QP。ReadData 为最终版本，一次读取两个文件。文件行可在读取或输出时去掉换行，最终配对必须在一行显示。两栈均空时不向任何栈压入空字符串；QP 未规定此时具体提示，测试只检查有输出且两个指针仍为 0。

## 英文原题（QP 原页转写）

```text
3   A program implements two stacks using 1D arrays. One stack stores the names of colours. One
    stack stores the names of animals.

    (a) The program contains the following global arrays and variables:

         •     1D array Animal to store the names of up to 20 animals.
         •     1D array Colour to store the names of up to 10 colours.
         •     AnimalTopPointer to point to the next free space in the array Animal, initialised to 0.
         •     ColourTopPointer to point to the next free space in the array Colour, initialised to 0.

         Write program code to declare the global arrays and variables.

 Save your program as Question3_J2023.

 Copy and paste the program code into part 3(a) in the evidence document.
                                                                                                   [3]

    (b) (i)    Study the pseudocode function PushAnimal():

               FUNCTION PushAnimal(DataToPush : STRING) RETURNS BOOLEAN

                   IF AnimalTopPointer = 20 THEN

                       RETURN FALSE

                   ELSE

                       Animal[AnimalTopPointer] ← DataToPush

                       AnimalTopPointer ← AnimalTopPointer + 1

                       RETURN TRUE

                   ENDIF

               ENDFUNCTION

               Write program code for the function PushAnimal()

 Save your program.

 Copy and paste the program code into part 3(b)(i) in the evidence document.
                                                                                                   [3]

(ii)   Study the pseudocode function PopAnimal():

                FUNCTION PopAnimal() RETURNS STRING

                    DECLARE ReturnData : STRING

                    IF AnimalTopPointer = 0 THEN

                       RETURN ""

                    ELSE

                       ReturnData ← Animal[AnimalTopPointer - 1]

                       AnimalTopPointer ← AnimalTopPointer - 1

                       RETURN ReturnData

                    ENDIF

                ENDFUNCTION

                Write program code to declare the function PopAnimal()

 Save your program.

 Copy and paste the program code into part 3(b)(ii) in the evidence document.
                                                                                              [3]

        (iii)   The procedure ReadData():

                •   reads the animal names from the file AnimalData.txt
                •   uses PushAnimal() to insert each name onto the stack
                •   uses appropriate exception handling if the file does not exist.

                Write program code for the procedure ReadData()

 Save your program.

 Copy and paste the program code into part 3(b)(iii) in the evidence document.
                                                                                              [5]

        (iv)    The function PushColour() performs the same actions as PushAnimal() but inserts
                an item into Colour.

                The function PopColour() performs the same actions as PopAnimal() but removes
                the next item from Colour.

                Write program code for the functions PushColour() and PopColour()

 Save your program.

 Copy and paste the program code into part 3(b)(iv) in the evidence document.
                                                                                              [2]

(v)    Amend the procedure ReadData() so that it also:

                •   reads the colours from the text file ColourData.txt
                •   uses PushColour() to insert each colour onto the stack
                •   uses appropriate exception handling if the file does not exist.

 Save your program.

 Copy and paste the program code into part 3(b)(v) in the evidence document.
                                                                                       [2]

    (c) The procedure OutputItem():

         •      pops the next item from both Animal and Colour
         •      outputs the colour and animal on one line, for example "black horse"

         If there is no data in Colour:

         •      the animal is pushed back onto Animal
         •      "No colour" is output.

         If there is no data in Animal:

         •      the colour is pushed back onto Colour
         •      "No animal" is output.

         Write program code for the procedure OutputItem()

 Save your program.

 Copy and paste the program code into part 3(c) in the evidence document.
                                                                                       [5]

    (d) The main program:

         •      calls the procedure ReadData()
         •      calls OutputItem() four times.

          (i)   Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 3(d)(i) in the evidence document.
                                                                                       [1]

         (ii)   Test your program.

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 3(d)(ii) in the evidence document.
                                                                                       [1]
```

## 证据文档对照表

已逐格核对官方 evidence.doc；一格一行。MP 编号均为语料 `markpoints[].n`（D37 ②）。一个 MP 同时含函数头与行为时，行为列自动，函数头仍须人工核对；只考结构的 MP 全部列人工。可选点超过行分时，按 `行分 × 自动点分 / 全部点分` 折算，不表示真实考试逐点授分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_s23_41:3(a) | 3 | 代码 | `test_3a_declarations` · MP1、MP2、MP3 | — |
| Part 3(b)(i) | 9618_s23_41:3(b)(i) | 3 | 代码 | `test_3b_stack_capacity_lifo_and_reuse`、`test_3b_no_algorithm_shortcuts` · MP1、MP2、MP3 | — |
| Part 3(b)(ii) | 9618_s23_41:3(b)(ii) | 3 | 代码 | `test_3b_stack_capacity_lifo_and_reuse` · MP1、MP2、MP3 | — |
| Part 3(b)(iii) | 9618_s23_41:3(b)(iii) | 5 | 代码 | `test_3b_read_files`、`test_3b_missing_file` · MP1、MP2、MP3、MP5 | MP4；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 3(b)(iv) | 9618_s23_41:3(b)(iv) | 2 | 代码 | `test_3b_stack_capacity_lifo_and_reuse` · MP1、MP2 | — |
| Part 3(b)(v) | 9618_s23_41:3(b)(v) | 2 | 代码 | `test_3b_read_files`、`test_3b_missing_file` · MP1、MP2 | — |
| Part 3(c) | 9618_s23_41:3(c) | 5 | 代码 | `test_3c_output_pair`、`test_3c_restores_unmatched_item`、`test_3c_both_empty_does_not_create_item` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 3(d)(i) | 9618_s23_41:3(d)(i) | 1 | 代码 | `test_3d_screenshot`、`test_3d_main_call_chain` · MPwhole | — |
| Part 3(d)(ii) | 9618_s23_41:3(d)(ii) | 1 | 截图 | `test_3d_screenshot` · MPwhole | — |

自动测分值 24.000000，人工核对分值 1.000000，自动占比 96.00%。这是验证覆盖口径，自动测试不为未实际核对的写法授分。

## 人工核对清单

- [ ] 9618_s23_41:3(b)(iii) MP4：Closing the file（1 分；人工核对代码结构 / 声明）。
- [ ] 所有模块头、参数个数与顺序、全局 / 局部作用域符合 QP；所有 list 的类型与大小有英文注释；没有用内置函数替代题目要求的算法（D10 ③）。
- [ ] 给定伪代码的整体流程、没有多余代码、打开与关闭文件位置，由导师按本题 MS 看代码核对。行为正确不替代这些检查。
- [ ] 截图清晰、输入与规定的输出可见；自动测试只验证输出内容，不验证图片本身。

## 原页、编号与差异记录

已看 QP pp.8–10 与 MS pp.26–38 全部渲染图，核对 evidence.doc 9 格。MS p.38 截图依次 pink hamster、blue elephant、white eagle、yellow rabbit。MS 用空 list + append，参考解按 D10 用固定长度数组和下标赋值，避免 Pop 后再次 Push 落到错误位置。MS ReadData 没去行尾，参考解去行尾使输出符合 QP 一行一对。MS 3(c) 两栈均空时将空串压回 Animal，按 QP “removed animal” 改为只放回实际取出的项目（D31）。MS 无独立数字 MP，语料按清单顺序；3(b)(iii) 首句印 1 mark，但五点与 5 分栏明确。与 s23_43 第 3 题相同，不重复创建。

## T38c2 · D46 验证补充

补测 ReadData 与四次 OutputItem（含实际双栈 Pop）；截图允许额外说明行。QP 明定配对一行的规则保留（QP pp.9–10/MS p.38）。 OutputItem 也允许额外说明行，配对本身仍在一行。

本次行为覆盖：自动 24.000000 分、人工 1.000000 分（96.00%）。调用测试不能代替类型注释、代码结构及证据截图的人工检查。
