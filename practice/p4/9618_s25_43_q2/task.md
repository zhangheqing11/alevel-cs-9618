# 9618_s25_43 Question 2 · 插入排序、数组格式输出、二分查找

## 中文导读

标识符、文件名照抄题目；真实数组须有类型与大小注释（D10）。题目要求的算法不得用 `sort`、`sorted`、`index`、`in`、`max` 等代劳。主程序放在 `if __name__ == "__main__":` 下，导入时不执行。

## QP 原题英文转写

A program sorts the data in the 1D array DataArray and searches DataArray for specific values.

DataArray stores 14 integer values and is declared local to the main program.

### 2(a) [1]

Write program code to create DataArray and initialise it with the following data values in the
        order they are written:
           0   3   4   56   67   44   43   32   31   345   45   6   54   1
 Save your program as Question2_J25.
 Copy and paste the program code into part 2(a) in the evidence document.

### 2(b) [5]

The function InsertionSort() takes an array of integers as a parameter. The function
        sorts the data in the array into ascending numerical order using an insertion sort. The function
        returns the sorted array.
        Write program code for InsertionSort()
        You must not use any inbuilt sorting functions for your programming language.
 Save your program.
 Copy and paste the program code into part 2(b) in the evidence document.

### 2(c) [2]

The procedure OutputArray() takes an array of integers as a parameter. The procedure
        outputs each element in the array from the first element to the last element. The output is on
        one line with a space between each number.
        An example output is:
                      "0 3 4 56 67 44 43 32 31 345 45 6 54 1"
        Write program code for OutputArray()
 Save your program.
 Copy and paste the program code into part 2(c) in the evidence document.

### 2(d)(i) [2]

The main program needs extending to:
            •   output the content of the unsorted array using OutputArray()
            •   sort the array using InsertionSort()
            •   output the content of the sorted array using OutputArray()
            Write program code to extend the main program.
 Save your program.
 Copy and paste the program code into part 2(d)(i) in the evidence document.

### 2(d)(ii) [1]

Test your program.
            Take a screenshot of the output(s).
 Save your program.
 Copy and paste the screenshot into part 2(d)(ii) in the evidence document.

### 2(e) [6]

The function Search() performs a binary search to find ItemToFind in DataArray
        The function takes two parameters:
        •   DataArray, an array of integers
        •   ItemToFind, an integer to find in DataArray
        The function returns:
        •   the index of ItemToFind if it is in DataArray
        •   –1 if ItemToFind is not in DataArray
        Write program code for Search()
        You must not use any inbuilt searching functions for your programming language.
 Save your program.
 Copy and paste the program code into part 2(e) in the evidence document.

### 2(f)(i) [2]

The main program needs extending to call Search() with the sorted array four times:
        •   the first time to find the index of the integer 0
        •   the second time to find the index of the integer 345
        •   the third time to find the index of the integer 67
        •   the fourth time to find the index of the integer 2
            If the integer is found in the array, output an appropriate message that includes the index.
            If the integer is not found, output that it was not found.
            Write program code to extend the main program.
 Save your program.
 Copy and paste the program code into part 2(f)(i) in the evidence document.

### 2(f)(ii) [1]

Test your program.
            Take a screenshot of the output(s).
 Save your program.
 Copy and paste the screenshot into part 2(f)(ii) in the evidence document.

## Python 接口与 QP / MS 差异

`InsertionSort(DataArray)` 返回升序数组；`OutputArray(DataArray)` 无返回值，按 QP 输出一行空格分隔；`Search(DataArray, ItemToFind)` 返回下标或 −1。无数据文件，不复制本卷其他题目的 QueueData.txt。
本题 Python MS 范例与 QP 无需作行为修正。2(c) 的 Java / VB 范例跳过值 −1，QP 要求输出每个元素，本练习一律按 QP 输出所有元素（含负整数）。允许迭代或递归二分查找，排序须为插入排序。
截图测试按 MS p.25 / p.32 的数值与顺序断言，不固定说明文字；单行空格格式只在 QP 明确要求的 OutputArray 中检查。

## 证据文档对照表

已用 textutil 读取本卷官方 evidence.doc，以下一行对应一个证据格。编号用语料 markpoints[].n；无拆分的 1 分行记 whole。自动测试与人工核对共同判断，不把自动测试通过等同于获得全部分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a) | 9618_s25_43:2(a) | 1 | 代码 | `test_2a_di_fi_main_call_sequence` · whole（原始 14 整数顺序） | 数组局部于主程序；INTEGER、大小 14 注释 |
| Part 2(b) | 9618_s25_43:2(b) | 5 | 代码 | `test_2b_insertion_sort` · MP1–MP5；`test_2b_e_no_builtin_shortcuts` | MP1 函数头；确为插入排序（不可换成冒泡等） |
| Part 2(c) | 9618_s25_43:2(c) | 2 | 代码 | `test_2c_output_format` · MP1–MP2 | MP1 过程头 |
| Part 2(d)(i) | 9618_s25_43:2(d)(i) | 2 | 代码 | `test_2a_di_fi_main_call_sequence`、`test_2dii_screenshot_unsorted_then_sorted` · MP1–MP2 | — |
| Part 2(d)(ii) | 9618_s25_43:2(d)(ii) | 1 | 截图 | `test_2dii_screenshot_unsorted_then_sorted` · whole | 截图清晰 |
| Part 2(e) | 9618_s25_43:2(e) | 6 | 代码 | `test_2e_search_found_and_missing` · MP2–MP6；`test_2e_search_halves_interval` · MP3–MP6；`test_2b_e_no_builtin_shortcuts` | MP1 函数头 |
| Part 2(f)(i) | 9618_s25_43:2(f)(i) | 2 | 代码 | `test_2a_di_fi_main_call_sequence` · MP1；`test_2fii_screenshot_locations` · MP2 | appropriate message 语义 |
| Part 2(f)(ii) | 9618_s25_43:2(f)(ii) | 1 | 截图 | `test_2fii_screenshot_locations` · whole（0、13、12，第四次未找到） | 截图清晰 |

## 人工核对清单

- 数组在主程序局部，注释 14 个 INTEGER。
- 模块头按 MS 检查；含返回值或输出行为的混合点仍计自动覆盖，其函数头由人工补核。
- 2(b) 必须插入排序：提取当前值、后移已排序段、插回正确位置。结果正确不能证明采用了指定排序。
- 2(e) 确为二分查找；允许递归或迭代，不限定变量名或循环形式。
- 2(f) appropriate message 语义与截图清晰度人工核对。

## 原页核验与编号对照

QP 4, 5, 6 页；MS 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 页已查看渲染图；Python 缩进依据原页。各行 MS 圆点顺序与语料 n 对应，无另印不同点号。可选点超过行分值时按点分值比例折算，仅用于覆盖统计，不取代实际批改。
