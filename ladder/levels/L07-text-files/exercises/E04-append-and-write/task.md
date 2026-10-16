# L07/E04 · APPEND 与 WRITE：追加日志、重写报表


### 中文导读

过程 `AppendEntry(FileName, Entry)`：把一行 `Entry` 追加到文件末尾，原有内容保留（文件不存在时新建）。过程 `WriteReport(FileName)`：用全局并行数组 `Names`、`Marks`（共 `NumStudents` 人）重写报表文件——第一行是 `Name,Mark`，之后每人一行 `名字,分数`，原有内容全部清掉。Python 里 `write_report` 的两个数组作为参数传入。

### English task

1. Write a procedure `AppendEntry()` that takes a file name and a string `Entry`, and adds `Entry` as a new line at the end of the file. Existing lines must be kept. If the file does not exist, it is created.
2. Write a procedure `WriteReport()` that takes a file name and writes a new report file from the global parallel arrays `Names` and `Marks` (`NumStudents` elements in use). The first line is `Name,Mark`; then there is one line for each student in the form `Ann,71`. Any existing contents of the file are lost.

Then write the Python functions `append_entry(file_name, entry)` and `write_report(file_name, names, marks)`. Both return `None`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

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

## 人工核对清单

- [ ] 伪代码：`OPENFILE FileName FOR APPEND` 与 `OPENFILE FileName FOR WRITE` 用在正确的过程里（ECR P2 2024 p.29：该追加时用了 WRITE）；每个过程最后 `CLOSEFILE FileName`。
- [ ] 伪代码：`WRITEFILE FileName, Names[Index] & "," & NUM_TO_STR(Marks[Index])`——整数先经 `NUM_TO_STR` 再用 `&`。
- [ ] 伪代码：参数名 `FileName` 不加引号，也不加 `.txt`（ECR P2 2024 p.29）。
- [ ] Python：用 `with open(file_name, "a")` / `with open(file_name, "w")`；能说出 `"w"` 在打开的那一刻就清空了文件。

## 出处

自编。误区依据：ECR P2 2024（9618_s24_22 Q8(c)）p.29（输出文件应以 APPEND 打开却用了 WRITE；文件名标识符的写法）。语法依据：指南 p.25（文件模式、WRITEFILE、CLOSEFILE）；插页 9618_w25_in_21 p.2（NUM_TO_STR）。
