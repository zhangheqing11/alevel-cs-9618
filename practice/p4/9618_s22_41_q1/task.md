# 9618_s22_41 第 1 题 · 高分榜（HighScore）

来源：`9618_s22_41:1(a)` – `9618_s22_41:1(f)`，10 行，29 分；QP pp.2–4，MS pp.4–17。题干、数据格式已对照 QP 原页转写；MS 原页看过 1(b)、1(e)(ii)、1(f) 的范例（pp.5、13、17）与两个截图样例（pp.9、16）；其余范例按 `ms_text` 核对。

## 导读

- 这是一道「读文件 → 输出 → 输入并验证 → 插入有序数组 → 写文件」的整题。从空白的 `solution.py` 写起（`make try EX=practice/p4/9618_s22_41_q1` 会建好并把 `HighScore.txt` 复制到旁边），一个小问一个小问地测：`make try EX=practice/p4/9618_s22_41_q1 K=1b`。
- 标识符、文件名照抄题目（`ReadHighScores`、`OutputHighScores`、`WriteTopTen`、`HighScore.txt`、`NewHighScore.txt`）。数组要建出真实的 list（11 个元素），注释写明大小与类型（D10 ①）；插入位置要自己写循环找，不用 `sort()`、`index()`、`insert()` 代劳（D10 ③）。
- 主程序写在 `if __name__ == "__main__":` 下面（MS 范例写在顶层；这只是为了测试导入时不运行 `input()`，不影响得分）。提示语写在 `input("…")` 里（D13）。
- `files/HighScore.txt` 是官方源文件原样副本：20 行，名字一行、分数一行交替，CRLF 行尾，最后一行 `2000` 后面**没有**换行。读进来要去掉行尾换行（`strip-newline`），比较分数前要转成整数（`type-conversion`），否则 `"9999" > "10000"`。

### Python 接口（测试约定）

- 1(e)(ii) 的过程 QP 没有命名，本练习用 MS 的名字 **`Arrange(Username, Score)`**：`Username` 是 3 字符字符串，`Score` 是整数（MS MP1「1 string and 1 integer parameter」）。
- 数据结构（一个二维数组、两个平行数组或记录数组）由你选，测试只经过上面几个过程检查结果：`OutputHighScores()` 每个玩家一行、格式 `PlayerName Score`（中间一个空格）。第 11 个元素输出成空行或不输出都可以（MS 1(d)(ii)「one extra blank space may, or may not be included」）。
- `WriteTopTen()` 的文件行格式 QP 没有规定（D31）：测试只检查 `NewHighScore.txt` 里依次是前十名的名字与分数（按空白或逗号分开），不检查一行一项还是一行一对。
- 截图格用整个程序运行代替：输入照 QP（`JKL`、`9999`），检查输出里依次出现 MS 截图样例的值；提示语不测。

## 英文原题（转写自 QP pp.2–4）

```text
A source file is used to answer question 1. The file is called HighScore.txt

1  The text file HighScore.txt stores the players who have scored the top ten scores in a game,
   in descending order of score. The file stores the 3-character name of the player, and their
   integer score, in the order: player, score.

   For example, the current top player in the text file:
       FYI is the player name
       10000 is the score

   The program:
   • reads in the data from HighScore.txt
   • allows the user to enter a new player name and their score
   • if appropriate, inserts the new player (name and score) into the top ten
   • writes the top ten players (name and score) into a new text file NewHighScore.txt

   (a) The program stores the players and their scores in an array of 11 elements (10 elements to
       be read from the file, 1 element to be inserted by the user).
       Write a program to declare one or more arrays, as global data structures, to store the
       player names and their scores.
       Save your program as Question1_J2022.
       Copy and paste the program code into part 1(a) in the evidence document.          [2]

   (b) The procedure ReadHighScores() opens the file HighScore.txt and reads the data into the
       data structure(s) declared in part 1(a).
       Write program code to declare the procedure ReadHighScores().
       Save your program.
       Copy and paste the program code into part 1(b) in the evidence document.          [6]

   (c) The procedure OutputHighScores() outputs all the values in the data structure(s) in the
       format:
           PlayerName Score
       For example, the first two data items:   FYI 10000
                                                ABC 9092
       Write program code to declare the procedure OutputHighScores().
       Save your program.
       Copy and paste the program code into part 1(c) in the evidence document.          [3]

   (d) The main program should first call ReadHighScores() and then OutputHighScores().
       (i)  Write the program code for the main program.
            Save your program.
            Copy and paste the program code into part 1(d)(i) in the evidence document.  [2]
       (ii) Test your program.
            Take a screenshot to show the output from part 1(d)(i).
            Copy and paste the screenshot into part 1(d)(ii) in the evidence document.  [1]

   (e) The main program needs to ask the user to input a new player name and a score. If this
       score is in the top ten then it will create a new top ten list that includes this score.
       (i)   Amend the main program to ask the user to input a 3-character player name and an
             integer score that must be between 1 and 100000 inclusive.
             Save your program.
             Copy and paste the program code into part 1(e)(i) in the evidence document. [3]
       (ii)  Write program code to declare a procedure that:
             • takes the player name and score as parameters
             • creates a new top ten list that includes the parameter if appropriate.
             Save your program.
             Copy and paste the program code into part 1(e)(ii) in the evidence document. [5]
       (iii) Amend the main program to call the procedure from part 1(e)(ii).
             Output the contents of the array before inserting the new player name and score,
             and output the contents of the array after inserting the new player name and score.
             Save your program.
             Copy and paste the program code into part 1(e)(iii) in the evidence document. [2]
       (iv)  Test your program by entering the player name "JKL" and the score "9999".
             Take a screenshot to show the output.
             Copy and paste the screenshot into part 1(e)(iv) in the evidence document.   [1]

   (f) The procedure WriteTopTen() stores the new top ten player names and scores in a text
       file called NewHighScore.txt
       Write program code to declare the procedure WriteTopTen().
       Save your program.
       Copy and paste the program code into part 1(f) in the evidence document.          [4]
```

QP 把分数排成 `10 000`、`9 092`（千位空格只是排版）；文件里是 `10000`、`9092`。

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_s22_41:1(a) | 2 | 代码 | `test_1a_global_array_has_11_elements` · MP1–MP2（有全局数组、11 个元素） | MP1 标识符合适；MP2 注释写明数据类型（D10 ①） |
| Part 1(b) | 9618_s22_41:1(b) | 6 | 代码 | `test_1b_reads_ten_players_from_file` · MP2–MP5；`test_1b_missing_file_handled` · MP7–MP8 | MP1 过程头（与结尾）；MP6 关闭文件（max 6） |
| Part 1(c) | 9618_s22_41:1(c) | 3 | 代码 | `test_1c_outputs_every_element_name_space_score` · MP2–MP3 | MP1 过程头与结尾 |
| Part 1(d)(i) | 9618_s22_41:1(d)(i) | 2 | 代码 | `test_1d_screenshot_shows_ten_players` · MP1–MP2（先读后输出） | — |
| Part 1(d)(ii) | 9618_s22_41:1(d)(ii) | 1 | 截图 | `test_1d_screenshot_shows_ten_players` · 10 个名字与分数（MS p.9 样例） | 截图清晰 |
| Part 1(e)(i) | 9618_s22_41:1(e)(i) | 3 | 代码 | `test_1e_i_rejects_name_not_3_characters` · MP1–MP2；`test_1e_i_score_upper_bound_100000_inclusive`、`test_1e_i_score_lower_bound` · MP3 | 提示语是否合适 |
| Part 1(e)(ii) | 9618_s22_41:1(e)(ii) | 5 | 代码 | `test_1e_ii_inserts_jkl_in_second_place`、`test_1e_ii_inserts_at_top`、`test_1e_ii_inserts_in_tenth_place`、`test_1e_ii_score_too_low_not_inserted` · MP2–MP5 | MP1 过程头：1 个字符串 + 1 个整数参数 |
| Part 1(e)(iii) | 9618_s22_41:1(e)(iii) | 2 | 代码 | `test_1e_iv_screenshot_before_and_after` · MP1–MP2（调用并在前后各输出一次） | — |
| Part 1(e)(iv) | 9618_s22_41:1(e)(iv) | 1 | 截图 | `test_1e_iv_screenshot_before_and_after` · 输入 JKL、9999，之后的列表 JKL 在第二位（MS p.16 样例） | 截图里能看到输入的 JKL、9999 |
| Part 1(f) | 9618_s22_41:1(f) | 4 | 代码 | `test_1f_writes_new_top_ten`、`test_1f_writes_unchanged_top_ten` · MP1（以写方式建 NewHighScore.txt）、MP3–MP4 | MP1 过程头；MP2 关闭文件；MP5 异常处理与输出（max 4） |

## 人工核对清单

- [ ] 1(a) MP1–MP2：数组是全局的、标识符有意义；注释写明 11 个元素与类型（只写注释或空 list 不给分，D10 ①）。
- [ ] 1(b) MP1：`def ReadHighScores():` 过程头；MP6：`close()` 带括号且在循环之后（MS Python 范例漏了括号 `File.close`，不要照抄）。
- [ ] 1(c) MP1、1(e)(ii) MP1、1(f) MP1：过程头；1(e)(ii) 的参数是一个字符串、一个整数。
- [ ] 1(e)(ii)：插入位置用循环逐个比较找出，元素后移也用循环写，不用 `insert()` / `sort()`（D10 ③）。
- [ ] 1(f) MP2：写完关闭文件；MP5（可选点）：`try` / `except` 并输出提示。
- [ ] 两个截图格：截图清晰、看得到输入值与前后两次输出。

## 说明

- MS 的 Python 范例有笔误：1(b)、1(f) 的 `File.close` 少了括号（1(f) 还写在循环里、文件名前多一个空格 `" NewHighScore.txt"`）；1(e)(ii) 的 `break` 写在内层 `while` 里，只移动了一个元素；1(e)(iii) 调用 `OutputHighScore()` 少了 `s`。参考解已改正，测试按 QP 的要求判（D31）。
- 本题 MS 用圆点列得分点，不印编号；语料 `markpoints[].n` 就是圆点的先后顺序，没有对照差异。
