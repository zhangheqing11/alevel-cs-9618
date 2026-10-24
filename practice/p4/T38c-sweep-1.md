# T38c1 · T35a + T35b 的 17 题 D46 排查

基线 origin/main `5effaee67bc2c8d3c302725e2bf2ed821af7a5d1`，包含 #57、D46、D47。逐题按同卷 QP/MS 核对，不修改原件。运行记录和等价版本位于 `/tmp/T38c1/`，不入库。

## 9618_s24_42_q3

F05：取消整个输出段数字严格相等；按 Recursive / Iterative 段匹配有序子序列，允许 Question 3 等数字说明及逐项换行。补查 BinarySearch 的真实调用、排好数组/0/6/644 参数及返回值；保留两个排序入口原始顺序检查。

- 调用观测：`test_3bii_cii_dii_traced_calls_and_results`。
- 原件：QP pp.10–13；MS pp.32、36、39（p.32 原图已查看）。
- hollow-main：保留参考模块，主程序只硬编码原参考输出；测试失败。
- 等价改写：主程序增加数字说明；主程序提取为 main()（必要时保留 global）。 两个版本均全过。
- 运行：27 passed in 0.22s；5 个 mutant 各至少一测失败。
- 占比：自动/人工分类不变，增加实际观测以支撑原自动声明；混合点中的结构/变量存储仍人工补核。

