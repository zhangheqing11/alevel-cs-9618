# 把嵌套选择改写为四个独立 IF

来源：9618_w22_22:5；QP p10，MS p8，4 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
Examine the following pseudocode.
        IF A = TRUE THEN
            IF B = TRUE THEN
               IF C = TRUE THEN
                   CALL Sub1()
               ELSE
                   CALL Sub2()
               ENDIF
            ENDIF
        ELSE
            IF B = TRUE THEN
               IF C = TRUE THEN
                  CALL Sub4()
               ELSE
                  CALL Sub3()
               ENDIF
            ELSE
               IF C = FALSE THEN
                  CALL Sub3()
               ELSE
                  CALL Sub4()
               ENDIF
            ENDIF
        ENDIF
    A programmer wants to re-write the pseudocode as four separate IF...THEN...ENDIF
    statements, each containing a single CALL statement. This involves writing a single, simplified
    logic expression as the condition in each statement.
    Write the amended pseudocode.
    1 .......................................................................................................................................................
    2 .......................................................................................................................................................
    3 .......................................................................................................................................................
    4 .......................................................................................................................................................
```

## Python 接口

入口：`main()`。输入为三个全局 Boolean，输出效果为调用对应 Sub 模块；是否恰好使用四个独立 IF、每个仅含一个 CALL 由人工核对，不检查 Python 内部结构。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：IF A AND B AND C THEN CALL Sub1() ENDIF
- [ ] MP2：IF (A AND B) AND NOT C THEN CALL Sub2() ENDIF
- [ ] MP3：IF (NOT A) AND (NOT C) THEN CALL Sub3() ENDIF
- [ ] MP4：IF (NOT A) AND C THEN CALL Sub4() ENDIF
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
