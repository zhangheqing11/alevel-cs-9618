# 因数和：迭代与递归填空

来源：9618_w23_42 第 2 题（2(a)(i)–2(b)(iii)，6 行，17 分）；QP p.6–8，MS p.17–21。题干与两段伪代码（2(b) 含五个空）按 QP 原页转写；得分点、填空答案与 Python 范例按 MS 原页核对。本题不用数据文件（这份卷的 `StackData.txt` 属于第 1 题）。

## 导读

先把给定的迭代伪代码翻成 Python；再把 2(b) 的递归伪代码补全（五个空）并翻成 Python。两问都在主程序里调用并输出。

- `make try EX=practice/p4/9618_w23_42_q2`（`K=2b` 只测递归部分）。
- 标识符照抄题目：`IterativeCalculate`、`RecursiveValue`，参数名 `Number`、`ToFind`（`p4-identifiers`）。
- `MODULUS` 在 Python 里是 `%`；`<>` 是 `!=`。
- 2(b) 的五个空是得分点：先在草稿上把伪代码补全，再照它写 Python，不要另起一套算法（MS：“remainder of function with nothing superfluous”）。
- 主程序写在 `if __name__ == "__main__":` 下面。

## 英文原题（QP p.6–8）

```text
2   An integer is said to be divisible by another integer if the result of the division is also an integer.

    For example:

    10 is divisible by 1, 2, 5 and 10:
    •  10 ÷ 1 = 10
    •  10 ÷ 2 = 5
    •  10 ÷ 5 = 2
    •  10 ÷ 10 = 1

    10 is not divisible by 4:
    •  10 ÷ 4 = 2.5

    1, 2, 5 and 10 are said to be the divisors of 10.

    The iterative function IterativeCalculate() totals all the divisors of its integer parameter and
    returns this total.

    Example 1: if the parameter is 10, the total will be 18 (1 + 2 + 5 + 10) .
    Example 2: if the parameter is 4, the total will be 7 (1 + 2 + 4) .

    A pseudocode algorithm for IterativeCalculate() is shown.

    FUNCTION IterativeCalculate(Number : INTEGER) RETURNS INTEGER
       DECLARE Total : Integer
       DECLARE ToFind : Integer
       ToFind ← Number
       Total ← 0
       WHILE Number <> 0
          IF ToFind MODULUS Number = 0 THEN
             Total ← Total + Number
          ENDIF
          Number ← Number - 1
       ENDWHILE
       RETURN Total
    ENDFUNCTION

    The operator MODULUS calculates the remainder when one number is divided by another.

    (a) (i)   Write program code for IterativeCalculate().
              Save your program as Question2_N23.
              Copy and paste the program code into part 2(a)(i) in the evidence document.   [5]

        (ii)  Write program code to call IterativeCalculate() with 10 as the parameter and
              output the return value.
              Save your program.
              Copy and paste the program code into part 2(a)(ii) in the evidence document.  [2]

        (iii) Test your program.
              Take a screenshot of the output.
              Save your program.
              Copy and paste the screenshot into part 2(a)(iii) in the evidence document.   [1]

    (b) IterativeCalculate() has been rewritten as the recursive function RecursiveValue().

        A pseudocode algorithm for RecursiveValue() is given. The function is incomplete.

        FUNCTION RecursiveValue(Number : INTEGER, ToFind : INTEGER)
              RETURNS INTEGER
           IF Number = .............. THEN
              RETURN 0
           ELSE
              IF ToFind .............. Number = 0 THEN
                 RETURN .............. + RecursiveValue(Number - 1, ToFind)
              ELSE
                 .............. RecursiveValue(Number - 1, ..............)
              ENDIF
           ENDIF
        ENDFUNCTION

        (i)   Write program code for RecursiveValue().
              Save your program.
              Copy and paste the program code into part 2(b)(i) in the evidence document.   [7]

        (ii)  Write program code to call RecursiveValue() with 50 as the first parameter and 50
              as the second parameter and output the return value.
              Save your program.
              Copy and paste the program code into part 2(b)(ii) in the evidence document.  [1]

        (iii) Test your program.
              Take a screenshot of the output.
              Save your program.
              Copy and paste the screenshot into part 2(b)(iii) in the evidence document.   [1]
```

## Python 接口与测试约定

- `IterativeCalculate(Number)`、`RecursiveValue(Number, ToFind)`：整数参数，返回整数。测试用 10→18、4→7、1→1、7→8、12→28、50→93。
- `RecursiveValue(5, 10)` 只加 10 的、不大于 5 的因数（1 + 2 + 5 = 8）：用来检查 `ToFind` 原样传下去。
- 递归检查：测试把模块里的 `RecursiveValue` 换成计数包装，`RecursiveValue(10, 10)` 应依次以 `Number` = 10, 9, …, 0 被调用（基本情况是 `Number = 0`）；迭代版只调用 1 次。
- 主程序先输出 18，再输出 93；可以带说明文字，测试只按顺序找这两个数。

## 证据文档对照表

MS 2(b)(i) 的三行没有编号：语料 MP1 = “One mark for each gap (5)”（一个点记 5 分），MP2 = 递归调用，MP3 = 其余部分（D37 ②）。其他小问的 `markpoints[].n` 与 MS 圆点顺序一致。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a)(i) | 9618_w23_42:2(a)(i) | 5 | 代码 | `test_2a_iterativecalculate_totals_divisors` · MP2–MP5；`test_2a_iterativecalculate_is_iterative` · MP2、MP5 | MP1 函数头带参数；MP5 与伪代码结构一致 |
| Part 2(a)(ii) | 9618_w23_42:2(a)(ii) | 2 | 代码 | `test_2a_screenshot_outputs_18` · MP1–MP2 | 参数是 10 |
| Part 2(a)(iii) | 9618_w23_42:2(a)(iii) | 1 | 截图 | `test_2a_screenshot_outputs_18` · 输出 18 | 截图清晰 |
| Part 2(b)(i) | 9618_w23_42:2(b)(i) | 7 | 代码 | `test_2b_recursivevalue_totals_divisors` · MP1（空 1–3）；`test_2b_recursivevalue_keeps_tofind` · MP1（空 4–5）；`test_2b_recursivevalue_is_recursive` · MP2 | MP3 其余部分照伪代码、没有多余内容；五个空的写法 |
| Part 2(b)(ii) | 9618_w23_42:2(b)(ii) | 1 | 代码 | `test_2b_screenshot_outputs_93` · 调用并输出 | 参数是 50、50 |
| Part 2(b)(iii) | 9618_w23_42:2(b)(iii) | 1 | 截图 | `test_2b_screenshot_outputs_93` · 输出 93 | 截图清晰 |

按分值：行为可自动测 15 分，只能人工核对 2 分（2(a)(i) MP1 函数头、2(b)(i) MP3 “nothing superfluous”）。

## 人工核对清单

- [ ] 2(a)(i) MP1：`def IterativeCalculate(Number):`；MP2–MP5：`WHILE Number <> 0` 循环、`ToFind % Number == 0`、循环后返回 `Total`，结构与伪代码一致。
- [ ] 2(b)(i) MP1 五个空：`0`、`MODULUS`、`Number`、`RETURN`、`ToFind`（MS p.19）；MP2：两处递归调用都正确且位置对；MP3：其余部分照伪代码，没有多余内容。
- [ ] 2(a)(ii)、2(b)(ii)：主程序分别输出 `IterativeCalculate(10)` 与 `RecursiveValue(50, 50)` 的返回值。
- [ ] 截图格：2(a)(iii) 显示 18；2(b)(iii) 显示 93。
