# 用已填好的布尔数组验证总分

来源：9618_w25_22:4(c)；QP p.7，MS p.9，4 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A quiz has nine questions. There are:
    •   five easy questions each worth 3 points
    •   four hard questions each worth 5 points.
    At the end of the quiz the points for each correctly answered question are added to give a total
    score.
    A check is made to test that the total score is valid using a 1D array CheckTotal of type BOOLEAN.
    Each index value of the array represents a possible total score. The corresponding element value
    is TRUE if the index value represents a valid total score and FALSE otherwise.
    The first nine rows of the array are:
      Index    Element
                                                     Comment
      value     value
        0     TRUE        valid total score (no correct answers)
        1     FALSE      invalid total score
        2     FALSE      invalid total score
        3     TRUE        valid total score (one 3-point question correct)
        4     FALSE      invalid total score
        5     TRUE        valid total score (one 5-point question correct)
        6     TRUE        valid total score (two 3-point questions correct)
        7     FALSE      invalid total score
        8     TRUE        valid total score (one 3-point question and one 5-point question correct)
    For example, a total score of 6 points is valid; the value of the array element at index value 6 is TRUE
The array elements have been assigned the required values.
        A module ValidateScore() will take an integer value representing a total score as a
        parameter. It will return TRUE if the total score is valid, or FALSE if it is not valid.
        Describe the algorithm for ValidateScore() using four steps.
        Do not use pseudocode in your answer.
```



## Python 接口

入口：`ValidateScore()`。保留 `ValidateScore(TotalScore)`，参数名字是测试约定；题目只要求一个整数参数。全局 CheckTotal 下标0–35，36个bool；provided 初始化体现题目“已赋好正确值”。返回实际 bool；先检查范围再取元素，负数不能变成Python负下标。测试只用整数，不新增类型验证；本题是范围判断+直接索引，具备实际可测行为。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Check that the parameter value is in the range 0 to 35
- [ ] MP2：... and if not, return FALSE
- [ ] MP3：Use the parameter value as the index to array CheckTotal
- [ ] MP4：Return the value from given index position
- [ ] 本小问总分上限 4 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
