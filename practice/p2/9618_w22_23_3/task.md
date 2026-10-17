# 分别累计正数与负数

来源：9618_w22_23:3；QP p.5，MS p.4，5 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text

An algorithm is needed to process a sequence of numbers. Numbers may be positive or negative
    and may be integer or decimal.
    The algorithm will:
    •   prompt and input one number at a time until the value zero is input
    •   sum the negative numbers
    •   sum the positive numbers
    •   when zero is input, output the two sum values and then end.
    Describe the algorithm needed. Do not include pseudocode statements in your answer.
```



## Python 接口

入口：`main()`。`main()` 逐个输入数值直到0；结束后输出两行纯数值，先 SumPos，再 SumNeg（原题未定顺序，此为 Python 格式约定）。包含小数、纯正/纯负与首个即0；不测试非法字符串。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Declare two (REAL)variables for the two sum values AND initialise both to zero
- [ ] MP2：Prompt AND Input a number
- [ ] MP3：If number greater than zero add to positive sum and If number less than zero add to negative sum
- [ ] MP4：Repeat from step 2 if number not zero
- [ ] MP5：After loop the Output SumPos and SumNeg
- [ ] 本小问总分上限 5 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
