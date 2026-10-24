# 9618_s24_41 第 2 题 · Tree selection and growth

标识符及文件名照 QP；数组建成真实 list，并用英文注释注明类型与大小（D10）。从空文件完成，主程序放在 `if __name__ == "__main__":` 下，提示写在 `input("…")` 中。按 `make try EX=practice/p4/9618_s24_41_q2 K=2b` 可分问测试。对象私有属性使用 `self.__Name`；测试允许正确的循环实现，不靠指定变量名或固定提示语判分。
同季 _43 与本卷整卷相同，本题不另复制。

来源：QP pp.6–10；MS pp.14–28。已看 QP 全题原页、MS Python 范例原页；证据格与官方 evidence.doc 逐格核对。

## 英文原题（对照 QP 原页转写）

```text
6

2   A computer program will store data about trees.

    The user can enter their requirements for a tree and a suitable tree will be selected.

    The program is written using object‑oriented programming.

    The class Tree stores data about the trees.

                                                      Tree
 TreeName : STRING                               stores the name of the tree

 HeightGrowth : INTEGER                          stores the number of cm the tree will grow each year

 MaxHeight : INTEGER                             stores the maximum height in cm that the tree will grow

 MaxWidth : INTEGER                              stores the maximum width in cm that the tree will grow

 Evergreen : STRING                              stores whether the tree keeps its leaves as "Yes", or
                                                 loses its leaves as "No"
 Constructor()                                   initialises TreeName, HeightGrowth, MaxHeight,
                                                 MaxWidth and Evergreen to its parameter values

 GetTreeName()                                   returns the name of the tree

 GetGrowth()                                     returns the number of cm the tree will grow each year

 GetMaxHeight()                                  returns the maximum height in cm that the tree will grow

 GetMaxWidth()                                   returns the maximum width in cm that the tree will grow

 GetEvergreen()                                  returns whether the tree keeps its leaves or loses its
                                                 leaves


    (a) (i)    Write program code to declare the class Tree and its constructor.

               Do not declare the other methods.

               Use the appropriate constructor for your programming language.

               All attributes must be private.

               If you are writing in Python, include attribute declarations using comments.

 Save your program as Question2_J24.

 Copy and paste the program code into part 2(a)(i) in the evidence document.
                                                                                                           [4]





                                                        7

         (ii)   The get methods GetTreeName(), GetGrowth(), GetMaxHeight(),
                GetMaxWidth() and GetEvergreen() each return the relevant attribute.

                Write program code for the get methods.

 Save your program.

 Copy and paste the program code into part 2(a)(ii) in the evidence document.
                                                                                                [3]

    (b) The text file Trees.txt stores data about 9 trees.

         The data in the file is stored in the format:

                Tree name,Height growth each year,Maximum height,Maximum width,Evergreen

         For example, the first row of data is:

                Beech,30,400,200,No

         The tree is a Beech. It can grow 30 cm each year. It has a maximum height of 400 cm.
         It has a maximum width of 200 cm. It is not evergreen (it loses its leaves).

         The function ReadData():

         •      creates an array of type Tree
         •      reads the data from the file
         •      raises an exception if the file is not found
         •      creates a new object of type Tree for each tree in the file
         •      appends each object to the array
         •      returns the array.

         Write program code for ReadData().

 Save your program.

 Copy and paste the program code into part 2(b) in the evidence document.
                                                                                                [7]





                                                          8

    (c) The procedure PrintTrees() takes a Tree object as a parameter and outputs the tree’s
        name, height growth each year, maximum height, maximum width and whether it is evergreen.

         The output message changes depending on whether it is evergreen.

         If it is evergreen, it is in the format:

                TreeName has a maximum height MaxHeight a maximum width MaxWidth and grows
                HeightGrowth cm a year. It does not lose its leaves.

         If it is not evergreen, it is in the format:

                TreeName has a maximum height MaxHeight a maximum width MaxWidth and grows
                HeightGrowth cm a year. It loses its leaves each year.

         Write program code for PrintTrees().

 Save your program.

 Copy and paste the program code into part 2(c) in the evidence document.
                                                                                              [4]

    (d) The main program calls ReadData(), stores the return value and calls PrintTrees() with
        the first object in the returned array.

          (i)   Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 2(d)(i) in the evidence document.
                                                                                              [2]

         (ii)   Test your program.

                Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot into part 2(d)(ii) in the evidence document.
                                                                                              [1]





                                                     9

    (e) The procedure ChooseTree() takes an array of Tree objects as a parameter.

         The procedure prompts the user to input their requirements for a tree.
         The user needs to enter:

         •      the maximum height the tree can be in cm
         •      the maximum width the tree can be in cm
         •      whether they want the tree to be evergreen, or not evergreen.

         A tree meets the requirements if:

         •      the tree’s maximum height is not more than the user’s input

         and

         •      the tree’s maximum width is not more than the user’s input

         and

         •      the tree matches their evergreen input.

         The procedure creates a new array of all the Tree objects that meet all the requirements.

         The procedure calls PrintTrees() for each Tree object that meets all the requirements. If
         there are no trees that meet all the requirements, a suitable message is output.

          (i)   Write program code for ChooseTree().

 Save your program.

 Copy and paste the program code into part 2(e)(i) in the evidence document.
                                                                                                      [6]

         (ii)   The procedure ChooseTree() needs amending. After the procedure has output the list
                of trees that meet all the requirements, the procedure needs to:

                •   take as input the name of one of the trees that the user would like to buy from those
                    that meet all the requirements
                •   take as input the height of the tree in cm when it is bought
                •   calculate and output how many years it will take the tree to grow to its maximum
                    height.

                For example, the user inputs the tree, Beech. The tree’s height is 40 cm when bought.
                The tree will take 12 years to reach its maximum height of 400 cm.

                Write program code to amend ChooseTree().

 Save your program.

 Copy and paste the program code into part 2(e)(ii) in the evidence document.
                                                                                                      [2]





                                                    10

        (iii)   Write program code to amend the main program to call ChooseTrees().

                Test your program with the following tree requirements:

                •   a maximum height of 400 cm
                •   a maximum width of 200 cm
                •   a tree that is evergreen (does not lose its leaves).

                When asked for the tree selection, use the following data:

                •   first tree name entered is ‘Blue Conifer’
                •   starting height is 100 cm.

                Take a screenshot of the outputs.

 Save your program.

 Copy and paste the screenshot into part 2(e)(iii) in the evidence document.
                                                                                      [2]
```

## Python 接口与 QP / MS 差异

接口照 QP：`Tree(Name, Growth, MaxHeight, MaxWidth, Evergreen)`、`ReadData()` 返回对象列表、`PrintTrees(Item)`、`ChooseTree(Trees)`。QP 2(e)(iii) 写 ChooseTrees（多 s），与前文不一致，按定义用 ChooseTree。输入次序采用 MS p.25：先 keep/lose、再最大高、再最大宽、选树名、购买高度。仅测试已声明的 keep/lose；不要求其他同义输入。空匹配时输出消息后结束，不进入 MS p.27 没有保护的无限购买循环。年数不强制取整；官方截图接受 3 / 3.75 / 4，Beech 示例接受 12。PrintTrees 按 QP 文字格式，末尾句号不影响判定。MS ReadData 用 split("\n")，遇文件末尾换行会产生空记录，参考解逐行读取；官方原件字节不变。

## 证据文档对照表

| 证据格 | 行 id | 分 | 内容 | 自动测（测试名 · 语料得分点） | 人工核对 |
|:--|:--|--:|:--|:--|:--|
| Part 2(a)(i) | 9618_s24_41:2(a)(i) | 4 | 代码 | `test_2a_constructor_getters` · MP2, MP4 | MP1, MP3 |
| Part 2(a)(ii) | 9618_s24_41:2(a)(ii) | 3 | 代码 | `test_2a_constructor_getters` · MP2, MP3 | MP1 |
| Part 2(b) | 9618_s24_41:2(b) | 7 | 代码 | `test_2b_reads_nine_objects` / `test_2b_missing_file` · MP1, MP2, MP3, MP4, MP5, MP6, MP7, MP8 | — |
| Part 2(c) | 9618_s24_41:2(c) | 4 | 代码 | `test_2c_printtrees_both_messages` · MP1, MP2, MP3, MP4 | — |
| Part 2(d)(i) | 9618_s24_41:2(d)(i) | 2 | 代码 | `test_2d_ii_and_2e_iii_screenshots` · MP1, MP2 | — |
| Part 2(d)(ii) | 9618_s24_41:2(d)(ii) | 1 | 截图 | `test_2d_ii_and_2e_iii_screenshots` · 整行 | — |
| Part 2(e)(i) | 9618_s24_41:2(e)(i) | 6 | 代码 | `test_2e_filter_inclusive_all_requirements_and_years` / `test_2e_no_suitable_trees` · MP1, MP2, MP3, MP4, MP5, MP6, MP7 | — |
| Part 2(e)(ii) | 9618_s24_41:2(e)(ii) | 2 | 代码 | `test_2e_filter_inclusive_all_requirements_and_years` · MP1, MP2 | — |
| Part 2(e)(iii) | 9618_s24_41:2(e)(iii) | 2 | 截图 | `test_2d_ii_and_2e_iii_screenshots` · MP1, MP2 | — |

自动覆盖表示行为得到验证；混合点里的函数头、注释、调用结构仍须补核，不能凭测试自动授予考试分数。可选得分点多于该行满分时，按 markpoints[].marks 加权后按该行满分比例折算。

## 人工核对清单

- [ ] 2(a)(i) MP1：Class Tree declaration (and end where appropriate)
- [ ] 2(a)(i) MP3：Constructor header (and end) taking 5 parameters
- [ ] 2(a)(ii) MP1：1 get method with no parameter …
- [ ] 所有方法头、主程序的调用顺序、返回值接收与题给标识符符合该题 MS；属性注释写明类型，私有属性不改成公有属性。
- [ ] 题目指定算法自行实现，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳（D10 ③；本项人工核对）。
- [ ] 截图清晰，输入、输出及要求的文件名可见；appropriate message 的语义与状态一致（措辞不限）。

## 得分点编号（D37 ②）

编号采用语料 markpoints[].n；1 分且未拆分的行记“整行”。本题 MS 圆点顺序与语料一致；若 MS 给可选点上限，按该行上限计分。
