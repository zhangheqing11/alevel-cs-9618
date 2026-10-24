# 9618_s25_41 Question 2 · 读取文件、按颜色拆分、追加写文件

## 中文导读

标识符、文件名照抄题目；真实数组须有类型与大小注释（D10）。题目要求的算法不得用 `sort`、`sorted`、`index`、`in`、`max` 等代劳。主程序放在 `if __name__ == "__main__":` 下，导入时不执行。

## QP 原题英文转写

A program reads data from a text file, splits the data depending on its content and stores the separated data into different files.

The text file TheData.txt contains 72 lines of data. Each line of data has an integer number and a string colour that are separated by a comma. For example, the first line in the file is:

```text
10,red
```

The integer is 10 and the string is "red". The file contains six different colours: red, green, blue, orange, yellow, pink.

(e) The main program calls ReadData() and then SplitData().

### 2(a) [7]

The function ReadData():
        •   prompts the user to enter a filename and reads this filename from the user
        •   opens the file and reads each line of data into a 1D array
        •   returns the populated 1D array.
        The function needs to work for a file that contains an unknown number of lines.
        Write program code for ReadData()
 Save your program as Question2_J25.
 Copy and paste the program code into part 2(a) in the evidence document.

### 2(b) [6]

The procedure SplitData() takes a 1D string array as a parameter with the identifier
        DataArray
        The procedure declares six 1D arrays: one array for each colour that appears in the file (red,
        green, blue, orange, yellow, pink).
        The procedure accesses each string in DataArray. The data in each string is split into the
        integer and the colour. The integer is stored in the array that matches the colour.
        For example, the first string in DataArray has the integer 10 and the colour red, so the
        integer 10 is stored in the array for the colour red.
        Write program code for SplitData()
 Save your program.
 Copy and paste the program code into part 2(b) in the evidence document.

### 2(c) [5]

The procedure StoreData():
        •   takes two parameters: a 1D array DataToStore and a filename
        •   opens the text file with the filename that is passed as a parameter
        •   appends each item of data from DataToStore to a new line in the text file
        •   uses exception handling when opening and writing data to the text file.
        Write program code for StoreData()
 Save your program.
 Copy and paste the program code into part 2(c) in the evidence document.

### 2(d) [2]

Each of the six colours has a blank text file where the numbers will be stored. The names of
        these six text files are:
        •   Blue.txt
        •   Green.txt
        •   Orange.txt
        •   Pink.txt
        •   Red.txt
        •   Yellow.txt
        The procedure SplitData() needs amending to call StoreData() six times, with each of
        the six colour arrays and the name of the text file that corresponds to that colour.
        For example, StoreData() will be called with the red array and the file name "Red.txt"
        Write program code to amend SplitData()
 Save your program.
 Copy and paste the program code into part 2(d) in the evidence document.

### 2(e)(i) [3]

Write program code for the main program.
 Save your program.
 Copy and paste the program code into part 2(e)(i) in the evidence document.

### 2(e)(ii) [2]

Test your program. Input the text "TheData.txt" when prompted.
            Take a screenshot of the output(s) and a screenshot showing the content of the file that
            stores the red numbers.
 Save your program.
 Copy and paste the screenshot(s) into part 2(e)(ii) in the evidence document.

## Python 接口与 QP / MS 差异

`ReadData()` 返回字符串列表；`SplitData(DataArray)` 无返回值，声明六个局部整数数组并分别调用 `StoreData(DataToStore, FileName)`；`StoreData` 追加写整数。按 MS 接口命名；数组在数据到达时增长（未知行数，不要求预留任意固定上限）。
2(a)：MS p.19 Python 直接 append(Line)，未去换行；按该行 MP6 与 QP 数据格式去除 CR/LF，否则分色失败。
2(b)/2(c)：MS p.21 将 SplitLine[0] 字符串加入数组，p.26 直接 write(Item)；QP 明确数组存 integer，参考解先 int()，写时 str()。
未知/损坏颜色和文件缺失时的返回数组内容 QP 未定义，测试不替题目规定；文件不存在须有异常消息。输出措辞不固定。官方空色文件一并复制，追加测试不覆写已有行。

## 证据文档对照表

已用 textutil 读取本卷官方 evidence.doc，以下一行对应一个证据格。编号用语料 markpoints[].n；无拆分的 1 分行记 whole。自动测试与人工核对共同判断，不把自动测试通过等同于获得全部分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a) | 9618_s25_41:2(a) | 7 | 代码 | `test_2a_read_official_file`、`test_2a_unknown_line_count` · MP2、MP4–MP7；`test_2a_missing_file` · MP8 | MP1 函数头；MP3 打开与关闭位置；提示语适当 |
| Part 2(b) | 9618_s25_41:2(b) | 6 | 代码 | `test_2b_d_split_six_integer_arrays`、`test_2b_d_split_official_and_empty_groups` · MP2–MP6 | MP1 函数头；六个数组声明与类型注释 |
| Part 2(c) | 9618_s25_41:2(c) | 5 | 代码 | `test_2c_append_new_lines` · MP1–MP4；`test_2c_open_error`、`test_2c_write_error` · MP5 | MP1 函数头、文件关闭位置；try 覆盖所有读写；消息语义 |
| Part 2(d) | 9618_s25_41:2(d) | 2 | 代码 | `test_2b_d_split_six_integer_arrays`、`test_2b_d_split_official_and_empty_groups` · MP1–MP2 | — |
| Part 2(e)(i) | 9618_s25_41:2(e)(i) | 3 | 代码 | `test_2ei_eii_screenshot_files` · MP1–MP3（完整链 ReadData → SplitData → 文件） | 调用 ReadData 与 SplitData，而非在主程序重写逻辑 |
| Part 2(e)(ii) | 9618_s25_41:2(e)(ii) | 2 | 截图 | `test_2ei_eii_screenshot_files` · MP1（文件名输入、提示存在）、MP2（Red.txt 内容） | 截图显示输入 TheData.txt、文件名与红色数据同屏可见、截图清晰 |

## 人工核对清单

- 按 MS 人工查 ReadData 函数头与打开/关闭位置（MP1、MP3），SplitData 函数头（MP1）。
- StoreData MP1 含函数头、追加行为、关闭位置；追加可自动测，函数头与关闭位置人工核对。
- 六个 INTEGER 数组及动态大小注释；实际局部数组由传给 StoreData 的值检查，不强制数组变量名。
- e(i) 调用链与返回值使用人工复核，e(ii) 文件名必须与数据同屏，输入与提示必须可见，截图须清晰。
- 2(a) 8 个可选点最多 7 分：按分值比例折算。

## 原页核验与编号对照

QP 4, 5 页；MS 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 页已查看渲染图；Python 缩进依据原页。各行 MS 圆点顺序与语料 n 对应，无另印不同点号。可选点超过行分值时按点分值比例折算，仅用于覆盖统计，不取代实际批改。
