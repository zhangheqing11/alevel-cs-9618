# L08/E02 · 干跑：记录赋值是复制，记录数组要逐个新建


### 中文导读

这段伪代码会输出 4 行。先手算填 `PREDICTED`，再译成 Python：定义 class `PupilRecord`（字段 `last_name`、`year_group`，初值 `""`、`0`），然后在 `run_trace()` 里执行主程序。注意两个地方 Python 的行为与伪代码不同，要特别处理。

### English task

Dry-run the pseudocode below and store each line it outputs, in order, in the list `PREDICTED`. Then:

- write a Python class `PupilRecord` whose constructor sets `last_name = ""` and `year_group = 0`
- write `run_trace()`, which runs the main program and prints exactly the same lines.

```pseudocode
TYPE PupilRecord
   DECLARE LastName : STRING
   DECLARE YearGroup : INTEGER
ENDTYPE

DECLARE Pupil1 : PupilRecord
DECLARE Pupil2 : PupilRecord
DECLARE Form : ARRAY[1:3] OF PupilRecord
DECLARE Index : INTEGER

Pupil1.LastName ← "Johnson"
Pupil1.YearGroup ← 6
Pupil2 ← Pupil1
Pupil1.YearGroup ← 7
OUTPUT Pupil1.YearGroup, " ", Pupil2.YearGroup
FOR Index ← 1 TO 3
   Form[Index].LastName ← "Student" & NUM_TO_STR(Index)
   Form[Index].YearGroup ← 10
NEXT Index
Form[2].YearGroup ← Form[2].YearGroup + 1
FOR Index ← 1 TO 3
   OUTPUT Form[Index].LastName, ": ", Form[Index].YearGroup
NEXT Index
```

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能说出指南 p.14 的 `Pupil2 ← Pupil1` 是什么意思（同类型的记录变量可以互相赋值）。
- [ ] Python 用 `copy.copy(pupil1)`，或新建一个 `PupilRecord()` 再逐个字段赋值。
- [ ] Python 用 `[PupilRecord() for _ in range(3)]`（或循环 `append`）建数组，并能解释 `[PupilRecord()] * 3` 为什么错。

## 出处

自编。结构参考指南 p.14 的记录使用例子（`Pupil2 ← Pupil1`、`Form[Index].YearGroup ← Form[Index].YearGroup + 1`）。语法依据：指南 p.13–14；插页 9618_w25_in_21 p.2（NUM_TO_STR）。
