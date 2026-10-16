# L01/E02 · 秒数换算：DIV 与 MOD

| 属性 | 值 |
|:--|:--|
| id | `L01/E02` |
| 目录 | `ladder/levels/L01-variables-io/exercises/E02-split-seconds/` |
| 形态 | `io`（见 `ladder/design.md` §7.2） |
| entry | `split_seconds` |
| pseudocode | `true` |
| files | `[]` |
| skills | `div-mod`, `type-conversion`, `input-prompt`, `output-format`, `declare-variables` |
| difficulty | 1 |
| title | `Split seconds into hours, minutes and seconds` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L01 card §3、§4、§5、§8 |

## 练习目标

写出第一个完整的「提示 → 输入 → 计算 → 输出」过程；用 `DIV`/`MOD`（Python `//`/`%`）做单位换算；体会 `input()` 必须 `int()`。

## 题面

### 中文导读

输入一个秒数（0 到 86399 的整数），把它换算成「几小时、几分钟、几秒」输出，格式如 `1 h 2 min 5 s`。先在 `answer.pseudo` 里写伪代码过程 `SplitSeconds()`：要有提示、有 `DECLARE`、用 `DIV` 和 `MOD`。再在 `solution.py` 里写 Python 版 `split_seconds()`。

### English task

Write a procedure `SplitSeconds()` that:

- prompts for and inputs a whole number of seconds, from 0 to 86399
- outputs the same amount of time as hours, minutes and seconds, in the form `1 h 2 min 5 s`.

Use `DIV` and `MOD` in your pseudocode. Then write the Python procedure `split_seconds()`, which reads the number with `input()` and prints exactly one line in the same format.

## 接口

```python
def split_seconds() -> None:
    """Input a number of seconds (0-86399); print it as '<h> h <m> min <s> s'."""
    raise NotImplementedError


if __name__ == "__main__":
    split_seconds()
```

`answer.pseudo` 模板：

```pseudocode
PROCEDURE SplitSeconds()
   // declare your variables, then prompt, input, calculate and output

ENDPROCEDURE
```

## 必测行为

每个测试喂 1 行输入；期望输出恰好 1 行。

| # | 输入 | 期望输出行 | 说明 |
|:--|:--|:--|:--|
| B1 | `3725` | `1 h 2 min 5 s` | 普通值 |
| B2 | `59` | `0 h 0 min 59 s` | 不满 1 分钟 |
| B3 | `60` | `0 h 1 min 0 s` | 刚好 1 分钟（边界） |
| B4 | `3600` | `1 h 0 min 0 s` | 刚好 1 小时（边界） |
| B5 | `0` | `0 h 0 min 0 s` | 最小值 |
| B6 | `86399` | `23 h 59 min 59 s` | 最大值 |
| B7 | `7199` | `1 h 59 min 59 s` | 分钟要先对 3600 取余：不能出现 119 min |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 用 `/` 代替 `//`：`hours = total / 3600` 等，输出 `1.0347222222222223 h …` | B1 等 |
| M2 | 分钟忘了取余：`minutes = total // 60`（不是 `total % 3600 // 60`），3725 输出 `1 h 62 min 5 s` | B1、B4、B6、B7 |
| M3 | 忘了 `int()`：`total = input()`，随后 `total // 3600` 抛 `TypeError` | 全部 |

## 人工核对清单

- [ ] 伪代码：`INPUT` 之前有 `OUTPUT` 提示语（ECR P2 2024 p.15 把漏提示列为常见错误）。
- [ ] 伪代码：每个变量都 `DECLARE … : INTEGER`；用 `DIV`、`MOD`，没有 `/`。
- [ ] 伪代码：`OUTPUT Hours, " h ", Minutes, " min ", Seconds, " s"` 这类逗号分隔写法，空格写在字符串里。
- [ ] 伪代码：以 `ENDPROCEDURE` 结束；关键字全大写，赋值用 `←`。
- [ ] Python：提示语写在 `input("…")` 里；用 f-string 输出。
- [ ] （可选）用常量 `CONSTANT SecondsPerHour = 3600` / `SECONDS_PER_HOUR = 3600`，并说出这样写的好处（指南 p.8）。

## 出处

自编。语法依据：指南 p.8（DECLARE、CONSTANT）、p.15（INPUT、OUTPUT、DIV、MOD）、p.22（PROCEDURE）。
