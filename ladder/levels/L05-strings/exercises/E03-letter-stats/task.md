# L05/E03 · 字母统计：逐字符循环与 OTHERWISE 里的判断


### 中文导读

统计一段文字里元音字母（A E I O U，不分大小写）、辅音字母（其余字母）和其他字符（数字、空格、标点等）的个数。伪代码写成过程，三个结果用 BYREF 参数交回；Python 写成函数，返回 `(元音数, 辅音数, 其他数)`。

### English task

Write a procedure `LetterStats()` that takes a string `Text` and three integer parameters passed by reference. It counts, in `Text`:

- the vowels `A`, `E`, `I`, `O`, `U` (upper or lower case)
- the consonants (all other letters `A` to `Z`, upper or lower case)
- all other characters (digits, spaces, punctuation and so on)

and assigns the three counts to the three parameters passed by reference.

Use a count-controlled loop with `MID()`, `TO_UPPER()` and a `CASE` structure. Then write the Python function `letter_stats(text)`, which returns the tuple `(vowels, consonants, others)`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`FOR Index ← 1 TO LENGTH(Text)`，`Ch ← TO_UPPER(MID(Text, Index, 1))`；没有 `Text[Index]`。
- [ ] 伪代码：`CASE OF Ch` 里五个元音各占一个子句（指南 p.19：一个子句一个值或一个范围）；`OTHERWISE` 子句里用 `IF Ch >= 'A' AND Ch <= 'Z' THEN … ELSE … ENDIF` 区分辅音与其他。
- [ ] 伪代码：三个计数在循环前置 0；参数头里三个结果参数是 `BYREF`。
- [ ] Python：可以用 `for ch in text`；元音判断可以用 `ch.upper() in "AEIOU"`。

## 出处

自编。误区依据：ECR P2 2021（9618_s21_22 Q6）p.32：考生用 OTHERWISE 统计非元音时把非字母也算了进去。语法依据：指南 p.19（CASE）、p.20（FOR）、p.24（BYREF）；插页 9618_w25_in_21 p.2（MID、TO_UPPER、LENGTH）。
