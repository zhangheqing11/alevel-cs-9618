# 9618_w23_42 第 1 题 · 元音与辅音双栈

覆盖 7 行，共 27 分。QP 原页：[2, 3, 4]；MS 原页：[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]，已逐页渲染核对。证据格另对照官方 evidence.doc。

## 导读

从 starter.py 的空白分节开始写；标识符、文件名照题目。数组必须建出真实 list，并以英文注释注明类型与大小（D10 ①）；指针初值照题目（D10 ②）。排序、查找及 ADT 操作自己写循环，不用 `sort()`、`sorted()`、`index()`、`max()`、`min()` 或成员测试 `in` 代劳（D10 ③）。主程序置于 `if __name__ == "__main__":` 下，以便测试导入；提示语写在 `input("…")` 中。

## 英文原题（QP 原页转写）

```text
Open the evidence document, evidence.doc

Make sure that your name, centre number and candidate number appear on every page of this
document. This document must contain your answers to each question.

Save this evidence document in your work area as:

evidence_ followed by your centre number_candidate number, for example: evidence_zz999_9999

A class declaration can be used to declare a record.

If the programming language used does not support arrays, a list can be used instead.

One source file is used to answer Question 1. The file is called StackData.txt

1   A program stores lower-case letters in two stacks.

    One stack stores vowels (a, e, i, o, u) and one stack stores consonants (letters that are not
    vowels).

    Each stack is implemented as a 1D array.

    (a) (i)     Write program code to declare two 1D global arrays: StackVowel and StackConsonant.

                Each array needs to store up to 100 letters. The index of the first element in each array is 0.

                If you are writing in Python, include declarations using comments.

 Save your program as Question1_N23.

 Copy and paste the program code into part 1(a)(i) in the evidence document.
                                                                                                            [2]

         (ii)   The global variable VowelTop is a pointer that stores the index of the next free space in
                StackVowel.

                The global variable ConsonantTop is a pointer that stores the index of the next free
                space in StackConsonant.

                VowelTop and ConsonantTop are both initialised to 0.

                Write program code to declare and initialise the two variables.

                If you are writing in Python, include declarations using comments.

 Save your program.

 Copy and paste the program code into part 1(a)(ii) in the evidence document.
                                                                                                            [1]






    (b) (i)     The procedure PushData() takes one letter as a parameter.

                If the parameter is a vowel, it is pushed onto StackVowel and the relevant pointer
                updated.

                If the stack is full, a suitable message is output.

                If the parameter is a consonant, it is pushed onto StackConsonant and the relevant
                pointer updated.

                If the stack is full, a suitable message is output.

                You do not need to validate that the parameter is a letter.

                Write program code for PushData().

 Save your program.

 Copy and paste the program code into part 1(b)(i) in the evidence document.
                                                                                               [6]

         (ii)   The file StackData.txt stores 100 lower-case letters.

                The procedure ReadData() reads each letter from the file and uses PushData() to
                push each letter onto its appropriate stack.

                Use appropriate exception handling if the file does not exist.

                Write program code for ReadData().

 Save your program.

 Copy and paste the program code into part 1(b)(ii) in the evidence document.
                                                                                               [6]

    (c) The function PopVowel() removes and returns the data at the top of StackVowel and
        updates the relevant pointer(s).

         The function PopConsonant() removes and returns the data from the top of StackConsonant
         and updates the relevant pointer(s).

         If either stack is empty, the string "No data" must be returned.

         Write program code to declare PopVowel() and PopConsonant().

 Save your program.

 Copy and paste the program code into part 1(c) in the evidence document.
                                                                                               [5]






    (d) The program first needs to call ReadData() and then:

         1.     prompt the user to input their choice of vowel or consonant
         2.     take, as input, the user’s choice
         3.     depending on the user’s choice, call PopVowel() or PopConsonant() and store the
                return value.

         The three steps are repeated until 5 letters have been successfully returned and stored.

         If either stack is empty at any stage, an appropriate message must be output.

         Once 5 letters have been successfully returned and stored, they are output on one line, for
         example:

                abyti

          (i)   Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 1(d)(i) in the evidence document.
                                                                                                    [6]

         (ii)   Test your program with the following inputs:

                    vowel

                    consonant

                    consonant

                    vowel

                    vowel

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 1(d)(ii) in the evidence document.
                                                                                                    [1]
```

## Python 接口与测试约定

- `StackVowel`、`StackConsonant` 均为 100 格全局 list；`VowelTop`、`ConsonantTop` 是下一空位，初值 0。
- `PushData(Letter)`、`ReadData()`、`PopVowel()`、`PopConsonant()` 使用题给名字。主程序选择输入使用 MS 的完整单词 `vowel` / `consonant`。
- 只以小写字母调用 PushData（QP 明确不要求字母校验）；不额外测大小写、标点。满栈与文件缺失输出不限措辞；空栈返回严格为 `No data`。
- 使用官方 StackData.txt；另造 100 个全元音/全辅音的文件检查空栈选择不算一次成功取字母。

## 证据文档对照表

表内 MP 号取语料 markpoints[].n。每行列出自动与人工主归属；类型注释、函数头和截图可读性仍须人工核对。自动占比只统计可观察行为，并非自动给出考试分数。

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a)(i) | 9618_w23_42:1(a)(i) | 2 | 代码 | `test_1a_arrays_and_next_free_pointers` · MP1、MP2 | — |
| Part 1(a)(ii) | 9618_w23_42:1(a)(ii) | 1 | 代码 | `test_1a_arrays_and_next_free_pointers` · MPwhole | — |
| Part 1(b)(i) | 9618_w23_42:1(b)(i) | 6 | 代码 | `test_1b_i_both_stacks_classify_and_overflow` · MP2、MP3、MP4、MP5、MP6 | MP1 Procedure PushData() heading (and end where appropriate) taking one parameter |
| Part 1(b)(ii) | 9618_w23_42:1(b)(ii) | 6 | 代码 | `test_1b_ii_read_official_letters`；`test_1b_ii_missing_file` · MP2、MP3、MP4、MP5、MP6 | MP1 Procedure header ReadData() with no parameter |
| Part 1(c) | 9618_w23_42:1(c) | 5 | 代码 | `test_1c_pop_lifo_empty_and_reuse` · MP2、MP3、MP4、MP5 | MP1 One function header with no parameter |
| Part 1(d)(i) | 9618_w23_42:1(d)(i) | 6 | 代码 | `test_1d_ii_screenshot_utxoe`；`test_1d_i_empty_choice_does_not_count_as_letter` · MP1、MP2、MP3、MP4、MP5、MP6、MP7 | — |
| Part 1(d)(ii) | 9618_w23_42:1(d)(ii) | 1 | 截图 | `test_1d_ii_screenshot_utxoe` · MPwhole | — |

## 人工核对清单

- [ ] 1(b)(i) MP1：Procedure PushData() heading (and end where appropriate) taking one parameter
- [ ] 1(b)(ii) MP1：Procedure header ReadData() with no parameter
- [ ] 1(c) MP1：One function header with no parameter
- [ ] 数组、指针与记录字段的英文类型注释及作用域正确，数组大小与 QP 一致。
- [ ] 按 QP 写指定算法；没有以内置容器操作代替数组 ADT 或查找、排序步骤。
- [ ] 所有截图清晰；输入、输出和要求的文件名可见；截图不能仅由 pytest 成功代替。


## QP / MS 差异与点号对照

- MS pp.4、7、11–12 采用空 list、append 和 del；按 D10 ① 改为固定 100 格数组，下标存取、仅更新指针，不删除实际格子。这不改变题目栈的有效数据。
- MS p.16 的 Python else 实际缩进在 DataAccessed 判断下，原页没有解析文本暗示的缩进缺陷；参考解遵守相同空栈重试逻辑。
- 官方输入 `vowel, consonant, consonant, vowel, vowel` 输出 utxoe（MS p.16），已按源文件实跑。

1(d)(i) 有 7 个候选点，最多 6 分；按候选点分值等权比例折算。其余语料点号与 MS 圆点顺序一致；1 分行不拆。
