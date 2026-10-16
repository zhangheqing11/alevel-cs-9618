# L11/E01 · 干跑：递归的「深入」与「展开」


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

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能画出 `Countdown(3)` 的调用栈，并指出「Up」各行是在哪一层返回时输出的。
- [ ] 能写出 `Power(2, 5)` 的展开过程：`2 * Power(2, 4)` = … = `2 * 2 * 2 * 2 * 2 * 1`。
- [ ] Python：递归调用写的是函数自己的名字；没有另写内部辅助函数。

## 出处

自编。依据：考纲 19.2（p.37：write and trace recursive algorithms）；指南 p.22–24。
