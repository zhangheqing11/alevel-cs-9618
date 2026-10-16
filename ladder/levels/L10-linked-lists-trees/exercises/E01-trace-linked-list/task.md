# L10/E01 · 干跑：沿指针遍历链表、表头插入


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

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能画出插入前后两条链（数据链与空闲链）。
- [ ] 能说出插入时四行赋值的顺序为什么不能随意调换（特别是 `FreePointer ← ListPointer[NewNode]` 必须在 `ListPointer[NewNode] ← StartPointer` 之前）。
- [ ] Python 的拼接可以用 `+`、f-string 或 `" ".join`；行尾多一个空格不影响测试。

## 出处

自编。依据：L10 card §1、§3、§4；指南 p.10（数组）、p.21（WHILE）。
