# 9618_s25_41 第 1 题 · 整数循环队列

## 导读

本练习覆盖 6 个小问，共 20 分。从空白程序完成整道大题；可用 `make try EX=practice/p4/9618_s25_41_q1 K=1b` 按小问测试。标识符、指针初值与文件名照抄 QP（D10）；数组必须建立固定长度的真实 list，并用英文注释写明大小与类型。算法自行编写循环与指针操作，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳。

主程序放在 `if __name__ == "__main__":` 下，避免导入时运行输入；提示写在 `input("…")` 里（D13）。测试通过与人工清单通过之后才能记录掌握（D3）。

## Python 接口

全局名 `Queue`、`HeadPointer`、`TailPointer`、`NumberItems`；`Enqueue(InputData)` 返回布尔值；`Dequeue()` 空时 -1。TailPointer 指最后一项，与 s22_41 的下一空位约定不同，不能套用前题指针公式。最后一个元素出队后两指针重设 -1（本题 MS 明确）。主程序输出数字与指定 Successful / Unsuccessful，最后输出两次出队值。

## 英文原题（QP 原页转写）

```text
You have been supplied with the following source files:

TheData.txt
Blue.txt
Green.txt
Orange.txt
Pink.txt
Red.txt
Yellow.txt

Open the evidence document, evidence.doc

Make sure that your name, centre number and candidate number will appear on every page of this
document. This document must contain your answers to each question.

Save this evidence document in your work area as:
evidence_ followed by your centre number_candidate number, for example: evidence_zz999_9999

A class declaration can be used to declare a record. If the programming language used does not
support arrays, a list can be used instead.

Seven source files are used to answer Question 2. The files are called TheData.txt, Blue.txt,
Green.txt, Orange.txt, Pink.txt, Red.txt and Yellow.txt

1      A program stores positive integers in a circular queue.

       The queue is stored as a global 1D array of 20 integers with the identifier Queue. Each index is
       initialised with the data –1

       The global variable HeadPointer, initialised to –1, points to the first element in the queue.
       The global variable TailPointer, initialised to –1, points to the last element in the queue.
       The global variable NumberItems, initialised to 0, stores the number of items in the queue.

       (a) Write program code to declare and initialise Queue, HeadPointer, TailPointer and
           NumberItems

    Save your program as Question1_J25.

    Copy and paste the program code into part 1(a) in the evidence document.
                                                                                                       [2]

       (b) The function Enqueue():

           •    takes an integer as a parameter
           •    checks if the queue is full
           •    returns FALSE if the queue is full
           •    stores the parameter in the next position in the queue and returns TRUE if the queue is
                not full
           •    updates the appropriate pointers and NumberItems

           Write program code for Enqueue()

    Save your program.

    Copy and paste the program code into part 1(b) in the evidence document.
                                                                                                       [6]

(c) The main program:

         •      attempts to store each of the integers 1 to 25 (inclusive) in the queue in ascending
                numerical order using Enqueue()
         •      outputs the integer that was passed to Enqueue() and "Successful" if it was stored
                in the queue, or "Unsuccessful" if it was not stored in the queue.
                For example:
                    if the integer 5 is passed to Enqueue() and is stored in the queue, the output will
                     be: "5 Successful"
                    if the integer 23 is passed to Enqueue() and is not stored in the queue, the output
                     will be: "23 Unsuccessful"

         Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 1(c) in the evidence document.
                                                                                                     [3]

    (d) The function Dequeue() returns –1 if the queue is empty. If the queue is not empty, the
        function returns the next item in the queue, updates the appropriate pointers and updates
        NumberItems

         Write program code for Dequeue()

 Save your program.

 Copy and paste the program code into part 1(d) in the evidence document.
                                                                                                     [6]

    (e) (i)     Write program code to extend the main program to call Dequeue() twice and output the
                return value each time.

 Save your program.

 Copy and paste the program code into part 1(e)(i) in the evidence document.
                                                                                                     [2]

         (ii)   Test your program.

                Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot into part 1(e)(ii) in the evidence document.
                                                                                                     [1]
```

## 证据文档对照表

已逐格核对官方 evidence.doc；一格一行。MP 编号均为语料 `markpoints[].n`（D37 ②）。一个 MP 同时含函数头与行为时，行为列自动，函数头仍须人工核对；只考结构的 MP 全部列人工。可选点超过行分时，按 `行分 × 自动点分 / 全部点分` 折算，不表示真实考试逐点授分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_s25_41:1(a) | 2 | 代码 | `test_1a_initial_state` · MP1、MP2 | — |
| Part 1(b) | 9618_s25_41:1(b) | 6 | 代码 | `test_1b_enqueue_full`、`test_1bd_wrap_partial_dequeue_and_refill` · MP1、MP2、MP3、MP4、MP5、MP6 | — |
| Part 1(c) | 9618_s25_41:1(c) | 3 | 代码 | `test_1ce_screenshot` · MP1、MP2、MP3 | — |
| Part 1(d) | 9618_s25_41:1(d) | 6 | 代码 | `test_1bd_wrap_partial_dequeue_and_refill`、`test_1d_empty_reset_and_reuse` · MP1、MP2、MP3、MP4、MP5、MP6 | — |
| Part 1(e)(i) | 9618_s25_41:1(e)(i) | 2 | 代码 | `test_1ce_screenshot` · MP1、MP2 | — |
| Part 1(e)(ii) | 9618_s25_41:1(e)(ii) | 1 | 截图 | `test_1ce_screenshot` · 整行 | — |

自动测分值 20.000000，人工核对分值 0.000000，自动占比 100.00%。这是验证覆盖口径，自动测试不为未实际核对的写法授分。

## 人工核对清单


- [ ] 所有模块头、参数个数与顺序、全局 / 局部作用域符合 QP；所有 list 的类型与大小有英文注释；没有用内置函数替代题目要求的算法（D10 ③）。
- [ ] 给定伪代码的整体流程、没有多余代码、打开与关闭文件位置，由导师按本题 MS 看代码核对。行为正确不替代这些检查。
- [ ] 截图清晰、输入与规定的输出可见；自动测试只验证输出内容，不验证图片本身。

## 原页、编号与差异记录

已看 QP pp.2–3、MS pp.7–17 全部渲染图（含 p.17 延续的截图），核对 evidence.doc 6 格。MS Python 1(c) 循环名 X 而 print 用 x，参考解统一 X；声明加类型和大小注释；其余采用 MS Python 算法，无算法边界偏离。1(c) MS 第二个圆点同时印两个行为句，语料拆为 MP2（selection）与 MP3（output），对应同一印刷圆点，D37 ②；其余圆点顺序相同。无本题数据文件，卷首七个文件仅属第2题，不复制。
