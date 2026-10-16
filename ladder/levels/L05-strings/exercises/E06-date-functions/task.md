# L05/E06 · 日期函数：插页 ↔ datetime.date


### 中文导读

Python 部分写四个函数：`day_index(d)` 与插页 `DAYINDEX` 相同（星期日 = 1 … 星期六 = 7）；`set_date(day, month, year)` 与插页 `SETDATE` 参数顺序相同；`date_to_string(d)` 返回 `DD/MM/YYYY`（日、月不足两位补 0）；`is_weekend(d)` 判断是不是星期六或星期日。伪代码部分只写后两个函数：`DateToString()` 与 `IsWeekend()`，直接使用插页的 `DAY`、`MONTH`、`YEAR`、`DAYINDEX`。

### English task

Python part — write four functions using `datetime.date`:

- `day_index(d)` returns the same value as the insert function `DAYINDEX()`: Sunday = 1, Monday = 2, …, Saturday = 7
- `set_date(day, month, year)` returns the same value as the insert function `SETDATE()`, with the parameters in the same order
- `date_to_string(d)` returns the date as a string in the form `DD/MM/YYYY`, with a leading `0` added to a one-digit day or month
- `is_weekend(d)` returns `True` if the date is a Saturday or a Sunday, otherwise `False`.

Pseudocode part — write the functions `DateToString()` and `IsWeekend()`, using the insert functions `DAY()`, `MONTH()`, `YEAR()`, `NUM_TO_STR()`, `LENGTH()` and `DAYINDEX()`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`DateToString` 先用 `NUM_TO_STR(DAY(ThisDate))` 等得到字符串，再 `IF LENGTH(DD) = 1 THEN DD ← "0" & DD ENDIF`；最后 `RETURN DD & "/" & MM & "/" & YYYY`——数字经 `NUM_TO_STR` 后才用 `&`。
- [ ] 伪代码：`IsWeekend` 写成 `RETURN DAYINDEX(ThisDate) = 1 OR DAYINDEX(ThisDate) = 7`（或等价的 IF）；返回 `BOOLEAN`。
- [ ] 伪代码：参数类型写 `DATE`（指南 p.7）；函数用 `RETURN`，不用 `OUTPUT`（ER w24 9618/21 Q6 p.17、9618/23 Q6 p.28 在日期函数题里都点名了这一点）。
- [ ] Python：`date` 的 `day`、`month`、`year` 是属性，不加括号；能说出 `weekday()` 与 `isoweekday()` 的区别。

## 出处

自编。函数依据：插页 9618_w25_in_21 p.3（DAY、MONTH、YEAR、DAYINDEX、SETDATE 及原例）、p.2（NUM_TO_STR、LENGTH）。误区依据：ER w24（9618/21 Q6 p.17；9618/23 Q6 p.28，后者还点名「DAYINDEX() 收到了错误类型的参数」）。
