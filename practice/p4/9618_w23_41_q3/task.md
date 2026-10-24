# 9618_w23_41 第 3 题 · Character 与 BikeCharacter：继承、边界与重写

## 导读与 Python 接口

从空白程序完成整道题。标识符与文件名照抄 QP；数组须建立真实 list 并以英文注释类型与大小；QP 要求私有的属性使用双下划线。主程序写在 `if __name__ == "__main__":` 下，提示语放在 `input()` 中。指定的算法自行实现，不用内置 sort / index / max 等代劳（D10）。

同季 _43 与 _41 整卷相同。构造参数按 MS Python 顺序 `(XPositionP, YPositionP, NameP)`，QP 未规定参数顺序，作为测试接口统一。本题没有强制 private，不以是否使用双下划线判分。MS p.37 Python 将移动分支缩进在方向校验循环中，导致有效方向不移动；参考解将分支放到循环后，按 QP 得到 jack right → (60, 50)、karla down → (100, 30)。无数据文件；函数头、属性类型、Move 是否使用 setter 人工补核。

## 英文原题（已对照 QP 原页）

### QP p.8

```text
8

3   A computer game is written using object-oriented programming.

    The game has multiple characters that can move around the screen.

    The class Character stores data about the characters. Each character has a name, a current X
    (horizontal) position and a current Y (vertical) position.

                                              Character
    Name : STRING                      stores the name of the character as a string

    XPosition : INTEGER                stores the X position as an integer

    YPosition : INTEGER                stores the Y position as an integer

    Constructor()                      initialises Name, XPosition and YPosition to its
                                       parameter values

    GetXPosition()                     returns the X position

    GetYPosition()                     returns the Y position

    SetXPosition()                     adds the parameter to the X position
                                       validates that the new X position is between 0 and 10 000
                                       inclusive

    SetYPosition()                     adds the parameter to the Y position
                                       validates that the new Y position is between 0 and 10 000
                                       inclusive

    Move()                             takes a direction as a parameter and calls either
                                       SetXPosition or SetYPosition with an integer value


    (a) (i)    Write program code to declare the class Character and its constructor.

               Do not declare the other methods.

               Use your programming language’s appropriate constructor.

               If you are writing in Python, include attribute declarations using comments.

 Save your program as Question3_N23.

 Copy and paste the program code into part 3(a)(i) in the evidence document.
                                                                                                   [4]




© UCLES 2023                                  9618/41/O/N/23
```

### QP p.9

```text
9

         (ii)   The get methods GetXPosition() and GetYPosition() each return the relevant
                attribute.

                Write program code for the get methods.

 Save your program.

 Copy and paste the program code into part 3(a)(ii) in the evidence document.
                                                                                                      [3]

        (iii)   The set methods SetXPosition() and SetYPosition() each take a value as a
                parameter and add this to the current X or Y position.

                If the new value exceeds 10 000, it is limited to 10 000.

                If the new value is below 0, it is limited to 0.

                Write program code for the set methods.

 Save your program.

 Copy and paste the program code into part 3(a)(iii) in the evidence document.
                                                                                                      [4]

        (iv)    The method Move() takes a string parameter: "up", "down", "left" or "right".

                The table shows the change each direction will make to the X or Y position.

                Use the appropriate method to change the position value.

                       Direction        Value change
                up                   Y position + 10
                down                 Y position − 10
                left                 X position − 10
                right                X position + 10

                Write program code for Move().

 Save your program.

 Copy and paste the program code into part 3(a)(iv) in the evidence document.
                                                                                                      [4]

    (b) Write program code to declare a new instance of Character with the identifier Jack.

         The starting X position is 50 and the starting Y position is 50, the character’s name is Jack.

 Save your program.

 Copy and paste the program code into part 3(b) in the evidence document.
                                                                                                      [2]
© UCLES 2023                                      9618/41/O/N/23                              [Turn over
```

### QP p.10

```text
10

    (c) The class BikeCharacter inherits from the class Character.

                                            BikeCharacter

    Constructor()                       takes Name, XPosition and YPosition as parameters
                                        calls its parent class constructor with the appropriate values

    Move()                              overrides the method Move() from the parent class by
                                        changing either the X position or the Y position by 20
                                        instead of 10

          (i)   Write program code to declare the class BikeCharacter and its constructor.

                Do not declare the other method.

                Use your programming language’s appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 3(c)(i) in the evidence document.
                                                                                                         [3]

         (ii)   The method Move() overrides the method from the parent class.

                The table shows the change each direction will make to the X or Y position.

                       Direction    Value change

                up                 Y position + 20
                down               Y position − 20
                left               X position − 20
                right              X position + 20

                Write program code for Move().

 Save your program.

 Copy and paste the program code into part 3(c)(ii) in the evidence document.
                                                                                                         [2]

    (d) Write program code to declare a new instance of BikeCharacter with the identifier Karla.

         The starting X position is 100, the starting Y position is 50 and the character’s name is Karla.

 Save your program.

 Copy and paste the program code into part 3(d) in the evidence document.
                                                                                                         [1]


© UCLES 2023                                   9618/41/O/N/23
```

### QP p.11

```text
11

    (e) (i)     Write program code to:

                •   take as input which of the two characters the user would like to move
                •   take as input the direction the user would like the character to move
                •   call the appropriate method to move the character
                •   output the character’s new X and Y position in an appropriate format, for example:
                          "Karla's new position is X = 100 Y = 200"

                All inputs require appropriate prompts and must be validated.

 Save your program.

 Copy and paste the program code into part 3(e)(i) in the evidence document.
                                                                                                    [5]

         (ii)   Test your program twice with the following inputs.

                Test 1: jack    right

                Test 2: karla   down

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 3(e)(ii) in the evidence document.
                                                                                                    [2]




© UCLES 2023                                   9618/41/O/N/23
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 3(a)(i) | 9618_w23_41:3(a)(i) | 4 | 代码 | `test_3ai_aii_construct_getters` · MP4 | MP1、MP2、MP3 |
| Part 3(a)(ii) | 9618_w23_41:3(a)(ii) | 3 | 代码 | `test_3ai_aii_construct_getters` · MP2、MP3 | MP1 |
| Part 3(a)(iii) | 9618_w23_41:3(a)(iii) | 4 | 代码 | `test_3aiii_clamps_and_accumulates` · MP2、MP3、MP4 | MP1 |
| Part 3(a)(iv) | 9618_w23_41:3(a)(iv) | 4 | 代码 | `test_3aiv_cii_move` · MP2、MP3、MP4 | MP1 |
| Part 3(b) | 9618_w23_41:3(b) | 2 | 代码 | `test_3b_d_main_instances` · MP1、MP2 | — |
| Part 3(c)(i) | 9618_w23_41:3(c)(i) | 3 | 代码 | `test_3ci_inherits_parent` · MP1、MP3 | MP2 |
| Part 3(c)(ii) | 9618_w23_41:3(c)(ii) | 2 | 代码 | `test_3aiv_cii_move` · MP1、MP2 | — |
| Part 3(d) | 9618_w23_41:3(d) | 1 | 代码 | `test_3b_d_main_instances` · 全行 | — |
| Part 3(e)(i) | 9618_w23_41:3(e)(i) | 5 | 代码 | `test_3ei_rejects_invalid_inputs`、`test_3eii_screenshots` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 3(e)(ii) | 9618_w23_41:3(e)(ii) | 2 | 截图 | `test_3eii_screenshots` · MP1 | — |

## 人工核对清单

- [ ] 3(c)(i) MP2: Constructor taking all 3 parameters …

- [ ] 3(a)(i) MP3: Constructor header (and end where appropriate) with 3 parameters

- [ ] 3(a)(i) MP1: Class header (and end where appropriate)
- [ ] 3(a)(i) MP2: Three attributes with correct names and data types
- [ ] 3(a)(ii) MP1: 1 get header with no parameter …
- [ ] 3(a)(iii) MP1: 1 set method header (and end where appropriate) with parameter …
- [ ] 3(a)(iv) MP1: Method header with (string) parameter
- [ ] 类型与大小的英文注释、函数头及参数、类与方法的归属、QP 要求时的私有属性声明符合本题 MS。混合得分点中能测行为的计自动，头部和类型仍须人工复核。
- [ ] 主程序的调用、返回值使用与分支逐项符合 QP；截图清晰并包含题目要求的输入与输出；提示语语义合适。
- [ ] 指定算法的实现没有用内置函数代劳；文件打开 / 关闭位置及异常范围按 MS 检查。

## MS 得分点编号

测试与上表使用语料 `markpoints[].n`。1 分行按全行计；未印 MP 数字的圆点按原页顺序对应。可选点多于行分值时，自动 / 人工分值按点的权重比例折算；结构整体点仅作人工。
