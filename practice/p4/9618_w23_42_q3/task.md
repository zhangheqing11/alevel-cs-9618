# 9618_w23_42 第 3 题 · Character 与 MagicCharacter：年龄与学习加成

## 导读与 Python 接口

从空白程序完成整道题。标识符与文件名照抄 QP；数组须建立真实 list 并以英文注释类型与大小；QP 要求私有的属性使用双下划线。主程序写在 `if __name__ == "__main__":` 下，提示语放在 `input()` 中。指定的算法自行实现，不用内置 sort / index / max 等代劳（D10）。

构造函数接口按 MS Python：`Character(CName, DBirth, Intell, SpeedP)` 与 `MagicCharacter(ElementP, CName, DBirth, Intell, SpeedP)`；日期使用标准库 `datetime.datetime`（亦可接收 `date`）。年龄固定按 2023 减出生年份，不能用机器当前年；不比较月日。本题未要求 private，公有或私有实现均可，类型注释人工核对。无数据文件；本题 Python 范例行为无需修正。截图按 MS p.29 Royal / 4 / 77 与 p.34 Light / 5 / 90 测数值，允许浮点表示与不同提示措辞。

## 英文原题（已对照 QP 原页）

### QP p.10

```text
10

3   A computer game is written using object-oriented programming.

    The game has multiple characters.

    The class Character stores data about the game characters. Each character has a name, date
    of birth, intelligence value and speed value.

                                                 Character
      CharacterName : STRING              stores the name of the character

      DateOfBirth : DATE                  stores the date of birth of the character

      Intelligence : REAL                 stores the intelligence value of the character

      Speed : INTEGER                     stores the speed value of the character
      Constructor()                       initialises CharacterName, DateOfBirth,
                                          Intelligence and Speed to the parameter values

      SetIntelligence()                   assigns the value of the parameter to Intelligence

      GetIntelligence()                   returns the value of Intelligence

      GetName()                           returns the name of the character

      ReturnAge()                         calculates and returns the age of the character as an integer

      Learn()                             increases the value of Intelligence by 10%


    (a) (i)     Write program code to declare the class Character and its constructor.

                Do not declare the other methods.

                Use your programming language’s appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program as Question3_N23.

 Copy and paste the program code into part 3(a)(i) in the evidence document.
                                                                                                      [5]

         (ii)   The get methods GetIntelligence() and GetName() return the attribute values.

                Write program code for the methods GetIntelligence() and GetName().

 Save your program.

 Copy and paste the program code into part 3(a)(ii) in the evidence document.
                                                                                                      [3]




© UCLES 2023                                   9618/42/O/N/23
```

### QP p.11

```text
11

        (iii)   The method SetIntelligence() assigns the value of its parameter to the attribute.

                Write program code for SetIntelligence().

 Save your program.

 Copy and paste the program code into part 3(a)(iii) in the evidence document.
                                                                                                      [2]

        (iv)    The method Learn() increases the current value of Intelligence by 10%.

                Write program code for Learn().

 Save your program.

 Copy and paste the program code into part 3(a)(iv) in the evidence document.
                                                                                                      [1]

         (v)    The method ReturnAge() calculates and returns the age of the character in years as
                an integer.

                Assume that the current year is 2023 and only use the year from the date of birth for the
                calculation. For example, the method returns 18 if the character was born on any date in
                2005.

                Write program code for the method ReturnAge().

 Save your program.

 Copy and paste the program code into part 3(a)(v) in the evidence document.
                                                                                                      [2]

    (b) (i)     Write program code to create a new instance of Character with the identifier
                FirstCharacter.

                The name of the character is Royal, date of birth is 1 January 2019, intelligence is 70
                and speed is 30.

 Save your program.

 Copy and paste the program code into part 3(b)(i) in the evidence document.
                                                                                                      [2]

         (ii)   Write program code to call the method Learn() for the character created in part 3(b)(i).

                Output the name, age and intelligence of the character in an appropriate message.

 Save your program.

 Copy and paste the program code into part 3(b)(ii) in the evidence document.
                                                                                                      [3]

© UCLES 2023                                   9618/42/O/N/23                                [Turn over
```

### QP p.12

```text
12

        (iii)   Test your program.

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 3(b)(iii) in the evidence document.
                                                                                                        [1]

    (c) The class MagicCharacter inherits from the class Character. A magic character has an
        element, for example, water. This element changes how they learn. The magic character’s
        element is stored in the additional attribute Element.

                                                MagicCharacter
           Element : STRING            stores the element for the character
           Constructor()               takes Element, CharacterName, DateOfBirth,
                                       Intelligence and Speed as parameters
                                       calls its parent class constructor with the appropriate values
                                       initialises Element to its parameter value

           Learn()                     alters the intelligence of the character depending on the
                                       character’s element


          (i)   Write program code to declare the class MagicCharacter and its constructor.

                Do not declare the other method.

                Use your programming language’s appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 3(c)(i) in the evidence document.
                                                                                                        [5]

         (ii)   The method Learn() overrides the parent class method and increases the intelligence
                depending on the character’s element.

                •   If the element is fire or water, intelligence increases by 20%.
                •   If the element is earth, intelligence increases by 30%.
                •   If the element is not fire, water or earth the intelligence increases by 10%.

                Write program code for Learn().

 Save your program.

 Copy and paste the program code into part 3(c)(ii) in the evidence document.
                                                                                                        [3]



© UCLES 2023                                   9618/42/O/N/23
```

### QP p.13

```text
13

    (d) (i)     Write program code to create a new instance of MagicCharacter with the identifier
                FirstMagic.

                The name of the character is Light, date of birth is 3 March 2018, intelligence is 75,
                speed is 22 and element is fire.

 Save your program.

 Copy and paste the program code into part 3(d)(i) in the evidence document.
                                                                                                     [2]

         (ii)   Write program code to call the method Learn() for the character created in part 3(d)(i).

                Output the name, age and intelligence of the character in an appropriate message.

 Save your program.

 Copy and paste the program code into part 3(d)(ii) in the evidence document.
                                                                                                     [1]

        (iii)   Test your program.

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 3(d)(iii) in the evidence document.
                                                                                                     [1]




© UCLES 2023                                   9618/42/O/N/23
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a)(i) | 9618_w23_42:3(a)(i) | 5 | 代码 | `test_3ai_aii_constructor_and_getters` · MP5 | MP1、MP2、MP3、MP4 |
| Part 3(a)(ii) | 9618_w23_42:3(a)(ii) | 3 | 代码 | `test_3ai_aii_constructor_and_getters` · MP2、MP3 | MP1 |
| Part 3(a)(iii) | 9618_w23_42:3(a)(iii) | 2 | 代码 | `test_3aiii_setter` · MP2 | MP1 |
| Part 3(a)(iv) | 9618_w23_42:3(a)(iv) | 1 | 代码 | `test_3aiv_learn` · 全行 | — |
| Part 3(a)(v) | 9618_w23_42:3(a)(v) | 2 | 代码 | `test_3av_age_uses_2023_and_year_only` · MP1、MP2 | — |
| Part 3(b)(i) | 9618_w23_42:3(b)(i) | 2 | 代码 | `test_3bi_di_named_instances` · MP1、MP2 | — |
| Part 3(b)(ii) | 9618_w23_42:3(b)(ii) | 3 | 代码 | `test_3main_call_chain` / `test_3biii_royal_screenshot` · MP1、MP2、MP3 | — |
| Part 3(b)(iii) | 9618_w23_42:3(b)(iii) | 1 | 截图 | `test_3biii_royal_screenshot` · 全行 | — |
| Part 3(c)(i) | 9618_w23_42:3(c)(i) | 5 | 代码 | `test_3ci_parent_constructor` · MP1、MP4、MP5 | MP2、MP3 |
| Part 3(c)(ii) | 9618_w23_42:3(c)(ii) | 3 | 代码 | `test_3cii_magic_learning` · MP1、MP2、MP3 | — |
| Part 3(d)(i) | 9618_w23_42:3(d)(i) | 2 | 代码 | `test_3bi_di_named_instances` · MP1、MP2 | — |
| Part 3(d)(ii) | 9618_w23_42:3(d)(ii) | 1 | 代码 | `test_3main_call_chain` / `test_3diii_magic_screenshot` · 全行 | — |
| Part 3(d)(iii) | 9618_w23_42:3(d)(iii) | 1 | 截图 | `test_3diii_magic_screenshot` · 全行 | — |

## 人工核对清单

- [ ] 3(c)(i) MP3: Constructor header taking 5 parameters …

- [ ] 3(a)(i) MP4: … taking 4 parameters

- [ ] 3(a)(i) MP1: Class declaration
- [ ] 3(a)(i) MP2: Four attributes with correct data types
- [ ] 3(a)(i) MP3: Constructor header
- [ ] 3(a)(ii) MP1: 1 get header with no parameter …
- [ ] 3(a)(iii) MP1: Set header with 1 parameter …
- [ ] 3(c)(i) MP2: Declaring Element as string
- [ ] 类型与大小的英文注释、函数头及参数、类与方法的归属、QP 要求时的私有属性声明符合本题 MS。混合得分点中能测行为的计自动，头部和类型仍须人工复核。
- [ ] 主程序的调用、返回值使用与分支逐项符合 QP；截图清晰并包含题目要求的输入与输出；提示语语义合适。
- [ ] 指定算法的实现没有用内置函数代劳；文件打开 / 关闭位置及异常范围按 MS 检查。

## MS 得分点编号

测试与上表使用语料 `markpoints[].n`。1 分行按全行计；未印 MP 数字的圆点按原页顺序对应。可选点多于行分值时，自动 / 人工分值按点的权重比例折算；结构整体点仅作人工。
