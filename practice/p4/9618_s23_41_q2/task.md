# 9618_s23_41 第 2 题 · Vehicle / Helicopter：继承与速度上限

标识符及文件名照 QP；数组建成真实 list，并用英文注释注明类型与大小（D10）。从空文件完成，主程序放在 `if __name__ == "__main__":` 下，提示写在 `input("…")` 中。按 `make try EX=practice/p4/9618_s23_41_q2 K=2b` 可分问测试。QP 要求私有属性时使用 `self.__Name`；未要求时可按 MS 使用公有属性；测试允许正确的循环实现，不靠指定变量名或固定提示语判分。
同季 _43 与本卷整卷相同，本题不另复制。

来源：QP pp.4–7；MS pp.12–25。已看 QP 全题原页、MS Python 范例原页；证据格与官方 evidence.doc 逐格核对。

## 英文原题（对照 QP 原页转写）

```text
4

2   A computer game is being designed that will include different vehicles. A prototype for the game is
    being developed using object‑oriented programming.

    The class Vehicle stores data about the vehicles. Each vehicle has an identification name,
    a maximum speed, a current speed and a horizontal position. The value IncreaseAmount is
    added to the current speed each time the vehicle increases its speed.

                                               Vehicle
 ID : STRING                                stores the identification name for the vehicle

 MaxSpeed : INTEGER                         stores the maximum speed

 CurrentSpeed : INTEGER                     stores the current speed

 IncreaseAmount : INTEGER                   stores the amount CurrentSpeed increases by

 HorizontalPosition : INTEGER               stores the horizontal position
 Constructor()                              initialises ID, MaxSpeed and IncreaseAmount to the
                                            parameter values
                                            initialises both CurrentSpeed and
                                            HorizontalPosition to 0

 GetCurrentSpeed()                          returns the current speed

 GetIncreaseAmount()                        returns the increase amount

 GetHorizontalPosition()                    returns the horizontal position

 GetMaxSpeed()                              returns the maximum speed

 SetCurrentSpeed()                          assigns the parameter to the current speed

 SetHorizontalPosition()                    assigns the parameter to the horizontal position

 IncreaseSpeed()                            calculates and stores the new speed and horizontal
                                            position of the vehicle


    (a) (i)    Write program code to declare the class Vehicle. All attributes must be private.

               You only need to declare the class and its constructor. Do not declare any other methods.

               Use your programming language’s appropriate constructor.

               If you are writing program code in Python, include attribute declarations using comments.

 Save your program as Question2_J2023.

 Copy and paste the program code into part 2(a)(i) in the evidence document.
                                                                                                     [5]






         (ii)   Write  program  code    for  the  get   methods   GetCurrentSpeed(),
                GetIncreaseAmount(), GetMaxSpeed() and GetHorizontalPosition()

 Save your program.

 Copy and paste the program code into part 2(a)(ii) in the evidence document.
                                                                                              [3]

        (iii)   Write program code for           the    set    methods   SetCurrentSpeed()   and
                SetHorizontalPosition()

 Save your program.

 Copy and paste the program code into part 2(a)(iii) in the evidence document.
                                                                                              [3]

        (iv)    The method IncreaseSpeed():

                •   adds IncreaseAmount to the current speed
                •   adds the updated current speed to the horizontal position.

                The current speed of a vehicle cannot exceed its maximum speed.

                Write program code for the method IncreaseSpeed()

 Save your program.

 Copy and paste the program code into part 2(a)(iv) in the evidence document.
                                                                                              [3]






    (b) The child class Helicopter inherits from the parent class Vehicle. A helicopter also has a
        vertical position and changes the vertical position when it increases speed.

                                                  Helicopter
 VerticalPosition : INTEGER                       stores the vertical position

 VerticalChange : INTEGER                         stores the amount VerticalPosition changes by

 MaxHeight : INTEGER                              stores the maximum height the helicopter can reach
 Constructor()                                    takes the ID, maximum speed, increase amount, vertical
                                                  change and maximum height as parameters
                                                  initialises the vertical position to 0

 GetVerticalPosition()                            returns the vertical position

 IncreaseSpeed()                                  changes the current speed, horizontal and vertical
                                                  position of the helicopter


          (i)   Write program code to declare the class Helicopter. You only need to declare the
                class and its constructor. You do not need to declare the other methods.

                Use your programming language’s appropriate constructor.

                All attributes must be private.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 2(b)(i) in the evidence document.
                                                                                                       [5]

         (ii)   The Helicopter method IncreaseSpeed() overrides the method from the parent
                class and:

                •   adds the amount of vertical change to the vertical position
                •   adds IncreaseAmount to the current speed
                •   adds the updated current speed to the horizontal position.

                The vertical position of a helicopter cannot exceed its maximum height.

                The current speed of a helicopter cannot exceed its maximum speed.

                Write program code for the method IncreaseSpeed()

 Save your program.

 Copy and paste the program code into part 2(b)(ii) in the evidence document.
                                                                                                       [4]






    (c) A procedure needs to output the horizontal position and speed of a vehicle. If the vehicle is a
        helicopter, it also outputs the vertical position.

         All outputs must include appropriate messages.

         Write program code for this procedure.

 Save your program.

 Copy and paste the program code into part 2(c) in the evidence document.
                                                                                                    [3]

    (d) The main program needs to:

         •      instantiate a car as a new vehicle with the ID "Tiger", a maximum speed of 100 and an
                increase amount of 20
         •      instantiate a new helicopter with the ID "Lion", a maximum speed of 350, an increase
                amount of 40, a vertical change of 3 and a maximum height of 100
         •      call IncreaseSpeed() twice for the car and then call the output procedure from
                part 2(c) for the car
         •      call IncreaseSpeed() twice for the helicopter and then call the output procedure from
                part 2(c) for the helicopter.

          (i)   Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 2(d)(i) in the evidence document.
                                                                                                    [5]

         (ii)   Test your program.

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 2(d)(ii) in the evidence document.
                                                                                                    [1]
```

## Python 接口与 QP / MS 差异

接口采用 QP 的 Vehicle / Helicopter 方法名，2(c) 未命名输出过程采用 MS 的对象方法 `OutputCurrentPosition()`（父、子类各一份）。`Helicopter(ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight)`；允许 `super()` 或显式父类调用。MS p.21 高度越界时写 `MaxHeight`，漏了 `self.__`；参考解修正为 `self.__MaxHeight`，并测试越过最大高度。MS 构造方法漏写 HorizontalPosition 的类型，补 INTEGER 注释。QP 类图的 `GetVerticalPosition()` 同时实现；它未有独立计分小问。截图只断言 MS p.25 的 60、40、120、80、6，提示文字人工核对。

## 证据文档对照表

| 证据格 | 行 id | 分 | 内容 | 自动测（测试名 · 语料得分点） | 人工核对 |
|:--|:--|--:|:--|:--|:--|
| Part 2(a)(i) | 9618_s23_41:2(a)(i) | 5 | 代码 | `test_2a_i_constructor_private` · MP2, MP4, MP5 | MP1, MP3 |
| Part 2(a)(ii) | 9618_s23_41:2(a)(ii) | 3 | 代码 | `test_2a_ii_iii_getters_setters` · MP2, MP3 | MP1 |
| Part 2(a)(iii) | 9618_s23_41:2(a)(iii) | 3 | 代码 | `test_2a_ii_iii_getters_setters` · MP2, MP3 | MP1 |
| Part 2(a)(iv) | 9618_s23_41:2(a)(iv) | 3 | 代码 | `test_2a_iv_speed_clamps_position_still_changes` · MP1, MP2, MP3 | — |
| Part 2(b)(i) | 9618_s23_41:2(b)(i) | 5 | 代码 | `test_2b_i_inheritance_private_fields` / `test_2b_i_inheritance_private_fields` · MP1, MP2, MP4, MP5 | MP3 |
| Part 2(b)(ii) | 9618_s23_41:2(b)(ii) | 4 | 代码 | `test_2b_ii_height_and_speed_caps` · MP2, MP3, MP4 | MP1 |
| Part 2(c) | 9618_s23_41:2(c) | 3 | 代码 | `test_2c_outputs_vehicle_and_helicopter` · MP1, MP2, MP3 | — |
| Part 2(d)(i) | 9618_s23_41:2(d)(i) | 5 | 代码 | `test_2di_main_call_chain` / `test_2d_ii_screenshot` · MP1, MP2, MP3, MP4, MP5 | — |
| Part 2(d)(ii) | 9618_s23_41:2(d)(ii) | 1 | 截图 | `test_2d_ii_screenshot` · 整行 | — |

自动覆盖表示行为得到验证；混合点里的函数头、注释、调用结构仍须补核，不能凭测试自动授予考试分数。可选得分点多于该行满分时，按 markpoints[].marks 加权后按该行满分比例折算。

## 人工核对清单

- [ ] 2(a)(i) MP1：Class header (and close where appropriate)
- [ ] 2(a)(i) MP3：Constructor header (and close where appropriate) taking 3 parameters (min)
- [ ] 2(a)(ii) MP1：1 get function header (and end where appropriate) with no parameter …
- [ ] 2(a)(iii) MP1：1 set procedure (and end where appropriate) taking parameter …
- [ ] 2(b)(i) MP3：Constructor (and end where appropriate) with (min) 5 parameters
- [ ] 2(b)(ii) MP1：Method header (overriding where required) with no parameter
- [ ] 所有方法头、主程序的调用顺序、返回值接收与题给标识符符合该题 MS；属性注释写明类型，QP 要求私有的属性不改成公有属性。
- [ ] 题目指定算法自行实现，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳（D10 ③；本项人工核对）。
- [ ] 截图清晰，输入、输出及要求的文件名可见；appropriate message 的语义与状态一致（措辞不限）。

## 得分点编号（D37 ②）

编号采用语料 markpoints[].n；1 分且未拆分的行记“整行”。本题 MS 圆点顺序与语料一致；若 MS 给可选点上限，按该行上限计分。

D46 / MS p.17：IncreaseSpeed 超上限可撤销本次增量或封顶，测试接受两者，位置累加实际更新后的速度。
