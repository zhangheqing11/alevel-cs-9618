# 将三行会员信息重组为一行

来源：9618_w25_22:3(a)；QP p.4，MS p.8，6 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A text file OldFile.txt contains IDs, names and email addresses for members of a club. Three
    information items are stored for each member and each item is stored on a separate line.
    The example shows the information for the first two members in the first six lines of the file:
      Line in file         Information item                  Example data
           1       member 1 ID                  "AB1234"
           2       member 1 name               "Freddie Jones"
           3       member 1 email address       "FreddieJ909@Cambridge.org"
           4       member 2 ID                  "BC2345"
           5       member 2 name               "Sue Smith"
           6       member 2 email address       "Sue1024@Cambridge.org"
    The member ID string is always two letters followed by four digits.
    The file design is to be changed so that information for each user is stored as a single line of the
    file, with the character '\' used as a separator between data items.
    For example, the single line for member 1 will be:
    "AB1234\Freddie Jones\FreddieJ909@Cambridge.org"
    An algorithm will produce a new file NewFile.txt from the contents of OldFile.txt
    Assume:
    •   LineX, LineY and LineZ are of type STRING and are used to store the three items of
        information for each member
    •   NewString is a temporary variable of type STRING
    •   OldFile.txt exists and contains valid data.
The algorithm to create the new file is expressed in steps.
Complete the following numbered steps:
Step 1 : open the file ..................................... in .....................................
Step 2 : open the file ..................................... in .....................................
Step 3 : read a line from ..................................... and store in .....................................
Step 4 : read a line from ..................................... and store in .....................................
Step 5 : read a line from ..................................... and store in .....................................
Step 6 : set NewString to ...........................................................................................
Step 7 : write NewString to .....................................
Step 8 : repeat from step ..................................... until .....................................
Step 9 : close both files.
```



## Python 接口

入口：`main()`。`main()` 把 OldFile.txt 每三行ID/姓名/email合成一行，以单个反斜杠分隔，写入/覆盖 NewFile.txt；每行LF结尾、源文件不变。样例照 QP 前六行，末行不换行；不测不完整记录。原题Step9已给，不另加分；语料MP3合计Steps3–5的一分，不按读取次数拆分（D37）。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：1 open the file OldFile.txt in read (mode)
- [ ] MP2：2 open the file NewFile.txt in write (mode)
- [ ] MP3：3 read a line from OldFile.txt and store in LineX MP3 4 read a line from OldFile.txt and store in LineY 5 read a line from OldFile.txt and store in LineZ
- [ ] MP4：6 set NewString to LineX & '\' & LineY & '\' & LineZ
- [ ] MP5：7 write NewString to NewFile.txt
- [ ] MP6：8 repeat from step 3 until end of OldFile.txt
- [ ] 本小问总分上限 6 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
