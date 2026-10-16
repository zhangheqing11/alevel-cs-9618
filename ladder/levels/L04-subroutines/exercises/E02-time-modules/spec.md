# L04/E02 · 按模块说明表写模块：BYREF ↔ 返回元组

| 属性 | 值 |
|:--|:--|
| id | `L04/E02` |
| 目录 | `ladder/levels/L04-subroutines/exercises/E02-time-modules/` |
| 形态 | `function`（三个函数，其中 `add_durations` 打印一行，用 `capsys` + `output_lines` 测） |
| entry | `add_durations`（同一文件还有 `to_minutes`、`split_minutes`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `module-header`, `byval-byref`, `return-value`, `div-mod`, `procedure-call` |
| difficulty | 3 |
| title | `Write three modules from a module table` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L04 card §2、§4、§7；L01 card §5 |

## 练习目标

练 P2 的「模块说明表」题型：从说明里判断过程还是函数、参数与传递方式、返回类型；在一个模块里使用另外两个模块的结果。

## 题面

### 中文导读

按下表写三个模块。注意 `SplitMinutes()` 用 BYREF 把小时、分钟两个结果交回调用者——Python 里改为返回元组 `(hours, minutes)`。`AddDurations()` 必须**使用**另外两个模块，不要重写它们的算法。

### English task

Three modules are defined:

| Module | Description |
|:--|:--|
| `ToMinutes()` | • called with two integer parameters: a number of hours and a number of minutes<br>• returns the total number of minutes |
| `SplitMinutes()` | • called with an integer parameter representing a total number of minutes, and two integer parameters passed by reference<br>• assigns the number of whole hours and the remaining minutes to the two parameters passed by reference |
| `AddDurations()` | • called with four integer parameters: the hours and minutes of a first duration, then the hours and minutes of a second duration<br>• uses `ToMinutes()` and `SplitMinutes()` to add the two durations<br>• outputs the result in the form `Total: 4 h 5 min` |

Write pseudocode for the three modules. Then write the Python functions:

- `to_minutes(hours, minutes)` returns an `int`
- `split_minutes(total)` returns a tuple `(hours, minutes)` — this replaces the two `BYREF` parameters
- `add_durations(h1, m1, h2, m2)` prints one line and returns nothing; it must call the other two functions.

All values are non-negative integers.

## 接口

```python
def to_minutes(hours: int, minutes: int) -> int:
    """Return hours * 60 + minutes."""
    raise NotImplementedError


def split_minutes(total: int) -> tuple[int, int]:
    """Return (whole hours, remaining minutes). Replaces the two BYREF parameters."""
    raise NotImplementedError


def add_durations(h1: int, m1: int, h2: int, m2: int) -> None:
    """Use to_minutes() and split_minutes(); print 'Total: <h> h <m> min'."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION ToMinutes(Hours : INTEGER, Minutes : INTEGER) RETURNS INTEGER

ENDFUNCTION

PROCEDURE SplitMinutes(BYVAL Total : INTEGER, BYREF Hours : INTEGER, BYREF Minutes : INTEGER)

ENDPROCEDURE

PROCEDURE AddDurations(H1 : INTEGER, M1 : INTEGER, H2 : INTEGER, M2 : INTEGER)
   // must use ToMinutes() and SplitMinutes()

ENDPROCEDURE
```

## 必测行为

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `to_minutes(2, 15)`、`to_minutes(0, 0)`、`to_minutes(0, 59)` | `135`、`0`、`59` | |
| B2 | `split_minutes(135)` | `(2, 15)` | 顺序是（小时，分钟） |
| B3 | `split_minutes(59)`、`split_minutes(60)`、`split_minutes(0)` | `(0, 59)`、`(1, 0)`、`(0, 0)` | 边界 |
| B4 | `add_durations(1, 50, 2, 15)` | 输出恰好一行 `Total: 4 h 5 min` | 分钟进位 |
| B5 | `add_durations(0, 30, 0, 30)` | `Total: 1 h 0 min` | 刚好进 1 小时 |
| B6 | `add_durations(0, 0, 0, 0)` | `Total: 0 h 0 min` | 全零 |
| B7 | `add_durations(10, 5, 0, 55)` | `Total: 11 h 0 min` | |
| B8 | 返回类型 | `to_minutes` 返回 `int`；`split_minutes` 返回由两个 `int` 组成的 `tuple`；`add_durations` 返回 `None` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `split_minutes` 返回顺序颠倒：`return total % 60, total // 60`；`add_durations` 照常解包，B4 输出 `Total: 5 h 4 min` | B2、B3、B4、B5、B7 |
| M2 | 照抄 BYREF：`split_minutes(total)` 在函数里给局部变量 `hours`、`minutes` 赋值但不返回；`add_durations` 里 `hours, minutes = split_minutes(…)` 抛 `TypeError` | B2–B8 |
| M3 | `add_durations` 不用两个模块，直接把小时、分钟分别相加：B4 输出 `Total: 3 h 65 min` | B4、B5、B7 |

## 人工核对清单

- [ ] 伪代码：`ToMinutes` 是 `FUNCTION … RETURNS INTEGER`，用 `RETURN`；`SplitMinutes` 是 `PROCEDURE`，两个结果参数是 `BYREF`（ER w22 9618/23 Q5 p.28：多数考生该用 ByRef 时没用）。
- [ ] 伪代码：`AddDurations` 里调用 `ToMinutes(…)` 时写在表达式里（如 `Total ← ToMinutes(H1, M1) + ToMinutes(H2, M2)`），调用 `SplitMinutes` 时用 `CALL SplitMinutes(Total, Hours, Minutes)`；没有对函数写 `CALL`。
- [ ] 伪代码：`AddDurations` 里用到的局部变量都 `DECLARE` 了；模块里没有多余的 `INPUT`（值已经由参数传入）。
- [ ] 伪代码：`OUTPUT "Total: ", Hours, " h ", Minutes, " min"`——不要用 `&` 连接整数（ER w25 p.16）。
- [ ] Python：`add_durations` 确实调用了 `to_minutes` 和 `split_minutes`。

## 出处

自编。题型参考 P2 常见的「Module | Description」说明表（如 9618_s24_22 Q8，见 ECR P2 2024 p.25–27）。语法依据：指南 p.22–24。
