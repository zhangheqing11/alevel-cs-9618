# L07/E04 · APPEND 与 WRITE：追加日志、重写报表

| 属性 | 值 |
|:--|:--|
| id | `L07/E04` |
| 目录 | `ladder/levels/L07-text-files/exercises/E04-append-and-write/` |
| 形态 | `function`（两个函数，写文件，返回 `None`） |
| entry | `append_entry`（同一文件还有 `write_report`） |
| pseudocode | `true` |
| files | `["log.txt", "report.txt"]` |
| skills | `file-write`, `file-append`, `file-close`, `type-conversion`, `string-concat` |
| difficulty | 2 |
| title | `APPEND and WRITE: add to a log, rewrite a report` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L07 card §1；常见坑 5、10、11 |

## 练习目标

分清两种写模式：`APPEND` 保留原有内容、写在后面；`WRITE` 新建文件、清掉原有内容。每次 `WRITEFILE` 写一行；Python 要自己加 `"\n"`；数字先转成字符串再连接。

## 题面

### 中文导读

过程 `AppendEntry(FileName, Entry)`：把一行 `Entry` 追加到文件末尾，原有内容保留（文件不存在时新建）。过程 `WriteReport(FileName)`：用全局并行数组 `Names`、`Marks`（共 `NumStudents` 人）重写报表文件——第一行是 `Name,Mark`，之后每人一行 `名字,分数`，原有内容全部清掉。Python 里 `write_report` 的两个数组作为参数传入。

### English task

1. Write a procedure `AppendEntry()` that takes a file name and a string `Entry`, and adds `Entry` as a new line at the end of the file. Existing lines must be kept. If the file does not exist, it is created.
2. Write a procedure `WriteReport()` that takes a file name and writes a new report file from the global parallel arrays `Names` and `Marks` (`NumStudents` elements in use). The first line is `Name,Mark`; then there is one line for each student in the form `Ann,71`. Any existing contents of the file are lost.

Then write the Python functions `append_entry(file_name, entry)` and `write_report(file_name, names, marks)`. Both return `None`.

## 接口

```python
def append_entry(file_name: str, entry: str) -> None:
    """Add entry as a new last line of the file; keep the existing lines."""
    raise NotImplementedError


def write_report(file_name: str, names: list[str], marks: list[int]) -> None:
    """Replace the file with 'Name,Mark' then one 'name,mark' line per student."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
PROCEDURE AppendEntry(FileName : STRING, Entry : STRING)

ENDPROCEDURE

// global: Names : ARRAY[1:50] OF STRING; Marks : ARRAY[1:50] OF INTEGER; NumStudents : INTEGER
PROCEDURE WriteReport(FileName : STRING)

ENDPROCEDURE
```

## 数据文件

全部以换行结束。

`files/log.txt`（2 行）：

```text
2026-10-01 start
2026-10-02 run
```

`files/report.txt`（1 行）：

```text
old report
```

## 必测行为

每个测试运行后用 `pathlib.Path(name).read_text().splitlines()` 读文件。

| # | 操作 | 文件的行 | 说明 |
|:--|:--|:--|:--|
| B1 | `append_entry("log.txt", "2026-10-03 stop")` | `["2026-10-01 start", "2026-10-02 run", "2026-10-03 stop"]` | 原有两行保留 |
| B2 | 连续 `append_entry("log.txt", "A")`、`append_entry("log.txt", "B")` | 原两行 + `"A"`、`"B"` | 每次是新的一行（不会粘在一起） |
| B3 | `append_entry("new.txt", "first")`（文件原来不存在） | `["first"]` | APPEND 也会新建文件 |
| B4 | `write_report("report.txt", ["Ann", "Bo"], [71, 64])` | `["Name,Mark", "Ann,71", "Bo,64"]` | `old report` 已被清掉 |
| B5 | `write_report("report.txt", [], [])` | `["Name,Mark"]` | 没有学生时只有标题行 |
| B6 | 先 `write_report("report.txt", ["Ann"], [71])`，再 `write_report("report.txt", ["Bo"], [64])` | `["Name,Mark", "Bo,64"]` | 第二次重写不保留第一次的内容 |
| B7 | 两个函数的返回值 | `None` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `append_entry` 用 `"w"` 打开：原有两行丢失 | B1、B2 |
| M2 | `append_entry` 写入时没加换行：B2 的最后一行变成 `"AB"` | B2 |
| M3 | `write_report` 用 `"a"` 打开：`old report` 还在第一行 | B4、B5、B6 |
| M4 | `write_report` 直接拼接整数：`name + "," + mark` 抛 `TypeError` | B4、B6 |

## 人工核对清单

- [ ] 伪代码：`OPENFILE FileName FOR APPEND` 与 `OPENFILE FileName FOR WRITE` 用在正确的过程里（ECR P2 2024 p.29：该追加时用了 WRITE）；每个过程最后 `CLOSEFILE FileName`。
- [ ] 伪代码：`WRITEFILE FileName, Names[Index] & "," & NUM_TO_STR(Marks[Index])`——整数先经 `NUM_TO_STR` 再用 `&`。
- [ ] 伪代码：参数名 `FileName` 不加引号，也不加 `.txt`（ECR P2 2024 p.29）。
- [ ] Python：用 `with open(file_name, "a")` / `with open(file_name, "w")`；能说出 `"w"` 在打开的那一刻就清空了文件。

## 出处

自编。误区依据：ECR P2 2024（9618_s24_22 Q8(c)）p.29（输出文件应以 APPEND 打开却用了 WRITE；文件名标识符的写法）。语法依据：指南 p.25（文件模式、WRITEFILE、CLOSEFILE）；插页 9618_w25_in_21 p.2（NUM_TO_STR）。
