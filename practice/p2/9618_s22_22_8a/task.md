# 大小写敏感的字符查找

来源：9618_s22_22:8(a)；QP p15，MS p12，5 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A program allows a user to save passwords used to log in to websites. A stored password is then
    inserted automatically when the user logs in to the corresponding website.
    A global 2D array Secret of type STRING stores the passwords together with the website domain
    name where they are used. Secret contains 1000 elements organised as 500 rows by 2 columns.
    Unused elements contain the empty string (""). These may occur anywhere in the array.
    An example of a part of the array is:
                        Array element                Value
                     Secret[27, 1]     "thiswebsite.com"
                     Secret[27, 2]     "••••••••••••"
                     Secret[28, 1]     "thatwebsite.com"
                     Secret[28, 2]     "••••••••••••"
    Note:
    •   For security, the passwords are stored in an encrypted form, shown as "••••••••••••" in the
        example.
    •   The passwords cannot be used without being decrypted.
    •   You may assume that the encrypted form of a password will NOT be an empty string.
    The programmer has started to define program modules as follows:
          Module                               Description
                       •   Takes two parameters:
                                ○ a string
                                ○ a character
       Exists()
                       •   Performs a case-sensitive search for the character in the string
                       •   Returns TRUE if the character occurs in the string, otherwise
                           returns FALSE
                       •   Takes a password as a parameter of type string
       Encrypt()
                       •   Returns the encrypted form of the password as a string
                       •   Takes an encrypted password as a parameter of type string
       Decrypt()
                       •   Returns the decrypted form of the password as a string
    Note: in a case-sensitive comparison, 'a' is not the same as 'A'.
Write pseudocode for the module Exists().
```

## Python 接口

入口：`Exists(ThisString, Search)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Conditional loop while character not found and not end of string
- [ ] MP2：Extract a char in a loop
- [ ] MP3：Compare with parameter without case conversion in a loop
- [ ] MP4：If match found, set termination logic in a loop
- [ ] MP5：Return BOOLEAN value
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
