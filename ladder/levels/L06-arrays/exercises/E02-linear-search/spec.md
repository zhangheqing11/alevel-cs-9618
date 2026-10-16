# L06/E02 · 线性查找：并行数组里找分数

| 属性 | 值 |
|:--|:--|
| id | `L06/E02` |
| 目录 | `ladder/levels/L06-arrays/exercises/E02-linear-search/` |
| 形态 | `function` |
| entry | `look_up_mark` |
| pseudocode | `true` |
| files | `[]` |
| skills | `linear-search`, `parallel-arrays`, `array-index`, `string-functions`, `return-value` |
| difficulty | 3 |
| title | `Linear search in parallel arrays` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L06 card §4、§6；L05 card §4 |

## 练习目标

写「找到就停」的线性查找；用同一个下标访问两个并行数组；不区分大小写地比较字符串；找不到时返回约定值。

## 题面

### 中文导读

两个全局数组：`Names` 存学生名，`Marks` 存对应的分数，`NumStudents` 是实际人数。写函数 `LookUpMark(SearchName)`：找到第一个名字与 `SearchName` 相同（**不区分大小写**）的学生，返回他的分数；找不到返回 `-1`。找到后必须立即停止查找。Python 里两个数组作为参数传入。

### English task

A program uses two global 1D arrays, `Names` (`ARRAY[1:50] OF STRING`) and `Marks` (`ARRAY[1:50] OF INTEGER`). `Names[i]` and `Marks[i]` belong to the same student. The global integer `NumStudents` is the number of elements in use, from 0 to 50.

Write a function `LookUpMark()` that takes a name `SearchName` and returns the mark of the first student whose name matches `SearchName`, ignoring case. It returns `-1` if there is no match. The search must stop as soon as a match is found.

Then write the Python function `look_up_mark(names, marks, search_name)`. The two lists are passed as parameters and have the same length (the number of students).

## 接口

```python
def look_up_mark(names: list[str], marks: list[int], search_name: str) -> int:
    """Return the mark of the first name matching search_name (ignoring case), or -1."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// global: Names : ARRAY[1:50] OF STRING
// global: Marks : ARRAY[1:50] OF INTEGER
// global: NumStudents : INTEGER
FUNCTION LookUpMark(SearchName : STRING) RETURNS INTEGER
   // stop searching as soon as a match is found

ENDFUNCTION
```

## 必测行为

除 B6 外都用 `NAMES = ["Ann", "Bo", "Cy", "bo", "Dee"]`、`MARKS = [71, 64, 88, 90, 55]`。

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `look_up_mark(NAMES, MARKS, "Cy")` | `88` | 中间的元素 |
| B2 | `look_up_mark(NAMES, MARKS, "Ann")` | `71` | 第一个元素（边界） |
| B3 | `look_up_mark(NAMES, MARKS, "Dee")` | `55` | 最后一个元素（边界） |
| B4 | `look_up_mark(NAMES, MARKS, "BO")`、`look_up_mark(NAMES, MARKS, "bo")` | `64`、`64` | 不区分大小写；有两个匹配时返回**第一个** |
| B5 | `look_up_mark(NAMES, MARKS, "Zed")` | `-1` | 找不到 |
| B6 | `look_up_mark([], [], "Ann")` | `-1` | 没有学生 |
| B7 | 调用后 `NAMES`、`MARKS` | 内容不变 | 查找不修改数组 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 返回下标而不是分数：`return index + 1`，B1 得 `3` | B1–B4 |
| M2 | 区分大小写：`names[index] == search_name`，`"BO"` 返回 `-1` | B4 |
| M3 | 不提前停止，记住最后一个匹配：`"bo"` 返回 `90` | B4 |
| M4 | 漏查最后一个：`for index in range(len(names) - 1)`，`"Dee"` 返回 `-1` | B3 |

## 人工核对清单

- [ ] 伪代码：用 `WHILE Index <= NumStudents AND Found = FALSE` 这类条件循环，或在 `FOR` 里找到后立即 `RETURN`；没有把 `FOR` 套在 `WHILE` 里（ER w25 p.15–16）。
- [ ] 伪代码：比较写成 `TO_UPPER(Names[Index]) = TO_UPPER(SearchName)`；分数用同一个下标 `Marks[Index]` 取出。
- [ ] 伪代码：循环上界是 `NumStudents`，不是 50，也不是 `LENGTH(Names)`（`LENGTH` 只用于字符串，ER w25 p.15）。
- [ ] 伪代码：以 `RETURN` 交回结果，函数里没有 `OUTPUT`（ECR P4 2021 p.25 点名「在函数里输出而不是返回」）。
- [ ] Python：没有用 `in` 或 `index()` 代替查找循环（ECR P4 2021 p.22）。

## 出处

自编。误区依据：ER w25 p.15–16（混合循环结构）；ECR P4 2021（9618_s21_42）p.22、p.25。语法依据：指南 p.10（数组）、p.21（WHILE）、p.23（FUNCTION）；插页 9618_w25_in_21 p.2（TO_UPPER）。
