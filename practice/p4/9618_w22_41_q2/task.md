# 9618_w22_41 第 2 题 · Card 与 Hand：封装、组合与计分

## 导读与 Python 接口

从空白程序完成整道题。标识符与文件名照抄 QP；数组须建立真实 list 并以英文注释类型与大小；私有属性使用双下划线。主程序写在 `if __name__ == "__main__":` 下，提示语放在 `input()` 中。指定的算法自行实现，不用内置 sort / index / max 等代劳（D10）。

同季 _43 与 _41 整卷相同，不另做练习。`CalculateValue(Player)` 使用 MS 的函数名；主程序各牌和两手牌名称不限。QP / MS 要求 Cards 有 10 格，MS p.11 Python 只 append 5 张；参考解分配 10 格。MS p.13 `range(0, 4)` 漏第五张，按 QP 改为 `range(0, 5)`。两手总分分别为 46、85；MS p.15 截图只要求 player 2 wins，测试不要求输出分数或固定措辞。平局分支由人工核对。

## 英文原题（已对照 QP 原页）

### QP p.4

```text
4

2   A computer program is being developed that uses a set of cards. The program is written using
    object-oriented programming.

    The program has two classes: Card and Hand.

    The methods and attributes of these classes are shown:

                                                      Card
      Number : INTEGER                            stores the card number from 1 to 5 inclusive

      Colour : STRING                             stores the card colour: red, blue or yellow
      Constructor()                               takes a number and colour as parameters and sets
                                                  the private values to these parameters

      GetNumber()                                 returns the card number

      GetColour()                                 returns the card colour


                                                      Hand
      Cards : ARRAY[0:9] OF Card                  1D array of type Card

      FirstCard : INTEGER                         stores the position of the first card in the hand

      NumberCards : INTEGER                       stores the number of cards in the hand
      Constructor()                               takes five card objects as parameters, assigns each
                                                  card to the array Cards[], initialises FirstCard to 0
                                                  and NumberCards to 5

      GetCard()                                   takes an index as a parameter and returns the card at
                                                  that index in the array

    (a) (i)     Write program code to declare the class Card, its attributes and constructor.

                Do not write program code for the get methods.

                Use your programming language appropriate constructor.

                All attributes must be private. If you are writing in Python, include attribute declarations
                using comments.

 Save your program as Question2_N22.

 Copy and paste the program code into part 2(a)(i) in the evidence document.
                                                                                                         [5]

         (ii)   Write program code for the class methods GetNumber() and GetColour().

 Save your program.

 Copy and paste the program code into part 2(a)(ii) in the evidence document.
                                                                                                         [3]
© UCLES 2022                                    9618/41/O/N/22
```

### QP p.5

```text
5

        (iii)   The program is tested with the following cards:

                                        Number              Colour
                                           1                    red
                                           2                    red
                                           3                    red
                                           4                    red
                                           5                    red
                                           1                    blue
                                           2                    blue
                                           3                    blue
                                           4                    blue
                                           5                    blue
                                           1                yellow
                                           2                yellow
                                           3                yellow
                                           4                yellow
                                           5                yellow

                Write program code to declare each of these cards as a variable of type Card in the
                main program.


 Save your program.

 Copy and paste the program code into part 2(a)(iii) in the evidence document.
                                                                                                [2]




© UCLES 2022                                   9618/41/O/N/22                           [Turn over
```

### QP p.6

```text
6

    (b) (i)     Write program code to declare the class Hand, its attributes and constructor.

                Do not write the get methods.

                Use your programming language appropriate constructor.

                All attributes must be private. If you are writing in Python, include attribute declarations
                using comments.

 Save your program.

 Copy and paste the program code into part 2(b)(i) in the evidence document.
                                                                                                         [6]

         (ii)   The get method GetCard() takes an index as a parameter and returns the card stored
                at that index in the array.

                Write program code for the method GetCard().

 Save your program.

 Copy and paste the program code into part 2(b)(ii) in the evidence document.
                                                                                                         [2]

        (iii)   Two players are declared with 5 cards each.

                Player 1 has the cards: 1 red, 2 red, 3 red, 4 red, 1 yellow.
                Player 2 has the cards: 2 yellow, 3 yellow, 4 yellow, 5 yellow, 1 blue.

                Write program code to declare player 1 and player 2 as objects of type Hand, with the
                cards indicated.

 Save your program.

 Copy and paste the program code into part 2(b)(iii) in the evidence document.
                                                                                                         [2]




© UCLES 2022                                    9618/41/O/N/22
```

### QP p.7

```text
7

    (c) The function CalculateValue() takes a player’s hand as a parameter and returns a score
        calculated using the following rules:

         •      If a card is red, 5 points are added to the player’s score.
         •      If a card is blue, 10 points are added to the player’s score.
         •      If a card is yellow, 15 points are added to the player’s score.
         •      The number of each card in the hand is added to the player’s score.

          (i)   Write program code for the function CalculateValue().
                Assume that there are only 5 cards in the player’s hand in this function.

 Save your program.

 Copy and paste the program code into part 2(c)(i) in the evidence document.
                                                                                                    [6]

         (ii)   Amend the main program by writing program code to use the function
                CalculateValue() for each of the two players. The player with the highest score wins.

                Output an appropriate message to identify the winning player, or if the game was a draw
                (both players have the same number of points).

 Save your program.

 Copy and paste the program code into part 2(c)(ii) in the evidence document.
                                                                                                    [4]

        (iii)   Test your program.

                Take a screenshot to show the output.

 Copy and paste the screenshot into part 2(c)(iii) in the evidence document.

                                                                                                    [1]




© UCLES 2022                                    9618/41/O/N/22                              [Turn over
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a)(i) | 9618_w22_41:2(a)(i) | 5 | 代码 | `test_2ai_card_private_constructor` · MP2、MP5 | MP1、MP3、MP4 |
| Part 2(a)(ii) | 9618_w22_41:2(a)(ii) | 3 | 代码 | `test_2aii_getters` · MP2、MP3 | MP1 |
| Part 2(a)(iii) | 9618_w22_41:2(a)(iii) | 2 | 代码 | `test_2aiii_biii_main_objects` · MP1、MP2 | — |
| Part 2(b)(i) | 9618_w22_41:2(b)(i) | 6 | 代码 | `test_2bi_hand_constructor` · MP2、MP3、MP5、MP6 | MP1、MP4 |
| Part 2(b)(ii) | 9618_w22_41:2(b)(ii) | 2 | 代码 | `test_2bii_getcard` · MP2 | MP1 |
| Part 2(b)(iii) | 9618_w22_41:2(b)(iii) | 2 | 代码 | `test_2aiii_biii_main_objects` · MP1、MP2 | — |
| Part 2(c)(i) | 9618_w22_41:2(c)(i) | 6 | 代码 | `test_2ci_score_all_five`、`test_2ci_getter_protocol` · MP1、MP2、MP3、MP4、MP5、MP6 | — |
| Part 2(c)(ii) | 9618_w22_41:2(c)(ii) | 4 | 代码 | `test_2cii_main_call_chain` / `test_2ciii_screenshot_player2` · MP1、MP2、 | MP3（调用后赋值 / 返回值比较使用关系人工核对）； MP4 |
| Part 2(c)(iii) | 9618_w22_41:2(c)(iii) | 1 | 截图 | `test_2ciii_screenshot_player2` · 全行 | — |

## 人工核对清单

- [ ] 2(b)(i) MP4: constructor with 5 Card objects as parameters

- [ ] 2(a)(i) MP4: …taking 2 parameters

- [ ] 2(a)(i) MP1: class Card declaration (and end where appropriate)
- [ ] 2(a)(i) MP3: constructor header (and end where appropriate)…
- [ ] 2(a)(ii) MP1: 1 get method as function (and end where appropriate) with no parameters…
- [ ] 2(b)(i) MP1: class Hand declaration (and end where appropriate)
- [ ] 2(b)(ii) MP1: function GetCard() header (and end where appropriate) taking (integer) parameter
- [ ] 2(c)(ii) MP4: … or if there was a draw in appropriate message
- [ ] 类型与大小的英文注释、函数头及参数、类与方法的归属、QP 要求时的私有属性声明符合本题 MS。混合得分点中能测行为的计自动，头部和类型仍须人工复核。
- [ ] 主程序的调用、返回值使用与分支逐项符合 QP；截图清晰并包含题目要求的输入与输出；提示语语义合适。
- [ ] 指定算法的实现没有用内置函数代劳；文件打开 / 关闭位置及异常范围按 MS 检查。

## MS 得分点编号

测试与上表使用语料 `markpoints[].n`。1 分行按全行计；未印 MP 数字的圆点按原页顺序对应。可选点多于行分值时，自动 / 人工分值按点的权重比例折算；结构整体点仅作人工。
