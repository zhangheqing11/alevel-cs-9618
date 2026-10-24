# 递归计数与逐字符拆分语句

来源：9618_w25_43 第 3 题（3(a)(i)–3(b)(iv)，7 行，20 分）；QP p.12–13，MS p.32–39。本次逐页查看了这些 QP / MS 渲染图，Python 缩进按原页核对；证据格按官方 evidence.doc 核对。本题没有数据文件（同卷的 BinaryData.txt 属于第 2 题）。

## 导读

先递归统计整数数组中某个数出现的次数，再逐字符读取一个含四条语句的字符串，遇到分号就存下当前语句，最后逐行输出。

- `make try EX=practice/p4/9618_w25_43_q3`；`K=3ai` 可只测递归部分。
- 标识符照抄题目：`RecursiveCount`、`ArrayCopy`、`NumberElements`、`DataToFind`、`SplitData`（p4-identifiers）。
- 数组要建出真实 list，并注释类型与大小（D10 ①）；主程序写在 `if __name__ == "__main__":` 下，导入时不运行。MS 将主程序写在顶层，此入口调整不影响调用和输出得分点。
- 必须递归，且每次传入去掉首元素的数组；不能用 `count()`、`in` 等代劳统计（D10 ③）。
- `SplitData()` 不能用 `split()` 等内置拆分方法，要自己比较字符、拼接字符串。可使用 `for` 或 `while`，不用照抄 MS 的循环形式。

## 英文原题（QP p.12–13）

```text
3   A program is written to perform different individual processes using arrays.

    (a) A 1D array stores 10 integers.

        (i) A recursive function RecursiveCount() takes three parameters:
            • ArrayCopy, an array of integers
            • NumberElements, the number of elements in the array of integers
            • DataToFind, an integer data to find in the array.

            The function counts and returns the number of times DataToFind is in ArrayCopy

            The recursive algorithm:
            • returns 0 if there are no elements in ArrayCopy
            • compares the first element in ArrayCopy with DataToFind
              ◦ if the element matches, the function returns 1 added to the return value from a
                recursive call (passing the array without the first element)
              ◦ if the element does not match, the function returns the return value from a
                recursive call (passing the array without the first element).

            Write program code for RecursiveCount()
            Save your program as Question3_N25.
            Copy and paste the program code into part 3(a)(i) in the evidence document. [6]

        (ii) The main program stores the following data in a 1D array of integers in the order given:
             0  5  1  2  5  9  9  6  5  0

             The main program calls RecursiveCount() with the parameters:
             • 0 as the data to find
             • 10 as the number of elements
             • the array of 10 integers.

             The return value is output.
             Write program code for the main program.
             Save your program.
             Copy and paste the program code into part 3(a)(ii) in the evidence document. [3]

        (iii) Test your program.
              Take a screenshot of the output(s).
              Save your program.
              Copy and paste the screenshot(s) into part 3(a)(iii) in the evidence document. [1]

    (b) The program stores the following string. The string has four statements that are each
        terminated by a semi-colon ';'
        "x=0;y=1;x=x+y;y++;"

        (i) Write program code to amend the main program to store the string "x=0;y=1;x=x+y;y++;"
            in a local variable.
            Save your program.
            Copy and paste the program code into part 3(b)(i) in the evidence document. [1]

        (ii) The function SplitData() splits a string parameter into four individual lines of code.
             The function creates an array of the strings where each line is stored in a new array
             element without the semi-colon.
             The function returns the array of strings.
             Do not use an inbuilt function to split the string.
             Write program code for SplitData()
             Save your program.
             Copy and paste the program code into part 3(b)(ii) in the evidence document. [6]

        (iii) The main program needs to call SplitData() with the string from part 3(b)(i). The
              main program then needs to output each element from the returned array on a new line.
              Write program code to amend the main program.
              Save your program.
              Copy and paste the program code into part 3(b)(iii) in the evidence document. [2]

        (iv) Test your program.
             Take a screenshot of the output(s).
             Save your program.
             Copy and paste the screenshot(s) into part 3(b)(iv) in the evidence document. [1]
```

## Python 接口与测试约定

- `RecursiveCount` 的三个参数名用 QP 给定的 `ArrayCopy`、`NumberElements`、`DataToFind`；QP 列表顺序与 MS 范例的 `RecursiveCount(DataToFind, ArrayCopy, NumberElements)` 不同，测试用关键字传参，两种顺序均可。数组与元素个数一致，不测试不一致的输入（D31）。
- 递归测试包装模块中的同名函数，检查每次递归的数组确实少首元素、个数减 1、目标值不变；10 个元素加空数组基本情况共 11 次调用。也测试空数组、全匹配、不匹配及目标在最后一位的情况。
- `SplitData(DataString)`：参数为四条由分号终止的语句，返回四条不带分号的字符串。允许与 MS Java/VB 范例类似的预分配数组在有效元素后留空位；不要求处理少于四条、缺末尾分号或带引号内分号等 QP 未定义的输入。
- 测试用字符串子类禁用直接调用的 `split` / `rsplit` / `partition` 等方法；是否借别的内置函数绕过算法仍需人工核对。
- 截图输出按 MS：3(a)(iii) 包含数值 `2`；3(b)(iv) 按顺序分行包含 `x=0`、`y=1`、`x=x+y`、`y++`。不限定额外说明文字（D31）。
- **与 MS 不一致、按 QP 处理（D31）**：MS p.38 的 3(b)(iii) 第一得分点写 “with array as argument”，QP 明确传入 3(b)(i) 的字符串，且 MS 自己的三种语言范例也传 `Code` 字符串；参考解与测试传字符串。
- 参考解保留 MS 的逐字符拆分算法；QP 保证四个完整语句，所以省去 MS 的兜底 `try/except`，不扩展未定义输入的要求。

## 证据文档对照表

本题 MS 没有印数字 MP 编号；下列 MP1 等采用语料 `markpoints[].n`，与原页圆点顺序一致（D37 ②）。三条 1 分行没有拆分 markpoints，以整行给分句计，manifest 记 `whole`。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a)(i) | 9618_w25_43:3(a)(i) | 6 | 代码 | `test_3ai_recursivecount_counts` · MP2–MP5；`test_3ai_each_call_drops_the_first_element` · MP4–MP6 | MP1 三参数函数头；确实实现题给递归算法，不用内置统计 |
| Part 3(a)(ii) | 9618_w25_43:3(a)(ii) | 3 | 代码 | `test_3aii_main_stores_array_and_passes_parameters` · MP1–MP2；`test_3aiii_screenshot_outputs_2` · MP3；`test_3aii_3biii_traced_results` · 实际调用、参数与数据链（D46） | 数组注释 INTEGER、10 个元素；输出的是调用返回值 |
| Part 3(a)(iii) | 9618_w25_43:3(a)(iii) | 1 | 截图 | `test_3aiii_screenshot_outputs_2` · 整行（2） | 截图清晰可读 |
| Part 3(b)(i) | 9618_w25_43:3(b)(i) | 1 | 代码 | `test_3bi_main_stores_the_string` · 整行（在主程序变量中存题给字符串） | 变量局部于主程序 |
| Part 3(b)(ii) | 9618_w25_43:3(b)(ii) | 6 | 代码 | `test_3bii_splitdata_four_statements` · MP2–MP6；`test_3bii_no_inbuilt_split` · MP2–MP4 的算法限制 | MP1 单字符串参数函数头；逐字符比较并拼接，无内置拆分代劳 |
| Part 3(b)(iii) | 9618_w25_43:3(b)(iii) | 2 | 代码 | `test_3biii_main_calls_splitdata_with_the_string` · MP1；`test_3biv_screenshot_four_lines` · MP2；`test_3aii_3biii_traced_results` · 实际调用、参数与数据链（D46） | MP1 使用 SplitData 的返回数组，传字符串（上文 D31） |
| Part 3(b)(iv) | 9618_w25_43:3(b)(iv) | 1 | 截图 | `test_3biv_screenshot_four_lines` · 整行（四条语句分别一行） | 截图清晰可读 |

按得分点分值加权：自动 18 / 20 分（90%），人工 2 / 20 分（10%），人工专属为两个函数头；行为点中附带的结构、注释等仍需看清单。

## 人工核对清单

- [ ] 3(a)(i) MP1：函数头带三个参数，函数有返回值；每次比较首元素，匹配时 `1 +` 递归返回值，不匹配时直接返回递归结果，基本情况返回 0；不用内置统计代劳。
- [ ] 3(a)(ii)：真实 list 按题目顺序存 10 个 INTEGER，注释大小与类型；主程序调用函数并输出返回值，没有把 `2` 写死。
- [ ] 3(b)(i)：字符串逐字符正确，存于主程序的局部变量。
- [ ] 3(b)(ii) MP1：函数带一个字符串参数；遍历字符、与 `;` 比较、拼接、存数组、返回；不借内置拆分函数代劳。真实字符串数组，注释类型及四个有效元素。
- [ ] 3(b)(iii)：传入字符串变量、使用返回数组，循环逐行输出元素，没有把四条输出写死。
- [ ] 两个截图格都有对应输出且清晰可读；以原 MS 的输出内容核对。

### T38c1 · D46 调用与输出核验

既有运行跟踪已观测主程序数组、字符串及调用参数；新增标准追踪并检查 RecursiveCount / SplitData 返回内容与输出。测试继续兼容参数顺序，数组额外未使用格原先已接受；四条语句分行是 QP 要求，保留。

测试观测候选文件中的实际模块调用、参数与返回值；结果与调用记录同时核对。注释、指定算法结构、变量接收返回值及截图呈现仍按人工清单检查；自动占比沿用逐点加权口径。
