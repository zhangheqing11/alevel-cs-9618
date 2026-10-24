# T38c2 · P4 练习逐题复核

19 道大题、136 行、447 分；只修改 T38c2 scope。基线 origin/main `5effaee`，含 #57 / D46 / D47。使用共享 venv，原件严格只读。

自动分表示测试真正覆盖的行为；消息含义、未触发选择分支和结构检查归人工，不以截图值推定调用。原 T35 的所有源文件 SHA 保留。

## 覆盖变化

| 练习 | 自动分（原 → 新） | 人工分 | 自动占比（原 → 新） |
|:--|--:|--:|--:|
| 9618_s22_41_q3 | 18.142857 → 16.142857 | 4.857143 | 86.39% → 76.87% |
| 9618_s22_42_q1 | 23.000000 → 20.000000 | 5.000000 | 92.00% → 80.00% |
| 9618_s23_41_q3 | 24.000000 → 24.000000 | 1.000000 | 96.00% → 96.00% |
| 9618_s23_42_q2 | 24.000000 → 23.200000 | 4.800000 | 85.71% → 82.86% |
| 9618_s24_41_q3 | 17.000000 → 16.250000 | 0.750000 | 100.00% → 95.59% |
| 9618_s25_41_q1 | 20.000000 → 19.000000 | 1.000000 | 100.00% → 95.00% |
| 9618_s25_42_q1 | 24.000000 → 24.000000 | 3.000000 | 88.89% → 88.89% |
| 9618_s25_42_q2 | 18.166667 → 18.166667 | 3.833333 | 82.58% → 82.58% |
| 9618_s25_43_q1 | 24.000000 → 24.000000 | 2.000000 | 92.31% → 92.31% |
| 9618_w22_41_q3 | 19.000000 → 18.000000 | 3.000000 | 90.48% → 85.71% |
| 9618_w22_42_q3 | 19.000000 → 19.000000 | 2.000000 | 90.48% → 90.48% |
| 9618_w23_41_q2 | 23.485700 → 23.485714 | 5.514286 | 80.99% → 80.99% |
| 9618_w23_42_q1 | 24.000000 → 24.000000 | 3.000000 | 88.89% → 88.89% |
| 9618_w24_41_q3 | 18.375000 → 18.375000 | 0.625000 | 96.71% → 96.71% |
| 9618_w24_42_q2 | 26.000000 → 23.000000 | 6.000000 | 89.66% → 79.31% |
| 9618_w25_41_q1 | 19.000000 → 19.000000 | 1.000000 | 95.00% → 95.00% |
| 9618_w25_41_q3 | 22.166700 → 22.166667 | 2.833333 | 88.67% → 88.67% |
| 9618_w25_42_q3 | 19.200000 → 19.200000 | 1.800000 | 91.43% → 91.43% |
| 9618_w25_43_q2 | 22.333300 → 22.333333 | 1.666667 | 93.06% → 93.06% |

## 9618_s22_41_q3

补测 11 次 Enqueue 的输入参数/返回状态与 2 次 Dequeue；移除 13 行及状态文字完全相同的额外限制（QP p.10/MS pp.32/34）。合适消息语义及按返回值选择消息改列人工补核。 截图的适当消息语义不可自动判别，截图整行列人工，A/B 输出测试作为行为辅助。

- 调用观测：`test_3d_main_call_chain`。
- 参考解：7 passed in 0.09s；全部 3 个 mutant 各至少一项失败，hollow-main 为 1 failed, 6 passed in 0.15s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_s22_42_q1

补测 Push(11..21) → PrintArray → Pop 两次 → PrintArray；输出允许说明数字、指针前后顺序及 MS 三种清槽方案（QP p.3/MS pp.5/8/10/12）。合适消息语义及按返回值分支改列人工补核。 截图的适当消息语义不可自动判别，1(d)(ii) 整行列人工。

- 调用观测：`test_1d_1e_main_call_chain`。
- 参考解：8 passed in 0.18s；全部 3 个 mutant 各至少一项失败，hollow-main 为 1 failed, 7 passed in 0.22s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_s23_41_q3

补测 ReadData 与四次 OutputItem（含实际双栈 Pop）；截图允许额外说明行。QP 明定配对一行的规则保留（QP pp.9–10/MS p.38）。 OutputItem 也允许额外说明行，配对本身仍在一行。

- 调用观测：`test_3d_main_call_chain`。
- 参考解：13 passed in 0.28s；全部 3 个 mutant 各至少一项失败，hollow-main 为 1 failed, 12 passed in 0.43s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_s23_42_q2

补测六次 EnterRecord → Dequeue → 第七次 EnterRecord 及记录参数、状态、返回记录输出；ID/数量允许说明和换行（QP p.7/MS pp.20/22）。固定输入不触发空记录分支，MP3 的空分支归人工补核。

- 调用观测：`test_2f_main_call_chain`。
- 参考解：8 passed in 0.12s；全部 3 个 mutant 各至少一项失败，hollow-main 为 1 failed, 7 passed in 0.18s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_s24_41_q3

补测 StoreItems → Dequeue 一次及返回项目输出；计数和项目输出不再固定倒数两行，允许相邻多行说明（QP p.13/MS pp.37–38）。 StoreItems 计数输出不固定末行；适当消息语义 MP7 改人工。

- 调用观测：`test_3d_main_call_chain`。
- 参考解：9 passed in 0.59s；全部 3 个 mutant 各至少一项失败，hollow-main 为 2 failed, 7 passed in 0.29s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_s25_41_q1

补测 Enqueue(1..25) 与两次 Dequeue 的返回值；取消固定 27 行，整数和 Successful/Unsuccessful 可分相邻行（QP p.3/MS pp.12/16）。返回值用于选择的代码分支由人工补核。

- 调用观测：`test_1c_1e_main_call_chain`。
- 参考解：7 passed in 0.19s；全部 3 个 mutant 各至少一项失败，hollow-main 为 1 failed, 6 passed in 0.13s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_s25_42_q1

F06：复现空壳主程序旧测试 17 passed；新增三份文件 ReadData(FileName) → Calculate → 返回值输出观测（含新数据 17），输出允许额外数字说明。复核 QP p.5、MS p.17 原页。

- 调用观测：`test_1f_main_call_chain`。
- 参考解：20 passed in 0.12s；全部 3 个 mutant 各至少一项失败，hollow-main 为 3 failed, 17 passed in 0.23s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_s25_42_q2

补测 Initialise → CreateHashTable → PrintSpare；PrintSpare 和截图的整段数字严格相等改为键值有序包含，允许题号/说明数字（QP p.8/MS pp.30–32）。固定 200/100 容量由 QP 指定，保留。

- 调用观测：`test_2f_ii_main_call_chain`。
- 参考解：17 passed in 0.23s；全部 3 个 mutant 各至少一项失败，hollow-main 为 1 failed, 16 passed in 0.20s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_s25_43_q1

补测 CreateQueue 调用及到 -1 的 Dequeue 总和；官方 3059 与新文件 27 双数据验证返回值使用，输出不固定最后一个数字（QP p.3/MS pp.17–18）。原有 Dequeue 观察保留。

- 调用观测：`test_1e_main_call_chain`。
- 参考解：9 passed in 0.23s；全部 3 个 mutant 各至少一项失败，hollow-main 为 2 failed, 7 passed in 0.32s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_w22_41_q3

补测 SearchValue 的根/15 参数、返回下标及 PostOrder 根结点；遍历与截图允许说明数字（QP pp.10–11/MS pp.21–23）。固定示例未触发的 not-found 消息仍人工补核。 固定主程序未触发 not-found 分支，3(e)(i) MP2 整点改人工。

- 调用观测：`test_3e_main_call_chain`。
- 参考解：17 passed in 0.16s；全部 3 个 mutant 各至少一项失败，hollow-main 为 1 failed, 16 passed in 0.18s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_w22_42_q3

原有注入一次失败的测试已观测 Enqueue；补测 RecursiveOutput(19) 调用及返回总和，210 输出允许后续说明数字（QP pp.8–9/MS pp.22–24）。

- 调用观测：`test_3c_3e_main_call_chain`。
- 参考解：6 passed in 0.23s；全部 4 个 mutant 各至少一项失败，hollow-main 为 2 failed, 4 passed in 0.15s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_w23_41_q2

补测 ReadData → 每项 TotalData → OutputRecords 的调用和实际 Dequeue 返回；原有 ID/Total 格式为 QP 明定，保留（QP pp.6–7/MS pp.22–24）。复核 MS p.9 minimum 50：数组允许至少 50 格，80 格的等价改写通过；QP 逻辑容量可保持 50 或随分配扩大；两种 80 格正确改写均通过。

- 调用观测：`test_2e_main_call_chain`。
- 参考解：9 passed, 1 warning in 1.19s；全部 4 个 mutant 各至少一项失败，hollow-main 为 1 failed, 8 passed in 0.28s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_w23_42_q1

补测 ReadData、按五个选择对应 Pop 的顺序与实际返回字母串；保留 QP 要求字母串一行，取消必须为最后一行的限制（QP p.4/MS pp.13–16）。原有空栈重选测试保留。

- 调用观测：`test_1d_main_call_chain`。
- 参考解：8 passed in 0.30s；全部 4 个 mutant 各至少一项失败，hollow-main 为 2 failed, 6 passed in 0.31s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_w24_41_q3

F07：复现空壳主程序旧测试 11 passed；新增三组数据 InsertData → OutputLinkedList → RemoveData(5) → OutputLinkedList 顺序/参数/输出观测；数据输出改为顺序包含。复核 QP pp.14–15、MS pp.32/36 原页。trace 前先限时执行，拒绝产生死循环的错误链表。补核 MS p.26 min 20×2，接受额外分配但逻辑链仍用前 20 结点；25×3 等价正确数组通过。

- 调用观测：`test_3c_ii_3d_ii_main_call_chain`。
- 参考解：14 passed in 0.56s；全部 4 个 mutant 各至少一项失败，hollow-main 为 3 failed, 11 passed in 0.57s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_w24_42_q2

补测 10 次有效 Enqueue（拒绝 -1）→ ReturnAllData → 两次 Dequeue → ReturnAllData；只保留 QP/MS 明定的一行队列格式，取消返回信息同一行、最终必须输出剩余数组的额外要求（QP pp.10–11/MS pp.23/26/28/30）。B 分行显示返回信息且只调用第二次 ReturnAllData；未触发的 full/empty 分支归人工。 2(e)(ii) MP1 中消息含义归人工；十个有效值的调用仍自动观察。

- 调用观测：`test_2e_2g_main_call_chain`。
- 参考解：9 passed in 1.39s；全部 4 个 mutant 各至少一项失败，hollow-main 为 4 failed, 5 passed in 0.97s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_w25_41_q1

原有种子/Push 观察已验证随机范围及首次失败停止；新增 FindValues 实际调用、Pop 值链与极值输出。允许说明文字提及 -999，不能据此认定把哨兵当结果（QP p.3/MS pp.11–14）。固定 30 格由 QP 指定。 新增 trace 使用固定种子并恢复主进程随机状态。

- 调用观测：`test_1d_1f_main_call_chain`。
- 参考解：9 passed in 0.35s；全部 4 个 mutant 各至少一项失败，hollow-main 为 2 failed, 7 passed in 0.30s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_w25_41_q3

补测 InitialiseHashTable → ReadData → 五次 GetRecord 的整数参数与有序返回字符串；原有输出已允许额外说明，容量为 QP 明定，无放宽项（QP p.12/MS pp.35–36）。

- 调用观测：`test_3g_main_call_chain`。
- 参考解：9 passed in 0.28s；全部 4 个 mutant 各至少一项失败，hollow-main 为 1 failed, 8 passed in 0.42s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_w25_42_q3

原有 AddNode 包装已观测输入调用；新增 WriteAllToFile 实际调用并核对生成文件。空壳保留模块但直接写出完整正确 Tree.txt，仍被调用测试拒绝。文件三字段/每结点一行是 QP 明定，保留（QP pp.11–12/MS pp.33/37–38）。

- 调用观测：`test_3c_3e_main_call_chain`。
- 参考解：9 passed in 1.41s；全部 4 个 mutant 各至少一项失败，hollow-main 为 2 failed, 7 passed in 0.72s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 9618_w25_43_q2

补测 ReadData → Compress 以及实际 Dequeue 字符，官方 19051306 与新数据 120313 双数据验证输出；取消固定末行/行尾，压缩串本身仍完整（QP pp.10–11/MS pp.28–31）。

- 调用观测：`test_2f_main_call_chain`。
- 参考解：18 passed in 0.45s；全部 4 个 mutant 各至少一项失败，hollow-main 为 1 failed, 17 passed in 19.23s。
- 正确等价 A：主程序额外打印带题号说明；B：提取 `main()`，并在适用题中分行输出、增加数组分配或省去 QP 未要求的第二次返回值输出。两版全过，详见下方运行表。

## 运行证据

临时正确版本、修改辅助脚本、原页渲染和完整 pytest 日志位于 `/tmp/T38c2/`，不入库。文件名 `<练习>-equivalent-a.py` / `-equivalent-b.py`，对应运行结果在 `<练习>-results.json`。每个测试 docstring 标注同题 MS 行；固定随机 trace 保存/恢复 PRNG 状态。完整验收结果在交付进度和 PR 补记。

| 练习 | 参考解 | 正确 A | 正确 B | hollow-main | 全部 mutant 数 |
|:--|:--|:--|:--|:--|--:|
| 9618_s22_41_q3 | 7 passed in 0.09s | 7 passed in 0.12s | 7 passed in 0.12s | 1 failed, 6 passed in 0.15s | 3 |
| 9618_s22_42_q1 | 8 passed in 0.18s | 8 passed in 0.21s | 8 passed in 0.20s | 1 failed, 7 passed in 0.22s | 3 |
| 9618_s23_41_q3 | 13 passed in 0.28s | 13 passed in 0.31s | 13 passed in 0.30s | 1 failed, 12 passed in 0.43s | 3 |
| 9618_s23_42_q2 | 8 passed in 0.12s | 8 passed in 0.13s | 8 passed in 0.13s | 1 failed, 7 passed in 0.18s | 3 |
| 9618_s24_41_q3 | 9 passed in 0.59s | 9 passed in 0.28s | 9 passed in 0.24s | 2 failed, 7 passed in 0.29s | 3 |
| 9618_s25_41_q1 | 7 passed in 0.19s | 7 passed in 0.11s | 7 passed in 0.12s | 1 failed, 6 passed in 0.13s | 3 |
| 9618_s25_42_q1 | 20 passed in 0.12s | 20 passed in 0.12s | 20 passed in 0.14s | 3 failed, 17 passed in 0.23s | 3 |
| 9618_s25_42_q2 | 17 passed in 0.23s | 17 passed in 0.28s | 17 passed in 0.25s | 1 failed, 16 passed in 0.20s | 3 |
| 9618_s25_43_q1 | 9 passed in 0.23s | 9 passed in 0.27s | 9 passed in 0.33s | 2 failed, 7 passed in 0.32s | 3 |
| 9618_w22_41_q3 | 17 passed in 0.16s | 17 passed in 0.18s | 17 passed in 0.15s | 1 failed, 16 passed in 0.18s | 3 |
| 9618_w22_42_q3 | 6 passed in 0.23s | 6 passed in 0.19s | 6 passed in 0.19s | 2 failed, 4 passed in 0.15s | 4 |
| 9618_w23_41_q2 | 9 passed, 1 warning in 1.19s | 9 passed in 0.51s | 9 passed in 0.80s | 1 failed, 8 passed in 0.28s | 4 |
| 9618_w23_42_q1 | 8 passed in 0.30s | 8 passed in 0.21s | 8 passed in 0.36s | 2 failed, 6 passed in 0.31s | 4 |
| 9618_w24_41_q3 | 14 passed in 0.56s | 14 passed in 0.69s | 14 passed in 0.48s | 3 failed, 11 passed in 0.57s | 4 |
| 9618_w24_42_q2 | 9 passed in 1.39s | 9 passed in 0.58s | 9 passed in 0.55s | 4 failed, 5 passed in 0.97s | 4 |
| 9618_w25_41_q1 | 9 passed in 0.35s | 9 passed in 0.32s | 9 passed in 0.41s | 2 failed, 7 passed in 0.30s | 4 |
| 9618_w25_41_q3 | 9 passed in 0.28s | 9 passed in 0.31s | 9 passed in 0.23s | 1 failed, 8 passed in 0.42s | 4 |
| 9618_w25_42_q3 | 9 passed in 1.41s | 9 passed in 1.02s | 9 passed in 0.77s | 2 failed, 7 passed in 0.72s | 4 |
| 9618_w25_43_q2 | 18 passed in 0.45s | 18 passed in 0.76s | 18 passed in 0.49s | 1 failed, 17 passed in 19.23s | 4 |

## 官方数据副本

- 9618_s23_41_q3/AnimalData.txt：SHA-256 `4c77f71887d5f912588f905f6e0023b027e2d9e6b87cc7ccb3177415437ed27f`，与只读原件逐字节一致。
- 9618_s23_41_q3/ColourData.txt：SHA-256 `b191a9e0f24c4131952f0f6242ae9ea8c76abf4ddd702cc4d6370b622c1c8893`，与只读原件逐字节一致。
- 9618_s25_42_q1/StackData.txt：SHA-256 `ea1c31f3a9ec7c5489c6e13b5749d869d295a92943bfdc42cf69376a04ba6c3b`，与只读原件逐字节一致。
- 9618_s25_42_q1/SecondStack.txt：SHA-256 `c8115e35b133ccea75bcf10e2f3184970c3619982ec25459f68a129827f59e16`，与只读原件逐字节一致。
- 9618_s25_42_q2/HashData.txt：SHA-256 `4c25e6d9c4b975d826d4d4aec5acba8c64535d54a654a8209c31a61c57d87c2f`，与只读原件逐字节一致。
- 9618_s25_43_q1/QueueData.txt：SHA-256 `9576e3e73ccf62362e05e12d40f2e99e4456984e745b2591b8c06bcaa34a29a5`，与只读原件逐字节一致。
- 9618_w23_41_q2/QueueData.txt：SHA-256 `9b4b28747275120bd9c4de28aeab68e1363a1eee3312cb2c99023b94390ce972`，与只读原件逐字节一致。
- 9618_w23_42_q1/StackData.txt：SHA-256 `eb72f3638b6437f63f4dda83943f4882f6c12f96a8f59cfde9909a1f199d09e1`，与只读原件逐字节一致。
- 9618_w25_41_q3/HashTableData.txt：SHA-256 `922b71fc41586e22993821383b1f017610ee23da881b8eb2756cae0f95cb6617`，与只读原件逐字节一致。
- 9618_w25_42_q3/TreeData.txt：SHA-256 `883d863da0888afc902c28bb87b8f039e07d632c6052bff2c28c68eeec2cab93`，与只读原件逐字节一致。
- 9618_w25_43_q2/BinaryData.txt：SHA-256 `b01a6bdb86b953c8acb8f3c84ed1d85d7250010a9456ca3ae9efea24cd509ded`，与只读原件逐字节一致。

## 已知限制与需要总控决定

- 本次对若干消息语义和未触发分支保守归人工，自动占比下降；请总控验收此分类。没有共享工具/schema 修改请求。
- `run_script_traced` 本身没有超时；新调用测试先作限时子进程预检，避免已知坏链表进入无界 trace。工具增强由总控另行决定，本任务不改 tools。
- w24/42 Q2 的第二次 ReturnAllData 只要求调用；正确版本可不打印该次结果。本次测试按 QP p.10 / MS p.28 放宽，请验收。
