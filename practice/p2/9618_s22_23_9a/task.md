# 生成分组且组内不重复的密码

来源：9618_s22_23:9(a)；QP p15，MS p10，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A program allows a user to save passwords used to log in to websites. A stored password is then
    inserted automatically when the user logs in to the corresponding website.
    A student is developing a program to generate a strong password. The password will be of a fixed
    format, consisting of three groups of four alphanumeric characters, separated by the hyphen
    character '-'.
    An example of a password is: "FxAf-3hzV-Aq49"
    A valid password:
    •   must be 14 characters long
    •   must be organised as three groups of four alphanumeric characters. The groups are
        separated by hyphen characters
    •   may include duplicated characters, provided these appear in different groups.
    The programmer has started to define program modules as follows:
          Module                                  Description
                       • Generates a single random character from within one of the following
                        ranges:
                         ○ 'a' to 'z'
     RandomChar()
                         ○ 'A' to 'Z'
                         ○ '0' to '9'
                       • Returns the character
                       • Takes two parameters:
                         ○ a string
                         ○ a character
     Exists()
                       • Performs a case-sensitive search for the character in the string
                       • Returns TRUE if the character occurs in the string, otherwise returns
                        FALSE
                       • Generates a valid password
     Generate()      • Uses RandomChar() and Exists()
                       • Returns the password
    Note: in a case-sensitive comparison, 'a' is not the same as 'A'.
Write pseudocode for the module Generate().
```

## Python 接口

入口：`Generate()`。已提供 RandomChar 和 Exists。测试可替换给定模块以确定性重现重复字符；组与组之间允许重复。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Declaration and initialisation of Password as STRING
- [ ] MP2：Outer loop for three groups / until password is complete // three group loops
- [ ] MP3：Attempt to use of both RandomChar() and Exists()in a loop
- [ ] MP4：(Inner) loop for 4 characters in a group // note every 4 chars in a loop
- [ ] MP5：Conditional loop until char is unique
- [ ] MP6：Concatenating unique character to Group in a loop
- [ ] MP7：Concatenate Group / random character to Password in a loop
- [ ] MP8：(Attempt to) insert hyphens between groups (or removing later) and Return Password
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
