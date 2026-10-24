# 9618_w25_43 第 1 题 · BoardObject 与 Board：二维对象数组与命中判断

## 导读与 Python 接口

从空白程序完成整道题。标识符与文件名照抄 QP；数组须建立真实 list 并以英文注释类型与大小；QP 要求私有的属性使用双下划线。主程序写在 `if __name__ == "__main__":` 下，提示语放在 `input()` 中。指定的算法自行实现，不用内置 sort / index / max 等代劳（D10）。

接口照 QP / MS Python：`BoardObject(Code, Value)`、`Board()`、`GetObject(row, column)`、`SetObject(TheObject, row, column)`、`DisplayBoard()`。Object1–Object5 是题给标识符，必须保留；主程序 Board 实例名不限。QP p.4 的网格图是行/列均0–9，黑格在 row1,column3，表示两个下标的含义，已在图旁原文转写；无额外数据。无数据文件，BinaryData.txt 属第2题。MS p.16 的完整棋盘与 p.19 输入10/4/-1/5的 C 5 输出已核对；Python 范例无需行为修正。本题未强制 private，公有/私有实现都可。

## 英文原题（已对照 QP 原页）

### QP p.2

```text
2

You have been supplied with the following source files:

BinaryData.txt



Open the evidence document, evidence.doc

Make sure that your name, centre number and candidate number will appear on every page of this
document. This document must contain your answers to each question.

Save this evidence document in your work area as:
evidence_ followed by your centre number_candidate number, for example: evidence_zz999_9999

A class declaration can be used to declare a record. If the programming language used does not
support arrays, a list can be used instead.

One source file is used to answer Question 2. The file is called BinaryData.txt

1      A program stores data for a board game using Object-Oriented Programming (OOP). The game
       has objects that are placed on the board. Each object has a string code (for example "A") and an
       integer value (for example, 2).

       The class BoardObject stores the data about the objects that can be placed on the board:

                                               BoardObject
        Code : String                   stores the board object’s code

        Value : Integer                 stores the integer value of the board object


        Constructor()                   initialises the attributes to the parameter values

        GetCode()                       returns Code

        GetValue()                      returns Value


       (a) (i)   Write program code to declare the class BoardObject and its constructor.

                 Do not declare the other methods.

                 Use your programming language appropriate constructor.

                 If you are writing in Python, include attribute declarations using comments.

    Save your program as Question1_N25.

    Copy and paste the program code into part 1(a)(i) in the evidence document.
                                                                                                    [5]




© UCLES 2025                                    9618/43/O/N/25
```

### QP p.3

```text
3

         (ii)   The methods GetCode() and GetValue() return the appropriate attribute.

                Write program code for GetCode() and GetValue()

 Save your program.

 Copy and paste the program code into part 1(a)(ii) in the evidence document.
                                                                                                  [3]

        (iii)   The table shows the code and value of five board objects. The table has the variable
                identifier where each of the objects are stored.

                    Variable
                                     Code            Value
                   identifier
                 Object1             "A"                       2
                 Object2             "B"                       3
                 Object3             "C"                       5
                 Object4             "D"                       2
                 Object5             "E"                       7

                Write program code for the main program to instantiate each of the five board objects
                and store them in the variables with the identifiers given.

 Save your program.

 Copy and paste the program code into part 1(a)(iii) in the evidence document.
                                                                                                  [3]




© UCLES 2025                                  9618/43/O/N/25                              [Turn over
```

### QP p.4

```text
4

    (b) The board objects are placed on a board that is represented by a 0-indexed 2D array:

         •     the board is a 10 x 10 grid
         •     each position on the board is identified by a row and column number
         •     rows are numbered 0 to 9
         •     columns are numbered 0 to 9
         •     board objects can be placed at a row and column position
         •     each board position is initialised with an empty BoardObject, an empty BoardObject
               has Code = "-" and Value = 0

         For example, the element highlighted in the given board is in row 1 and column 3.

                      Row                          Column
                              0    1    2    3     4     5       6    7     8    9
                          0
                          1
                          2
                          3
                          4
                          5
                          6
                          7
                          8
                          9

         The class Board stores the data about the board and where the board objects are placed.

                                                 Board
 TheBoard : ARRAY[0:9, 0:9] of BoardObject                   stores the board contents as a 2D array of
                                                             10 x 10 elements of type BoardObject
 Constructor()                                               initialises each of TheBoard elements to
                                                             an empty BoardObject with Code = "-"
                                                             and Value = 0

 GetObject()                                                 takes a row and column number as
                                                             parameters and returns the BoardObject
                                                             at the row, column position

 SetObject()                                                 takes a BoardObject, row number and
                                                             column number as parameters. Stores the
                                                             BoardObject in TheBoard at the given
                                                             row, column position

 DisplayBoard()                                              outputs the code of each BoardObject
                                                             stored in TheBoard, one row at a time



© UCLES 2025                                9618/43/O/N/25
```

### QP p.5

```text
5

          (i)   Write program code to declare the class Board and its constructor.

                Do not declare the other methods.

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 1(b)(i) in the evidence document.
                                                                                                      [4]

         (ii)   The method GetObject() takes a row number and column number as parameters.

                The method returns the BoardObject stored at the parameter position.

                Write program code for GetObject()

 Save your program.

 Copy and paste the program code into part 1(b)(ii) in the evidence document.
                                                                                                      [2]

        (iii)   The method SetObject() takes three parameters: a BoardObject, row number and
                column number.

                The method stores the BoardObject parameter in the row, column position in
                TheBoard

                Write program code for SetObject()

 Save your program.

 Copy and paste the program code into part 1(b)(iii) in the evidence document.
                                                                                                      [2]




© UCLES 2025                                   9618/43/O/N/25                                  [Turn over
```

### QP p.6

```text
6

        (iv)   The method DisplayBoard() outputs the Code of each BoardObject stored in
               TheBoard using GetCode()

               Each row in TheBoard is output on one line with a space between each Code

               For example, the following board contains these four board objects:

               •   one object has code "A" in row 0 column 7
               •   one object has code "B" in row 0 column 9
               •   one object has code "C" in row 1 column 1
               •   one object has code "E" in row 6 column 5

               The other board objects are empty. The output for this board will be:

                   - - - - - - - A - B
                   - C - - - - - - - -
                   - - - - - - - - - -
                   - - - - - - - - - -
                   - - - - - - - - - -
                   - - - - - - - - - -
                   - - - - - E - - - -
                   - - - - - - - - - -
                   - - - - - - - - - -
                   - - - - - - - - - -

               Write program code for DisplayBoard()

 Save your program.

 Copy and paste the program code into part 1(b)(iv) in the evidence document.
                                                                                           [3]




© UCLES 2025                                  9618/43/O/N/25
```

### QP p.7

```text
7

    (c) (i)     The table gives the row and column position on the board to store each of the five objects
                created in part 1(a)(iii).

                      Object                          column
                                  row position
                     identifier                       position
                    Object1                   0                  0
                    Object2                   9                  9
                    Object3                   4                  5
                    Object4                   2                  2
                    Object5                   8                  7

                Write program code to amend the main program to:

                •     declare a new instance of Board()
                •     store each BoardObject in the position given in the table
                •     call DisplayBoard() for the new board object.

 Save your program.

 Copy and paste the program code into part 1(c)(i) in the evidence document.
                                                                                                       [3]

         (ii)   Test your program.

                Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot(s) into part 1(c)(ii) in the evidence document.
                                                                                                       [1]




© UCLES 2025                                   9618/43/O/N/25                                 [Turn over
```

### QP p.8

```text
8

    (d) (i)     Amend the main program to:

                •   repeatedly take a row position as input until it is between 0 and 9 inclusive
                •   repeatedly take a column position as input until it is between 0 and 9 inclusive
                •   use the appropriate method(s) to identify if there is an object in the array position
                    input
                •   output "Miss" if there is an empty BoardObject in that position
                •   output the Code and Value if there is a non-empty BoardObject in that position.

                All outputs must include appropriate messages.

 Save your program.

 Copy and paste the program code into part 1(d)(i) in the evidence document.
                                                                                                      [4]

         (ii)   Test your program by entering this test data in the order given:

                    Row position first input:              10

                    Row position second input:             4

                    Column position first input:           –1

                    Column position second input:          5

                Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot(s) into part 1(d)(ii) in the evidence document.
                                                                                                      [1]




© UCLES 2025                                    9618/43/O/N/25
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a)(i) | 9618_w25_43:1(a)(i) | 5 | 代码 | `test_1ai_aii_boardobject` · MP5 | MP1、MP2、MP3、MP4 |
| Part 1(a)(ii) | 9618_w25_43:1(a)(ii) | 3 | 代码 | `test_1ai_aii_boardobject` · MP2、MP3 | MP1 |
| Part 1(a)(iii) | 9618_w25_43:1(a)(iii) | 3 | 代码 | `test_1aiii_ci_named_objects_and_placement` · MP1、MP2、MP3 | — |
| Part 1(b)(i) | 9618_w25_43:1(b)(i) | 4 | 代码 | `test_1bi_initial_board` · MP3、MP4 | MP1、MP2 |
| Part 1(b)(ii) | 9618_w25_43:1(b)(ii) | 2 | 代码 | `test_1bii_biii_get_set_coordinates` · MP2 | MP1 |
| Part 1(b)(iii) | 9618_w25_43:1(b)(iii) | 2 | 代码 | `test_1bii_biii_get_set_coordinates` · MP2 | MP1 |
| Part 1(b)(iv) | 9618_w25_43:1(b)(iv) | 3 | 代码 | `test_1biv_display_qp_example` · MP1、MP2、MP3 | — |
| Part 1(c)(i) | 9618_w25_43:1(c)(i) | 3 | 代码 | `test_1aiii_ci_named_objects_and_placement`、`test_1cii_board_screenshot` · MP1、MP2、MP3 | — |
| Part 1(c)(ii) | 9618_w25_43:1(c)(ii) | 1 | 截图 | `test_1cii_board_screenshot` · 全行 | — |
| Part 1(d)(i) | 9618_w25_43:1(d)(i) | 4 | 代码 | `test_1di_hit_miss_and_edges`、`test_1dii_invalid_inputs_screenshot` · MP1、MP2、MP3、MP4 | — |
| Part 1(d)(ii) | 9618_w25_43:1(d)(ii) | 1 | 截图 | `test_1dii_invalid_inputs_screenshot` · 全行 | — |

## 人工核对清单

- [ ] 1(a)(i) MP4: … taking two parameters …

- [ ] 1(a)(i) MP1: Class header (and end where appropriate)
- [ ] 1(a)(i) MP2: Declaring Code as string and Value as integer
- [ ] 1(a)(i) MP3: Constructor header (and end where appropriate) within class …
- [ ] 1(a)(ii) MP1: 1 get header (and end where appropriate) with no parameter …
- [ ] 1(b)(i) MP1: Class header (and end where appropriate)
- [ ] 1(b)(i) MP2: Constructor header (and end where appropriate) within class
- [ ] 1(b)(ii) MP1: Get method header taking 2 (integer) parameters …
- [ ] 1(b)(iii) MP1: Set method header taking three parameters (TheObject, row, column) …
- [ ] 类型与大小的英文注释、函数头及参数、类与方法的归属、QP 要求时的私有属性声明符合本题 MS。混合得分点中能测行为的计自动，头部和类型仍须人工复核。
- [ ] 主程序的调用、返回值使用与分支逐项符合 QP；截图清晰并包含题目要求的输入与输出；提示语语义合适。
- [ ] 指定算法的实现没有用内置函数代劳；文件打开 / 关闭位置及异常范围按 MS 检查。

## MS 得分点编号

测试与上表使用语料 `markpoints[].n`。1 分行按全行计；未印 MP 数字的圆点按原页顺序对应。可选点多于行分值时，自动 / 人工分值按点的权重比例折算；结构整体点仅作人工。

## QP p.4 网格图转写

下表加粗黑格与原图相同（row 1, column 3）；行列均从 0 开始。

| Row / Column | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 0 |  |  |  |  |  |  |  |  |  |  |
| 1 |  |  |  | **■** |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |  |  |  |  |
| 9 |  |  |  |  |  |  |  |  |  |  |
