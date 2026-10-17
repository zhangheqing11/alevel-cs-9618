# 统计玩家某角色数量与总技能

来源：9618_w24_23:8(a)；QP p15，MS p13，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program is being developed to implement a game for up to six players.
    During the game, each player assembles a team of characters. At the start of the game there are
    45 characters available.
    Each character has four attributes, as follows:
      Attribute         Examples                          Comment
     Player      0, 1, 3                  The player the character is assigned to.
                                        The job that the character will perform in the
     Role        Builder, Teacher, Doctor
                                        game.
                                        The name of the character. Several characters
     Name      Bill, Lee, Farah, Mo      may perform the same role, but they will each
                                        have a unique name.
     Skill level   14, 23, 76               An integer in the range 0 to 100, inclusive.
    The programmer has defined a record type to define each character. The record type definition is
    shown in pseudocode as follows:
    TYPE CharacterType
        DECLARE Player : INTEGER
        DECLARE Role : STRING
        DECLARE Name : STRING
        DECLARE SkillLevel : INTEGER
    ENDTYPE
    The Player field indicates the player to which the character is assigned (1 to 6). This field value
    is 0 if the character is not assigned to any player.
    The programmer has defined a global array to store the character data, as follows:
    DECLARE Character : ARRAY[1:45] OF CharacterType
    At the start of the game all record fields are initialised, and all Player fields are set to 0
    The programmer has defined a program module as follows:
      Module                                Description
     Count()   •   called with two parameters:
                     ○   an integer representing a player
                     ○   a string representing a character role
                 •   searches the Character array for characters with the given role that are
                     assigned to the given player
                 •   counts the number of assigned characters and sums their total skill level
                 •   outputs the result of the search if characters with the given role are found,
                     for example:
                     "Player 3 has 4 characters with the role of Teacher
                     and the total skill level is 65"
                 •   if no characters with the given role are found, outputs:
                     "No characters with that role are assigned to this
                     player"
Complete the pseudocode for module Count().
        PROCEDURE Count(ThisPlayer : INTEGER, ThisRole : STRING)
        ENDPROCEDURE
```

## Python 接口

入口：`Count(ThisPlayer,ThisRole)`。QP 规定参数 ThisPlayer 然后 ThisRole；Python 下标=QP−1。SkillLevel 字段与本卷定义一致，不使用另一 variant 的 Level。不改记录。只 print 一行 QP 示例句式 Player <玩家> has <数量> characters with the role of <角色> and the total skill level is <总和>；无匹配时原题警告句一行。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 7 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Initialisation of local integers for Num and Total
- [ ] MP2：Loop through 45 elements
- [ ] MP3：Attempt to check Player and Role fields in a loop
- [ ] MP4：Correctly compare Player field with parameter in a loop
- [ ] MP5：Correctly compare Role field with parameter in a loop
- [ ] MP6：... if player and role found, increment Num and sum Skill Total in a loop
- [ ] MP7：Test for any matches after the loop
- [ ] MP8：Both possible OUTPUT statements correctly formed following an attempt at MP6 but outputting one only
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
