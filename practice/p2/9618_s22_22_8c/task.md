# 生成无重复字符的分组密码

来源：9618_s22_22:8(c)；QP p.18，MS p.14，6 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text

A password has a fixed format, consisting of three groups of four alphanumeric characters,
separated by the hyphen character '-'.
An example of a password is: "FxAf-3haV-Tq49"
Each password must:
• be 14 characters long
• be organised as three groups of four alphanumeric characters. The groups are separated
  by hyphen characters
• not include any duplicated characters, except for the hyphen characters.
An algorithm is needed for a new function GeneratePassword(), which will generate and
return a password in this format.
Assume that the following modules have already been written:
Module        Description
Exists()      Takes two parameters: a string, a character.
              Performs a case-sensitive search for the character in the string.
              Returns TRUE if the character occurs in the string, otherwise returns FALSE.
RandomChar()  Generates a single random character from within one of the following ranges:
              'a' to 'z', 'A' to 'Z', '0' to '9'. Returns the character.
Note: in a case-sensitive comparison, 'a' is not the same as 'A'.
Describe the algorithm for GeneratePassword().
Do not use pseudocode statements in your answer.
```



## Python 接口

入口：`GeneratePassword()`。保留 `GeneratePassword()`、provided `Exists(Text, Character)` 和 `RandomChar()`；无输入、不打印，返回 str。随机源测试时注入，只核对格式、合法字符、全局无重复及大小写区别，不强制抽取顺序。此问不使用前面 Secret 数组。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Initialise password to empty string at the start and return (attempted) password at the end of the function
- [ ] MP2：Two loops to generate 3 groups of 4 characters // One loop to generate 12 / 14 characters
- [ ] MP3：Use of RandomChar()to generate a character in a loop
- [ ] MP4：Reject character if Exists()returns TRUE, otherwise form string in a loop
- [ ] MP5：(Attempt to) use hyphens to link three groups
- [ ] MP6：Three groups of four characters generated correctly with hyphens and without duplication (completely working algorithm)
- [ ] 本小问总分上限 6 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
