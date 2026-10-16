# L05/E03 · 字母统计：逐字符循环与 OTHERWISE 里的判断

| 属性 | 值 |
|:--|:--|
| id | `L05/E03` |
| 目录 | `ladder/levels/L05-strings/exercises/E03-letter-stats/` |
| 形态 | `function` |
| entry | `letter_stats` |
| pseudocode | `true` |
| files | `[]` |
| skills | `char-loop`, `string-functions`, `case-of`, `byval-byref`, `accumulator` |
| difficulty | 3 |
| title | `Count vowels, consonants and other characters` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L05 card §3、§4；L02 card 常见坑 10；L04 card §4 |

## 练习目标

写标准的逐字符循环（`FOR` + `MID`）；用 `TO_UPPER` 统一大小写后用 CASE 判断元音；在 `OTHERWISE` 里再判断是不是字母（ECR P2 2021 p.32：只用 `OTHERWISE` 会把非字母也算成辅音）；用 BYREF 交回三个计数（Python 返回元组）。

## 题面

### 中文导读

统计一段文字里元音字母（A E I O U，不分大小写）、辅音字母（其余字母）和其他字符（数字、空格、标点等）的个数。伪代码写成过程，三个结果用 BYREF 参数交回；Python 写成函数，返回 `(元音数, 辅音数, 其他数)`。

### English task

Write a procedure `LetterStats()` that takes a string `Text` and three integer parameters passed by reference. It counts, in `Text`:

- the vowels `A`, `E`, `I`, `O`, `U` (upper or lower case)
- the consonants (all other letters `A` to `Z`, upper or lower case)
- all other characters (digits, spaces, punctuation and so on)

and assigns the three counts to the three parameters passed by reference.

Use a count-controlled loop with `MID()`, `TO_UPPER()` and a `CASE` structure. Then write the Python function `letter_stats(text)`, which returns the tuple `(vowels, consonants, others)`.

## 接口

```python
def letter_stats(text: str) -> tuple[int, int, int]:
    """Return (vowels, consonants, others) for text; letters are A-Z in either case."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
PROCEDURE LetterStats(BYVAL Text : STRING, BYREF Vowels : INTEGER, BYREF Consonants : INTEGER, BYREF Others : INTEGER)
   DECLARE Index : INTEGER
   DECLARE Ch : CHAR
   // count-controlled loop, MID(), TO_UPPER() and a CASE structure

ENDPROCEDURE
```

## 必测行为

全部输入只含 ASCII 字符。

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `letter_stats("Hello, World!")` | `(3, 7, 3)` | 普通值：逗号、空格、感叹号是「其他」 |
| B2 | `letter_stats("")` | `(0, 0, 0)` | 空串（边界） |
| B3 | `letter_stats("AEIOUaeiou")` | `(10, 0, 0)` | 大小写元音都要算 |
| B4 | `letter_stats("xyz123")` | `(0, 3, 3)` | 数字是「其他」 |
| B5 | `letter_stats("Y")`、`letter_stats(" ")` | `(0, 1, 0)`、`(0, 0, 1)` | 一个字符 |
| B6 | `letter_stats("Programming 101")` | `(3, 8, 4)` | 最后一个字符也要数到 |
| B7 | 返回类型 | 由三个 `int` 组成的 `tuple` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 「不是元音就是辅音」：没有在 OTHERWISE 里判断是否字母，B1 得 `(3, 10, 0)` | B1、B4、B5、B6 |
| M2 | 判断元音前没有统一大小写，只认小写 `aeiou`：B3 得 `(5, 5, 0)` | B3 |
| M3 | 循环少一次：`for index in range(1, len(text))` 后取 `text[index - 1]`，漏掉最后一个字符：B1 得 `(3, 7, 2)` | B1、B3、B4、B5、B6 |

## 人工核对清单

- [ ] 伪代码：`FOR Index ← 1 TO LENGTH(Text)`，`Ch ← TO_UPPER(MID(Text, Index, 1))`；没有 `Text[Index]`。
- [ ] 伪代码：`CASE OF Ch` 里五个元音各占一个子句（指南 p.19：一个子句一个值或一个范围）；`OTHERWISE` 子句里用 `IF Ch >= 'A' AND Ch <= 'Z' THEN … ELSE … ENDIF` 区分辅音与其他。
- [ ] 伪代码：三个计数在循环前置 0；参数头里三个结果参数是 `BYREF`。
- [ ] Python：可以用 `for ch in text`；元音判断可以用 `ch.upper() in "AEIOU"`。

## 出处

自编。误区依据：ECR P2 2021（9618_s21_22 Q6）p.32：考生用 OTHERWISE 统计非元音时把非字母也算了进去。语法依据：指南 p.19（CASE）、p.20（FOR）、p.24（BYREF）；插页 9618_w25_in_21 p.2（MID、TO_UPPER、LENGTH）。
