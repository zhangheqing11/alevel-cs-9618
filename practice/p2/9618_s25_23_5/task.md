# 添加偶校验位

来源：9618_s25_23:5；QP p10，MS p10，8 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A module Parity() takes a string as a parameter. The parameter has the identifier BitString
    and it represents a binary value.
    The module will concatenate a single character to the end of BitString by applying one of the
    two rules:
    •   '0' if Bitstring contains an even number of 1s
    •   '1' if Bitstring contains an odd number of 1s.
    The modified value of BitString is then returned.
    For example:
          Parameter         String returned                    Explanation
     "0010010110"      "00100101100"     there are an even number of 1s in the string
                                              passed to Parity() so a '0' is concatenated
                                              to the end of BitString
     "101010"           "1010101"          there are an odd number of 1s in the string
                                              passed to Parity() so a '1' is concatenated
                                              to the end of BitString
    Write pseudocode for the module Parity()
    Assume the parameter BitString can only contain the characters '0' and '1'
```

## Python 接口

入口：`Parity(BitString)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading and ending and parameter (STRING) and return type STRING
- [ ] MP2：Loop for length of BitString
- [ ] MP3：Extract current character in a loop
- [ ] MP4：Compare current character to '1' or '0' in a loop
- [ ] MP5：Increment count and was Initialised earlier in a loop
- [ ] MP6：Check if even/odd number of 1s
- [ ] MP7：Append '1' or '0' as appropriate
- [ ] MP8：Return amended BitString
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
