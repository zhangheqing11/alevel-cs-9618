# 9618_w25_43 第 2 题 · 线性队列与二进制游程压缩

覆盖 7 行，共 24 分。QP 原页：[9, 10, 11]；MS 原页：[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]，已逐页渲染核对。证据格另对照官方 evidence.doc。

## 导读

从 starter.py 的空白分节开始写；标识符、文件名照题目。数组必须建出真实 list，并以英文注释注明类型与大小（D10 ①）；指针初值照题目（D10 ②）。排序、查找及 ADT 操作自己写循环，不用 `sort()`、`sorted()`、`index()`、`max()`、`min()` 或成员测试 `in` 代劳（D10 ③）。主程序置于 `if __name__ == "__main__":` 下，以便测试导入；提示语写在 `input("…")` 中。

## 英文原题（QP 原页转写）

```text
2      A program reads string data from a text file into a linear queue and then compresses the data.

       The queue is created using the global 1D array Queue. The queue can store up to 100 elements.
       Each element is initialised to the empty string ""

       The queue has two pointers that are global to the program:

       •   QueueHead that points to the index of the first element in the queue, initialised to –1
       •   QueueTail that points to the index of the last element in the queue, initialised to –1

       The global variable NumberItems stores the number of elements stored in the queue, initialised
       to 0

       (a) Write program code to declare and initialise Queue, QueueHead, QueueTail and
           NumberItems

    Save your program as Question2_N25.

    Copy and paste the program code into part 2(a) in the evidence document.
                                                                                                         [2]

       (b) The function Enqueue() takes a string as a parameter. The function checks if the queue is
           full, and returns Boolean FALSE if the queue is full.

           If the queue is not full, the parameter is inserted into the next position in Queue. The function
           updates the appropriate pointer(s), updates NumberItems and then returns Boolean TRUE

           Write program code for Enqueue()

    Save your program.

    Copy and paste the program code into part 2(b) in the evidence document.
                                                                                                         [5]

       (c) The function Dequeue() returns the string "False" if the queue is empty.

           If the queue is not empty, the function returns the next element in the queue. The function
           updates the appropriate pointer(s) and updates NumberItems

           Write program code for Dequeue()

    Save your program.

    Copy and paste the program code into part 2(c) in the evidence document.
                                                                                                         [3]

(d) The text file BinaryData.txt stores individual binary digits, '1' and '0'. Each digit is on
        a new line. For example, the first line in the text file stores '1', the second line stores '1'

         The procedure ReadData() reads in each line from the text file BinaryData.txt and
         inserts it into the queue using the appropriate method.

         The procedure needs to work for a text file with any number of lines up to a maximum of 100.

         Write program code for ReadData()

 Save your program.

 Copy and paste the program code into part 2(d) in the evidence document.
                                                                                                    [5]

    (e) The string data in the text file is compressed.

         The compression algorithm counts the number of times each binary digit appears
         consecutively, then stores the binary digit followed by the number of times it appears. The
         algorithm stores the compressed data in a single string.

         For example, if the text file contains the data:

               1
               1
               0
               0
               0
               1
               1
               1

         The compression algorithm will create the string "120313" because there are two '1' digits,
         followed by three '0' digits, followed by three '1' digits.

         The procedure Compress() uses Dequeue() to remove each element from the queue in
         turn. The procedure then compresses the data following the compression algorithm described.
         The new compressed string is stored in the global variable NewString

         You can assume that one binary digit will never appear more than nine times consecutively in
         the sequence.

         You can assume that there will always be at least one item in the queue.

         Write program code for Compress()

 Save your program.

 Copy and paste the program code into part 2(e) in the evidence document.
                                                                                                    [6]

(f)   (i)    Write program code for the main program to:

                 •   call ReadData()
                 •   call Compress()
                 •   output the content of the compressed string.

 Save your program.

 Copy and paste the program code into part 2(f)(i) in the evidence document.
                                                                                        [2]

          (ii)   Test your program.

                 Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot(s) into part 2(f)(ii) in the evidence document.
                                                                                        [1]
```

## Python 接口与测试约定

- 全局 `Queue` 100 格空字符串，`QueueHead=-1`、`QueueTail=-1`（尾指针是最后一格），`NumberItems=0`。与其他题“下一空格”约定不同。
- `Enqueue(TheData)` 返回布尔值；`Dequeue()` 空时返回字符串 `False`，不是布尔 False。`ReadData()`、`Compress()` 按 QP 名字；压缩结果存全局 NewString。
- 使用 BinaryData.txt，ReadData 另测 0–100 行文件（含末行不换行）。Compress 只测至少一项、每段连续次数最多 9 的数据，符合 QP 假设。
- 不规定线性队列耗尽后的重置/复用策略，不要求循环回绕。读文件失败信息不限措辞；文件异常只在 ReadData 的函数测试中核对。

## 证据文档对照表

表内 MP 号取语料 markpoints[].n。每行列出自动与人工主归属；类型注释、函数头和截图可读性仍须人工核对。自动占比只统计可观察行为，并非自动给出考试分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a) | 9618_w25_43:2(a) | 2 | 代码 | `test_2a_globals` · MP1、MP2 | — |
| Part 2(b) | 9618_w25_43:2(b) | 5 | 代码 | `test_2b_last_used_tail_capacity` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 2(c) | 9618_w25_43:2(c) | 3 | 代码 | `test_2c_dequeue_string_false_and_fifo` · MP1、MP2、MP3 | — |
| Part 2(d) | 9618_w25_43:2(d) | 5 | 代码 | `test_2d_reads_official_file`；`test_2d_any_file_length_to_100`；`test_2d_missing_file` · MP3、MP4、MP5、MP6 | MP1 Procedure header (and end where appropriate)；MP2 Opening the file and closing the file (in appropriate place) |
| Part 2(e) | 9618_w25_43:2(e) | 6 | 代码 | `test_2e_compress_all_runs_including_final_singleton` · MP1、MP2、MP3、MP4、MP5、MP6 | — |
| Part 2(f)(i) | 9618_w25_43:2(f)(i) | 2 | 代码 | `test_2f_ii_screenshot_official_compressed_output` · MP1、MP2 | — |
| Part 2(f)(ii) | 9618_w25_43:2(f)(ii) | 1 | 截图 | `test_2f_ii_screenshot_official_compressed_output` · MPwhole | — |

## 人工核对清单

- [ ] 2(d) MP1：Procedure header (and end where appropriate)
- [ ] 2(d) MP2：Opening the file and closing the file (in appropriate place)
- [ ] 数组、指针与记录字段的英文类型注释及作用域正确，数组大小与 QP 一致。
- [ ] 按 QP 写指定算法；没有以内置容器操作代替数组 ADT 或查找、排序步骤。
- [ ] 所有截图清晰；输入、输出和要求的文件名可见；截图不能仅由 pytest 成功代替。
- [ ] 2(b) MP1、2(c) MP1、2(e) MP1 含模块头；行为自动，头部人工。2(d) MP6 的文件访问是否全部位于 try 内人工查看。

## QP / MS 差异与点号对照

- MS p.21 Python 初始化多缩进一级，p.23 Enqueue 条件混入 `{` 且缺冒号；参考解修正为合法 Python。
- MS p.27 ReadData 漏异常处理；参考解补上其 MP6 要求，源文件内容不改。
- MS p.29 Compress 外循环为 `while NumberItems > 0 and First != "False"`：First 已经保存一个出队项，队列余量为 0 不代表 First 无效。该范例会漏掉单项输入及最后仅 1 项的游程。参考解/测试按 QP p.10 完整压缩，外循环只检查 First 不是字符串 False（D31）；原 MS 得分点仍保留。
- 官方文件压缩结果仍为 MS p.31 的 19051306；附加 `1` → `11`、`01` → `0111` 等边界抓取上述缺陷。

2(d) 6 个候选点最多 5 分，按权重比例折算。其余语料编号与 MS 圆点顺序一致。Compress 的哨兵终止与按 NumberItems 终止只要完整处理最后一段，行为测试都接受。
