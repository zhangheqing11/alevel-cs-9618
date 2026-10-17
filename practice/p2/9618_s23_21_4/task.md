# 替换所有指定字符

来源：9618_s23_21:4；QP p8，MS p6，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
Function Replace() will:
    1.  take three parameters:
        •   a string (the original string)
        •   a char (the original character)
        •   a char (the new character)
    2.  form a new string from the original string where all instances of the original character are
        replaced by the new character
    3.  return the new string.
    Write pseudocode for function Replace().
```

## Python 接口

入口：`Replace(OldString, Char1, Char2)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading and ending, including parameters and return type
- [ ] MP2：Declaration of local variables used including loop counter
- [ ] MP3：Loop for length of OldString
- [ ] MP4：Extract char and test in a loop
- [ ] MP5：Use of concatenate to build NewString replace char if necessary, in a loop
- [ ] MP6：Return NewString after reasonable attempt
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
