# 将栈中数据保存到文本文件

来源：9618_s23_23:3(b)(ii)；QP p.7，MS p.4，5 分。题干、给定定义与示例已对照原页。

先在 `answer.steps.md` 用英文文字步骤作答，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A program processes data using a stack. The data is copied to a text file before the program ends.
The operation of this stack may be summarised as follows (QP p6):
• The TopOfStack pointer points to the last item added to the stack.
• The BottomOfStack pointer points to the first item on the stack.
• The stack grows upwards when items are added.
Memory location  Value  Pointer
506
505              WWW    TopOfStack
504              YYY
503              XXX
502              ZZZ
501              NNN
500              PPP    BottomOfStack
A module SaveStack() will write the data from the stack to a text file.
            Express an algorithm for SaveStack() as five steps that could be used to produce
            pseudocode.
            Write the five steps.
```

### MS 的两套步骤（p.4）

语料 MP1–MP5 是 POP 方案，最多5分。原页另接受不使用 POP 的方案：

- [ ] Alternative MP1: Open the text file in WRITE mode
- [ ] Alternative MP2: Check there is a value on the stack
- [ ] Alternative MP3: Read value from ToS location
- [ ] Alternative MP4: Write the value to the text file – Must some attempt at ‘the value’ NOT ‘all the values’
- [ ] Alternative MP5: Decrement ToS
- [ ] Alternative MP6: Repeat from step 2 // loop referencing the stack items

选与作答一致的方案核对，不能把两方案相加；均封顶5分。

## Python 接口

入口：`SaveStack()`。保留 `SaveStack()`；QP p.6 的 Stack 内存500–506映射为长度7的真实 list（Python 下标=内存地址−500），TopOfStack/BottomOfStack 保留原值；允许原 MS 的 POP 及不使用 POP 两方案。文件名 FileName="Stack.txt" 是包装约定；按栈顶到栈底逐行写、覆盖已有文件、LF结尾，不额外输出；不强制调用 POP、也不强制栈内容被清空。

未命名算法的 `main()`、未命名数据的 Python 名字及未给出的文件名/字段长度仅是测试接口约定，不是原卷新要求。骨架 provided 部分为已给定模块或数据；学生完成算法。所有数值输出允许等值表示；题面指定纯输出行时不另加说明文字。输入提示使用 `input(prompt)`（D13）。

## 人工核对清单

Python 测试只核对同算法行为，不能代替按本题 MS 给分；D31：Python 边界按 QP，人工评分按 MS 得分点。下列 MP 使用语料编号；有封顶时不能把全部可选点相加当总分。

- [ ] MP1：Open the text file in WRITE mode
- [ ] MP2：Check there is a value on the stack
- [ ] MP3：POP value ….
- [ ] MP4：Write value to the text file
- [ ] MP5：Repeat from Step 2 // loop referencing the stack items
- [ ] 本小问总分上限 5 分。
- [ ] 用英文一句一步，不写伪代码语句；说明循环的终止条件和动作位置（in the loop / after the loop）。原题给定的步骤只补空缺，定义与声明分另核对（D38）。
- [ ] 数组为题定上下界的全局数组，Python 建真实 list 并说明换算（D10/D24）；不依赖 AND 短路来防止越界（D25）。
- [ ] 不用内置查找、排序、max 等替代题目要求的算法；原题未定义的边界不自行额外判分。
