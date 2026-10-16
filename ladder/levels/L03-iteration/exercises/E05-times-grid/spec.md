# L03/E05 · 乘法表：嵌套 FOR 与总累加器

| 属性 | 值 |
|:--|:--|
| id | `L03/E05` |
| 目录 | `ladder/levels/L03-iteration/exercises/E05-times-grid/` |
| 形态 | `io`（见 `ladder/design.md` §7.2） |
| entry | `times_grid` |
| pseudocode | `true` |
| files | `[]` |
| skills | `nested-loops`, `count-loop`, `accumulator`, `string-concat`, `loop-bounds` |
| difficulty | 3 |
| title | `Multiplication grid with nested FOR loops` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L03 card §1（指南嵌套 FOR 例子）、§5；L01 card §6 |

## 练习目标

写嵌套 `FOR`：外层管行、内层管列；一行的内容先拼成字符串再输出（伪代码的 `OUTPUT` 每次都换行）；总累加器在两层循环之外初始化。

## 题面

### 中文导读

输入 N（1 到 9），输出 N×N 乘法表：第 i 行是 i×1、i×2、…、i×N，数字之间用一个空格分隔。最后一行输出所有乘积之和 `Total: <和>`。伪代码里一行要先拼成字符串（用 `&` 和 `NUM_TO_STR`），再 `OUTPUT`；行尾多一个空格没关系。

### English task

Write a procedure `TimesGrid()` that:

- prompts for and inputs an integer `N` from 1 to 9
- outputs `N` lines; line `i` contains the products `i * 1`, `i * 2`, …, `i * N`, separated by single spaces
- finally outputs `Total: ` followed by the sum of all the products in the grid.

Use nested `FOR` loops. In pseudocode, build each line as a string with `&` and `NUM_TO_STR()` before outputting it. Then write the Python procedure `times_grid()`. A trailing space at the end of a line is allowed.

## 接口

```python
def times_grid() -> None:
    """Input n (1-9); print an n-by-n multiplication grid, then 'Total: <sum>'."""
    raise NotImplementedError


if __name__ == "__main__":
    times_grid()
```

`answer.pseudo` 模板：

```pseudocode
PROCEDURE TimesGrid()
   DECLARE N : INTEGER
   DECLARE Row : INTEGER
   DECLARE Column : INTEGER
   DECLARE Line : STRING
   DECLARE Total : INTEGER
   // use nested FOR loops

ENDPROCEDURE
```

## 必测行为

每个测试喂 1 行输入。输出行按 design.md §7.3 比对（行尾空格已去掉）。

| # | 输入 | 期望输出行 | 说明 |
|:--|:--|:--|:--|
| B1 | `3` | `1 2 3`、`2 4 6`、`3 6 9`、`Total: 36` | 普通值 |
| B2 | `1` | `1`、`Total: 1` | 最小值 |
| B3 | `5` | `1 2 3 4 5`、`2 4 6 8 10`、`3 6 9 12 15`、`4 8 12 16 20`、`5 10 15 20 25`、`Total: 225` | 两位数乘积 |
| B4 | `9` | 共 10 行；第 9 行 `9 18 27 36 45 54 63 72 81`；最后一行 `Total: 2025` | 最大值 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 两层都用 `range(1, n)`：少一行也少一列，B1 只输出 `1 2`、`2 4`、`Total: 9` | B1–B4 |
| M2 | 总累加器放进外层循环（每行清零）：B1 输出 `Total: 18` | B1、B3、B4 |
| M3 | 数字之间没有分隔：`print(row * column, end="")`，B1 第一行为 `123` | B1、B3、B4 |

## 人工核对清单

- [ ] 伪代码：外层 `FOR Row ← 1 TO N … NEXT Row`，内层 `FOR Column ← 1 TO N … NEXT Column`，`NEXT` 后写循环变量名（指南 p.20）。
- [ ] 伪代码：每行开始前 `Line ← ""`；内层用 `Line ← Line & NUM_TO_STR(Row * Column) & " "`；内层结束后 `OUTPUT Line`（插页 p.2 NUM_TO_STR，指南 p.17 &）。
- [ ] 伪代码：`Total ← 0` 在两层循环之外；以 `ENDPROCEDURE` 结束。
- [ ] Python：每行结束后换行（`print()` 或拼好字符串后 `print(line)`）。

## 出处

自编。结构参考指南 p.20 的嵌套 FOR 例子（行累加器与总累加器）。语法依据：指南 p.17（&）、p.20（FOR、NEXT）；插页 9618_w25_in_21 p.2（NUM_TO_STR）。
