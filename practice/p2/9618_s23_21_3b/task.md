# 按消费金额计算积分

来源：9618_s23_21:3(b)；QP p.7，MS p.5，5 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
Customers collect points every time they make a purchase at a store.
    A program is used to manage the points system and the table lists some of the information stored
    for one customer.
            Information          Data type required
     Name                             String
     Number of points collected          Integer
     Date of birth                        Date
Customers receive points depending on the amount they spend. The number of points
        depends on the band that the amount falls into:
              Band                 Amount                      Points
                1        Less than $10                  5 per whole dollar ($)
                2        Between $10 and $100 inclusive  7 per whole dollar ($)
                3        Over $100                      10 per whole dollar ($)
        For example, if the amount is $99.77, this amount is in band 2 and therefore the number of
        points is 7 × 99, which is 693 points.
        The algorithm to calculate the points from a given amount is expressed as follows:
        •   work out the appropriate band
        •   calculate and output the number of points.
        Apply the process of stepwise refinement to increase the detail of the algorithm. Structure
        your algorithm into a sequence of five steps that could be used to produce pseudocode.
        Write the five steps.
```



## Python 接口

入口：`main()`。`main()` 输入一个非负金额；按原题金额判断 band，再取整美元乘对应积分率；只输出一行纯积分数值。QP 未规定负金额，不测。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Reference to the use of constants or variables for the two threshold values of 10 and 100 // Input amount spent (by customer and store in a numeric variable)
- [ ] MP2：Work out one band that amount maps to
- [ ] MP3：Work out all bands that amount maps to
- [ ] MP4：Calculate rounded value of amount / whole number part of amount
- [ ] MP5：Calculate the points by multiplying the (rounded) amount by the appropriate value for appropriate band /all bands
- [ ] MP6：Output the number of points
- [ ] 本小问总分上限 5 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
