# 9618_s23_41 第 1 题 · 读 25 个整数、输出数组、线性查找计数

来源：`9618_s23_41:1(a)(i)` – `9618_s23_41:1(d)(ii)`，8 行，18 分；QP pp.2–3，MS pp.4–11。题干已对照 QP 原页转写；MS 原页看过两个截图样例（pp.8、11），范例按 `ms_text` 核对（Python 范例很短，缩进不影响理解）。

## 导读

- 从空白的 `solution.py` 写起（`make try EX=practice/p4/9618_s23_41_q1` 会建好并把 `Data.txt` 复制到旁边），一问一问地测：`make try EX=practice/p4/9618_s23_41_q1 K=1c`。
- 标识符照抄题目（`DataArray`、`PrintArray`、`LinearSearch`、`Data.txt`）。数组建成真实的 25 个元素的 list，注释写明大小与类型（D10 ①；MS 范例写 `DataArray = [] #25 elements Integer` 再 `append`，MS 也给分，但按本系统口径请写 `[0] * 25`）。计数自己写循环，不用 `count()` 代劳（D10 ③）。
- 主程序**直接**写在 `if __name__ == "__main__":` 下面，不要再包进一个 `main()` 函数：`DataArray` 是主程序的局部数组，测试要在主程序运行完后读它。提示语写在 `input("…")` 里（D13）。
- `files/Data.txt` 是官方源文件原样副本：25 行整数，CRLF 行尾，最后一行 `0` 后面**没有**换行。读进来要转成整数（`type-conversion`），否则 `LinearSearch(DataArray, 12)` 一个也找不到。

### Python 接口（测试约定）

- `PrintArray(DataArray)`：所有元素按存放顺序输出在**同一行**，用空格隔开（几个空格、末尾有没有空格都可以）。
- `LinearSearch(DataArray, DataToFind)`：返回出现次数（整数）。
- 主程序：先读文件、`PrintArray(DataArray)`，再输入并验证一个 0–100 的整数，输出 `The number 12 is found 4 times.`（末尾句点可有可无；MS 范例没有句点）。只测范围验证，不测输入非数字（QP 未要求处理，MS 范例直接 `int()`，D31）。
- `Data.txt` 不存在时程序不得崩溃（异常处理）；提示语措辞不测。

## 英文原题（转写自 QP pp.2–3）

```text
One source file is used to answer Question 1 ... The files are called Data.txt, AnimalData.txt
and ColourData.txt

1  A program reads data from a file and searches for specific data.

   (a) The main program needs to read 25 integer data items from the text file Data.txt into a
       local 1D array, DataArray
       (i)  Write program code to declare the local array DataArray
            Save your program as Question1_J2023.
            Copy and paste the program code into part 1(a)(i) in the evidence document.  [1]
       (ii) Amend the main program to read the contents of Data.txt into DataArray
            Save your program.
            Copy and paste the program code into part 1(a)(ii) in the evidence document. [4]

   (b) (i)   The procedure PrintArray() takes an integer array as a parameter and outputs the
             contents of the array in the order they are stored.
             The items are printed on the same line, for example:
                 10  4  5  13  25
             Write program code for the procedure PrintArray()
             Save your program.
             Copy and paste the program code into part 1(b)(i) in the evidence document.  [3]
       (ii)  Amend the main program to output the contents of DataArray using the procedure
             PrintArray()
             Save your program.
             Copy and paste the program code into part 1(b)(ii) in the evidence document. [1]
       (iii) Test your program.
             Take a screenshot of the output.
             Save your program.
             Copy and paste the screenshot into part 1(b)(iii) in the evidence document.  [1]

   (c) The function LinearSearch():
       • takes an integer array and integer search value as parameters
       • counts and returns the number of times the search value is found in the array.
       Write program code for the function LinearSearch()
       Save your program.
       Copy and paste the program code into part 1(c) in the evidence document.          [3]

   (d) (i)  Amend the main program to:
            • prompt the user to input a whole number between 0 and 100 inclusive
            • read and validate the input from the user
            • call LinearSearch() with DataArray and the validated input value
            • output the result in the format:
              The number 7 is found 2 times.
            Save your program.
            Copy and paste the program code into part 1(d)(i) in the evidence document.  [4]
       (ii) Test your program by inputting the number 12.
            Take a screenshot of the output.
            Save your program.
            Copy and paste the screenshot into part 1(d)(ii) in the evidence document.   [1]
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a)(i) | 9618_s23_41:1(a)(i) | 1 | 代码 | `test_1a_dataarray_holds_25_integers_from_file` · 名为 DataArray、25 个整数 | 注释写明 25 个元素与 INTEGER；局部于主程序 |
| Part 1(a)(ii) | 9618_s23_41:1(a)(ii) | 4 | 代码 | `test_1a_dataarray_holds_25_integers_from_file` · MP1–MP3；`test_1a_missing_file_handled` · MP4（不崩溃） | MP4 提示语合适；MP5 关闭文件且位置合适（max 4） |
| Part 1(b)(i) | 9618_s23_41:1(b)(i) | 3 | 代码 | `test_1b_i_print_array_one_line_in_order`、`test_1b_i_print_array_any_length` · MP2–MP3 | MP1 过程头带一个数组参数 |
| Part 1(b)(ii) | 9618_s23_41:1(b)(ii) | 1 | 代码 | `test_1b_iii_screenshot_array_output` · 以 DataArray 调用 PrintArray；`test_1bii_di_traced_main` · 实际调用、参数与数据链（D46） | — |
| Part 1(b)(iii) | 9618_s23_41:1(b)(iii) | 1 | 截图 | `test_1b_iii_screenshot_array_output` · 一行里依次是 Data.txt 的 25 个数（MS p.8 样例） | 截图清晰 |
| Part 1(c) | 9618_s23_41:1(c) | 3 | 代码 | `test_1c_linear_search_counts`、`test_1c_linear_search_other_array` · MP2–MP3 | MP1 函数头带数组与查找值两个参数；不用 `count()` |
| Part 1(d)(i) | 9618_s23_41:1(d)(i) | 4 | 代码 | `test_1d_i_validates_0_to_100` · MP1–MP4；`test_1d_i_bounds_inclusive` · MP2；`test_1bii_di_traced_main` · 实际调用、参数与数据链（D46） | MP1 提示语合适 |
| Part 1(d)(ii) | 9618_s23_41:1(d)(ii) | 1 | 截图 | `test_1d_ii_screenshot_number_12` · `The number 12 is found 4 times`（MS p.11 样例） | 截图里能看到输入的 12 |

## 人工核对清单

- [ ] 1(a)(i)：`DataArray` 建成 25 个元素的真实 list，注释写明 INTEGER（D10 ①）；声明在主程序里。
- [ ] 1(a)(ii) MP4–MP5：`try` / `except` 有合适的提示；`close()` 在读完之后、`try` 里（max 4，五点中任四点）。
- [ ] 1(b)(i) MP1、1(c) MP1：过程头 / 函数头与参数。
- [ ] 1(c)：计数用循环逐个比较，不用 `DataArray.count()`（D10 ③）。
- [ ] 1(d)(i) MP1：提示语说明要输入 0–100 的整数。
- [ ] 两个截图格：截图清晰、看得到输入值与输出。

## 说明

- MS 的 Java 范例 `X < DataArray.length - 1` 少查最后一个元素（MS p.11 截图里数组末尾的 `0` 也没输出）；QP 要求「outputs the contents of the array」「counts … the number of times」，测试按 QP 查到最后一个元素（D31）。
- 1(a)(i)、1(b)(ii)、1(b)(iii)、1(d)(ii) 是 1 分行，语料不拆得分点；其余行 MS 用圆点列点，语料 `markpoints[].n` 就是圆点顺序，没有对照差异。

### T38c1 · D46 调用与输出核验

增加 PrintArray(DataArray)、LinearSearch(DataArray, validated input) 的实际调用与返回值消息核对，覆盖三种查找值。QP 明定数组同行、完整结果消息格式；允许额外数字标题与消息中的相邻换行，仍检查规定的词序和数值。 等价 main() 暴露旧测试只查 runpy 模块命名空间，已改成观测主程序帧中的 DataArray，接受局部 main()。

测试观测候选文件中的实际模块调用、参数与返回值；结果与调用记录同时核对。注释、指定算法结构、变量接收返回值及截图呈现仍按人工清单检查；自动占比沿用逐点加权口径。
