# T35a · P4 真题练习：批 1 前半（s 季）

9 道大题，201 分；2022–2025 s 季，涵盖 PR / AR / FL / SR / RC 及主程序、截图。按 T35 分批表全收，不含 2021 扩展卷和保留作模考的 s26；与同季 _41 重复的 _43 不另建练习。每题一个文件夹，元数据、空骨架、参考解、至少两个 mutant、按小问分组的测试与证据格对照齐全。

## 覆盖统计

自动覆盖 182.85 分（90.97%），人工核对 18.15 分（9.03%）。按 markpoints[].marks 加权；可选点超过行分值时按比例折算；只考模块头、文件关闭位置或整体结构的点列为人工。混合点含可测行为时计自动，但其函数头、注释等仍列人工补核，不能把自动通过当成满分。

| 练习 | 分 | 自动分（占比） | 人工分（占比） | mutant 数 |
|:--|--:|--:|--:|--:|
| [9618_s22_41_q1](9618_s22_41_q1/task.md) | 29 | 23.9（82.41%） | 5.1（17.59%） | 5 |
| [9618_s22_42_q2](9618_s22_42_q2/task.md) | 23 | 22（95.65%） | 1（4.35%） | 5 |
| [9618_s23_41_q1](9618_s23_41_q1/task.md) | 18 | 15.2（84.44%） | 2.8（15.56%） | 6 |
| [9618_s23_42_q1](9618_s23_42_q1/task.md) | 14 | 14（100.00%） | 0（0.00%） | 6 |
| [9618_s24_41_q1](9618_s24_41_q1/task.md) | 27 | 25（92.59%） | 2（7.41%） | 6 |
| [9618_s24_42_q1](9618_s24_42_q1/task.md) | 22 | 19.5（88.64%） | 2.5（11.36%） | 6 |
| [9618_s24_42_q3](9618_s24_42_q3/task.md) | 23 | 22（95.65%） | 1（4.35%） | 5 |
| [9618_s25_41_q2](9618_s25_41_q2/task.md) | 25 | 22.25（89.00%） | 2.75（11.00%） | 6 |
| [9618_s25_43_q2](9618_s25_43_q2/task.md) | 20 | 19（95.00%） | 1（5.00%） | 6 |

机器可读逐行记录见 `manifest-T35a.json`。`rows[].auto_mps/manual_mps` 使用语料 n；无拆分 1 分行用 whole。s24_42 Q1 1(c)(i) MP1 同时含模块头与输出行为，自动/人工原有重复登记已改为自动计 1 分、函数头人工补核。

## 原页与证据文档

前六题的原页核验记录沿用原分支逐题提交中的 manifest；本次续做亲自查看后三题完整 QP 与 MS 渲染图（包含 Python 缩进及截图）。每个 evidence.doc 均读取对应大题的全部证据格，一格一行写入 task.md；每个截图格都有自动测试，文件名同屏、输入可见与截图清晰度留人工核对。

| 练习 | QP 页 | MS 页 |
|:--|:--|:--|
| 9618_s22_41_q1 | 2, 3, 4 | 5, 9, 13, 16, 17 |
| 9618_s22_42_q2 | 4, 5, 6 | 21, 22, 24 |
| 9618_s23_41_q1 | 2, 3 | 8, 11 |
| 9618_s23_42_q1 | 2, 3, 4 | 8, 10 |
| 9618_s24_41_q1 | 2, 3, 4, 5 | 7, 9, 13 |
| 9618_s24_42_q1 | 2, 3, 4 | 13, 14 |
| 9618_s24_42_q3 | 10, 11, 12, 13 | 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39 |
| 9618_s25_41_q2 | 4, 5 | 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 |
| 9618_s25_43_q2 | 4, 5, 6 | 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 |

## 接口与执行

- 标识符和数据文件名遵从 QP；QP 没有命名的模块采用同题 MS Python 范例名，在 task.md 说明。
- 主程序写在 `if __name__ == "__main__":` 入口内，允许调用 `main()`；导入模块只定义数据/函数，不读取输入。
- `starter.py` 只给分节注释与入口，不预写可得分的声明或模块头。
- 读文件函数测试用 `use_files`；脚本截图测试用 `run_script`，在临时目录复制 files，不读取 sources。
- 算法结果、递归调用、循环替代、边界与返回值自动测；指定排序的算法结构、类型/大小注释、文件关闭位置与截图呈现人工核对。新增排序题含本地 AST 内置函数检查，不修改共享工具。
- `make try EX=practice/p4/<目录> K=3b` 等可逐小问测试；全部自动通过并完成人工清单后才能判掌握（D3）。

## 按 QP 处理与已知问题

### 9618_s22_41_q1

- 1(e)(ii): MS Python example breaks after one shift; reference and tests follow QP (whole list moves down)
- 1(f): MS example writes to " NewHighScore.txt" (leading space) and closes inside the loop; tests use the QP file name

### 9618_s22_42_q2

- 2(c)(i): MS Python example tests `if Upper >= 0`; reference follows the QP `IF Upper >= Lower`
- 2(c): the QP Mid formula (Lower + (Upper - 1)) DIV 2 recurses forever for some positions; tests use only cases the faithful translation answers correctly (standard formula also passes)

### 9618_s23_41_q1

- 1(b)/1(c): MS Java example loops to length - 1 (last element skipped, also visible in the MS p.11 screenshot); tests follow QP and include the last element

### 9618_s23_42_q1

- 1(c): QP pseudocode inner loop FOR Y <- 0 TO ArrayLength - X - 1 (inclusive) would index Animals[10]; tests check only the sorted result, MS Python range() form passes
- 1(a): MS Python example is only `global Animals #comment`; per D10 (1) the test requires a real 10-element module-level list

### 9618_s24_41_q1

- 1(a): MS Python example is only `global DataStored #integer`; per D10 (1) the test requires a real 20-element module-level list
- 1(e)(iii): MS accepts index 16 (whole 20-slot array sorted); test accepts 1 or 16

### 9618_s24_42_q1

- 1(a)/1(c): MS Python example sets NumberWords = len(WordArray) (main word included) and then mixes NumberWords-1 and NumberWords+1; QP and MS MP7 say NumberWords counts answers only, reference and tests follow QP
- 1(d)(iii): MS p.14 screenshot shows an extra debug line (97); tests check only the values the MS lists

### 9618_s24_42_q3

- `RecursiveInsertion(IntegerArray, NumberElements)`；`IterativeInsertion(IntegerArray, NumberElements)`（MS 也接受仅数组参数，测试兼容）；`BinarySearch(IntegerArray, First, Last, ToFind)`。
- 3(c)(i)：MS p.35 的 Python 外循环从 NumberElements 向下递减，不能对原始数组完成升序排序；例如 [3, 2, 1] 得到 [1, 3, 2]。按 QP 改为依次插入长度递增的前缀。
- 3(c)(ii)：QP 要求 original initialised array；MS p.36 直接复用已被递归排序改变的 NumberArray。参考解给两个排序各传副本，测试检查两次入口数组都为原始顺序。
- 3(b)(i) 原卷使用无界 ARRAY[] 参数；此处忠实转写，属 QP 原文，不作为 D24 教学新写法。测试不要求输出数组采用 Python 列表格式或逐行输出。

### 9618_s25_41_q2

- `ReadData()` 返回字符串列表；`SplitData(DataArray)` 无返回值，声明六个局部整数数组并分别调用 `StoreData(DataToStore, FileName)`；`StoreData` 追加写整数。按 MS 接口命名；数组在数据到达时增长（未知行数，不要求预留任意固定上限）。
- 2(a)：MS p.19 Python 直接 append(Line)，未去换行；按该行 MP6 与 QP 数据格式去除 CR/LF，否则分色失败。
- 2(b)/2(c)：MS p.21 将 SplitLine[0] 字符串加入数组，p.26 直接 write(Item)；QP 明确数组存 integer，参考解先 int()，写时 str()。
- 未知/损坏颜色和文件缺失时的返回数组内容 QP 未定义，测试不替题目规定；文件不存在须有异常消息。输出措辞不固定。官方空色文件一并复制，追加测试不覆写已有行。

### 9618_s25_43_q2

- `InsertionSort(DataArray)` 返回升序数组；`OutputArray(DataArray)` 无返回值，按 QP 输出一行空格分隔；`Search(DataArray, ItemToFind)` 返回下标或 −1。无数据文件，不复制本卷其他题目的 QueueData.txt。
- 本题 Python MS 范例与 QP 无需作行为修正。2(c) 的 Java / VB 范例跳过值 −1，QP 要求输出每个元素，本练习一律按 QP 输出所有元素（含负整数）。允许迭代或递归二分查找，排序须为插入排序。
- 截图测试按 MS p.25 / p.32 的数值与顺序断言，不固定说明文字；单行空格格式只在 QP 明确要求的 OutputArray 中检查。

s24_42 Q3 的 QP 原始伪代码使用 ARRAY[] 参数，转写忠实保留；不是新编伪代码的推荐格式。MS 3(c)(i) 倒序外循环不能正确排序原始数据，参考解改为递增有序前缀，并保留错误范例为 mutant。3(c)(ii) 两次排序各传原始数组的副本，避免第二次得到已排序数组。

s25_41 Q2 官方空色文件六份也逐字节复制；按 QP 将分组数据转为整数，输出时再转字符串。空数组/未知行数有测试；题目未定义的损坏颜色、失败返回数组内容不另设规则。

自动覆盖仅是测试范围统计；学生实现是否贴合题给伪代码或真正采用插入排序仍需人工复核。s22_42 Q2 已知 Mid 公式缺陷沿用既有说明，不扩大为共享 schema/语料修改。

## 数据文件 sha256

所有 12 个副本当前重新与 `pipeline/extract/source_files_p4.json` 核对相同；包括六个空文件。CRLF 和末行是否换行均保留。s24_42 Q3 与 s25_43 Q2 无数据文件；不复制同卷其他题的数据。

| 练习 / 文件 | 字节 | sha256 |
|:--|--:|:--|
| 9618_s22_41_q1/HighScore.txt | 109 | `df01ab58ab0f085bfbb4a8f80d8e80406de487ed059df33830bc9cc0decc5270` |
| 9618_s23_41_q1/Data.txt | 89 | `1621c8fb2d4c9c6c5a98b7bbb66514ebdd75c6bf6d6ee79d010851481b5fadd2` |
| 9618_s24_42_q1/Easy.txt | 79 | `a70412a68fe5ebebd7e5e94a7de486f718213bdb47d97103f159f9cc30e11497` |
| 9618_s24_42_q1/Medium.txt | 273 | `8e665d58bc9c9ec87e301da29c5e15dffc29648cab7a8435497843fb41fdc07a` |
| 9618_s24_42_q1/Hard.txt | 570 | `774cee18b5abd92155c5550baf4a7787c6c29ff7cc7186c7d00287b95fcbbf13` |
| 9618_s25_41_q2/Blue.txt | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 9618_s25_41_q2/Green.txt | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 9618_s25_41_q2/Orange.txt | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 9618_s25_41_q2/Pink.txt | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 9618_s25_41_q2/Red.txt | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 9618_s25_41_q2/TheData.txt | 674 | `d8e5431c47d57241d14f05dc1fec736f71fca7557556f293e75a4d4a2f2beb24` |
| 9618_s25_41_q2/Yellow.txt | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

## 验收与需要总控决定

逐题参考解必过，所有 mutant 至少失败一项；单题运行小于 5 秒。最终 rebase 后 `make check-all`、`make check-scope TASK=T35a` 的结果与 PR 状态记录在 `tasks/progress/T35a.md`。

需要总控决定：无新增阻塞项。上述 QP/MS 差异按 D31 执行，供验收复核；没有改共享文件或语料。PR 由总控审核合并。

## T38c1 · D46 复核

9 道全部排查；每道增加 `mutant_hollow_main.py`，本批现有 51 个 mutant。调用类得分点现由实际调用记录、参数与返回结果/输出共同核对；指定结构、变量存储位置和截图仍人工补核。逐题发现、原件定位、正反对照与最终验证见 [T38c-sweep-1.md](T38c-sweep-1.md)。自动/人工分值保持原逐点分配，占比按未取整分值重算；提高的是覆盖证据，不新增分数。

T38c1 最终验收（2026-10-24）：rebase 最新主线后 `make check-all` 244/244 练习通过、657 个 mutant 各失败至少一测；`make check-scope TASK=T38c1` 与 `git diff --check` 通过。
