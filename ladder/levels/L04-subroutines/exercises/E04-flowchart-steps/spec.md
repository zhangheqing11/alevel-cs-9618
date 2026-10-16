# L04/E04 · 流程图 → 伪代码：数到 1 要几步

| 属性 | 值 |
|:--|:--|
| id | `L04/E04` |
| 目录 | `ladder/levels/L04-subroutines/exercises/E04-flowchart-steps/` |
| 形态 | `io`（见 `ladder/design.md` §7.2） |
| entry | `count_steps` |
| pseudocode | `true` |
| files | `[]` |
| skills | `flowchart-to-pseudocode`, `pre-condition-loop`, `nested-if`, `div-mod`, `accumulator` |
| difficulty | 3 |
| title | `Flowchart to pseudocode: steps to reach 1` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L04 card §6；L03 card §2 |

## 练习目标

补上 Learner Guide p.20「Write pseudocode from … a flowchart」这一项：从流程图里认出循环（判断框在前、箭头回到判断框 → `WHILE`）和选择（判断框后不回头 → `IF`），写成结构化的伪代码，不用跳转。

## 题面

### 中文导读

把下面的流程图写成过程 `CountSteps()` 的伪代码，再写成 Python 的 `count_steps()`。规则：数是偶数就除以 2，是奇数就乘 3 加 1，数一共做了几次才变成 1。先看清楚：哪个判断框带着回头的箭头？它的 Yes 分支是继续还是退出？

### English task

The flowchart represents an algorithm for the procedure `CountSteps()`. Write pseudocode for the procedure, using structured statements only (no jumps). Then write the Python procedure `count_steps()`, which inputs a positive integer and prints `Steps: ` followed by the number of steps.

```text
              ( START )
                  |
           [ INPUT Number ]
                  |
          [ Set Steps to 0 ]
                  |
                  v
      +--> < Is Number = 1 ? > -- Yes --> [ OUTPUT "Steps: ", Steps ] --> ( END )
      |           |
      |           No
      |           v
      |    < Is Number MOD 2 = 0 ? > -- Yes --> [ Set Number to Number DIV 2 ] --+
      |           |                                                               |
      |           No                                                              |
      |           v                                                               |
      |    [ Set Number to 3 * Number + 1 ]                                       |
      |           |                                                               |
      |           +<--------------------------------------------------------------+
      |           |
      |    [ Set Steps to Steps + 1 ]
      |           |
      +-----------+
```

（流程图用文字画法：`( )` 为开始/结束，`[ ]` 为处理或输入输出，`< >` 为判断。）

## 接口

```python
def count_steps() -> None:
    """Input a positive integer; print 'Steps: <n>' as in the flowchart."""
    raise NotImplementedError


if __name__ == "__main__":
    count_steps()
```

`answer.pseudo` 模板：

```pseudocode
PROCEDURE CountSteps()
   DECLARE Number : INTEGER
   DECLARE Steps : INTEGER
   // write the algorithm from the flowchart

ENDPROCEDURE
```

## 必测行为

每个测试喂 1 行输入；期望输出恰好 1 行。

| # | 输入 | 期望输出行 | 说明 |
|:--|:--|:--|:--|
| B1 | `6` | `Steps: 8` | 6→3→10→5→16→8→4→2→1 |
| B2 | `1` | `Steps: 0` | 一开始就是 1：循环体一次都不执行（边界） |
| B3 | `2` | `Steps: 1` | |
| B4 | `16` | `Steps: 4` | 只走偶数分支 |
| B5 | `7` | `Steps: 16` | |
| B6 | `27` | `Steps: 111` | 步数多 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 把判断写在循环末尾（`REPEAT … UNTIL Number = 1` / `while True` + 末尾判断）：输入 `1` 时先变成 4 再回到 1，输出 `Steps: 3` | B2 |
| M2 | `Steps` 加 1 写进了奇数分支里（没注意两条分支在「Set Steps」之前汇合）：B1 输出 `Steps: 2` | B1、B3、B4、B5、B6 |
| M3 | `Steps` 初值写成 1：全部多 1 | B1–B6 |

## 人工核对清单

- [ ] 伪代码：外层是 `WHILE Number <> 1 … ENDWHILE`——判断框的 Yes 分支是**退出**，所以条件要取反（或用等价写法），并且是前测循环（输入 1 时一次也不执行）。
- [ ] 伪代码：里面是 `IF Number MOD 2 = 0 THEN … ELSE … ENDIF`；`Steps ← Steps + 1` 在 `ENDIF` 之后、`ENDWHILE` 之前。
- [ ] 伪代码：`OUTPUT "Steps: ", Steps` 在循环之后；没有 `GOTO`、`BREAK`；以 `ENDPROCEDURE` 结束。
- [ ] 伪代码：用 `DIV`，不用 `/`（`/` 的结果是 REAL，指南 p.15）。
- [ ] （可选）`INPUT` 前加提示语。流程图里没有提示语，加上不算错。

## 出处

自编（数学上称 Collatz 过程）。流程图写法参考 9618_s24_22 Q2 的流程图题（ECR P2 2024 p.8–11）。语法依据：指南 p.15（DIV、MOD）、p.18（IF）、p.21（WHILE）、p.22（PROCEDURE）。
