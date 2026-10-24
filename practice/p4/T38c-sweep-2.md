# T38c2 · P4 练习逐题复核

范围：T35c + T35d 的 19 道题，447 分。依据 D31/D46；原件只读。所有运行使用共享 venv，等价正确改写与详细运行日志放在 `/tmp/T38c2/`（不入库）。自动占比是行为覆盖，不代替人工给分。

## 9618_s25_42_q1

F06：复现空壳主程序旧测试 17 passed；新增三份文件 ReadData(FileName) → Calculate → 返回值输出观测（含新数据 17），输出允许额外数字说明。复核 QP p.5、MS p.17 原页。

- 调用观测：`test_1f_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：3 failed, 17 passed in 0.23s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：20 passed in 0.12s；全部 3 个 mutant 各至少一测失败。
- 自动/人工：24.000000/3.000000 分，88.89% → 88.89%。

## 9618_w24_41_q3

F07：复现空壳主程序旧测试 11 passed；新增三组数据 InsertData → OutputLinkedList → RemoveData(5) → OutputLinkedList 顺序/参数/输出观测；数据输出改为顺序包含。复核 QP pp.14–15、MS pp.32/36 原页。trace 前先限时执行，拒绝产生死循环的错误链表。

- 调用观测：`test_3c_ii_3d_ii_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：3 failed, 11 passed in 0.23s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：14 passed in 0.28s；全部 4 个 mutant 各至少一测失败。
- 自动/人工：18.375000/0.625000 分，96.71% → 96.71%。

## 9618_s22_41_q3

补测 11 次 Enqueue 的输入参数/返回状态与 2 次 Dequeue；移除 13 行及状态文字完全相同的额外限制（QP p.10/MS pp.32/34）。合适消息语义及按返回值选择消息改列人工补核。

- 调用观测：`test_3d_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：1 failed, 6 passed in 0.15s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：7 passed in 0.09s；全部 3 个 mutant 各至少一测失败。
- 自动/人工：17.142857/3.857143 分，86.39% → 81.63%。

## 9618_s22_42_q1

补测 Push(11..21) → PrintArray → Pop 两次 → PrintArray；输出允许说明数字、指针前后顺序及 MS 三种清槽方案（QP p.3/MS pp.5/8/10/12）。合适消息语义及按返回值分支改列人工补核。

- 调用观测：`test_1d_1e_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：1 failed, 7 passed in 0.22s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：8 passed in 0.18s；全部 3 个 mutant 各至少一测失败。
- 自动/人工：21.000000/4.000000 分，92.00% → 84.00%。

## 9618_s23_41_q3

补测 ReadData 与四次 OutputItem（含实际双栈 Pop）；截图允许额外说明行。QP 明定配对一行的规则保留（QP pp.9–10/MS p.38）。

- 调用观测：`test_3d_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：1 failed, 12 passed in 0.16s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：13 passed in 0.15s；全部 3 个 mutant 各至少一测失败。
- 自动/人工：24.000000/1.000000 分，96.00% → 96.00%。

## 9618_s23_42_q2

补测六次 EnterRecord → Dequeue → 第七次 EnterRecord 及记录参数、状态、返回记录输出；ID/数量允许说明和换行（QP p.7/MS pp.20/22）。固定输入不触发空记录分支，MP3 的空分支归人工补核。

- 调用观测：`test_2f_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：1 failed, 7 passed in 0.18s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：8 passed in 0.12s；全部 3 个 mutant 各至少一测失败。
- 自动/人工：23.200000/4.800000 分，85.71% → 82.86%。

## 9618_s24_41_q3

补测 StoreItems → Dequeue 一次及返回项目输出；计数和项目输出不再固定倒数两行，允许相邻多行说明（QP p.13/MS pp.37–38）。

- 调用观测：`test_3d_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：2 failed, 7 passed in 0.47s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：9 passed in 0.18s；全部 3 个 mutant 各至少一测失败。
- 自动/人工：17.000000/0.000000 分，100.00% → 100.00%。

## 9618_s25_41_q1

补测 Enqueue(1..25) 与两次 Dequeue 的返回值；取消固定 27 行，整数和 Successful/Unsuccessful 可分相邻行（QP p.3/MS pp.12/16）。返回值用于选择的代码分支由人工补核。

- 调用观测：`test_1c_1e_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：1 failed, 6 passed in 0.13s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：7 passed in 0.19s；全部 3 个 mutant 各至少一测失败。
- 自动/人工：19.000000/1.000000 分，100.00% → 95.00%。

## 9618_s25_42_q2

补测 Initialise → CreateHashTable → PrintSpare；PrintSpare 和截图的整段数字严格相等改为键值有序包含，允许题号/说明数字（QP p.8/MS pp.30–32）。固定 200/100 容量由 QP 指定，保留。

- 调用观测：`test_2f_ii_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：1 failed, 16 passed in 0.20s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：17 passed in 0.23s；全部 3 个 mutant 各至少一测失败。
- 自动/人工：18.166667/3.833333 分，82.58% → 82.58%。

## 9618_s25_43_q1

补测 CreateQueue 调用及到 -1 的 Dequeue 总和；官方 3059 与新文件 27 双数据验证返回值使用，输出不固定最后一个数字（QP p.3/MS pp.17–18）。原有 Dequeue 观察保留。

- 调用观测：`test_1e_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：2 failed, 7 passed in 0.32s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：9 passed in 0.23s；全部 3 个 mutant 各至少一测失败。
- 自动/人工：24.000000/2.000000 分，92.31% → 92.31%。

## 9618_w22_41_q3

补测 SearchValue 的根/15 参数、返回下标及 PostOrder 根结点；遍历与截图允许说明数字（QP pp.10–11/MS pp.21–23）。固定示例未触发的 not-found 消息仍人工补核。

- 调用观测：`test_3e_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：1 failed, 16 passed in 0.18s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：17 passed in 0.16s；全部 3 个 mutant 各至少一测失败。
- 自动/人工：19.000000/2.000000 分，90.48% → 90.48%。

## 9618_w22_42_q3

原有注入一次失败的测试已观测 Enqueue；补测 RecursiveOutput(19) 调用及返回总和，210 输出允许后续说明数字（QP pp.8–9/MS pp.22–24）。

- 调用观测：`test_3c_3e_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：2 failed, 4 passed in 0.15s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：6 passed in 0.23s；全部 4 个 mutant 各至少一测失败。
- 自动/人工：19.000000/2.000000 分，90.48% → 90.48%。

## 9618_w23_41_q2

补测 ReadData → 每项 TotalData → OutputRecords 的调用和实际 Dequeue 返回；原有 ID/Total 格式为 QP 明定，保留（QP pp.6–7/MS pp.22–24）。没有容量 min/恰好冲突。

- 调用观测：`test_2e_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：1 failed, 8 passed in 2.29s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：9 passed in 0.13s；全部 4 个 mutant 各至少一测失败。
- 自动/人工：23.485714/5.514286 分，80.99% → 80.99%。

## 9618_w23_42_q1

补测 ReadData、按五个选择对应 Pop 的顺序与实际返回字母串；保留 QP 要求字母串一行，取消必须为最后一行的限制（QP p.4/MS pp.13–16）。原有空栈重选测试保留。

- 调用观测：`test_1d_main_call_chain`。
- 原页：该题同卷 QP / MS（本次复核页见后续正文；原 T35 页清单保留于 manifest）。
- hollow-main：2 failed, 6 passed in 0.31s，已被拒绝。
- 等价正确 A：主程序额外输出带题号说明；B：提取 `main()` 并作所列输出/循环改写。两版均通过。
- 参考解：8 passed in 0.30s；全部 4 个 mutant 各至少一测失败。
- 自动/人工：24.000000/3.000000 分，88.89% → 88.89%。
