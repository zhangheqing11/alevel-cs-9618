# 9618_w25_42 第 1 题 · Bird：飞行距离、坐标与输入校验

## 导读与 Python 接口

从空白程序完成整道题。标识符与文件名照抄 QP；数组须建立真实 list 并以英文注释类型与大小；QP 要求私有的属性使用双下划线。主程序写在 `if __name__ == "__main__":` 下，提示语放在 `input()` 中。指定的算法自行实现，不用内置 sort / index / max 等代劳（D10）。

构造参数按 MS Python `Bird(pDistancePerHour, pSpecies)`。主程序的输入编码 QP 未指定：本练习沿用 MS 的鸟选择 1/2，输入顺序为选择 → 分钟 → 方向 N/S/E/W（MS pp.15–17），已作为测试接口约定。QP 列方向与时间输入要求，没有给定这两者的测试输入顺序；若学生采用别的界面，先按此接口调整。Move 本身无需验证参数。MS p.17 的四次结果分别 (500,571)、(500,472)、(464.5,500)、(556,500)；不固定输出措辞，只 GetPosition 按 QP 明确格式。无数据文件，TreeData.txt 属第3题。

## 英文原题（已对照 QP 原页）

### QP p.2

```text
2

You have been supplied with the following source files:

TreeData.txt

Open the evidence document, evidence.doc

Make sure that your name, centre number and candidate number will appear on every page of this
document. This document must contain your answers to each question.

Save this evidence document in your work area as:
evidence_ followed by your centre number_candidate number, for example: evidence_zz999_9999

A class declaration can be used to declare a record. If the programming language used does not
support arrays, a list can be used instead.

One source file is used to answer Question 3. The file is called TreeData.txt

1   A program stores data about birds using Object-Oriented Programming (OOP).

    The class Bird stores the data about the birds:

                                                   Bird
      DistancePerHour : Real             stores the number of kilometres per hour (km/h) the bird
                                         can fly (between 0.0 and 100.0 inclusive)

      Species : String                   stores the species of the bird, for example Pigeon

      XPosition : Real                   stores the current horizontal position of the bird

      YPosition : Real                   stores the current vertical position of the bird
      Constructor()                      initialises Species and DistancePerHour to the
                                         parameter values; initialises XPosition and YPosition
                                         to 500.0

      GetPosition()                      returns a string message that contains the horizontal and
                                         vertical position of the bird

      GetSpecies()                       returns the species of the bird

      Move()                             takes a direction and number of minutes flying (between
                                         0 and 500 inclusive) as parameters and updates the
                                         appropriate horizontal or vertical position




© UCLES 2025                                 9618/42/O/N/25
```

### QP p.3

```text
3

    (a) (i)     Write program code to declare the class Bird and its constructor.

                Do not declare the other methods.

                All attributes should be private.

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program as Question1_N25.

 Copy and paste the program code into part 1(a)(i) in the evidence document.
                                                                                                      [4]

         (ii)   The method GetSpecies() returns the species of the bird.

                Write program code for GetSpecies()

 Save your program.

 Copy and paste the program code into part 1(a)(ii) in the evidence document.
                                                                                                      [2]

        (iii)   The method GetPosition() returns a string of the bird’s data in the format:

                "X = " & <XPosition> & " Y = " & <YPosition>

                An example string for a bird is:

                X = 500.0 Y = 250.0

                Write program code for GetPosition()

 Save your program.

 Copy and paste the program code into part 1(a)(iii) in the evidence document.
                                                                                                      [3]




© UCLES 2025                                        9618/42/O/N/25                             [Turn over
```

### QP p.4

```text
4

        (iv)   If the bird is travelling north, the vertical position increases. If the bird is travelling south,
               the vertical position decreases.

               If the bird is travelling east, the horizontal position increases. If the bird is travelling west,
               the horizontal position decreases.

               The method Move():

               •    takes the direction of travel as a parameter in the form ‘N’ for north, ‘S’ for south,
                    ‘E’ for east or ‘W’ for west
               •    takes the number of minutes that the bird has been flying (to the nearest minute) as
                    a parameter
               •    calculates the distance travelled by the bird using the formula:
                    distance travelled = (distance per hour / 60) * minutes flying
               •    updates the vertical or horizontal position using the distance calculated.

               You do not need to validate the parameters.

               Write program code for Move()

 Save your program.

 Copy and paste the program code into part 1(a)(iv) in the evidence document.
                                                                                                              [5]

    (b) The main program creates two instances of Bird

         The first bird is the species ‘Cockatiel’ and flies 71.0 km/h.

         The second bird is the species ‘Macaw’ and flies 56.0 km/h.

         Write program code to declare and initialise the two birds.

 Save your program.

 Copy and paste the program code into part 1(b) in the evidence document.
                                                                                                              [3]




© UCLES 2025                                     9618/42/O/N/25
```

### QP p.5

```text
5

    (c) (i)     The main program needs to:

                •   output a message that includes the species and current X position and Y position for
                    each bird
                •   prompt the user to select one of the birds to move and take this as an input
                •   prompt the user to enter the direction the bird has been travelling and take this as
                    an input
                •   prompt the user to enter the time to the nearest minute that the bird has been
                    travelling and take this as an input
                •   call the appropriate method to update the chosen bird’s position
                •   output an update on the bird’s new position.

                Each input needs to repeat until valid data is entered. All outputs must be meaningful.

                Write program code to amend the main program.

 Save your program.

 Copy and paste the program code into part 1(c)(i) in the evidence document.
                                                                                                          [8]

         (ii)   Test your program four times to meet these criteria:

                Test 1: The Cockatiel travels north for 60 minutes.

                Test 2: The Macaw travels south for 30 minutes.

                Test 3: The Cockatiel travels west for 30 minutes.

                Test 4: The Macaw travels east for 60 minutes.

                Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot(s) into part 1(c)(ii) in the evidence document.
                                                                                                          [3]




© UCLES 2025                                   9618/42/O/N/25                                 [Turn over
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 1(a)(i) | 9618_w25_42:1(a)(i) | 4 | 代码 | `test_1ai_aii_constructor_species` · MP2、MP3、MP4 | MP1 |
| Part 1(a)(ii) | 9618_w25_42:1(a)(ii) | 2 | 代码 | `test_1ai_aii_constructor_species` · MP2 | MP1 |
| Part 1(a)(iii) | 9618_w25_42:1(a)(iii) | 3 | 代码 | `test_1aiii_position_return` · MP1、MP2、MP3 | — |
| Part 1(a)(iv) | 9618_w25_42:1(a)(iv) | 5 | 代码 | `test_1aiv_moves` · MP2、MP3、MP4、MP5 | MP1 |
| Part 1(b) | 9618_w25_42:1(b) | 3 | 代码 | `test_1b_main_objects` · MP1、MP2、MP3 | — |
| Part 1(c)(i) | 9618_w25_42:1(c)(i) | 8 | 代码 | `test_1cii_four_screenshots`、`test_1ci_validation` · MP1、MP2、MP3、MP4、MP5、MP6、MP7、MP8 | — |
| Part 1(c)(ii) | 9618_w25_42:1(c)(ii) | 3 | 截图 | `test_1cii_four_screenshots` · MP1、MP2、MP3 | — |

## 人工核对清单

- [ ] 1(a)(i) MP1: Class header (and end)
- [ ] 1(a)(ii) MP1: Get method header (and end) with no parameter ….
- [ ] 1(a)(iv) MP1: Method header (and end) taking direction and minutes flying as parameters
- [ ] 类型与大小的英文注释、函数头及参数、类与方法的归属、私有属性声明符合本题 MS。混合得分点中能测行为的计自动，头部和类型仍须人工复核。
- [ ] 主程序的调用、返回值使用与分支逐项符合 QP；截图清晰并包含题目要求的输入与输出；提示语语义合适。
- [ ] 指定算法的实现没有用内置函数代劳；文件打开 / 关闭位置及异常范围按 MS 检查。

## MS 得分点编号

测试与上表使用语料 `markpoints[].n`。1 分行按全行计；未印 MP 数字的圆点按原页顺序对应。可选点多于行分值时，自动 / 人工分值按点的权重比例折算；结构整体点仅作人工。
