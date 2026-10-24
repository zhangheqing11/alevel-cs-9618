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
