# T36b · 按审计修正 P3 题型手册（执行：子智能体）

## 目标

按 `docs/DECISIONS.md` **D44** 修正 T36 审计（#46）找出的问题：F01–F05、F07–F12 共 11 条（F06 不改），外加 D44 ③ 的 BL-02 变式。只改有问题的地方及审计点名的同类重复表述。

## 输入

- `papers/p3/audit/T36-findings.jsonl`（F 编号 = 行序）、`papers/p3/audit/T36-report.md`（证据与建议）。
- `docs/DECISIONS.md` D1、D2、D25、D37、D41、**D44**（D44 的裁决优先于 findings 里的 suggestion）；`schemas/card-format.md`。
- 原卷（只读）：`/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/`；动笔前重读相关 QP / MS 原页。

## 改法要求

1. 每条按 findings 的 suggestion 改，D44 另有规定的按 D44：F05 写成“官方笔误（D41 ②），教学按 D.(A + B̅)，给分仍按 MS”，删掉“已报总控决定”一类说法；F10 在 CT-02 代表题处加一句“照 MS 填空得分；自己写时按模板处理边界（目标小于 Names[1] 时原代码会读 Names[0]）”；F11 改成“本型语料里空栈时 Top 的取值各题不同（如 w25/33 MS 接受 –1、0、1），按该题题干约定”，core/CT.md 同步。
2. D44 ③：BL-02 的“下一道变式”改为正式变式 `9618_s21_31:7(c)`（2021 扩展卷），删去“无第二道”说法；front.md 或其他处若有同类说法一并改。
3. 「…」⟦行 id⟧ 只放 MS 原文；新写的非 MS 句子不加「」。F04 去掉引文里的 “[1]” 计分标记（取 MS 原句里不含标记的片段）。
4. 不改 F06 那三处 s26 引文（D44 ①）。

## 产出

- 修正后的 `papers/p3/cards/*.md`、`papers/p3/core/*.md`、`papers/p3/front.md` / `back.md`（按需）。
- `papers/p3/audit/T36-fixes.md`：F 编号 → 文件与行 → 改动摘要（warn 附改后原文片段）；末尾列 D44 ③ 的改动；重跑 `papers/p3/audit/` 的审计脚本并记录结果。

## 允许写的路径

`papers/p3/cards/**`、`papers/p3/core/**`、`papers/p3/front.md`、`papers/p3/back.md`、`papers/p3/audit/**`、`tasks/progress/T36b.md`。

## 完成标准

- `make check` 全绿；`make build` 后 `output/p3/` 正常；`make check-scope TASK=T36b` 全绿。
- 11 条与 D44 ③ 每条都在 `T36-fixes.md` 有对应记录。

## 工作方式

从最新 `origin/main` 开分支 `task/T36b-p3-fixes`；交付：rebase → `make check` → `make build` → `make check-scope TASK=T36b` → push → `gh pr create --base main --title "T36b: fix P3 handbook per audit"`。不要合并。
