## MP　主程序与测试证据：伪代码 ↔ Python 对照与模板 {#core-MP}

主程序按顺序协调已经写好的模块。最需要分清的是“调用”和“再次调用”：Pop / Dequeue 会改变数据结构，判断时再调用一次就会额外取走一个元素。

### 1. 调用与返回值

| 意图 | 伪代码 | Python | 作用 |
|:--|:--|:--|:--|
| 无返回过程 | `CALL PrintArray()` | `PrintArray()` | Python 调用不写 CALL |
| 接住函数结果 | `Returned ← Dequeue()` | `Returned = Dequeue()` | 调用一次，保存结果 |
| 检查布尔值 | `IF Stored = TRUE THEN` | `if Stored == True:` | 根据这次调用的结果分支 |
| 返回数组传下一模块 | `Data ← ReadData()`、`CALL SplitData(Data)` | `Data = ReadData()`、`SplitData(Data)` | 不能丢掉返回数组 |
| 记录字段输出 | `OUTPUT Returned.SaleID, Returned.Quantity` | `print(Returned.SaleID, Returned.Quantity)` | print(对象) 不等于 print(字段) |
| 输出函数返回字符串 | `OUTPUT Items.Traverse()` | `print(Items.Traverse())` | 只调用不 print，屏幕可能什么也没有 |

**一次调用，保存并复用**：

```pseudocode
Removed ← Dequeue()
IF Removed.SaleID = "" THEN
   OUTPUT "Queue empty"
ELSE
   OUTPUT Removed.SaleID, Removed.Quantity
ENDIF
```

Python 对应见 MP-01 完整程序的 main 部分。下列自包含小程序用一个计数器演示为什么不能为了 if 再调用一次：一次调用返回 10，下一次已经返回 20。

```python
Data = [10, 20]              # INTEGER, 2 elements
Head = 0                    # INTEGER


def Take():
    global Head
    if Head == 2:
        return -1
    Result = Data[Head]
    Head = Head + 1
    return Result


if __name__ == "__main__":
    Returned = Take()
    if Returned != -1:
        print(Returned)
    print(Take())
```

这是教学示例，不是指定真题的 Dequeue 实现。真实题要保留该题的数组、指针、空值和返回类型。

### 2. 定次循环与后测循环

| 伪代码 | Python | 易错 |
|:--|:--|:--|
| `FOR Count ← 1 TO 11` … `NEXT Count` | `for Count in range(11):` | 只用来控制次数，不用循环值时可从 0 起 |
| `FOR Value ← 1 TO 25` … `NEXT Value` | `for Value in range(1, 26):` | 要传出实际数值时，起点与终点都要保留 |
| `INPUT Value`（INTEGER） | `Value = int(input("Enter a number "))` | input 默认是 STRING；提示在 input 内（D13） |
| `Stored ← Push(Value)` | `Stored = Push(Value)` | 一次输入只 Push 一次 |
| `REPEAT` … `UNTIL Valid = TRUE` | `while True:` … `if Valid == True: break` | UNTIL 是退出条件，不是继续条件 |

定次“尝试”不等于“成功次数”：s22/42 1(d)(i) 只要 11 次尝试，最后一次栈满也要计入；不能再多问一次输入。题目若明确要求重输合法值，再加校验循环。main 负责调用 ADT 操作，操作内部负责判空判满，不能两处同时偷偷改指针。

### 3. 程序入口与文件

| 场景 | 考场写法 |
|:--|:--|
| 主程序入口 | `if __name__ == "__main__":` 下写调用顺序 |
| 全局数据 | 在所有函数外初始化，main 里避免重复初始化导致测试之间状态被清空 |
| 读文件 | try 内 open/read/close，except 输出题目要求的适当信息；回 FL 卡看具体分点 |
| 保存 | 按 QP 指定的 Question 文件名保存 Python 程序；不要只在控制台输入临时代码 |
| 修改已写模块 | 运行最新保存版本，再更新对应代码格和受影响的截图 |

### 4. 截图格对照

| 本格要求 | 截图里要看见 | 例题 |
|:--|:--|:--|
| 删除前、删除后 | 两行真实运行结果，顺序及数值正确 | s25_43:3(c)(ii)，MS p.45 |
| 六条输入、一次失败与重试 | 题表输入、成功/失败消息、出队结果、重试及最终数组 | s23_42:2(f)(ii)，MS p.22 |
| 输入后删除前后 | 全部 11 个输入及前后结果；本题允许不同的出栈后显示 | s22_42:1(e)(ii)，MS p.12 |
| 文本文件证据 | 输入 TheData.txt 的提示与输入；另图内有 Red.txt 文件名和实际内容 | s25_41:2(e)(ii)，MS p.29 |

这些是各题自己的要求，不是所有截图都必须包含所有项目。一个一分截图可以有多项联合条件；两分截图可能是两个独立测试；计数按 MS，不按截图张数或圆点数猜。学习时用控制台输出核对逻辑，真实考试仍按题干把实际截图交入证据文档。

### 5. 提交前的对应关系

把每个小问标成“代码”或“截图”，逐格核对：题号正确、代码仍有缩进、属性类型注释可见、截图能读清、输入与结果未被裁去。QP s22/42 p.2 要求证据文档每页都有姓名、centre number、candidate number，并按 `evidence_<centre number>_<candidate number>` 保存。其他卷使用该卷自己的首页说明与证据模板。

前置阶梯：L04 E01/E02（过程和函数）、L03 E01（定次循环）、L08 E03（栈）、L10 E02（链表）、L12 E01（对象）。完整考题的行为检查、MS 人工核对和截图核对分别做，不能用“程序没报错”代替其中任何一项。
