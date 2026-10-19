# 数元音：迭代改递归

来源：9618_w23_41 第 1 题（1(a)(i)–1(b)(iii)，6 行，16 分）；QP p.2–3，MS p.4–8。题干与给定伪代码按 QP 原页转写（含 `←`）；得分点与 Python 范例按 MS 原页核对。9618_w23_43 第 1 题与本题整题相同，不另做练习。本题不用数据文件（这份卷的 `QueueData.txt` 属于第 2 题）。

## 导读

先把给定的迭代伪代码照结构翻译成 Python，再把它改写成递归函数。两问都要在主程序里调用并输出结果。

- `make try EX=practice/p4/9618_w23_41_q1`（`K=1b` 只测递归部分）。
- 标识符照抄题目：`IterativeVowels`、`RecursiveVowels`（`p4-identifiers`）。
- 1(a)(i) 要**照题目伪代码的结构**写（MS MP6 “must match structure of given algorithm”）：先算 `LengthString`，循环 `LengthString` 次，每次看第一个字符，再把 `Value` 换成去掉第一个字符的剩余部分。
- `MID(Value, 0, 1)` 对应 `Value[0]`；`MID(Value, 1, LENGTH(Value)-1)` 对应 `Value[1:]`（伪代码里字符串从位置 0 开始，见题目说明）。
- 只数小写元音 a、e、i、o、u；不要先 `lower()`，也不要用 `in "aeiou"` / `count()` 代劳（D10 ③，人工核对）。
- 主程序写在 `if __name__ == "__main__":` 下面。

## 英文原题（QP p.2–3）

```text
1   This iterative pseudocode algorithm for the function IterativeVowels() takes a string as a
    parameter and counts the number of lower-case vowels in this string.
    The vowels are the letters a, e, i, o and u.

    FUNCTION IterativeVowels(Value : STRING) RETURNS INTEGER
       DECLARE Total : INTEGER
       DECLARE LengthString : INTEGER
       DECLARE FirstCharacter : CHAR
       Total ← 0
       LengthString ← LENGTH(Value)
       FOR X ← 0 TO LengthString - 1
          FirstCharacter ← MID(Value, 0, 1)
          IF FirstCharacter = 'a' OR FirstCharacter = 'e' OR
             FirstCharacter = 'i' OR FirstCharacter = 'o' OR
             FirstCharacter = 'u' THEN
                Total ← Total + 1
          ENDIF
          Value ← MID(Value, 1, LENGTH(Value)-1)
       NEXT X
       RETURN Total
    ENDFUNCTION

    The pseudocode function MID(X, Y, Z) returns Z number of characters from string X, starting
    at the character in position Y. The first character in a string is in position 0, for example:

        MID("computer", 0, 3) returns "com"

    The pseudocode function LENGTH(X) returns the number of characters in the string X, for
    example:

        LENGTH("computer") returns 8

    (a) (i)   Write program code for the function IterativeVowels().
              Save your program as Question1_N23.
              Copy and paste the program code into part 1(a)(i) in the evidence document.   [5]

        (ii)  Write program code to call the function IterativeVowels() with the parameter
              "house" from the main program.
              Output the return value.
              Save your program.
              Copy and paste the program code into part 1(a)(ii) in the evidence document.  [2]

        (iii) Test your program.
              Take a screenshot of the output.
              Save your program.
              Copy and paste the screenshot into part 1(a)(iii) in the evidence document.   [1]

    (b) (i)   Rewrite the function IterativeVowels() as a recursive function with the identifier
              RecursiveVowels().
              Save your program.
              Copy and paste the program code into part 1(b)(i) in the evidence document.   [6]

        (ii)  Write program code to call the function RecursiveVowels() with the parameter
              "imagine" from the main program.
              Output the return value.
              Save your program.
              Copy and paste the program code into part 1(b)(ii) in the evidence document.  [1]

        (iii) Test your program.
              Take a screenshot of the output.
              Save your program.
              Copy and paste the screenshot into part 1(b)(iii) in the evidence document.   [1]
```

## Python 接口与测试约定

- `IterativeVowels(Value)`、`RecursiveVowels(Value)`：一个字符串参数，返回整数。测试用 `"house"`→3、`"imagine"`→4、空串→0、`"AEIOU"`→0（只数小写）等。
- 递归检查：测试把模块里的 `RecursiveVowels` 换成计数包装，`"imagine"` 应当调用 8 次（7 个字符各一次 + 空串的基本情况一次，MS MP3 的基本情况是 “length is 0”）。迭代版只应调用 1 次。
- 主程序先输出 1(a)(ii) 的 3，再输出 1(b)(ii) 的 4；输出里可以带说明文字，测试只按顺序找这两个数。

## 证据文档对照表

`markpoints[].n` 与 MS 圆点顺序一致，本题无编号差异（D37 ②）。1(a)(i) MS 列 6 点、封顶 5 分。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a)(i) | 9618_w23_41:1(a)(i) | 5 | 代码 | `test_1a_iterativevowels_counts` · MP2–MP6；`test_1a_iterativevowels_is_not_recursive` · MP6 | MP1 函数头；MP6 结构与给定伪代码一致、没有多余步骤 |
| Part 1(a)(ii) | 9618_w23_41:1(a)(ii) | 2 | 代码 | `test_1a_screenshot_house_outputs_3` · MP1–MP2 | 调用的参数是 `"house"` |
| Part 1(a)(iii) | 9618_w23_41:1(a)(iii) | 1 | 截图 | `test_1a_screenshot_house_outputs_3` · 输出 3 | 截图清晰 |
| Part 1(b)(i) | 9618_w23_41:1(b)(i) | 6 | 代码 | `test_1b_recursivevowels_counts` · MP3–MP6；`test_1b_recursivevowels_is_recursive` · MP1、MP5–MP6 | MP2 函数头（一个字符串参数） |
| Part 1(b)(ii) | 9618_w23_41:1(b)(ii) | 1 | 代码 | `test_1b_screenshot_imagine_outputs_4` · 调用并输出 | 调用的是递归版、参数 `"imagine"` |
| Part 1(b)(iii) | 9618_w23_41:1(b)(iii) | 1 | 截图 | `test_1b_screenshot_imagine_outputs_4` · 输出 4 | 截图清晰 |

得分点 17 个：行为可自动测 15 个，只能人工核对 2 个（1(a)(i) MP1、1(b)(i) MP2 的函数头）。

## 人工核对清单

- [ ] 1(a)(i) MP1：`def IterativeVowels(Value):` 一个字符串参数。
- [ ] 1(a)(i) MP6：照给定伪代码的结构（`Total` 置 0、`LengthString`、循环、取首字符、五个元音的 OR 比较、取剩余部分、返回），没有多余的步骤。
- [ ] 1(b)(i) MP2：`def RecursiveVowels(Value):` 一个字符串参数；MP3：基本情况是长度为 0 时返回 0。
- [ ] 1(a)(ii)、1(b)(ii)：主程序里分别用 `"house"`、`"imagine"` 调用并输出返回值。
- [ ] 截图格：1(a)(iii) 显示 3；1(b)(iii) 显示 4。
