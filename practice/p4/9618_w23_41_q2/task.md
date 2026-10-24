# 9618_w23_41 第 2 题 · 游戏 ID 线性队列与记录汇总

覆盖 10 行，共 29 分。QP 原页：[4, 5, 6, 7]；MS 原页：[9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]，已逐页渲染核对。证据格另对照官方 evidence.doc。

## 导读

从 starter.py 的空白分节开始写；标识符、文件名照题目。数组必须建出真实 list，并以英文注释注明类型与大小（D10 ①）；指针初值照题目（D10 ②）。排序、查找及 ADT 操作自己写循环，不用 `sort()`、`sorted()`、`index()`、`max()`、`min()` 或成员测试 `in` 代劳（D10 ③）。主程序置于 `if __name__ == "__main__":` 下，以便测试导入；提示语写在 `input("…")` 中。

## 英文原题（QP 原页转写）

```text
2   A linear queue is implemented using the 1D array, Queue. The index of the first element in the
    array is 0.

    (a) (i)     Write program code to declare:

                •   Queue — a global array with space to store 50 IDs of type string
                •   HeadPointer — a global variable to point to the first element in the queue,
                    initialised to −1
                •   TailPointer — a global variable to point to the next available space in the queue,
                    initialised to 0.

 Save your program as Question2_N23.

 Copy and paste the program code into part 2(a)(i) in the evidence document.
                                                                                                          [2]

         (ii)   The procedure Enqueue() takes a string parameter.

                If the queue is full, the procedure outputs a suitable message. If the queue is not full, the
                procedure inserts the parameter into the queue and updates the relevant pointer(s).

                Write program code for Enqueue().

 Save your program.

 Copy and paste the program code into part 2(a)(ii) in the evidence document.
                                                                                                          [4]

        (iii)   The function Dequeue() checks if the queue is empty.

                If the queue is empty, the function outputs a suitable message and returns the string
                "Empty".
                If the queue is not empty, the function returns the first element in the queue and updates
                the relevant pointer(s).

                Write program code for Dequeue().

 Save your program.

 Copy and paste the program code into part 2(a)(iii) in the evidence document.
                                                                                                          [4]

(b) A shop sells computer games. Each game has a unique identifier (ID) of string data type.

         The text file QueueData.txt contains a list of game IDs.

         The procedure ReadData() reads the data from the text file and inserts each item of data
         into the array Queue.

         Write program code for the procedure ReadData().

 Save your program.

 Copy and paste the program code into part 2(b) in the evidence document.
                                                                                                   [6]

    (c) Some game IDs appear in the text file more than once.

         The program needs to total the number of times each game ID appears in the text file.

         The record structure RecordData has the following fields:

         •      ID — a string to store the game ID
         •      Total — an integer to store the total number of times that game ID appears in the text
                file.

          (i)   Write program code to declare the record structure RecordData.

                If you are writing in Python, include attribute declarations as comments.

 Save your program.

 Copy and paste the program code into part 2(c)(i) in the evidence document.
                                                                                                   [2]

         (ii)   The global 1D array Records stores up to 50 items of type RecordData.

                The global variable NumberRecords stores the number of records currently in the array
                Records and is initialised to 0.

                Write program code to declare Records and NumberRecords.

                If you are writing in Python, include attribute declarations as comments.

 Save your program.

 Copy and paste the program code into part 2(c)(ii) in the evidence document.
                                                                                                   [2]

(iii)   The pseudocode algorithm for the procedure TotalData():

                •   uses Dequeue() to remove an ID from the queue
                •   checks whether a RecordData with the returned ID exists in Records
                •   increments the total for that ID in the record if the ID already exists
                •   creates a new record and stores it in Records if the ID does not exist.

                PROCEDURE TotalData()
                    DECLARE DataAccessed : STRING
                    DECLARE Flag : BOOLEAN
                    DataAccessed       ← Dequeue()
                    Flag    ← FALSE
                    IF NumberRecords = 0 THEN
                       Records[NumberRecords].ID ← DataAccessed
                       Records[NumberRecords].Total ← 1
                       Flag ← TRUE
                       NumberRecords ← NumberRecords + 1
                     ELSE
                       FOR X    ← 0 TO NumberRecords - 1
                            IF Records[X].ID = DataAccessed THEN
                               Records[X].Total         ← Records[X].Total + 1
                                Flag   ← TRUE
                             ENDIF
                           NEXT X
                    ENDIF
                    IF Flag = FALSE THEN
                       Records[NumberRecords].ID ← DataAccessed
                       Records[NumberRecords].Total ← 1
                       NumberRecords ← NumberRecords + 1
                    ENDIF
                ENDPROCEDURE

                Write program code for the procedure TotalData().

 Save your program.

 Copy and paste the program code into part 2(c)(iii) in the evidence document.
                                                                                              [5]

(d) The procedure OutputRecords() outputs the ID and total of each record in Records in the
        format:

                ID   1234     Total      4

         Write program code for OutputRecords().

 Save your program.

 Copy and paste the program code into part 2(d) in the evidence document.
                                                                                            [1]

    (e) The main program needs to:

         •      call ReadData()
         •      call TotalData() for each element in the queue
         •      call OutputRecords().

          (i)   Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 2(e)(i) in the evidence document.
                                                                                            [2]

         (ii)   Test your program.

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 2(e)(ii) in the evidence document.
                                                                                            [1]
```

## Python 接口与测试约定

- 全局 `Queue`（50 格 STRING）、`HeadPointer=-1`、`TailPointer=0`；`Enqueue(Data)`、`Dequeue()`、`ReadData()`、`TotalData()`、`OutputRecords()` 使用 QP 名字。
- `RecordData` 可公开 `ID`/`Total` 字段，也可采用 MS 的 `GetID()` / `GetTotal()` 访问接口；构造方法自行设计，测试不强制额外构造签名。
- `Records` 建成 50 个真实格子，`NumberRecords=0`。按 D10 ①，不能只写空 list；`Enqueue` 和创建记录按下标写入，替换 MS 的 append。
- 使用官方 `QueueData.txt`，函数型文件测试在临时副本目录运行；不规定满/空/缺文件提示的具体措辞。2(d) 输出按 QP 的 ID / Total 格式，空白宽度不限。

## 证据文档对照表

表内 MP 号取语料 markpoints[].n。每行列出自动与人工主归属；类型注释、函数头和截图可读性仍须人工核对。自动占比只统计可观察行为，并非自动给出考试分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a)(i) | 9618_w23_41:2(a)(i) | 2 | 代码 | `test_2a_i_globals` · MP1、MP2 | — |
| Part 2(a)(ii) | 9618_w23_41:2(a)(ii) | 4 | 代码 | `test_2a_ii_enqueue_full` · MP2、MP3、MP4 | MP1 Procedure Enqueue() header (and close where appropriate) with one (string) parameter |
| Part 2(a)(iii) | 9618_w23_41:2(a)(iii) | 4 | 代码 | `test_2a_iii_dequeue_empty_and_fifo` · MP2、MP3、MP4、MP5 | MP1 Function header Dequeue() (and end where appropriate) with no parameter |
| Part 2(b) | 9618_w23_41:2(b) | 6 | 代码 | `test_2b_read_official_file`；`test_2b_missing_file` · MP2、MP4、MP5、MP6、MP7 | MP1 Procedure header ReadData() with no parameters；MP3 … and closing file |
| Part 2(c)(i) | 9618_w23_41:2(c)(i) | 2 | 代码 | — | MP1 Declaration of record type/class RecordData；MP2 ID as a string and total as an Integer |
| Part 2(c)(ii) | 9618_w23_41:2(c)(ii) | 2 | 代码 | `test_2a_i_globals` · MP1、MP2 | — |
| Part 2(c)(iii) | 9618_w23_41:2(c)(iii) | 5 | 代码 | `test_2c_iii_total_first_existing_and_new` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 2(d) | 9618_w23_41:2(d) | 1 | 代码 | `test_2d_output_records` · MPwhole | — |
| Part 2(e)(i) | 9618_w23_41:2(e)(i) | 2 | 代码 | `test_2e_ii_screenshot_totals` · MP1、MP2 | — |
| Part 2(e)(ii) | 9618_w23_41:2(e)(ii) | 1 | 截图 | `test_2e_ii_screenshot_totals` · MPwhole | — |

## 人工核对清单

- [ ] 2(a)(ii) MP1：Procedure Enqueue() header (and close where appropriate) with one (string) parameter
- [ ] 2(a)(iii) MP1：Function header Dequeue() (and end where appropriate) with no parameter
- [ ] 2(b) MP1：Procedure header ReadData() with no parameters
- [ ] 2(b) MP3：… and closing file
- [ ] 2(c)(i) MP1：Declaration of record type/class RecordData
- [ ] 2(c)(i) MP2：ID as a string and total as an Integer
- [ ] 数组、指针与记录字段的英文类型注释及作用域正确，数组大小与 QP 一致。
- [ ] 按 QP 写指定算法；没有以内置容器操作代替数组 ADT 或查找、排序步骤。
- [ ] 所有截图清晰；输入、输出和要求的文件名可见；截图不能仅由 pytest 成功代替。
- [ ] 2(c)(iii) 对照 QP p.6 的 Flag、首次记录、遍历查重和未找到分支，不能只看最终计数。

## QP / MS 差异与点号对照

- MS pp.9、17 的 Python 范例为空 list（且 p.17 把 NumberRecords 声明写进注释），按 D10 ① 改为 50 格数组和独立的 NumberRecords 赋值。
- MS p.21 `TotalData` 的末行 NumberRecords += 1 多缩进一级；参考解对照 QP p.6 修正。
- MS p.24 把 `OutputRecords()` 缩进在 while 内，导致重复输出中间结果；参考解按 QP p.7 在全部汇总后输出一次。
- MS p.24 主程序把 HeadPointer 改成 0；本练习保留 QP 初值 -1，首次入队置 0；空队列主循环用额外判断避免从 -1 开始读。

2(a)(iii) 有 5 个候选点，最多 4 分；2(b) 有 7 个候选点，最多 6 分，均按候选点权重比例折算。2(c)(iii) 语料 MP1 是递增 NumberRecords，MP2 是模块头与 Dequeue，MP3–MP5 为三个分支；MS 没有印数字编号，顺序照圆点。
