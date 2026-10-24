# 9618_w22_42 第 3 题 · 线性队列与递归求和

覆盖 6 行，共 21 分。QP 原页：[8, 9]；MS 原页：[20, 21, 22, 23, 24]，已逐页渲染核对。证据格另对照官方 evidence.doc。

## 导读

从 starter.py 的空白分节开始写；标识符、文件名照题目。数组必须建出真实 list，并以英文注释注明类型与大小（D10 ①）；指针初值照题目（D10 ②）。排序、查找及 ADT 操作自己写循环，不用 `sort()`、`sorted()`、`index()`、`max()`、`min()` 或成员测试 `in` 代劳（D10 ③）。主程序置于 `if __name__ == "__main__":` 下，以便测试导入；提示语写在 `input("…")` 中。

## 英文原题（QP 原页转写）

```text
3   A program uses a linear queue to store up to 100 integers.

    (a) A 1D array, Queue, is used to store the data. The head pointer points to the first number
        stored in the queue and the tail pointer points to the next free space in the queue.

         Write program code to:

         •     declare the global array Queue
         •     declare the global variable head pointer and assign an appropriate initial value
         •     declare the global variable tail pointer and assign an appropriate initial value.

 Save your program as Question3_N22.

 Copy and paste the program code into part 3(a) in the evidence document.
                                                                                                   [3]

    (b) The function Enqueue() takes an integer value as a parameter and stores it in the queue. It
        returns TRUE if the value was successfully stored and FALSE otherwise.

         Write program code for the function Enqueue().

 Save your program.

 Copy and paste the program code into part 3(b) in the evidence document.
                                                                                                   [6]

    (c) The main program uses the Enqueue() function to store the numbers 1 to 20 (inclusive)
        in the queue, in ascending numerical order. The program should output ‘Successful’ if all
        numbers are successfully enqueued, and ‘Unsuccessful’ otherwise.

         Amend the main program by writing program code to perform this task.

 Save your program.

 Copy and paste the program code into part 3(c) in the evidence document.
                                                                                                   [4]

(d) The following iterative pseudocode function calculates the total of all the values stored in the
        queue.

         FUNCTION IterativeOutput(Start: INTEGER) RETURNS INTEGER

                DECLARE Total : INTEGER

                Total ←0
                FOR Count ← Start - 1 TO HeadPointer STEP -1

                   Total ← Total + Queue[Count]

                NEXT Count

                RETURN Total

         ENDFUNCTION

         Rewrite the function as a recursive function using program code.

 Save your program.

 Copy and paste the program code into part 3(d) in the evidence document.
                                                                                                     [6]

    (e) The main program calls the recursive function from part 3(d) and outputs the value returned.

          (i)   Amend the main program by writing program code to perform this task.

 Save your program.

 Copy and paste the program code into part 3(e)(i) in the evidence document.
                                                                                                     [1]

         (ii)   Test your program.

                Take a screenshot to show the output.

 Copy and paste the screenshot into part 3(e)(ii) in the evidence document.

                                                                                                     [1]
```

## Python 接口与测试约定

- `Queue`、`HeadPointer`、`TailPointer` 为全局变量；`Enqueue(Data)` 返回布尔值。
- QP 未命名的递归函数采用 MS 名字 `RecursiveOutput(Start)`。接口按 MS：Start 是最后一个有效下标，主程序传 `TailPointer - 1`。原迭代伪代码的 Start 是尾后位置，两者参数换算后计算相同的队列总和。测试不要求把未定义的空队列传给递归函数。
- 无数据文件（本卷 sf 中的数据属于其他题）。

## 证据文档对照表

表内 MP 号取语料 markpoints[].n。每行列出自动与人工主归属；类型注释、函数头和截图可读性仍须人工核对。自动占比只统计可观察行为，并非自动给出考试分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_w22_42:3(a) | 3 | 代码 | `test_3a_queue_and_pointers` · MP1、MP2、MP3 | — |
| Part 3(b) | 9618_w22_42:3(b) | 6 | 代码 | `test_3b_first_last_and_full` · MP2、MP3、MP4、MP5、MP6 | MP1 Function header (and close where appropriate) with integer parameter |
| Part 3(c) | 9618_w22_42:3(c) | 4 | 代码 | `test_3e_ii_screenshot_total`、`test_3c_reports_any_enqueue_failure` · MP1、MP2、MP3、MP4 | — |
| Part 3(d) | 9618_w22_42:3(d) | 6 | 代码 | `test_3d_recursive_sum` · MP2、MP3、MP4、MP5、MP6 | MP1 function call (and end where appropriate) taking a parameter |
| Part 3(e)(i) | 9618_w22_42:3(e)(i) | 1 | 代码 | `test_3e_ii_screenshot_total` · MPwhole | — |
| Part 3(e)(ii) | 9618_w22_42:3(e)(ii) | 1 | 截图 | `test_3e_ii_screenshot_total` · MPwhole | — |

## 人工核对清单

- [ ] 3(b) MP1：Function header (and close where appropriate) with integer parameter
- [ ] 3(d) MP1：function call (and end where appropriate) taking a parameter
- [ ] 数组、指针与记录字段的英文类型注释及作用域正确，数组大小与 QP 一致。
- [ ] 按 QP 写指定算法；没有以内置容器操作代替数组 ADT 或查找、排序步骤。
- [ ] 所有截图清晰；输入、输出和要求的文件名可见；截图不能仅由 pytest 成功代替。


## QP / MS 差异与点号对照

- MS p.21 的 Python 范例漏 `global HeadPointer`，首次入队会引发 UnboundLocalError；参考解补齐。
- 3(c) QP 要求所有入队都成功才输出 Successful；参考解累计失败标志。MS p.22 范例只保留最后一次返回值；给定空队列装入 20 项时没有输出差异。
- QP/MS 原页的赋值箭头转写为 `←`；递归参数采用上述明确约定。

语料点号按本题 MS 圆点顺序；未拆得分点的 1 分行以 whole 表示。
