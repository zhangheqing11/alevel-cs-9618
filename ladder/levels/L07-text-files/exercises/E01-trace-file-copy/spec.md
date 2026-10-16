# L07/E01 · 干跑：读到文件尾、跳过空行、写新文件

| 属性 | 值 |
|:--|:--|
| id | `L07/E01` |
| 目录 | `ladder/levels/L07-text-files/exercises/E01-trace-file-copy/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2）：手算两样东西——写出的文件内容与屏幕输出 |
| entry | `run_trace` |
| pseudocode | `false` |
| files | `["words.txt", "out.txt"]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `file-open-read`, `loop-to-eof`, `file-write`, `file-close` |
| difficulty | 3 |
| title | `Dry run: read to end of file, skip blank lines, write a new file` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L07 card §1、§2 |

## 练习目标

精确执行 `WHILE NOT EOF` + `READFILE` 循环：空行读出来是空串；`WRITE` 模式会清掉文件原有内容；每次 `WRITEFILE` 写一行。再译成 Python，处理好 `"\n"`。

## 题面

### 中文导读

文件 `words.txt` 和 `out.txt` 的内容见下面「数据文件」。先手算：程序结束后 `out.txt` 里有哪几行（填进 `PREDICTED_FILE`），屏幕上输出哪几行（填进 `PREDICTED_OUTPUT`）。再把程序译成 Python 的 `run_trace()`，在当前目录读写这两个文件。

### English task

The files `words.txt` and `out.txt` are shown below. Dry-run the pseudocode and store:

- in `PREDICTED_FILE`, the lines that `out.txt` contains when the program ends
- in `PREDICTED_OUTPUT`, the lines that the program outputs.

Then translate the pseudocode into the Python function `run_trace()`, which reads and writes the two files in the current directory.

```pseudocode
DECLARE LineOfText : STRING
DECLARE Count : INTEGER
DECLARE Blank : INTEGER
Count ← 0
Blank ← 0
OPENFILE "words.txt" FOR READ
OPENFILE "out.txt" FOR WRITE
WHILE NOT EOF("words.txt")
   READFILE "words.txt", LineOfText
   IF LineOfText = "" THEN
      Blank ← Blank + 1
   ELSE
      Count ← Count + 1
      WRITEFILE "out.txt", NUM_TO_STR(Count) & ": " & TO_UPPER(LineOfText)
   ENDIF
ENDWHILE
CLOSEFILE "words.txt"
CLOSEFILE "out.txt"
OUTPUT "Lines written: ", Count
OUTPUT "Blank lines: ", Blank
```

## 接口

```python
PREDICTED_FILE: list[str] = []    # lines of out.txt at the end, filled in by hand first
PREDICTED_OUTPUT: list[str] = []  # lines output by the program, filled in by hand first


def run_trace() -> None:
    """Translate the pseudocode: read words.txt, write out.txt, print the two totals."""
    raise NotImplementedError


if __name__ == "__main__":
    run_trace()
```

（不需要 `answer.pseudo`。）

## 数据文件

`files/words.txt`（6 行，每行以换行结束；第 2、5 行是空行）：

```text
apple

Banana
cherry

date
```

`files/out.txt`（程序运行前已存在，1 行，以换行结束）：

```text
old line
```

## 必测行为

已用参考实现核对。测试在 `sol` fixture 给出的临时目录里运行（`files/` 已复制进去），运行后读 `out.txt` 的 `read_text().splitlines()`。

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED_FILE` | `["1: APPLE", "2: BANANA", "3: CHERRY", "4: DATE"]` |
| B2 | `sol.PREDICTED_OUTPUT` | `["Lines written: 4", "Blank lines: 2"]` |
| B3 | `run_trace()` 后 `out.txt` 的行 | 与 B1 相同（`old line` 已被 WRITE 模式清掉） |
| B4 | `run_trace()` 的输出行（`output_lines`） | 与 B2 相同 |
| B5 | `run_trace()` 后 `words.txt` | 内容不变 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 读出的行没去 `"\n"`：空行 `"\n"` 不等于 `""`，被当成普通行写出；输出 `Lines written: 6`、`Blank lines: 0`；预测写对 | B3、B4 |
| M2 | 输出文件用 `"a"` 打开：`old line` 还在第一行；预测写对 | B3 |
| M3 | 写文件时没加换行：`out.txt` 只有一行 `1: APPLE2: BANANA3: CHERRY4: DATE`；预测写对 | B3 |

## 人工核对清单

- [ ] 预测是先手算的；能说出 `READFILE` 读到空行时 `LineOfText` 的值是 `""`。
- [ ] 能说出 `OPENFILE "out.txt" FOR WRITE` 对原有内容做了什么（指南 p.25）。
- [ ] Python 用了 `with`（或在结尾 `close()` 两个文件）；读写都通过文件对象，而不是文件名。

## 出处

自编。结构参考指南 p.26 的文件复制例子。语法依据：指南 p.25–26（OPENFILE、READFILE、EOF、WRITEFILE、CLOSEFILE）；插页 9618_w25_in_21 p.2（NUM_TO_STR、TO_UPPER）。
