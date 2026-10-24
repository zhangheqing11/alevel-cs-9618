# 9618_w22_42 第 2 题 · Character：文件对象数组、检索与移动

## 导读与 Python 接口

从空白程序完成整道题。标识符与文件名照抄 QP；数组须建立真实 list 并以英文注释类型与大小；私有属性使用双下划线。主程序写在 `if __name__ == "__main__":` 下，提示语放在 `input()` 中。指定的算法自行实现，不用内置 sort / index / max 等代劳（D10）。

类方法按 QP 命名，无需另加读文件函数。主程序数组名称不限，测试在 main 命名空间检查包含 10 个 Character 的 list。MS p.16 Python 只 lower 输入、没有 lower 存储姓名，无法找到 Qui；参考解双方 lower，实现 MS 的大小写点并通过 QP 指定 qui 测试。MS p.19 的 Python 输出 CharacterName 却从未赋输入，参考解输出对象 GetName()。MS p.20 截图为 X = 83、Y = 9；QP p.7 的格式示例 Y = 0 只是示例格式，不是该次输入的结果。缺文件之后如何继续 QP 未定义，测试只核对捕获异常和消息。

## 英文原题（已对照 QP 原页）

### QP p.5

```text
5

2   A computer game is being developed. The game has 10 different characters that are all active in
    the game.

    Part of the game is being written using object-oriented programming.

    The class Character stores data about the characters. Each character has a name and the x
    coordinate and y coordinate of their current position.

                                                 Character
      Name : STRING                    stores the name of the character

      XCoordinate : INTEGER            stores the x coordinate

      YCoordinate : INTEGER            stores the y coordinate
      Constructor()                    initialises Name, XCoordinate and YCoordinate from the
                                       values passed as parameters

      GetName()                        returns the name of the character

      GetX()                           returns the x coordinate of the character

      GetY()                           returns the y coordinate of the character

      ChangePosition()                 takes XChange as an integer parameter and adds it to the
                                       x coordinate
                                       takes YChange as an integer parameter and adds it to the
                                       y coordinate

    (a) Write program code to declare the class Character and its constructor. Do not write
        program code for the other methods.

         Use your programming language appropriate constructor.

         All attributes must be private. If you are writing in Python, include attribute declarations using
         comments.

 Save your program as Question2_N22.

 Copy and paste the program code into part 2(a) in the evidence document.
                                                                                                        [4]

    (b) Write program code for the three get methods for the class Character.

 Save your program.

 Copy and paste the program code into part 2(b) in the evidence document.
                                                                                                        [3]




© UCLES 2022                                  9618/42/O/N/22                                   [Turn over
```

### QP p.6

```text
6

    (c) Write program code for the method ChangePosition().

 Save your program.

 Copy and paste the program code into part 2(c) in the evidence document.
                                                                                                   [2]

    (d) The main program has a 1D array of characters. Each character is stored as an object of type
        Character.

         The game has a maximum of 10 characters. The character names, x coordinates and y
         coordinates are stored in the file Characters.txt in the order:

         •     name
         •     x coordinate
         •     y coordinate.

         For example, the first character in the file is named Amal, with the x coordinate 0 and the y
         coordinate 2.

         Amend the main program by writing program code to:

         •     declare the array
         •     read in all 10 characters from Characters.txt
         •     store each character as an object in the array.

 Save your program.

 Copy and paste the program code into part 2(d) in the evidence document.
                                                                                                   [7]

    (e) The main program needs to read in a character’s name from the user, search for the character
        in the array and store the index of its position. It repeats until the user enters a name that
        exists in the array.

         Amend the main program by writing program code to perform this task.

 Save your program.

 Copy and paste the program code into part 2(e) in the evidence document.
                                                                                                   [5]




© UCLES 2022                                9618/42/O/N/22
```

### QP p.7

```text
7

    (f)   The user will enter a letter to identify the direction the chosen character from part 2(e) should
          move.

          •      If ‘A’ is input, the character moves left (x coordinate minus 1).
          •      If ‘W’ is input, the character moves up (y coordinate plus 1).
          •      If ‘S’ is input, the character moves down (y coordinate minus 1).
          •      If ‘D’ is input, the character moves right (x coordinate plus 1).

          Amend the main program by writing program code to:

          •      take a letter as input until it is a valid move (A, W, S or D)
          •      change the position of the character using the appropriate method.

 Save your program.

 Copy and paste the program code into part 2(f) in the evidence document.
                                                                                                        [7]

    (g) (i)      When a change to a character’s position has been made, the program needs to output
                 the character’s name and the new x and y coordinates of the character, in the format:

                 Qui has changed coordinates to X = 83 and Y = 0

                 Amend the main program by writing program code to perform these tasks.

 Save your program.

 Copy and paste the program code into part 2(g)(i) in the evidence document.
                                                                                                        [2]

          (ii)   Test your program by inputting the following four items of data in the order given:

                     THOMAS
                     qui
                     X
                     A

                 Take a screenshot of the output.

 Copy and paste the screenshot into part 2(g)(ii) in the evidence document.

                                                                                                        [1]




© UCLES 2022                                    9618/42/O/N/22                                 [Turn over
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a) | 9618_w22_42:2(a) | 4 | 代码 | `test_2a_private_initialisation` · MP2、MP4 | MP1、MP3 |
| Part 2(b) | 9618_w22_42:2(b) | 3 | 代码 | `test_2b_getters` · MP2、MP3 | MP1 |
| Part 2(c) | 9618_w22_42:2(c) | 2 | 代码 | `test_2c_change_adds` · MP2 | MP1 |
| Part 2(d) | 9618_w22_42:2(d) | 7 | 代码 | `test_2d_all_file_objects`、`test_2d_missing_file` · MP1、MP2、MP3、MP4、MP5、MP6、MP8、MP9 | MP7 |
| Part 2(e) | 9618_w22_42:2(e) | 5 | 代码 | `test_2e_f_g_moves` · MP1、MP2、MP3、MP4、MP5、MP6 | — |
| Part 2(f) | 9618_w22_42:2(f) | 7 | 代码 | `test_2main_call_chain` / `test_2e_f_g_moves` · MP1、MP2、MP3、MP4、MP5、MP6、MP7 | — |
| Part 2(g)(i) | 9618_w22_42:2(g)(i) | 2 | 代码 | `test_2main_call_chain` / `test_2e_f_g_moves` · MP1、MP2 | — |
| Part 2(g)(ii) | 9618_w22_42:2(g)(ii) | 1 | 截图 | `test_2gii_screenshot` · 全行 | — |

## 人工核对清单

- [ ] 2(a) MP3: Constructor method (and end where appropriate) taking 3 parameters …

- [ ] 2(a) MP1: Class declaration (and end where appropriate) for Character
- [ ] 2(b) MP1: 1 get method header (and end where appropriate) with no parameters…
- [ ] 2(c) MP1: method header (and end where appropriate) taking 2 (integer) parameters
- [ ] 2(d) MP7: closing the text file (in appropriate place)
- [ ] 类型与大小的英文注释、函数头及参数、类与方法的归属、QP 要求时的私有属性声明符合本题 MS。混合得分点中能测行为的计自动，头部和类型仍须人工复核。
- [ ] 主程序的调用、返回值使用与分支逐项符合 QP；截图清晰并包含题目要求的输入与输出；提示语语义合适。
- [ ] 指定算法的实现没有用内置函数代劳；文件打开 / 关闭位置及异常范围按 MS 检查。

## MS 得分点编号

测试与上表使用语料 `markpoints[].n`。1 分行按全行计；未印 MP 数字的圆点按原页顺序对应。可选点多于行分值时，自动 / 人工分值按点的权重比例折算；结构整体点仅作人工。
