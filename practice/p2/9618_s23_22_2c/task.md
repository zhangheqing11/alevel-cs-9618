# 由生日输出星期名

来源：9618_s23_22:2(c)；QP p.3，MS p.4，6 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program stores a user’s date of birth using a variable MyDOB of type DATE.
The program will output the day of the week corresponding to MyDOB.
        For example, given the date 22/06/2023, the program will output "Thursday".
        An algorithm is required. An array will be used to store the names of the days of the week.
        Define the array and describe the algorithm in four steps.
        Do not use pseudocode statements in your answer.
```



## Python 接口

入口：`main()`。`main()` 使用全局 MyDOB（datetime.date），provided DAYINDEX 遵循插页 Sunday=1…Saturday=7；输出一行英文星期名。题目未给数组名，Python 用 Days；数组定义是作答部分，不提前填在 starter。语料 MP1/MP2 对应 MS 数组定义两点；MP3–MP6 对应原 MS Step1–Step4（D37）。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：A (1D) array containing 7 elements
- [ ] MP2：of type STRING
- [ ] MP3：Assign value "Sunday" to first element, "Monday" to second element etc.
- [ ] MP4：Use the function DAYINDEX() to return / find the day number from MyDoB
- [ ] MP5：Use the returned value as the array index / to access the element that contains the name / string
- [ ] MP6：Output the element / name / string
- [ ] 本小问总分上限 6 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
