# 9618_s22_42 第 3 题 · Card selection without replacement

标识符及文件名照 QP；数组建成真实 list，并用英文注释注明类型与大小（D10）。从空文件完成，主程序放在 `if __name__ == "__main__":` 下，提示写在 `input("…")` 中。按 `make try EX=practice/p4/9618_s22_42_q3 K=3b` 可分问测试。对象私有属性使用 `self.__Name`；测试允许正确的循环实现，不靠指定变量名或固定提示语判分。
来源：QP pp.7–9；MS pp.25–35。已看 QP 全题原页、MS Python 范例原页；证据格与官方 evidence.doc 逐格核对。

## 英文原题（对照 QP 原页转写）

```text
7

3   A programmer is designing a computer game that uses a set of cards.

    Each card has a number and a colour. The cards are saved in the text file CardValues.txt

    The program has a class named Card. The class has the following attributes and methods.

                                                Card
      Number : INTEGER            The number of the card

      Colour : STRING             The colour of the card
      Constructor()               Takes two values as parameters and sets them to the private
                                  attributes

      GetNumber()                 Returns the number of the card

      GetColour()                 Returns the colour of the card

    (a) The constructor takes the number and colour of the card as parameters and sets them to the
        private attributes.

         Write program code to declare the class Card and its constructor. Do not write any other
         methods.

         Use your programming language appropriate constructor.

         All attributes should be private. If you are writing in Python, include attribute declarations
         using comments.

 Save your program as Question3_J22.

 Copy and paste the program code into part 3(a) in the evidence document.
                                                                                                    [5]

    (b) The two get methods return the associated attribute.

         Write program code for the get methods GetNumber() and GetColour().

 Save your program.

 Copy and paste the program code into part 3(b) in the evidence document.
                                                                                                    [3]





                                                         8

    (c) The text file CardValues.txt stores the data for 30 cards, in the order: number, colour.

         For example, the first card in the text file:

                1 is the number
                red is the colour.

         A 1D array of type Card is declared to store all the cards read in from CardValues.txt

         Write the main program to:

         •      declare an array of type Card with 30 elements
         •      read in the data for the 30 cards from CardValues.txt and assign each to the array.

 Save your program.

 Copy and paste the program code into part 3(c) in the evidence document.
                                                                                                   [7]

    (d) The program needs to allow all players (maximum of 5) to select 4 cards from the 30 available.
        A card can only be selected once, so the program needs to record which cards have already
        been selected.

         The function, ChooseCard():

         •      takes as input an integer to represent an array index from 1 to 30
         •      validates that the value is between 1 and 30 inclusive
         •      checks if the card is available (it has not already been selected)
         •      loops until an available card is selected
         •      returns the index of the card if it is available.

         Amend the program to store which cards have already been selected and write program
         code for the function ChooseCard().

 Save your program.

 Copy and paste the program code into part 3(d) in the evidence document.
                                                                                                   [6]

    (e) The main program needs to allow one player to select all their 4 cards.

          (i)   Amend the main program to:

                •   create an array, Player1, for player 1 of type Card
                •   ask player 1 to input 4 integers using the function from part 3(d)
                •   store the cards in Player1
                •   output the number and colour of the 4 cards in Player1.

 Save your program.

 Copy and paste the program code into part 3(e)(i) in the evidence document.
                                                                                                   [5]



                                                      9

         (ii)   Test your program with the following test data:

                Test 1: 1      5       9       10

                Test 2: 2      2       3       4          4      5

                Take a screenshot to show the output.

 Copy and paste the screenshot into part 3(e)(ii) in the evidence document.
                                                                              [1]
```

## Python 接口与 QP / MS 差异

接口取 QP 的 `ChooseCard()`（大写 C），用 MS 的全局 `NumbersChosen` 保存 30 个 BOOLEAN；返回 0–29 下标。`CardArray` 与 `Player1` 在主程序建立，测试运行完整入口后读取这两个数组。MS p.32 的 `chooseCard` / `true` / `NumbersChosen(...)` 分别修为 `ChooseCard` / `True` / 方括号下标；p.29 的 `File.close` 改为 `with` 自动关闭，去掉颜色行的换行。MS p.35 测试 2 将 white 误写为 while，按 QP 数据文件输出 white。输出可为“数字 颜色”或“颜色 数字”，同一张牌可分两行。3(c) 10 个可选点最多 7 分，3(d) 9 个可选点最多 6 分。缺文件测试在读取阶段后停止，避免对 QP 未规定的后续选择作要求。

## 证据文档对照表

| 证据格 | 行 id | 分 | 内容 | 自动测（测试名 · 语料得分点） | 人工核对 |
|:--|:--|--:|:--|:--|:--|
| Part 3(a) | 9618_s22_42:3(a) | 5 | 代码 | `test_3a_private_constructor` · MP3, MP5 | MP1, MP2, MP4 |
| Part 3(b) | 9618_s22_42:3(b) | 3 | 代码 | `test_3b_both_getters` · MP2, MP3 | MP1 |
| Part 3(c) | 9618_s22_42:3(c) | 7 | 代码 | `test_3c_reads_all_cards_and_3e_player` / `test_3c_missing_file_message` · MP1, MP2, MP3, MP4, MP5, MP6, MP7, MP8, MP9 | MP10 |
| Part 3(d) | 9618_s22_42:3(d) | 6 | 代码 | `test_3d_validation_and_duplicate_rejection` · MP1, MP2, MP3, MP4, MP5, MP6, MP7, MP8, MP9 | — |
| Part 3(e)(i) | 9618_s22_42:3(e)(i) | 5 | 代码 | `test_3c_reads_all_cards_and_3e_player` / `test_3e_ii_both_screenshots` · MP1, MP2, MP3, MP4, MP5 | — |
| Part 3(e)(ii) | 9618_s22_42:3(e)(ii) | 1 | 截图 | `test_3e_ii_both_screenshots` · 整行 | — |

自动覆盖表示行为得到验证；混合点里的函数头、注释、调用结构仍须补核，不能凭测试自动授予考试分数。可选得分点多于该行满分时，按 markpoints[].marks 加权后按该行满分比例折算。

## 人工核对清单

- [ ] 3(a) MP1：Card class declaration (and end where appropriate)
- [ ] 3(a) MP2：Both attributes (Number and Colour) declared with suitable data types …
- [ ] 3(a) MP4：correct constructor header (and end where appropriate) with two parameters …
- [ ] 3(b) MP1：1 get method header (and close where appropriate) with no parameter …
- [ ] 3(c) MP10：Closing the file in a suitable place
- [ ] 所有方法头、主程序的调用顺序、返回值接收与题给标识符符合该题 MS；属性注释写明类型，私有属性不改成公有属性。
- [ ] 题目指定算法自行实现，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳（D10 ③；本项人工核对）。
- [ ] 截图清晰，输入、输出及要求的文件名可见；appropriate message 的语义与状态一致（措辞不限）。

## 得分点编号（D37 ②）

编号采用语料 markpoints[].n；1 分且未拆分的行记“整行”。本题 MS 圆点顺序与语料一致；若 MS 给可选点上限，按该行上限计分。
