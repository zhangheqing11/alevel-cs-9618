# 按完整单词裁剪音乐标题

来源：9618_s24_22:6(a)；QP p12，MS p9，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A music player stores music in a digital form and has a display which shows the track being
    played.
Up to 16 characters can be displayed. Track titles longer than 16 characters will need to be
        trimmed as follows:
        •   Words must be removed from the end of the track title until the resulting title is less than
            14 characters.
        •   When a word is removed, the space in front of that word is also removed.
        •   Three dots are added to the end of the last word displayed when one or more words
            have been removed.
        The table below shows some examples:
     Original title                 Display string
Bat out of Hull                Bat out of Hull
Bohemian Symphony              Bohemian...
Paperbook Writer               Paperbook Writer
Chris Sings the Blues          Chris Sings...
Green Home Alabama             Green Home...
A function Trim() will:
        •   take a string representing the original title
        •   return the string to be displayed.
        Assume:
        •   Words in the original title are separated by a single space character.
        •   There are no spaces before the first word or after the last word of the original title.
        •   The first word of the original title is less than 14 characters.
        Write pseudocode for the function Trim().
```

## Python 接口

入口：`Trim(Name)`。按 QP 的“少于 14 字符”保留完整单词。参考解每次删除单词时同时删除其前空格；避免 MS 范例将最终空格留到循环外时，在 13 字符边界多删单词。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

本题 MS 总分上限为 7 分；以下候选得分点不能简单相加超过此上限。

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading, ending, parameter and return type
- [ ] MP2：If length of original string <= 16 then return original string
- [ ] MP3：Any Conditional loop...
- [ ] MP4：until string is short enough
- [ ] MP5：Inner conditional loop / second condition to identify word(s) to remove from the end of string // Check to identify word(s) to remove from the end of string
- [ ] MP6：Attempt to strip characters back to space
- [ ] MP7：Correct removal of word/words from end of string and remove final space
- [ ] MP8：Concatenate Dots and return result
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
