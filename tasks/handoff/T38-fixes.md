# 交接 · T38b（改 P4 卡）与 T38c1–3（排查 54 道 P4 练习）

任务卡：`tasks/T38-fixes.md`；裁决：`docs/DECISIONS.md` D46；证据：`papers/p4/audit/T38-report.md`、`T38-findings.jsonl`、`practice-runs.json`（审计员复现用的反例与命令）。

## T38c 每道练习的执行方案

1. 读 `task.md` 证据格对照表，列出所有标“自动”的主程序 / 调用点（MS 原文含 call / use the return value / pass … as parameter / output the value returned）。
2. 读 `test_task.py`：这些点的测试是只看输出数值，还是真观测了调用？只看数值的 → 用 `run_script_traced` 补：
   ```python
   from testkit import run_script_traced
   def test_1f_main_calls_readdata_and_calculate(candidate_path, exercise_dir):
       """9618_s25_42:1(f)(i) MP1–MP2: main inputs a file name, calls ReadData, then Calculate, outputs its result."""
       r = run_script_traced(candidate_path, stdin="StackData.txt\n", files_dir=exercise_dir / "files")
       assert r.error is None
       assert [c.args.get("FileName") for c in r.called("ReadData")] == ["StackData.txt"]   # parameter name as in the QP
       calc = r.called("Calculate")
       assert calc and str(calc[-1].result) in r.stdout
   ```
   参数名、模块名照 QP；能用两份不同数据文件证明“输出来自真实计算”时一并测。
3. 写 `ref/mutant_hollow_main.py`：复制参考解，主程序改成不调用模块、直接 `print` 期望值（照 F06 / F07 的反例写法）。跑 `CANDIDATE=…/ref/mutant_hollow_main.py pytest -q practice/p4/<名>/test_task.py` 必须有失败。
4. 查过严断言：`re.findall(r"-?\d+", out)` 一类全量提取、`^…$` 整行正则、`len(x) == N` 而 MS 写 min、输出必须同一行——按 QP / MS 放宽，并在 docstring 写依据（QP / MS 页）。
5. 写 1–2 个等价正确改写（临时目录），连同参考解与全部 mutant 跑一遍：参考解全过、改写全过、mutant 全挂。
6. 更新对照表、manifest、README；`practice/p4/T38c-sweep-<n>.md` 加一节；提交 `T38c<n>: harden <目录名>`。
7. 子批完成：`make check-all` → `make check-scope TASK=T38c<n>` → PR。

## T38b 的执行方案

照 `tasks/handoff/T37-cards.md`「每张卡的执行方案」写三个新代表题（OP-02、OP-03、OP-07）：看原页 → 写整题可运行程序并在官方源文件上跑 → 卡里作答与程序一致 → MP 对齐 → 证据格怎么交；F01–F04 是小改。T37B 的辅助脚本在 `~/Desktop/alevel-cs-wt/handoff/t37b-scripts/`。
