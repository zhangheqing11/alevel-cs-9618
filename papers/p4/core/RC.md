## RC　递归：伪代码 ↔ Python 对照与模板 {#core-RC}

递归（recursion）是函数在更小的同类问题上调用自己。每层有自己的参数、局部变量和返回位置；基本情况不用再调用，返回后逐层组合结果。

### 1. 三件事必须一起成立

| 部件 | 要回答的问题 | 例 |
|:--|:--|:--|
| 基本情况（base case） | 什么时候可以直接回答？ | 空字符串的元音数为 0 |
| 缩小（progress） | 参数怎样接近基本情况？ | 每层去掉第一个字符 |
| 返回值组合（return / unwind） | 子问题答案怎样变成本层答案？ | 首字符是元音就加 1 |

「Base case checking (length is 0) and returning 0」⟦9618_w23_41:1(b)(i)⟧ 是该题单独一点；只判断长度却没返回 0 并不完整。「… if not a vowel, return recursive call with 1 less character」⟦9618_w23_41:1(b)(i)⟧ 提醒非元音也要返回答案。

### 2. 同一算法的两种控制结构

下面伪代码自行示范，MID 按 2027–29 指南 §5.5 从 1 起；不同于 w23_41 原题指定的 0 起函数。

```pseudocode
FUNCTION RecursiveVowels(Value : STRING) RETURNS INTEGER
   DECLARE First : CHAR
   IF LENGTH(Value) = 0 THEN
      RETURN 0
   ENDIF
   First ← MID(Value, 1, 1)
   IF First = 'a' OR First = 'e' OR First = 'i' OR First = 'o' OR First = 'u' THEN
      RETURN 1 + RecursiveVowels(MID(Value, 2, LENGTH(Value) - 1))
   ELSE
      RETURN RecursiveVowels(MID(Value, 2, LENGTH(Value) - 1))
   ENDIF
ENDFUNCTION
```

```python
def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    First = Value[0]
    if First == "a" or First == "e" or First == "i" or First == "o" or First == "u":
        return 1 + RecursiveVowels(Value[1:])
    else:
        return RecursiveVowels(Value[1:])


def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for X in range(LengthString):
        First = Value[0]
        if First == "a" or First == "e" or First == "i" or First == "o" or First == "u":
            Total = Total + 1
        Value = Value[1:]
    return Total


if __name__ == "__main__":
    print(IterativeVowels("house"))
    print(RecursiveVowels("imagine"))
```

| 迭代 | 递归 |
|:--|:--|
| 循环已知次数，或直到空串 | 每次调用先判空 |
| 变量 Value 每轮缩短 | 用缩短后的 Value 作新参数 |
| Total 累计 | return 本层贡献 + 递归结果 |
| 循环后 return Total | 基本情况 return 0，逐层送回答案 |

`Value[1:]` 是从 Python 下标 1 到结尾，不包含首字符。空串先判断，避免读 Value[0]。这题只数小写元音，不自动 lower，也不用成员运算代替逐字符算法。

### 3. 数组参数与元素个数同步

```python
def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if NumberElements == 0:
        return 0
    if ArrayCopy[0] == DataToFind:
        return 1 + RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)
    else:
        return RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)
```

「… all recursive calls have array without first element, NumberElements-1 and DataToFind」⟦9618_w25_43:3(a)(i)⟧ 是三项同时满足的一点。参数次序可以一致地选择；题目若指定接口，则按指定接口。不能只传数量减 1 却保留原数组，也不能把目标值减 1。

追踪 `[0,5,0]`、目标 0：

| 本层参数 | 本层贡献 | 等待的结果 |
|:--|--:|:--|
| `[0,5,0]`, 3 | 1 | 1 + 后两项的次数 |
| `[5,0]`, 2 | 0 | 后一项的次数 |
| `[0]`, 1 | 1 | 1 + 空数组的次数 |
| `[]`, 0 | 0 | 直接返回 0 |

从最后一行往回算：0 → 1 → 1 → 2。没有全局 Total；再次调用不会沿用上次总数。

### 4. 递归转迭代的检查

1. 用循环状态表示递归参数，例如下标、剩余个数、边界。
2. 初始化累计量，循环每轮做与一层调用相同的动作，再推进状态。
3. 原递归若一层只调用一次且线性累计，通常可直接改循环；树遍历等需要记住分支返回位置时还要显式栈，不能删掉调用就算改完。
4. 题目要求递归时，只有循环的解不满足要求；结果正确还要核对调用结构。

### 5. 常见边界

| 检查 | 写法 |
|:--|:--|
| 空数组 / 空串 | 访问首项前先判基本情况 |
| 只有一个元素 | 处理一次，递归到空后返回 |
| 求和 / 计数 | 加当前值 / 加 1，不混用 |
| 队列指针 | 本题的参数是尾后位置还是当前下标？先写清再递减 |
| 二分查找 | First > Last 才为空，访问中点前先判 |
| 基本情况返回什么 | 计数与求和常为 0；二分未找到为 −1；按当前题规定 |

队列变式 ⟦9618_w22_42:3(d)⟧ 的 MS 示例从 TailPointer−1 调用，基本情况在队首下标返回该项，和“空区间返回 0”是不同的接口约定；不要把单题初值推广成统一规则。二分查找与树遍历的完整模板分别见 SR、LT。
