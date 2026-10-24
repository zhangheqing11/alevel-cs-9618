# 作业优先级：二维数组与插入排序

来源：9618_w22_42 第 1 题（1(a)–1(g)(ii)，8 行，23 分）；QP p.2–4，MS p.3–10。题干、伪代码声明与 1(d) 的表按 QP 原页转写；得分点、Python 范例与 1(g)(ii) 截图样例按 MS 原页核对。本题不用数据文件（这份卷的 `Characters.txt` 属于第 2 题），所以没有 `files/`。

## 导读

一道「全局二维数组 + 插入排序」的完整大题：声明 → 初始化 → 加入作业 → 主程序 → 按优先级插入排序 → 输出。`starter.py` 只有分节注释和主程序入口。

- `make try EX=practice/p4/9618_w22_42_q1`（可加 `K=1e` 只测一问）。
- 标识符照抄题目：`Jobs`、`NumberOfJobs`、`Initialise`、`AddJob`、`InsertionSort`、`PrintArray`（`p4-identifiers`）。
- `Jobs` 要建出真实的 100 × 2 list，并用注释写明 INTEGER、100 × 2（D10 ①）。MS 的 Python 范例 1(a) 只写了注释 `Jobs # global integer, 100 by 2 elements`，按 ER 与 D10 ① 这样不够。
- 下标照伪代码 `ARRAY[0:99, 0:1]`：`Jobs[i][0]` 是作业号，`Jobs[i][1]` 是优先级（D24）。
- 主程序写在 `if __name__ == "__main__":` 下面。
- 插入排序自己写（外层循环、内层向前移动、插入），不用 `sort()`（D10 ③，人工核对）。

## 英文原题（QP p.2–4）

```text
1   A computer program is needed to store jobs in order of priority. Each job has a job number
    (for example, 123) and a priority from 1 to 10, with 1 being the highest priority and 10 the lowest.

    The program stores the jobs in a global 2D array.

    The pseudocode declaration for the array is:

        DECLARE Jobs : ARRAY[0:99, 0:1] OF INTEGER

    For example:
    •  Jobs[0, 0] stores the job number of the first job.
    •  Jobs[0, 1] stores the priority of the first job.

    The global variable, NumberOfJobs, stores the number of jobs currently in the array.

    (a) Write program code to declare the global 2D array Jobs and the global variable
        NumberOfJobs.
        Save your program as Question1_N22.
        Copy and paste the program code into part 1(a) in the evidence document.        [3]

    (b) The procedure Initialise() stores –1 in each of the array elements and assigns 0 to
        NumberOfJobs.
        Write program code for the procedure Initialise().
        Save your program.
        Copy and paste the program code into part 1(b) in the evidence document.        [3]

    (c) The procedure AddJob():
        •  takes a job number and priority as parameters
        •  stores the job in the next free array element
        •  outputs 'Added' if the job was successfully stored in the array
        •  outputs 'Not added' if the job was not successfully stored in the array.
        Write program code for the procedure AddJob().
        Save your program.
        Copy and paste the program code into part 1(c) in the evidence document.        [5]

    (d) The main program should call the procedure Initialise() and then use the AddJob()
        procedure to store the following jobs in the order given:

            Job number | Priority
            -----------+---------
                12     |   10
               526     |    9
                33     |    8
                12     |    9
                78     |    1

        Write program code for the main program and perform the tasks described.
        Save your program.
        Copy and paste the program code into part 1(d) in the evidence document.        [2]

    (e) When a new job has been added, the array is sorted into ascending numerical order of priority
        using an insertion sort.
        Write program code for the procedure InsertionSort() to sort the data into ascending
        numerical order of priority.
        Save your program.
        Copy and paste the program code into part 1(e) in the evidence document.        [5]

    (f) The procedure PrintArray() outputs each job number and priority on a line, for example:

            123 priority 1
            39 priority 3
            120 priority 7

        Write program code for the procedure PrintArray().
        Save your program.
        Copy and paste the program code into part 1(f) in the evidence document.        [3]

    (g) The main program needs to sort the array and then output the contents of the array.

        (i)  Amend the main program by writing program code to call procedures InsertionSort()
             and PrintArray().
             Save your program.
             Copy and paste the program code into part 1(g)(i) in the evidence document. [1]

        (ii) Test your program.
             Take a screenshot of the output.
             Copy and paste the screenshot into part 1(g)(ii) in the evidence document. [1]
```

## Python 接口与测试约定

- `Jobs`、`NumberOfJobs` 是模块级全局变量；测试会调用 `Initialise()`、`AddJob()` 后直接读 `Jobs` 与 `NumberOfJobs`，所以各过程必须改的是全局的这两个（`global` 声明）。`Jobs` 的每一行可以是 list（`Jobs[i][0]`、`Jobs[i][1]`），测试按 `Jobs[i][0..1]` 读取。
- `Initialise()` 之后 `Jobs` 仍是 100 行、每行 `[-1, -1]`。MS 的 Python 范例用 `Jobs.append([-1,-1])`，那是建立在 1(a) 只有注释（空表）的前提上；本练习按 D10 ① 在 1(a) 就建好 100 × 2 的表，所以 `Initialise()` 要原地赋 –1，不能再追加 100 行。
- `AddJob()`：输出 `Added` / `Not added`（QP 给了这两个词，测试按整行比对）。已有 100 个作业时不存、输出 `Not added`。
- `InsertionSort()`：只排已存的 `NumberOfJobs` 个作业（MS MP2「number of jobs」）；排完后第 6 行起仍是 `[-1, -1]`。优先级相同的作业先后不限（MS：「526 and 12 can be reversed」）。
- `PrintArray()`：每个已存作业一行，形如 `123 priority 1`。测试允许单词两边多出空格（`print(a, " priority ", b)` 也行），只要求「作业号 priority 优先级」三段在同一行；不输出未用的 –1 行。

## 证据文档对照表

`markpoints[].n` 与 MS 圆点顺序一致，本题无编号差异（D37 ②）。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_w22_42:1(a) | 3 | 代码 | `test_1a_jobs_is_100_by_2_and_numberofjobs_declared` · MP1–MP3 | 注释写明 INTEGER、100 × 2；两者在全局（D10 ①） |
| Part 1(b) | 9618_w22_42:1(b) | 3 | 代码 | `test_1b_initialise_sets_all_minus_one_and_zero` · MP1–MP3 | MP1 过程头；MP2 两层循环 |
| Part 1(c) | 9618_w22_42:1(c) | 5 | 代码 | `test_1c_addjob_stores_in_next_free_element` · MP4–MP6；`test_1c_addjob_full_outputs_not_added` · MP2–MP3 | MP1 过程头带两个参数 |
| Part 1(d) | 9618_w22_42:1(d) | 2 | 代码 | `test_1g_screenshot_added_five_times_then_jobs_in_order` · MP1–MP2（5 次 Added、五个作业都在）；`test_1d_1gi_traced_main` · 实际调用、参数与数据链（D46） | 5 次调用的参数与顺序照表 |
| Part 1(e) | 9618_w22_42:1(e) | 5 | 代码 | `test_1e_insertionsort_orders_given_jobs_by_priority` · MP2–MP5；`test_1e_insertionsort_only_sorts_stored_jobs` · MP2；`test_1e_insertionsort_reverse_order` · MP3–MP5 | MP1 过程头；确实是插入排序（不用 `sort()`） |
| Part 1(f) | 9618_w22_42:1(f) | 3 | 代码 | `test_1f_printarray_format` · MP1–MP3 | MP1 过程头 |
| Part 1(g)(i) | 9618_w22_42:1(g)(i) | 1 | 代码 | `test_1g_screenshot_added_five_times_then_jobs_in_order` · 先排序后输出；`test_1d_1gi_traced_main` · 实际调用、参数与数据链（D46） | 调用顺序 |
| Part 1(g)(ii) | 9618_w22_42:1(g)(ii) | 1 | 截图 | `test_1g_screenshot_added_five_times_then_jobs_in_order` · Added ×5、作业按优先级 | 截图清晰 |

得分点 24 个：行为可自动测 22 个，只能人工核对 2 个（1(c) MP1、1(e) MP1 的过程头）。

## 人工核对清单

- [ ] 1(a)：`Jobs` 与 `NumberOfJobs` 在全局声明，注释写明类型与大小。
- [ ] 1(b) MP1：`def Initialise():` 过程头；MP2：两层循环遍历两个维度。
- [ ] 1(c) MP1：`def AddJob(JobNumber, Priority):` 两个参数。
- [ ] 1(d)：主程序先 `Initialise()`，再按表的顺序 5 次 `AddJob()`。
- [ ] 1(e) MP1：`def InsertionSort():` 过程头；外层循环到作业数、内层循环把较大的往后移、比较的是第二个下标（优先级）。
- [ ] 1(f) MP1：`def PrintArray():` 过程头。
- [ ] 1(g)(i)：主程序先 `InsertionSort()` 再 `PrintArray()`。
- [ ] 1(g)(ii) 截图：5 行 `Added`，然后 `78 priority 1`、`33 priority 8`、`526 priority 9`、`12 priority 9`、`12 priority 10`（526 与 12 可互换）。

### T38c1 · D46 调用与输出核验

原截图测试对整段严格十行且头五行必须 Added，误拒额外标题。改为找到五个 Added 与有序五作业块，逐作业规定格式保留。新增 Initialise、五次 AddJob 的参数/次序、InsertionSort → PrintArray 调用观测。100×2 为 QP 固定声明，保留。

测试观测候选文件中的实际模块调用、参数与返回值；结果与调用记录同时核对。注释、指定算法结构、变量接收返回值及截图呈现仍按人工清单检查；自动占比沿用逐点加权口径。
