# 9618_s25_42 第 3 题 · Animal inheritance and descriptions

标识符及文件名照 QP；数组建成真实 list，并用英文注释注明类型与大小（D10）。从空文件完成，主程序放在 `if __name__ == "__main__":` 下，提示写在 `input("…")` 中。按 `make try EX=practice/p4/9618_s25_42_q3 K=3b` 可分问测试。对象私有属性使用 `self.__Name`；测试允许正确的循环实现，不靠指定变量名或固定提示语判分。
来源：QP pp.9–12；MS pp.33–45。已看 QP 全题原页、MS Python 范例原页；证据格与官方 evidence.doc 逐格核对。

## 英文原题（对照 QP 原页转写）

```text
9

3   A program stores data about animals using Object‑Oriented Programming (OOP).

    The class Animal stores the data about animals.

                                                 Animal
 Name : String                      stores the name of the animal

 Sound : String                     stores the sound the animal makes

 Size : Integer                     stores the size of the animal as an integer between 1 (smallest)
                                    and 10 (largest)

 Intelligence : Integer             stores the intelligence of the animal as an integer between 1 (least)
                                    and 10 (most)
 Constructor()                      initialises all attributes to its parameter values

 Description()                      returns a string message that contains the data from the attributes

    (a) (i)     Write program code to declare the class Animal and its constructor.

                Do not declare the other methods.

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program as Question3_J25.

 Copy and paste the program code into part 3(a)(i) in the evidence document.
                                                                                                       [4]

         (ii)   The method Description() creates and returns a string of the animal’s data in the
                format:

                "The animal's name is " <Name> ", it makes a " <Sound> ", its size
                is " <Size> " and its intelligence level is " <Intelligence>

                For example:

                The animal's name is Teddy, it makes a Bark, its size is 4 and its
                intelligence level is 6

                Write program code for Description()

 Save your program.

 Copy and paste the program code into part 3(a)(ii) in the evidence document.
                                                                                                       [3]





                                                     10

    (b) The class Parrot inherits from the class Animal

         Parrot inherits the attributes from Animal and overrides the Description() method. The
         additional attributes and methods in the class Parrot are:

                                                 Parrot
 WingSpan : Integer                 the width of the parrot’s wings to the nearest cm

 NumberWords : Integer              the number of words the parrot can speak
 Constructor()                      calls the parent constructor using its parameter values;
                                    initialises WingSpan and NumberWords to its parameter values

 ChangeNumberWords()                takes an integer parameter and adds this to the number currently
                                    in NumberWords

          (i)   Write program code to declare the class Parrot, its constructor and the method
                ChangeNumberWords()

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 3(b)(i) in the evidence document.
                                                                                                   [4]

         (ii)   The method Description() in the class Parrot creates and returns a string of the
                animal’s data in the format:

                "The animal's name is " <Name> ", it makes a " <Sound> ", its size
                is " <Size> " and its intelligence level is " <Intelligence> ". It
                has a wingspan of " <WingSpan> "cm and can say " <NumberWords> "
                words."

                For example:

                The animal's name is Chewie, it makes a Squawk, its size is 1 and
                its intelligence level is 10. It has a wingspan of 30cm and can
                say 29 words.

                Write program code for Description()

 Save your program.

 Copy and paste the program code into part 3(b)(ii) in the evidence document.
                                                                                                   [2]





                                                     11

    (c) The class Wolf inherits from the class Animal

         Wolf inherits the attributes from Animal and overrides the Description() method. The
         additional attributes and methods in the class Wolf are:

                                                   Wolf
 TerritorySize : Integer            stores the size of the area where the wolf lives, to the nearest
                                    square mile
 Constructor()                      calls the parent constructor using its parameter values;
                                    initialises TerritorySize to its parameter value

 SetTerritorySize()                 takes an integer parameter and adds this to the number currently
                                    in TerritorySize

          (i)   Write program code to declare the class Wolf, its constructor and the method
                SetTerritorySize()

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 3(c)(i) in the evidence document.
                                                                                                      [4]

         (ii)   The method Description() in the class Wolf creates and returns a string of the
                animal’s data in the format:

                "The animal's name is " <Name> ", it makes a " <Sound> ", its size
                is " <Size> " and its intelligence level is " <Intelligence> ".
                Its territory is " <TerritorySize> " square miles."

                For example:

                The animal's name is Nighteyes, it makes a Howl, its size is 8 and
                its intelligence level is 7. Its territory is 100 square miles.

                Write program code for Description()

 Save your program.

 Copy and paste the program code into part 3(c)(ii) in the evidence document.
                                                                                                      [2]





                                                                            12

       (d) (i)       The main program declares instances of the classes for three animals:

                     •      A parrot with the name ‘Chewie’; it makes a ‘Squawk’ sound. Its size is 1, intelligence
                            is 10, wingspan is 30 cm and it can say 29 words.
                     •      A wolf with the name ‘Nighteyes’; it makes a ‘Howl’ sound. Its size is 8, intelligence
                            is 7 and its territory is 100 square miles.
                     •      An animal that is a horse with the name ‘Copper’; it makes a ‘Neigh’ sound. Its size
                            is 10 and its intelligence is 6.

                     Write program code for the main program.

 Save your program.

 Copy and paste the program code into part 3(d)(i) in the evidence document.
                                                                                                                                                         [2]

             (ii)    The main program also needs to:

                     •      decrease the territory for the wolf Nighteyes by 20 square miles
                     •      increase the number of words the parrot Chewie can say by 2 words
                     •      output the description for all three animals.

                     Write program code to extend the main program.

 Save your program.

 Copy and paste the program code into part 3(d)(ii) in the evidence document.
                                                                                                                                                         [3]

            (iii)    Test your program.

                     Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot into part 3(d)(iii) in the evidence document.
                                                                                                                                                         [2]




Permission to reproduce items where third‑party owned material protected by copyright is included has been sought and cleared where possible. Every
reasonable effort has been made by the publisher (UCLES) to trace copyright holders, but if any items requiring clearance have unwittingly been included, the
publisher will be pleased to make amends at the earliest possible opportunity.

To avoid the issue of disclosure of answer‑related information to candidates, all copyright acknowledgements are reproduced online in the Cambridge
Assessment International Education Copyright Acknowledgements Booklet. This is produced for each series of examinations and is freely available to download
at www.cambridgeinternational.org after the live examination series.

Cambridge Assessment International Education is part of Cambridge Assessment. Cambridge Assessment is the brand name of the University of Cambridge
Local Examinations Syndicate (UCLES), which is a department of the University of Cambridge.
```

## Python 接口与 QP / MS 差异

接口照 QP：`Animal(Name,Sound,Size,Intelligence)`、`Parrot(...,WingSpan,NumberWords)`、`Wolf(...,TerritorySize)`、`Description()` 返回字符串。`SetTerritorySize(Change)` 虽叫 Set，QP 类图和 MS 都要求“加上参数”，负参数用于减少。MS p.42 Wolf.Description 把 Message 赋成 self.Sound、拼接缺项，且写成 it's territory；按 QP p.11 的完整句式修正为“. Its territory is … square miles.”。其他长字符串在 PDF 里跨行，参考解用合法的分段拼接。此题没有私有属性要求，照 MS 用公有属性，不强制学生改成私有。不测试 1–10 以外的 size/intelligence，QP 未要求校验。

## 证据文档对照表

| 证据格 | 行 id | 分 | 内容 | 自动测（测试名 · 语料得分点） | 人工核对 |
|:--|:--|--:|:--|:--|:--|
| Part 3(a)(i) | 9618_s25_42:3(a)(i) | 4 | 代码 | `test_3a_animal_constructor_description` · MP4 | MP1, MP2, MP3 |
| Part 3(a)(ii) | 9618_s25_42:3(a)(ii) | 3 | 代码 | `test_3a_animal_constructor_description` · MP2, MP3 | MP1 |
| Part 3(b)(i) | 9618_s25_42:3(b)(i) | 4 | 代码 | `test_3b_parrot_inherits_updates_and_overrides` · MP1, MP2, MP3, MP4 | — |
| Part 3(b)(ii) | 9618_s25_42:3(b)(ii) | 2 | 代码 | `test_3b_parrot_inherits_updates_and_overrides` · MP1, MP2 | — |
| Part 3(c)(i) | 9618_s25_42:3(c)(i) | 4 | 代码 | `test_3c_wolf_inherits_adds_signed_territory` · MP1, MP2, MP3, MP4 | — |
| Part 3(c)(ii) | 9618_s25_42:3(c)(ii) | 2 | 代码 | `test_3c_wolf_inherits_adds_signed_territory` · MP1, MP2 | — |
| Part 3(d)(i) | 9618_s25_42:3(d)(i) | 2 | 代码 | `test_3d_iii_screenshot_all_updated_descriptions` · MP1, MP2 | — |
| Part 3(d)(ii) | 9618_s25_42:3(d)(ii) | 3 | 代码 | `test_3d_iii_screenshot_all_updated_descriptions` · MP1, MP2, MP3 | — |
| Part 3(d)(iii) | 9618_s25_42:3(d)(iii) | 2 | 截图 | `test_3d_iii_screenshot_all_updated_descriptions` · MP1, MP2 | — |

自动覆盖表示行为得到验证；混合点里的函数头、注释、调用结构仍须补核，不能凭测试自动授予考试分数。可选得分点多于该行满分时，按 markpoints[].marks 加权后按该行满分比例折算。

## 人工核对清单

- [ ] 3(a)(i) MP1：Class header (and end when appropriate)
- [ ] 3(a)(i) MP2：Four attributes with appropriate data types
- [ ] 3(a)(i) MP3：Constructor header (and end where appropriate) within class taking (min) 4 parameters …
- [ ] 3(a)(ii) MP1：Description() method header (and end where appropriate) with no parameter
- [ ] 所有方法头、主程序的调用顺序、返回值接收与题给标识符符合该题 MS；属性注释写明类型，私有属性不改成公有属性。
- [ ] 题目指定算法自行实现，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳（D10 ③；本项人工核对）。
- [ ] 截图清晰，输入、输出及要求的文件名可见；appropriate message 的语义与状态一致（措辞不限）。

## 得分点编号（D37 ②）

编号采用语料 markpoints[].n；1 分且未拆分的行记“整行”。本题 MS 圆点顺序与语料一致；若 MS 给可选点上限，按该行上限计分。
