# L08/E05 · 括号配对：用栈解决问题


### 中文导读

写函数 `Balanced(Text)`：检查字符串里的三种括号 `()`、`[]`、`{}` 是否配对正确，其他字符一律忽略。配对正确的意思是：每个右括号都和它前面最近的、还没配对的左括号同类型，并且结束时没有剩下没配对的左括号。

### English task

Write a function `Balanced()` that takes a string `Text` and returns `TRUE` if the brackets in it are balanced, otherwise `FALSE`. Only the characters `(`, `)`, `[`, `]`, `{` and `}` are checked; all other characters are ignored.

The brackets are balanced when each closing bracket matches the most recent unmatched opening bracket of the same type, and no opening bracket is left unmatched at the end.

In pseudocode, use a local array of characters and a top pointer as a stack (assume `Text` contains at most 100 brackets). Then write the Python function `balanced(text)`; a Python list may be used as the stack.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：逐字符循环 `FOR Index ← 1 TO LENGTH(Text)` + `MID(Text, Index, 1)`；左括号「`TopPointer ← TopPointer + 1`、`Stack[TopPointer] ← Ch`」。
- [ ] 伪代码：右括号先判断 `TopPointer = 0`（不平衡，`RETURN FALSE`），再取 `Stack[TopPointer]` 比较类型，再 `TopPointer ← TopPointer - 1`。
- [ ] 伪代码：循环结束后 `RETURN TopPointer = 0`（或等价的 IF）。
- [ ] 伪代码：判断括号类型可以用 CASE（每个括号一个子句）或 IF；字符字面量用单引号。
- [ ] Python：能说出 `stack.append(ch)`、`stack.pop()` 分别对应伪代码的哪几行。

## 出处

自编（经典的栈应用）。语法依据：指南 p.10（数组）、p.19（CASE）、p.20（FOR）、p.23（FUNCTION）；插页 9618_w25_in_21 p.2（MID、LENGTH）。
