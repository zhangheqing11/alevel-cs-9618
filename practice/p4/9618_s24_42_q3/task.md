# 9618_s24_42 Question 3 · 递归与迭代插入排序、递归二分查找

## 中文导读

标识符、文件名照抄题目；真实数组须有类型与大小注释（D10）。题目要求的算法不得用 `sort`、`sorted`、`index`、`in`、`max` 等代劳。主程序放在 `if __name__ == "__main__":` 下，导入时不执行。

## QP 原题英文转写

A program sorts an array of integers and searches the array for a particular value.

(c) The function RecursiveInsertion() can be changed to use iteration instead of recursion.

(d) The recursive function BinarySearch() takes the parameters: IntegerArray – an array of integers; First – the index of the first array element; Last – the index of the last array element; ToFind – an integer to search for in the array. The function uses recursion to perform a binary search for ToFind in IntegerArray. The function returns the index where ToFind is stored or returns −1 if ToFind is not in the array.

### 3(a) [1]

The array of integers, NumberArray, stores the following data in the order given:
            100      85      644      22      15      8      1
        The array is declared and initialised local to the main program.
        Write program code to declare and initialise the array.
 Save your program as Question3_J24.
 Copy and paste the program code into part 3(a) in the evidence document.

### 3(b)(i) [4]

The following recursive pseudocode function sorts the array into ascending order using
            an insertion sort and returns the sorted array.
```text
            DECLARE LastItem : INTEGER
            DECLARE CheckItem : INTEGER
            DECLARE LoopAgain : BOOLEAN
            FUNCTION RecursiveInsertion(IntegerArray : ARRAY[] OF INTEGER,
                            NumberElements : INTEGER) RETURNS ARRAY[] OF INTEGER
                IF NumberElements <= 1 THEN
                    RETURN IntegerArray
                ELSE
                    CALL RecursiveInsertion(IntegerArray, NumberElements - 1)
                    LastItem ← IntegerArray[NumberElements - 1]
                    CheckItem ← NumberElements - 2
                ENDIF
                LoopAgain ← TRUE
                IF CheckItem < 0 THEN
                    LoopAgain ← FALSE
                ELSE
                    IF IntegerArray[CheckItem] < LastItem THEN
                        LoopAgain ← FALSE
                    ENDIF
                ENDIF
                WHILE LoopAgain
                    IntegerArray[CheckItem + 1] ← IntegerArray[CheckItem]
                    CheckItem ← CheckItem - 1
                    IF CheckItem < 0 THEN
                        LoopAgain ← FALSE
                    ELSE
                        IF IntegerArray[CheckItem] < LastItem THEN
                            LoopAgain ← FALSE
                        ENDIF
                    ENDIF
                ENDWHILE
                IntegerArray[CheckItem + 1] ← LastItem
                RETURN IntegerArray
            ENDFUNCTION
```
            Write the program code for the pseudocode function RecursiveInsertion().
 Save your program.
 Copy and paste the program code into part 3(b)(i) in the evidence document.

### 3(b)(ii) [2]

Amend the main program to:
            •   call RecursiveInsertion()with the initialised array NumberArray and the
                number of elements as parameters
            •   output the word ‘Recursive’
            •   output the content of the returned array.
 Save your program.
 Copy and paste the program code into part 3(b)(ii) in the evidence document.

### 3(b)(iii) [1]

Test your program.
            Take a screenshot of the output(s).
 Save your program.
 Copy and paste the screenshot into part 3(b)(iii) in the evidence document.

### 3(c)(i) [4]

Write program code for the function IterativeInsertion()to perform the same
            processes as RecursiveInsertion()but using iteration instead of recursion.
 Save your program.
 Copy and paste the program code into part 3(c)(i) in the evidence document.

### 3(c)(ii) [1]

Write program code to amend the main program to also:
            •   call IterativeInsertion()with the original initialised array NumberArray
            •   output the word ‘iterative’
            •   output the content of the returned array.
 Save your program.
 Copy and paste the program code into part 3(c)(ii) in the evidence document.

### 3(c)(iii) [1]

Test your program.
            Take a screenshot of the output(s).
 Save your program.
 Copy and paste the screenshot into part 3(c)(iii) in the evidence document.

### 3(d)(i) [6]

Write program code for the recursive function BinarySearch().
 Save your program.
 Copy and paste the program code into part 3(d)(i) in the evidence document.

### 3(d)(ii) [2]

Write program code to amend the main program to:
            •   call BinarySearch()with the sorted array and the integer 644 as the search value
            •   output ‘Not found’ if 644 is not found in the array
            •   output the index if 644 is found in the array.
 Save your program.
 Copy and paste the program code into part 3(d)(ii) in the evidence document.

### 3(d)(iii) [1]

Test your program.
            Take a screenshot of the output(s).
 Save your program.
 Copy and paste the screenshot into part 3(d)(iii) in the evidence document.

## Python 接口与 QP / MS 差异

`RecursiveInsertion(IntegerArray, NumberElements)`；`IterativeInsertion(IntegerArray, NumberElements)`（MS 也接受仅数组参数，测试兼容）；`BinarySearch(IntegerArray, First, Last, ToFind)`。
3(c)(i)：MS p.35 的 Python 外循环从 NumberElements 向下递减，不能对原始数组完成升序排序；例如 [3, 2, 1] 得到 [1, 3, 2]。按 QP 改为依次插入长度递增的前缀。
3(c)(ii)：QP 要求 original initialised array；MS p.36 直接复用已被递归排序改变的 NumberArray。参考解给两个排序各传副本，测试检查两次入口数组都为原始顺序。
3(b)(i) 原卷使用无界 ARRAY[] 参数；此处忠实转写，属 QP 原文，不作为 D24 教学新写法。测试不要求输出数组采用 Python 列表格式或逐行输出。

## 证据文档对照表

已用 textutil 读取本卷官方 evidence.doc，以下一行对应一个证据格。编号用语料 markpoints[].n；无拆分的 1 分行记 whole。自动测试与人工核对共同判断，不把自动测试通过等同于获得全部分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_s24_42:3(a) | 1 | 代码 | `test_3a_bii_cii_main_calls_original_arrays` · whole | 局部作用域、7 个 INTEGER 注释 |
| Part 3(b)(i) | 9618_s24_42:3(b)(i) | 4 | 代码 | `test_3bi_recursive_sort` · MP1–MP3；`test_3bi_ci_di_no_builtin_shortcuts` | MP4：照题给结构；MP1 的函数头 |
| Part 3(b)(ii) | 9618_s24_42:3(b)(ii) | 2 | 代码 | `test_3a_bii_cii_main_calls_original_arrays` · MP1；`test_3biii_ciii_diii_screenshots` · MP2；`test_3bii_3cii_3dii_traced_calls_and_results` · 实际调用、参数与数据链（D46） | — |
| Part 3(b)(iii) | 9618_s24_42:3(b)(iii) | 1 | 截图 | `test_3biii_ciii_diii_screenshots` · whole（Recursive + 1 8 15 22 85 100 644） | 截图清晰 |
| Part 3(c)(i) | 9618_s24_42:3(c)(i) | 4 | 代码 | `test_3ci_iterative_sort` · MP1–MP4；`test_3bi_ci_di_no_builtin_shortcuts` | MP1 函数头；插入排序过程而非别种排序 |
| Part 3(c)(ii) | 9618_s24_42:3(c)(ii) | 1 | 代码 | `test_3a_bii_cii_main_calls_original_arrays`、`test_3biii_ciii_diii_screenshots` · whole；`test_3bii_3cii_3dii_traced_calls_and_results` · 实际调用、参数与数据链（D46） | — |
| Part 3(c)(iii) | 9618_s24_42:3(c)(iii) | 1 | 截图 | `test_3biii_ciii_diii_screenshots` · whole（Iterative + 同一升序结果） | 截图清晰 |
| Part 3(d)(i) | 9618_s24_42:3(d)(i) | 6 | 代码 | `test_3di_recursive_binary_search` · MP1–MP7；`test_3bi_ci_di_no_builtin_shortcuts` | MP1 函数头与参数 |
| Part 3(d)(ii) | 9618_s24_42:3(d)(ii) | 2 | 代码 | `test_3biii_ciii_diii_screenshots` · MP1–MP2；`test_3dii_main_not_found_branch` · MP2；`test_3bii_3cii_3dii_traced_calls_and_results` · 实际调用、参数与数据链（D46） | 失败消息语义 |
| Part 3(d)(iii) | 9618_s24_42:3(d)(iii) | 1 | 截图 | `test_3biii_ciii_diii_screenshots` · whole（index 6） | 截图清晰 |

## 人工核对清单

- 数组局部于主程序，注释大小 7 与 INTEGER。
- 3(b)(i) MP4：逐段核对题给伪代码结构，包括 LoopAgain 与界限检查；只看排序结果不够。
- 3(c)(i) 确为插入排序（允许 while / for 的正确实现）；3(d)(i) 确为二分递归。
- 函数头和参数名、截图清晰度、Not found 语义人工核对。
- 3(d)(i) 有 7 个候选点，最多 6 分：统计按比例折算。

## 原页核验与编号对照

QP 10, 11, 12, 13 页；MS 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39 页已查看渲染图；Python 缩进依据原页。各行 MS 圆点顺序与语料 n 对应，无另印不同点号。可选点超过行分值时按点分值比例折算，仅用于覆盖统计，不取代实际批改。

### T38c1 · D46 调用与输出核验

F05：取消整个输出段数字严格相等；按 Recursive / Iterative 段匹配有序子序列，允许 Question 3 等数字说明及逐项换行。补查 BinarySearch 的真实调用、排好数组/0/6/644 参数及返回值；保留两个排序入口原始顺序检查。

测试观测候选文件中的实际模块调用、参数与返回值；结果与调用记录同时核对。注释、指定算法结构、变量接收返回值及截图呈现仍按人工清单检查；自动占比沿用逐点加权口径。
