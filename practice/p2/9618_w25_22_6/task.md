# 按首尾位置与大小写比较字符串

来源：9618_w25_22:6；QP p10，MS p11，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A string function Compare() will compare two strings.
    The function will:
    •   take four parameters:
        ○   two strings, String1 and String2
        ○   a character, Position, to indicate whether String1 will be compared with the start
            ('s'), or the end ('e') of String2
        ○   a Boolean, CaseMatters, to indicate whether an upper case character and lower case
            character (for example, 'A' and 'a') are regarded as different (TRUE), or as the same
            (FALSE)
    •   return FALSE if String2 has fewer characters than String1
    •   return TRUE if the comparison is true, otherwise return FALSE
    For example:
                                  Parameter
                                                                             Return
                                                                              value
         String1         String2      CaseMatters      Position
     "Cat"           "Catalogue"    TRUE            's'                TRUE
     "CAT"           "Catalogue"    TRUE            's'                FALSE
     "CAT"           "Catalogue"    FALSE           's'                TRUE
     "Cat"           "Catalogue"    TRUE            'e'                FALSE
     "GUE"           "Catalogue"    FALSE           'e'                TRUE
     "Catalogue"    "Cat"           TRUE            's'                FALSE
    Write pseudocode for the function Compare()
```

## Python 接口

入口：`Compare(String1,String2,CaseMatters,Position)`。参数顺序采用 QP 示例参数表（String1, String2, CaseMatters, Position），与 MS 函数头一致；QP 前文枚举先说明 Position 再说明 CaseMatters。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading and parameters and ending and return type
- [ ] MP2：Calculate length of String1
- [ ] MP3：if String2 is shorter than String1, return FALSE
- [ ] MP4：Compare (modified) strings
- [ ] MP5：Test CaseMatters - if FALSE and convert two string(s) to same case
- [ ] MP6：Test for the value of ‘s’/’e’ and form modified string(s) in one or both cases
- [ ] MP7：Return appropriate BOOLEAN value in all cases
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
