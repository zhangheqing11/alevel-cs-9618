# 向密码表添加新网站

来源：9618_s22_23:9(b)；QP p16，MS p11，6 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

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
A global 2D array Secret of type STRING stores the passwords together with the website
        domain name where they are used. Secret contains 1000 elements organised as 500 rows
        by 2 columns.
        Unused elements contain the empty string (""). These may occur anywhere in the array.
        An example of part of the array is:
               Array element                  Value
         Secret[27, 1]            "www.thiswebsite.com"
         Secret[27, 2]            "●●●●●●●●●●●●"
         Secret[28, 1]            "www.thatwebsite.com"
         Secret[28, 2]            "●●●●●●●●●●●●"
        Note:
        •   For security, the passwords are stored in an encrypted form, shown as "●●●●●●●●●●●●"
            in the example.
        •   The passwords cannot be used without being decrypted.
        •   You may assume that the encrypted form of a password will not be an empty string.
        Additional modules are defined as follows:
               Module                                Description
                             • Takes a password as a string
         Encrypt()
                             • Returns the encrypted form of the password as a string
                             • Takes an encrypted password as a string
         Decrypt()
                             • Returns the decrypted form of the password as a string
                             • Takes a website domain name as a string
                             • Searches for the website domain name in the array Secret
                             • If the website domain name is found, the decrypted password is
         FindPassword()
                              returned
                             • If the website domain name is not found, an empty string is
                              returned
                             • Takes two parameters as strings: a website domain name and a
                              password
                             • Searches for the website domain name in the array Secret and
         AddPassword()      if not found, adds the website domain name and the encrypted
                              password to the array
                             • Returns TRUE if the website domain name and encrypted
                              password are added to the array, otherwise returns FALSE
        The first three modules have been written.
        Write pseudocode for the module AddPassword().
```

## Python 接口

入口：`AddPassword(Name,Password)`。Python 行列下标=QP下标−1。用按数组顺序的第一个空行插入，作为本练习明确的空位选择约定；已有网站或满表返回 False 且不改变表。给定 Encrypt/Decrypt/FindPassword 保留为 provided 模块；不输出说明文字。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Check that the website domain name isn't already in array using FindPassword() / linear search, otherwise:
- [ ] MP2：(Conditional) loop while not added and not end of array
- [ ] MP3：Check for unused element by testing value in column 1 in a loop
- [ ] MP4：If unused, write parameter values to column 1 and 2 and set flag / variable
- [ ] MP5：...having used Encrypt() on the password
- [ ] MP6：Return BOOLEAN value (correctly in all cases)
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
