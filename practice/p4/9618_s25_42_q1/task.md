# 9618_s25_42 第 1 题 · 文件栈计算器

## 导读

本练习覆盖 7 个小问，共 27 分。从空白程序完成整道大题；可用 `make try EX=practice/p4/9618_s25_42_q1 K=1b` 按小问测试。标识符、指针初值与文件名照抄 QP（D10）；数组必须建立固定长度的真实 list，并用英文注释写明大小与类型。算法自行编写循环与指针操作，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳。

主程序放在 `if __name__ == "__main__":` 下，避免导入时运行输入；提示写在 `input("…")` 里（D13）。测试通过与人工清单通过之后才能记录掌握（D3）。

## Python 接口

接口 `Push(Data)` 返回整数 1 / -1，`Pop()` 返回字符串（空时 "-1"）；`ReadData(FileName)` 读取任意行数直到 EOF，并处理无法打开/读取的文件；`Calculate()` 通过 Pop 取出栈顶起的一串“数字、运算符、数字…”进行顺序计算。`Stack` 固定20格，`TopOfStack` 指最后一项，初值 -1。输入文件每行一项，先入栈后从文件末尾开始取出，别误当通常的中缀运算或后缀表达式。Calculate 只测试 QP 保证的非空、完整表达式，不测试未定义的空栈表达式、除零。

## 英文原题（QP 原页转写）

```text
You have been supplied with the following source files:

StackData.txt
SecondStack.txt
HashData.txt

Open the evidence document, evidence.doc

Make sure that your name, centre number and candidate number will appear on every page of this
document. This document must contain your answers to each question.

Save this evidence document in your work area as:
evidence_ followed by your centre number_candidate number, for example: evidence_zz999_9999

A class declaration can be used to declare a record. If the programming language used does not
support arrays, a list can be used instead.

Three source files are used to answer Questions 1 and 2. The files are called StackData.txt,
SecondStack.txt and HashData.txt

1   A program reads data from a text file and stores it in a stack. The stack Stack is stored as a 1D
    array of up to 20 elements. The pointer TopOfStack stores the index of the last element stored in
    the stack.

    (a) Stack is a global array of strings with all elements initialised to "-1"

         TopOfStack is a global variable initialised to –1

         Write program code to declare and initialise Stack and TopOfStack

 Save your program as Question1_J25.

 Copy and paste the program code into part 1(a) in the evidence document.
                                                                                                  [2]

    (b) The function Push() takes a string parameter and attempts to store it on the stack.

         The function returns –1 if the stack is full.

         The function returns 1 if the parameter is successfully pushed onto the stack.

         Write program code for Push()

 Save your program.

 Copy and paste the program code into part 1(b) in the evidence document.
                                                                                                  [4]

(c) The function Pop() returns the next item from the stack.

         The function returns "–1" if the stack is empty.

         Write program code for Pop()

 Save your program.

 Copy and paste the program code into part 1(c) in the evidence document.
                                                                                                   [4]

    (d) The text file StackData.txt stores numbers and mathematical operators. Each number
        and operator are on a new line in the text file.

         The mathematical operators used in this program are:

                                  mathematical
                                                          meaning
                                    operator
                                        +                   addition
                                         –               subtraction
                                         /                    division
                                         *             multiplication
                                         ^                power of

         The procedure ReadData():

         •     takes a string filename as a parameter
         •     opens the file and reads in each line of data
         •     uses the Push() function to insert each line of data onto the stack
         •     outputs "Stack full" if any data cannot be stored on the stack because the stack is
               full
         •     uses exception handling when opening and reading from the text file.

         The procedure needs to work for a file that contains an unknown number of lines.

         Write program code for ReadData()

 Save your program.

 Copy and paste the program code into part 1(d) in the evidence document.
                                                                                                   [6]

(e) The values stored in the stack are used to perform mathematical operations.

         A total is initialised to the first value in the stack. The first value in the stack will always be a
         number.

         The next value will be a mathematical operator and the next value will be the number to apply
         to the calculation. This is repeated until there are no values left in the stack. There will always
         be a number following a mathematical operator.

         For example, the contents of a stack are:

             10                         TopOfStack
             +
             3
             –
             2


         The total is initialised to the first value in the stack: 10

                  total = 10

         The next two values are: + 3

                  total = 10 + 3 = 13

         The next two values are: – 2

                  total = 13 – 2 = 11

         The final total is 11 and this is returned.

         Write program code for the function Calculate() to:

         •        take each value from the stack
         •        calculate and return the final total.

 Save your program.

 Copy and paste the program code into part 1(e) in the evidence document.
                                                                                                           [7]

(f)   (i)    Write program code to extend the main program to:

                 •   take a filename as input from the user
                 •   call ReadData() with the input filename
                 •   call Calculate()
                 •   output the final total.

 Save your program.

 Copy and paste the program code into part 1(f)(i) in the evidence document.
                                                                                      [2]

          (ii)   Test your program twice with the file names:

                 StackData.txt
                 SecondStack.txt

                 Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot into part 1(f)(ii) in the evidence document.
                                                                                      [2]
```

## 证据文档对照表

已逐格核对官方 evidence.doc；一格一行。MP 编号均为语料 `markpoints[].n`（D37 ②）。一个 MP 同时含函数头与行为时，行为列自动，函数头仍须人工核对；只考结构的 MP 全部列人工。可选点超过行分时，按 `行分 × 自动点分 / 全部点分` 折算，不表示真实考试逐点授分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_s25_42:1(a) | 2 | 代码 | `test_1a_initial_state` · MP1、MP2 | — |
| Part 1(b) | 9618_s25_42:1(b) | 4 | 代码 | `test_1b_push_full` · MP2、MP3、MP4；`test_1b_no_algorithm_shortcuts` · D10 写法检查 | MP1 |
| Part 1(c) | 9618_s25_42:1(c) | 4 | 代码 | `test_1c_pop_empty_lifo_reuse` · MP1、MP2、MP3、MP4 | — |
| Part 1(d) | 9618_s25_42:1(d) | 6 | 代码 | `test_1d_read_official_files`、`test_1d_overflow_and_missing_file` · MP2、MP3、MP4、MP5、MP6 | MP1 |
| Part 1(e) | 9618_s25_42:1(e) | 7 | 代码 | `test_1e_calculate_all_operators` · MP2、MP3、MP4、MP5、MP6、MP7 | MP1 |
| Part 1(f)(i) | 9618_s25_42:1(f)(i) | 2 | 代码 | `test_1f_screenshots` · MP1、MP2；`test_1f_main_call_chain` · 实际调用、参数与结果链 | — |
| Part 1(f)(ii) | 9618_s25_42:1(f)(ii) | 2 | 截图 | `test_1f_screenshots` · MP1、MP2 | — |

自动测分值 24.000000，人工核对分值 3.000000，自动占比 88.89%。这是验证覆盖口径，自动测试不为未实际核对的写法授分。

## 人工核对清单

- [ ] 9618_s25_42:1(b) MP1：Push function header (and end where appropriate) taking one (string) parameter（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s25_42:1(d) MP1：Procedure header (and end where appropriate) taking one (string) parameter（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s25_42:1(e) MP1：Calculate() function header (and end where appropriate)（1 分；人工核对代码结构 / 声明）。
- [ ] 所有模块头、参数个数与顺序、全局 / 局部作用域符合 QP；所有 list 的类型与大小有英文注释；没有用内置函数替代题目要求的算法（D10 ③）。
- [ ] 给定伪代码的整体流程、没有多余代码、打开与关闭文件位置，由导师按本题 MS 看代码核对。行为正确不替代这些检查。
- [ ] 截图清晰、输入与规定的输出可见；自动测试只验证输出内容，不验证图片本身。

## 原页、编号与差异记录

已看 QP pp.2–5、MS pp.7–18 全部渲染图，并核对 evidence.doc 7 格。QP p.4 栈图转写为顶到底 10、+、3、−、2，结果11；MS p.18 两次截图分别131.0、320.0，测试接受相同数值的整数/浮点显示。参考解采用 MS Python 顺序运算、Pop 取数；只收窄 bare except 为 OSError 并加英文类型注释、入口保护，无 QP/MS 算法冲突。MP 与印刷清单一致。HashData.txt 属第2题，不复制。

## T38c2 · D46 验证补充

F06：复现空壳主程序旧测试 17 passed；新增三份文件 ReadData(FileName) → Calculate → 返回值输出观测（含新数据 17），输出允许额外数字说明。复核 QP p.5、MS p.17 原页。 自动/人工分值口径不变；新增调用观测支持原表自动分类。截图清晰度与代码结构仍按人工清单核对。
