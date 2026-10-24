# 9618_w25_41 第 3 题 · 二维哈希桶与公开记录对象

覆盖 8 行，共 25 分。QP 原页：[9, 10, 11, 12]；MS 原页：[26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]，已逐页渲染核对。证据格另对照官方 evidence.doc。

## 导读

从 starter.py 的空白分节开始写；标识符、文件名照题目。数组必须建出真实 list，并以英文注释注明类型与大小（D10 ①）；指针初值照题目（D10 ②）。排序、查找及 ADT 操作自己写循环，不用 `sort()`、`sorted()`、`index()`、`max()`、`min()` 或成员测试 `in` 代劳（D10 ③）。主程序置于 `if __name__ == "__main__":` 下，以便测试导入；提示语写在 `input("…")` 中。

## 英文原题（QP 原页转写）

```text
3      A program stores records in the 2D array HashTable. Each record is stored at a specific index of
       the array that is calculated using a hashing algorithm with the record’s key field.

       The array has 100 × 10 elements. The hashing algorithm uses the key to generate an index
       between 0 and 99 (inclusive). If two key fields generate the same index, there is a collision. Any
       records that have a collision are stored in the next space in the same index.

       For example: In this table two record keys generated the same hash value of 1. Four record keys
       generated the same hash value of 3.

         Index        0          1          2             3        4          5          …          9

           0        record

           1        record     record

           2

           3        record     record    record      record

           4

           …

           99


       The program uses Object-Oriented Programming (OOP).

       (a) The class Record stores data about the records:

                                                    Record

        Key : Integer                               stores the integer key field for the data

        Data : String                               stores the string data
        Constructor()                               initialises Key and Data to its parameter values


           The attributes Key and Data are public.

           Write program code to declare the class Record and its constructor.

           Use your programming language appropriate constructor.

    Save your program as Question3_N25.

    Copy and paste the program code into part 3(a) in the evidence document.
                                                                                                        [2]

(b) The procedure InitialiseHashTable() initialises each element in the array to an empty
        or null record.

         Write program code to declare the global 2D array HashTable and the procedure
         InitialiseHashTable()

 Save your program.

 Copy and paste the program code into part 3(b) in the evidence document.
                                                                                               [2]

    (c) The function Hash():

         •     takes an integer key field as a parameter
         •     calculates and returns the hash value of the key field.

         The hash value is the result from the formula: key MOD 100

         Write program code for Hash()

 Save your program.

 Copy and paste the program code into part 3(c) in the evidence document.
                                                                                               [2]

    (d) The procedure InsertData():

         •     takes an object of type Record as a parameter
         •     calculates the hash value for the parameter using the appropriate function
         •     stores the parameter in the correct position in HashTable

         You can assume there will be no more than 10 objects that generate the same hash value.

         Write program code for InsertData()

 Save your program.

 Copy and paste the program code into part 3(d) in the evidence document.
                                                                                               [4]

(e) The file "HashTableData.txt" stores 200 key values and string data items in the format:
                    key,string

          For example, the first row in the text file is:
                    528,permission

          The key is 528 and the string data is "permission"

          The procedure ReadData():

          •    opens the text file and reads each line
          •    splits each line into the key and data
          •    calls InsertData() with an object containing each key and matching data.

          Write program code for ReadData()

 Save your program.

 Copy and paste the program code into part 3(e) in the evidence document.
                                                                                                   [5]

    (f)   The function GetRecord():

          •    takes an integer key field as a parameter
          •    calculates the hash value for the key field using the appropriate function
          •    searches the hash table for the record with the matching key field
          •    returns the data for the record if the record is found
          •    returns "Not found" if the record is not found.

          Write program code for GetRecord()

 Save your program.

 Copy and paste the program code into part 3(f) in the evidence document.
                                                                                                   [5]

(g) The main program:

              •      calls InitialiseHashTable() and ReadData()
              •      takes five integer key fields as input from the user
              •      calls GetRecord() with each input and outputs the return value.

              (i)    Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 3(g)(i) in the evidence document.
                                                                                                                                                         [3]

             (ii)    Test your program with the following five inputs in the order given:

                            528

                            1128

                            1828

                            1062

                            39

                     Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot(s) into part 3(g)(ii) in the evidence document.
                                                                                                                                                         [2]
```

## Python 接口与测试约定

- `Record(pKey, pData)` 公共属性为 `Key`（整数）、`Data`（字符串）。`HashTable` 全局固定 100×10；空记录可用 None 或 Key=-1 的 Record，记录字符串初值可按 MS 使用空串。
- `InitialiseHashTable()`、`Hash(Key)`、`InsertData(RecordData)`、`ReadData()`、`GetRecord(Key)` 按 QP 名字。
- QP 保证每个桶最多 10 项，测试只填到第 10 格，不自行要求第 11 次冲突时的策略；不测试 QP 未定义的重复 key 策略。
- 使用官方 HashTableData.txt，所有行逐字节复制；读入后 data 不含行尾。截图按 MS 列出的五个词的顺序查找，提示语不限。

## 证据文档对照表

表内 MP 号取语料 markpoints[].n。每行列出自动与人工主归属；类型注释、函数头和截图可读性仍须人工核对。自动占比只统计可观察行为，并非自动给出考试分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_w25_41:3(a) | 2 | 代码 | `test_3a_public_record_constructor` · MP2 | MP1 Class header (and end) and constructor header (and end) in class |
| Part 3(b) | 9618_w25_41:3(b) | 2 | 代码 | `test_3b_initialise_all_cells` · MP1、MP2 | — |
| Part 3(c) | 9618_w25_41:3(c) | 2 | 代码 | `test_3c_hash_modulo` · MP1、MP2 | — |
| Part 3(d) | 9618_w25_41:3(d) | 4 | 代码 | `test_3d_insert_collision_slots_once` · MP2、MP3、MP4 | MP1 Procedure header (and end) taking one Record parameter |
| Part 3(e) | 9618_w25_41:3(e) | 5 | 代码 | `test_3e_reads_official_records`；`test_3e_missing_file_handled` · MP2、MP3、MP4、MP5、MP6 | MP1 Procedure header (and end), opening file and closing file (in appropriate place) |
| Part 3(f) | 9618_w25_41:3(f) | 5 | 代码 | `test_3f_getrecord_last_collision_and_missing` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 3(g)(i) | 9618_w25_41:3(g)(i) | 3 | 代码 | `test_3g_ii_screenshot_words` · MP1、MP2、MP3 | — |
| Part 3(g)(ii) | 9618_w25_41:3(g)(ii) | 2 | 截图 | `test_3g_ii_screenshot_words` · MP1、MP2 | — |

## 人工核对清单

- [ ] 3(a) MP1：Class header (and end) and constructor header (and end) in class
- [ ] 3(d) MP1：Procedure header (and end) taking one Record parameter
- [ ] 3(e) MP1：Procedure header (and end), opening file and closing file (in appropriate place)
- [ ] 数组、指针与记录字段的英文类型注释及作用域正确，数组大小与 QP 一致。
- [ ] 按 QP 写指定算法；没有以内置容器操作代替数组 ADT 或查找、排序步骤。
- [ ] 所有截图清晰；输入、输出和要求的文件名可见；截图不能仅由 pytest 成功代替。
- [ ] 3(b) MP2、3(c) MP1、3(f) MP1 含模块头；行为自动检查，模块声明人工复核。3(e) MP6 的全部文件访问均位于 try 内须人工查看。

## QP / MS 差异与点号对照

- MS p.30 Python InsertData 缺成功后的 break/return，会把一个记录写满该桶；参考解按 QP p.10 的“下一空格”要求，在写入一次后退出。
- MS p.32 ReadData 先把 Line.strip() 赋给 Data，下一行却又用 Line.split() 覆盖，保留换行；参考解对去掉行尾后的文本 split。同时补上 MS MP6 的文件异常处理（范例漏写不等于该点不要求）。
- HashTable 按 D10 ① 在导入时已有真实 100×10 格；InitialiseHashTable 再填空记录，不只声明空 list。
- MS Python 的空记录共享对象写法在整体替换槽位时可行；测试不对空记录对象身份过拟合。

3(d) MS p.29 第 3 圆点含无冲突与有冲突的两段，语料拆成 MP3 / MP4。3(e) 有 6 个候选点，最多 5 分，按权重比例折算；MP1 归人工（函数头和文件关闭位置），MP2–MP6 归行为自动。
