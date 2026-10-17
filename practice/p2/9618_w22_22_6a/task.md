# 识别阶乘的底数

来源：9618_w22_22:6(a)；QP p12，MS p9，7 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
The factorial of an integer number is the product of all the integers from that number down
        to 1.
        In general, the factorial of n is n × (n−1) × ... × 2 × 1
        For example, the factorial of 5 is 5 × 4 × 3 × 2 × 1 = 120
        In this question, n will be referred to as the BaseNumber.
        A function FindBaseNumber() will:
        •   be called with a positive, non-zero integer value as a parameter
        •   return BaseNumber if the parameter value is the factorial of the BaseNumber
        •   return −1 if the parameter value is not a factorial.
        For example:
                             Parameter value    Value returned
                                   120                 5
                                   12                 −1
                                    6                  3
                                    1                  1
        FindBaseNumber(12) will return −1 because 12 is not a factorial.
        You may use the rest of this page for rough working.
        Write pseudocode for the function FindBaseNumber().
```

## Python 接口

入口：`FindBaseNumber(ThisValue)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading and ending including parameter and return type
- [ ] MP2：Declaration and initialisation of local Num
- [ ] MP3：Any conditional loop
- [ ] MP4：Conditional loop until ThisValue found or Try out of range
- [ ] MP5：Multiply Try by Num in a loop
- [ ] MP6：Compare Try with ThisValue and set termination if the same in a loop
- [ ] MP7：Increment Num and repeat in a loop
- [ ] MP8：Attempt to Return Num if ThisValue is a factorial or -1 otherwise
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
