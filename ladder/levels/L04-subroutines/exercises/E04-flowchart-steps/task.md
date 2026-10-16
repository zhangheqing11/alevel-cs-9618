# L04/E04 · 流程图 → 伪代码：数到 1 要几步


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

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

提示语写在 `input("…")` 中，不要另用 `print` 输出提示；只打印题目规定的输出。

## 人工核对清单

- [ ] 伪代码：外层是 `WHILE Number <> 1 … ENDWHILE`——判断框的 Yes 分支是**退出**，所以条件要取反（或用等价写法），并且是前测循环（输入 1 时一次也不执行）。
- [ ] 伪代码：里面是 `IF Number MOD 2 = 0 THEN … ELSE … ENDIF`；`Steps ← Steps + 1` 在 `ENDIF` 之后、`ENDWHILE` 之前。
- [ ] 伪代码：`OUTPUT "Steps: ", Steps` 在循环之后；没有 `GOTO`、`BREAK`；以 `ENDPROCEDURE` 结束。
- [ ] 伪代码：用 `DIV`，不用 `/`（`/` 的结果是 REAL，指南 p.15）。
- [ ] （可选）`INPUT` 前加提示语。流程图里没有提示语，加上不算错。

## 出处

自编（数学上称 Collatz 过程）。流程图写法参考 9618_s24_22 Q2 的流程图题（ECR P2 2024 p.8–11）。语法依据：指南 p.15（DIV、MOD）、p.18（IF）、p.21（WHILE）、p.22（PROCEDURE）。
