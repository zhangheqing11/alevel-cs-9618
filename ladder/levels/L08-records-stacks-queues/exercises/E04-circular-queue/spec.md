# L08/E04 · 循环队列：队首、队尾指针与绕回

| 属性 | 值 |
|:--|:--|
| id | `L08/E04` |
| 目录 | `ladder/levels/L08-records-stacks-queues/exercises/E04-circular-queue/` |
| 形态 | `function`（全局数组与指针 + 两个函数；测试检查返回值与全局变量） |
| entry | `enqueue`（同一文件还有 `dequeue` 与全局变量 `queue`、`front_pointer`、`rear_pointer`、`number_of_items`、常量 `QUEUE_SIZE`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `queue-array`, `global-scope`, `div-mod`, `boundary-values`, `boolean-return` |
| difficulty | 4 |
| title | `Circular queue: front and rear pointers that wrap round` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L08 card §4；常见坑 6、9 |

## 练习目标

用数组、队首指针、队尾指针和计数实现循环队列：用计数判断满与空；指针越过末尾时绕回开头；出队后空出的位置能被再次使用。

## 题面

### 中文导读

队列最多存 5 个字符串。伪代码用 1 起数组，`FrontPointer` 初值 1、`RearPointer` 初值 0、`NumberOfItems` 初值 0。Python 用 0 起 list，`front_pointer = 0`、`rear_pointer = -1`、`number_of_items = 0`。`Enqueue(Item)`：队满返回 `FALSE`，否则把 `Item` 放在队尾并返回 `TRUE`。`Dequeue()`：队空返回 `""`，否则移走并返回队首元素。两个指针越过数组末尾时都要绕回开头。

### English task

A circular queue holds up to 5 strings.

In pseudocode, the queue is the global array `Queue : ARRAY[1:5] OF STRING` with the global integers `FrontPointer` (initialised to 1), `RearPointer` (initialised to 0) and `NumberOfItems` (initialised to 0). Write:

- a function `Enqueue()` that takes a string `Item`; it returns `FALSE` if the queue is full, otherwise it adds `Item` at the rear of the queue and returns `TRUE`
- a function `Dequeue()` that returns the empty string if the queue is empty, otherwise it removes and returns the item at the front of the queue.

Both pointers wrap round to the first element when they move past the last element.

In Python, use the module-level variables given in the starter: `QUEUE_SIZE = 5`, `queue = [""] * QUEUE_SIZE`, `front_pointer = 0`, `rear_pointer = -1`, `number_of_items = 0`. Write `enqueue(item)` and `dequeue()` with the same behaviour.

## 接口

```python
QUEUE_SIZE = 5
queue = [""] * QUEUE_SIZE   # ARRAY of 5 STRING -> indexes 0 to 4
front_pointer = 0
rear_pointer = -1
number_of_items = 0


def enqueue(item: str) -> bool:
    """Return False if the queue is full; otherwise add item at the rear and return True."""
    raise NotImplementedError


def dequeue() -> str:
    """Return "" if the queue is empty; otherwise remove and return the front item."""
    raise NotImplementedError
```

（`starter.py` 里五个模块级变量照上面给出。）

`answer.pseudo` 模板：

```pseudocode
DECLARE Queue : ARRAY[1:5] OF STRING
DECLARE FrontPointer : INTEGER
DECLARE RearPointer : INTEGER
DECLARE NumberOfItems : INTEGER
FrontPointer ← 1
RearPointer ← 0
NumberOfItems ← 0

FUNCTION Enqueue(Item : STRING) RETURNS BOOLEAN

ENDFUNCTION

FUNCTION Dequeue() RETURNS STRING

ENDFUNCTION
```

## 必测行为

`sol` fixture 每个测试都重新加载模块，所有全局变量回到初值。

| # | 操作（同一测试内按顺序） | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | 刚加载 | `front_pointer == 0`、`rear_pointer == -1`、`number_of_items == 0`、`queue == [""] * 5` | 初值 |
| B2 | `enqueue` `"A"`、`"B"`、`"C"`，再 `dequeue()` 两次 | 三次都返回 `True`；两次 `dequeue` 依次返回 `"A"`、`"B"`；`number_of_items == 1` | 先进先出 |
| B3 | `enqueue` `"A"` 到 `"E"`，再 `enqueue("F")` | 前 5 次 `True`，第 6 次 `False`；`queue == ["A", "B", "C", "D", "E"]` | 队满（边界） |
| B4 | `enqueue` `"A"` 到 `"E"`；`dequeue()` 两次；再 `enqueue("F")`、`enqueue("G")` | 两次 `dequeue` 返回 `"A"`、`"B"`；两次 `enqueue` 都返回 `True`；`rear_pointer == 1`；`queue == ["F", "G", "C", "D", "E"]` | 队尾绕回 |
| B5 | 接 B4，`dequeue()` 六次 | 依次返回 `"C"`、`"D"`、`"E"`、`"F"`、`"G"`、`""`；之后 `front_pointer == 2`、`number_of_items == 0` | 队首绕回；最后为空 |
| B6 | 空队列上 `dequeue()` | 返回 `""`；指针与计数不变 | 队空（边界） |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 队尾不绕回：`rear_pointer = rear_pointer + 1`，B4 的 `enqueue("F")` 访问 `queue[5]` 抛 `IndexError` | B4、B5 |
| M2 | 用 `rear_pointer == QUEUE_SIZE - 1` 判断「满」（线性队列的想法）：B4 中已出队两次，`enqueue("F")` 仍返回 `False` | B4、B5 |
| M3 | 队首不绕回：`front_pointer = front_pointer + 1`，B5 第四次 `dequeue` 访问 `queue[5]` 抛 `IndexError` | B5 |

## 人工核对清单

- [ ] 伪代码：满/空都用 `NumberOfItems` 判断；入队「先移 `RearPointer`、绕回、再存」，出队「先取值、再移 `FrontPointer`、绕回」。
- [ ] 伪代码：绕回写成 `IF RearPointer > 5 THEN RearPointer ← 1 ENDIF`，或 `RearPointer ← (RearPointer MOD 5) + 1`；能说出后一种写法为什么要先 MOD 再加 1。
- [ ] 伪代码：入队、出队都没有移动其他元素（ER s23 9618/22 Q3 p.19）；两个函数用 `RETURN`。
- [ ] Python：`global` 写全了要赋值的三个变量；绕回用 `% QUEUE_SIZE`。

## 出处

自编。误区依据：ER s23 9618/22 Q3 p.19（循环队列：以为加入新数据前要移动或删除已有内容）。语法依据：指南 p.10（数组）、p.15（MOD）、p.23（FUNCTION）。
