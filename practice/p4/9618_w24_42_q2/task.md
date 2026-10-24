# 9618_w24_42 第 2 题 · 记录结构线性队列

覆盖 9 行，共 29 分。QP 原页：[8, 9, 10, 11]；MS 原页：[18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]，已逐页渲染核对。证据格另对照官方 evidence.doc。

## 导读

从 starter.py 的空白分节开始写；标识符、文件名照题目。数组必须建出真实 list，并以英文注释注明类型与大小（D10 ①）；指针初值照题目（D10 ②）。排序、查找及 ADT 操作自己写循环，不用 `sort()`、`sorted()`、`index()`、`max()`、`min()` 或成员测试 `in` 代劳（D10 ③）。主程序置于 `if __name__ == "__main__":` 下，以便测试导入；提示语写在 `input("…")` 中。

## 英文原题（QP 原页转写）

```text
2      A linear queue data structure is designed using a record structure.

       The record structure Queue has the following fields:

       •   QueueArray, a 1D array of up to 100 integer values
       •   Headpointer, a variable that stores the index of the first data item in QueueArray
       •   Tailpointer, a variable that stores the index of the next free location in QueueArray.

       (a) Write program code to declare the record structure Queue and its fields.

           If your programming language does not support record structures, a class can be declared
           instead.

           If you are writing in Python, use comments to declare the appropriate data types.

    Save your program as Question2_N24.

    Copy and paste the program code into part 2(a) in the evidence document.
                                                                                                        [3]

       (b) The main program creates a new Queue record with the identifier TheQueue. The head
           pointer is initialised to –1. The tail pointer is initialised to 0. Each element in the array is
           initialised with –1.

           Write program code for the main program.

    Save your program.

    Copy and paste the program code into part 2(b) in the evidence document.
                                                                                                        [3]

(c) The pseudocode function Enqueue() inserts an integer value into the queue.

         The function is incomplete. There are three incomplete statements.

         FUNCTION Enqueue(BYREF AQueue : Queue, BYVAL TheData : INTEGER)
                          RETURNS INTEGER

               IF AQueue.Headpointer = -1 THEN

                 AQueue.QueueArray[AQueue.Tailpointer]                    ← ........................................
                 AQueue.Headpointer  ←0
                  AQueue.Tailpointer ← AQueue.Tailpointer + 1

                  RETURN 1

               ELSE

                  IF AQueue.Tailpointer > ........................................ THEN

                       RETURN -1

                  ELSE

                       AQueue.QueueArray[AQueue.Tailpointer]                   ← TheData
                       AQueue.Tailpointer         ← AQueue.Tailpointer ........................................
                       RETURN 1

                  ENDIF

               ENDIF

         ENDFUNCTION

         Write program code for Enqueue().

 Save your program.

 Copy and paste the program code into part 2(c) in the evidence document.
                                                                                                                       [5]

    (d) The function ReturnAllData() accesses TheQueue. It concatenates all the integer
        values that have been inserted into the queue’s array, starting from the value stored at
        HeadPointer, with a space between each integer value. The string of concatenated values
        is returned.

         None of the integer values are removed from the queue.

         Write program code for ReturnAllData().

 Save your program.

 Copy and paste the program code into part 2(d) in the evidence document.
                                                                                                                       [3]

(e) (i)      The main program asks the user to enter 10 integers with values of 0 or greater. It reads
                 each input repeatedly until a valid number is entered.

                 All 10 valid inputs are added to the queue, using Enqueue().

                 If the value returned from Enqueue() is –1, a message is output to state that the queue
                 is full, otherwise a message is output to state that the item has been added to the queue.

                 The function ReturnAllData() is called once all 10 integers have been entered and
                 the return value from the function call is output.

                 Amend the main program to perform these actions.

 Save your program.

 Copy and paste the program code into part 2(e)(i) in the evidence document.
                                                                                                        [5]

          (ii)   Test your program with the following inputs in the order given:

                       10     9     –1     8     7     6         5   4   3     2     1

                 Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 2(e)(ii) in the evidence document.
                                                                                                        [2]

    (f)   The function Dequeue() accesses TheQueue. The function returns –1 if the queue is empty.
          If the queue is not empty, the function returns the next item in the queue and updates the
          relevant pointer(s).

          The data is not replaced or deleted from the queue.

          Write program code for Dequeue().

 Save your program.

 Copy and paste the program code into part 2(f) in the evidence document.
                                                                                                        [4]

    (g) (i)      The main program calls Dequeue() twice, and each time it either outputs ‘Queue empty’
                 if there is no data in the queue or outputs the return value.

                 The main program then calls ReturnAllData() a second time.

                 Amend the main program.

 Save your program.

 Copy and paste the program code into part 2(g)(i) in the evidence document.
                                                                                                        [3]

(ii)   Test your program with the following inputs in the order given:

                         10      9     8     7      6        5    4   3   2       1

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 2(g)(ii) in the evidence document.
                                                                                             [1]
```

## Python 接口与测试约定

- `Queue()` 创建记录对象；字段 `QueueArray` 为 100 格真实 list。指针字段兼容 QP 的 `Headpointer` / `Tailpointer` 及 MS 的 `HeadPointer` / `TailPointer`。
- `Enqueue(AQueue, TheData)`、`Dequeue(AQueue)` 可照 MS 返回 `(AQueue, status_or_data)`，也可直接修改对象并返回整数；测试兼容。`ReturnAllData(TheQueue)` 可显式传对象，也可无参数访问全局 TheQueue。Enqueue/Dequeue 同样兼容 MS Java 风格只传数据/无参数而访问全局对象。
- 2(b) 的初始化既可写在构造方法，也可写在主程序。脚本测试在首次 Enqueue 调用前观察对象，不限制初始化位置。
- 提示语与说明文字不限，但每次入队有结果消息；ReturnAllData 返回数字间以一个空格分隔的字符串，允许首尾空白。整数输入校验只测试负数与 0，不自行加入 QP 未明确要求的非整数字符串测试。
- 无数据文件。

## 证据文档对照表

表内 MP 号取语料 markpoints[].n。每行列出自动与人工主归属；类型注释、函数头和截图可读性仍须人工核对。自动占比只统计可观察行为，并非自动给出考试分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a) | 9618_w24_42:2(a) | 3 | 代码 | `test_2a_record_array` · MP2 | MP1 Record structure or class with constructor Queue (and end where appropriate) …；MP3 … containing HeadPointer and TailPointer as integers |
| Part 2(b) | 9618_w24_42:2(b) | 3 | 代码 | `test_2b_record_initialised_before_enqueue` · MP1、MP2、MP3 | — |
| Part 2(c) | 9618_w24_42:2(c) | 5 | 代码 | `test_2c_enqueue_first_and_capacity` · MP1、MP2 | MP3 1 mark for function header taking (at least) one parameter and the rest of function correct and using the record/class data structure accurately. |
| Part 2(d) | 9618_w24_42:2(d) | 3 | 代码 | `test_2d_all_data_without_removing` · MP1、MP2、MP3 | — |
| Part 2(e)(i) | 9618_w24_42:2(e)(i) | 5 | 代码 | `test_2e_2g_main_call_chain` + 原有输出测试 · MP1、MP2、MP3、MP5 | MP4：消息语义 / 未触发分支按同题 MS 核对 |
| Part 2(e)(ii) | 9618_w24_42:2(e)(ii) | 2 | 截图 | `test_2e_ii_screenshot_rejects_negative` · MP1、MP2 | — |
| Part 2(f) | 9618_w24_42:2(f) | 4 | 代码 | `test_2f_dequeue_fifo_preserves_cells` · MP1、MP2、MP3、MP4 | — |
| Part 2(g)(i) | 9618_w24_42:2(g)(i) | 3 | 代码 | `test_2e_2g_main_call_chain` + 原有输出测试 · MP1、MP3 | MP2：消息语义 / 未触发分支按同题 MS 核对 |
| Part 2(g)(ii) | 9618_w24_42:2(g)(ii) | 1 | 截图 | `test_2g_ii_screenshot_two_returns` · MPwhole | — |

## 人工核对清单

- [ ] 9618_w24_42:2(g)(i) MP2：按同题 MS 查看消息语义及未触发的选择分支；不由固定输出推定。

- [ ] 9618_w24_42:2(e)(i) MP4：按同题 MS 查看消息语义及未触发的选择分支；不由固定输出推定。

- [ ] 2(a) MP1：Record structure or class with constructor Queue (and end where appropriate) …
- [ ] 2(a) MP3：… containing HeadPointer and TailPointer as integers
- [ ] 2(c) MP3：1 mark for function header taking (at least) one parameter and the rest of function correct and using the record/class data structure accurately.
- [ ] 数组、指针与记录字段的英文类型注释及作用域正确，数组大小与 QP 一致。
- [ ] 按 QP 写指定算法；没有以内置容器操作代替数组 ADT 或查找、排序步骤。
- [ ] 所有截图清晰；输入、输出和要求的文件名可见；截图不能仅由 pytest 成功代替。
- [ ] 2(e)(i) MP4 的队满消息、2(g)(i) MP2 的空队列消息：主程序正常十次输入不会进入这些分支，人工核对条件和输出含义。
- [ ] 2(c) MP3 要逐段核对题给伪代码结构；2(d) MP1、2(f) MP1 同时含函数头，头部人工复核。

## QP / MS 差异与点号对照

- MS p.18 Python 2(a) 的 HeadPointer/TailPointer 少 self.，只会创建局部变量；参考解按 p.19 完整范例修正为对象字段。
- MS p.26 Python Dequeue 条件使用单等号 `=`，不能运行；参考解修为 `==` 语义。
- 2(g)(ii) QP 测试串不含 -1，MS p.30 截图沿用含 -1 的 2(e)(ii) 串；自动测试分别用各自 QP 串，返回值同为 10、9。
- 2(c) QP 的三处空白保留，人工核对时用 MS p.20 的 TheData / 99 / + 1；Python 对象传参无需真的返回对象，但允许 MS 的双返回接口。

2(c) 语料 MP1=三处补全（3 分），MP2=返回值（1 分），MP3=模块头和其余结构（1 分）。不能把语料 MP1 当作单个 1 分点。其余点号与 MS 圆点顺序一致。

## T38c2 · D46 验证补充

补测 10 次有效 Enqueue（拒绝 -1）→ ReturnAllData → 两次 Dequeue → ReturnAllData；只保留 QP/MS 明定的一行队列格式，取消返回信息同一行、最终必须输出剩余数组的额外要求（QP pp.10–11/MS pp.23/26/28/30）。B 分行显示返回信息且只调用第二次 ReturnAllData；未触发的 full/empty 分支归人工。 自动/人工分类以本次复核后的证据表和 manifest 为准。截图清晰度与代码结构仍按人工清单核对。
