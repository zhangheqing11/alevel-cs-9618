# L01/E01 · 干跑：赋值、DIV/MOD 与 OUTPUT

| 属性 | 值 |
|:--|:--|
| id | `L01/E01` |
| 目录 | `ladder/levels/L01-variables-io/exercises/E01-trace-basics/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2） |
| entry | `run_trace` |
| pseudocode | `false` |
| files | `[]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `div-mod`, `operator-precedence`, `output-format` |
| difficulty | 1 |
| title | `Dry run: assignment, DIV/MOD and OUTPUT` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L01 card §3、§4、§5、§6 |

## 练习目标

在不运行代码的情况下准确读出一段指南写法的伪代码会输出什么；再把它逐行译成 Python，验证自己的手算。重点：`/` 与 `DIV`、`MOD`；乘法优先于减法；`OUTPUT` 的逗号不加空格；`&` 连接；`INT`。

## 题面

### 中文导读

下面这段伪代码会输出 7 行。**先不要写 Python**：在纸上（或脑子里）一行一行执行，把每次 `OUTPUT` 显示的内容按顺序写进 `PREDICTED` 列表（每个元素是一行，写成字符串）。写完再把伪代码逐行翻译成 Python 函数 `run_trace()`，运行它，看看和你的预测是否一致。两部分都会被测试。

### English task

Dry-run the pseudocode below. Write the exact text of each line it outputs, in order, as strings in the list `PREDICTED`. Then translate the pseudocode line by line into the Python function `run_trace()`, which must print exactly the same lines.

```pseudocode
DECLARE Total : INTEGER
DECLARE Count : INTEGER
DECLARE Mean : REAL
DECLARE Code : STRING
CONSTANT Prefix = "ID-"
Total ← 17
Count ← 5
Mean ← Total / Count
OUTPUT Total DIV Count
OUTPUT Total MOD Count
OUTPUT Mean
Count ← Count + 2
Total ← Total - Count * 2
OUTPUT Total, " ", Count
Code ← Prefix & "42"
OUTPUT Code
OUTPUT INT(Mean * 10)
OUTPUT "Mean is ", Mean, "!"
```

## 接口

```python
PREDICTED: list[str] = []  # fill in by hand BEFORE writing run_trace()


def run_trace() -> None:
    """Translate the pseudocode line by line; print exactly what OUTPUT displays."""
    raise NotImplementedError


if __name__ == "__main__":
    run_trace()
```

（`starter.py` 里 `PREDICTED` 留空列表；不需要 `answer.pseudo`。）

## 必测行为

期望输出（共 7 行，已用参考实现核对）：

```text
3
2
3.4
3 7
ID-42
34
Mean is 3.4!
```

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED` | 恰好等于上面 7 个字符串组成的列表（元素为 `str`） |
| B2 | `run_trace()` 输出行的第 1–2 行 | `"3"`、`"2"`（DIV、MOD 用的是整除与取余，不是 `/`） |
| B3 | 第 4 行 | `"3 7"`（先乘后减：17 − 7×2 = 3；中间只有一个空格） |
| B4 | 第 7 行 | `"Mean is 3.4!"`（`OUTPUT` 逗号不加空格） |
| B5 | `run_trace()` 全部输出行 | 与上面 7 行逐行完全相等（比对规则见 design.md §7.3） |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `PREDICTED` 正确，但 `run_trace()` 用 `print` 的逗号直译 `OUTPUT`：`print(total, " ", count)`、`print("Mean is ", mean, "!")`，输出 `3   7` 与 `Mean is  3.4 !` | B3、B4、B5 |
| M2 | 把 `Total - Count * 2` 算成 `(Total - Count) * 2`：`PREDICTED` 第 4 行写 `"20 7"`，`run_trace()` 也这样算 | B1、B3、B5 |
| M3 | 把 `DIV` 译成 `/`：`PREDICTED` 第 1 行写 `"3.4"`，`run_trace()` 打印 `total / count` | B1、B2、B5 |

## 人工核对清单

- [ ] `PREDICTED` 是在写 `run_trace()` **之前**手算的（导师当面问一句即可）。
- [ ] 能说出第 4 行为什么是 `3 7`：乘法先算；`Count` 在上一行已经变成 7。
- [ ] 能说出 `CONSTANT Prefix = "ID-"` 为什么用 `=` 而不是 `←`（指南 p.8）。
- [ ] Python 里常量写成全大写名字（如 `PREFIX = "ID-"`）。

## 出处

自编。语法依据：指南 p.8（DECLARE、CONSTANT）、p.9（←）、p.15（OUTPUT、DIV、MOD）、p.17（&、INT）。
