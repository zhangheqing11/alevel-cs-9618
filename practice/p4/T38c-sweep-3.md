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
