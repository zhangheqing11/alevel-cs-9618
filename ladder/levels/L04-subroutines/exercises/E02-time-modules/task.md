# L04/E02 · 按模块说明表写模块：BYREF ↔ 返回元组


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

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`ToMinutes` 是 `FUNCTION … RETURNS INTEGER`，用 `RETURN`；`SplitMinutes` 是 `PROCEDURE`，两个结果参数是 `BYREF`（ER w22 9618/23 Q5 p.28：多数考生该用 ByRef 时没用）。
- [ ] 伪代码：`AddDurations` 里调用 `ToMinutes(…)` 时写在表达式里（如 `Total ← ToMinutes(H1, M1) + ToMinutes(H2, M2)`），调用 `SplitMinutes` 时用 `CALL SplitMinutes(Total, Hours, Minutes)`；没有对函数写 `CALL`。
- [ ] 伪代码：`AddDurations` 里用到的局部变量都 `DECLARE` 了；模块里没有多余的 `INPUT`（值已经由参数传入）。
- [ ] 伪代码：`OUTPUT "Total: ", Hours, " h ", Minutes, " min"`——不要用 `&` 连接整数（ER w25 p.16）。
- [ ] Python：`add_durations` 确实调用了 `to_minutes` 和 `split_minutes`。

## 出处

自编。题型参考 P2 常见的「Module | Description」说明表（如 9618_s24_22 Q8，见 ECR P2 2024 p.25–27）。语法依据：指南 p.22–24。
