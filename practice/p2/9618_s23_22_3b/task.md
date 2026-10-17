# 将文件逐行加入队列

来源：9618_s23_22:3(b)；QP p.5，MS p.4，5 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program stores data in a text file. When data is read from the file, it is placed in a queue.
The design of the queue is completed and the number of locations is increased.
        A function AddToQueue() has been written. It takes a string as a parameter and adds this to
        the queue. The function will return TRUE if the string was added successfully.
        A procedure FileToQueue() will add each line from the file to the queue. This procedure
        will end when all lines have been added or when the queue is full.
        Describe the algorithm for procedure FileToQueue().
        Do not use pseudocode in your answer.
```



## Python 接口

入口：`FileToQueue()`。保留 `FileToQueue()`、provided `AddToQueue(Value)`；原题没有文件名，包装用全局 FileName="queue.txt"。AddToQueue 的 False 表示满；只测通过该接口加入的行及遇满终止，不考原题已写好的队列实现。空行也是一条字符串，末行不换行的样例在 files/。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Open file in READ mode
- [ ] MP2：Loop to EOF()// read / process all the lines in file
- [ ] MP3：Loop will end when return value from AddToQueue() is FALSE / queue is full
- [ ] MP4：Read a line from the file in a loop
- [ ] MP5：Pass string to AddToQueue()// AddToQueue()is executed with line as parameter
- [ ] 本小问总分上限 5 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
