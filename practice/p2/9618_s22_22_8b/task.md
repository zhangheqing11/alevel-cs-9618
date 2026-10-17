# 只报告首组重复密码

来源：9618_s22_22:8(b)；QP p16，MS p13，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

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
A new module SearchDuplicates() will:
        •   search for the first password that occurs more than once in the array and output a
            message each time a duplicate is found.
            For example, if the same password was used for the three websites ThisWebsite.com,
            website27.net and websiteZ99.org, then the following messages will be output:
                "Password for ThisWebsite.com also used for website27.net"
                "Password for ThisWebsite.com also used for websiteZ99.org"
        •   end once all messages have been output.
        The module will output a message if no duplicates are found.
        For example:
                "No duplicate passwords found"
        Write efficient pseudocode for the module SearchDuplicates(). Encrypt() and
        Decrypt() functions have been written.
        Note: It is necessary to decrypt each password before checking its value.
```

## Python 接口

入口：`SearchDuplicates()`。Python 行列下标 = QP 下标−1。输出严格用 QP 示例的 Password for <site> also used for <site>，每条一行；只报告按数组顺序发现的第一组密码的全部后续匹配。没有重复时只输出 No duplicate passwords found。不得对空单元解密，不用内置查找代替循环。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 8 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：(Any) conditional loop...
- [ ] MP2：... from 1 to 499 while (attempt at) no duplicate
- [ ] MP3：Skip unused password
- [ ] MP4：Use Decrypt() and assign return value to ThisPassword
- [ ] MP5：Inner loop from outer loop index + 1 to 500 searching for duplicates
- [ ] MP6：Compare ThisPassword with subsequent passwords (after use of Decrypt())
- [ ] MP7：If match found, set outer loop termination
- [ ] MP8：and attempt an Output message giving duplicate
- [ ] MP9：Output 'No duplicate passwords found' message if no duplicates found after the loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
