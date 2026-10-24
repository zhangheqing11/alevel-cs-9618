# 9618_w24_42 第 1 题 · EventItem 与 Character：按技能算概率与比赛积分

## 导读与 Python 接口

从空白程序完成整道题。标识符与文件名照抄 QP；数组须建立真实 list 并以英文注释类型与大小；QP 要求私有的属性使用双下划线。主程序写在 `if __name__ == "__main__":` 下，提示语放在 `input()` 中。指定的算法自行实现，不用内置 sort / index / max 等代劳（D10）。

构造参数顺序照 MS Python；主程序两名 Character 的变量名不限（MS 用 P1/P2）。QP 类图写 Type / CharacterName，MS Python 写 EventType / CName；参考解用 QP 名称，行为测试容许这两个私有属性的 MS 别名，标识符仍按 QP 人工核对。无数据文件，本卷 HighScoreTable.txt 属第3题，不复制。MS p.17 截图依次 Tarz/Tarz/Tarz/Geni/Tarz，最终 Tarz 4 分。1(e)(ii) 的单场平局 MP5 及 MP6 内总分平局分支人工核对，固定比赛数据无平局；其余积分行为自动测。

## 英文原题（已对照 QP 原页）

### QP p.2

```text
2

Open the evidence document, evidence.doc

Make sure that your name, centre number and candidate number appear on every page of this
document. This document must contain your answers to each question.

Save this evidence document in your work area as:
evidence_ followed by your centre number_candidate number, for example: evidence_zz999_9999

A class declaration can be used to declare a record. If the programming language used does not
support arrays, a list can be used instead.

One source file is used to answer Question 3. The file is called HighScoreTable.txt

1      A computer game is designed for users to select characters. Each character can take part in a
       group of events. Each group has five events. There are four types of event: jump, swim, run, drive.

       The program is written using object-oriented programming.

       (a) The class EventItem stores data about the events.

                                                    EventItem
          EventName : STRING               stores the name of the event
          Type : STRING                    stores the type of event, either: jump, swim, run or drive
          Difficulty : INTEGER             stores the difficulty of the event from 1 (easiest) to 5
                                           (hardest)
          Constructor()                    initialises EventName, Type and Difficulty to its
                                           parameter values
          GetName()                        returns the name of the event
          GetDifficulty()                  returns the difficulty of the event
          GetEventType()                   returns the type of event


            (i)   Write program code to declare the class EventItem and its constructor.

                  Do not declare the other methods.

                  Use your programming language’s appropriate constructor.

                  All attributes must be private.

                  If you are writing in Python, include attribute declarations, using comments.

    Save your program as Question1_N24.

    Copy and paste the program code into part 1(a)(i) in the evidence document.
                                                                                                        [4]




© UCLES 2024                                        9618/42/O/N/24
```

### QP p.3

```text
3

         (ii)   The get methods GetName(), GetDifficulty() and GetEventType() each return
                the relevant attribute.

                Write program code for the three get methods.

 Save your program.

 Copy and paste the program code into part 1(a)(ii) in the evidence document.
                                                                                                   [3]

    (b) The array Group stores five objects of type EventItem.

          (i)   Write program code to declare Group local to the main program.

 Save your program.

 Copy and paste the program code into part 1(b)(i) in the evidence document.
                                                                                                   [1]

         (ii)   One group has the following events:

                      Event name           Event type           Event difficulty
                     Bridge                   jump                     3
                     Water wade               swim                     4
                     100 mile run              run                     5
                     Gridlock                 drive                    2
                     Wall on wall             jump                     4


                Write program code to create an instance of EventItem for each of the five events, and
                store them in Group.

 Save your program.

 Copy and paste the program code into part 1(b)(ii) in the evidence document.
                                                                                                   [3]




© UCLES 2024                                  9618/42/O/N/24                               [Turn over
```

### QP p.4

```text
4

    (c) The class Character stores data about the characters in the game.

         Each character has a skill level for each type of event. The skill level is an integer between
         1 and 5 inclusive. Skill level 1 is the lowest skill level, and skill level 5 is the highest skill level.

                                                 Character
       CharacterName : STRING              stores the name of the character
       Jump : INTEGER                      stores the character’s skill level at events of type jump
       Swim : INTEGER                      stores the character’s skill level at events of type swim
       Run : INTEGER                       stores the character’s skill level at events of type run
       Drive : INTEGER                     stores the character’s skill level at events of type drive
       Constructor()                       initialises CharacterName, Jump, Swim, Run and
                                           Drive to its parameter values
       GetName()                           returns the name of the character
       CalculateScore()                    takes the type of event and difficulty as parameters.
                                           Calculates and returns the chance of the character
                                           completing the event


         Write program code to declare the class Character, its constructor and get method.

         Use your programming language’s appropriate constructor.

         All attributes must be private.

         If you are writing in Python, include attribute declarations, using comments.

 Save your program.

 Copy and paste the program code into part 1(c) in the evidence document.
                                                                                                               [4]




© UCLES 2024                                     9618/42/O/N/24
```

### QP p.5

```text
5

    (d) The method CalculateScore() in the Character class calculates and returns the
        percentage chance of a character completing an event.

         When a character’s skill level is greater than or equal to the difficulty of that event, the
         percentage chance of completing the event is 100%.

         When a character’s skill level is less than the difficulty of that event, the character’s skill level
         is subtracted from the difficulty of that event. This difference is used to identify the percentage
         chance of success using this table:

                                                      Percentage chance
                                    Difference
                                                          of success
                                         1                        80
                                         2                        60
                                         3                        40
                                         4                        20


         For example:

         •     A character has a skill level of 3 for events of type run.
         •     An event of type run has a difficulty level of 5
         •     The character’s skill level is less than the difficulty, therefore the difference is calculated.
         •     The difference is the character’s skill level subtracted from the event difficulty, 5 – 3 = 2
         •     The difference is 2, therefore the percentage chance of succeeding is 60%

         Write program code for the method CalculateScore() to:

         •     take the type of event and difficulty as parameters
         •     calculate the percentage chance of the character completing the event
         •     return the percentage chance of completing the event as an integer number, for example
               60

 Save your program.

 Copy and paste the program code into part 1(d) in the evidence document.
                                                                                                            [4]




© UCLES 2024                                     9618/42/O/N/24                                    [Turn over
```

### QP p.6

```text
6

    (e) Two characters are attempting each event in the group you created in part 1(b).

         One character has the name Tarz and the skill levels:

                Jump    5

                Swim    3

                Run     5

                Drive   1

         The second character has the name Geni and the skill levels:

                Jump    2

                Swim    2

                Run     3

                Drive   4

         Each Character object is stored in a variable.

          (i)   Amend the main program to declare and create an instance of a Character object for
                Tarz and for Geni.

 Save your program.

 Copy and paste the program code into part 1(e)(i) in the evidence document.
                                                                                               [2]




© UCLES 2024                                 9618/42/O/N/24
```

### QP p.7

```text
7

         (ii)   Both characters Tarz and Geni take part in each event in the group you created in part
                1(b).

                These steps are repeated for all five events:

                •   The percentage chance of each character completing the event is calculated and
                    compared.
                •   The character with the highest percentage chance of completing the event gets 1
                    point. Their character name is output together with a message telling them they
                    have won that event.
                •   If both characters have the same percentage chance of completing the event, the
                    scores do not change, and a message is output stating that the event is a draw.

                When the total score for each character has been calculated, the name of the character
                with the highest score is output stating they have won and the number of points they
                have. If both characters have the same number of points, a message is output telling
                them the group is a draw.

                Amend the main program to:

                •   calculate the score for each character in each event
                •   output the name of the character that wins each event or that the event is a draw
                •   output the name of the character that has the most points for the group or that the
                    group is a draw.

 Save your program.

 Copy and paste the program code into part 1(e)(ii) in the evidence document.
                                                                                                    [7]

        (iii)   Test your program.

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 1(e)(iii) in the evidence document.
                                                                                                    [1]




© UCLES 2024                                   9618/42/O/N/24                               [Turn over
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a)(i) | 9618_w24_42:1(a)(i) | 4 | 代码 | `test_1ai_aii_event` · MP2、MP4 | MP1、MP3 |
| Part 1(a)(ii) | 9618_w24_42:1(a)(ii) | 3 | 代码 | `test_1ai_aii_event` · MP2、MP3 | MP1 |
| Part 1(b)(i) | 9618_w24_42:1(b)(i) | 1 | 代码 | `test_1bi_bii_ei_main_objects` · 全行 | — |
| Part 1(b)(ii) | 9618_w24_42:1(b)(ii) | 3 | 代码 | `test_1bi_bii_ei_main_objects` · MP1、MP2、MP3 | — |
| Part 1(c) | 9618_w24_42:1(c) | 4 | 代码 | `test_1c_character` · MP2、MP3、MP4 | MP1 |
| Part 1(d) | 9618_w24_42:1(d) | 4 | 代码 | `test_1d_all_skills_difficulties` · MP2、MP3、MP4、MP5 | MP1 |
| Part 1(e)(i) | 9618_w24_42:1(e)(i) | 2 | 代码 | `test_1bi_bii_ei_main_objects` · MP1、MP2 | — |
| Part 1(e)(ii) | 9618_w24_42:1(e)(ii) | 7 | 代码 | `test_1eiii_screenshot` · MP1、MP2、MP3、MP4、MP6、MP7 | MP5 |
| Part 1(e)(iii) | 9618_w24_42:1(e)(iii) | 1 | 截图 | `test_1eiii_screenshot` · 全行 | — |

## 人工核对清单

- [ ] 1(a)(i) MP3: Constructor header (and end where appropriate) with 3 (min) parameters within class declaration …

- [ ] 1(a)(i) MP1: Class EventItem header (and end where appropriate)
- [ ] 1(a)(ii) MP1: 1 get method with no parameter …
- [ ] 1(c) MP1: Class Character declared (and end where appropriate)
- [ ] 1(d) MP1: Method header CalculateScore (and end where appropriate) taking (min) 2 parameters
- [ ] 1(e)(ii) MP5: …outputting message if it's a draw.
- [ ] 类型与大小的英文注释、函数头及参数、类与方法的归属、QP 要求时的私有属性声明符合本题 MS。混合得分点中能测行为的计自动，头部和类型仍须人工复核。
- [ ] 主程序的调用、返回值使用与分支逐项符合 QP；截图清晰并包含题目要求的输入与输出；提示语语义合适。
- [ ] 指定算法的实现没有用内置函数代劳；文件打开 / 关闭位置及异常范围按 MS 检查。

## MS 得分点编号

测试与上表使用语料 `markpoints[].n`。1 分行按全行计；未印 MP 数字的圆点按原页顺序对应。可选点多于行分值时，自动 / 人工分值按点的权重比例折算；结构整体点仅作人工。
