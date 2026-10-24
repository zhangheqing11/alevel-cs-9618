# 9618_s22_42 第 1 题 · 数组栈与下一空位指针

## 导读

本练习覆盖 7 个小问，共 25 分。从空白程序完成整道大题；可用 `make try EX=practice/p4/9618_s22_42_q1 K=1b` 按小问测试。标识符、指针初值与文件名照抄 QP（D10）；数组必须建立固定长度的真实 list，并用英文注释写明大小与类型。算法自行编写循环与指针操作，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳。

主程序放在 `if __name__ == "__main__":` 下，避免导入时运行输入；提示写在 `input("…")` 里（D13）。测试通过与人工清单通过之后才能记录掌握（D3）。

## Python 接口

全局 `StackData`（10 个整数）和 `StackPointer`（初值 0）；`Push(DataToPush)` 返回布尔值；`Pop()` 返回整数，空时 -1。QP 未命名的输出过程采用 MS 名 `PrintArray()`，输出指针与全部十格（前后顺序、单行或多行均可）。截图测试按所需数值的有序子序列读取，允许说明文字带数字。状态提示措辞和是否正确表示成功/失败由导师人工核对，不要求每次提示相同。主程序连续输出入栈后和两次出栈后的两份状态。允许保留已出栈槽值、清零或清空；这是 MS 明文允许的变体，不把清除槽值作为得分条件。

## 英文原题（QP 原页转写）

```text
Open the document evidence.doc

Make sure that your name, centre number and candidate number will appear on every page of this
document. This document must contain your answers to each question.

Save this evidence document in your work area as:

evidence_ followed by your centre number_candidate number, for example: evidence_zz999_9999

A class declaration can be used to declare a record.
If the programming language used does not support arrays, a list can be used instead.

A source file is used to answer Question 3. The file is called CardValues.txt

1   A program needs to use a stack data structure. The stack can store up to 10 integer elements.

    A 1D array StackData is used to store the stack globally. The global variable StackPointer
    points to the next available space in the stack and is initialised to 0.

    (a) Write program code to declare the array and pointer as global data structures. Initialise the
        pointer to 0.

 Save your program as Question1_J22.

 Copy and paste the program code into part 1(a) in the evidence document.
                                                                                                    [3]

    (b) Write a procedure to output all 10 elements in the stack and the value of StackPointer.

 Save your program.

 Copy and paste the program code into part 1(b) in the evidence document.
                                                                                                    [3]

    (c) The function Push() takes an integer parameter and returns FALSE if the stack is full. If the
        stack is not full, it puts the parameter value on the stack, updates the relevant pointer and
        returns TRUE.

         Write program code for the function Push().

 Save your program.

 Copy and paste the program code into part 1(c) in the evidence document.
                                                                                                    [6]

(d) (i)     Edit the main program to test the Push() function. The main program needs to:

                •    allow the user to enter 11 numbers and attempt to add these to the stack
                •    output an appropriate message when a number is added to the stack
                •    output an appropriate message when a number is not added to the stack if it is full
                •    output the contents of the stack after attempting to add all 11 numbers.

 Save your program.

 Copy and paste the program code into part 1(d)(i) in the evidence document.
                                                                                                      [5]

         (ii)   Test your program from part 1(d)(i) with the following 11 inputs:

                11     12     13     14     15       16       17   18    19     20     21

                Take a screenshot to show the output.

 Copy and paste the screenshot into part 1(d)(ii) in the evidence document.
                                                                                                      [1]

    (e) The function Pop() returns −1 if the stack is empty. If the stack is not empty, it returns the
        element at the top of the stack and updates the relevant pointer.

          (i)   Write program code for the function Pop().

 Save your program.

 Copy and paste the program code into part 1(e)(i) in the evidence document.
                                                                                                      [5]

         (ii)   After the code you wrote in the main program for part 1(d)(i), add program code to:

                •    remove two elements from the stack using Pop()
                •    output the updated contents of the stack.

                Test your program and take a screenshot to show the output.

 Copy and paste the screenshot into part 1(e)(ii) in the evidence document.
                                                                                                      [2]
```

## 证据文档对照表

已逐格核对官方 evidence.doc；一格一行。MP 编号均为语料 `markpoints[].n`（D37 ②）。一个 MP 同时含函数头与行为时，行为列自动，函数头仍须人工核对；只考结构的 MP 全部列人工。可选点超过行分时，按 `行分 × 自动点分 / 全部点分` 折算，不表示真实考试逐点授分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_s22_42:1(a) | 3 | 代码 | `test_1a_declarations` · MP1、MP2、MP3 | — |
| Part 1(b) | 9618_s22_42:1(b) | 3 | 代码 | `test_1b_printarray` · MP2、MP3 | MP1；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 1(c) | 9618_s22_42:1(c) | 6 | 代码 | `test_1c_push_boundary`、`test_1b_no_algorithm_shortcuts` · MP2、MP3、MP4、MP5、MP6 | MP1；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 1(d)(i) | 9618_s22_42:1(d)(i) | 5 | 代码 | `test_1d_1e_main_call_chain` · MP1、MP2、MP5 | MP3、MP4；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 1(d)(ii) | 9618_s22_42:1(d)(ii) | 1 | 截图 | 行为辅助测试（不计自动分） | MPwhole；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 1(e)(i) | 9618_s22_42:1(e)(i) | 5 | 代码 | `test_1e_pop_lifo_empty_reuse` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 1(e)(ii) | 9618_s22_42:1(e)(ii) | 2 | 截图 | `test_1e_screenshot_after_two_pops` · MP1、MP2 | — |

自动测分值 20.000000，人工核对分值 5.000000，自动占比 80.00%。这是验证覆盖口径，自动测试不为未实际核对的写法授分。

## 人工核对清单

- [ ] 9618_s22_42:1(d)(ii) MPwhole：本次归人工，按同题 MS 核对适当消息或固定主程序未覆盖的分支。

- [ ] 9618_s22_42:1(d)(i) MP3、MP4：按同题 MS 查看消息语义及未触发的选择分支；不由固定输出推定。

- [ ] 9618_s22_42:1(b) MP1：procedure header with sensible identifier (and end where appropriate)（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s22_42:1(c) MP1：function Push() taking an integer parameter（1 分；人工核对代码结构 / 声明）。
- [ ] 所有模块头、参数个数与顺序、全局 / 局部作用域符合 QP；所有 list 的类型与大小有英文注释；没有用内置函数替代题目要求的算法（D10 ③）。
- [ ] 给定伪代码的整体流程、没有多余代码、打开与关闭文件位置，由导师按本题 MS 看代码核对。行为正确不替代这些检查。
- [ ] 截图清晰、输入与规定的输出可见；自动测试只验证输出内容，不验证图片本身。

## 原页、编号与差异记录

已看 QP pp.2–3 与 MS pp.4–12 全部渲染图，并核对 evidence.doc 7 格。MS Python 例正确，参考解只加入口保护；Java 主程序循环少一次，不采用（QP 明确 11 次）。MS 1(e)(ii) 明确接受 11–20、11–18、11–18 后两个 null；测试接受这些输出，固定数组声明与 Pop 指针行为另测。MS 没有印数字 MP，语料清单顺序一致；无编号差异。无源数据文件。

## T38c2 · D46 验证补充

补测 Push(11..21) → PrintArray → Pop 两次 → PrintArray；输出允许说明数字、指针前后顺序及 MS 三种清槽方案（QP p.3/MS pp.5/8/10/12）。合适消息语义及按返回值分支改列人工补核。 截图的适当消息语义不可自动判别，1(d)(ii) 整行列人工。

本次行为覆盖：自动 20.000000 分、人工 5.000000 分（80.00%）。调用测试不能代替类型注释、代码结构及证据截图的人工检查。
