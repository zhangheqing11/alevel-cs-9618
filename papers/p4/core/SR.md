## SR　查找与排序：伪代码 ↔ Python 对照与模板 {#core-SR}

算法的关键是“这一轮前，哪一段已经处理好”。下表不是给分清单；给分看对应小问的 MS。

| 算法 | 已处理部分 / 不变量 | 每轮推进 |
|:--|:--|:--|
| 线性计数 | Count 是已访问部分中的命中数 | 下标加 1，命中时 Count 加 1 |
| 二分查找 | 目标若存在，只可能在 First..Last | 排除中点后的一半区间 |
| 冒泡排序 | 无交换的一轮说明相邻各对都已正确 | 扫描相邻对，必要时交换 |
| 插入排序 | 0..X−1 已有序 | 暂存 X，移动左边较大项，填空位 |

### 1. 线性计数

「Looping through each array element and keeping count of the number of times the parameter appears」⟦9618_s23_41:1(c)⟧。计数题 return 必须在循环后，不能命中一次就停。

```pseudocode
DECLARE DataArray : ARRAY[0:24] OF INTEGER
FUNCTION LinearSearch(Target : INTEGER) RETURNS INTEGER
   DECLARE Count : INTEGER
   DECLARE I : INTEGER
   Count ← 0
   FOR I ← 0 TO 24
      IF DataArray[I] = Target THEN
         Count ← Count + 1
      ENDIF
   NEXT I
   RETURN Count
ENDFUNCTION
```

```python
def LinearSearch(DataArray, Target):
    Count = 0
    for I in range(len(DataArray)):
        if DataArray[I] == Target:
            Count = Count + 1
    return Count
```

左侧数组是带界的全局声明（D24）；右侧按 P4 常见接口传 list，并从参数求长度。若题目给全局数组、无数组参数，就按题目改签名。

### 2. 二分查找：闭区间

| 伪代码 | Python | 原因 |
|:--|:--|:--|
| `First ← 0`、`Last ← NumberItems - 1` | 同 | 上界是最后一项下标，不是元素个数 |
| `WHILE First <= Last` | `while First <= Last:` | 一项的区间仍要检查 |
| `Middle ← (First + Last) DIV 2` | `Middle = (First + Last) // 2` | 下标必须整数 |
| `IF Target < A[Middle] THEN` | `if Target < A[Middle]:` | 比较数值，不比较下标 |
| `Last ← Middle - 1` | 同 | 中点已经比较过，排除它 |
| `First ← Middle + 1` | 同 | 不能保留 Middle 导致不前进 |
| `RETURN -1` | `return -1` | 空区间才说明未找到 |

```python
def BinarySearch(A, Target):
    First = 0
    Last = len(A) - 1
    while First <= Last:
        Middle = (First + Last) // 2
        if A[Middle] == Target:
            return Middle
        elif Target < A[Middle]:
            Last = Middle - 1
        else:
            First = Middle + 1
    return -1


def RecursiveBinarySearch(A, First, Last, Target):
    if First > Last:
        return -1
    Middle = (First + Last) // 2
    if A[Middle] == Target:
        return Middle
    elif Target < A[Middle]:
        return RecursiveBinarySearch(A, First, Middle - 1, Target)
    else:
        return RecursiveBinarySearch(A, Middle + 1, Last, Target)
```

调用递归版用 `RecursiveBinarySearch(A, 0, len(A)-1, Target)`；同一数组不切片，返回位置仍是原数组下标。对应「Checking if not found and returning –1」⟦9618_w25_42:2(e)⟧。递归分支前面要有 return，才能把深层的结果送回最外层。

### 3. 冒泡：相邻交换

```python
def BubbleSort(A):
    Swap = True
    while Swap:
        Swap = False
        for I in range(len(A) - 1):
            if A[I] > A[I + 1]:
                Temp = A[I]
                A[I] = A[I + 1]
                A[I + 1] = Temp
                Swap = True
    return A
```

「Sort must work for array of any length i.e. loops for length of parameter array」⟦9618_w25_42:2(c)⟧ 在本题是单独一分，不能把 `20` 写死。若题目给定固定次数的伪代码，就按伪代码结构翻译；不为了优化改掉要考的结构。

### 4. 插入：暂存、移位、放回

```pseudocode
DECLARE A : ARRAY[0:13] OF INTEGER
DECLARE X : INTEGER
DECLARE Y : INTEGER
DECLARE Current : INTEGER
DECLARE Moving : BOOLEAN
FOR X ← 1 TO 13
   Current ← A[X]
   Y ← X - 1
   Moving ← TRUE
   WHILE Y >= 0 AND Moving
      IF A[Y] > Current THEN
         A[Y + 1] ← A[Y]
         Y ← Y - 1
      ELSE
         Moving ← FALSE
      ENDIF
   ENDWHILE
   A[Y + 1] ← Current
NEXT X
```

```python
def InsertionSort(A):
    for X in range(1, len(A)):
        Current = A[X]
        Y = X - 1
        Moving = True
        while Y >= 0 and Moving:
            if A[Y] > Current:
                A[Y + 1] = A[Y]
                Y = Y - 1
            else:
                Moving = False
        A[Y + 1] = Current
    return A
```

这里 `AND` 两边都不访问数组；只有循环确认 Y 非负后才访问 A[Y]，符合 D25。`FOR X ← 1 TO 13` 含终点；Python `range(1, 14)` 不含终点。空位在 Y+1，不是 Y。

### 5. 记录、二维数组与接口

| 情况 | 比较 | 交换 / 移动 |
|:--|:--|:--|
| 整数数组升序 | `A[I] > A[I+1]` | 两个整数 |
| 按字符串长度 | `len(A[I]) > len(A[I+1])` | 整个字符串 |
| Jobs 按 priority | `Jobs[Y][1] > CurrentPriority` | job number 与 priority 两列都移 |
| 对象按字段 | 用题给 getter 取关键字 | 移动对象引用 |

⟦9618_w22_42:1(e)⟧ 用 priority（第二列）比较，但两列必须一起移动。数组中有空位时只处理 NumberOfJobs 个已存项；二分查找前的排序和查找必须使用同一关键字与方向。

P4 指定写算法时不用 `sort()`、`sorted()`、`index()`、`count()`、`in` 等代劳。模板里的 `for I in range(...)` 是循环语法，不是用成员运算替代查找。验证工具可用内置排序作独立核对，考场解答不靠它完成算法。
