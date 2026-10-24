# 9618_w25_41 第 1 题 · 随机整数栈与弹栈求极值

覆盖 7 行，共 20 分。QP 原页：[2, 3]；MS 原页：[6, 7, 8, 9, 10, 11, 12, 13, 14]，已逐页渲染核对。证据格另对照官方 evidence.doc。

## 导读

从 starter.py 的空白分节开始写；标识符、文件名照题目。数组必须建出真实 list，并以英文注释注明类型与大小（D10 ①）；指针初值照题目（D10 ②）。排序、查找及 ADT 操作自己写循环，不用 `sort()`、`sorted()`、`index()`、`max()`、`min()` 或成员测试 `in` 代劳（D10 ③）。主程序置于 `if __name__ == "__main__":` 下，以便测试导入；提示语写在 `input("…")` 中。

## 英文原题（QP 原页转写）

```text
You have been supplied with the following source files:

HashTableData.txt

Open the evidence document, evidence.doc

Make sure that your name, centre number and candidate number will appear on every page of this
document. This document must contain your answers to each question.

Save this evidence document in your work area as:

evidence_ followed by your centre number_candidate number, for example: evidence_zz999_9999

A class declaration can be used to declare a record. If the programming language used does not
support arrays, a list can be used instead.

One source file is used to answer Question 3. The file is called HashTableData.txt

1      A program stores integers in a stack. The stack is represented as a 1D array of 30 elements with
       the identifier Stack

       The global pointer TopOfStack stores the index of the last element inserted into the stack.
       TopOfStack is initialised to –1

       (a) Write program code to declare Stack, initialise each element in the array with a null value
           and declare and initialise TopOfStack

    Save your program as Question1_N25.

    Copy and paste the program code into part 1(a) in the evidence document.
                                                                                                         [2]

       (b) The function Push() takes an integer parameter. If the stack is full, the function returns
           FALSE. If the stack is not full, the parameter is inserted into the stack, the pointer is updated
           and the function returns TRUE

           Write the program code for Push()

    Save your program.

    Copy and paste the program code into part 1(b) in the evidence document.
                                                                                                         [4]






    (c) The function Pop() returns the next integer in the stack and updates the pointer as
        appropriate. If there is no data in the stack, the function returns the value –999

          Write program code for Pop()

 Save your program.

 Copy and paste the program code into part 1(c) in the evidence document.
                                                                                                     [4]

    (d) The main program generates 40 random integers between 0 and 1000 (inclusive) and attempts
        to insert each one into the stack using the appropriate function. If the return value from the
        function call indicates the stack is full, no more integers are generated and "Stack full" is
        output.

          Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 1(d) in the evidence document.
                                                                                                     [4]

    (e) The procedure FindValues():

          •      pops each integer from the stack until the stack is empty
          •      finds and outputs the largest number that was in the stack in an appropriate message
          •      finds and outputs the smallest number that was in the stack in an appropriate message.

          Write program code for FindValues()

 Save your program.

 Copy and paste the program code into part 1(e) in the evidence document.
                                                                                                     [4]

    (f)   (i)    Extend the main program to call FindValues()

 Save your program.

 Copy and paste the program code into part 1(f)(i) in the evidence document.
                                                                                                     [1]

          (ii)   Test your program.

                 Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot(s) into part 1(f)(ii) in the evidence document.
                                                                                                     [1]
```

## Python 接口与测试约定

- 全局 `Stack` 为 30 格，null 用 Python 的 None；`TopOfStack=-1` 指向最后一次入栈的位置。`Push(DataToPush)` 返回布尔值，`Pop()` 返回整数或 -999，`FindValues()` 输出最大、最小值。
- 主程序通过 Python random 模块产生随机数；脚本包装器先设 seed，再运行完整程序并记录 Push 调用。测试比较本次生成的前 30 个数的实际极值，不硬编码某个随机序列，也不要求使用 randint 而排斥等价实现。
- 40 次是循环上限；容量 30，所以第 31 次 Push 首次失败后停止，Stack full 只出现一次。40 次上限本身人工核对。
- FindValues 测试覆盖至少一个数的栈；QP 未定义空栈求极值的输出，不测该情况。极值输出顺序不限，说明措辞人工核对。
- 本卷 HashTableData.txt 属于第 3 题，本练习无数据文件。

## 证据文档对照表

表内 MP 号取语料 markpoints[].n。每行列出自动与人工主归属；类型注释、函数头和截图可读性仍须人工核对。自动占比只统计可观察行为，并非自动给出考试分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_w25_41:1(a) | 2 | 代码 | `test_1a_null_array_last_used_pointer` · MP1、MP2 | — |
| Part 1(b) | 9618_w25_41:1(b) | 4 | 代码 | `test_1b_capacity_and_boolean` · MP1、MP2、MP3、MP4 | — |
| Part 1(c) | 9618_w25_41:1(c) | 4 | 代码 | `test_1c_pop_lifo_empty_reuse` · MP1、MP2、MP3、MP4 | — |
| Part 1(d) | 9618_w25_41:1(d) | 4 | 代码 | `test_1f_ii_screenshot_stack_full_and_extrema` · MP2、MP3、MP4 | MP1 Looping 40 times |
| Part 1(e) | 9618_w25_41:1(e) | 4 | 代码 | `test_1e_find_values_uses_pop` · MP1、MP2、MP3、MP4 | — |
| Part 1(f)(i) | 9618_w25_41:1(f)(i) | 1 | 代码 | `test_1f_ii_screenshot_stack_full_and_extrema` · MPwhole | — |
| Part 1(f)(ii) | 9618_w25_41:1(f)(ii) | 1 | 截图 | `test_1f_ii_screenshot_stack_full_and_extrema` · MPwhole | — |

## 人工核对清单

- [ ] 1(d) MP1：Looping 40 times
- [ ] 数组、指针与记录字段的英文类型注释及作用域正确，数组大小与 QP 一致。
- [ ] 按 QP 写指定算法；没有以内置容器操作代替数组 ADT 或查找、排序步骤。
- [ ] 所有截图清晰；输入、输出和要求的文件名可见；截图不能仅由 pytest 成功代替。
- [ ] 1(b) MP1、1(c) MP1、1(e) MP1 均混有模块头；自动测返回/输出行为，模块头与提示含义人工核对。
- [ ] 1(d) MP2：随机区间含 0 与 1000；seed 测试仅能检验采样落在范围内，边界生成方式需人工核对。

## QP / MS 差异与点号对照

- 本题 Python 范例与 QP 在被测情况下一致；无 Python 范例修正。
- MS p.11 VB.NET 随机上限写 RandomNumber.Next(0, 1000)，与 QP 的含 1000 不同；参考解使用含上界的 randint(0, 1000)。

1(d) MS p.11 把调用与失败退出写在一个圆点及续文中，语料拆为 MP3 / MP4，各 1 分；MP1=40 次循环上限，MP2=随机范围。其余顺序与圆点一致。
