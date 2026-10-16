# L09/E01 · 安全转换：try/except ValueError + 范围检查


### 中文导读

写函数 `ConvertMark(MarkString)`：如果 `MarkString` 能被 Python 的 `int()` 转成整数，并且这个整数在 0 到 100 之间（含两端），就返回这个整数；否则返回 `-1`。必须用 `try`/`except ValueError`，不要用不带类型的 `except:`。

### English task

Write a function `ConvertMark()` that takes a string parameter `MarkString`.

- If `MarkString` can be converted to an integer using `int()`, and the integer is between 0 and 100 inclusive, the function returns that integer.
- Otherwise the function returns `-1`.

Use exception handling (`try` / `except ValueError`) for the conversion.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] 用的是 `except ValueError:`，不是不带类型的 `except:` 或 `except Exception:`。
- [ ] `try` 块里只有转换那一行（或很少几行），范围检查放在 `try` 之外或 `else` 里。
- [ ] 函数名、参数名与题目一致（`ConvertMark`、`MarkString`）。
- [ ] 能说出 P2 的伪代码里怎样不用异常完成同样的检查（`IS_NUM` + `STR_TO_NUM` + `INT(Mark) = Mark`，卡片 §1）。

## 出处

自编。依据：考纲 20.2（p.38）；插页 9618_w25_in_21 p.2–3（IS_NUM、STR_TO_NUM）。
