## AR　数组与记录：伪代码 ↔ Python 对照与模板 {#core-AR}

P4 题目常先给伪代码声明（`DECLARE Jobs : ARRAY[0:99, 0:1] OF INTEGER`、`TYPE NewRecord … ENDTYPE`），再让你“write program code to declare …”。左列按 2027–29 伪代码指南（§3 数组 p.10–11，§4 记录 p.12–14），右列是考场 Python。英文列带 ⟦⟧ 的是该题 MS 原文。

### 1. 声明一维数组：建出来，注释写类型与个数（D10 ①）

| 伪代码 | Python | 不对应之处 |
|:--|:--|:--|
| `DECLARE DataArray : ARRAY[0:99] OF INTEGER` | `DataArray = [0] * 100  # INTEGER, 100 elements` | Python 没有声明，建出 100 个元素就是“声明” |
| `DECLARE Names : ARRAY[1:30] OF STRING` | `Names = [""] * 30  # STRING, 30 elements` | 题目用 1 起下标时，Python 下标 0–29 对应 1–30；或建 31 个、空出 0 号——照题目和测试约定 |
| `DECLARE Flags : ARRAY[0:29] OF BOOLEAN` | `Flags = [False] * 30  # BOOLEAN, 30 elements` | |
| 全局 | 文件顶层赋值；子程序里给它重新赋值时写 `global 名字` | 只改元素 `DataArray[3] = 5` 不需要 `global` |
| 局部于主程序 | 写在 `if __name__ == "__main__":` 下面 | MS 范例常写在文件顶层的 `#main` 部分 |

声明的得分句：「(global) 1D (Integer) array DataArray」⟦9618_w22_41:1(a)⟧、「100 elements」⟦9618_w22_41:1(a)⟧。只写 `DataArray = []`、或只写注释 `# DataArray integer 100`，考官报告说拿不到这一分（⟦9618_s23_42:1(a)⟧、⟦9618_w24_42:3(a)⟧ 的考官报告）。

### 2. 二维数组（指南 §3.2，p.11）

| 伪代码 | Python | 坑 |
|:--|:--|:--|
| `DECLARE Grid : ARRAY[0:9, 0:9] OF INTEGER` | `Grid = [[0] * 10 for i in range(10)]` | 不能 `[[0] * 10] * 10` |
| `Grid[R, C] ← 5` | `Grid[R][C] = 5` | |
| “first dimension 7 elements, second dimension 3” | `HighScores = [[""] * 3 for y in range(7)]` | 外层是第一维（行） |
| 嵌套 `FOR R ← 0 TO 9` / `FOR C ← 0 TO 9` | `for R in range(10):` / `for C in range(10):` | |

```pseudocode
DECLARE Jobs : ARRAY[0:99, 0:1] OF INTEGER
DECLARE NumberOfJobs : INTEGER
FOR Row ← 0 TO 99
   FOR Col ← 0 TO 1
      Jobs[Row, Col] ← -1
   NEXT Col
NEXT Row
NumberOfJobs ← 0
```

```python
Jobs = [[0] * 2 for Row in range(100)]   # INTEGER, 100 x 2
NumberOfJobs = 0                          # INTEGER
for Row in range(100):
    for Col in range(2):
        Jobs[Row][Col] = -1
NumberOfJobs = 0
print(Jobs[0], Jobs[99], NumberOfJobs)
```

### 3. 记录（指南 §4.1，p.12）

```pseudocode
TYPE NewRecord
   DECLARE Key : INTEGER
   DECLARE Item1 : INTEGER
   DECLARE Item2 : INTEGER
ENDTYPE
DECLARE HashTable : ARRAY[0:199] OF NewRecord
HashTable[5].Key ← 205
```

```python
class NewRecord:                    # record -> class with only attributes
    def __init__(self):
        self.Key = -1               # INTEGER
        self.Item1 = -1             # INTEGER
        self.Item2 = -1             # INTEGER


HashTable = [NewRecord() for i in range(200)]   # 200 SEPARATE records
HashTable[5].Key = 205
print(HashTable[5].Key, HashTable[6].Key)
```

| 伪代码 | Python | 坑 |
|:--|:--|:--|
| `TYPE R … ENDTYPE` | `class R:` + `def __init__(self):` | 字段必须在 `__init__` 里用 `self.` 创建（考官报告：没有构造方法时字段不存在） |
| `DECLARE Key : INTEGER`（字段） | `self.Key = 0  # INTEGER` | 少了 `self.` 就只是局部变量（⟦9618_w24_42:2(a)⟧ 的 MS 范例就漏了） |
| `DECLARE Item : R` | `Item = R()` | |
| `Item.Key ← 5` | `Item.Key = 5` | |
| `DECLARE A : ARRAY[0:49] OF R` | `A = [R() for i in range(50)]` | `[R()] * 50` 是 50 个引用指向同一个记录 |
| `Pupil2 ← Pupil1`（复制整条记录） | `Pupil2 = copy.copy(Pupil1)` | Python 的 `=` 只是起别名 |
| 字段是数组 `DECLARE QueueArray : ARRAY[0:99] OF INTEGER` | `self.QueueArray = [0] * 100` | |

记录的得分句：「Record/class NewRecord declared」⟦9618_s25_42:2(a)⟧、「3 variables within structure (all integer)」⟦9618_s25_42:2(a)⟧。题目说 “An empty record has the integer –1 stored in each field” 时，`__init__` 里各字段初值就写 –1。

### 4. 遍历与输出（AR-04、AR-05）

| 要做的事 | Python | 伪代码 |
|:--|:--|:--|
| 走遍全部 | `for I in range(len(A)):` | `FOR I ← 0 TO 99` … `NEXT I` |
| 只走已存的 | `for I in range(NumberItems):` | `FOR I ← 0 TO NumberItems - 1` |
| 同一行空格分隔 | `print(A[I], end=" ")`，循环后 `print()` | 先拼字符串 `Line ← Line & NUM_TO_STR(A[I]) & " "`，循环后 `OUTPUT Line` |
| 每项一行带文字 | `print(Jobs[I][0], "priority", Jobs[I][1])` | `OUTPUT Jobs[I, 0], " priority ", Jobs[I, 1]` |
| 拼成字符串返回 | `Text = Text + str(A[I]) + " "` … `return Text` | `RETURN Text` |
| 计数 / 求和 | `Count = Count + 1`、`Total = Total + A[I]` | `Count ← Count + 1` |
| 最大值（不用 `max()`） | `Max = A[0]`，逐个 `if A[I] > Max: Max = A[I]` | 同 |

### 5. 随机数（AR-01、AR-02）

| 伪代码 | Python |
|:--|:--|
| `INT(RAND(100)) + 1`（1–100 的整数） | `random.randint(1, 100)` |
| `INT(RAND(101))`（0–100 的整数） | `random.randint(0, 100)` |

文件开头写 `import random`；`randint` 两端都包含。“unique”时每个新数先在已存部分里查重（AR-01 模板）。

### 6. 常见失分对照

| 失分 | 例 | 改成 |
|:--|:--|:--|
| 只写注释 / 空列表 | `Animals = []  # 10 strings` | `Animals = [""] * 10  # STRING, 10 elements` |
| 类型不对 | 字符串数组用 `[0] * 10` | `[""] * 10` |
| 二维建成一维，或行列反了 | `[[""] * 7 for y in range(3)]`（7 行 3 列写反） | `[[""] * 3 for y in range(7)]` |
| 二维共用一行 | `[[0] * 2] * 100` | `[[0] * 2 for i in range(100)]` |
| 记录字段不在结构里 | 三个单独的全局变量 | 一个类，三个 `self.` 属性 |
| 记录数组共用一个对象 | `[R()] * 50` | `[R() for i in range(50)]` |
| 输出没换行 / 没空格 | `print(A)` 整个列表 | 循环 + `end=" "` + `print()` |
| 空元素也输出了 | 走满 100 行 | 走到 `NumberOfJobs` 或跳过 –1 |
