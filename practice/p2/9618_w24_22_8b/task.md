# 将角色记录保存为文本

来源：9618_w24_22:8(b)；QP p20，MS p12，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program is being developed to implement a game for up to six players.
    During the game, each player assembles a team of characters. At the start of the game there are
    45 characters available.
    Each character has four attributes, as follows:
      Attribute          Examples                           Comment
     Player      0, 1, 3                    The player the character is assigned to.
                                          The job that the character will perform in the
     Role       Builder, Teacher, Doctor
                                          game.
                                          The name of the character. Several characters
     Name      Bill, Lee, Farah, Mo        may perform the same role, but they will each
                                          have a unique name.
                                          The skill level of the character. An integer in the
     Level       14, 23, 76
                                          range 0 to 100 inclusive.
    The programmer has defined a record type to define each character.
    The record type definition is shown in pseudocode as follows:
    TYPE CharacterType
        DECLARE Player : INTEGER
        DECLARE Role : STRING
        DECLARE Name : STRING
        DECLARE Level : INTEGER
    ENDTYPE
    The Player field indicates the player to which the character is assigned (1 to 6). The field value is
    0 if the character is not assigned to any player.
    The programmer has defined a global array to store the character data as follows:
    DECLARE Character : ARRAY[1:45] OF CharacterType
    At the start of the game all record fields are initialised, and all Player field values are set to 0
    The programmer has defined a program module as follows:
       Module                                 Description
     Assign()   •   called with two parameters:
                      ○   an integer representing a player
                      ○   a string representing a character role
                  •   search the Character array for an unassigned character with the
                      required role
                  •   If found, assign the character to the given player and output a confirmation
                      message, for example:
                      "Bill the Builder has been assigned to player 3"
                  •   If no unassigned character with the required role is found, output a suitable
                      message.
A new module will store the contents of the Character array in a text file.
        The module is defined as follows:
           Module                             Description
         Save()      •   form a string from each record with fields separated by the
                          character '^'
                      •   write each string to a separate line of the new file named
                          SaveFile.txt
        Complete the pseudocode for module Save().
        PROCEDURE Save()
        ENDPROCEDURE
```

## Python 接口

入口：`Save()`。字段顺序依 QP 记录表 Player^Role^Name^Level，每条记录一行 LF，含未分配角色，完整写 45 条；覆盖 SaveFile.txt。不输出。字符串字段不含分隔符 ^ 或换行（QP 未定义转义机制，不测此类输入）。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Declaration of local integer for Index (and string type for Line)
- [ ] MP2：Open "SaveFile.txt" in write mode and subsequently close
- [ ] MP3：Loop through 45 elements
- [ ] MP4：Attempt to form Line - four fields in a loop
- [ ] MP5：Correct use of NUM_TO_STR()x2 (Player and Level) in a loop
- [ ] MP6：Correct use of three &<separator>& strings in a loop
- [ ] MP7：Line from MP4 written to file in a loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
