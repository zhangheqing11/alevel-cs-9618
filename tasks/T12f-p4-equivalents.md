# T12f · P4 重复行补 equivalent_of + P3 一行补链 + 回写 P3 裁决（执行工位 codex）

## 目标

1. **D42 ③**：P4 有 **162 行**与同季 `_41` 卷同题号逐字相同（题干、`stem_ctx`、MS 压缩空白后相同）却没有 `equivalent_of`。照 D35 / T12e 的办法核对 QP 图形后补上，让 P4 的统计、打标签（T34）与练习（T35）不把同一道题算两次。
2. **D41 ⑤**：`9618_s24_33:10(b)` 与 `9618_s24_31:10(b)` 是同一道题（MS 逐字相同；题干只差 `←` 在抽取文本里的位置），补 `equivalent_of`。
3. **D41 ④**：把 `papers/p3/adjudication.csv` 的 5 行裁决回写进 P3 标签真源，置信度改 high，`tag_note` 引用裁决规则。

## 输入

- `docs/DECISIONS.md` D21、D33、D35、**D41**、**D42**；`papers/p3/adjudication.csv`；`papers/p4/tagging-guide.md` §6（特殊行）。
- 现成范本：T12e（#31）的 `pipeline/extract/p3_equivalents.py`（scan → 人工审阅清单 → apply → verify）、`pipeline/extract/p3_equivalents_review.json`、`pipeline/extract/overrides.json` 里 `9618_s24_33:*` 的写法。
- 原卷（只读）：`/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/`。

## 162 行的分布（总控复核，按题干 + `stem_ctx` + MS 压缩空白后逐行比对）

| 卷 | 行数 | 已有链 | 待补 | 对应 |
|:--|--:|--:|--:|:--|
| 9618_s22_43 | 23 | 9 | 14 | s22_41 |
| 9618_s23_43 | 26 | 14 | 12 | s23_41 |
| 9618_s24_43 | 25 | 3 | 22 | s24_41 |
| 9618_w22_43 | 21 | 1 | 20 | w22_41 |
| 9618_w23_43 | 26 | 6 | 20 | w23_41 |
| 9618_w24_43 | 26 | 6 | 20 | w24_41 |
| 9618_s21_42 | 19 | 0 | 19 | s21_41（2021 扩展） |
| 9618_s21_43 | 19 | 0 | 19 | s21_41（2021 扩展） |
| 9618_w21_42 | 21 | 4 | 16 | w21_41（2021 扩展） |

## 做法要求

1. **P4 候选**：把 `p3_equivalents.py` 泛化（或另写 `p4_equivalents.py`），列出 P4 中 paper 不是 `_41`、`equivalent_of` 为空、且 `stem`、`stem_ctx`、`ms_text` 压缩空白后与同季 `_41` 同 `q` 行完全相同的行。数目应与上表一致，不一致的在报告里逐行说明。泛化时不要改变 P3 脚本的行为（P3 的 verify 仍须通过）。
2. **QP 图形核对**：每个候选行（尤其 `has_figure`）渲染两卷对应 `qp_page` 的题目区域，比对代码框、表格、截图格是否相同（像素哈希或逐页目视，结论写进 `pipeline/extract/p4_equivalents_review.json`）。图形不同或拿不准的行**不补**，列进报告「需要总控决定」。P4 源文件（`9618_<季><yy>_sf_<卷号>/`）也比一下：两卷数据文件不同的题不补。
3. **`9618_s24_33:10(b)`**：题干因 `←` 位置不同过不了逐字比对，单独写一条 override，`reason` 写明“D41 ⑤：MS 逐字相同，题干只差 `←` 的抽取位置；QP p.10 原页核对图形相同”，并在审阅清单里留渲染证据。
4. **写法**：只写 `pipeline/extract/overrides.json`，再用 `run_all.py` 重出 rows，**不要手改 jsonl**。
5. **P3 裁决回写**：按 `papers/p3/adjudication.csv` 改 `pipeline/tag/p3/p3_tags.jsonl` 里那 5 行——`primary` / `cross` 照表（与现值相同，应不变）、`confidence` 改 `high`、`note` 改成“D41 ④ / 裁决规则 Cn：……”（取 csv 的 reason 要点）；再跑 `pipeline/tag/p3/apply_p3.py`。
6. **只变该变的**：重跑后确认 P4 只有这 162 行（减去未补的）+ P3 一行的 `equivalent_of` 变化，P3 那 5 行只有 `tag_confidence`、`tag_note` 变化，其余字段逐字节不变；`types`、`markpoints`、`ms_max`、`er` 等下游字段原样保留（D33）；P1 / P2 rows 无变化。用脚本证明（verify 子命令或 diff 统计），结果写进报告。

## 产出

- `pipeline/extract/overrides.json`（新增条目）、`pipeline/extract/p4_equivalents_review.json`、泛化后的脚本与测试。
- 更新后的 `corpus/rows/p3/*.jsonl`、`corpus/rows/p4/*.jsonl`。
- `pipeline/tag/p3/p3_tags.jsonl`（5 行）。
- `corpus/extract_report.md` 新小节「T12f」：每卷补了几行、跳过几行及原因、字段不变性的验证结果、P3 裁决回写的 5 行。

## 允许写的路径

`pipeline/extract/**`、`corpus/rows/p3/**`、`corpus/rows/p4/**`、`corpus/extract_report.md`、`pipeline/tag/p3/p3_tags.jsonl`、`tasks/progress/T12f.md`。

## 完成标准

- `make check-all` 全绿；`make check-scope TASK=T12f` 全绿。
- `pipeline/tag/p3/apply_p3.py --check`、`pipeline/tag/p2/apply_p2.py --check`、`pipeline/er/apply_er.py --check` 都 0 改动。
- PR 描述：补链行数（按卷）、跳过的行与原因、不变性验证、P3 回写的 5 行、「需要总控决定」。

## 工作方式

从最新 `origin/main` 开分支 `task/T12f-p4-equivalents`；进度写 `tasks/progress/T12f.md`；交付：rebase → `make check-all` → `make check-scope TASK=T12f` → push → `gh pr create --base main --title "T12f: link duplicated P4 rows + write back P3 adjudication"`。不要合并。

**与 T34 的关系**：T34（P4 全量打标签）同时进行，也会改 `corpus/rows/p4/`。本任务先合并；T34 的真源在 `pipeline/tag/p4/`，它 rebase 时取 main 的 rows 后重跑 apply 即可。
