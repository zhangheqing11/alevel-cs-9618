# L09/E02 · 输入校验：名字与分数分别检查、反复输入

| 属性 | 值 |
|:--|:--|
| id | `L09/E02` |
| 目录 | `ladder/levels/L09-exceptions-validation/exercises/E02-input-validation/` |
| 形态 | `function`（两个函数，内部用 `input()`；测试用 `feed_input` 喂输入、用 `capsys` + `output_lines` 查提示，再检查返回值） |
| entry | `InputName`（同一文件还有 `InputScore`） |
| pseudocode | `false` |
| files | `[]` |
| skills | `input-validation`, `exception-handling`, `post-condition-loop`, `boundary-values`, `p4-identifiers` |
| difficulty | 3 |
| title | `Validate a 3-letter name and a score separately` |
| adapted_from | `CS50P Problem Set 3 "Fuel Gauge" (https://cs50.harvard.edu/python/psets/3/fuel/), CC BY-NC-SA 4.0; adapted: idea of catching ValueError and re-prompting, applied to a name and a score validated separately with new rules and messages` |
| 对应卡片小节 | L09 card §2、§4；L03 card §5（输入校验循环） |

## 练习目标

P4 常见的输入校验：每项数据**单独**校验并反复输入；长度要「正好」而不是「最多」；数值用 `try` 判断是不是整数，再做范围检查。

## 题面

### 中文导读

写两个函数。`InputName()`：反复输入，直到输入的是**正好 3 个大写字母**（A 到 Z），每次无效时输出 `Invalid name`，最后返回这个名字。`InputScore()`：反复输入，直到输入的是 0 到 1000（含两端）的整数，每次无效时输出 `Invalid score`，最后返回这个整数。两项分开校验：名字的问题不影响分数，反之亦然（ER s22 9618/41 Q1 p.36）。

### English task

Write two functions.

- `InputName()` repeatedly inputs a player name until it is exactly 3 characters long and every character is an upper-case letter `A` to `Z`. It outputs `Invalid name` after each invalid name and returns the valid name.
- `InputScore()` repeatedly inputs a score until it is an integer from 0 to 1000 inclusive. Use exception handling to detect input that is not an integer. It outputs `Invalid score` after each invalid score and returns the valid score as an integer.

Neither function outputs anything else.

## 接口

```python
def InputName() -> str:
    """Input until a name of exactly 3 upper-case letters is entered; return it."""
    raise NotImplementedError


def InputScore() -> int:
    """Input until an integer from 0 to 1000 is entered; return it."""
    raise NotImplementedError
```

（不需要 `answer.pseudo`。）

## 必测行为

每个测试用 `feed_input` 喂入恰好需要的行数（多要一次就会 `AssertionError`），检查返回值和输出行。

| # | 函数 | 输入（按顺序） | 期望返回 | 期望输出行 | 说明 |
|:--|:--|:--|:--|:--|:--|
| B1 | `InputName` | `ABC` | `"ABC"` | （无） | 第一次就有效 |
| B2 | `InputName` | `AB`、`abc`、`A1C`、`ZZZ` | `"ZZZ"` | `Invalid name` ×3 | 太短、小写、含数字 |
| B3 | `InputName` | `ABCD`、`XYZ` | `"XYZ"` | `Invalid name` ×1 | 太长 |
| B4 | `InputScore` | `500` | `500` | （无） | |
| B5 | `InputScore` | `abc`、`1001`、`-1`、`7.5`、`0` | `0` | `Invalid score` ×4 | 非整数、越界；0 是有效的下边界 |
| B6 | `InputScore` | `1000` | `1000` | （无） | 上边界 |
| B7 | `InputScore` | （空行）、`12` | `12` | `Invalid score` ×1 | 空输入 |
| B8 | 返回类型 | | `InputName` 返回 `str`；`InputScore` 返回 `int` | | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 名字长度写成 `len(Name) <= 3`：`"AB"` 被接受，B2 返回 `"AB"` | B2 |
| M2 | `InputScore` 没有异常处理：`int("abc")` 抛 `ValueError` | B5、B7 |
| M3 | 只检查长度、不检查大写字母：`"abc"` 被接受 | B2 |
| M4 | 分数上端写成 `< 1000`：输入 `1000` 被拒，程序再要输入 → `AssertionError` | B6 |

## 人工核对清单

- [ ] 名字的检查写成「长度正好 3」并逐个字符检查 `"A" <= Ch <= "Z"`（或 `isupper()` 加 `isalpha()` 等价写法）。
- [ ] `InputScore` 用 `try: int(…)` / `except ValueError:`；范围检查不放在 `except` 里。
- [ ] 两个函数各管各的：没有把名字和分数放进同一个循环一起判断。
- [ ] 提示语写在 `input("…")` 里（测试不检查提示语）；函数名与题目一致。

## 出处

思路改编自 CS50P Problem Set 3 “Fuel Gauge”（<https://cs50.harvard.edu/python/psets/3/fuel/>，David J. Malan，CC BY-NC-SA 4.0）：捕捉 `ValueError` 后重新输入。改动：改为名字与分数两项、规则与提示全部重写。误区依据：ER s22 9618/41 Q1 p.36（3 字符名字写成 `<= 3`；两项数据应分别校验）。
