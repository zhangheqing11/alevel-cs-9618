# 输出周销量超过500的周号

来源：9618_s25_23:4(a)；QP p.8，MS p.9，5 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A programmer is developing a new stock control program for a shop owner to produce sales
    reports.
A text file Sales.txt stores strings representing the number of items sold.
        The file contains 52 lines, each representing the number of items sold in each week of the
        year.
        For example:
         File line number     File data
                1              "350"
                2              "502"
                3              "434"
               49             "492"
               50             "872"
               51             "772"
               52             "201"
        The example shows that 502 items were sold in week 2.
        The owner requires a module to output all week numbers where the number of items sold is
        greater than 500.
        Describe an algorithm that produces the required module.
        Do not include pseudocode statements in your answer.
```



## Python 接口

入口：`main()`。`main()` 读取 Sales.txt 的52条整数字符串；按原顺序输出所有销量>500的周号，一周一行纯数字，不输出销量或提示。不测非52行/非法数字。样例保留 QP 已列出的第1–3、49–52周，中间未展示周用自制0补齐；files/Sales.txt末行不换行。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Open the file (Sales.txt) in read mode and subsequently close
- [ ] MP2：Read a line (from the text file)
- [ ] MP3：Convert the line read (string) to a number
- [ ] MP4：If the number is greater than 500 and then output week number
- [ ] MP5：Increment week number (must have been Initialised …)
- [ ] MP6：Repeat from step 2 for 52 times // Repeat from step 2 until end of file
- [ ] 本小问总分上限 5 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
