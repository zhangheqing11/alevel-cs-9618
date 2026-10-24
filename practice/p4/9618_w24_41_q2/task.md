# 9618_w24_41 第 2 题 · Horse 与 Fence：校验、成功率与最高平均值

## 导读与 Python 接口

从空白程序完成整道题。标识符与文件名照抄 QP；数组须建立真实 list 并以英文注释类型与大小；QP 要求私有的属性使用双下划线。主程序写在 `if __name__ == "__main__":` 下，提示语放在 `input()` 中。指定的算法自行实现，不用内置 sort / index / max 等代劳（D10）。

同季 _43 与 _41 整卷相同。构造参数顺序及方法名照 MS Python；`Horses` 和 `Course` 在主程序入口内声明。无数据文件。MS p.22 Python `Winner = -1` 在第一匹获胜时错误地取最后一匹，参考解初始化 0，增加 Beauty 获胜用例。QP 只要求 appropriate messages，截图测试只比较名字及数值（容许浮点舍入），不固定文字。MS p.25 两匹每跳成功率及平均值已核对：Beauty 14.4/72/57.6/50.4，平均48.6；Jet 39/65/52/45.5，平均50.375。

## 英文原题（已对照 QP 原页）

### QP p.6

```text
6

2      A computer program is designed to simulate horses doing show jumping. In show jumping, horses
       jump over obstacles called fences. A horse successfully jumps a fence if it does not knock the
       fence down.

       The program is written using Object-Oriented Programming (OOP).

       The class Horse stores data about the horses.

                                                       Horse

        Name : STRING                             stores the name given to the horse

        MaxFenceHeight : INTEGER                  stores the maximum height in cm that the horse can
                                                  jump, for example 132

        PercentageSuccess : INTEGER               stores the percentage chance of a horse not knocking
                                                  down a fence, for example 70 represents a 70% chance
                                                  of jumping a fence successfully
        Constructor()                             initialises Name, MaxFenceHeight and
                                                  PercentageSuccess to its parameter values

        GetName()                                 returns the name of the horse

        GetMaxFenceHeight()                       returns the maximum height the horse can jump

        Success()                                 calculates and returns the percentage chance of a horse
                                                  successfully jumping a specific fence


       (a) (i)    Write program code to declare the class Horse and its constructor.

                  Do not declare the other methods.

                  Use your programming language’s appropriate constructor.

                  All attributes must be private. If you are writing in Python, include attribute declarations
                  using comments.

    Save your program as Question2_N24.

    Copy and paste the program code into part 2(a)(i) in the evidence document.
                                                                                                           [4]

           (ii)   The get methods GetName() and GetMaxFenceHeight() each return the relevant
                  attribute.

                  Write program code for the get methods.

    Save your program.

    Copy and paste the program code into part 2(a)(ii) in the evidence document.
                                                                                                           [3]



© UCLES 2024                                      9618/41/O/N/24
```

### QP p.7

```text
7

    (b) The array Horses stores objects of type Horse.

          (i)   The program has two horses:

                •   The horse named ‘Beauty’ can jump a maximum height of 150 cm and has a success
                    percentage rate of 72%.
                •   The horse named ‘Jet’ can jump a maximum height of 160 cm and has a success
                    percentage rate of 65%.

                Write program code to:

                •   declare the array, Horses, local to the main program with space for two Horse
                    objects
                •   store the two horses described in the array
                •   output the name of both Horse objects from the array.

 Save your program.

 Copy and paste the program code into part 2(b)(i) in the evidence document.
                                                                                               [5]

         (ii)   Test your program.

                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 2(b)(ii) in the evidence document.
                                                                                               [1]




© UCLES 2024                                   9618/41/O/N/24                          [Turn over
```

### QP p.8

```text
8

    (c) The class Fence stores data about the fences. Each fence has a height in cm and a risk
        number.

         The risk is a whole number between 1 and 5 inclusive. A risk of 1 means the fence is the
         easiest type to jump. A risk of 5 means the fence is the hardest type to jump.

                                                       Fence

      Height : INTEGER                            stores the height of the fence in cm
                                                  the height is between 70 and 180 inclusive

      Risk : INTEGER                              stores the risk as a whole number between 1 and 5
                                                  inclusive
      Constructor()                               initialises Height and Risk to its parameter values

      GetHeight()                                 returns the height of the fence

      GetRisk()                                   returns the risk of the fence


          (i)   Write program code to declare the class Fence, its constructor and get methods.

                Use your programming language’s appropriate constructor.

                All attributes must be private.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 2(c)(i) in the evidence document.
                                                                                                        [4]

         (ii)   The array Course stores four Fence objects. The user inputs the height and risk for
                each fence, and these are validated before each fence is created.

                Amend the main program to:

                •   declare the local array Course
                •   take as input the data for four fences from the user
                •   loop the input until both the height and risk are valid for each fence
                •   create an instance of Fence for each of the four valid fences and store each
                    instance in the array.

 Save your program.

 Copy and paste the program code into part 2(c)(ii) in the evidence document.
                                                                                                        [5]




© UCLES 2024                                      9618/41/O/N/24
```

### QP p.9

```text
9

    (d) The chance of a horse jumping a fence without knocking it down is calculated as follows.

         If the height of the fence is more than the maximum height a horse can jump, the success
         percentage is 20% of the horse’s PercentageSuccess. The risk does not affect this value.

         If the height of the fence is less than or equal to the maximum height a horse can jump, the
         risk gives a modifier value to multiply with the horse’s PercentageSuccess.

         The risk values and their modifiers are given in this table:

                    Risk                     Modifier

                      5                         0.6

                      4                         0.7

                      3                         0.8

                      2                         0.9

                      1                         1.0


         For example:

         •     The horse Jet has PercentageSuccess of 65 and MaxFenceHeight of 160.
         •     A fence has a height of 140 and a risk of 3.
         •     The height of the fence is less than the horse’s MaxFenceHeight, therefore the risk is
               used.
         •     The risk of 3 gives the modifier 0.8.
         •     The modifier 0.8 is multiplied by the horse’s PercentageSuccess of 65, which gives 52.
         •     The chance of the horse successfully jumping this fence is 52%.

         The method Success() in the Horse class:

         •     takes the height and risk of a fence as parameters
         •     calculates the percentage chance of success for that horse jumping the fence without
               knocking it down
         •     returns the calculated percentage chance of success as a real number.

         Write program code for Success().

 Save your program.

 Copy and paste the program code into part 2(d) in the evidence document.
                                                                                                   [5]




© UCLES 2024                                  9618/41/O/N/24                              [Turn over
```

### QP p.10

```text
10

    (e) (i)     Write program code to amend the main program to:

         •      calculate and output the chance of the first horse jumping each of the four fences without
                knocking each fence down
         •      calculate and output the chance of the second horse jumping each of the four fences
                without knocking each fence down.

                All outputs must have appropriate messages including the name of the horse and the
                fence number.

                An example output for one horse jumping two fences is:

                "The horse Fox at fence 1 has a 68% chance of success
                The horse Fox at fence 2 has a 72% chance of success"

 Save your program.

 Copy and paste the program code into part 2(e)(i) in the evidence document.
                                                                                                       [3]

         (ii)   Write program code to amend the main program to:

                •   calculate and output the average chance of success for each horse jumping over all
                    four fences without knocking each fence down (the average is the total of values
                    divided by the quantity of values). An example output for one horse jumping all of
                    the fences is:

                "The horse Fox has an average 70% chance of jumping over all four
                fences"

                •   output the name of the horse that has the highest average chance of success.

                You can assume that each average will be different.

                All outputs must have appropriate messages.

 Save your program.

 Copy and paste the program code into part 2(e)(ii) in the evidence document.
                                                                                                       [2]




© UCLES 2024                                   9618/41/O/N/24
```

### QP p.11

```text
11

        (iii)   Test your program with the following input data for four fences:

                         Height                      Risk
                           152                           5
                           121                           1
                           130                           3
                           145                           4


                Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 2(e)(iii) in the evidence document.
                                                                                          [2]




© UCLES 2024                                   9618/41/O/N/24                      [Turn over
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a)(i) | 9618_w24_41:2(a)(i) | 4 | 代码 | `test_2ai_aii_horse` · MP2、MP3、MP4 | MP1 |
| Part 2(a)(ii) | 9618_w24_41:2(a)(ii) | 3 | 代码 | `test_2ai_aii_horse` · MP2、MP3 | MP1 |
| Part 2(b)(i) | 9618_w24_41:2(b)(i) | 5 | 代码 | `test_2bi_cii_main_arrays`、`test_2bii_screenshot_names` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 2(b)(ii) | 9618_w24_41:2(b)(ii) | 1 | 截图 | `test_2bii_screenshot_names` · 全行 | — |
| Part 2(c)(i) | 9618_w24_41:2(c)(i) | 4 | 代码 | `test_2ci_fence` · MP2、MP3、MP4 | MP1 |
| Part 2(c)(ii) | 9618_w24_41:2(c)(ii) | 5 | 代码 | `test_2bi_cii_main_arrays`、`test_2cii_validation_boundaries` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 2(d) | 9618_w24_41:2(d) | 5 | 代码 | `test_2d_success` · MP1、MP2、MP3、MP4、MP5 | — |
| Part 2(e)(i) | 9618_w24_41:2(e)(i) | 3 | 代码 | `test_2eiii_screenshot_all_chances` · MP1、MP2、MP3 | — |
| Part 2(e)(ii) | 9618_w24_41:2(e)(ii) | 2 | 代码 | `test_2eiii_screenshot_all_chances`、`test_2eii_first_horse_can_win` · MP1、MP2 | — |
| Part 2(e)(iii) | 9618_w24_41:2(e)(iii) | 2 | 截图 | `test_2eiii_screenshot_all_chances` · MP1、MP2 | — |

## 人工核对清单

- [ ] 2(a)(i) MP1: Class Horse declaration (and end where appropriate)
- [ ] 2(a)(ii) MP1: 1 get method header with no parameter …
- [ ] 2(c)(i) MP1: Class Fence header (and end where appropriate) with no inheritance
- [ ] 类型与大小的英文注释、函数头及参数、类与方法的归属、私有属性声明符合本题 MS。混合得分点中能测行为的计自动，头部和类型仍须人工复核。
- [ ] 主程序的调用、返回值使用与分支逐项符合 QP；截图清晰并包含题目要求的输入与输出；提示语语义合适。
- [ ] 指定算法的实现没有用内置函数代劳；文件打开 / 关闭位置及异常范围按 MS 检查。

## MS 得分点编号

测试与上表使用语料 `markpoints[].n`。1 分行按全行计；未印 MP 数字的圆点按原页顺序对应。可选点多于行分值时，自动 / 人工分值按点的权重比例折算；结构整体点仅作人工。
