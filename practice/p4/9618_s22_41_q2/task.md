# 9618_s22_41 第 2 题 · Balloon：生命值与防御

标识符及文件名照 QP；数组建成真实 list，并用英文注释注明类型与大小（D10）。从空文件完成，主程序放在 `if __name__ == "__main__":` 下，提示写在 `input("…")` 中。按 `make try EX=practice/p4/9618_s22_41_q2 K=2b` 可分问测试。QP 要求私有属性时使用 `self.__Name`；未要求时可按 MS 使用公有属性；测试允许正确的循环实现，不靠指定变量名或固定提示语判分。
同季 _43 与本卷整卷相同，本题不另复制。

来源：QP pp.5–7；MS pp.19–26。已看 QP 全题原页、MS Python 范例原页；证据格与官方 evidence.doc 逐格核对。

## 英文原题（对照 QP 原页转写）

```text
5

2   A computer game is being developed using object-oriented programming.

    One element of the game is a balloon. This is designed as the class Balloon.

    The class has the following attributes and methods.

                                                Balloon
Health : INTEGER                              The health of the balloon

Colour : STRING                               The colour of the balloon

DefenceItem : STRING                          The item the balloon uses to defend itself

Constructor()                                 Initialises the defence item and colour using the
                                              parameters
                                              Initialises health to 100

ChangeHealth()                                Takes the change as a parameter and adds this to the
                                              health

GetDefenceItem()                              Returns the defence item of the object

CheckHealth()                                 If the health is 0 or less, it returns TRUE, otherwise it
                                              returns FALSE


    (a) The constructor takes the name of the defence item and the balloon’s colour as parameters
        and sets these to the attributes. The health is initialised to 100.

         Write program code to declare the class Balloon and its constructor. Do not write any other
         methods.

         Use your language appropriate constructor.

         All attributes should be private. If you are writing in Python include attribute declarations using
         comments.

 Save your program as Question2_J2022.

 Copy and paste the program code into part 2(a) in the evidence document.
                                                                                                          [5]

    (b) The get method GetDefenceItem() returns the defence item of the object.

         Amend your program code to include the get method GetDefenceItem().

 Save your program.

 Copy and paste the program code into part 2(b) in the evidence document.
                                                                                                          [2]






    (c) The object’s method ChangeHealth() takes an integer number as a parameter and adds
        this to the health attribute of the object.

          Amend your program code to include the method ChangeHealth().

 Save your program.

 Copy and paste the program code into part 2(c) in the evidence document.
                                                                                                  [2]

    (d) The object’s method CheckHealth() returns TRUE if the health of the object is 0 or less (no
        health remaining) and returns FALSE otherwise (health remaining).

          Amend your program code to include the method CheckHealth().

 Save your program.

 Copy and paste the program code into part 2(d) in the evidence document.
                                                                                                  [2]

    (e) Amend the main program to:

          •    take as input a defence item and colour from the user
          •    create a new balloon with the identifier Balloon1 using the data input.

 Save your program.

 Copy and paste the program code into part 2(e) in the evidence document.
                                                                                                  [3]

    (f)   The function Defend():

          •    takes a balloon object as a parameter
          •    takes as input the strength of an opponent from the user
          •    uses the ChangeHealth() method to subtract the strength input from the object’s
               health
          •    outputs the defence item of the balloon
          •    checks the health of the object and outputs an appropriate message if it has no health
               remaining, or if it has health remaining
          •    returns the amended balloon object.

          Write program code to declare the function Defend().

 Save your program.

 Copy and paste the program code into part 2(f) in the evidence document.
                                                                                                  [8]






    (g) (i)     Amend the main program to call the function Defend().

 Save your program.

 Copy and paste the program code into part 2(g)(i) in the evidence document.
                                                                                      [2]

         (ii)   Test your program using the following inputs:

                •   balloon defence method "Shield"
                •   balloon colour "Red"
                •   strength of opponent 50

                Take a screenshot to show the output.

 Copy and paste the screenshot into part 2(g)(ii) in the evidence document.
                                                                                      [1]
```

## Python 接口与 QP / MS 差异

接口：`Balloon(DefenceItem, Colour)`、`GetDefenceItem()`、`ChangeHealth(Change)`、`CheckHealth()`、`Defend(MyBalloon)`。MS p.25 原页 Python 把 `ChangeHealth` 印成 `VhangeHealth`，参考解修正为题干方法名。提示语和状态文字不固定；测试只要求输出盾牌名称及状态行，人工核对该状态表示仍有生命值。主程序接收返回对象的赋值与 Balloon1 名称人工补核。2(f) 有 10 个可选点最多 8 分，按比例折算。

## 证据文档对照表

| 证据格 | 行 id | 分 | 内容 | 自动测（测试名 · 语料得分点） | 人工核对 |
|:--|:--|--:|:--|:--|:--|
| Part 2(a) | 9618_s22_41:2(a) | 5 | 代码 | `test_2a_constructor_private_values` · MP2, MP4, MP5 | MP1, MP3 |
| Part 2(b) | 9618_s22_41:2(b) | 2 | 代码 | `test_2b_getter` · MP2 | MP1 |
| Part 2(c) | 9618_s22_41:2(c) | 2 | 代码 | `test_2c_change_health_accumulates` · MP2 | MP1 |
| Part 2(d) | 9618_s22_41:2(d) | 2 | 代码 | `test_2d_health_zero_boundary` · MP1, MP2 | — |
| Part 2(e) | 9618_s22_41:2(e) | 3 | 代码 | `test_2g_ii_screenshot_shield` · MP1, MP2, MP3 | — |
| Part 2(f) | 9618_s22_41:2(f) | 8 | 代码 | `test_2f_defend_calls_methods_and_returns_object` · MP2, MP3, MP4, MP5, MP6, MP7, MP8, MP9, MP10 | MP1 |
| Part 2(g)(i) | 9618_s22_41:2(g)(i) | 2 | 代码 | `test_2g_ii_screenshot_shield` · MP1, MP2 | — |
| Part 2(g)(ii) | 9618_s22_41:2(g)(ii) | 1 | 截图 | `test_2g_ii_screenshot_shield` · 整行 | — |

自动覆盖表示行为得到验证；混合点里的函数头、注释、调用结构仍须补核，不能凭测试自动授予考试分数。可选得分点多于该行满分时，按 markpoints[].marks 加权后按该行满分比例折算。

## 人工核对清单

- [ ] 2(a) MP1：Class Balloon declaration (and end where appropriate)
- [ ] 2(a) MP3：constructor header (and end) with two parameters …
- [ ] 2(b) MP1：get header and close with no parameter …
- [ ] 2(c) MP1：procedure header and close taking 1 parameter …
- [ ] 2(f) MP1：function header (and end where appropriate) and taking balloon object as parameter
- [ ] 所有方法头、主程序的调用顺序、返回值接收与题给标识符符合该题 MS；属性注释写明类型，QP 要求私有的属性不改成公有属性。
- [ ] 题目指定算法自行实现，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳（D10 ③；本项人工核对）。
- [ ] 截图清晰，输入、输出及要求的文件名可见；appropriate message 的语义与状态一致（措辞不限）。

## 得分点编号（D37 ②）

编号采用语料 markpoints[].n；1 分且未拆分的行记“整行”。本题 MS 圆点顺序与语料一致；若 MS 给可选点上限，按该行上限计分。
