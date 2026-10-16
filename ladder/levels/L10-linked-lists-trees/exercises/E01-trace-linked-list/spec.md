# L10/E01 · 干跑：沿指针遍历链表、表头插入

| 属性 | 值 |
|:--|:--|
| id | `L10/E01` |
| 目录 | `ladder/levels/L10-linked-lists-trees/exercises/E01-trace-linked-list/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2） |
| entry | `RunTrace` |
| pseudocode | `false` |
| files | `[]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `linked-list`, `array-index`, `p4-identifiers` |
| difficulty | 3 |
| title | `Dry run: traverse a linked list and insert at the start` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L10 card §1、§3、§4 |

## 练习目标

看清链表的顺序由指针决定、与数组顺序无关；准确执行「从空闲表取结点 → 存数据 → 改两个指针」的表头插入；再译成 Python。

## 题面

### 中文导读

链表存在两个并行数组里，初始状态见伪代码开头。先手算这段伪代码输出的 3 行，填进 `PREDICTED`；再把它译成 Python 的 `RunTrace()`（用 Python list 表示两个数组，下标同样从 0 起）。

### English task

Dry-run the pseudocode below and store each line it outputs, in order, in the list `PREDICTED`. Then translate it into the Python procedure `RunTrace()`, which must output exactly the same lines. Use Python lists for the two arrays; indexes start at 0, as in the pseudocode.

```pseudocode
DECLARE ListData : ARRAY[0:5] OF STRING
DECLARE ListPointer : ARRAY[0:5] OF INTEGER
DECLARE StartPointer : INTEGER
DECLARE FreePointer : INTEGER
DECLARE Current : INTEGER
DECLARE NewNode : INTEGER
DECLARE Line : STRING

// initial state
ListData[0] ← "Cat"
ListData[1] ← "Ant"
ListData[2] ← "Dog"
ListData[3] ← ""
ListData[4] ← "Bee"
ListData[5] ← ""
ListPointer[0] ← 2
ListPointer[1] ← 4
ListPointer[2] ← -1
ListPointer[3] ← 5
ListPointer[4] ← 0
ListPointer[5] ← -1
StartPointer ← 1
FreePointer ← 3

Line ← ""
Current ← StartPointer
WHILE Current <> -1
   Line ← Line & ListData[Current] & " "
   Current ← ListPointer[Current]
ENDWHILE
OUTPUT Line

NewNode ← FreePointer
FreePointer ← ListPointer[NewNode]
ListData[NewNode] ← "Elk"
ListPointer[NewNode] ← StartPointer
StartPointer ← NewNode

Line ← ""
Current ← StartPointer
WHILE Current <> -1
   Line ← Line & ListData[Current] & " "
   Current ← ListPointer[Current]
ENDWHILE
OUTPUT Line
OUTPUT "Free: ", FreePointer
```

## 接口

```python
PREDICTED: list[str] = []  # fill in by hand BEFORE writing RunTrace()


def RunTrace() -> None:
    """Translate the pseudocode; output exactly what OUTPUT displays."""
    raise NotImplementedError


if __name__ == "__main__":
    RunTrace()
```

（不需要 `answer.pseudo`。）

## 必测行为

期望输出（共 3 行，已用参考实现核对；行尾空格按 design.md §7.3 去掉）：

```text
Ant Bee Cat Dog
Elk Ant Bee Cat Dog
Free: 5
```

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED`（每项先 `rstrip()` 再比） | 等于上面 3 行 |
| B2 | `RunTrace()` 输出的第 1 行 | `"Ant Bee Cat Dog"`（沿指针，不是数组顺序） |
| B3 | 第 2 行 | `"Elk Ant Bee Cat Dog"`（新结点在表头） |
| B4 | 第 3 行 | `"Free: 5"`（空闲表的下一个结点） |
| B5 | `RunTrace()` 全部输出行（`output_lines`） | 与上面 3 行完全相等 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 按数组顺序输出（`for i in range(6)` 拼接非空数据）：第 1 行 `Cat Ant Dog Bee`；`PREDICTED` 也照此写 | B1、B2、B5 |
| M2 | 插入时没有更新 `FreePointer`：第 3 行 `Free: 3`；`PREDICTED` 写对 | B4、B5 |
| M3 | 遍历条件写成 `while ListPointer[Current] != -1`：漏掉最后的 `Dog`；`PREDICTED` 写对 | B2、B3、B5 |

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能画出插入前后两条链（数据链与空闲链）。
- [ ] 能说出插入时四行赋值的顺序为什么不能随意调换（特别是 `FreePointer ← ListPointer[NewNode]` 必须在 `ListPointer[NewNode] ← StartPointer` 之前）。
- [ ] Python 的拼接可以用 `+`、f-string 或 `" ".join`；行尾多一个空格不影响测试。

## 出处

自编。依据：L10 card §1、§3、§4；指南 p.10（数组）、p.21（WHILE）。
