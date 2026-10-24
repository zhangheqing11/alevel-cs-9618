# 高分榜：二维数组读入与双关键字冒泡排序

来源：9618_w24_42 第 3 题（3(a)–3(e)(ii)，6 行，17 分）；QP p.12–14，MS p.31–39。题干与 3(d) 的示例表按 QP 原页转写；得分点、Python 范例与 3(e)(ii) 的截图样例按 MS 原页核对。

## 导读

一张 7 人的高分榜：先在主程序里声明 7 × 3 的字符串数组 → 读文件（每 3 行一组）→ 按格式输出 → 先按关卡、同关卡再按分数降序的冒泡排序 → 主程序按顺序调用并输出前后两份榜单。

- `make try EX=practice/p4/9618_w24_42_q3`（会把 `files/HighScoreTable.txt` 复制到作答目录；`K=3d` 只测排序）。
- 标识符、文件名照抄题目：`HighScores`、`ReadData`、`OutputHighScores`、`SortScores`、`HighScoreTable.txt`（`p4-identifiers`）。
- `HighScores` **局部于主程序**：写在 `if __name__ == "__main__":` 下面，建出 7 × 3、每格 `""` 的真实 list，并注释类型与大小（D10 ①）。
- 数组里一律存字符串（QP 3(a)）；排序时比较关卡与分数要先转成整数，否则 `"9"` 会排在 `"15"` 前面。
- 交换时整行（ID、关卡、分数）一起换；冒泡排序自己写，不用 `sort()` / `sorted()`（D10 ③）。

## 英文原题（QP p.12–14）

```text
3   The text file HighScoreTable.txt stores the top seven player scores for a game.

    The data in the file is stored in the order:

        Player ID
        Game level
        Score

    Each item of data is stored on a new line. For example, the first set of data in the file is:

        Player ID:    GHEH
        Game level:   3
        Score:        10

    (a) The data about the players and their scores is stored in a 2D array of strings with the identifier
        HighScores.
        The first dimension of the array has seven elements: one for each player. The second
        dimension of the array has three elements: one for the player ID, one for the game level and
        one for the score. All data is stored in the array as strings.
        HighScores is declared local to the main program, and all elements are initialised to an
        empty string, for example "".
        Write program code to declare and initialise HighScores.
        Save your program as Question3_N24.
        Copy and paste the program code into part 3(a) in the evidence document.        [2]

    (b) The function ReadData() reads the data from HighScoreTable.txt and stores the data
        in a 2D array. The function returns the 2D array.
        The function uses exception handling when opening and reading data from the file.
        Write program code for ReadData().
        Save your program.
        Copy and paste the program code into part 3(b) in the evidence document.        [5]

    (c) The procedure OutputHighScores() takes a 2D array as a parameter. It outputs each
        player's ID, level and score in the order they are in the array. The outputs are in the format:

            GHEH reached level 3 with a score of 10

        Write program code for OutputHighScores().
        Save your program.
        Copy and paste the program code into part 3(c) in the evidence document.        [2]

    (d) The scores in HighScoreTable.txt are not in order.
        The player scores are first sorted by the game level they reached. For example, all players
        that reached level 5 are higher in the high score table than players that reached level 4.
        The players that reached the same level are then sorted in descending order of score.
        An example sorted high score table is:

            Position | Player ID | Game level | Score
            ---------+-----------+------------+------
               1     |   GFED    |     5      |  25
               2     |   HJKM    |     4      |  21
               3     |   RERR    |     4      |  19
               4     |   TTYU    |     4      |  15
               5     |   WSVG    |     3      |  20
               6     |   PPTR    |     3      |  15
               7     |   SNQT    |     2      |  10

        The function SortScores() uses a bubble sort to sort the data as described and returns the
        sorted array.
        Write program code for SortScores().
        Save your program.
        Copy and paste the program code into part 3(d) in the evidence document.        [4]

    (e) (i)  Amend the main program to implement these steps in the order given:
             •  call ReadData() and store the returned array in HighScores
             •  output "Before"
             •  call OutputHighScores() with HighScores as a parameter
             •  call SortScores() and store the returned array in HighScores
             •  output "After"
             •  call OutputHighScores() with HighScores as a parameter.
             Save your program.
             Copy and paste the program code into part 3(e)(i) in the evidence document. [2]

        (ii) Test your program
             Take a screenshot of the output.
             Save your program.
             Copy and paste the screenshot into part 3(e)(ii) in the evidence document.  [2]
```

## 数据文件

`files/HighScoreTable.txt`：从官方源文件逐字节复制（89 字节，sha256 `d93b28d1e74024d672692655e3bc0c9a988a4ef1010aae9f54dd4b24f87635d7`）。21 行（7 人 × 3 行），CRLF 行尾，**最后一行（22）后面没有换行**。

## Python 接口与测试约定

- 3(a)：测试以 `__main__` 身份在进程内运行整个程序并跟踪主程序里 `HighScores` 的取值，要求它在某一时刻是 7 × 3、每格 `""` 的 list（先写 `HighScores = []` 再赋 7 × 3 也可以，MS 范例就是这样）。
- `ReadData()`：无参数，返回 7 × 3 的字符串二维 list（去掉换行）；文件缺失时不抛异常、输出一条提示（不检查此时的返回值）。
- `OutputHighScores(HighScores)`：每人一行，格式按 QP：`GHEH reached level 3 with a score of 10`；测试把连续空白当作一个空格。
- `SortScores(HighScores)`：返回排好的二维 list；关卡降序、同关卡分数降序，按数值比较。
- 主程序输出：`Before`、7 行原顺序、`After`、7 行排好序，共 16 行，不要多输出别的行。
- **与 MS 不一致、按 QP 处理（D31）**：MS 3(e)(ii) 的截图样例每行写 “got to level”，QP 3(c) 规定的格式是 “reached level”（MS 3(c) 的 Python 范例也是 “reached level”）；测试按 QP。

## 证据文档对照表

`markpoints[].n` 与 MS 圆点顺序一致，本题无编号差异（D37 ②）。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_w24_42:3(a) | 2 | 代码 | `test_3a_highscores_7_by_3_empty_strings` · MP1–MP2 | 局部于主程序；注释写明 STRING、7 × 3 |
| Part 3(b) | 9618_w24_42:3(b) | 5 | 代码 | `test_3b_readdata_returns_7_players_of_3_strings` · MP1、MP3–MP4；`test_3b_readdata_closes_file` · MP2；`test_3b_missing_file_is_handled` · MP5 | MP1 函数头；MP2 关闭的位置；MP5 所有文件操作都在 `try` 里 |
| Part 3(c) | 9618_w24_42:3(c) | 2 | 代码 | `test_3c_output_format_in_array_order` · MP1–MP2 | MP1 过程头带二维数组参数 |
| Part 3(d) | 9618_w24_42:3(d) | 4 | 代码 | `test_3d_sortscores_official_data` · MP1–MP4；`test_3d_sortscores_qp_example_from_reverse` · MP2–MP4；`test_3d_sortscores_compares_numbers_not_text` · MP3 | MP1 函数头；确实是冒泡排序 |
| Part 3(e)(i) | 9618_w24_42:3(e)(i) | 2 | 代码 | `test_3e_screenshot_before_and_after` · MP1–MP2；`test_3ei_traced_main` · 实际调用、参数与数据链（D46） | 返回值存回 `HighScores` |
| Part 3(e)(ii) | 9618_w24_42:3(e)(ii) | 2 | 截图 | `test_3e_screenshot_before_and_after` · MP1（Before + 原顺序）、MP2（After + 排好序） | 截图清晰 |

得分点分值 17：行为可自动测 17，没有只能人工核对的点（各点里的函数头、注释、位置部分仍按下面的清单看）。

## 人工核对清单

- [ ] 3(a)：`HighScores` 在主程序里声明（不是全局），7 × 3，每格 `""`，注释写明类型与大小。
- [ ] 3(b) MP1：`def ReadData():` 并返回填好的数组；MP2：以读方式打开、在合适位置关闭；MP5：打开与读取都在 `try` 里，`except` 有输出。
- [ ] 3(c) MP1：`def OutputHighScores(HighScores):`，遍历第一维。
- [ ] 3(d)：`def SortScores(HighScores):` 返回排好的数组；先比关卡、关卡相同再比分数，整行交换；外层、内层循环正确。
- [ ] 3(e)(i)：六步顺序与题目一致。
- [ ] 3(e)(ii) 截图：`Before` 与 7 行原顺序；`After` 与 `JGHF 5 22`、`RFOO 5 20`、`KWQW 4 20`、`MMND 4 18`、`XXHD 3 19`、`QWSD 3 15`、`GHEH 3 10`。

### T38c1 · D46 调用与输出核验

发现另一个 min 容量误拒：MS p.31 声明 min 7×3，旧 test_3a 只接受恰好 7×3。改查至少 7 行且至少 3 列，声明中所有格为空；不要求读取函数任意扩容。整段截图严格相等改为 Before/七条原顺序/After/七条排序结果的有序子序列，规定的单条句式保留。补测 ReadData → OutputHighScores → SortScores → OutputHighScores；HighScores 接收返回值仍人工。

测试观测候选文件中的实际模块调用、参数与返回值；结果与调用记录同时核对。注释、指定算法结构、变量接收返回值及截图呈现仍按人工清单检查；自动占比沿用逐点加权口径。
