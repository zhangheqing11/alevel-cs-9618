# 按指定次数生成字符串

来源：9618_s23_23:4；QP p8，MS p5，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A function MakeString() will:
    1.  take two parameters:
        •   a count as an integer
        •   a character
    2.  generate a string of length equal to the count, made up of the character
    3.  return the string generated, or return "ERROR" if the count is less than 1.
    For example, the function call:
        MakeString(3, 'Z') will return the string "ZZZ"
    Write pseudocode for function MakeString().
```

## Python 接口

入口：`MakeString(Count, AChar)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading and end including parameters and return type
- [ ] MP2：Declaration of locals Index and MyString
- [ ] MP3：Test for Count < 1 and if true, assign "ERROR" to MyString / Immediate RETURN
- [ ] MP4：Loop for Count iterations
- [ ] MP5：Use of concatenate – must have been initialised in a loop
- [ ] MP6：Return STRING (correctly in both cases)
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
