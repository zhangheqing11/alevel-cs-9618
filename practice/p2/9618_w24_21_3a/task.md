# 补全输出文件最后三行的文字步骤

来源：9618_w24_21:3(a)；QP p.6，MS p.5，4 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
An algorithm will output the last three lines from a text file Result.txt
    The lines need to be output in the same order as they appear in the file.
    Assume:
    •   Three variables LineX, LineY and LineZ will store the three lines. These are of type string
        and all three variables have been initialised to an empty string.
    •   The file exists and contains at least three lines.
The algorithm to output the lines is expressed in eight steps.
Complete the steps.
1. Open the file ........................................................
2. Loop until ...........................................................
3. ............................................. and store in ThisLine
4. Assign LineY to LineX
5. Assign LineZ to LineY
6. Assign ThisLine to LineZ
7. After the loop, .......................................................
8. Output LineX, LineY, LineZ
```



## Python 接口

入口：`main()`。`main()` 读 Result.txt，至少三行；结束后逐行输出最后三行，保留空行及行内空格。files/Result.txt 为五行自制样例、末行LF。不测少于三行。原题已给移位和输出步骤，四分仅给补空部分；语料 MP1/MP2/MP3/MP4 分别对应原页 Step1/Step2/Step3/Step7（D37）。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Open the file (Result.txt) in read mode
- [ ] MP2：Loop until EOF(Result.txt) // EOF // end of file
- [ ] MP3：Read a / the / next line (from the file) and store in ThisLine
- [ ] MP4：After the loop, close the file (Result.txt)
- [ ] 本小问总分上限 4 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
