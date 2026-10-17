## AD　算法设计与问题求解：伪代码 ↔ Python 对照与模板 {#core-AD}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。伪代码按 2027–29 指南书写，Python 按阶梯推荐写法（全表见 `ladder/design.md` §5）。

### 1. 术语（三层）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Abstraction | 「Abstraction is used to filter out information / data that is not necessary for the task」⟦9618_w22_21:2(a)⟧ | 滤掉与当前任务无关的信息，只保留解决问题必需的数据与操作 | 出门只带这趟用得上的东西 | P2-AD-01 |
| Benefit of abstraction | 「To make the solution easier to design / implement / solve」⟦9618_s24_21:7(a)(i)⟧ | 解法更简单，更容易设计和实现 | 背包轻了走得快 | P2-AD-01 |
| Decomposition | 「Breaking down a problem into sub problems」⟦9618_s25_21:1(c)⟧ | 把一个复杂问题拆成若干子问题，每个子问题最后成为一个模块 | 办聚会拆成列名单、发邀请、订场地 | P2-AD-02 |
| Benefits of decomposition | 「Smaller problems are easier to program / test / maintain」⟦9618_s22_22:3(b)⟧ | 子问题更易理解、编程、测试、维护，可分给不同的人并行完成 | 一人一件事，各自检查 | P2-AD-02 |
| Stepwise refinement | 「To increase the level of detail of the algorithm」⟦9618_s25_22:2(a)⟧；「until steps can be directly translated into lines of code」⟦9618_s25_22:2(a)⟧ | 把算法的每一步逐层细化，直到每一步都能直接写成代码 | 从“做饭”细化到“开火、倒油、下菜” | P2-AD-02、P2-AD-06 |
| Algorithm | 「An algorithm」⟦9618_s22_21:1(a)⟧（题干：a sequence of steps that describe how to solve a problem） | 解决一个问题的有限、有序的步骤序列 | 菜谱 | P2-AD-06 |
| Structured English | A way of describing an algorithm in numbered steps using a limited set of English words.（非 MS 原句） | 用编号步骤、有限的英文词汇描述算法，不写代码语句 | 菜谱里的“第 1 步……第 2 步……” | P2-AD-06 |
| Program flowchart | A diagram that shows the sequence of steps, decisions and loops of an algorithm using standard symbols.（非 MS 原句） | 用起止框、处理框、输入输出框、判断菱形和箭头表示算法的图 | 地铁线路图：沿箭头走，遇菱形选路 | P2-AD-04、P2-AD-05 |
| Identifier table | 「Identifier table」⟦9618_s24_22:1(c)⟧ | 记录每个标识符的名字、类型、用途说明、示例值等的表 | 一张“变量身份证” | P2-AD-03 |
| Meaningful identifier | 「The names do not reflect / indicate the purpose of the variable」⟦9618_s24_21:1(c)(i)⟧（坏名字的原因） | 能反映变量用途的名字，让程序易懂、易调试、易维护 | 盒子上的标签写清里面装什么 | P2-AD-03 |
| Count-controlled loop | 「The number of iterations required is known」⟦9618_s25_21:4(a)⟧ | 次数事先已知的循环（`FOR … NEXT`） | 绕操场跑 10 圈 | P2-AD-05、P2-PG-05 |
| Pre-condition loop | 「Pre-condition (loop) / count-controlled (loop)」⟦9618_w22_22:4(b)⟧ | 先判断后执行，可能一次都不执行（`WHILE … ENDWHILE`） | 先看有没有水再倒 | P2-AD-05、P2-PG-05 |
| Post-condition loop | 「Post-condition(al) loop」⟦9618_s26_23:1(a)⟧ | 先执行后判断，至少执行一次（`REPEAT … UNTIL`） | 先尝一口再决定还吃不吃 | P2-AD-05、P2-PG-05 |
| Rogue / sentinel value | A special input value that marks the end of the data and is not processed.（非 MS 原句） | 表示“输入结束”的特殊值（如 0、-1、99.9），本身不参与处理 | 列车终点站的牌子 | P2-AD-04、P2-AD-06 |

### 2. 流程图符号 ↔ 伪代码 ↔ Python

| 流程图 | 伪代码 | Python | 常见失分 |
|:--|:--|:--|:--|
| 圆角框 START / END | （模块的开头与结尾，或程序开始、结束） | — | 漏画 END 或箭头悬空 |
| 矩形 Set Count to 0 | `Count ← 0` | `count = 0` | 初值框画在回路里面 |
| 矩形 Set Total to Total + Num | `Total ← Total + Num` | `total = total + num` | 伪代码没有 `+=` |
| 矩形 CALL Reset(Port) | `CALL Reset(Port)` | `reset(port)` | 函数（有返回值）不能 CALL |
| 矩形 Set Flag to GetStat() | `Flag ← GetStat()` | `flag = get_stat()` | 返回值没存起来就判断别的变量 |
| 平行四边形 INPUT Num | `INPUT Num`（提示语先 `OUTPUT "…"`） | `num = int(input("…"))` | Python 忘了 `int()` |
| 平行四边形 OUTPUT Total | `OUTPUT "Total: ", Total` | `print("Total:", total)` | 输出放进了循环里 |
| 菱形 Is Num > Max ?（Yes / No） | `IF Num > Max THEN … ELSE … ENDIF` | `if num > max_value:` … `else:` | 两个出口没标 Yes / No |
| 菱形 + 指回上方的箭头（判断在前） | `WHILE <继续条件>` … `ENDWHILE` | `while <继续条件>:` | 照抄菱形的退出条件，方向反了 |
| 菱形 + 指回上方的箭头（判断在后） | `REPEAT` … `UNTIL <退出条件>` | `while True:` … `if <退出条件>: break` | Python 没有后测循环 |
| 初值框 + 判断 Index > n ? + 加 1 框 | `FOR Index ← 1 TO n` … `NEXT Index` | `for index in range(1, n + 1):` | `range` 不含终点 |

### 3. 流程图里的四种循环：模板与对照

**计数循环**（遍历一维数组 Data 的 30 个元素）

```pseudocode
FOR Index ← 1 TO 30
   IF Data[Index] <> "" THEN
      OUTPUT Data[Index]
   ENDIF
NEXT Index
```

```python
for index in range(30):          # Python index 0..29 stands for Data[1]..Data[30]
    if data[index] != "":
        print(data[index])
```

**前测循环**（条件变量在循环前和循环末尾都要更新）

```pseudocode
Flag ← GetStat()
WHILE Flag <> TRUE
   CALL Reset(1)
   Flag ← GetStat()
ENDWHILE
```

```python
flag = get_stat()
while not flag:
    reset(1)
    flag = get_stat()
```

**后测循环**（至少执行一次；UNTIL 后面是退出条件）

```pseudocode
REPEAT
   OUTPUT "Enter a mark (0 to 100): "
   INPUT Mark
UNTIL Mark >= 0 AND Mark <= 100
```

```python
while True:
    mark = int(input("Enter a mark (0 to 100): "))
    if mark >= 0 and mark <= 100:
        break
```

**哨兵循环**（先读一个，判断不是哨兵再处理；哨兵本身不处理）

```pseudocode
Total ← 0
INPUT Num
WHILE Num <> 0
   Total ← Total + Num
   INPUT Num
ENDWHILE
OUTPUT "Total: ", Total
```

```python
total = 0
num = int(input())
while num != 0:
    total = total + num
    num = int(input())
print("Total:", total)
```

**又是计数又是条件**（存满或遇到哨兵就停，如 ⟦9618_w25_22:2⟧）：用标志变量或分层判断，不要靠 `AND` 短路去保护数组下标（决策 D25）：

```pseudocode
Index ← 1
Finished ← FALSE
WHILE Finished = FALSE
   INPUT Num
   IF Num = 99.9 THEN
      Finished ← TRUE
   ELSE
      Data[Index] ← Num
      Index ← Index + 1
      IF Index > 20 THEN
         Finished ← TRUE
      ENDIF
   ENDIF
ENDWHILE
```

### 4. 文字步骤 ↔ 伪代码（AD-06 句型）

| 伪代码 | 文字步骤（英文） | MS 对应的常见得分点 |
|:--|:--|:--|
| `DECLARE Max : INTEGER` | Declare an integer variable Max. | 「Declare a variable / an integer Max」⟦9618_w22_21:3⟧ |
| `Count ← 0` | Set Count to zero (before the loop). | Initialise … |
| `OPENFILE "Sales.txt" FOR READ` | Open the file Sales.txt in read mode. | Open the file … in read mode (and subsequently close) |
| `FOR Index ← 1 TO 200` | Set up a loop to repeat 200 times, from the start to the end of the array. | Set up a loop to repeat 200 times / from start to end of array |
| `WHILE NOT EOF("Sales.txt")` | Repeat the following steps until the end of the file is reached. | 「Repeat (the next three steps) until the end of file is reached」⟦9618_s24_23:2(a)⟧ |
| `READFILE "Sales.txt", Line` | Read the next line from the file. | Read a line from the file |
| `Data[Index]` | Use the loop counter as the index to access the current element. | 「Use the loop counter as the array index」⟦9618_w22_21:3⟧ |
| `IF Num > 29 AND Num < 71 THEN` | Check if the number is greater than 29 and less than 71. | 「Check if number greater than 29 and less than 71」⟦9618_w23_21:2(a)⟧ |
| `Total ← Total + Num` | … if so, add the number to Total. | … if check is true – add number to total |
| `CLOSEFILE …` / `OUTPUT Max` | After the loop, close the file / output Max. | 「After the loop, Output Max」⟦9618_w22_21:3⟧ |

### 5. 常见失分（AD 章）

| 失分 | 正确做法 | 题型 |
|:--|:--|:--|
| 数据项与理由不对应，理由写“it is needed” | 理由指向模块的动作：to send / to personalise / to decide whether … | P2-AD-01 |
| 模块名与用途脱离情境 | 动词 + 名词()，用途写清对什么数据做什么 | P2-AD-02 |
| 标识符表名字对类型错 | 每行名字与类型都对才得分；看示例值定类型 | P2-AD-03 |
| 菱形出口没标 Yes / No | 每个菱形两个出口都标 | P2-AD-04 |
| 初值画进回路、输出画进回路 | 初值在第一个菱形之前；最终结果在出口一侧 | P2-AD-04、P2-AD-06 |
| WHILE 照抄菱形的退出条件 | WHILE 写继续条件（取反）；UNTIL 写退出条件 | P2-AD-05 |
| 文字步骤里写伪代码语句 | 一行伪代码念成一句英文 | P2-AD-06 |
| 循环只写“loop through”不说次数或结束条件 | 写 200 times / until the end of the file / until 0 is input | P2-AD-04、P2-AD-06 |
