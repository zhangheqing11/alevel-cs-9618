# L01/E01 · 干跑：赋值、DIV/MOD 与 OUTPUT


### 中文导读

下面这段伪代码会输出 7 行。**先不要写 Python**：在纸上（或脑子里）一行一行执行，把每次 `OUTPUT` 显示的内容按顺序写进 `PREDICTED` 列表（每个元素是一行，写成字符串）。写完再把伪代码逐行翻译成 Python 函数 `run_trace()`，运行它，看看和你的预测是否一致。两部分都会被测试。

### English task

Dry-run the pseudocode below. Write the exact text of each line it outputs, in order, as strings in the list `PREDICTED`. Then translate the pseudocode line by line into the Python function `run_trace()`, which must print exactly the same lines.

```pseudocode
DECLARE Total : INTEGER
DECLARE Count : INTEGER
DECLARE Mean : REAL
DECLARE Code : STRING
CONSTANT Prefix = "ID-"
Total ← 17
Count ← 5
Mean ← Total / Count
OUTPUT Total DIV Count
OUTPUT Total MOD Count
OUTPUT Mean
Count ← Count + 2
Total ← Total - Count * 2
OUTPUT Total, " ", Count
Code ← Prefix & "42"
OUTPUT Code
OUTPUT INT(Mean * 10)
OUTPUT "Mean is ", Mean, "!"
```

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

## 人工核对清单

- [ ] `PREDICTED` 是在写 `run_trace()` **之前**手算的（导师当面问一句即可）。
- [ ] 能说出第 4 行为什么是 `3 7`：乘法先算；`Count` 在上一行已经变成 7。
- [ ] 能说出 `CONSTANT Prefix = "ID-"` 为什么用 `=` 而不是 `←`（指南 p.8）。
- [ ] Python 里常量写成全大写名字（如 `PREFIX = "ID-"`）。

## 出处

自编。语法依据：指南 p.8（DECLARE、CONSTANT）、p.9（←）、p.15（OUTPUT、DIV、MOD）、p.17（&、INT）。
