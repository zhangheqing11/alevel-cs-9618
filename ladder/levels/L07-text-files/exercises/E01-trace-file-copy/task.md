# L07/E01 · 干跑：读到文件尾、跳过空行、写新文件


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

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

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

## 人工核对清单

- [ ] 预测是先手算的；能说出 `READFILE` 读到空行时 `LineOfText` 的值是 `""`。
- [ ] 能说出 `OPENFILE "out.txt" FOR WRITE` 对原有内容做了什么（指南 p.25）。
- [ ] Python 用了 `with`（或在结尾 `close()` 两个文件）；读写都通过文件对象，而不是文件名。

## 出处

自编。结构参考指南 p.26 的文件复制例子。语法依据：指南 p.25–26（OPENFILE、READFILE、EOF、WRITEFILE、CLOSEFILE）；插页 9618_w25_in_21 p.2（NUM_TO_STR、TO_UPPER）。
