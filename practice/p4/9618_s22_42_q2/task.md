# 9618_s22_42 第 2 题 · 二维随机数组：冒泡排序与递归二分查找

来源：`9618_s22_42:2(a)` – `9618_s22_42:2(c)(ii)`，6 行，23 分；QP pp.4–6，MS pp.13–24。题干与两段伪代码已对照 QP 原页转写；MS 原页看过 2(c)(i) 范例（p.22）与两个截图样例（pp.21、24）。

## 导读

- 本题没有数据文件：数组里的数是程序随机生成的。从空白的 `solution.py` 写起（`make try EX=practice/p4/9618_s22_42_q2`），一问一问地测：`make try EX=practice/p4/9618_s22_42_q2 K=2c`。
- 标识符照抄题目（`ArrayData`、`BinarySearch`、`SearchArray`、`Lower`、`Upper`、`SearchValue`）。数组要建出真实的 10 × 10 list，注释写明大小与类型（D10 ①）；冒泡排序照题目伪代码写三重循环，**不得**用 `sort()` / `sorted()`（QP 明令禁止，测试会检查）。
- 主程序写在 `if __name__ == "__main__":` 下面（MS 范例写在顶层；这只是为了测试导入时不运行主程序，不影响得分）。2(a) 要求数组是**主程序里的局部数组**，Python 里写在这个入口下面即可。
- 伪代码 `ArrayData[X, Z]` 在 Python 里写成 `ArrayData[X][Z]`；`DIV` 写成 `//`（或 `int(… / 2)`）。

### 题目伪代码的缺陷（照写得分，测试已避开）

2(c) 给的 `Mid ← (Lower + (Upper - 1)) DIV 2` 不是标准写法：`Lower = Upper` 时 `Mid` 会落到 `Lower - 1`，于是（`Lower = 0`、`Upper = 9`、各值互不相同时）找下标 3、5、9 处的值或大于整行最大值的数会无限递归，找下标 0 处的值会返回 `-1`。**考试照 QP 把六个空填完就得分**（MS「1 mark for each completed statement」），所以：

- 自动测试只用照 QP 写的函数能正确返回的情形：下标 1、2、4、7、8 处的值，以及比整行都小的数（返回 `-1`）。标准写法 `(Lower + Upper) // 2` 也能通过这些测试。
- 2(c)(ii) 主程序里自己测试时，「在第一行里的数」请选 `ArrayData[0][2]` 这类能找到的位置，「不在第一行里的数」选 `0`（数组里只有 1–100）；选到会无限递归的位置程序会崩溃，测试也会失败。
- 自己写二分查找时（不是照本题填空），按模板 `Mid ← (Lower + Upper) DIV 2` 处理边界。

### Python 接口（测试约定）

- 主程序用 `random`，测试先用固定种子再运行你的程序，检查的是性质（任何种子都应成立）：输出里依次有两个 10 × 10 的网格（每行 10 个整数，空格或逗号分隔都可以），第一个是排序前、第二个是排序后；网格之后输出两次查找的返回值。
- 网格前后的说明文字（如 `Before` / `After`）随意，不测（D31）。
- 2(b)(ii) 的输出过程 QP 没有命名，名字自定，测试只看输出。
- `BinarySearch(SearchArray, Lower, Upper, SearchValue)`：`SearchArray` 是二维数组，只查第一行 `SearchArray[0]`；测试用 `Lower = 0`、`Upper = 9` 调用。

## 英文原题（转写自 QP pp.4–6）

```text
2  A 2D array stores data entered by a user.

   (a) The main program declares a 2D array of 10 by 10 integer elements.
       The array is initialised with a random number between 1 and 100 in each element.
       Write program code for the main program.
       Save your program as Question2_J22.
       Copy and paste the program code into part 2(a) in the evidence document.          [4]

   (b) The following bubble sort pseudocode algorithm sorts the data in the first dimension of
       the 2D array into ascending numerical order.

       ArrayLength ← 10
       FOR X ← 0 TO ArrayLength - 1
         FOR Y ← 0 TO ArrayLength - 2
           FOR Z ← 0 TO ArrayLength - Y - 2
             IF ArrayData[X, Z] > ArrayData[X, Z + 1] THEN
               TempValue ← ArrayData[X, Z]
               ArrayData[X, Z] ← ArrayData[X, Z+1]
               ArrayData[X, Z + 1] ← TempValue
             ENDIF
           NEXT Z
         NEXT Y
       NEXT X

       (i)   Amend your main program by writing program code to implement the bubble sort
             algorithm after the initialisation of the array elements.
             You must not use any built-in sorting functions for your programming language.
             Save your program.
             Copy and paste the program code into part 2(b)(i) in the evidence document. [5]
       (ii)  Write program code for a procedure to output all the values in the 2D array. The
             values should be output as a 2D grid, with values in rows and columns.
             Call the procedure before and after your bubble sort code.
             Save your program.
             Copy and paste the program code into part 2(b)(ii) in the evidence document. [3]
       (iii) Test your program.
             Take a screenshot to show the output.
             Copy and paste the screenshot into part 2(b)(iii) in the evidence document.  [1]

   (c) The following pseudocode function uses recursion to perform a binary search in the first
       row of the array, for the value SearchValue in the array SearchArray.
       The function returns -1 if the item was not found, or it returns the index where it is
       found.
       There are six incomplete statements.

       FUNCTION BinarySearch(SearchArray, Lower, Upper, SearchValue) RETURNS INTEGER
         IF Upper >= Lower THEN
           Mid ← (Lower + (Upper - 1)) DIV ..........
           IF SearchArray[0, Mid] = .......... THEN
             RETURN ..........
           ELSE
             IF SearchArray[0, Mid] > SearchValue THEN
               RETURN BinarySearch(SearchArray, .........., Mid - 1, SearchValue)
             ELSE
               RETURN BinarySearch(SearchArray, Mid + 1, .........., SearchValue)
             ENDIF
           ENDIF
         ENDIF
         RETURN ..........
       ENDFUNCTION

       Note: the arithmetic operator DIV performs integer division, e.g. the result of
       10 DIV 3 will be 3.

       (i)  Write program code for the recursive function BinarySearch().
            Save your program.
            Copy and paste the program code into part 2(c)(i) in the evidence document.  [8]
       (ii) In the main program, test the function BinarySearch() twice, outputting the
            returned value each time.
            One test should be for a number that is in the first line of the array.
            One test should be for a number that is not in the first line of the array.
            Take a screenshot to show the output.
            Copy and paste the screenshot into part 2(c)(ii) in the evidence document.   [2]
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a) | 9618_s22_42:2(a) | 4 | 代码 | `test_2a_ten_by_ten_random_1_to_100` · MP1–MP4；`test_2a_values_are_random` · MP4 | MP1 数组局部于主程序；MP2 注释写明 INTEGER（D10 ①） |
| Part 2(b)(i) | 9618_s22_42:2(b)(i) | 5 | 代码 | `test_2b_i_bubble_sort_each_line_ascending` · MP1–MP5；`test_2b_i_no_builtin_sort`（QP 禁用内置排序） | 三重循环照伪代码（MP1 外层、MP2 第二层、MP3 内层界） |
| Part 2(b)(ii) | 9618_s22_42:2(b)(ii) | 3 | 代码 | `test_2b_iii_screenshot_unsorted_then_sorted` · MP2–MP3（每行一整行、排序前后各调用一次） | MP1 过程头 |
| Part 2(b)(iii) | 9618_s22_42:2(b)(iii) | 1 | 截图 | `test_2b_iii_screenshot_unsorted_then_sorted` · 先未排序、后在一个维度上排好（MS p.21 样例） | 截图清晰 |
| Part 2(c)(i) | 9618_s22_42:2(c)(i) | 8 | 代码 | `test_2c_i_finds_value_in_first_row`、`test_2c_i_not_found_returns_minus_1` · MP1（六个空：`2`、`SearchValue`、`Mid`、`Lower`、`Upper`、`-1`）、MP3；`test_2c_i_is_recursive` · MP2 | MP1 六个空逐句对照 QP；MP2 函数头参数；MP3 用整数除法 |
| Part 2(c)(ii) | 9618_s22_42:2(c)(ii) | 2 | 截图 | `test_2c_ii_screenshot_index_and_minus_1` · MP1（找到时输出下标）、MP2（找不到输出 –1） | 截图里的两个测试数确实一个在第一行、一个不在 |

## 人工核对清单

- [ ] 2(a)：数组声明在主程序里（局部），注释写明 10 × 10 INTEGER；用嵌套循环逐个赋随机数（MS 接受 1–100 含或不含端点）。
- [ ] 2(b)(i)：照伪代码写 X / Y / Z 三层循环与交换（MS 也接受 `a, b = b, a` 写法交换）；不用内置排序。
- [ ] 2(b)(ii) MP1：输出过程的过程头；网格每行一整行。
- [ ] 2(c)(i)：六个空照 QP 填（`DIV 2`、`SearchValue`、`Mid`、`Lower`、`Upper`、`-1`），整体结构照题目伪代码（`translate-pseudocode`）；函数头参数四个。
- [ ] 两个截图格：截图清晰；2(c)(ii) 两个返回值都在截图里。

## 说明

- MS 的 Python 范例有笔误：2(c)(i) 把条件写成 `if Upper >= 0`（QP 是 `Upper >= Lower`）、`If` 大写；2(b)(ii) 主程序里调用 `printarray`（定义是 `Printarray`）。参考解按 QP 写，测试按 QP 的要求判（D31）。
- QP 的 `Mid` 公式本身有缺陷（见上）：参考解照 QP 写，测试只用照 QP 能正确返回的情形，标准写法同样能过。
- 本题 MS 用圆点列得分点，不印编号。2(c)(i) 语料把「1 mark for each completed statement (6)」记为 MP1（6 分），两个圆点记为 MP2、MP3。
