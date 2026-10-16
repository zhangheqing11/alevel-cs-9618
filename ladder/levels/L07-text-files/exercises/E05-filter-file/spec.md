# L07/E05 · 过滤文件：拆字段、按条件写出、计数

| 属性 | 值 |
|:--|:--|
| id | `L07/E05` |
| 目录 | `ladder/levels/L07-text-files/exercises/E05-filter-file/` |
| 形态 | `function`（读一个文件、写另一个文件、返回计数） |
| entry | `filter_marks` |
| pseudocode | `true` |
| files | `["marks.txt"]` |
| skills | `file-open-read`, `loop-to-eof`, `file-write`, `file-close`, `string-functions`, `type-conversion` |
| difficulty | 4 |
| title | `Filter a file: split fields, write matching lines, count the rest` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L07 card §1、§2；L05 card §2、§3、§5 |

## 练习目标

一个读文件、一个写文件同时打开；每行按逗号拆成名字与分数（伪代码用 `MID` 循环找逗号，Python 可以用 `split`）；分数先转成数字再比较；跳过空行；返回没有写出的行数。这是 P2 文件题的完整形态（参考 9618_s24_22 Q8(c)）。

## 题面

### 中文导读

`marks.txt` 每行是 `名字,分数`，中间可能有空行。写函数 `FilterMarks(InFile, OutFile, PassMark)`：把分数 **≥ PassMark** 的行原样写进 `OutFile`（`OutFile` 新建，原有内容丢失），返回分数低于 `PassMark` 而没有写出的行数。空行既不写出，也不计数。分数一定是非负整数，名字里没有逗号。

### English task

Each line of a text file holds a name and an integer mark separated by a comma, for example `Ann,71`. The file may contain blank lines.

Write a function `FilterMarks()` that takes an input file name, an output file name and an integer `PassMark`. It:

- copies each line whose mark is greater than or equal to `PassMark` to the output file, unchanged and in the same order; the output file is a new file (any existing contents are lost)
- ignores blank lines (they are not copied and not counted)
- returns the number of lines that were not copied because the mark was below `PassMark`.

Marks are non-negative integers; names do not contain commas. Then write the Python function `filter_marks(in_name, out_name, pass_mark)`.

## 接口

```python
def filter_marks(in_name: str, out_name: str, pass_mark: int) -> int:
    """Copy lines with mark >= pass_mark to out_name; return how many were left out."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION FilterMarks(InFile : STRING, OutFile : STRING, PassMark : INTEGER) RETURNS INTEGER
   // find the comma with MID(), convert the mark with STR_TO_NUM()

ENDFUNCTION
```

## 数据文件

`files/marks.txt`（7 行，以换行结束；第 5 行是空行）：

```text
Ann,71
Bo,39
Cy,40
Dee,88

Eve,0
Fay,100
```

## 必测行为

每个测试调用后读输出文件 `passed.txt` 的 `read_text().splitlines()`。

| # | 调用 | 返回 | `passed.txt` 的行 | 说明 |
|:--|:--|:--|:--|:--|
| B1 | `filter_marks("marks.txt", "passed.txt", 40)` | `2` | `["Ann,71", "Cy,40", "Dee,88", "Fay,100"]` | 40 分刚好通过（边界）；空行不计 |
| B2 | `filter_marks("marks.txt", "passed.txt", 41)` | `3` | `["Ann,71", "Dee,88", "Fay,100"]` | 40 分刚好不通过 |
| B3 | `filter_marks("marks.txt", "passed.txt", 0)` | `0` | 全部 6 个非空行 | 全部通过 |
| B4 | `filter_marks("marks.txt", "passed.txt", 100)` | `5` | `["Fay,100"]` | 100 分：按数值比较，不按字符串 |
| B5 | 先写入 `passed.txt` 一行 `junk`，再调用 B1 | 同 B1 | 同 B1（`junk` 被清掉） | 输出文件是新文件 |
| B6 | 调用后 `marks.txt` | 内容不变 | | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 分数按字符串比较：`mark >= str(pass_mark)`；B1 时 `"100" < "40"`，`Fay` 没写出，返回 `3`；B4 时 `"71" >= "100"` 为真，返回 `1` | B1、B2、B4 |
| M2 | 用 `>` 代替 `>=`：B1 时 `Cy,40` 没写出，返回 `3` | B1、B3、B4 |
| M3 | 空行也算作「没写出」：B1 返回 `3` | B1、B2、B3、B4 |

（T10 已用参考实现核对：M1 在 B3 上碰巧正确——任何字符串都 `>= "0"`；M2 在 B2 上碰巧正确——没有人恰好 41 分。）

## 人工核对清单

- [ ] 伪代码：两个文件分别以 `READ`、`WRITE` 打开，各 `CLOSEFILE` 一次，`CLOSEFILE` 在 `RETURN` 之前。
- [ ] 伪代码：用 `FOR` + `MID(Line, Index, 1) = ','` 找到逗号位置，再用 `RIGHT(Line, LENGTH(Line) - CommaPos)` 取出分数，`STR_TO_NUM` 转成数字；没有 `split`（D2）。
- [ ] 伪代码：空行判断 `IF Line <> "" THEN` 写在拆字段之前。
- [ ] 伪代码：计数器先初始化；`RETURN` 的是计数，没有 `OUTPUT`。
- [ ] Python：可以用 `line.split(",")`、`int(…)`；两个文件都用 `with`。

## 出处

自编。题型参考 9618_s24_22 Q8(c) 的 `Stage_2()`（ECR P2 2024 p.27–29：逐行读、处理、按条件写出、统计并汇报被去掉的行数）。语法依据：指南 p.25–26；插页 9618_w25_in_21 p.2（MID、RIGHT、LENGTH、STR_TO_NUM）。
