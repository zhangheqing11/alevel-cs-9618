# L08/E03 · 栈：数组 + 栈顶指针

| 属性 | 值 |
|:--|:--|
| id | `L08/E03` |
| 目录 | `ladder/levels/L08-records-stacks-queues/exercises/E03-array-stack/` |
| 形态 | `function`（全局数组与指针 + 两个函数；测试检查返回值与全局变量） |
| entry | `push`（同一文件还有 `pop` 与全局变量 `stack`、`top_pointer`、常量 `MAX_SIZE`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `stack-array`, `global-scope`, `boundary-values`, `boolean-return`, `return-value` |
| difficulty | 3 |
| title | `Stack: an array and a top pointer` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L08 card §3；L04 card §5；常见坑 6、7、8 |

## 练习目标

用数组和栈顶指针实现栈的入栈与出栈：先判断满/空；入栈「先加指针再存」，出栈「先取值再减指针」；Python 里给全局指针赋值要写 `global`。

## 题面

### 中文导读

栈最多存 8 个字符串。伪代码用 1 起数组 `Stack : ARRAY[1:8] OF STRING`，`TopPointer` 初值 0 表示空栈。Python 用 0 起 list，`top_pointer` 初值 **-1** 表示空栈（与 P4 常见写法一致）。`Push(Item)`：栈满返回 `FALSE`，否则存入并返回 `TRUE`。`Pop()`：栈空返回空串 `""`，否则返回栈顶元素并移走它。

### English task

A stack holds up to 8 strings.

In pseudocode, the stack is the global array `Stack : ARRAY[1:8] OF STRING` with the global integer `TopPointer`, initialised to 0 (empty stack). Write:

- a function `Push()` that takes a string `Item`; it returns `FALSE` if the stack is full, otherwise it adds `Item` to the top of the stack and returns `TRUE`
- a function `Pop()` that returns the empty string if the stack is empty, otherwise it removes and returns the item at the top of the stack.

In Python, use the module-level variables given in the starter: `MAX_SIZE = 8`, `stack = [""] * MAX_SIZE` and `top_pointer = -1` (empty stack, indexes 0 to 7). Write `push(item)` and `pop()` with the same behaviour.

## 接口

```python
MAX_SIZE = 8
stack = [""] * MAX_SIZE   # ARRAY of 8 STRING -> indexes 0 to 7
top_pointer = -1          # -1 means the stack is empty


def push(item: str) -> bool:
    """Return False if the stack is full; otherwise add item at the top and return True."""
    raise NotImplementedError


def pop() -> str:
    """Return "" if the stack is empty; otherwise remove and return the top item."""
    raise NotImplementedError
```

（`starter.py` 里三个模块级变量照上面给出。）

`answer.pseudo` 模板：

```pseudocode
DECLARE Stack : ARRAY[1:8] OF STRING
DECLARE TopPointer : INTEGER
TopPointer ← 0

FUNCTION Push(Item : STRING) RETURNS BOOLEAN

ENDFUNCTION

FUNCTION Pop() RETURNS STRING

ENDFUNCTION
```

## 必测行为

`sol` fixture 每个测试都重新加载模块：每个测试开始时 `top_pointer == -1`，`stack == [""] * 8`。

| # | 操作（同一测试内按顺序） | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | 刚加载 | `sol.top_pointer == -1`、`sol.stack == [""] * 8` | 初值 |
| B2 | `push("A")`、`push("B")`、`push("C")` | 都返回 `True`；`sol.top_pointer == 2`；`sol.stack[:3] == ["A", "B", "C"]` | |
| B3 | 接 B2，`pop()` 两次 | 依次返回 `"C"`、`"B"`；`sol.top_pointer == 0` | 后进先出 |
| B4 | 连续 `push` `"1"` 到 `"8"`，再 `push("9")` | 前 8 次返回 `True`，第 9 次返回 `False`；`sol.top_pointer == 7`；`sol.stack == ["1", …, "8"]` | 满栈（边界）；失败的入栈不改任何东西 |
| B5 | 空栈上 `pop()` | 返回 `""`；`sol.top_pointer == -1` | 空栈（边界） |
| B6 | `push("A")`、`push("B")`、`pop()`、`push("X")`，再 `pop()` 三次 | `sol.stack[:2] == ["A", "X"]`；三次 `pop` 依次返回 `"X"`、`"A"`、`""` | 位置被重新使用 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 两个函数都漏了 `global top_pointer`：第一次 `push` 就抛 `UnboundLocalError` | B2、B3、B4、B5、B6 |
| M2 | 满栈判断差一：`if top_pointer == MAX_SIZE:`，第 9 次 `push` 访问 `stack[8]` 抛 `IndexError` | B4 |
| M3 | 出栈先减指针再取值：`top_pointer -= 1; return stack[top_pointer]`，B3 第一次返回 `"B"` | B3、B6 |

（M1 在 B5 也失败：`pop` 读 `top_pointer` 前没有 `global`，但函数里有赋值，所以 Python 把它当局部变量，读取时抛 `UnboundLocalError`。）

## 人工核对清单

- [ ] 伪代码：`Push` 先 `IF TopPointer = 8 THEN RETURN FALSE`，再 `TopPointer ← TopPointer + 1`、`Stack[TopPointer] ← Item`、`RETURN TRUE`。
- [ ] 伪代码：`Pop` 先判断 `TopPointer = 0`；取值存进局部变量后再 `TopPointer ← TopPointer - 1`，最后 `RETURN`。
- [ ] 伪代码：全局变量没有在函数里重新 `DECLARE`；两个函数都用 `RETURN`，没有 `OUTPUT`。
- [ ] Python：只在需要给 `top_pointer` 赋值的函数里写 `global top_pointer`；`stack[...] = ...` 不需要 `global stack`（L04 card §5）。
- [ ] 能说出 1 起数组空栈用 0、0 起数组空栈用 -1 的原因，以及 P4 题目给了初值时为什么必须照用（ER s23 9618/41 Q3 p.39）。

## 出处

自编。误区依据：ER s23 9618/41 Q3 p.39（栈指针初值、Python 数组声明）。语法依据：指南 p.10（数组）、p.23（FUNCTION、RETURN）。
