# L09/E03 · 读分数文件：文件不存在、坏数据行、P4 式全局数组

| 属性 | 值 |
|:--|:--|
| id | `L09/E03` |
| 目录 | `ladder/levels/L09-exceptions-validation/exercises/E03-read-scores/` |
| 形态 | `function`（模块级全局数组与计数；测试检查返回值、全局变量与输出行） |
| entry | `ReadScores`（同一文件还有全局变量 `ScoreArray`、`NumberScores`） |
| pseudocode | `false` |
| files | `["Scores.txt"]` |
| skills | `exception-handling`, `file-open-read`, `loop-to-eof`, `global-scope`, `p4-identifiers`, `type-conversion` |
| difficulty | 3 |
| title | `Read a scores file safely into a global array` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L09 card §2、§3、§5；L07 card §3 |

## 练习目标

P4 第一题的常见形态：把源文件读进**全局数组**并记下个数；文件打不开时给出提示而不是崩溃；跳过不能转换的行；数组按 D10 的要求真实建出并注释大小与类型。

## 题面

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

## 接口

```python
ScoreArray = [-1] * 20   # INTEGER, 20 elements, each initialised to -1
NumberScores = 0         # INTEGER


def ReadScores(FileName: str) -> int:
    """Read integers from FileName into ScoreArray; return NumberScores."""
    raise NotImplementedError
```

（`starter.py` 里两个全局变量照上面给出。）

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

## 必测行为

`sol` fixture 每个测试都重新加载模块，并把当前目录设为 `files/` 的副本。

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | 刚加载 | `sol.ScoreArray == [-1] * 20`、`sol.NumberScores == 0` | 全局数组真实建出 |
| B2 | `ReadScores("Scores.txt")` | 返回 `4`；`sol.NumberScores == 4` | |
| B3 | 接 B2 | `sol.ScoreArray[:4] == [120, 85, 300, 42]`；其余 16 个仍是 `-1` | 跳过坏行与空行，顺序不变 |
| B4 | 接 B2 的输出行（`output_lines`） | `["Skipped: abc", "Skipped: 7.5"]` | 空行不输出 |
| B5 | `ReadScores("Nope.txt")` | 返回 `0`；输出行 `["File not found"]`；`sol.ScoreArray` 全是 `-1` | 文件不存在（不能抛异常） |
| B6 | 连续调用两次 `ReadScores("Scores.txt")` | 两次都返回 `4`；`sol.ScoreArray[:5] == [120, 85, 300, 42, -1]` | 每次调用先把计数置 0 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 没有处理 `FileNotFoundError`：`ReadScores("Nope.txt")` 抛异常 | B5 |
| M2 | 转换没有异常处理：读到 `abc` 时抛 `ValueError` | B2、B3、B4、B6 |
| M3 | 没有在开头把 `NumberScores` 置 0：第二次调用返回 `8` | B6 |
| M4 | 空行也当坏数据输出：多出一行 `Skipped: ` | B4 |

（M4 输出的是 `"Skipped: "`；`output_lines` 去掉行尾空格后是 `"Skipped:"`，仍与期望不同。）

## 人工核对清单

- [ ] 全局数组按 D10：`ScoreArray = [-1] * 20` 并有注释写明 INTEGER、20 个元素；`NumberScores` 有初值与类型注释。
- [ ] `ReadScores` 里写了 `global NumberScores`；没有写多余的 `global ScoreArray`（只改元素不需要；写了也不算错）。
- [ ] 打开文件在 `try` 里，并用 `with`（或在 `try` 里关闭）；`except FileNotFoundError:` 与 `except ValueError:` 各管各的。
- [ ] 标识符与题目一致：`ReadScores`、`FileName`、`ScoreArray`、`NumberScores`。

## 出处

自编。题型参考 P4 第一题常见的「读源文件到全局数组」（如 9618_s24_42 Q1，ECR P4 2024 p.5–7）。误区依据：ER s23 9618/41 Q3 p.39（文件与异常；数组声明）；ER s22 9618/41 Q1 p.35（关闭文件的位置）。
