# L05/E05 · 凯撒移位：ASC、CHR 与 MOD

| 属性 | 值 |
|:--|:--|
| id | `L05/E05` |
| 目录 | `ladder/levels/L05-strings/exercises/E05-caesar-shift/` |
| 形态 | `function` |
| entry | `caesar_shift` |
| pseudocode | `true` |
| files | `[]` |
| skills | `char-loop`, `char-code`, `div-mod`, `char-compare`, `string-concat` |
| difficulty | 3 |
| title | `Caesar shift with ASC, CHR and MOD` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L05 card §2、§3、§4 |

## 练习目标

用 `ASC`/`CHR` 在字符和编码之间转换，用 `MOD 26` 实现从 Z 绕回 A；分大写、小写两种情况；非字母原样保留；逐字符拼出新串。

## 题面

### 中文导读

把文字里的每个字母在字母表中向后移 `Shift` 位（0 到 25），超过 Z 就从 A 接着数；大写仍是大写，小写仍是小写；其他字符不变。例如 `"XYZ"` 移 3 位得 `"ABC"`，`"Hello, World!"` 移 13 位得 `"Uryyb, Jbeyq!"`。

### English task

Write a function `CaesarShift()` that takes a string `Text` and an integer `Shift` from 0 to 25, and returns a new string in which:

- each upper-case letter is replaced by the letter `Shift` places later in the alphabet, wrapping round from `'Z'` to `'A'`
- each lower-case letter is shifted in the same way, wrapping round from `'z'` to `'a'`
- every other character is unchanged.

Use `ASC()`, `CHR()` and `MOD`. Then write the Python function `caesar_shift(text, shift)`.

## 接口

```python
def caesar_shift(text: str, shift: int) -> str:
    """Shift letters by shift places (0-25), keeping case; other characters unchanged."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION CaesarShift(Text : STRING, Shift : INTEGER) RETURNS STRING
   // use ASC(), CHR() and MOD

ENDFUNCTION
```

## 必测行为

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `caesar_shift("ABC", 1)` | `"BCD"` | 普通 |
| B2 | `caesar_shift("XYZ", 3)` | `"ABC"` | 绕回（边界） |
| B3 | `caesar_shift("Hello, World!", 13)` | `"Uryyb, Jbeyq!"` | 大小写与标点 |
| B4 | `caesar_shift("abc", 0)` | `"abc"` | 移 0 位 |
| B5 | `caesar_shift("", 5)` | `""` | 空串 |
| B6 | `caesar_shift("Zz", 1)` | `"Aa"` | 大小写各自绕回 |
| B7 | `caesar_shift("a-z", 25)` | `"z-y"` | 最大移位 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 不绕回：`chr(ord(ch) + shift)`，B2 得 `"[\]"` | B2、B3、B6、B7 |
| M2 | 小写字母也按 `'A'` 为基准计算：`chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))`，B4 得 `"GHI"` | B3、B4、B6、B7 |
| M3 | 非字母也移位：字母按规则绕回，其他字符写成 `chr(ord(ch) + shift)`；B3 中 `","` 变成 `"9"`，B7 中 `"-"` 变成 `"F"` | B3、B7 |

## 人工核对清单

- [ ] 伪代码：`NewCode ← (ASC(Ch) - ASC('A') + Shift) MOD 26 + ASC('A')`（小写换成 `'a'`）；用 `CHR(NewCode)` 转回字符（插页 p.3）。
- [ ] 伪代码：判断大写/小写用比较 `Ch >= 'A' AND Ch <= 'Z'`；用 `&` 把字符接到结果串上，循环前结果串置 `""`。
- [ ] 伪代码：`FUNCTION … RETURNS STRING`，以 `RETURN` 交回新串。
- [ ] 能说出不用 `MOD`、改用 `IF NewCode > ASC('Z') THEN NewCode ← NewCode - 26` 也行，以及为什么 `Shift` 在 0–25 时这样就够。

## 出处

自编。函数依据：插页 9618_w25_in_21 p.3（ASC、CHR）、p.4（MOD）；指南 p.15（MOD）。
