# 借助队列反转栈的现有元素

来源：9618_s25_21:5；QP p.10，MS p.10，7 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text

Stacks and queues are both abstract data types.
    A stack uses a top-of-stack pointer to indicate the location of the last item added to the stack.
    A queue uses two pointers:
    •   a front pointer to indicate the location of the next item to be removed from the queue
    •   a rear pointer to indicate the location of the next item to be added to the queue.
    A queue can be used to reverse the items stored on a stack.
    For example, if a stack contains six items:
    Initial state of the stack:
    top-of-stack pointer               item 6
                                    item 5
                                    item 4
                                    item 3
                                    item 2
                                    item 1
    Final state of the stack when the items have been reversed:
    top-of-stack pointer               item 1
                                    item 2
                                    item 3
                                    item 4
                                    item 5
                                    item 6
    Describe how the queue could be used to reverse the items that are currently stored on the stack.
    Your description must include how the pointers are used in both the stack and queue.
    Assume:
    •   The stack initially contains an unknown number of items.
    •   The queue can store all the items currently stored on the stack.
    •   The queue is initially empty.
```



## Python 接口

入口：`main()`。原题未给名字与下标，Python 测试包装明确 Stack、Queue 两个真实 list 和 TopOfStack（最后一个有效下标，空为−1）、FrontPointer（下次移除位置）、RearPointer（下次加入位置）；FrontPointer=RearPointer 表示队列空。容量只须足够，starter 的100不是新增上限。执行后 Stack 有效前缀反转，TopOfStack 仍指最后项，队列为空且两队列指针各前移原元素数；不要求清空无效槽。人工描述必须讲清原题指针的使用。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Pop an item off the stack
- [ ] MP2：Update Stack pointer
- [ ] MP3：Add it to the queue
- [ ] MP4：Update Rear pointer
- [ ] MP5：Repeat until the stack is empty
- [ ] MP6：Remove an item from the queue
- [ ] MP7：Update Front pointer
- [ ] MP8：Push it onto the stack
- [ ] MP9：Update the Stack pointer
- [ ] MP10：Repeat until the queue is empty
- [ ] 本小问总分上限 7 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
