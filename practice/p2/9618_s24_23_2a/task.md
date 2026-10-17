# 将文件逐行复制到全局数组

来源：9618_s24_23:2(a)；QP p.4，MS p.4，5 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text

A program uses a global 1D array of type string and a text file.
        An algorithm that forms part of the program is expressed as follows:
        •   copy the first line from the file into the first element of the array
        •   copy the second line from the file into the second element of the array
        •   continue until all lines in the file have been copied into the array.
        Stepwise refinement is applied to the algorithm.
        Outline five steps for this algorithm that could be used to produce pseudocode.
        Assume there are more elements in the array than lines in the file.
        Do not use pseudocode statements in your answer.
```



## Python 接口

入口：`main()`。原题未命名数组/文件，Python 全局 Data 与 FileName="data.txt"；Data 为真实 list、长度只需大于文件行数，starter 的64仅是样例容量。不要求清空未使用元素。保留空行，末行无 LF 也作为一行，去掉行结束符后入数组。files/data.txt 为自制样例，末行不换行。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Open the file (in read mode and subsequently close)
- [ ] MP2：Initialise an index variable (to 1 // 0)
- [ ] MP3：Repeat (the next three steps) until the end of file is reached
- [ ] MP4：Read a line from the file (into a string variable)
- [ ] MP5：Store the line / variable in the array at the index
- [ ] MP6：Increment the index in a loop
- [ ] 本小问总分上限 5 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
