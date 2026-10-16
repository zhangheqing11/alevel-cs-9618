# L05/E02 · 干跑：插页字符串函数


### 中文导读

这段伪代码会输出 8 行。先手算填 `PREDICTED`，再译成 Python 的 `run_trace()`。可以在 `solution.py` 里先写好上一题的 `left`/`right`/`mid` 再调用它们，也可以直接写切片。

### English task

Dry-run the pseudocode below and store each line it outputs, in order, in the list `PREDICTED`. Then translate it into the Python function `run_trace()`, which must print exactly the same lines.

```pseudocode
DECLARE Word : STRING
DECLARE Result : STRING
DECLARE Index : INTEGER
Word ← "Computer"
OUTPUT LENGTH(Word)
OUTPUT LEFT(Word, 3) & RIGHT(Word, 3)
OUTPUT MID(Word, 4, 2)
OUTPUT TO_UPPER(Word)
Result ← ""
FOR Index ← LENGTH(Word) TO 1 STEP -2
   Result ← Result & MID(Word, Index, 1)
NEXT Index
OUTPUT Result
OUTPUT ASC('C') - ASC('A')
OUTPUT CHR(ASC(MID(Word, 2, 1)) + 1)
OUTPUT NUM_TO_STR(LENGTH(Word) * 2) & "!"
```

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] `PREDICTED` 是先手算的。
- [ ] 能说出 `FOR Index ← LENGTH(Word) TO 1 STEP -2` 依次取哪些位置，并写出对应的 `range`。
- [ ] 能说出 `ASC('C') - ASC('A')` 为什么是 2（字母在编码表里连续）。

## 出处

自编。函数依据：插页 9618_w25_in_21 p.2–3（LEFT、RIGHT、MID、LENGTH、TO_UPPER、NUM_TO_STR、ASC、CHR）；指南 p.20（STEP 负步长）。
