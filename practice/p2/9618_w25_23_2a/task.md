# 把非空数组元素追加到现有文件

来源：9618_w25_23:2(a)；QP p.4，MS p.7，6 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text

A program contains a global 1D array of type STRING containing 65 elements.
        An existing text file is used to store the data in the array. Only non-blank elements (those that
        do not contain an empty string) are written to the text file.
        An algorithm will:
        •   write the first element of the array as a new line in the text file
        •   continue until all elements have been written, each to a new line of the text file.
        Stepwise refinement is applied to the algorithm.
        Describe up to six steps for this algorithm that could be used to produce pseudocode.
        Do not use pseudocode statements in your answer.
```



## Python 接口

入口：`main()`。原题未命名数组和文件，Python 用 Data（65个STRING）和 FileName="data.txt"。按本题MS以APPEND模式保留现有内容，再按下标顺序逐元素写入，每行LF；只跳过空串，空格字符串仍须写。输入文件样例为自制且LF结尾；不测试原文件缺行结束符时如何连接新记录（QP未定义）。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Open the file in append mode (and subsequently close) before loop
- [ ] MP2：Initialise a variable to 1 / 0 before loop
- [ ] MP3：Use the variable as an index to the array to access an element in a loop
- [ ] MP4：Test if element value is blank / empty in a loop
- [ ] MP5：If not blank then write the value to the file in a loop
- [ ] MP6：Increment the variable in a loop
- [ ] MP7：Repeat from MP3 until variable value is 66 / 65 / all elements (in the array) have been checked
- [ ] 本小问总分上限 6 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
