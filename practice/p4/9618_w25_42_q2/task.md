# 随机数组：冒泡排序与递归二分查找

来源：9618_w25_42 第 2 题（2(a)–2(f)(ii)，8 行，26 分）；QP p.6–8，MS p.18–26。题干按 QP 原页转写；得分点与 Python 范例按 MS 原页核对（两个截图格 MS 只有文字说明，“All screenshots will be unique to the candidate”）。本题不用数据文件（这份卷的 `TreeData.txt` 属于第 3 题）。

## 导读

主程序生成 20 个不重复的随机整数 → 输出 → 冒泡排序 → 输出 “Sorted” 与排好的数组 → 输入一个数，用递归二分查找找它的下标。

- `make try EX=practice/p4/9618_w25_42_q2`（`K=2e` 只测二分查找）。
- 标识符照抄题目：`PrintArray`、`BubbleSort`、`RecursiveBinarySearch`；输出文字 `Sorted`、`Not found`、`Found at position` 照抄（`p4-identifiers`）。
- 数组**局部于主程序**：写在 `if __name__ == "__main__":` 下面，注释写明 INTEGER、20 个元素（D10 ①）。`import random` 写在文件开头。
- 不重复：可以用 `random.sample(range(0, 101), 20)`（MS 范例），也可以自己生成、查重后再存；范围是 0 到 100，**含** 100。
- `BubbleSort()` 不能用 `sort()` / `sorted()`（QP 明文要求），要对任意长度的数组都能用（用 `len()` 控制循环）。
- `RecursiveBinarySearch()` 要真的递归、每次把范围减半；找不到返回 –1。
- 提示语写在 `input("…")` 里（D13）。

## 英文原题（QP p.6–8）

```text
2   A program stores 20 unique random integers between 0 and 100 (inclusive) in a 1D array that is
    local to the main program.

    (a) Write program code to declare the array local to the main program and store 20 unique
        random numbers between 0 and 100 (inclusive) in the array.
        Save your program as Question2_N25.
        Copy and paste the program code into part 2(a) in the evidence document.        [3]

    (b) The procedure PrintArray() takes an integer array as a parameter. The procedure outputs
        the array contents on a single line with a space between each integer.
        Write the program code for PrintArray()
        Save your program.
        Copy and paste the program code into part 2(b) in the evidence document.        [3]

    (c) The function BubbleSort():
        •  takes an integer array as a parameter
        •  sorts the data into ascending order using a bubble sort
        •  returns the sorted array.
        The function needs to work for an array of any length.
        Do not use an inbuilt sorting method.
        Write program code for BubbleSort()
        Save your program.
        Copy and paste the program code into part 2(c) in the evidence document.        [5]

    (d) (i)  The main program:
             •  outputs the contents of the array using PrintArray()
             •  sorts the array using BubbleSort()
             •  outputs "Sorted"
             •  outputs the contents of the sorted array using PrintArray()
             Write program code for the main program.
             Save your program.
             Copy and paste the program code into part 2(d)(i) in the evidence document.  [3]

        (ii) Test your program.
             Take a screenshot of the output(s).
             Save your program.
             Copy and paste the screenshot(s) into part 2(d)(ii) in the evidence document. [1]

    (e) The recursive function RecursiveBinarySearch() takes four parameters:
        •  an integer array
        •  the lower bound of the array
        •  the upper bound of the array
        •  the value to find in the array.
        The recursive function performs a binary search to find the index of the value in the array.
        The function returns the index of the value if it is found. The function returns –1 if the value is
        not found.
        Write program code for RecursiveBinarySearch()
        Save your program.
        Copy and paste the program code into part 2(e) in the evidence document.        [6]

    (f) (i)  The main program:
             •  prompts the user to enter an integer
             •  takes the integer as input
             •  calls RecursiveBinarySearch() with the sorted array, appropriate lower bound,
                appropriate upper bound and the user's input as parameters
             •  outputs "Not found" if the input is not within the array
             •  outputs "Found at position" and the index if the input is within the array.
             Write program code to amend the main program.
             Save your program.
             Copy and paste the program code into part 2(f)(i) in the evidence document.  [3]

        (ii) Test your program three times with each of the inputs described:
             Test 1: the smallest number in the array
             Test 2: the largest number in the array
             Test 3: a number not in the array
             Take a screenshot of each output.
             Save your program.
             Copy and paste the screenshot(s) into part 2(f)(ii) in the evidence document. [2]
```

## Python 接口与测试约定

- 整个程序（主程序）用随机数，测试先 `random.seed(…)` 再以 `__main__` 运行你的文件：同一个种子得到同一个数组，所以测试可以先跑一次看清数组，再分别输入最小值、最大值。不要在程序里自己调用 `random.seed()`，否则测试无法复现。
- 主程序输出顺序：数组一行（20 个整数）、`Sorted`、排好的数组一行、输入提示与查找结果。数组行里只放这 20 个整数；提示语里不要写数字。
- 2(a) 用 8 个种子各跑一次：每次 20 个数都在 0–100 内且互不相同，不同种子得到的数组不全相同。
- `PrintArray(DataArray)`：20 个整数一行、空格分隔（末尾多一个空格可以）。题目里的数组是 20 个元素，测试只用 20 个元素的数组（D31）。
- `BubbleSort(DataArray)`：返回排好的 list；测试会用 0、1、2、20、30 个元素的数组（QP：any length），并让 `list.sort()` 与 `sorted()` 一调用就报错。
- `RecursiveBinarySearch(DataArray, Lower, Upper, DataToFind)`：返回下标或 –1；测试统计递归调用次数，20 个元素最多 6 次（确实在减半）。
- 2(f)：输入最小值应输出 `Found at position` 和 0，最大值输出 `Found at position` 和 19，999（不在数组里）输出 `Not found`。

## 证据文档对照表

`markpoints[].n` 与 MS 圆点顺序一致，本题无编号差异（D37 ②）。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a) | 9618_w25_42:2(a) | 3 | 代码 | `test_2a_twenty_unique_random_integers_0_to_100` · MP1–MP3 | 数组局部于主程序；注释写明类型与大小 |
| Part 2(b) | 9618_w25_42:2(b) | 3 | 代码 | `test_2b_printarray_single_line_with_spaces` · MP2–MP3 | MP1 过程头带数组参数 |
| Part 2(c) | 9618_w25_42:2(c) | 5 | 代码 | `test_2c_bubblesort_any_length` · MP1–MP5；`test_2c_no_inbuilt_sort` · MP2–MP4 | MP1 函数头；确实是冒泡排序（外层、内层循环、相邻交换） |
| Part 2(d)(i) | 9618_w25_42:2(d)(i) | 3 | 代码 | `test_2d_screenshot_unsorted_sorted_line_then_sorted` · MP1–MP3 | 用 `BubbleSort()` 的返回值 |
| Part 2(d)(ii) | 9618_w25_42:2(d)(ii) | 1 | 截图 | `test_2d_screenshot_unsorted_sorted_line_then_sorted` · 未排序 20 个、`Sorted`、同一批数升序 | 截图清晰 |
| Part 2(e) | 9618_w25_42:2(e) | 6 | 代码 | `test_2e_finds_every_index` · MP2–MP5；`test_2e_returns_minus_one_when_not_found` · MP6；`test_2e_is_recursive_and_halves` · MP1–MP2、MP4–MP5 | MP1 函数头四个参数 |
| Part 2(f)(i) | 9618_w25_42:2(f)(i) | 3 | 代码 | `test_2f_screenshot_smallest_largest_missing` · MP1–MP3 | 提示语；调用参数是排好的数组、0、19 |
| Part 2(f)(ii) | 9618_w25_42:2(f)(ii) | 2 | 截图 | `test_2f_screenshot_smallest_largest_missing` · MP1（最小值→0、最大值→19）、MP2（不在数组→Not found） | 三张截图都在、输入可见 |

得分点分值 26：行为可自动测 25，只能人工核对 1（2(b) MP1 过程头）。

## 人工核对清单

- [ ] 2(a)：数组在主程序里声明（局部），注释写明 INTEGER、20；20 个数随机、在 0–100 内、互不相同。
- [ ] 2(b) MP1：`def PrintArray(DataArray):`，一行输出、空格分隔。
- [ ] 2(c)：`def BubbleSort(DataArray):` 返回排好的数组；外层、内层循环，相邻比较交换；循环次数随 `len(DataArray)` 变（不写死 20）；不用内置排序。
- [ ] 2(d)(i)：先 `PrintArray(TheArray)`，再 `BubbleSort()`，再输出 `Sorted` 与 `PrintArray()`。
- [ ] 2(e)：四个参数；求中点；相等返回下标；中点值偏大递归到 `Middle - 1`，偏小递归到 `Middle + 1`；下界超过上界返回 –1。
- [ ] 2(f)(i)：提示并输入整数；`RecursiveBinarySearch(SortedArray, 0, 19, DataToFind)`；按返回值输出 `Not found` 或 `Found at position` 与下标。
- [ ] 截图格：2(d)(ii) 一张；2(f)(ii) 三张（最小值、最大值、不在数组里的数）。
