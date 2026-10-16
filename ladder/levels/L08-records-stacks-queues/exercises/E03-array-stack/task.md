# L08/E03 · 栈：数组 + 栈顶指针


### 中文导读

栈最多存 8 个字符串。伪代码用 1 起数组 `Stack : ARRAY[1:8] OF STRING`，`TopPointer` 初值 0 表示空栈。Python 用 0 起 list，`top_pointer` 初值 **-1** 表示空栈（与 P4 常见写法一致）。`Push(Item)`：栈满返回 `FALSE`，否则存入并返回 `TRUE`。`Pop()`：栈空返回空串 `""`，否则返回栈顶元素并移走它。

### English task

A stack holds up to 8 strings.

In pseudocode, the stack is the global array `Stack : ARRAY[1:8] OF STRING` with the global integer `TopPointer`, initialised to 0 (empty stack). Write:

- a function `Push()` that takes a string `Item`; it returns `FALSE` if the stack is full, otherwise it adds `Item` to the top of the stack and returns `TRUE`
- a function `Pop()` that returns the empty string if the stack is empty, otherwise it removes and returns the item at the top of the stack.

In Python, use the module-level variables given in the starter: `MAX_SIZE = 8`, `stack = [""] * MAX_SIZE` and `top_pointer = -1` (empty stack, indexes 0 to 7). Write `push(item)` and `pop()` with the same behaviour.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`Push` 先 `IF TopPointer = 8 THEN RETURN FALSE`，再 `TopPointer ← TopPointer + 1`、`Stack[TopPointer] ← Item`、`RETURN TRUE`。
- [ ] 伪代码：`Pop` 先判断 `TopPointer = 0`；取值存进局部变量后再 `TopPointer ← TopPointer - 1`，最后 `RETURN`。
- [ ] 伪代码：全局变量没有在函数里重新 `DECLARE`；两个函数都用 `RETURN`，没有 `OUTPUT`。
- [ ] Python：只在需要给 `top_pointer` 赋值的函数里写 `global top_pointer`；`stack[...] = ...` 不需要 `global stack`（L04 card §5）。
- [ ] 能说出 1 起数组空栈用 0、0 起数组空栈用 -1 的原因，以及 P4 题目给了初值时为什么必须照用（ER s23 9618/41 Q3 p.39）。

## 出处

自编。误区依据：ER s23 9618/41 Q3 p.39（栈指针初值、Python 数组声明）。语法依据：指南 p.10（数组）、p.23（FUNCTION、RETURN）。
