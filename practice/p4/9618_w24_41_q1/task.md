# 颜色字符串：逐字符比较与冒泡排序

来源：9618_w24_41 第 1 题（1(a)–1(d)(iii)，8 行，22 分）；QP p.2–5，MS p.4–11。题干按 QP 原页转写；得分点、Python 范例与 1(b)(iii)、1(d)(iii) 的截图样例按 MS 原页核对。9618_w24_43 第 1 题与本题整题相同，不另做练习。

## 导读

读文件进数组 → 把数组拼成一行输出 → 自己写逐字符的字符串比较 → 用它做冒泡排序 → 再输出排好的一行。`starter.py` 只有分节注释和主程序入口。

- `make try EX=practice/p4/9618_w24_41_q1`（会把 `files/Data.txt` 复制到作答目录；`K=1c` 只测比较函数）。
- 标识符、文件名照抄题目：`ReadData`、`FormatArray`、`CompareStrings`、`Bubble`、`Data.txt`（`p4-identifiers`）。
- `ReadData()` 里的数组是**局部**的，要建出 45 个元素的真实 list 并注释类型与大小（D10 ①）；读行时去掉行尾换行。
- `CompareStrings()` **不能**整串比较（`First < Second`），必须一个字符一个字符地比（QP 明文要求）。
- `Bubble()` 比较两个字符串时要调用 `CompareStrings()`，不用 `sort()` / `sorted()`（D10 ③）。
- 主程序写在 `if __name__ == "__main__":` 下面。

## 英文原题（QP p.2–5）

```text
One source file is used to answer Question 1. The file is called Data.txt

1   A program sorts string data using different sorting methods.

    (a) The text file Data.txt stores string data items. Each data item is on a new line in the text
        file.
        The function ReadData():
        •  has a local array of strings that can store 45 items
        •  reads each line of data and stores it in the array
        •  returns the array.
        Write program code for the function ReadData().
        Save your program as Question1_N24.
        Copy and paste the program code into part 1(a) in the evidence document.        [6]

    (b) The function FormatArray() takes an array of strings as a parameter. It concatenates the
        contents of the array into one string with a space between each array element. The function
        returns the concatenated string.

        (i)   Write program code for FormatArray().
              Save your program.
              Copy and paste the program code into part 1(b)(i) in the evidence document.   [2]

        (ii)  The main program:
              •  calls ReadData() and stores the returned array
              •  calls FormatArray() with the returned array and outputs the returned string.
              Write program code for the main program.
              Save your program.
              Copy and paste the program code into part 1(b)(ii) in the evidence document.  [3]

        (iii) Test your program.
              Take a screenshot of the output.
              Save your program.
              Copy and paste the screenshot into part 1(b)(iii) in the evidence document.   [1]

    (c) The function CompareStrings():
        •  takes two strings as parameters
        •  compares each string, one character at a time, to identify which string comes first
           alphabetically. If the first two characters are the same, the second character of each
           string is compared. This continues until the two characters are different.
        The function:
        •  returns 1 if the first parameter comes before the second alphabetically
        •  returns 2 if the second parameter comes before the first alphabetically.
        Write program code for CompareStrings().
        Assume that all strings are in lower case.
        Assume that a difference between two strings will always be identified before the end of one
        string is reached.
        Do not use an in-built string comparison function.
        The strings must be compared one character at a time.
        Save your program.
        Copy and paste the program code into part 1(c) in the evidence document.        [4]

    (d) The function Bubble() takes an array of strings as a parameter and sorts the data into
        ascending alphabetical order, using a bubble sort. The bubble sort uses CompareStrings()
        to compare each string.
        The function returns the sorted list.

        (i)   Write program code for Bubble().
              Save your program.
              Copy and paste the program code into part 1(d)(i) in the evidence document.   [3]

        (ii)  Write program code to amend the main program to:
              •  call Bubble() with the unsorted array as a parameter
              •  call FormatArray() with the sorted array and output the returned string.
              Save your program.
              Copy and paste the program code into part 1(d)(ii) in the evidence document.  [2]

        (iii) Test your program.
              Take a screenshot of the output.
              Save your program.
              Copy and paste the screenshot into part 1(d)(iii) in the evidence document.   [1]
```

## 数据文件

`files/Data.txt`：从官方源文件逐字节复制（333 字节，sha256 `11de7ca3386dbb247af40dae432a048f3082b640b6494f5c0ddaf0b860b5e659`）。45 个小写颜色名，一行一个，CRLF 行尾，**最后一行（sage）后面没有换行**；45 个各不相同，也没有一个是另一个的前缀（符合 1(c) 的假设）。

## Python 接口与测试约定

- `ReadData()`：无参数，返回 45 个字符串的 list（不带换行）；文件缺失时不抛异常、输出一条提示。MS 的 Python 范例用 `File.read().split("\n")`，也能通过测试；文件缺失时 MS 范例不返回数组，测试不检查这种情况下的返回值。
- `FormatArray(DataArray)`：返回字符串，元素之间一个空格；末尾多一个空格可以（MS 范例就是这样），测试先去掉首尾空白再比。题目说数组存 45 项，测试只用 45 个元素的数组（D31）。
- `CompareStrings(First, Second)`：返回 1 或 2。测试会传入一种特殊的字符串：整串用 `<`、`>` 比较会报错，取单个字符（`First[i]`）比较照常可用——用来检查「逐字符比较」。
- `Bubble(DataArray)`：返回排好的 list；测试会把模块里的 `CompareStrings` 换成计数包装，检查排序确实调用了它。
- 主程序：先输出原顺序的一行，再输出排好序的一行（与 MS 截图样例一致）。

## 证据文档对照表

`markpoints[].n` 与 MS 圆点顺序一致，本题无编号差异（D37 ②）。1(a) MS 列 7 点、封顶 6 分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_w24_41:1(a) | 6 | 代码 | `test_1a_readdata_returns_all_45_items` · MP2、MP4–MP6；`test_1a_readdata_closes_file` · MP3；`test_1a_missing_file_is_handled` · MP7 | MP1 函数头；MP2 数组注释（STRING、45）；MP3 关闭的位置 |
| Part 1(b)(i) | 9618_w24_41:1(b)(i) | 2 | 代码 | `test_1b_formatarray_joins_with_spaces` · MP2 | MP1 函数头带参数 |
| Part 1(b)(ii) | 9618_w24_41:1(b)(ii) | 3 | 代码 | `test_1b_screenshot_all_colours_in_one_string` · MP1–MP3；`test_1bii_1dii_traced_main` · 实际调用、参数与数据链（D46） | 返回的数组存进变量再传入 |
| Part 1(b)(iii) | 9618_w24_41:1(b)(iii) | 1 | 截图 | `test_1b_screenshot_all_colours_in_one_string` · 45 个颜色在一行 | 截图清晰 |
| Part 1(c) | 9618_w24_41:1(c) | 4 | 代码 | `test_1c_comparestrings_returns_1_or_2` · MP1、MP3–MP4；`test_1c_compares_one_character_at_a_time` · MP2 | MP1 函数头；每种情况都有返回值 |
| Part 1(d)(i) | 9618_w24_41:1(d)(i) | 3 | 代码 | `test_1d_bubble_sorts_official_data` · MP1、MP3；`test_1d_bubble_reverse_order` · MP3；`test_1d_bubble_uses_comparestrings` · MP2 | MP1 函数头；确实是冒泡排序 |
| Part 1(d)(ii) | 9618_w24_41:1(d)(ii) | 2 | 代码 | `test_1d_screenshot_sorted_data` · MP1–MP2；`test_1bii_1dii_traced_main` · 实际调用、参数与数据链（D46） | 用 `Bubble()` 的返回值调用 `FormatArray()` |
| Part 1(d)(iii) | 9618_w24_41:1(d)(iii) | 1 | 截图 | `test_1d_screenshot_sorted_data` · 排好序的一行 | 截图清晰 |

得分点分值 23（1(a) 7 点封顶 6 分）：行为可自动测 21，只能人工核对 2（1(a) MP1、1(b)(i) MP1 的函数头）。

## 人工核对清单

- [ ] 1(a) MP1：`def ReadData():`；MP2：局部数组建出 45 个元素并注释类型；MP3：以读方式打开 `Data.txt`、在合适位置关闭；MP7：`try` / `except` 并有输出。
- [ ] 1(b)(i) MP1：`def FormatArray(DataArray):` 至少一个参数。
- [ ] 1(b)(ii)：`Colours = ReadData()`，再 `print(FormatArray(Colours))`。
- [ ] 1(c)：两个参数；逐字符比较（不用整串比较或 `sorted()` 之类）；1 / 2 两种返回都有。
- [ ] 1(d)(i)：数组作参数、返回排好的数组；比较用 `CompareStrings()`，结果为 2 时交换；外层、内层循环正确。
- [ ] 1(d)(ii)：`Bubble()` 的返回值存起来或直接传给 `FormatArray()` 并输出。
- [ ] 截图格：1(b)(iii) 一行显示全部 45 个颜色（原顺序）；1(d)(iii) 一行显示排好序的颜色（`amber aqua azure … violet white yellow`）。

### T38c1 · D46 调用与输出核验

新增 ReadData 返回数组 → FormatArray，以及 Bubble 返回数组 → FormatArray 的实际调用/参数/结果检查。截图原先要求颜色行整行完全一致，改为行内包含指定字符串并检查先后，接受额外说明。明确存入某变量等语法仍人工补核。

测试观测候选文件中的实际模块调用、参数与返回值；结果与调用记录同时核对。注释、指定算法结构、变量接收返回值及截图呈现仍按人工清单检查；自动占比沿用逐点加权口径。
