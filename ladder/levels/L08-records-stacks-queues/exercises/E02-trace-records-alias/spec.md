# L08/E02 · 干跑：记录赋值是复制，记录数组要逐个新建

| 属性 | 值 |
|:--|:--|
| id | `L08/E02` |
| 目录 | `ladder/levels/L08-records-stacks-queues/exercises/E02-trace-records-alias/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2） |
| entry | `run_trace`（同一文件还有记录类 `PupilRecord`） |
| pseudocode | `false` |
| files | `[]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `record-type`, `array-of-records`, `array-copy` |
| difficulty | 3 |
| title | `Dry run: record assignment copies, arrays of records` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L08 card §1；常见坑 4、5 |

## 练习目标

读懂记录赋值 `Pupil2 ← Pupil1`（复制，之后互不影响）与记录数组的逐个字段赋值；译成 Python 时做出真正的复制、为数组的每个元素新建对象。

## 题面

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

## 接口

```python
PREDICTED: list[str] = []  # fill in by hand BEFORE writing run_trace()


class PupilRecord:
    """Record type PupilRecord."""

    def __init__(self) -> None:
        raise NotImplementedError   # last_name = "", year_group = 0


def run_trace() -> None:
    """Run the main program; print exactly what OUTPUT displays."""
    raise NotImplementedError


if __name__ == "__main__":
    run_trace()
```

（不需要 `answer.pseudo`。）

## 必测行为

期望输出（共 4 行，已用参考实现核对）：

```text
7 6
Student1: 10
Student2: 11
Student3: 10
```

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED` | 恰好等于上面 4 个字符串组成的列表 |
| B2 | `run_trace()` 输出的第 1 行 | `"7 6"`（`Pupil2` 是复制，不跟着变） |
| B3 | 以 `Student` 开头的 3 行 | 名字各不相同，只有 `Student2` 是 11 |
| B4 | `run_trace()` 全部输出行 | 与上面 4 行逐行完全相等 |
| B5 | `PupilRecord()` | `last_name == ""`、`year_group == 0` |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `pupil2 = pupil1`（起别名）：第 1 行变成 `7 7`；`PREDICTED` 写对 | B2、B4 |
| M2 | `form = [PupilRecord()] * 3`：三个元素是同一个对象，后 3 行都变成 `Student3: 11`；`PREDICTED` 写对 | B3、B4 |
| M3 | `PREDICTED` 按「改 `Pupil1` 也改了 `Pupil2`」手算成 `"7 7"`，`run_trace()` 正确 | B1 |

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能说出指南 p.14 的 `Pupil2 ← Pupil1` 是什么意思（同类型的记录变量可以互相赋值）。
- [ ] Python 用 `copy.copy(pupil1)`，或新建一个 `PupilRecord()` 再逐个字段赋值。
- [ ] Python 用 `[PupilRecord() for _ in range(3)]`（或循环 `append`）建数组，并能解释 `[PupilRecord()] * 3` 为什么错。

## 出处

自编。结构参考指南 p.14 的记录使用例子（`Pupil2 ← Pupil1`、`Form[Index].YearGroup ← Form[Index].YearGroup + 1`）。语法依据：指南 p.13–14；插页 9618_w25_in_21 p.2（NUM_TO_STR）。
