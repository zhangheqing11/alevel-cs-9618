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

本轮逐行核对本题配对 MS（19, 20, 21, 22, 23, 24, 25, 26 页）中的调用/输出点，QP 要求以题面转写及原 PDF 为准。hollow-main 修前：11 passed in 0.05s；修后与等价改写：

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

本轮逐行核对本题配对 MS（25, 27, 28, 29, 31, 32, 34, 35, 36 页）中的调用/输出点，QP 要求以题面转写及原 PDF 为准。hollow-main 修前：3 failed, 3 passed in 0.15s；修后与等价改写：

- mutant_1.py: 2 failed, 5 passed in 0.14s
- mutant_2.py: 4 failed, 3 passed in 0.11s
- mutant_hollow_main.py: 4 failed, 3 passed in 0.09s
- solution.py: 7 passed in 0.09s
- equivalent_banner.py: 7 passed in 0.09s
- equivalent_footer.py: 7 passed in 0.09s

自动分 22.3 → 22.3；占比 82.59% → 82.59%。

## 9618_s23_41_q2

整段数字相等误拒说明数字，改为按所需值顺序匹配。主程序增加父/子构造参数、两次加速与输出调用观测；构造继承补核保持人工注释。

本轮逐行核对本题配对 MS（12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 页）中的调用/输出点，QP 要求以题面转写及原 PDF 为准。hollow-main 修前：1 failed, 7 passed in 0.05s；修后与等价改写：

- mutant_1.py: 1 failed, 7 passed in 0.06s
- mutant_2.py: 3 failed, 5 passed in 0.07s
- mutant_hollow_main.py: 1 failed, 7 passed in 0.06s
- solution.py: 8 passed in 0.07s
- equivalent_banner.py: 8 passed in 0.08s
- equivalent_footer.py: 8 passed in 0.13s

自动分 26.0 → 26.0；占比 81.25% → 81.25%。

## 9618_s23_42_q3

工资截图原将全段数字两两组装，额外说明数字会误拒。改为每个已知 ID 后查工资值，允许换行。新增 EnterHours/getter/父构造调用。

本轮逐行核对本题配对 MS（23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37 页）中的调用/输出点，QP 要求以题面转写及原 PDF 为准。hollow-main 修前：1 failed, 9 passed in 0.12s；修后与等价改写：

- mutant_1.py: 3 failed, 8 passed in 0.11s
- mutant_2.py: 4 failed, 7 passed in 0.21s
- mutant_hollow_main.py: 2 failed, 9 passed in 0.11s
- solution.py: 11 passed in 0.10s
- equivalent_banner.py: 11 passed in 0.10s
- equivalent_footer.py: 11 passed in 0.11s

自动分 27.0 → 27.0；占比 81.82% → 81.82%。

## 9618_s24_42_q2

主程序只核对数字，新增 InsertNode 七次 Node 参数顺序和 OutputTree/getter。输出数字改子序列；No nodes 允许附带说明。20 格为 QP 明确容量，保持。

本轮逐行核对本题配对 MS（15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27 页）中的调用/输出点，QP 要求以题面转写及原 PDF 为准。hollow-main 修前：1 failed, 7 passed in 0.14s；修后与等价改写：

- mutant_1.py: 1 failed, 8 passed in 0.11s
- mutant_2.py: 5 failed, 4 passed in 0.10s
- mutant_hollow_main.py: 2 failed, 7 passed in 0.10s
- solution.py: 9 passed in 0.07s
- equivalent_banner.py: 9 passed in 0.07s
- equivalent_footer.py: 9 passed in 0.07s

自动分 23.142857 → 23.1429；占比 77.14% → 77.14%。
