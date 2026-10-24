# T38c3 · T35e + T35f 逐题排查

按 D46/D31 核验自动调用点与输出约束。运行使用共享 venv。临时等价候选和原页在 `/tmp/T38c3/`，不入库。调用身份、结构及未观测的返回赋值仍需人工检查；自动覆盖不是考试自动授分。

## 9618_s24_41_q2

F08：MS p.18 明确 min 9，改测至少 9 格及前九对象；20 格等价候选修前 1 failed/7 passed，修后全过。QP pp.7–10、MS p.18 与 pp.21,28 调用点核对。 新增真实调用、参数与返回输出检查；hollow-main 保留正确模块、主程序仅输出参考结果。自动占比暂保持原值，最终分类复核见后续汇总。

- mutant_1.py: 1 failed, 8 passed in 0.16s
- mutant_2.py: 2 failed, 7 passed in 0.12s
- mutant_hollow_main.py: 1 failed, 8 passed in 0.14s
- solution.py: 9 passed in 0.32s
- equivalent.py: 9 passed in 0.15s

## 9618_w25_42_q1

F09：QP p.5、MS p.12 appropriate messages(s) 不限同一行；鸟名/坐标允许相邻行，GetPosition 返回格式保持 QP p.3 要求。分行等价候选修前 6 failed/23 passed，修后全过。 新增真实调用、参数与返回输出检查；hollow-main 保留正确模块、主程序仅输出参考结果。自动占比暂保持原值，最终分类复核见后续汇总。

- mutant_1.py: 17 failed, 14 passed in 0.49s
- mutant_2.py: 4 failed, 27 passed in 0.47s
- mutant_hollow_main.py: 8 failed, 23 passed in 0.74s
- solution.py: 31 passed in 0.55s
- equivalent.py: 31 passed in 1.73s

## 9618_s22_41_q2

主程序原仅凭 Shield 和输出行数推断调用。补构造参数、Defend 对象参数/返回身份与方法调用；返回对象重新赋给 Balloon1 的赋值无法由 traced 观测，2(g)(i) MP2 归人工。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：11 passed in 0.05s；修后与等价改写：

- mutant_1.py: 1 failed, 11 passed in 0.09s
- mutant_2.py: 4 failed, 8 passed in 0.07s
- mutant_3.py: 1 failed, 11 passed in 0.07s
- mutant_hollow_main.py: 1 failed, 11 passed in 0.07s
- solution.py: 12 passed in 0.10s
- equivalent_banner.py: 12 passed in 0.14s
- equivalent_footer.py: 12 passed in 0.16s

自动分 20.2 → 19.2；占比 80.80% → 76.80%。

## 9618_s22_42_q3

原通过 runpy 验证 Player1 状态但没有真测 ChooseCard/getter 调用；新增四次选择返回下标与 getter 输出链。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：3 failed, 3 passed in 0.15s；修后与等价改写：

- mutant_1.py: 2 failed, 5 passed in 0.14s
- mutant_2.py: 4 failed, 3 passed in 0.11s
- mutant_hollow_main.py: 4 failed, 3 passed in 0.09s
- solution.py: 7 passed in 0.09s
- equivalent_banner.py: 7 passed in 0.09s
- equivalent_footer.py: 7 passed in 0.09s

自动分 22.3 → 22.3；占比 82.59% → 82.59%。

## 9618_s23_41_q2

整段数字相等误拒说明数字，改为按所需值顺序匹配。主程序增加父/子构造参数、两次加速与输出调用观测；构造继承补核保持人工注释。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：1 failed, 7 passed in 0.05s；修后与等价改写：

- mutant_1.py: 1 failed, 7 passed in 0.06s
- mutant_2.py: 3 failed, 5 passed in 0.07s
- mutant_hollow_main.py: 1 failed, 7 passed in 0.06s
- solution.py: 8 passed in 0.07s
- equivalent_banner.py: 8 passed in 0.08s
- equivalent_footer.py: 8 passed in 0.13s

自动分 26.0 → 26.0；占比 81.25% → 81.25%。

## 9618_s23_42_q3

工资截图原将全段数字两两组装，额外说明数字会误拒。改为每个已知 ID 后查工资值，允许换行。新增 EnterHours/getter/父构造调用。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：1 failed, 9 passed in 0.12s；修后与等价改写：

- mutant_1.py: 3 failed, 8 passed in 0.11s
- mutant_2.py: 4 failed, 7 passed in 0.21s
- mutant_hollow_main.py: 2 failed, 9 passed in 0.11s
- solution.py: 11 passed in 0.10s
- equivalent_banner.py: 11 passed in 0.10s
- equivalent_footer.py: 11 passed in 0.11s

自动分 27.0 → 27.0；占比 81.82% → 81.82%。

## 9618_s24_42_q2

主程序只核对数字，新增 InsertNode 七次 Node 参数顺序和 OutputTree/getter。输出数字改子序列；No nodes 允许附带说明。20 格为 QP 明确容量，保持。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：1 failed, 7 passed in 0.14s；修后与等价改写：

- mutant_1.py: 1 failed, 8 passed in 0.11s
- mutant_2.py: 5 failed, 4 passed in 0.10s
- mutant_hollow_main.py: 2 failed, 7 passed in 0.10s
- solution.py: 9 passed in 0.07s
- equivalent_banner.py: 9 passed in 0.07s
- equivalent_footer.py: 9 passed in 0.07s

自动分 23.142857 → 23.1429；占比 77.14% → 77.14%。

## 9618_s25_41_q3

runpy 树结构正确仍不证明 Insert/OutputInOrder 调用；补 Node 参数顺序与 root 返回对象传递。截图/递归输出允许说明数字。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：1 failed, 5 passed in 0.08s；修后与等价改写：

- mutant_1.py: 6 failed, 1 passed in 0.14s
- mutant_2.py: 2 failed, 5 passed in 0.09s
- mutant_hollow_main.py: 2 failed, 5 passed in 0.06s
- solution.py: 7 passed in 0.06s
- equivalent_banner.py: 7 passed in 0.06s
- equivalent_footer.py: 7 passed in 0.07s

自动分 23.0 → 23.0；占比 76.67% → 76.67%。

## 9618_s25_42_q3

补参数化动物构造、父构造、领地/词数更新与 Description 返回输出。QP 明确描述字符串保持；完整输出允许附加说明/相邻换行。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：4 passed in 0.09s；修后与等价改写：

- mutant_1.py: 2 failed, 3 passed in 0.14s
- mutant_2.py: 2 failed, 3 passed in 0.10s
- mutant_hollow_main.py: 1 failed, 4 passed in 0.13s
- solution.py: 5 passed in 0.09s
- equivalent_banner.py: 5 passed in 0.09s
- equivalent_footer.py: 5 passed in 0.07s

自动分 22.0 → 22.0；占比 84.62% → 84.62%。

## 9618_s25_43_q3

补五次 InsertNode、RemoveNode(30)、前后 Traverse 返回输出顺序与 SetNextNode；截图数字改子序列。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：9 passed in 0.09s；修后与等价改写：

- mutant_1.py: 1 failed, 9 passed in 0.12s
- mutant_2.py: 3 failed, 7 passed in 0.16s
- mutant_3.py: 1 failed, 9 passed in 0.09s
- mutant_hollow_main.py: 1 failed, 9 passed in 0.09s
- solution.py: 10 passed in 0.08s
- equivalent_banner.py: 10 passed in 0.08s
- equivalent_footer.py: 10 passed in 0.08s

自动分 22.0 → 22.0；占比 75.86% → 75.86%。

## 9618_w22_41_q2

补两次 CalculateValue 及各手牌参数、返回分数；比较使用返回值的代码关系无法仅从固定赢家证明，2(c)(ii) MP3 归人工（截图仍自动）。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：1 failed, 7 passed in 0.18s；修后与等价改写：

- mutant_1.py: 3 failed, 6 passed in 0.12s
- mutant_2.py: 1 failed, 8 passed in 0.09s
- mutant_hollow_main.py: 2 failed, 7 passed in 0.10s
- solution.py: 9 passed in 0.10s
- equivalent_banner.py: 9 passed in 0.10s
- equivalent_footer.py: 9 passed in 0.09s

自动分 23.0 → 22.0；占比 74.19% → 70.97%。

## 9618_w22_42_q2

主程序调用点原只匹配坐标；补实际 ChangePosition 参数与三个 getter。QP 给出消息格式，保留 X/Y 标识，允许相邻行。另四方向另测。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：4 failed, 6 passed in 0.33s；修后与等价改写：

- mutant_1.py: 5 failed, 6 passed in 0.44s
- mutant_2.py: 9 failed, 2 passed in 0.68s
- mutant_hollow_main.py: 5 failed, 6 passed in 0.33s
- solution.py: 11 passed in 0.30s
- equivalent_banner.py: 11 passed in 0.32s
- equivalent_footer.py: 11 passed in 0.26s

自动分 26.2222 → 26.2222；占比 84.59% → 84.59%。

## 9618_w23_41_q3

补 Move 的输入参数和位置 getter 真实调用；X/Y 输出允许换行；父构造原有 spy 已测。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：2 failed, 14 passed in 0.17s；修后与等价改写：

- mutant_1.py: 1 failed, 16 passed in 0.18s
- mutant_2.py: 2 failed, 15 passed in 0.26s
- mutant_hollow_main.py: 3 failed, 14 passed in 0.20s
- solution.py: 17 passed in 0.16s
- equivalent_banner.py: 17 passed in 0.24s
- equivalent_footer.py: 17 passed in 0.18s

自动分 23.0 → 23.0；占比 76.67% → 76.67%。

## 9618_w23_42_q3

截图数值可由空壳伪造，补 Learn/ReturnAge/getter 及返回值输出；输出本已容许换行。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：2 failed, 13 passed in 0.14s；修后与等价改写：

- mutant_1.py: 7 failed, 8 passed in 0.15s
- mutant_2.py: 5 failed, 10 passed in 0.24s
- mutant_hollow_main.py: 2 failed, 13 passed in 0.17s
- solution.py: 15 passed in 0.15s
- equivalent_banner.py: 15 passed in 0.11s
- equivalent_footer.py: 15 passed in 0.11s

自动分 23.0 → 23.0；占比 74.19% → 74.19%。

## 9618_w24_41_q2

补八次 Success 的 Fence 高度/风险参数、getter 与计算结果输出；赢家从整段输出识别，不再要求最后一行。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：3 failed, 19 passed in 0.26s；修后与等价改写：

- mutant_1.py: 5 failed, 18 passed in 0.24s
- mutant_2.py: 1 failed, 22 passed in 0.18s
- mutant_hollow_main.py: 4 failed, 19 passed in 0.21s
- solution.py: 23 passed in 0.17s
- equivalent_banner.py: 23 passed in 0.23s
- equivalent_footer.py: 23 passed in 0.16s

自动分 30.0 → 30.0；占比 88.24% → 88.24%。

## 9618_w24_42_q1

新增五场两人 CalculateScore 及 getter 参数；固定数据难证明比较直接使用返回分数，MP3 归人工。赢家/总分检查允许说明和换行。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：1 failed, 28 passed in 0.12s；修后与等价改写：

- mutant_1.py: 4 failed, 26 passed in 0.11s
- mutant_2.py: 1 failed, 29 passed in 0.09s
- mutant_hollow_main.py: 2 failed, 28 passed in 0.13s
- solution.py: 30 passed in 0.10s
- equivalent_banner.py: 30 passed in 0.09s
- equivalent_footer.py: 30 passed in 0.07s

自动分 23.2 → 22.2；占比 80.00% → 76.55%。

## 9618_w25_41_q2

新增 AddTrain 四次参数及成功/满站返回值、两站 GetTrains 返回输出；QP 格式保留，截图允许相邻行组合。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：1 failed, 6 passed in 0.08s；修后与等价改写：

- mutant_1.py: 3 failed, 5 passed in 0.08s
- mutant_2.py: 4 failed, 4 passed in 0.09s
- mutant_hollow_main.py: 2 failed, 6 passed in 0.08s
- solution.py: 8 passed in 0.06s
- equivalent_banner.py: 8 passed in 0.07s
- equivalent_footer.py: 8 passed in 0.06s

自动分 25.0 → 25.0；占比 83.33% → 83.33%。

## 9618_w25_43_q1

新增 SetObject 各坐标、DisplayBoard/GetCode、输入坐标 GetObject 和返回对象 getter；QP 棋盘逐行格式保持，命中消息允许分行。

本轮用该题自己的 MS 得分点逐项核对调用/输出分类；本轮实际原页查阅清单见末节（原 T35 的完整页表仍保留在 README）。hollow-main 修前：6 failed, 10 passed in 0.37s；修后与等价改写：

- mutant_1.py: 9 failed, 8 passed in 0.57s
- mutant_2.py: 1 failed, 16 passed in 0.36s
- mutant_hollow_main.py: 7 failed, 10 passed in 0.31s
- solution.py: 17 passed in 0.33s
- equivalent_banner.py: 17 passed in 0.34s
- equivalent_footer.py: 17 passed in 0.28s

自动分 22.0 → 22.0；占比 70.97% → 70.97%。

## 最终自审与运行汇总

新增调用测试全部包含对应小问号，供 D47 的 K= 局部掌握判断使用。w22/42 的 ChangePosition 四个分支、w23/41 的两角色调用已真测；PrintTrees / OutputTree 的 getter 调用另由单元 spy 观察。s23/41 超速测试接受本题 MS p.17 的 remove increase / assign maximum，两种速度策略都累计实际更新速度。主程序输出的说明数字、尾注与相邻换行不再决定算法正误。

本轮读取全部 18 题本题配对的语料 MS 原文及已有测试；另从只读原件提取/核对主程序 QP 页面：s22/41 p.7、s22/42 p.8、s23/41 p.7、s23/42 p.12、s24/41 pp.7–10、s24/42 p.9、s25/41 p.9、s25/42 p.12、s25/43 p.10、w22/41 p.7、w22/42 p.7、w23/41 p.11、w23/42 p.13、w24/41 p.10、w24/42 p.7、w25/41 p.8、w25/42 pp.3,5、w25/43 p.8。

已实际看过渲染 MS 原页：s22/41 p.26、s22/42 p.34、s23/41 pp.17,24、s23/42 pp.28,36、s24/41 pp.18,22、s24/42 p.26、s25/41 p.41、s25/42 p.44、s25/43 p.43、w22/41 p.15、w22/42 p.18、w23/41 p.35、w23/42 pp.29,30、w24/41 p.21、w24/42 p.13、w25/41 p.23、w25/42 p.12、w25/43 pp.15,17。渲染图片在 `/tmp/T38c3/`；不把“已提取/渲染”当作“已人工看图”，未列页不声称本轮重审。

| 练习 | 当前用例 | mutant | 等价候选 | 参考解 / 等价候选 | 全部 mutant |
|:--|--:|--:|--:|:--|:--|
| 9618_s22_41_q2 | 12 | 4 | 2 | 全过 | 各至少一测失败 |
| 9618_s22_42_q3 | 7 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_s23_41_q2 | 8 | 3 | 3 | 全过 | 各至少一测失败 |
| 9618_s23_42_q3 | 11 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_s24_41_q2 | 9 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_s24_42_q2 | 9 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_s25_41_q3 | 7 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_s25_42_q3 | 5 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_s25_43_q3 | 10 | 4 | 2 | 全过 | 各至少一测失败 |
| 9618_w22_41_q2 | 9 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_w22_42_q2 | 14 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_w23_41_q3 | 18 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_w23_42_q3 | 15 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_w24_41_q2 | 23 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_w24_42_q1 | 30 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_w25_41_q2 | 8 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_w25_42_q1 | 31 | 3 | 2 | 全过 | 各至少一测失败 |
| 9618_w25_43_q1 | 17 | 3 | 2 | 全过 | 各至少一测失败 |

临时候选及逐次 pytest 输出：`/tmp/T38c3/<练习>/equivalent*.py`、`*-review.log`；结构化本轮记录 `/tmp/T38c3/final-unit-runs.json`。所有候选通过共享 venv 的 `python -m pytest -q <练习>/test_task.py` 配 `CANDIDATE=<候选绝对路径>` 实际运行。通常两份候选分别在主程序增加 Question N 说明和 End of question N 尾注；F08 为 20 格容量与尾注；F09 为 species/坐标分行与 X/Y 分行；s23/41 另有撤销速度增量实现。

人工分值变化：s22/41 Q2 的 2(g)(i) MP2、w22/41 Q2 的 2(c)(ii) MP3、w24/42 Q1 的 1(e)(ii) MP3 各 1 分从自动归回人工；各自 task 表与 manifest 已同步，相关返回赋值/比较使用关系由导师查看代码。调用本身已经观测，不能用固定输出倒推上述关系。其余题自动占比维持。

- T35e：自动 212.6429/263（80.85%），人工 50.3571。
- T35f：自动 217.4222/275（79.06%），人工 57.5778。
- 总计：18 题 / 165 格 / 538 分；243 个参数化用例，56 个 mutant，其中 hollow-main 18 个；自动 430.0651/538（79.94%）。

需要总控决定：无共享文件修改请求；请验收以上三处保守归人工分类。traced 不记录 self 且返回值只作浅拷贝，接收对象身份/代码赋值及因果关系仍需结合现有状态测试和人工清单，不宣称自动授予整道题的考试分数。
