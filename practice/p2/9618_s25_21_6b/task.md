# 按速度对传感器读数冒泡排序

来源：9618_s25_21:6(b)；QP p12，MS p11，8 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program monitors the speed of vehicles as they move around a large building site.
    Each vehicle contains a sensor which reads an integer value that represents the speed of the
    vehicle. The value is expected to be in the range 0 to 60 inclusive.
    The sensors cannot read values less than 0.
    A program module has been written to validate the values read by the sensors.
Each sensor used in the system has a unique sensor ID number in the range 1 to 50.
        The program that is used to monitor the speed of each vehicle reads each sensor value
        every second and stores this value along with the sensor’s unique ID into a global 2D array
        Reading
        The global array Reading has been declared as follows:
                 DECLARE Reading : ARRAY[1:2000, 1:2] OF INTEGER
        The array contains 4000 elements organised as 2000 rows and 2 columns.
        Column 1 contains the sensor value, and column 2 contains the sensor ID.
        When 2000 sensor readings have been taken, the array is full and the system stops taking
        any more sensor readings until the array has been processed.
        A procedure Sort() is needed to sort the array into ascending order of sensor value using
        an efficient bubble sort algorithm.
        Write efficient pseudocode for the procedure Sort()
```

## Python 接口

入口：`Sort()`。Reading 是真实 2000×2 list；两列是速度与传感器 ID，必须成对移动，原位升序排序，不输出。相同速度的稳定性 QP 未规定，测试不限制同速行顺序。禁止 sort/sorted/index/in 等替代要求的冒泡算法；循环、交换标志与缩短边界仍须人工按 MS 检查。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

## 人工核对清单

本题 MS 总分上限 8 分，候选得分点不能简单相加超过此上限。

Python 测试只验证行为，不能替代伪代码逐点批改。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Procedure heading and ending
- [ ] MP2：Conditional loop correctly formed including Boolean flag declared and initialised
- [ ] MP3：An inner loop
- [ ] MP4：Correct range 1 to 1999 for inner loop
- [ ] MP5：Comparison of element J with J+1 in a loop
- [ ] MP6：Declare Temp variable and swap elements in a loop
- [ ] MP7：Both SensorID and Speed values were swapped in a loop
- [ ] MP8：'No-Swap' mechanism: • Conditional outer loop including flag reset • Flag set in inner loop to indicate swap
- [ ] MP9：Reducing Boundary in the outer loop
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
