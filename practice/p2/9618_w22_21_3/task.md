# 扫描200个整数并输出最大值

来源：9618_w22_21:3；QP p.5，MS p.4，5 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text

A 1D array Data of type integer contains 200 elements. Each element has a unique value.
    An algorithm is required to search for the largest value and output it.
    Describe the steps that the algorithm should perform.
    Do not include pseudocode statements in your answer.
```



## Python 接口

入口：`main()`。`main()` 使用全局 Data，恰200个互不相同整数；只在结束后输出一行纯最大值，不改 Data。覆盖全负数与首末位置。不能用 max/sorted 等代替原题的扫描算法；声明/输出是否在循环外仍人工核对。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Declare a variable / an integer Max
- [ ] MP2：Assign value of first / any element to Max
- [ ] MP3：Set up a loop to repeat 200 times / from start to end of array
- [ ] MP4：Use the loop counter as the array index
- [ ] MP5：If value of current element is greater than Max...
- [ ] MP6：...then assign value to Max
- [ ] MP7：After the loop, Output Max
- [ ] 本小问总分上限 5 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
