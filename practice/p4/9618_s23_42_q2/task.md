# 9618_s23_42 第 2 题 · 销售记录循环队列

## 导读

本练习覆盖 7 个小问，共 28 分。从空白程序完成整道大题；可用 `make try EX=practice/p4/9618_s23_42_q2 K=2b` 按小问测试。标识符、指针初值与文件名照抄 QP（D10）；数组必须建立固定长度的真实 list，并用英文注释写明大小与类型。算法自行编写循环与指针操作，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳。

主程序放在 `if __name__ == "__main__":` 下，避免导入时运行输入；提示写在 `input("…")` 里（D13）。测试通过与人工清单通过之后才能记录掌握（D3）。

## Python 接口

`SaleData(SaleIDp, Quantityp)` 建记录，公开字段 `SaleID`、`Quantity`（本题是记录，不要求私有属性）。`Enqueue(RecordToAdd)` 返回 1 / -1；`Dequeue()` 返回记录，空时可为 None 或 `SaleData("", -1)`；`EnterRecord()` 输入 ID、整数数量并输出 QP 指定的 Stored / Full。全局 `CircularQueue`、`Head`、`Tail`、`NumberOfItems`。最后按数组下标顺序输出五条记录，而不是从 Head 开始的逻辑队列顺序（QP 写 array CircularQueue；MS 图也按下标输出）。

## 英文原题（QP 原页转写）

```text
2   A business sells a single product. Customers can purchase one or more of this product.

    Each sale has an ID and a quantity, for example "ABC" and 2

    The business needs a program to store the data about the sales in a circular queue data structure.

    (a) Write program code to declare a record structure, SaleData, to store the data about each
        sale.

 Save your program as Question2_J2023.

 Copy and paste the program code into part 2(a) in the evidence document.
                                                                                                   [2]

    (b) Write program code to:

         •     declare a global array, CircularQueue, of 5 items to store the sale records
         •     declare the global pointers Head and Tail
         •     declare the global variable NumberOfItems
         •     initialise all elements of the array CircularQueue to an empty record, where the ID is
               null ("") and quantity is -1
         •     initialise Head, Tail and NumberOfItems to 0

 Save your program.

 Copy and paste the program code into part 2(b) in the evidence document.
                                                                                                   [4]

    (c) The function Enqueue():

         •     takes a new record as a parameter
         •     inserts the record in the circular queue at the element pointed to by Tail
         •     updates pointers and other variables as required
         •     returns −1 if the circular queue is full
         •     returns 1 if the record is stored successfully.

         Write program code for the function Enqueue().

 Save your program.

 Copy and paste the program code into part 2(c) in the evidence document.
                                                                                                   [6]

(d) The function Dequeue():

         •     returns a null or empty record if the circular queue is empty
         •     returns the first record in the queue if the circular queue is not empty
         •     updates pointers and other variables as required.

         Write program code for the function Dequeue().

 Save your program.

 Copy and paste the program code into part 2(d) in the evidence document.
                                                                                          [6]

    (e) The procedure EnterRecord():

         •     takes an ID and quantity as input and creates a sale record
         •     uses Enqueue() to insert the record in the circular queue
         •     outputs "Full" if the record was not inserted in the circular queue
         •     outputs "Stored" if the record was inserted in the circular queue.

         Write program code for the procedure EnterRecord().

 Save your program.

 Copy and paste the program code into part 2(e) in the evidence document.
                                                                                          [5]

(f)   The following sale records need to be entered into the program:

                                             ID             Quantity
                                            ADF                    10
                                            OOP                    1
                                           BXW                     5
                                            XXZ                    22
                                            HQR                    6
                                            LLP                    3


          (i)    Amend the main program to:

                 •   use EnterRecord() to input the six records in the table
                 •   use Dequeue() to remove one record
                 •   output either the ID and quantity of the removed record, or an error message if the
                     circular queue is empty
                 •   use EnterRecord() to input the record with the ID "LLP" for a second time
                 •   output the ID and quantity for all the records currently stored in the array
                     CircularQueue.

                 Write program code to perform these tasks.

 Save your program.

 Copy and paste the program code into part 2(f)(i) in the evidence document.
                                                                                                     [4]

          (ii)   Test your program.

                 Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 2(f)(ii) in the evidence document.
                                                                                                     [1]
```

## 证据文档对照表

已逐格核对官方 evidence.doc；一格一行。MP 编号均为语料 `markpoints[].n`（D37 ②）。一个 MP 同时含函数头与行为时，行为列自动，函数头仍须人工核对；只考结构的 MP 全部列人工。可选点超过行分时，按 `行分 × 自动点分 / 全部点分` 折算，不表示真实考试逐点授分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a) | 9618_s23_42:2(a) | 2 | 代码 | `test_2a_record` · MP2 | MP1；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 2(b) | 9618_s23_42:2(b) | 4 | 代码 | `test_2b_initial_state`、`test_2b_no_algorithm_shortcuts` · MP1、MP2、MP3、MP4 | — |
| Part 2(c) | 9618_s23_42:2(c) | 6 | 代码 | `test_2c_enqueue_full_wrap` · MP2、MP3、MP4、MP5、MP6 | MP1；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 2(d) | 9618_s23_42:2(d) | 6 | 代码 | `test_2d_dequeue_empty_fifo_reuse` · MP2、MP3、MP4、MP5、MP6 | MP1；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 2(e) | 9618_s23_42:2(e) | 5 | 代码 | `test_2e_enter_record_stored_and_full`、`test_2f_main_call_chain` · MP2、MP3、MP4、MP5 | MP1；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 2(f)(i) | 9618_s23_42:2(f)(i) | 4 | 代码 | `test_2f_main_call_chain` · MP1、MP2、MP4、MP5 | MP3；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 2(f)(ii) | 9618_s23_42:2(f)(ii) | 1 | 截图 | `test_2f_screenshot` · MPwhole | — |

自动测分值 23.200000，人工核对分值 4.800000，自动占比 82.86%。这是验证覆盖口径，自动测试不为未实际核对的写法授分。

## 人工核对清单

- [ ] 9618_s23_42:2(f)(i) MP3：按同题 MS 查看消息语义及未触发的选择分支；不由固定输出推定。

- [ ] 9618_s23_42:2(a) MP1：Record declaration named SaleData // class declaration (and end) named SaleData…（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s23_42:2(c) MP1：Function Enqueue() header (and end) taking one parameter (type SaleData)（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s23_42:2(d) MP1：Function header Dequeue() (and end where appropriate)（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s23_42:2(e) MP1：Procedure header EnterRecord (and end where appropriate) (ignore parameters)（1 分；人工核对代码结构 / 声明）。
- [ ] 所有模块头、参数个数与顺序、全局 / 局部作用域符合 QP；所有 list 的类型与大小有英文注释；没有用内置函数替代题目要求的算法（D10 ③）。
- [ ] 给定伪代码的整体流程、没有多余代码、打开与关闭文件位置，由导师按本题 MS 看代码核对。行为正确不替代这些检查。
- [ ] 截图清晰、输入与规定的输出可见；自动测试只验证输出内容，不验证图片本身。

## 原页、编号与差异记录

已看 QP pp.5–7、MS pp.11–22 全部渲染图，核对 evidence.doc 7 格。MS Python EnterRecord 未 int 转换，参考解按 QP 数量整数及 MP2 修正；其他逻辑贴近 MS。MS 2(f)(i) 五个可选点 max4，自动/人工按比例折算；2(f)(ii) 为整行1分。没有 MS 印号 / 语料编号差异。无源数据文件。

## T38c2 · D46 验证补充

补测六次 EnterRecord → Dequeue → 第七次 EnterRecord 及记录参数、状态、返回记录输出；ID/数量允许说明和换行（QP p.7/MS pp.20/22）。固定输入不触发空记录分支，MP3 的空分支归人工补核。

本次行为覆盖：自动 23.200000 分、人工 4.800000 分（82.86%）。调用测试不能代替类型注释、代码结构及证据截图的人工检查。
