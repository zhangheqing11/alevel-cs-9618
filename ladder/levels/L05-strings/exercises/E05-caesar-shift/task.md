# L05/E05 · 凯撒移位：ASC、CHR 与 MOD


### 中文导读

把文字里的每个字母在字母表中向后移 `Shift` 位（0 到 25），超过 Z 就从 A 接着数；大写仍是大写，小写仍是小写；其他字符不变。例如 `"XYZ"` 移 3 位得 `"ABC"`，`"Hello, World!"` 移 13 位得 `"Uryyb, Jbeyq!"`。

### English task

Write a function `CaesarShift()` that takes a string `Text` and an integer `Shift` from 0 to 25, and returns a new string in which:

- each upper-case letter is replaced by the letter `Shift` places later in the alphabet, wrapping round from `'Z'` to `'A'`
- each lower-case letter is shifted in the same way, wrapping round from `'z'` to `'a'`
- every other character is unchanged.

Use `ASC()`, `CHR()` and `MOD`. Then write the Python function `caesar_shift(text, shift)`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`NewCode ← (ASC(Ch) - ASC('A') + Shift) MOD 26 + ASC('A')`（小写换成 `'a'`）；用 `CHR(NewCode)` 转回字符（插页 p.3）。
- [ ] 伪代码：判断大写/小写用比较 `Ch >= 'A' AND Ch <= 'Z'`；用 `&` 把字符接到结果串上，循环前结果串置 `""`。
- [ ] 伪代码：`FUNCTION … RETURNS STRING`，以 `RETURN` 交回新串。
- [ ] 能说出不用 `MOD`、改用 `IF NewCode > ASC('Z') THEN NewCode ← NewCode - 26` 也行，以及为什么 `Shift` 在 0–25 时这样就够。

## 出处

自编。函数依据：插页 9618_w25_in_21 p.3（ASC、CHR）、p.4（MOD）；指南 p.15（MOD）。
