# 固定长度字段的首次匹配

来源：9618_s22_21:5；QP p.8，MS p.5，6 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text

Each line of a text file contains data organised into fixed-length fields as shown:
        <Field 1><Field 2><Field 3>
    An algorithm is required to search for the first instance of a given value of Field 2 and, if found, to
    output the corresponding values for Field 1 and Field 3.
    Describe the algorithm needed.
    Do not include pseudocode statements in your answer.
```



## Python 接口

入口：`main()`。Python 包装为 `main(FileName, SearchValue, Length1, Length2, Length3)`；字段宽度由调用者提供，输入均合法；字段2匹配后输出字段1、字段3，各一行，保留字段内空格；找不到不输出。不定义无效行处理。files/fields.txt 为自制固定宽度样例，LF 结尾。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Open file in read mode
- [ ] MP2：Set up a conditional loop, repeating until the value is found or the EOF() is reached
- [ ] MP3：Read a line from the file in a loop
- [ ] MP4：Extract Field 2
- [ ] MP5：Description of how Field 2 could be extracted e.g. using substring function and lengths of Field 1 and Field 2
- [ ] MP6：Compare extracted field with search value
- [ ] MP7：If search value found, extract Field 1and Field 3 and output them
- [ ] MP8：Close the file after loop has finished
- [ ] 本小问总分上限 6 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
