# 9618_s22_41 第 3 题 · 循环队列

## 导读

本练习覆盖 5 个小问，共 21 分。从空白程序完成整道大题；可用 `make try EX=practice/p4/9618_s22_41_q3 K=3b` 按小问测试。标识符、指针初值与文件名照抄 QP（D10）；数组必须建立固定长度的真实 list，并用英文注释写明大小与类型。算法自行编写循环与指针操作，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳。

主程序放在 `if __name__ == "__main__":` 下，避免导入时运行输入；提示写在 `input("…")` 里（D13）。测试通过与人工清单通过之后才能记录掌握（D3）。

## Python 接口

采用 MS Python 的显式状态返回接口：`Enqueue(Queue, Head, Tail, NumItems, InputData)` 返回 `(成功布尔值, Queue, Head, Tail, NumItems)`；`Dequeue(Queue, Head, Tail, NumItems)` 返回 `(出队字符串, Queue, Head, Tail, NumItems)`。空队列按 QP 返回字符串 `"FALSE"`。全局声明名用 MS 的 `QueueArray`、`QueueHeadPointer`、`QueueTailPointer`、`NumberOfItems`。每次调用都接回全部返回值；Python 整数参数不能直接实现 ByRef。空元素字符串的具体内容不测。

3(d) 的状态提示可自行措辞，允许每次消息包含不同输入值；是否正确表达成功/失败由导师人工核对。测试观察真实调用，并按顺序查找返回的 A、B，不限制总行数。

## 英文原题（QP 原页转写）

```text
3   A program uses a circular queue to store strings. The queue is created as a 1D array, QueueArray,
    with 10 string items.

    The following data is stored about the queue:

    •    the head pointer initialised to 0
    •    the tail pointer initialised to 0
    •    the number of items in the queue initialised to 0.

    (a) Declare the array, head pointer, tail pointer and number of items.

    If you are writing in Python, include attribute declarations using comments.

 Save your program as Question3_J2022.

 Copy and paste the program code into part 3(a) in the evidence document.
                                                                                                  [2]

(b) The function Enqueue is written in pseudocode. The function adds DataToAdd to the queue.
        It returns FALSE if the queue is full and returns TRUE if the item is added.

         The function is incomplete, there are five incomplete statements.

FUNCTION Enqueue(BYREF QueueArray[] : STRING, BYREF HeadPointer : INTEGER,
                 BYREF TailPointer : INTEGER, NumberItems : INTEGER,
                 DataToAdd : STRING) RETURNS BOOLEAN

  IF NumberItems = …………………………………… THEN

     RETURN ……………………………………

  ENDIF

  QueueArray[……………………………………]                           ← DataToAdd
  IF TailPointer >= 9 THEN

     TailPointer      ← ……………………………………
  ELSE

     TailPointer      ← TailPointer + 1
  ENDIF

  NumberItems     ← NumberItems ……………………………………
  RETURN TRUE

ENDFUNCTION

         Write program code for the function Enqueue().

 Save your program.

 Copy and paste the program code into part 3(b) in the evidence document.
                                                                                              [7]

    (c) The function Dequeue() returns "FALSE" if the queue is empty, or it returns the next data
        item in the queue.

         Write program code for the function Dequeue().

 Save your program.

 Copy and paste the program code into part 3(c) in the evidence document.
                                                                                              [6]

(d) (i)     Amend the main program to:

                •   take as input 11 string values from the user
                •   use the Enqueue() function to add each element to the queue
                •   output an appropriate message to state whether each addition was successful, or
                    not
                •   call Dequeue() function twice and output the return value each time.

 Save your program.

 Copy and paste the program code into part 3(d)(i) in the evidence document.
                                                                                                [5]

         (ii)   Test your program with the input data:

                       "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K"

                Take a screenshot to show the output.

 Copy and paste the screenshot into part 3(d)(ii) in the evidence document.
                                                                                                [1]
```

## 证据文档对照表

已逐格核对官方 evidence.doc；一格一行。MP 编号均为语料 `markpoints[].n`（D37 ②）。一个 MP 同时含函数头与行为时，行为列自动，函数头仍须人工核对；只考结构的 MP 全部列人工。可选点超过行分时，按 `行分 × 自动点分 / 全部点分` 折算，不表示真实考试逐点授分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_s22_41:3(a) | 2 | 代码 | `test_3a_initial_state` · MP1、MP2 | — |
| Part 3(b) | 9618_s22_41:3(b) | 7 | 代码 | `test_3b_enqueue_full_and_wrap`、`test_3bc_reuse_slots_after_dequeue`、`test_3b_no_algorithm_shortcuts` · MP1 | MP2、MP3；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 3(c) | 9618_s22_41:3(c) | 6 | 代码 | `test_3c_dequeue_fifo_empty_and_wrap`、`test_3bc_reuse_slots_after_dequeue` · MP2、MP3、MP4、MP5、MP6、MP7 | MP1；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 3(d)(i) | 9618_s22_41:3(d)(i) | 5 | 代码 | `test_3d_main_call_chain` · MP1、MP2、MP4、MP5 | MP3；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 3(d)(ii) | 9618_s22_41:3(d)(ii) | 1 | 截图 | 行为辅助测试（不计自动分） | MPwhole；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |

自动测分值 16.142857，人工核对分值 4.857143，自动占比 76.87%。这是验证覆盖口径，自动测试不为未实际核对的写法授分。

## 人工核对清单

- [ ] 9618_s22_41:3(d)(ii) MPwhole：本次归人工，按同题 MS 核对适当消息或固定主程序未覆盖的分支。

- [ ] 9618_s22_41:3(d)(i) MP3：按同题 MS 查看消息语义及未触发的选择分支；不由固定输出推定。

- [ ] 9618_s22_41:3(b) MP2：1 mark for function heading and end, dealing with ByRef（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s22_41:3(b) MP3：1 mark for remainder of function correct and following the logic（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s22_41:3(c) MP1：Function header and end（1 分；人工核对代码结构 / 声明）。
- [ ] 所有模块头、参数个数与顺序、全局 / 局部作用域符合 QP；所有 list 的类型与大小有英文注释；没有用内置函数替代题目要求的算法（D10 ③）。
- [ ] 给定伪代码的整体流程、没有多余代码、打开与关闭文件位置，由导师按本题 MS 看代码核对。行为正确不替代这些检查。
- [ ] 截图清晰、输入与规定的输出可见；自动测试只验证输出内容，不验证图片本身。

## 原页、编号与差异记录

QP pp.8–10、MS pp.27–34 全部渲染图已读，evidence.doc 第 3 题 5 格已核。MS 3(c) Python 原图 p.30 印 `false`、`Queue(Head)` 以及先加一后 `Head >= 9`，参考解改为 QP 的 `"FALSE"`、`Queue[Head]`、`Head > 9`；后者符合同页得分句 more than 9，不跳过第十个元素（D31）。3(b) 语料 MP1 是五处填空合计 5 分，不拆成五个自造点号；MP2 是函数头 / ByRef、MP3 是 remainder / following logic，归人工。MS 未印独立 MP 数字，其余按清单顺序，无 D37 编号差异。与 s22_43 第 3 题整题相同，不重复创建。

## T38c2 · D46 验证补充

补测 11 次 Enqueue 的输入参数/返回状态与 2 次 Dequeue；移除 13 行及状态文字完全相同的额外限制（QP p.10/MS pp.32/34）。合适消息语义及按返回值选择消息改列人工补核。 截图的适当消息语义不可自动判别，截图整行列人工，A/B 输出测试作为行为辅助。

本次行为覆盖：自动 16.142857 分、人工 4.857143 分（76.87%）。调用测试不能代替类型注释、代码结构及证据截图的人工检查。
