# 9618_s25_42 第 2 题 · 哈希表与溢出区

## 导读

本练习覆盖 9 个小问，共 22 分。从空白程序完成整道大题；可用 `make try EX=practice/p4/9618_s25_42_q2 K=2b` 按小问测试。标识符、指针初值与文件名照抄 QP（D10）；数组必须建立固定长度的真实 list，并用英文注释写明大小与类型。算法自行编写循环与指针操作，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳。

主程序放在 `if __name__ == "__main__":` 下，避免导入时运行输入；提示写在 `input("…")` 里（D13）。测试通过与人工清单通过之后才能记录掌握（D3）。

## Python 接口

记录类名依 QP 用 `NewRecord(pKey, pItem1, pItem2)`（MS Python 写成 Record）。三字段可用公开属性 Key / Item1 / Item2 或 MS 的 GetKey() / GetItem1() / GetItem2() 读取，测试同时接受，不强加封装。函数名 `Initialise()`、`CalculateHash(Key)`、`InsertIntoHash(TheRecord)`、`CreateHashTable()`、`PrintSpare()`。HashTable 200格、Spare 100格；导入时先建真实 list，Initialise 才将全部槽设为三个 -1 的空记录。只测试有足够 Spare 空间的插入（QP保证），不添加满区异常处理要求。

## 英文原题（QP 原页转写）

```text
2   A program stores data in a 1D array of records, HashTable. The array has space for 200 records.
    Each data item is stored in a specific index of the array that is calculated using an algorithm. The
    index is calculated from the key field using the formula: Key MOD 200

    If two key fields generate the same index, there is a collision. Any records that have a collision
    are stored in a second array, Spare. This array has space for 100 records. When a collision is
    detected, the record is stored in the next free space in Spare.

    (a) The pseudocode record format is:

         TYPE NewRecord

                DECLARE Key : INTEGER

                DECLARE Item1 : INTEGER

                DECLARE Item2 : INTEGER

         ENDTYPE

         Write program code to declare the record type NewRecord

         If your chosen programming language does not support record formats, a class can be used
         instead.

 Save your program as Question2_J25.

 Copy and paste the program code into part 2(a) in the evidence document.
                                                                                                     [2]

    (b) (i)      Write program code to declare the global arrays HashTable and Spare

 Save your program.

 Copy and paste the program code into part 2(b)(i) in the evidence document.
                                                                                                     [1]

         (ii)    An empty record has the integer –1 stored in each field.

                 The procedure Initialise() stores an empty record in each element in HashTable
                 and Spare

                 Write program code for Initialise()

 Save your program.

 Copy and paste the program code into part 2(b)(ii) in the evidence document.
                                                                                                     [2]

(c) The hash value is calculated from the key field using the formula: Key MOD 200

         The function CalculateHash() takes a key field as a parameter and calculates and returns
         the hash value for the key field.

         Write program code for CalculateHash()

 Save your program.

 Copy and paste the program code into part 2(c) in the evidence document.
                                                                                                    [2]

    (d) The procedure InsertIntoHash():

         •     takes a record of type NewRecord as a parameter
         •     uses CalculateHash() to calculate the hash value for the key field in the record
         •     checks if the hash value index in HashTable currently stores an empty record
               ○ if the index stores an empty record, store the parameter in this index
               ○ if the index does not store an empty record, store the parameter in Spare

         You can assume there will always be enough space in Spare to store any collisions.

         Write program code for InsertIntoHash()

 Save your program.

 Copy and paste the program code into part 2(d) in the evidence document.
                                                                                                    [6]

    (e) The text file HashData.txt stores up to 200 rows of data to be stored into the hash table.
        Each row contains three integer numbers separated by commas.

         The first number is the key field, the second number is item 1 and the third number is item 2.

         For example:

         The first row in the text file contains: 646, 12, 568

         The key field is 646, item 1 is 12 and item 2 is 568

         The procedure CreateHashTable():

         •     opens the file HashData.txt
         •     creates a record for each row of data in the file
         •     calls InsertIntoHash() with each record.

         Write program code for CreateHashTable()

 Save your program.

 Copy and paste the program code into part 2(e) in the evidence document.
                                                                                                    [5]

(f)    (i)    The procedure PrintSpare() outputs the key field of each element in the array Spare
                  that does not contain an empty record.

                  Write program code for PrintSpare()

 Save your program.

 Copy and paste the program code into part 2(f)(i) in the evidence document.
                                                                                                       [2]

          (ii)    The main program should call the procedure to initialise the arrays, call the procedure
                  to create the hash table and then call the procedure to output the contents of the array
                  Spare

                  Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 2(f)(ii) in the evidence document.
                                                                                                       [1]

          (iii)   Test your program.

                  Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot into part 2(f)(iii) in the evidence document.
                                                                                                       [1]
```

## 证据文档对照表

已逐格核对官方 evidence.doc；一格一行。MP 编号均为语料 `markpoints[].n`（D37 ②）。一个 MP 同时含函数头与行为时，行为列自动，函数头仍须人工核对；只考结构的 MP 全部列人工。可选点超过行分时，按 `行分 × 自动点分 / 全部点分` 折算，不表示真实考试逐点授分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a) | 9618_s25_42:2(a) | 2 | 代码 | 行为辅助测试（不计自动分） | MP1、MP2；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 2(b)(i) | 9618_s25_42:2(b)(i) | 1 | 代码 | `test_2b_arrays_and_initialise`、`test_2b_no_algorithm_shortcuts` · MPwhole | — |
| Part 2(b)(ii) | 9618_s25_42:2(b)(ii) | 2 | 代码 | `test_2b_arrays_and_initialise` · MP1、MP2 | — |
| Part 2(c) | 9618_s25_42:2(c) | 2 | 代码 | `test_2c_hash` · MP1、MP2 | — |
| Part 2(d) | 9618_s25_42:2(d) | 6 | 代码 | `test_2d_insert_and_collisions`、`test_2d_last_spare_slot` · MP2、MP3、MP4、MP5、MP6 | MP1；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 2(e) | 9618_s25_42:2(e) | 5 | 代码 | `test_2e_create_from_official_data`、`test_2e_missing_file` · MP2、MP3、MP4、MP5、MP6 | MP1；结构、消息语义 / 未触发分支按下方清单及同题 MS 核对 |
| Part 2(f)(i) | 9618_s25_42:2(f)(i) | 2 | 代码 | `test_2f_printspare_empty_partial_full` · MP1、MP2 | — |
| Part 2(f)(ii) | 9618_s25_42:2(f)(ii) | 1 | 代码 | `test_2f_screenshot`、`test_2f_ii_main_call_chain` · MPwhole | — |
| Part 2(f)(iii) | 9618_s25_42:2(f)(iii) | 1 | 截图 | `test_2f_screenshot` · MPwhole | — |

自动测分值 18.166667，人工核对分值 3.833333，自动占比 82.58%。这是验证覆盖口径，自动测试不为未实际核对的写法授分。

## 人工核对清单

- [ ] 9618_s25_42:2(a) MP1：Record/class NewRecord declared（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s25_42:2(a) MP2：3 variables within structure (all integer)（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s25_42:2(d) MP1：Procedure header (and end where appropriate) taking one record as a parameter（1 分；人工核对代码结构 / 声明）。
- [ ] 9618_s25_42:2(e) MP1：Procedure header (and end where appropriate), opening and closing file HashData.txt（1 分；人工核对代码结构 / 声明）。
- [ ] 所有模块头、参数个数与顺序、全局 / 局部作用域符合 QP；所有 list 的类型与大小有英文注释；没有用内置函数替代题目要求的算法（D10 ③）。
- [ ] 给定伪代码的整体流程、没有多余代码、打开与关闭文件位置，由导师按本题 MS 看代码核对。行为正确不替代这些检查。
- [ ] 截图清晰、输入与规定的输出可见；自动测试只验证输出内容，不验证图片本身。

## 原页、编号与差异记录

已看 QP pp.6–8、MS pp.19–32 全部渲染图并放大 MS p.32 截图，核对 evidence.doc 9 格。MS p.32 61个键逐项核对，官方数据重算与图一致。MS Python class Record 与 QP NewRecord 不一致，按 QP 命名；MS PrintSpare 无上界检查，全100格非空会越界，参考解补 X<100，保留按连续填入顺序输出（D31）。Initialise 采用下标赋值满足固定大小数组，不对空 list append。2(a) 两点仅声明结构/类型，分值归人工，字段值测试作辅助。2(e) 六可选点 max5。未印数字MP；语料圆点序号一致。

## T38c2 · D46 验证补充

补测 Initialise → CreateHashTable → PrintSpare；PrintSpare 和截图的整段数字严格相等改为键值有序包含，允许题号/说明数字（QP p.8/MS pp.30–32）。固定 200/100 容量由 QP 指定，保留。

本次行为覆盖：自动 18.166667 分、人工 3.833333 分（82.58%）。调用测试不能代替类型注释、代码结构及证据截图的人工检查。
