# 阶乘与非法负数

来源：9618_s22_23:6(a)；QP p8，MS p7，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
The factorial of a number is the product of all the integers from 1 to that number.
        For example:
            factorial of 5 is given by 1 × 2 × 3 × 4 × 5 = 120
            factorial of 7 is given by 1 × 2 × 3 × 4 × 5 × 6 × 7 = 5040
            factorial of 1 = 1
        Note: factorial of 0 = 1
        A function Factorial() will:
        •   be called with an integer number as a parameter
        •   calculate and return the factorial of the number
        •   return −1 if the number is negative.
        Write pseudocode for the function Factorial().
```

## Python 接口

入口：`Factorial(ThisNum)`。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Function heading and ending including parameter and return value
- [ ] MP2：Declaration and initialisation (to 1) of local Integer Value for result
- [ ] MP3：Check for illegal value (< 0)
- [ ] MP4：(Conditional) loop while ThisNum not zero // loop for ThisNum iterations
- [ ] MP5：Attempt to form answer by successive multiplication
- [ ] MP6：Completely correct MP5
- [ ] MP7：Return INTEGER value correctly in both cases: ThisNum < 0 and >= 0
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
