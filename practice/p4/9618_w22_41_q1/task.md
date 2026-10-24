# 整数文件：读入、计数与冒泡排序

来源：9618_w22_41 第 1 题（1(a)–1(e)，6 行，23 分）；QP p.2–3，MS p.3–7。题干按 QP 原页转写，得分点与 Python 范例按 MS 原页核对（含 1(d)(ii) 的截图样例）。9618_w22_43 第 1 题与本题整题相同，不另做练习。

## 导读

这是一道完整的上机大题：从空文件写起，依次完成全局数组声明 → 读文件 → 输入校验与计数 → 主程序 → 冒泡排序。`starter.py` 只给了各小问的分节注释和主程序入口，声明、过程头本身就是得分点，要自己写。

- 把 `starter.py` 复制成 `attempts/practice/p4/9618_w22_41_q1/solution.py`（`make try EX=practice/p4/9618_w22_41_q1` 会自动做，并把 `files/IntegerData.txt` 复制到同一目录，可以直接 `python solution.py` 运行）。一问一问地测：`make try EX=practice/p4/9618_w22_41_q1 K=1c`。
- 标识符照抄题目：`DataArray`、`ReadFile`、`FindValues`、`BubbleSort`，文件名 `IntegerData.txt`（`p4-identifiers`）。
- 数组要建出真实的 list（100 个元素），并用注释写明大小与类型（D10 ①）；只写注释或空 list 不给声明分。
- 主程序写在 `if __name__ == "__main__":` 下面（MS 范例写在顶层，得分点看的是调用与输出，不看入口写法）。
- 提示语写在 `input("…")` 里，不要先 `print` 提示（D13）。
- 冒泡排序自己写循环与交换，不用 `sort()` / `sorted()` 代劳（D10 ③，人工核对）。

## 英文原题（QP p.2–3）

```text
A source file is used to answer Question 1. The file is called IntegerData.txt

1   The text file IntegerData.txt stores 100 integer numbers between 1 and 100 inclusive. A
    program is required to read in this data and perform searching and sorting on the data.

    (a) Write program code to declare a global 1D array, DataArray, with space for 100 integer
        values.
        Save your program as Question1_N22.
        Copy and paste the program code into part 1(a) in the evidence document.        [2]

    (b) The procedure ReadFile() must read in the numbers from the text file and store each one
        in the array. Use appropriate exception handling.
        Write program code for the procedure ReadFile().
        Save your program.
        Copy and paste the program code into part 1(b) in the evidence document.        [6]

    (c) The function FindValues() asks the user to enter a number to search for in the array.
        The number input must be a whole number between 1 and 100 inclusive. The function then
        returns the number of times the number input appears in the array.
        Write program code for the function FindValues().
        Save your program.
        Copy and paste the program code into part 1(c) in the evidence document.        [7]

    (d) (i)  Write program code to call ReadFile() and FindValues() from the main program.
             The return value from FindValues() must be output with an appropriate message.
             Save your program.
             Copy and paste the program code into part 1(d)(i) in the evidence document. [3]

        (ii) Test your program using the number 61 as input.
             Take a screenshot to show the output.
             Copy and paste the screenshot into part 1(d)(ii) in the evidence document.  [1]

    (e) The procedure BubbleSort() needs to perform a bubble sort on the array and print the
        contents of the sorted array.
        Write program code for the procedure BubbleSort() and call it from the main program.
        Save your program.
        Copy and paste the program code into part 1(e) in the evidence document.        [4]
```

## 数据文件

`files/IntegerData.txt`：从官方源文件逐字节复制（391 字节，sha256 `109ddf3b50460af6ef63a32c7db2403b017e5dd918fad76495c915451d12f86d`）。100 行整数，CRLF 行尾，**最后一行（19）后面没有换行**。逐行读时记得去掉行尾换行并转成 `int`。

## Python 接口与测试约定

- `DataArray`：模块级全局 list，100 个元素。测试会直接给 `DataArray` 赋值再调用 `FindValues()` / `BubbleSort()`，所以这两个过程必须用全局 `DataArray`。
- `ReadFile()`：无参数；文件缺失时不抛异常、输出一条提示。
- `FindValues()`：无参数，用 `input()` 读数，范围外（< 1 或 > 100）要重新输入，返回出现次数（整数）。题目说 “whole number”，MS 只要求 “validation/casting … as integer”，测试只喂整数，不测非数字输入（D31：QP 未定义的情形不测）。
- `BubbleSort()`：排好 `DataArray` 并**在过程里**输出排好的内容。输出格式题目没规定，`print(DataArray)` 或一行一个都可以，测试只按顺序取出输出中的整数。
- **与 MS 范例不一致、按 QP 处理的地方（D31）**：①MS 的 Python 范例 `FindValues()` 用 `range(0, 99)`，漏掉最后一个元素；QP 与 MP4 都要求遍历全部 100 个，测试用只出现在下标 99 的 19 检查。②MS 的 Python 范例把 `print(DataArray)` 写在主程序里；QP 说 BubbleSort() “print the contents of the sorted array”，MP1 也写 “outputting array contents at end of procedure”，所以测试检查过程本身的输出。③MS 范例 `DataArray[X].rstrip('\n')` 一行没有把结果存回（无效语句），参考解改为 `int(File.readline().strip())`。

## 证据文档对照表

`markpoints[].n` 与 MS 圆点顺序一致，本题无编号差异（D37 ②）。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_w22_41:1(a) | 2 | 代码 | `test_1a_dataarray_has_100_elements` · MP1–MP2 | 注释写明 INTEGER 与 100（D10 ①）；声明在全局 |
| Part 1(b) | 9618_w22_41:1(b) | 6 | 代码 | `test_1b_readfile_stores_all_100_integers` · MP2–MP4；`test_1b_readfile_closes_file` · MP5；`test_1b_missing_file_is_handled` · MP6–MP7 | MP1 过程头；MP5 关闭的位置；MP7 提示措辞 |
| Part 1(c) | 9618_w22_41:1(c) | 7 | 代码 | `test_1c_rejects_out_of_range_then_counts` · MP2、MP3、MP5–MP7；`test_1c_accepts_both_bounds` · MP3；`test_1c_checks_all_100_elements` · MP4；`test_1c_returns_zero_when_absent` · MP6–MP7 | MP1 函数头与输入提示 |
| Part 1(d)(i) | 9618_w22_41:1(d)(i) | 3 | 代码 | `test_1d_main_revalidates_and_outputs_count` · MP1–MP3（由 1(d)(ii) 一并端到端检查）；`test_1di_1e_traced_main` · 实际调用、参数与数据链（D46） | MP3 “appropriate message” 的措辞 |
| Part 1(d)(ii) | 9618_w22_41:1(d)(ii) | 1 | 截图 | `test_1d_screenshot_input_61_outputs_2` · 输入 61、输出 2 | 截图清晰、能看到输入的 61 |
| Part 1(e) | 9618_w22_41:1(e) | 4 | 代码 | `test_1e_bubblesort_sorts_and_prints_official_data` · MP1–MP4；`test_1e_bubblesort_reverse_order` · MP2–MP4；`test_1e_main_calls_bubblesort` · MP1；`test_1di_1e_traced_main` · 实际调用、参数与数据链（D46） | MP1 过程头；确实是冒泡排序（外层 / 内层循环、相邻比较与交换），没有用 `sort()` |

得分点 24 个（1(b) 7 点封顶 6 分）：行为可自动测 23 个，只能人工核对 1 个（1(b) MP1 过程头）。其余点里的「头部 / 措辞 / 类型注释」部分仍按下面的清单人工看。

## 人工核对清单

- [ ] 1(a) MP1：`DataArray` 是全局 1D 数组，注释写明类型（INTEGER）。
- [ ] 1(b) MP1：`def ReadFile():` 过程头；MP5：`close()` 在循环之后、`try` 之内的合理位置；MP6–MP7：`try` 覆盖打开与读取，`except` 有输出。
- [ ] 1(c) MP1：`def FindValues():` 函数头，输入带提示；MP2：输入转成 `int`。
- [ ] 1(d)(i) MP1–MP3：主程序先 `ReadFile()` 再 `FindValues()`，返回值带说明文字输出。
- [ ] 1(e) MP1：过程头，过程末尾输出数组，主程序调用 `BubbleSort()`；MP2–MP4：外层循环、内层循环、相邻比较并交换全部元素（不用 `sort()`，D10 ③）。
- [ ] 截图格：能看到输入 61 与输出 2（MS 样例：`Enter a number between 1 and 100` / `61` / `The number was found 2 times`）。

### T38c1 · D46 调用与输出核验

主程序原先用正确数值证明三个模块已调用，新增 ReadFile → FindValues → BubbleSort 的实际顺序和两种输入的计数返回值检查。消息与数字允许相邻换行；排序输出用有序连续块匹配，允许其后额外数字说明。

测试观测候选文件中的实际模块调用、参数与返回值；结果与调用记录同时核对。注释、指定算法结构、变量接收返回值及截图呈现仍按人工清单检查；自动占比沿用逐点加权口径。
