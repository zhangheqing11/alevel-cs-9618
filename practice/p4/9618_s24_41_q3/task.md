# 9618_s24_41 第 3 题 · 线性队列与校验位

## 导读

本练习覆盖 6 个小问，共 17 分。从空白程序完成整道大题；可用 `make try EX=practice/p4/9618_s24_41_q3 K=3b` 按小问测试。标识符、指针初值与文件名照抄 QP（D10）；数组必须建立固定长度的真实 list，并用英文注释写明大小与类型。算法自行编写循环与指针操作，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳。

主程序放在 `if __name__ == "__main__":` 下，避免导入时运行输入；提示写在 `input("…")` 里（D13）。测试通过与人工清单通过之后才能记录掌握（D3）。

## Python 接口

`QueueData` 二十格，`QueueHead = QueueTail = -1`；`Enqueue(DataToInsert)` 返回布尔值；`Dequeue()` 空时返回 QP 指定的小写字符串 `"false"`。这是线性队列，尾指针到 19 就满，不回绕。`StoreItems()` 无参，输入十条七字符数据，存入时去掉末尾校验位。最后一行计数报告含无效项数量，主程序再输出一次 Dequeue 结果或空队列提示。只测试 QP 定义的七字符格式（前六位数字），不替题目添加格式校验。

## 英文原题（QP 原页转写）

```text
3   A program reads data from the user and stores the data that is valid in a linear queue.

    The queue is stored as a global 1D array, QueueData, of string values. The array needs space for
    20 elements.

    The global variable QueueHead stores the index of the first element in the queue.
    The global variable QueueTail stores the index of the last element in the queue.

    (a) The main program initialises all the elements in QueueData to a suitable null value,
        QueueHead to −1 and QueueTail to −1.

         Write program code for the main program.

 Save your program as Question3_J24.

 Copy and paste the program code into part 3(a) in the evidence document.
                                                                                                         [1]

    (b) The function Enqueue() takes the data to insert into the queue as a parameter.

         If the queue is not full, it inserts the parameter in the queue, updates the appropriate pointer(s)
         and returns TRUE. If the queue is full, it returns FALSE.

         Write program code for Enqueue().

 Save your program.

 Copy and paste the program code into part 3(b) in the evidence document.
                                                                                                         [4]

    (c) The function Dequeue() returns "false" if the queue is empty. If the queue is not empty, it
        returns the next item in the queue and updates the appropriate pointer(s).

         Write program code for Dequeue().

 Save your program.

 Copy and paste the program code into part 3(c) in the evidence document.
                                                                                                         [3]

(d) The string values to be stored in the queue are 7 characters long. The first 6 characters are
        digits and the 7th character is a check digit. The check digit is calculated from the first 6 digits
        using this algorithm:

         •      multiply the digits in position 0, position 2 and position 4 by 1
         •      multiply the digits in position 1, position 3 and position 5 by 3
         •      calculate the sum of the products (add together the results from all of the multiplications)
         •      divide the sum of the products by 10 and round the result down to the nearest integer to
                get the check digit
         •      if the check digit equals 10 then it is replaced with 'X'.

         Example:

         Data is 954123

 Character position            0             1               2           3            4             5
 Digit                         9             5               4           1            2             3
 Multiplier                    1             3               1           3            1             3
 Product                       9            15               4           3            2             9

         Sum of products = 9 + 15 + 4 + 3 + 2 + 9 = 42

         Divide sum of products by 10: 42 / 10 = 4 (rounded down)

         The check digit = 4. This is inserted into character position 6.

         The data including the check digit is: 9541234

         A 7‑character string is valid if the 7th character matches the check digit for that data. For
         example, the data 9541235 is invalid because the 7th character (5) does not match the check
         digit for 954123.

          (i)   The subroutine StoreItems() takes ten 7‑character strings as input from the user and
                uses the check digit to validate each input.

                Each valid input has the check digit removed and is stored in the queue using
                Enqueue().
                An appropriate message is output if the item is inserted. An appropriate message is
                output if the queue is already full.

                Invalid inputs are not stored in the queue.

                The subroutine counts and outputs the number of invalid items that were entered.

                StoreItems() can be a procedure or a function as appropriate.

                Write program code for StoreItems().

 Save your program.

 Copy and paste the program code into part 3(d)(i) in the evidence document.
                                                                                                         [6]

(ii)   Write program code to amend the main program to:

                •   call StoreItems()
                •   call Dequeue()
                •   output a suitable message if the queue was empty
                •   output the returned value if the queue was not empty.

 Save your program.

 Copy and paste the program code into part 3(d)(ii) in the evidence document.
                                                                                 [1]

        (iii)   Test the program with the following inputs in the order given:

                    999999X
                    1251484
                    5500212
                    0033585
                    9845788
                    6666666
                    3258746
                    8111022
                    7568557
                    0012353


                Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot into part 3(d)(iii) in the evidence document.
                                                                                 [2]
```

## 证据文档对照表

已逐格核对官方 evidence.doc；一格一行。MP 编号均为语料 `markpoints[].n`（D37 ②）。一个 MP 同时含函数头与行为时，行为列自动，函数头仍须人工核对；只考结构的 MP 全部列人工。可选点超过行分时，按 `行分 × 自动点分 / 全部点分` 折算，不表示真实考试逐点授分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_s24_41:3(a) | 1 | 代码 | `test_3a_initial_state` · 整行 | — |
| Part 3(b) | 9618_s24_41:3(b) | 4 | 代码 | `test_3b_enqueue_linear_full` · MP1、MP2、MP3、MP4；`test_3b_no_algorithm_shortcuts` · D10 写法检查 | — |
| Part 3(c) | 9618_s24_41:3(c) | 3 | 代码 | `test_3c_dequeue_fifo_and_empty_string` · MP1、MP2、MP3 | — |
| Part 3(d)(i) | 9618_s24_41:3(d)(i) | 6 | 代码 | `test_3d_storeitems_official_sequence`、`test_3d_x_and_numeric_checks_at_full_queue` · MP1、MP2、MP3、MP4、MP5、MP6、MP7、MP8 | — |
| Part 3(d)(ii) | 9618_s24_41:3(d)(ii) | 1 | 代码 | `test_3d_screenshot`、`test_3d_main_empty_message` · 整行；`test_3d_main_call_chain` · 实际调用、参数与结果链 | — |
| Part 3(d)(iii) | 9618_s24_41:3(d)(iii) | 2 | 截图 | `test_3d_screenshot` · MP1、MP2 | — |

自动测分值 17.000000，人工核对分值 0.000000，自动占比 100.00%。这是验证覆盖口径，自动测试不为未实际核对的写法授分。

## 人工核对清单


- [ ] 所有模块头、参数个数与顺序、全局 / 局部作用域符合 QP；所有 list 的类型与大小有英文注释；没有用内置函数替代题目要求的算法（D10 ③）。
- [ ] 给定伪代码的整体流程、没有多余代码、打开与关闭文件位置，由导师按本题 MS 看代码核对。行为正确不替代这些检查。
- [ ] 截图清晰、输入与规定的输出可见；自动测试只验证输出内容，不验证图片本身。

## 原页、编号与差异记录

已看 QP pp.11–13、MS pp.29–38 全部渲染图，核对 evidence.doc 6 格。MS Python Enqueue 用 append 将数据放在预留20格后，改为 QueueData[QueueTail]；Dequeue 返回 False 与 QP / 得分句的字符串 false 不同，按 QP 修正；StoreItems 对不匹配的 X 可能执行 int("X")，改为先算期望校验字符后比较。保留 X 代表10的 QP算法，未擅自改成常见校验算法（D31）。3(d)(i) 八个可选点 max6，按分值折算；1分行按 whole，不编造点号。其余圆点顺序与语料一致。与 s24_43 第3题相同。

## T38c2 · D46 验证补充

补测 StoreItems → Dequeue 一次及返回项目输出；计数和项目输出不再固定倒数两行，允许相邻多行说明（QP p.13/MS pp.37–38）。 自动/人工分类以本次复核后的证据表和 manifest 为准。截图清晰度与代码结构仍按人工清单核对。
