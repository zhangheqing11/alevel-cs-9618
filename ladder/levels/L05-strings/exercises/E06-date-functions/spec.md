# L05/E06 · 日期函数：插页 ↔ datetime.date

| 属性 | 值 |
|:--|:--|
| id | `L05/E06` |
| 目录 | `ladder/levels/L05-strings/exercises/E06-date-functions/` |
| 形态 | `function`（四个函数；参数与返回值用 `datetime.date`） |
| entry | `date_to_string`（同一文件还有 `day_index`、`set_date`、`is_weekend`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `date-functions`, `string-functions`, `type-conversion`, `boolean-return` |
| difficulty | 3 |
| title | `Insert date functions and datetime.date` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L05 card §5、§6；常见坑 10、11 |

## 练习目标

把插页的 `DAYINDEX`、`SETDATE` 写成 Python（注意星期编号与参数顺序都和 Python 不同）；用 `DAY`/`MONTH`/`YEAR` + `NUM_TO_STR` + 补前导零，把日期变成 `DD/MM/YYYY` 字符串；用 `DAYINDEX` 判断周末。

## 题面

### 中文导读

Python 部分写四个函数：`day_index(d)` 与插页 `DAYINDEX` 相同（星期日 = 1 … 星期六 = 7）；`set_date(day, month, year)` 与插页 `SETDATE` 参数顺序相同；`date_to_string(d)` 返回 `DD/MM/YYYY`（日、月不足两位补 0）；`is_weekend(d)` 判断是不是星期六或星期日。伪代码部分只写后两个函数：`DateToString()` 与 `IsWeekend()`，直接使用插页的 `DAY`、`MONTH`、`YEAR`、`DAYINDEX`。

### English task

Python part — write four functions using `datetime.date`:

- `day_index(d)` returns the same value as the insert function `DAYINDEX()`: Sunday = 1, Monday = 2, …, Saturday = 7
- `set_date(day, month, year)` returns the same value as the insert function `SETDATE()`, with the parameters in the same order
- `date_to_string(d)` returns the date as a string in the form `DD/MM/YYYY`, with a leading `0` added to a one-digit day or month
- `is_weekend(d)` returns `True` if the date is a Saturday or a Sunday, otherwise `False`.

Pseudocode part — write the functions `DateToString()` and `IsWeekend()`, using the insert functions `DAY()`, `MONTH()`, `YEAR()`, `NUM_TO_STR()`, `LENGTH()` and `DAYINDEX()`.

## 接口

```python
from datetime import date


def day_index(d: date) -> int:
    """Like DAYINDEX(): Sunday = 1, Monday = 2, ..., Saturday = 7."""
    raise NotImplementedError


def set_date(day: int, month: int, year: int) -> date:
    """Like SETDATE(Day, Month, Year): note the parameter order."""
    raise NotImplementedError


def date_to_string(d: date) -> str:
    """Return 'DD/MM/YYYY' with leading zeros for day and month."""
    raise NotImplementedError


def is_weekend(d: date) -> bool:
    """Return True for Saturday or Sunday."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION DateToString(ThisDate : DATE) RETURNS STRING
   // use DAY(), MONTH(), YEAR(), NUM_TO_STR() and LENGTH()

ENDFUNCTION

FUNCTION IsWeekend(ThisDate : DATE) RETURNS BOOLEAN
   // use DAYINDEX()

ENDFUNCTION
```

## 必测行为

已用 Python 核对星期：2023-05-09 星期二；2027-05-02 星期日；2027-05-03 星期一；2027-05-08 星期六；2026-10-16 星期五。

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `day_index(date(2023, 5, 9))` | `3` | 插页原例 `DAYINDEX(09/05/2023)` |
| B2 | `day_index(date(2027, 5, 2))`、`day_index(date(2027, 5, 8))` | `1`、`7` | 星期日、星期六（两端） |
| B3 | `day_index(date(2027, 5, 3))`、`day_index(date(2026, 10, 16))` | `2`、`6` | 星期一、星期五 |
| B4 | `set_date(26, 10, 2003)` | `date(2003, 10, 26)` | 插页原例 `SETDATE(26, 10, 2003)` |
| B5 | `date_to_string(date(2003, 10, 4))` | `"04/10/2003"` | 日补 0 |
| B6 | `date_to_string(date(2027, 1, 5))` | `"05/01/2027"` | 日、月都补 0 |
| B7 | `date_to_string(date(2027, 12, 31))` | `"31/12/2027"` | 不需补 0 |
| B8 | `is_weekend(date(2027, 5, 2))`、`is_weekend(date(2027, 5, 8))`、`is_weekend(date(2027, 5, 3))` | `True`、`True`、`False` | |
| B9 | 返回类型 | `day_index` → `int`；`set_date` → `date`；`date_to_string` → `str`；`is_weekend` → `bool` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `day_index` 直接返回 `d.isoweekday()`（星期一 = 1）：B1 得 2；`is_weekend` 按 `day_index in (1, 7)` 判断也跟着错 | B1、B2、B3、B8 |
| M2 | `set_date` 照搬参数顺序：`return date(day, month, year)`，B4 抛 `ValueError` | B4 |
| M3 | 不补前导零：`f"{d.day}/{d.month}/{d.year}"`，B5 得 `"4/10/2003"` | B5、B6 |

## 人工核对清单

- [ ] 伪代码：`DateToString` 先用 `NUM_TO_STR(DAY(ThisDate))` 等得到字符串，再 `IF LENGTH(DD) = 1 THEN DD ← "0" & DD ENDIF`；最后 `RETURN DD & "/" & MM & "/" & YYYY`——数字经 `NUM_TO_STR` 后才用 `&`。
- [ ] 伪代码：`IsWeekend` 写成 `RETURN DAYINDEX(ThisDate) = 1 OR DAYINDEX(ThisDate) = 7`（或等价的 IF）；返回 `BOOLEAN`。
- [ ] 伪代码：参数类型写 `DATE`（指南 p.7）；函数用 `RETURN`，不用 `OUTPUT`（ER w24 9618/21 Q6 p.17、9618/23 Q6 p.28 在日期函数题里都点名了这一点）。
- [ ] Python：`date` 的 `day`、`month`、`year` 是属性，不加括号；能说出 `weekday()` 与 `isoweekday()` 的区别。

## 出处

自编。函数依据：插页 9618_w25_in_21 p.3（DAY、MONTH、YEAR、DAYINDEX、SETDATE 及原例）、p.2（NUM_TO_STR、LENGTH）。误区依据：ER w24（9618/21 Q6 p.17；9618/23 Q6 p.28，后者还点名「DAYINDEX() 收到了错误类型的参数」）。
