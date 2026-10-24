# 9618_s24_41 第 1 题 · 输入整数、冒泡排序、迭代二分查找

来源：`9618_s24_41:1(a)` – `9618_s24_41:1(e)(iii)`，10 行，27 分；QP pp.2–5，MS pp.4–13。题干与三组测试数据已对照 QP 原页转写；MS 原页看过 1(d)(i) 的 Python 范例（p.9）与三个截图样例（pp.7、9、13）。

## 导读

- 本题没有数据文件（本卷的 `Trees.txt` 属于第 2 题），数据全部由键盘输入。从空白的 `solution.py` 写起（`make try EX=practice/p4/9618_s24_41_q1`），一问一问地测：`make try EX=practice/p4/9618_s24_41_q1 K=1e`。
- 标识符照抄题目（`DataStored`、`NumberItems`、`Initialise`、`BubbleSort`、`BinarySearch`、`DataToFind`）。
- **全局数组要建出真实的 list**：模块顶层写 `DataStored = [0] * 20`、`NumberItems = 0`，注释写明类型与大小（D10 ①）。MS 的 Python 范例只写了 `global DataStored #integer`，在 Python 里这句什么也不声明，再在 `Initialise` 里 `append`；考试里 MS 给分，但本系统要求真实的 list，测试也检查导入后 `DataStored` 有 20 个元素。于是 `Initialise` 要按下标存：`DataStored[NumberItems] = …`，存一个 `NumberItems` 加 1。
- 函数里给全局变量**赋值**（如 `NumberItems = NumberItems + 1`）要先写 `global NumberItems`；只改 list 的元素不需要。
- 排序、查找自己写循环，不用 `sort()`、`index()`、`in`（D10 ③）。
- 主程序写在 `if __name__ == "__main__":` 下面（MS 范例写在顶层；这只是为了测试导入时不运行 `input()`，不影响得分）。提示语写在 `input("…")` 里（D13）。

### Python 接口（测试约定）

- 函数测试会直接设置 `DataStored`、`NumberItems` 再调用 `BubbleSort()` / `BinarySearch(DataToFind)`，所以这两个过程要用全局的 `DataStored` 与 `NumberItems`，不要另建局部数组。测试把没用到的格子填成 999（比所有测试值都大），所以「只排前 `NumberItems` 个」与「整个 20 格都排」两种做法都能通过（MS 1(e)(iii) 也接受后者的「found in index 16」）。
- 输出数组的格式不限（一行一个、一行全部、`print(DataStored)` 的 `[3, 9, 4, 1, 2]` 都行）：测试把输出里的整数按顺序取出、去掉 0（20 格数组里没用到的格子）后查找 `3 9 4 1 2` 与 `1 2 3 4 9`。
- 截图格按 QP 的输入顺序整串喂给程序；最后一次输入是要找的数，程序最后输出的整数应是 `BinarySearch` 的返回值。

## 英文原题（转写自 QP pp.2–5）

```text
1  A program needs to take integer numbers as input, sort the numbers and then search for a
   specific number.

   (a) The integer numbers will be stored in the global 1D array, DataStored, with space for up
       to 20 integers.
       The global variable NumberItems stores the quantity of items the array contains.
       Write program code to declare DataStored and NumberItems.
       Save your program as Question1_J24.
       Copy and paste the program code into part 1(a) in the evidence document.          [1]

   (b) The procedure Initialise():
       • prompts the user to input the quantity of numbers the user would like to enter
       • reads the input and validates it is between 1 and 20 (inclusive)
       • prompts the user to input each number and stores each number in DataStored.
       Write program code for Initialise().
       Save your program.
       Copy and paste the program code into part 1(b) in the evidence document.          [5]

   (c) The main program stores 0 in NumberItems, calls Initialise() and then outputs the
       contents of DataStored.
       (i)  Write program code for the main program.
            Save your program.
            Copy and paste the program code into part 1(c)(i) in the evidence document.  [2]
       (ii) Test your program by inputting the following data in the order given:
                30
                5
                3
                9
                4
                1
                2
            Take a screenshot of the output(s).
            Save your program.
            Copy and paste the screenshot into part 1(c)(ii) in the evidence document.   [2]

   (d) The procedure BubbleSort() uses a bubble sort to sort the data in DataStored into
       ascending numerical order.
       (i)   Write program code for BubbleSort().
             Save your program.
             Copy and paste the program code into part 1(d)(i) in the evidence document. [4]
       (ii)  Write program code to amend the main program to call BubbleSort() and then
             output the contents of DataStored.
             Save your program.
             Copy and paste the program code into part 1(d)(ii) in the evidence document.[1]
       (iii) Test your program by inputting the following data in the order given:
                5
                3
                9
                4
                1
                2
             Take a screenshot of the output(s).
             Save your program.
             Copy and paste the screenshot into part 1(d)(iii) in the evidence document. [1]

   (e) The function BinarySearch():
       • takes the integer parameter DataToFind to search for in the array
       • performs an iterative binary search on the array DataStored
       • returns the index where DataToFind is found in DataStored. If DataToFind is not
         found, the function returns -1.
       (i)   Write program code for the iterative function BinarySearch().
             Save your program.
             Copy and paste the program code into part 1(e)(i) in the evidence document. [6]
       (ii)  Write program code to amend the main program to:
             • take a number as input from the user
             • call BinarySearch() with the number input
             • output the value returned from the function call as its parameter.
             Save your program.
             Copy and paste the program code into part 1(e)(ii) in the evidence document.[3]
       (iii) Test your program twice with the following inputs:
             Test 1: 5   1   6   2   8   10   2
             Test 2: 5   1   6   2   8   10   7
             Take a screenshot of the output(s).
             Save your program.
             Copy and paste the screenshot into part 1(e)(iii) in the evidence document. [2]
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_s24_41:1(a) | 1 | 代码 | `test_1a_globals_declared` · 全局 DataStored（20 格）与 NumberItems | 注释写明 INTEGER（D10 ①） |
| Part 1(b) | 9618_s24_41:1(b) | 5 | 代码 | `test_1b_initialise_rejects_30_then_stores_five` · MP2–MP5；`test_1b_initialise_quantity_1_to_20_inclusive` · MP3 | MP1 过程头无参数；MP2 提示语合适 |
| Part 1(c)(i) | 9618_s24_41:1(c)(i) | 2 | 代码 | `test_1c_ii_screenshot_invalid_30_then_array` · MP1–MP2 | MP1 先把 0 存进 NumberItems |
| Part 1(c)(ii) | 9618_s24_41:1(c)(ii) | 2 | 截图 | `test_1c_ii_screenshot_invalid_30_then_array` · MP1（30 被拒、5 被收）、MP2（数组输出 3 9 4 1 2；MS p.7 样例） | 截图里看得到两次输入数量 |
| Part 1(d)(i) | 9618_s24_41:1(d)(i) | 4 | 代码 | `test_1d_i_bubble_sort_ascending` · MP1–MP4 | MP1 过程头 |
| Part 1(d)(ii) | 9618_s24_41:1(d)(ii) | 1 | 代码 | `test_1d_iii_screenshot_sorted` · 调用 BubbleSort 后输出数组 | — |
| Part 1(d)(iii) | 9618_s24_41:1(d)(iii) | 1 | 截图 | `test_1d_iii_screenshot_sorted` · 1 2 3 4 9（MS p.9 样例） | 截图里看得到输入 |
| Part 1(e)(i) | 9618_s24_41:1(e)(i) | 6 | 代码 | `test_1e_i_binary_search_found`、`test_1e_i_binary_search_larger_array` · MP2–MP5；`test_1e_i_binary_search_not_found` · MP6 | MP1 函数头带 DataToFind；确是迭代（循环）不是递归 |
| Part 1(e)(ii) | 9618_s24_41:1(e)(ii) | 3 | 代码 | `test_1e_iii_screenshot_test_1_found`、`test_1e_iii_screenshot_test_2_not_found` · MP1–MP3 | — |
| Part 1(e)(iii) | 9618_s24_41:1(e)(iii) | 2 | 截图 | `test_1e_iii_screenshot_test_1_found` · 测试 1 输出 1（MS 也接受 16）；`test_1e_iii_screenshot_test_2_not_found` · 测试 2 输出 –1（MS p.13 样例） | 两次测试都截图 |

## 人工核对清单

- [ ] 1(a)：`DataStored` 建成 20 个元素的真实 list，`NumberItems` 初值 0，注释写明 INTEGER（D10 ①）。
- [ ] 1(b) MP1：`def Initialise():` 无参数；MP2 提示语说明要输入数量。
- [ ] 1(d)(i) MP1、1(e)(i) MP1：过程头 / 函数头。
- [ ] 1(e)(i)：迭代（`while` 循环）而不是递归；`Mid` 用整数除法；不用 `index()` / `in`（D10 ③）。
- [ ] 三个截图格：截图清晰、看得到输入与输出。

## 说明

- MS 的 Python 范例 `BinarySearch` 用 `Last = NumberItems`（比最后一个下标大 1）；在 `append` 出来的只有 5 个元素的 list 上找比最大值还大的数会越界。参考解用 `Last = NumberItems - 1`；测试数组都有 20 格，两种写法都能通过。
- MS 的 Python 范例冒泡排序比较的是 `DataStored[Count2] > DataStored[Count]`（两个循环变量各自走全程），也能排好；参考解用相邻元素比较的标准写法。
- 1(a)、1(d)(ii)、1(d)(iii) 是 1 分行，语料不拆得分点；1(e)(iii) 语料把「1 mark for each test」记为 MP1（2 分）。其余行语料 `markpoints[].n` 就是 MS 圆点顺序。
