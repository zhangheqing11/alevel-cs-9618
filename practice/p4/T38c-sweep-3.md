# T38c3 · T35e + T35f 逐题排查

按 D46/D31 核验自动调用点与输出约束。运行使用共享 venv。临时等价候选和原页在 `/tmp/T38c3/`，不入库。调用身份、结构及未观测的返回赋值仍需人工检查；自动覆盖不是考试自动授分。

## 9618_s24_41_q2

F08：MS p.18 明确 min 9，改测至少 9 格及前九对象；20 格等价候选修前 1 failed/7 passed，修后全过。QP pp.7–10、MS p.18 与 pp.21,28 调用点核对。 新增真实调用、参数与返回输出检查；hollow-main 保留正确模块、主程序仅输出参考结果。自动占比暂保持原值，最终分类复核见后续汇总。

- mutant_1.py: 1 failed, 8 passed in 0.16s
- mutant_2.py: 2 failed, 7 passed in 0.12s
- mutant_hollow_main.py: 1 failed, 8 passed in 0.14s
- solution.py: 9 passed in 0.32s
- equivalent.py: 9 passed in 0.15s
