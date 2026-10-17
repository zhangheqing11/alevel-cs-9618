# 拆解固定宽度库存字段

来源：9618_w22_23:5(a)(i)；QP p7，MS p5，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A text string contains three data items concatenated as shown:
        <StockID><Description><Cost>
        Item lengths are:
                              Item              Length
                           StockID      5
                           Description   32
                           Cost         the remainder of the string
        A procedure Unpack() takes four parameters of type string. One parameter is the original
        text string. The other three parameters are used to represent the three data items shown in
        the table and are assigned values within the procedure. These values will be used by the
        calling program after the procedure ends.
Write pseudocode for the procedure Unpack().
```

## Python 接口

入口：`Unpack(TLine,SID,SDesc,SCost)`。按 QP 标识符 Unpack（MS 范例写 UnPack）。三个 BYREF 字符串参数用单元素 list；原始字符串参数不修改。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Procedure heading and ending including four parameters...
- [ ] MP2：...and use of BYREF for the three extracted values
- [ ] MP3：Extract and assign SID
- [ ] MP4：Extract and assign SDesc
- [ ] MP5：Calculation of length of SCost (remainder of string)
- [ ] MP6：Extract and assign SCost following an attempt at MP5
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
