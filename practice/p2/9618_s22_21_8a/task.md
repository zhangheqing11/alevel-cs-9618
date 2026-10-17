# 生成随机字母或数字

来源：9618_s22_21:8(a)；QP p15，MS p10，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A program allows a user to save passwords used to login to websites. A stored password is
    inserted automatically when the user logs into the corresponding website.
    A student is developing a program to generate a password. The password will be of a fixed format,
    consisting of three groups of four alphanumeric characters. The groups are separated by the
    hyphen character '-'.
    An example of a password is:   "FxAf-3haV-Tq49"
    A global 2D array Secret of type STRING stores the passwords together with the website domain
    name where they are used. Secret contains 1000 elements organised as 500 rows by 2 columns.
    Unused elements contain the empty string (""). These may occur anywhere in the array.
    An example of a part of the array is:
                        Array element                Value
                    Secret[27, 1]        "www.thiswebsite.com"
                    Secret[27, 2]        "••••••••••••••"
                    Secret[28, 1]        "www.thatwebsite.com"
                    Secret[28, 2]        "••••••••••••••"
    Note:
    •   For security, passwords are stored in an encrypted form, shown as "••••••••••••••" in the
        example.
    •   The passwords cannot be used without being decrypted.
    •   Assume that the encrypted form of a password will not be an empty string.
    The programmer has started to define program modules as follows:
          Module                                Description
     RandomChar()    •   Generates a single random character from within one of the
                           following ranges:
                           ○   'a' to 'z'
                           ○   'A' to 'Z'
                           ○   '0' to '9'
                       •   Returns the character
     Encrypt()       •   Takes a password as a parameter of type string
                       •   Returns the encrypted form of the password as a string
     Decrypt()       •   Takes an encrypted password as a parameter of type string
                       •   Returns the decrypted form of the password as a string
    For reference, relevant ASCII values are as follows:
                              Character range     ASCII range
                              'a' to 'z'            97 to 122
                              'A' to 'Z'           65 to 90
                              '0' to '9'            48 to 57
Write pseudocode for module RandomChar().
        You may wish to refer to the insert for a description of the CHR() function. Other functions
        may also be required.
```

## Python 接口

入口：`RandomChar()`。使用标准库 random；测试固定种子，只检查允许范围、字符类型与三个字符类别，不要求特定随机序列。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Generation of any integer random number
- [ ] MP2：Randomly decide which of the three ranges to select
- [ ] MP3：Selection structure based on range
- [ ] MP4：One alphanumeric character range correct
- [ ] MP5：All alphanumeric character ranges correct
- [ ] MP6：Return ThisChar, following a reasonable attempt to generate a character in each range
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
