# 检查项目至少十个非空行

来源：9618_w22_21:8(a)；QP p14，MS p9，7 分。题干、定义、表格、数据格式与示例已对照 QP 原页。

先在 `answer.pseudo` 写剑桥伪代码，再把同一算法写入 Python `solution.py`。

## 英文原题与给定信息

```text
A teacher is designing a program to perform simple syntax checks on programs written by
    students. Student programs are submitted as text files, which are known as project files.
    A project file may contain blank lines.
    The teacher has defined the first program module as follows:
              Module                                  Description
                               • takes the name of an existing project file as a parameter of type
                                string
     CheckFile()
                               • returns TRUE if the file is valid (it contains at least 10 non-blank
                                lines), otherwise returns FALSE
Write pseudocode for module CheckFile().
```

## Python 接口

入口：`CheckFile(ThisFile)`。文件存在，可含空行；blank 用长度 0 的文件行，本题未界定纯空格行，不拿它作额外判分。返回 bool，不输出。空文件、一行、9/10/11 个非空行均测试；达到 10 后提前结束的效率点人工核对。

骨架 provided 部分是题目给定的类型、全局量或已有模块，不属于本小问作答。题目没有指定参数名字时采用本题 MS 名字；无命名算法的 Python 入口 main 仅为测试包装。

样例文件按 QP 的数据格式构造（不是官方给定的完整数据集）；测试在临时目录使用 files/ 的副本：

- `project.txt`：89 字节；最后一行无换行。


## 人工核对清单

本题 MS 总分上限 7 分，候选得分点不能简单相加超过此上限。

Python 行为测试不能替代伪代码逐点批改；另对题目明令禁止的内置查找/排序捷径作单独要求检查。D31：行为边界按 QP；人工批改按本题 MS 得分点，范例代码不是得分点。

- [ ] MP1：Function heading and ending including parameter and return type
- [ ] MP2：Declaration and initialisation of local Integer for Count
- [ ] MP3：OPEN in READ mode and CLOSE
- [ ] MP4：Conditional loop until EOF()
- [ ] MP5：Read a line in a loop
- [ ] MP6：If non-blank, increment count in a loop
- [ ] MP7：Terminate loop when 10 non-blank lines have been read
- [ ] MP8：Return Boolean in both cases
- [ ] 模块头、参数类型/顺序、RETURNS、声明与结束行逐项核对。
- [ ] 只使用指南伪代码语法与插页函数；关键字大写、赋值用 `←`。混入 Python 语法时依 D2 判该点不给。
- [ ] 数组按题给上下界全局声明，Python 真实 list 与索引换算按接口；不用内置查找/排序代替所要求算法（D10/D24）。
- [ ] 不依赖 AND 短路；先检查指针/下标，再读元素（D25）。
- [ ] QP 未定义的情况不额外推断；题面另列的 Python 接口约定仅用于自动测。
