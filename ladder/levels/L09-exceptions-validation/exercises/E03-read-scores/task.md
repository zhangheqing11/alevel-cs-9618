# L09/E03 · 读分数文件：文件不存在、坏数据行、P4 式全局数组


### 中文导读

全局数组 `ScoreArray` 有 20 个整数元素，初值都是 `-1`；全局变量 `NumberScores` 记录存了几个分数。写函数 `ReadScores(FileName)`：

- 先把 `NumberScores` 置 0；
- 打开文件逐行读：去掉首尾空白后是空行就跳过（不输出）；不能转换成整数的行输出 `Skipped: <该行>` 后跳过；能转换的依次存进 `ScoreArray`；
- 文件不存在时输出 `File not found`；
- 返回 `NumberScores`。

可以假设有效的行不超过 20 个。

### English task

The program uses two global variables:

- `ScoreArray`, a 1D array of 20 integers, each initialised to `-1`
- `NumberScores`, an integer that stores how many scores have been read.

Write a function `ReadScores()` that takes a file name as a parameter and:

- sets `NumberScores` to 0
- reads the file one line at a time; leading and trailing spaces and the newline are removed from each line
- ignores blank lines
- outputs `Skipped: ` followed by the line for each line that cannot be converted to an integer, and ignores that line
- stores each integer in the next element of `ScoreArray` and adds 1 to `NumberScores`
- outputs `File not found` if the file does not exist
- returns `NumberScores`.

Use exception handling for both the file and the conversion. You may assume there are at most 20 valid lines.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 数据文件

`files/Scores.txt`（7 行，以换行结束；第 4 行是空行）：

```text
120
85
abc

300
7.5
42
```

## 人工核对清单

- [ ] 全局数组按 D10：`ScoreArray = [-1] * 20` 并有注释写明 INTEGER、20 个元素；`NumberScores` 有初值与类型注释。
- [ ] `ReadScores` 里写了 `global NumberScores`；没有写多余的 `global ScoreArray`（只改元素不需要；写了也不算错）。
- [ ] 打开文件在 `try` 里，并用 `with`（或在 `try` 里关闭）；`except FileNotFoundError:` 与 `except ValueError:` 各管各的。
- [ ] 标识符与题目一致：`ReadScores`、`FileName`、`ScoreArray`、`NumberScores`。

## 出处

自编。题型参考 P4 第一题常见的「读源文件到全局数组」（如 9618_s24_42 Q1，ECR P4 2024 p.5–7）。误区依据：ER s23 9618/41 Q3 p.39（文件与异常；数组声明）；ER s22 9618/41 Q1 p.35（关闭文件的位置）。
