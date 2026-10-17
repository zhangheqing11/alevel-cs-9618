# 忽略大小写的回文判断

来源：9618_s22_21:7(a)；QP p11，MS p8，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A string is a palindrome if it reads the same forwards as backwards.
    The following strings are examples of palindromes:
        "Racecar"
        "madam"
        "12344321"
    Upper-case and lower-case characters need to be treated the same. For example, 'A' is equivalent
    to 'a'.
A function IsPalindrome() will take a string parameter. The function will return TRUE if the
        string is a palindrome and will return FALSE if the string is not a palindrome.
        Write pseudocode for IsPalindrome().
```

## Python 接口

入口：`IsPalindrome(InString)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Functions header including parameter, ending and return type
- [ ] MP2：Calculation of number of pairs to match (length or half length)
- [ ] MP3：Loop for half or whole string
- [ ] MP4：…Extracting characters to compare // create reverse string
- [ ] MP5：Convert characters to same case
- [ ] MP6：Check for mismatch of characters inside loop / test for mismatch after loop for reversed string
- [ ] MP7：Returning Boolean in both cases
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
