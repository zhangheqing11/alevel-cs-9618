# 9618_s25_43 第 1 题 · 文件线性队列求和

## 导读

本练习覆盖 6 个小问，共 26 分。从空白程序完成整道大题；可用 `make try EX=practice/p4/9618_s25_43_q1 K=1b` 按小问测试。标识符、指针初值与文件名照抄 QP（D10）；数组必须建立固定长度的真实 list，并用英文注释写明大小与类型。算法自行编写循环与指针操作，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳。

主程序放在 `if __name__ == "__main__":` 下，避免导入时运行输入；提示写在 `input("…")` 里（D13）。测试通过与人工清单通过之后才能记录掌握（D3）。

## Python 接口

`Queue` 五十整数，`HeadPointer`、`TailPointer` 初值 -1；`Enqueue(Data)` 返回布尔值，`Dequeue()` 空时整数 -1；`CreateQueue()` 无参读取 QueueData.txt。这是线性队列，不回绕。源文件每行一个正整数；不自行在接口中添加入队值校验。主程序按 QP 使用 Dequeue 逐个求和，测试通过运行时调用记录验证，不能直接 sum(Queue)。

## 英文原题（QP 原页转写）

```text
You have been supplied with the following source files:

QueueData.txt

Open the evidence document, evidence.doc

Make sure that your name, centre number and candidate number will appear on every page of this
document. This document must contain your answers to each question.

Save this evidence document in your work area as:
evidence_ followed by your centre number_candidate number, for example: evidence_zz999_9999

A class declaration can be used to declare a record. If the programming language used does not
support arrays, a list can be used instead.

One source file is used to answer Question 1. The file is called QueueData.txt

1   A program reads data from a text file and stores it in a queue. The linear queue Queue is stored as
    a 1D array of up to 50 elements. The queue has the following pointers:

    •    HeadPointer – this stores the index of the first element in the queue, initialised to –1
    •    TailPointer – this stores the index of the last element in the queue, initialised to –1

    (a) Queue is a global array of 50 integers with all elements initialised to –1 in the main program.

         The two pointers are declared as global variables and initialised to –1

         Write program code to declare and initialise Queue, HeadPointer and TailPointer

 Save your program as Question1_J25.

 Copy and paste the program code into part 1(a) in the evidence document.
                                                                                                    [3]

    (b) The function Enqueue():

         •     takes an integer parameter to store in the next position in the queue
         •     returns FALSE if the queue is full and the parameter cannot be stored in the queue
         •     returns TRUE if the parameter is stored in the queue
         •     updates the pointers where appropriate.

         Write program code for Enqueue()

 Save your program.

 Copy and paste the program code into part 1(b) in the evidence document.
                                                                                                    [6]

(c) The function Dequeue():

         •      returns the next item in the queue, if the queue is not empty
         •      returns –1 if the queue is empty
         •      updates the pointers where appropriate.

         Write program code for Dequeue()

 Save your program.

 Copy and paste the program code into part 1(c) in the evidence document.
                                                                                                   [5]

    (d) The text file QueueData.txt stores positive integers. Each integer is on a new line in the
        file.

         The procedure CreateQueue():

         •      opens the file QueueData.txt
         •      reads in each line from the text file and uses Enqueue() to insert each line into the
                queue
         •      outputs "Queue full" if any item cannot be inserted into the queue
         •      uses exception handling when opening and reading from the text file.

         The procedure needs to work for a file that contains an unknown number of lines.

         Write program code for CreateQueue()

 Save your program.

 Copy and paste the program code into part 1(d) in the evidence document.
                                                                                                   [6]

    (e) (i)     The main program needs extending to call CreateQueue(). The main program then
                adds together all of the integers stored in the queue, using Dequeue() to access each
                integer. The total is then output.

                Write program code to extend the main program.

 Save your program.

 Copy and paste the program code into part 1(e)(i) in the evidence document.
                                                                                                   [5]

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
| Part 1(a) | 9618_s25_43:1(a) | 3 | 代码 | `test_1a_initial_state` · MP1、MP2、MP3 | — |
| Part 1(b) | 9618_s25_43:1(b) | 6 | 代码 | `test_1b_enqueue_full` · MP2、MP3、MP4、MP5、MP6 | MP1 |
| Part 1(c) | 9618_s25_43:1(c) | 5 | 代码 | `test_1c_dequeue_fifo_empty` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 1(d) | 9618_s25_43:1(d) | 6 | 代码 | `test_1d_official_file`、`test_1d_unknown_length_overflow_and_missing` · MP2、MP3、MP4、MP5、MP6 | MP1 |
| Part 1(e)(i) | 9618_s25_43:1(e)(i) | 5 | 代码 | `test_1e_screenshot`、`test_1e_main_uses_dequeue_until_sentinel` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 1(e)(ii) | 9618_s25_43:1(e)(ii) | 1 | 截图 | `test_1e_screenshot` · 整行 | — |

自动测分值 24.000000，人工核对分值 2.000000，自动占比 92.31%。这是验证覆盖口径，自动测试不为未实际核对的写法授分。

## 人工核对清单

- [ ] 9618_s25_43:1(b) MP1：Function Enqueue() header (and end) taking one (integer) parameter（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s25_43:1(d) MP1：CreateQueue() header (and end) and opening the file to read and closing file in appropriate place（1 分；人工核对代码结构 / 声明）。
- [ ] 所有模块头、参数个数与顺序、全局 / 局部作用域符合 QP；所有 list 的类型与大小有英文注释；没有用内置函数替代题目要求的算法（D10 ③）。
- [ ] 给定伪代码的整体流程、没有多余代码、打开与关闭文件位置，由导师按本题 MS 看代码核对。行为正确不替代这些检查。
- [ ] 截图清晰、输入与规定的输出可见；自动测试只验证输出内容，不验证图片本身。

## 原页、编号与差异记录

已看 QP pp.2–3、MS pp.7–18 全部渲染图，核对 evidence.doc 6 格。MS p.18 截图3059，官方文件运行一致。MS Python CreateQueue 在第一次满时 break；参考解继续读到 EOF，符合 QP 每行调用和未知行数要求，测试允许满提示一次或多次（MS MP5 明文）。MP1只考函数头与文件打开/关闭位置，归人工；MP6行为测缺文件，所有访问是否在try仍人工核对。其余采用 MS Python，无给分编号差异。
