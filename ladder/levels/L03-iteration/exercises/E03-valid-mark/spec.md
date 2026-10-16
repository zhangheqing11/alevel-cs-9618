# L03/E03 · 输入校验：REPEAT…UNTIL ↔ while True + break

| 属性 | 值 |
|:--|:--|
| id | `L03/E03` |
| 目录 | `ladder/levels/L03-iteration/exercises/E03-valid-mark/` |
| 形态 | `function`，但函数内部用 `input()` 读数据：测试用 `feed_input` 喂输入、用 `capsys` 查提示信息、再检查返回值 |
| entry | `get_mark` |
| pseudocode | `true` |
| files | `[]` |
| skills | `post-condition-loop`, `input-validation`, `boundary-values`, `return-value`, `type-conversion` |
| difficulty | 3 |
| title | `Validate a mark with a post-condition loop` |
| adapted_from | `CS50P Lecture 2 notes, "Improving with User Input" (https://cs50.harvard.edu/python/notes/2/#improving-with-user-input), CC BY-NC-SA 4.0; adapted: idea of a while True / break validation loop, applied to a 0-100 mark with an error message and a returned value` |
| 对应卡片小节 | L03 card §3、§4、§5（输入校验）；常见坑 3 |

## 练习目标

用 `REPEAT … UNTIL` 写输入校验，并把它正确译成 Python 的 `while True` + `break`（或 `return`）；函数把有效值**返回**给调用者，而不是打印。

## 题面

### 中文导读

写一个函数：反复输入分数，直到输入的是 0 到 100（含两端）之间的整数为止，然后返回这个分数。每次输入无效时输出一行 `Invalid: must be 0 to 100`；输入有效时不输出任何东西。（本题假设输入的一定是整数。）

### English task

Write a function `GetMark()` that:

- repeatedly prompts for and inputs an integer mark until the mark is between 0 and 100 inclusive
- outputs the message `Invalid: must be 0 to 100` each time an invalid mark is input
- returns the valid mark.

Use a post-condition (`REPEAT … UNTIL`) loop. You may assume every input is an integer.

Then write the Python function `get_mark()`. It reads the marks with `input()`, prints the message after each invalid mark, prints nothing else, and returns the valid mark as an `int`.

## 接口

```python
def get_mark() -> int:
    """Input marks until one is 0-100; print a message for each invalid one; return the valid mark."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION GetMark() RETURNS INTEGER
   DECLARE Mark : INTEGER
   // use a REPEAT ... UNTIL loop

ENDFUNCTION
```

## 必测行为

测试用 `feed_input(monkeypatch, …)` 喂入恰好需要的行数，调用 `sol.get_mark()`，检查返回值，并用 `capsys` 取输出行（规则见 design.md §7.3）。

| # | 输入（按顺序） | 期望返回 | 期望输出行 | 说明 |
|:--|:--|:--|:--|:--|
| B1 | `72` | `72` | （无） | 第一次就有效 |
| B2 | `105`、`-3`、`72` | `72` | `Invalid: must be 0 to 100` ×2 | 两次无效（两侧越界） |
| B3 | `0` | `0` | （无） | 下边界有效 |
| B4 | `100` | `100` | （无） | 上边界有效 |
| B5 | `101`、`100` | `100` | `Invalid: must be 0 to 100` ×1 | 刚好越界一次 |
| B6 | `-1`、`0` | `0` | `Invalid: must be 0 to 100` ×1 | 下边界外侧 |
| B7 | 任一调用的返回值 | `type(result) is int` | | 不是字符串 `"72"` |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 边界用严格不等号：`if 0 < mark < 100`，输入 `0` 被当作无效、程序再要一次输入 → `feed_input` 抛 `AssertionError` | B3–B6 |
| M2 | 校验时转了 `int`，返回的却是原字符串：`text = input(); if 0 <= int(text) <= 100: return text` | B1–B7（返回值比较 / 类型） |
| M3 | 每次输入后都打印消息（包括有效的那次）：B1 多出一行 `Invalid: must be 0 to 100` | B1–B6 |

## 人工核对清单

- [ ] 伪代码：`REPEAT … UNTIL Mark >= 0 AND Mark <= 100`，条件两半都完整（指南 p.20–21、p.16）。
- [ ] 伪代码：循环里先 `OUTPUT` 提示再 `INPUT Mark`；无效时用 `IF … THEN OUTPUT … ENDIF` 给消息；循环后 `RETURN Mark`；没有 `BREAK`。
- [ ] Python：用 `while True` + `break`/`return`（或标志变量）；`UNTIL` 的条件照抄，没有取反。
- [ ] 提示语写在 `input("…")` 里（测试不检查提示语）。
- [ ] 能回答：为什么这里用 `REPEAT` 而不用 `WHILE`（至少要输入一次）。

## 出处

思路改编自 CS50P Lecture 2 讲义 “Improving with User Input”（<https://cs50.harvard.edu/python/notes/2/#improving-with-user-input>，David J. Malan，CC BY-NC-SA 4.0）：`while True` + `break` 的输入校验循环。改动：改为 0–100 的分数、加无效提示、改为返回值。语法依据：指南 p.20–21（REPEAT）、p.23（FUNCTION、RETURN）。
