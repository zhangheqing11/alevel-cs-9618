# L06/E04 · 井字棋：二维数组的行、列与对角线

| 属性 | 值 |
|:--|:--|
| id | `L06/E04` |
| 目录 | `ladder/levels/L06-arrays/exercises/E04-noughts-crosses/` |
| 形态 | `function` |
| entry | `winner` |
| pseudocode | `true` |
| files | `[]` |
| skills | `array-2d`, `array-index`, `nested-loops`, `logic-ops`, `return-value` |
| difficulty | 3 |
| title | `Noughts and crosses: rows, columns and diagonals of a 2D array` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L06 card §1、§3 |

## 练习目标

用二维数组的行列下标检查三行、三列、两条对角线；写对反对角线的下标关系（行 + 列 = 4，或 Python 里 `r + c == 2`）；不要把三格空白当成有人获胜。

## 题面

### 中文导读

用指南里的二维数组 `NoughtsAndCrosses : ARRAY[1:3,1:3] OF CHAR`（指南 p.10）表示井字棋盘，每格是 `'X'`、`'O'` 或空格 `' '`。写函数 `Winner()`：有一条线（任一行、任一列或任一条对角线）三格都是 `'X'` 就返回 `"X"`，都是 `'O'` 就返回 `"O"`，否则返回空串 `""`。可以假设棋盘上最多只有一方获胜。

### English task

The global 2D array `NoughtsAndCrosses : ARRAY[1:3,1:3] OF CHAR` stores a noughts and crosses board. Each element is `'X'`, `'O'` or a space `' '`.

Write a function `Winner()` that returns `"X"` if any row, column or diagonal contains three `'X'` characters, `"O"` if any contains three `'O'` characters, and the empty string `""` otherwise. You may assume that at most one player has won.

Then write the Python function `winner(board)`. `board` is a list of 3 rows; each row is a list of 3 one-character strings.

## 接口

```python
def winner(board: list[list[str]]) -> str:
    """Return "X" or "O" for a completed line, otherwise ""."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// global: NoughtsAndCrosses : ARRAY[1:3,1:3] OF CHAR
FUNCTION Winner() RETURNS STRING
   // check 3 rows, 3 columns and 2 diagonals

ENDFUNCTION
```

## 必测行为

下表把每个棋盘写成三行字符串，测试里转成 `[list(r) for r in rows]`。

| # | 棋盘（行 1 / 行 2 / 行 3） | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `"XXX"` / `"OO "` / `"   "` | `"X"` | 一行 |
| B2 | `"OX "` / `"OX "` / `"O X"` | `"O"` | 一列 |
| B3 | `"X O"` / `" XO"` / `"  X"` | `"X"` | 主对角线 |
| B4 | `"  O"` / `" O "` / `"O X"` | `"O"` | 反对角线 |
| B5 | `"XOX"` / `"XOO"` / `"OXX"` | `""` | 下满、无人获胜 |
| B6 | `"   "` / `"   "` / `"   "` | `""` | 空棋盘：三格空格不算获胜 |
| B7 | `"XO "` / `"   "` / `"OX "` | `""` | 有一整行是空格、无人获胜 |
| B8 | 调用后 `board` | 内容不变 | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 只检查行，不查列和对角线 | B2、B3、B4 |
| M2 | 反对角线下标写错：两条对角线都用 `board[i][i]` | B4 |
| M3 | 没有排除空格：三格相同就返回该字符，空棋盘返回 `" "` | B6、B7 |

## 人工核对清单

- [ ] 伪代码：二维下标写成 `NoughtsAndCrosses[Row, Column]`（指南 p.10）；反对角线是 `[1,3]`、`[2,2]`、`[3,1]`。
- [ ] 伪代码：比较三格时写成完整的 `A = B AND B = C AND A <> ' '`，没有 `A = B = C`。
- [ ] 伪代码：行、列用 `FOR` 循环检查，而不是把 8 条线全部手写（两种都对，循环更不容易漏）；`RETURN` 的是 STRING。
- [ ] Python：二维下标写成 `board[r][c]`；没有修改棋盘。

## 出处

自编。棋盘数组取自指南 p.10 的示例声明 `DECLARE NoughtsAndCrosses : ARRAY[1:3,1:3] OF CHAR`。语法依据：指南 p.10（二维数组）、p.16（AND）、p.20（嵌套 FOR）。
