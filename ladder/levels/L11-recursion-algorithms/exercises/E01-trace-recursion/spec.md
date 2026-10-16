# L11/E01 · 干跑：递归的「深入」与「展开」

| 属性 | 值 |
|:--|:--|
| id | `L11/E01` |
| 目录 | `ladder/levels/L11-recursion-algorithms/exercises/E01-trace-recursion/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2）；另有两个模块也要测 |
| entry | `RunTrace`（同一文件还有 `Countdown`、`Power`） |
| pseudocode | `false` |
| files | `[]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `recursion`, `p4-identifiers` |
| difficulty | 3 |
| title | `Dry run: winding and unwinding in recursion` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L11 card §1 |

## 练习目标

看清递归过程里「递归调用之前的语句」与「之后的语句」各在什么时候执行；追踪递归函数的返回值；再译成 Python。

## 题面

### 中文导读

先手算下面程序输出的 9 行，填进 `PREDICTED`；再把两个模块和主程序译成 Python：`Countdown(N)`、`Power(Base, Exponent)`、`RunTrace()`。`Countdown` 和 `Power` 都必须是递归的。

### English task

Dry-run the pseudocode below and store each line it outputs, in order, in the list `PREDICTED`. Then translate it into Python: the recursive procedure `Countdown(N)`, the recursive function `Power(Base, Exponent)`, and `RunTrace()`, which runs the main program and outputs exactly the same lines.

```pseudocode
PROCEDURE Countdown(N : INTEGER)
   IF N = 0 THEN
      OUTPUT "Go"
   ELSE
      OUTPUT "Down ", N
      CALL Countdown(N - 1)
      OUTPUT "Up ", N
   ENDIF
ENDPROCEDURE

FUNCTION Power(Base : INTEGER, Exponent : INTEGER) RETURNS INTEGER
   IF Exponent = 0 THEN
      RETURN 1
   ELSE
      RETURN Base * Power(Base, Exponent - 1)
   ENDIF
ENDFUNCTION

// main program
CALL Countdown(3)
OUTPUT Power(2, 5)
OUTPUT Power(7, 0)
```

## 接口

```python
PREDICTED: list[str] = []  # fill in by hand BEFORE writing the code


def Countdown(N: int) -> None:
    """Recursive procedure from the pseudocode."""
    raise NotImplementedError


def Power(Base: int, Exponent: int) -> int:
    """Recursive function from the pseudocode."""
    raise NotImplementedError


def RunTrace() -> None:
    """Run the main program."""
    raise NotImplementedError


if __name__ == "__main__":
    RunTrace()
```

（不需要 `answer.pseudo`。）

## 必测行为

期望输出（共 9 行，已用参考实现核对）：

```text
Down 3
Down 2
Down 1
Go
Up 1
Up 2
Up 3
32
1
```

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED` | 恰好等于上面 9 行 |
| B2 | `RunTrace()` 全部输出行（`output_lines`） | 与上面 9 行完全相等 |
| B3 | `Countdown(1)` 的输出行 | `["Down 1", "Go", "Up 1"]` |
| B4 | `Power(3, 4)`、`Power(5, 1)`、`Power(9, 0)` | `81`、`5`、`1` |
| B5 | 递归检查：把 `sol.Power` 换成计数包装后调用 `sol.Power(2, 5)` | 结果 `32`，包装被调用的次数 ≥ 2（函数通过自己的名字调用自己） |

B5 的写法：`orig = sol.Power`；`sol.Power = wrapper`（wrapper 先计数再调用 `orig`）；调用 `sol.Power(2, 5)`；测试结束前恢复。`Countdown` 同法检查（`Countdown(3)` 计数 ≥ 2）。

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `Countdown` 把 `Up` 那一行写在递归调用**之前**：输出 `Down 3`、`Up 3`、`Down 2`…；`PREDICTED` 也照此写 | B1、B2、B3 |
| M2 | `Power` 的基本情况返回 0：所有结果都是 0；`PREDICTED` 写对 | B2、B4、B5 |
| M3 | `Power` 写成循环（不递归），结果正确 | B5 |

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能画出 `Countdown(3)` 的调用栈，并指出「Up」各行是在哪一层返回时输出的。
- [ ] 能写出 `Power(2, 5)` 的展开过程：`2 * Power(2, 4)` = … = `2 * 2 * 2 * 2 * 2 * 1`。
- [ ] Python：递归调用写的是函数自己的名字；没有另写内部辅助函数。

## 出处

自编。依据：考纲 19.2（p.37：write and trace recursive algorithms）；指南 p.22–24。
