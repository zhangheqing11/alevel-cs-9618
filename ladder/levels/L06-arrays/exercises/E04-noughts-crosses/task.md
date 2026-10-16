# L06/E04 · 井字棋：二维数组的行、列与对角线


### 中文导读

用指南里的二维数组 `NoughtsAndCrosses : ARRAY[1:3,1:3] OF CHAR`（指南 p.10）表示井字棋盘，每格是 `'X'`、`'O'` 或空格 `' '`。写函数 `Winner()`：有一条线（任一行、任一列或任一条对角线）三格都是 `'X'` 就返回 `"X"`，都是 `'O'` 就返回 `"O"`，否则返回空串 `""`。可以假设棋盘上最多只有一方获胜。

### English task

The global 2D array `NoughtsAndCrosses : ARRAY[1:3,1:3] OF CHAR` stores a noughts and crosses board. Each element is `'X'`, `'O'` or a space `' '`.

Write a function `Winner()` that returns `"X"` if any row, column or diagonal contains three `'X'` characters, `"O"` if any contains three `'O'` characters, and the empty string `""` otherwise. You may assume that at most one player has won.

Then write the Python function `winner(board)`. `board` is a list of 3 rows; each row is a list of 3 one-character strings.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：二维下标写成 `NoughtsAndCrosses[Row, Column]`（指南 p.10）；反对角线是 `[1,3]`、`[2,2]`、`[3,1]`。
- [ ] 伪代码：比较三格时写成完整的 `A = B AND B = C AND A <> ' '`，没有 `A = B = C`。
- [ ] 伪代码：行、列用 `FOR` 循环检查，而不是把 8 条线全部手写（两种都对，循环更不容易漏）；`RETURN` 的是 STRING。
- [ ] Python：二维下标写成 `board[r][c]`；没有修改棋盘。

## 出处

自编。棋盘数组取自指南 p.10 的示例声明 `DECLARE NoughtsAndCrosses : ARRAY[1:3,1:3] OF CHAR`。语法依据：指南 p.10（二维数组）、p.16（AND）、p.20（嵌套 FOR）。
