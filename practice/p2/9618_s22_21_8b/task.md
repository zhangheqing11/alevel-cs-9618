# 在二维密码表中查找网站

来源：9618_s22_21:8(b)；QP p16，MS p11，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

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
A new module is defined as follows:
               Module                                Description
         FindPassword()    •   Takes a website domain name as a parameter of type string
                              •   Searches for the website domain name in the array Secret
                              •   If the website domain name is found, the decrypted password
                                  is returned
                              •   If the website domain name is not found, a warning message
                                  is output, and an empty string is returned
        Write pseudocode for module FindPassword().
        Assume that modules Encrypt() and Decrypt() have already been written.
```

## Python 接口

入口：`FindPassword(Name)`。Secret 为 500×2 真实 list；Python 行列下标 = QP 下标 −1。Encrypt/Decrypt 是可替换的给定模块。找到时仅返回解密结果，不输出；找不到时返回空串且输出一条非空警告。查找不得用 in/index/max 等替代，测试单独检查这些被明令禁止的操作。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Declare all local variables used, attempted solution has to be reasonable
- [ ] MP2：Conditional loop while not found and not end of array
- [ ] MP3：Compare value of element in column 1 with parameter passed into function
- [ ] MP4：...and use Decrypt() with element in column 2 as parameter
- [ ] MP5：…use the return value of Decrypt()
- [ ] MP6：Output warning message if parameter not found
- [ ] MP7：Return STRING value
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
