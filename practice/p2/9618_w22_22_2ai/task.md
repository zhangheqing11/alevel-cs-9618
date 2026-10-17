# 追加需要学习支持的学生名单

来源：9618_w22_22:2(a)(i)；QP p.3，MS p.4，5 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
An algorithm will process data from a test taken by a group of students. The algorithm will
        prompt and input the name and test mark for each of the 35 students.
        The algorithm will add the names of all the students with a test mark of less than 20 to an
        existing text file Support_List.txt, which already contains data from other group tests.
Describe the steps that the algorithm should perform.
            Do not include pseudocode statements in your answer.
```



## Python 接口

入口：`main()`。`main()` 按 Name、Mark 顺序输入35组；只把 mark<20 的姓名各追加一行到 Support_List.txt；现有文件内容保留，不写成绩、不另外打印。样例现有名单为自制且 LF 结尾；不测试非数值成绩或未定义的分值上限。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Open file in APPEND mode (and subsequent Close)
- [ ] MP2：Prompt and Input a student name and mark
- [ ] MP3：If mark greater than or equal to 20 jump to step 5
- [ ] MP4：Write only the name to the file
- [ ] MP5：Repeat from Step 2 for 35 times / the number of students
- [ ] 本小问总分上限 5 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
