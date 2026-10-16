# L08/E05 · 括号配对：用栈解决问题

| 属性 | 值 |
|:--|:--|
| id | `L08/E05` |
| 目录 | `ladder/levels/L08-records-stacks-queues/exercises/E05-bracket-check/` |
| 形态 | `function` |
| entry | `balanced` |
| pseudocode | `true` |
| files | `[]` |
| skills | `stack-array`, `char-loop`, `string-functions`, `boolean-return`, `boundary-values` |
| difficulty | 4 |
| title | `Check that brackets are balanced using a stack` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L08 card §3、§5；L05 card §3 |

## 练习目标

把栈当工具用：遇到左括号入栈，遇到右括号出栈并检查是否配对；处理「栈空时还要出栈」与「结束时栈不空」两种不平衡。伪代码用局部数组 + 指针实现栈；Python 可以用 list 的 `append`/`pop`。

## 题面

### 中文导读

写函数 `Balanced(Text)`：检查字符串里的三种括号 `()`、`[]`、`{}` 是否配对正确，其他字符一律忽略。配对正确的意思是：每个右括号都和它前面最近的、还没配对的左括号同类型，并且结束时没有剩下没配对的左括号。

### English task

Write a function `Balanced()` that takes a string `Text` and returns `TRUE` if the brackets in it are balanced, otherwise `FALSE`. Only the characters `(`, `)`, `[`, `]`, `{` and `}` are checked; all other characters are ignored.

The brackets are balanced when each closing bracket matches the most recent unmatched opening bracket of the same type, and no opening bracket is left unmatched at the end.

In pseudocode, use a local array of characters and a top pointer as a stack (assume `Text` contains at most 100 brackets). Then write the Python function `balanced(text)`; a Python list may be used as the stack.

## 接口

```python
def balanced(text: str) -> bool:
    """Return True if (), [] and {} are correctly matched and nested in text."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION Balanced(Text : STRING) RETURNS BOOLEAN
   DECLARE Stack : ARRAY[1:100] OF CHAR
   DECLARE TopPointer : INTEGER
   // push opening brackets, pop and compare on closing brackets

ENDFUNCTION
```

## 必测行为

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `balanced("()")`、`balanced("([]{})")`、`balanced("{[()()]}")` | `True`、`True`、`True` | 配对与嵌套 |
| B2 | `balanced("a(b[c]d)e")` | `True` | 忽略其他字符 |
| B3 | `balanced("")` | `True` | 空串（边界） |
| B4 | `balanced("(]")`、`balanced("([)]")` | `False`、`False` | 类型不配 / 交错 |
| B5 | `balanced("((")`、`balanced("(")` | `False`、`False` | 结束时栈不空 |
| B6 | `balanced("))")`、`balanced(")(")` | `False`、`False` | 栈空时遇到右括号（不能抛异常） |
| B7 | 返回类型 | `bool` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 只比较左右括号的总数：`([)]`、`)(` 被判为 `True` | B4、B6 |
| M2 | 最后没有检查栈是否为空：`((`、`(` 被判为 `True` | B5 |
| M3 | 遇到右括号时不检查栈是否为空就出栈：`))` 抛 `IndexError` | B6 |

（M1 的参考写法：比较 `text.count` 得到的左、右括号总数是否相等。T10 已用参考实现核对：M1 在 `"))"`、`"(("`、`"("` 上碰巧正确，因为左右括号数不相等；在 `"(]"`、`"([)]"`、`")("` 上出错。）

## 人工核对清单

- [ ] 伪代码：逐字符循环 `FOR Index ← 1 TO LENGTH(Text)` + `MID(Text, Index, 1)`；左括号「`TopPointer ← TopPointer + 1`、`Stack[TopPointer] ← Ch`」。
- [ ] 伪代码：右括号先判断 `TopPointer = 0`（不平衡，`RETURN FALSE`），再取 `Stack[TopPointer]` 比较类型，再 `TopPointer ← TopPointer - 1`。
- [ ] 伪代码：循环结束后 `RETURN TopPointer = 0`（或等价的 IF）。
- [ ] 伪代码：判断括号类型可以用 CASE（每个括号一个子句）或 IF；字符字面量用单引号。
- [ ] Python：能说出 `stack.append(ch)`、`stack.pop()` 分别对应伪代码的哪几行。

## 出处

自编（经典的栈应用）。语法依据：指南 p.10（数组）、p.19（CASE）、p.20（FOR）、p.23（FUNCTION）；插页 9618_w25_in_21 p.2（MID、LENGTH）。
