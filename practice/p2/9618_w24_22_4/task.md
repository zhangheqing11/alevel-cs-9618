# 用毫秒时钟定时提醒

来源：9618_w24_22:4；QP p8，MS p7，6 分。已对照 QP 原页核对下列题干、表格与示例。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`，按下列接口测试。

## 英文原题与给定信息

```text
A global integer variable Tick is always incremented every millisecond (1000 times per second)
    regardless of the other programs running.
    The value of Tick can be read by any program but the value should not be changed.
    Assume that the value of Tick does not overflow.
    As an example, the following pseudocode algorithm would output "Goodbye" 40 seconds after
    outputting "Hello".
        DECLARE Start : INTEGER
        OUTPUT "Hello"
        Start ← Tick
        REPEAT
            //do nothing
        UNTIL Tick = Start + 40000
        OUTPUT "Goodbye"
    A program is needed to help a user to time an event such as boiling an egg.
    The time taken for the event is known as the elapsed time.
    The program contains a procedure Timer() which will:
    •   take two integer values representing an elapsed time in minutes and seconds
    •   use the value of variable Tick to calculate the elapsed time
    •   output a warning message 30 seconds before the elapsed time is up
    •   output a final message when the total time has elapsed.
    For example, to set an alarm for 5 minutes and 45 seconds the program makes the following call:
        CALL Timer(5, 45)
    When 5 minutes and 15 seconds have elapsed, the program will output:
        "30 seconds to go"
    When 5 minutes and 45 seconds have elapsed, the program will output:
        "The time is up!"
    Write pseudocode for the procedure Timer().
```

## Python 接口

入口：`Timer(Mins,Secs)`。Python 使用已提供 ReadTick() 读取外部更新的 Tick，伪代码直接读全局 Tick。测试注入毫秒时钟，无真实等待；持续时间至少 30 秒（原题未说明不足 30 秒时的提前提醒规则）。不限定消息措辞，只核对两个时刻与非空消息。

骨架中标注为“provided”的辅助模块来自题目给定契约，不属于本小问作答；保留它们即可。未给参数名时采用该题 MS 范例的名字。题目没有模块名时，`main` 是本练习的 Python 调用入口，伪代码仍按原题写算法。

## 人工核对清单

Python 测试只核对行为；下面逐点以本题 MS 人工批改，不能把测试通过当作伪代码得分。

- [ ] MP1：Procedure heading and parameters and ending
- [ ] MP2：‘Attempt’ to calculate ‘total time’/EndTick // ‘elapsed time’ // WarningTick
- [ ] MP3：Correct calculation of EndTick and WarningTick
- [ ] MP4：(Design mark) • Two separate loops – checking warning time then the final time, OR … • Single loop checking the final time with an IF statement to check for warning time, OR … • Single loop with two IF statements checking the warning time and final time
- [ ] MP5：Completely correct MP4
- [ ] MP6：Output both messages (must be meaningful and follow successful MP4)
- [ ] 模块头、参数类型/顺序、RETURNS、结束行与变量声明逐项核对；只要求补算法时不额外要求函数头。
- [ ] 伪代码使用指南关键字、大写关键字与 `←`；要求 pseudocode 时，混入 Python 语法或插页外语言函数，该得分点不给（D2）。
- [ ] 不用内置查找/排序等代替题目要求的算法；数组使用题给上下界的全局声明（D10/D24）。
- [ ] 不依赖 AND 短路；先检查索引/长度，再读取元素（D25）。
