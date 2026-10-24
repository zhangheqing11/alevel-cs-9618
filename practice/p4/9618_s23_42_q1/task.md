# 9618_s23_42 第 1 题 · 动物名数组：按首字母降序冒泡排序

来源：`9618_s23_42:1(a)` – `9618_s23_42:1(d)(ii)`，5 行，14 分；QP pp.2–4，MS pp.4–10。题干与伪代码已对照 QP 原页（p.3）转写；MS 原页看过 1(c) 的 Python 范例（p.8）与截图样例（p.10）。

## 导读

- 本题没有数据文件（本卷的 `Employees.txt`、`HoursWeek1.txt` 属于第 3 题）。从空白的 `solution.py` 写起（`make try EX=practice/p4/9618_s23_42_q1`），一问一问地测：`make try EX=practice/p4/9618_s23_42_q1 K=1c`。
- 标识符照抄题目（`Animals`、`SortDescending`、`ArrayLength`、`Temp`）。
- **全局数组要建出真实的 list**：在模块顶层写 `Animals = [""] * 10`，注释写明 10 个元素、STRING（D10 ①）。MS 的 Python 范例只写了 `global Animals #array 10 elements string`，在 Python 里这句什么也不声明；考试里 MS 给分，但本系统按 D10 ① 要求真实的 list，测试也检查导入后有 10 个元素的 `Animals`。
- 1(b) 往这个数组里按下标存名字（`Animals[0] = "horse"` …）；如果在已有 10 个元素的 list 上 `append`，就变成 20 个元素了。
- 排序照题目伪代码写，只比较首字母（`MID(Animals[Y], 0, 1)` → `Animals[Y][0:1]` 或 `Animals[Y][0]`），不用 `sort()` / `sorted()`（D10 ③）。
- 主程序写在 `if __name__ == "__main__":` 下面（MS 范例写在顶层；这只是为了测试导入时不运行主程序，不影响得分）。

### 题目伪代码的越界（照写会出错）

伪代码内层是 `FOR Y ← … TO ArrayLength - X - 1`（含上界），`X = 0` 时 `Y` 取到 9，`Animals[Y + 1]` 就是 `Animals[10]`，越界。MS 的 Python 范例写成 `range(0, ArrayLength - X - 1)`（不含上界），正好避开；外层也写成 `range(0, ArrayLength - 1)`。照 MS 范例写即可，填空的四处是 `0`、`Y + 1`、`Y`、`Temp`。

### Python 接口（测试约定）

- `SortDescending()` 没有参数，排序全局数组 `Animals`。测试会把 `Animals` 换成别的 10 个名字再调用它，所以过程里用的必须是全局 `Animals`，不要另建一个局部数组。
- 主程序：存入 10 个名字 → 调用 `SortDescending()` → 每行输出一个名字。测试在 `SortDescending()` 被调用的那一刻读 `Animals`，检查 1(b) 存入的顺序。

## 英文原题（转写自 QP pp.2–4）

```text
1  A 1D array needs to store the names of 10 animals.

   (a) Write program code to declare the global string array Animals to store 10 items.
       Save your program as Question1_J2023.
       Copy and paste the program code into part 1(a) in the evidence document.          [2]

   (b) The main program needs to store the following animals in the array:
           horse
           lion
           rabbit
           mouse
           bird
           deer
           whale
           elephant
           kangaroo
           tiger
       Write program code to store these animal names in the array.
       The names must be in lower case and stored in the order given in the list.
       Save your program.
       Copy and paste the program code into part 1(b) in the evidence document.          [2]

   (c) The following pseudocode procedure sorts the array into a descending alphabetical order
       using only the first character in each animal name.
       The function LENGTH(DataArray) returns the number of elements in the array DataArray.
       The function MID(String, Start, Quantity) returns Quantity number of characters from
       String starting at index Start. The first character in the string is index 0, for example:
           MID("tiger", 0, 2) will return "ti"
       There are four incomplete statements in the procedure.

       PROCEDURE SortDescending()
         DECLARE ArrayLength : INTEGER
         DECLARE Temp : STRING
         ArrayLength ← LENGTH(Animals)
         FOR X ← 0 TO ArrayLength - 1
           FOR Y ← .......... TO ArrayLength - X - 1
             IF MID(Animals[Y], 0, 1) < MID(Animals[..........], 0, 1) THEN
               Temp ← Animals[..........]
               Animals[Y] ← Animals[Y + 1]
               Animals[Y + 1] ← ..........
             ENDIF
           NEXT Y
         NEXT X
       ENDPROCEDURE

       Write program code for the procedure SortDescending().
       Save your program.
       Copy and paste the program code into part 1(c) in the evidence document.          [6]

   (d) (i)  Write program code to amend the main program to:
            • call the procedure SortDescending()
            • output the sorted contents of the array with each animal name on a new line.
            Save your program.
            Copy and paste the program code into part 1(d)(i) in the evidence document.  [3]
       (ii) Test your program.
            Take a screenshot of the output.
            Save your program.
            Copy and paste the screenshot into part 1(d)(ii) in the evidence document.   [1]
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_s23_42:1(a) | 2 | 代码 | `test_1a_global_array_animals_10_elements` · MP1–MP2 | MP2 注释写明 STRING |
| Part 1(b) | 9618_s23_42:1(b) | 2 | 代码 | `test_1b_ten_names_stored_in_order` · MP1–MP2 | — |
| Part 1(c) | 9618_s23_42:1(c) | 6 | 代码 | `test_1c_sorts_given_animals_descending`、`test_1c_already_sorted_and_reversed` · MP1（四个空）、MP3；`test_1c_only_first_character_compared` · MP2 | MP1 四个空逐句对照 QP；MP3 其余部分照伪代码（`translate-pseudocode`） |
| Part 1(d)(i) | 9618_s23_42:1(d)(i) | 3 | 代码 | `test_1d_ii_screenshot_sorted_names` · MP1–MP3；`test_1b_ten_names_stored_in_order` · MP1（调用 SortDescending）；`test_1di_traced_sort` · 实际调用、参数与数据链（D46） | — |
| Part 1(d)(ii) | 9618_s23_42:1(d)(ii) | 1 | 截图 | `test_1d_ii_screenshot_sorted_names` · whale … bird 每行一个（MS p.10 样例） | 截图清晰 |

## 人工核对清单

- [ ] 1(a)：`Animals` 在模块顶层建成 10 个元素的真实 list，注释写明 STRING（D10 ①）。
- [ ] 1(c)：四个空照 QP 填（`0`、`Y + 1`、`Y`、`Temp`）；用 MID / LENGTH 对应的 Python 写法（切片或下标取首字母、`len()`）；其余结构照伪代码；不用内置排序。
- [ ] 1(d)(ii)：截图清晰。

## 说明

- QP 伪代码内层循环上界含 `ArrayLength - X - 1`，照写会让 `Animals[Y + 1]` 越界；MS 的 Python 范例用不含上界的 `range`。测试只查排序结果（D31）。
- MS 1(c) 语料把「1 mark for each completed statement to MAX 4」记为 MP1（4 分），两个圆点记为 MP2、MP3；其余行语料 `markpoints[].n` 就是圆点顺序。

### T38c1 · D46 调用与输出核验

已有 profiler 真正观测 SortDescending 及排序前十个名字，新增标准 run_script_traced 检查并保留。输出原先要求十条相邻行，改成逐行有序子序列以容许额外说明；每个动物单独一行仍由 QP 规定。十格容量明确，保留。

测试观测候选文件中的实际模块调用、参数与返回值；结果与调用记录同时核对。注释、指定算法结构、变量接收返回值及截图呈现仍按人工清单检查；自动占比沿用逐点加权口径。

D46 输出补核：每行动物名前加文字标签，仍每动物一行。自动测规定内容与格式，允许额外说明；未增加自动分值。
