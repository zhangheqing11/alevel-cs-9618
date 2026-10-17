# 累加100个输入中闭区间的数

来源：9618_w23_21:2(a)；QP p.3，MS p.5，5 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text

An algorithm is expressed as follows:
        •   input 100 numbers, one at a time
        •   keep a total of all numbers input that have a value between 30 and 70 inclusive and
            output this total after the last number has been input.
        Outline, using stepwise refinement, the five steps for this algorithm which could be used to
        produce pseudocode.
        Do not use pseudocode statements in your answer.
```



## Python 接口

入口：`main()`。`main()` 恰输入100个数，按 QP 闭区间30–70累计，结束后只输出一行纯总和。测试使用整数输入；QP未限定数值类型，不以 MS 的 >29/<71 写法添加小数边界评分要求（D31）。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Set total to zero
- [ ] MP2：Input a number
- [ ] MP3：Check if number greater than 29 and less than 71
- [ ] MP4：… if check is true - add number to total
- [ ] MP5：Repeat from step 2 99 times // for a total of 100 iterations
- [ ] MP6：Output the total
- [ ] 本小问总分上限 5 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
