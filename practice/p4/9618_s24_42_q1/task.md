# 9618_s24_42 第 1 题 · 猜词游戏：读词表文件、输入猜词、统计百分比

来源：`9618_s24_42:1(a)` – `9618_s24_42:1(d)(iii)`，7 行，22 分；QP pp.2–4，MS pp.4–14。题干已对照 QP 原页转写；MS 原页看过两个截图样例（pp.13、14），范例按 `ms_text` 核对。

## 导读

- 从空白的 `solution.py` 写起（`make try EX=practice/p4/9618_s24_42_q1` 会建好并把三个词表复制到旁边），一问一问地测：`make try EX=practice/p4/9618_s24_42_q1 K=1c`。
- 标识符照抄题目（`WordArray`、`NumberWords`、`ReadWords`、`Play`、`Easy.txt`、`Medium.txt`、`Hard.txt`）。全局数组建成真实的 list（如 `WordArray = [""] * 100`），注释写明类型（D10 ①）；函数里给全局变量**赋值**要先写 `global`。
- **`NumberWords` 是答案个数，不算第一行的主词**（QP「the number of words that can be made from the letters in the main word」、MS MP7「excluding main word」）：`Easy.txt` 是 14，`Medium.txt` 44，`Hard.txt` 97。
- `files/` 里三个词表是官方源文件原样副本：第一行主词，之后每行一个答案；CRLF 行尾，**最后一行没有换行**。读进来要去掉行尾换行（`strip-newline`）——不去的话，只有最后一个词（如 `she`）能猜中。
- 查找自己写循环，不用 `in` / `index()` 代劳（D10 ③）。主程序写在 `if __name__ == "__main__":` 下面（MS 范例写在顶层；这只是为了测试导入时不运行 `input()`，不影响得分）。提示语写在 `input("…")` 里（D13）。

### Python 接口（测试约定）

- `ReadWords(FileName)`：读完后 `WordArray[0]` 是主词，`WordArray[1]` … `WordArray[NumberWords]` 依次是答案；最后调用 `Play()`（1(d)(i)）。测试 1(a) 时会把 `Play` 换成空过程。文件打不开时输出提示、不崩溃。
- `Play()`：没有参数，用全局 `WordArray`、`NumberWords`；每读一个词就输出「是答案」或「不是答案」的提示（措辞自定，两种提示要不同）；输入 `no` 结束。猜中的答案在数组里换成空值（`""` 或 `None`），所以同一个答案第二次输入不再算对。主词（下标 0）不算答案。
- 结束时先输出百分比，再输出没猜到的答案（QP 的顺序）。百分比格式不限：`7.142857142857142`、`7.14`、`7.1` 都行，取整时后面要跟 `%`；没猜到的答案一行一个或同一行用空格隔开都行。
- 不测大小写转换（QP 没要求；MS 范例用了 `.lower()`）。

## 英文原题（转写自 QP pp.2–4）

```text
Three source files are used to answer Question 1. The files are called Easy.txt, Medium.txt and
Hard.txt

1  A program outputs a main word. The program asks the user to enter the different words of 3 or
   more letters that can be made from the letters in the main word. These are called the answers.

   There are 3 files: Easy.txt, Medium.txt and Hard.txt. Each file has the main word on the
   first line. For example, the main word in Easy.txt is house.

   The answers are stored in the file. Each answer is on a new line after the main word. For
   example, Easy.txt has 14 answers that can be made from the letters in house.

   The words read from the text file are stored in the global array WordArray. The number of
   words that can be made from the letters in the main word is stored in the global variable
   NumberWords.

   (a) The procedure ReadWords():
       • takes a file name as a parameter
       • opens the file and reads in the data
       • stores the main word in the first element in WordArray
       • stores each answer in a new element in WordArray
       • counts and stores the number of answers.
       Write program code for the procedure ReadWords().
       Save your program as Question1_J24.
       Copy and paste the program code into part 1(a) in the evidence document.          [6]

   (b) The main program asks the user to enter "easy", "medium" or "hard" and calls
       ReadWords() with the filename that matches the user's input. For example, if the user
       enters "easy", the parameter is "Easy.txt".
       Write program code for the main program.
       Save your program.
       Copy and paste the program code into part 1(b) in the evidence document.          [4]

   (c) (i)  The procedure Play():
            • outputs the main word from the array and the number of answers
            • allows the user to enter words until they enter the word 'no' to indicate they
              want to stop
            • outputs whether each word the user enters is an answer or not an answer
            • counts the number of answers the user gets correct
            • replaces each answer that the user gets correct with a null value in the array.
            Write program code for the procedure Play().
            Save your program.
            Copy and paste the program code into part 1(c)(i) in the evidence document.  [6]
       (ii) Amend the procedure Play() so that when the user enters the command to stop, the
            procedure:
            • outputs the percentage of answers the user entered from the array
            • outputs all the answers that the user did not enter.
            Write program code to amend Play().
            Save your program.
            Copy and paste the program code into part 1(c)(ii) in the evidence document. [3]

   (d) (i)   The procedure ReadWords() calls Play() after the data in the file has been read.
             Write program code to amend ReadWords().
             Save your program.
             Copy and paste the program code into part 1(d)(i) in the evidence document. [1]
       (ii)  Test your program by inputting these words in the order shown:
                easy
                she
                out
                no
             Take a screenshot of the output(s).
             Save your program.
             Copy and paste the screenshot into part 1(d)(ii) in the evidence document.  [1]
       (iii) Test your program by inputting these words in the order shown:
                hard
                fine
                fined
                idea
                no
             Take a screenshot of the output(s).
             Save your program.
             Copy and paste the screenshot into part 1(d)(iii) in the evidence document. [1]
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a) | 9618_s24_42:1(a) | 6 | 代码 | `test_1a_read_words_main_word_answers_and_count` · MP2、MP4–MP7；`test_1a_missing_file_handled` · MP3 | MP1 过程头带字符串参数；MP8 关闭文件（max 6） |
| Part 1(b) | 9618_s24_42:1(b) | 4 | 代码 | `test_1b_choice_selects_file` · MP2–MP4；`test_1di_readwords_calls_play_after_loading`、`test_1b_1di_traced_main` · 实际调用、参数与数据链（D46） | MP1 提示语合适 |
| Part 1(c)(i) | 9618_s24_42:1(c)(i) | 6 | 代码 | `test_1c_i_outputs_main_word_and_number_of_answers` · MP1；`test_1c_i_found_and_not_found_messages` · MP2、MP4；`test_1c_i_correct_answer_replaced_with_null` · MP3；`test_1c_i_main_word_is_not_an_answer` · MP2；`test_1c_ii_percentage_counts_each_answer_once` · MP3、MP5；各 `play` 测试以 `no` 结束 · MP6 | MP1 过程头无参数 |
| Part 1(c)(ii) | 9618_s24_42:1(c)(ii) | 3 | 代码 | `test_1c_ii_percentage_counts_each_answer_once`、`test_1c_ii_all_found_is_100_percent` · MP1；`test_1c_ii_outputs_answers_not_entered` · MP2–MP3 | — |
| Part 1(d)(i) | 9618_s24_42:1(d)(i) | 1 | 代码 | `test_1b_choice_selects_file` · 读完文件后调用 Play()；`test_1di_readwords_calls_play_after_loading`、`test_1b_1di_traced_main` · 实际调用、参数与数据链（D46） | — |
| Part 1(d)(ii) | 9618_s24_42:1(d)(ii) | 1 | 截图 | `test_1d_ii_screenshot_easy` · house、14、7.14 %、其余 13 个答案（MS p.13 样例） | 截图里看得到四个输入 |
| Part 1(d)(iii) | 9618_s24_42:1(d)(iii) | 1 | 截图 | `test_1d_iii_screenshot_hard` · fainted、97、3.09 %、其余 94 个答案（MS p.14 样例） | 截图里看得到五个输入 |

## 人工核对清单

- [ ] 全局 `WordArray`、`NumberWords` 建成真实的变量，注释写明类型（D10 ①）。
- [ ] 1(a) MP1：`def ReadWords(FileName):`；MP8：读完关闭文件（或用 `with open(...)`）。
- [ ] 1(b) MP1：提示用户输入 easy / medium / hard。
- [ ] 1(c)(i) MP1：`def Play():` 无参数；查找用循环逐个比较（D10 ③）。
- [ ] 两个截图格：截图清晰、看得到输入与对应输出。

## 说明

- MS 的 Python 范例 `ReadWords` 用 `NumberWords = len(WordArray)`（把主词也算进去），于是 `Play` 里要写 `NumberWords-1` 输出个数，而 `range(1, NumberWords+1)` 又会越界。QP 与 MS MP7 都说 `NumberWords` 是答案个数（不含主词），参考解与测试按 QP（D31）。
- MS p.14 的截图里程序多输出了一行 `97`（调试输出）；测试只查 MS 列出的值。
- 1(d)(i)–(iii) 是 1 分行，语料不拆得分点；其余行语料 `markpoints[].n` 就是 MS 圆点顺序（1(c)(i) 原页 MP3 与 MP4 两个圆点写在一起，语料按两条记）。

### T38c1 · D46 调用与输出核验

原选择测试只看主词与答案数，补测三个文件名传参以及 ReadWords 后真实 Play 调用。再以 ReadWords 的 Play 替身记录已加载数组与计数，真正验证由 ReadWords 内部在读完数据后调用。输出百分比与未答词本来已按内容匹配，无新增容量限制。

测试观测候选文件中的实际模块调用、参数与返回值；结果与调用记录同时核对。注释、指定算法结构、变量接收返回值及截图呈现仍按人工清单检查；自动占比沿用逐点加权口径。
