# T27 · 考官报告摘录挂载报告

由 `pipeline/er/report_er.py` 生成（读 `corpus/er/*.jsonl` 与 `corpus/rows/`）。ER 只用于「易错与失分」，不是给分依据。

## 总览

- 行总数 2558，挂上 `er` 2281（本级 2281、上级回退 0），无 ER 277。
- 排除 s26（尚无 ER）后覆盖率：2281/2313 = 98.6%（其中 s21_31 的 27 行因 ER 只有「考生太少、不出报告」一句而没有）。
- P4（`9618_*_4x`）的 ER 已抽取入 `corpus/er/`，行尚未入库，`apply_er.py` 在 P4 行出现后重跑即可。

| 卷 | ER 条数 | 行数 | 挂上 | 其中本级 | 其中上级回退 | 无 ER 的行 | 未用的 ER 标签 |
|:--|--:|--:|--:|--:|--:|--:|--:|
| 9618_s21_11 | 30 | 30 | 30 | 30 | 0 | 0 | 0 |
| 9618_s21_12 | 28 | 28 | 28 | 28 | 0 | 0 | 0 |
| 9618_s21_13 | 30 | 30 | 30 | 30 | 0 | 0 | 0 |
| 9618_w21_11 | 29 | 29 | 29 | 29 | 0 | 0 | 0 |
| 9618_w21_12 | 28 | 28 | 28 | 28 | 0 | 0 | 0 |
| 9618_w21_13 | 29 | 29 | 29 | 29 | 0 | 0 | 0 |
| 9618_s22_11 | 25 | 25 | 25 | 25 | 0 | 0 | 0 |
| 9618_s22_12 | 29 | 29 | 29 | 29 | 0 | 0 | 0 |
| 9618_s22_13 | 27 | 27 | 27 | 27 | 0 | 0 | 0 |
| 9618_w22_11 | 36 | 36 | 36 | 36 | 0 | 0 | 0 |
| 9618_w22_12 | 36 | 36 | 36 | 36 | 0 | 0 | 0 |
| 9618_w22_13 | 35 | 35 | 35 | 35 | 0 | 0 | 0 |
| 9618_s23_11 | 29 | 29 | 29 | 29 | 0 | 0 | 0 |
| 9618_s23_12 | 29 | 29 | 29 | 29 | 0 | 0 | 0 |
| 9618_s23_13 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_w23_11 | 33 | 33 | 33 | 33 | 0 | 0 | 0 |
| 9618_w23_12 | 32 | 32 | 32 | 32 | 0 | 0 | 0 |
| 9618_w23_13 | 29 | 29 | 29 | 29 | 0 | 0 | 0 |
| 9618_s24_11 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_s24_12 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_s24_13 | 30 | 30 | 30 | 30 | 0 | 0 | 0 |
| 9618_w24_11 | 32 | 32 | 32 | 32 | 0 | 0 | 0 |
| 9618_w24_12 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_w24_13 | 30 | 30 | 30 | 30 | 0 | 0 | 0 |
| 9618_s25_11 | 28 | 28 | 28 | 28 | 0 | 0 | 0 |
| 9618_s25_12 | 29 | 29 | 29 | 29 | 0 | 0 | 0 |
| 9618_s25_13 | 27 | 27 | 27 | 27 | 0 | 0 | 0 |
| 9618_w25_11 | 36 | 36 | 36 | 36 | 0 | 0 | 0 |
| 9618_w25_12 | 35 | 35 | 35 | 35 | 0 | 0 | 0 |
| 9618_w25_13 | 28 | 28 | 28 | 28 | 0 | 0 | 0 |
| 9618_s26_11 | 0 | 29 | 0 | 0 | 0 | 29 | 0 |
| 9618_s26_12 | 0 | 28 | 0 | 0 | 0 | 28 | 0 |
| 9618_s26_13 | 0 | 29 | 0 | 0 | 0 | 29 | 0 |
| 9618_s21_21 | 20 | 20 | 20 | 20 | 0 | 0 | 0 |
| 9618_s21_22 | 22 | 22 | 22 | 22 | 0 | 0 | 0 |
| 9618_s21_23 | 20 | 20 | 20 | 20 | 0 | 0 | 0 |
| 9618_w21_21 | 22 | 22 | 22 | 22 | 0 | 0 | 0 |
| 9618_w21_22 | 24 | 24 | 24 | 24 | 0 | 0 | 0 |
| 9618_w21_23 | 22 | 22 | 22 | 22 | 0 | 0 | 0 |
| 9618_s22_21 | 21 | 20 | 20 | 20 | 0 | 0 | 1 |
| 9618_s22_22 | 19 | 19 | 19 | 19 | 0 | 0 | 0 |
| 9618_s22_23 | 24 | 24 | 24 | 24 | 0 | 0 | 0 |
| 9618_w22_21 | 22 | 22 | 22 | 22 | 0 | 0 | 0 |
| 9618_w22_22 | 21 | 21 | 21 | 21 | 0 | 0 | 0 |
| 9618_w22_23 | 22 | 22 | 22 | 22 | 0 | 0 | 0 |
| 9618_s23_21 | 24 | 23 | 23 | 23 | 0 | 0 | 1 |
| 9618_s23_22 | 22 | 22 | 21 | 21 | 0 | 1 | 1 |
| 9618_s23_23 | 24 | 24 | 24 | 24 | 0 | 0 | 0 |
| 9618_w23_21 | 21 | 21 | 21 | 21 | 0 | 0 | 0 |
| 9618_w23_22 | 21 | 20 | 20 | 20 | 0 | 0 | 1 |
| 9618_w23_23 | 20 | 20 | 20 | 20 | 0 | 0 | 0 |
| 9618_s24_21 | 22 | 22 | 22 | 22 | 0 | 0 | 0 |
| 9618_s24_22 | 22 | 22 | 21 | 21 | 0 | 1 | 1 |
| 9618_s24_23 | 21 | 21 | 21 | 21 | 0 | 0 | 0 |
| 9618_w24_21 | 22 | 22 | 22 | 22 | 0 | 0 | 0 |
| 9618_w24_22 | 24 | 24 | 23 | 23 | 0 | 1 | 1 |
| 9618_w24_23 | 21 | 20 | 19 | 19 | 0 | 1 | 2 |
| 9618_s25_21 | 18 | 18 | 18 | 18 | 0 | 0 | 0 |
| 9618_s25_22 | 23 | 23 | 23 | 23 | 0 | 0 | 0 |
| 9618_s25_23 | 21 | 21 | 21 | 21 | 0 | 0 | 0 |
| 9618_w25_21 | 23 | 22 | 22 | 22 | 0 | 0 | 1 |
| 9618_w25_22 | 19 | 19 | 19 | 19 | 0 | 0 | 0 |
| 9618_w25_23 | 19 | 20 | 19 | 19 | 0 | 1 | 0 |
| 9618_s26_21 | 0 | 28 | 0 | 0 | 0 | 28 | 0 |
| 9618_s26_22 | 0 | 24 | 0 | 0 | 0 | 24 | 0 |
| 9618_s26_23 | 0 | 27 | 0 | 0 | 0 | 27 | 0 |
| 9618_s21_31 | 0 | 27 | 0 | 0 | 0 | 27 | 0 |
| 9618_s21_32 | 27 | 27 | 27 | 27 | 0 | 0 | 0 |
| 9618_s21_33 | 27 | 27 | 27 | 27 | 0 | 0 | 0 |
| 9618_w21_31 | 28 | 28 | 28 | 28 | 0 | 0 | 0 |
| 9618_w21_32 | 28 | 28 | 28 | 28 | 0 | 0 | 0 |
| 9618_s22_31 | 24 | 24 | 24 | 24 | 0 | 0 | 0 |
| 9618_s22_32 | 28 | 28 | 28 | 28 | 0 | 0 | 0 |
| 9618_s22_33 | 24 | 24 | 24 | 24 | 0 | 0 | 0 |
| 9618_w22_31 | 31 | 31 | 31 | 31 | 0 | 0 | 0 |
| 9618_w22_32 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_w22_33 | 31 | 31 | 31 | 31 | 0 | 0 | 0 |
| 9618_s23_31 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_s23_32 | 27 | 27 | 27 | 27 | 0 | 0 | 0 |
| 9618_s23_33 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_w23_31 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_w23_32 | 24 | 24 | 24 | 24 | 0 | 0 | 0 |
| 9618_w23_33 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_s24_31 | 29 | 29 | 29 | 29 | 0 | 0 | 0 |
| 9618_s24_32 | 27 | 27 | 27 | 27 | 0 | 0 | 0 |
| 9618_s24_33 | 29 | 29 | 29 | 29 | 0 | 0 | 0 |
| 9618_w24_31 | 25 | 25 | 25 | 25 | 0 | 0 | 0 |
| 9618_w24_32 | 27 | 27 | 27 | 27 | 0 | 0 | 0 |
| 9618_w24_33 | 25 | 25 | 25 | 25 | 0 | 0 | 0 |
| 9618_s25_31 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_s25_32 | 27 | 27 | 27 | 27 | 0 | 0 | 0 |
| 9618_s25_33 | 26 | 26 | 26 | 26 | 0 | 0 | 0 |
| 9618_w25_31 | 28 | 28 | 28 | 28 | 0 | 0 | 0 |
| 9618_w25_32 | 30 | 30 | 30 | 30 | 0 | 0 | 0 |
| 9618_w25_33 | 23 | 23 | 23 | 23 | 0 | 0 | 0 |
| 9618_s26_31 | 0 | 28 | 0 | 0 | 0 | 28 | 0 |
| 9618_s26_32 | 0 | 26 | 0 | 0 | 0 | 26 | 0 |
| 9618_s26_33 | 0 | 26 | 0 | 0 | 0 | 26 | 0 |
| 9618_s21_41 | 0 | — | 0 | 0 | 0 | — | 0 |
| 9618_s21_42 | 19 | — | 0 | 0 | 0 | — | 19 |
| 9618_s21_43 | 19 | — | 0 | 0 | 0 | — | 19 |
| 9618_w21_41 | 21 | — | 0 | 0 | 0 | — | 21 |
| 9618_w21_42 | 21 | — | 0 | 0 | 0 | — | 21 |
| 9618_s22_41 | 26 | — | 0 | 0 | 0 | — | 26 |
| 9618_s22_42 | 22 | — | 0 | 0 | 0 | — | 22 |
| 9618_s22_43 | 26 | — | 0 | 0 | 0 | — | 26 |
| 9618_w22_41 | 24 | — | 0 | 0 | 0 | — | 24 |
| 9618_w22_42 | 25 | — | 0 | 0 | 0 | — | 25 |
| 9618_w22_43 | 24 | — | 0 | 0 | 0 | — | 24 |
| 9618_s23_41 | 29 | — | 0 | 0 | 0 | — | 29 |
| 9618_s23_42 | 25 | — | 0 | 0 | 0 | — | 25 |
| 9618_s23_43 | 29 | — | 0 | 0 | 0 | — | 29 |
| 9618_w23_41 | 29 | — | 0 | 0 | 0 | — | 29 |
| 9618_w23_42 | 29 | — | 0 | 0 | 0 | — | 29 |
| 9618_w23_43 | 29 | — | 0 | 0 | 0 | — | 29 |
| 9618_s24_41 | 28 | — | 0 | 0 | 0 | — | 28 |
| 9618_s24_42 | 29 | — | 0 | 0 | 0 | — | 29 |
| 9618_s24_43 | 28 | — | 0 | 0 | 0 | — | 28 |
| 9618_w24_41 | 26 | — | 0 | 0 | 0 | — | 26 |
| 9618_w24_42 | 24 | — | 0 | 0 | 0 | — | 24 |
| 9618_w24_43 | 26 | — | 0 | 0 | 0 | — | 26 |
| 9618_s25_41 | 22 | — | 0 | 0 | 0 | — | 22 |
| 9618_s25_42 | 25 | — | 0 | 0 | 0 | — | 25 |
| 9618_s25_43 | 23 | — | 0 | 0 | 0 | — | 23 |
| 9618_w25_41 | 24 | — | 0 | 0 | 0 | — | 24 |
| 9618_w25_42 | 21 | — | 0 | 0 | 0 | — | 21 |
| 9618_w25_43 | 25 | — | 0 | 0 | 0 | — | 25 |

## 没有挂上 ER 的行（P1–P3，不含 s26）

- `9618_s23_22`：1 行（6）— ER 里没有 6 或其上级标签（但有更细标签 6(a)）
- `9618_s24_22`：1 行（1(c)）— ER 里没有 1(c) 或其上级标签
- `9618_w24_22`：1 行（1(b)）— ER 里没有 1(b) 或其上级标签（但有更细标签 1(b)(i)）
- `9618_w24_23`：1 行（6）— ER 里没有 6 或其上级标签（但有更细标签 6(a)）
- `9618_w25_23`：1 行（8(b)）— ER 里没有 8(b) 或其上级标签
- `9618_s21_31`：27 行（全部）— ER 无报告：There were too few candidates for a meaningful report to be produced.

- s26 的 6 个 P1–P3 卷共 245 行：该考季尚无 ER，不写 `er`。

## 未用的 ER 标签

### P4：行尚未入库（697）

9618_s21_42（19）、9618_s21_43（19）、9618_s22_41（26）、9618_s22_42（22）、9618_s22_43（26）、9618_s23_41（29）、9618_s23_42（25）、9618_s23_43（29）、9618_s24_41（28）、9618_s24_42（29）、9618_s24_43（28）、9618_s25_41（22）、9618_s25_42（24）、9618_s25_43（23）、9618_w21_41（21）、9618_w21_42（21）、9618_w22_41（24）、9618_w22_42（25）、9618_w22_43（24）、9618_w23_41（29）、9618_w23_42（29）、9618_w23_43（29）、9618_w24_41（26）、9618_w24_42（24）、9618_w24_43（26）、9618_w25_41（24）、9618_w25_42（21）、9618_w25_43（25）

### 被更细的本级评论取代（按任务规则不挂）（5）

- `9618_s22_21` 4（ER p.13）：every row below it has its own comment: 4(a), 4(b)。“Abstract data types are one of the topics covered on paper 2 for the n…”
- `9618_s23_21` 7(b)（ER p.15）：every row below it has its own comment: 7(b)(i), 7(b)(ii)。“Both parts of this question carry on the theme of decomposition and fo…”
- `9618_w23_22` 3（ER p.17）：every row below it has its own comment: 3(a), 3(b)。“This question required candidates to understand how a linked list is i…”
- `9618_w24_23` 3（ER p.26）：every row below it has its own comment: 3(a)(i), 3(a)(ii), 3(b), 3(c)。“This question is assessing the candidates understanding of the use of …”
- `9618_w25_21` 5（ER p.19）：every row below it has its own comment: 5(a)(i), 5(a)(ii), 5(a)(iii), 5(b)(i), 5(b)(ii)。“All parts of Question 5 required candidates to analyse a block of code…”

### ER 比行更细（3）

- `9618_s23_22` 6(a)（ER p.21）：ER is finer than row 6 (rows are not split there)。“A small number of very good solutions were seen, often gaining all 6 m…”
- `9618_w24_22` 1(b)(i)（ER p.20）：ER is finer than row 1(b) (rows are not split there)。“See the earlier comment on the ‘Key messages’ section. A few answers w…”
- `9618_w24_23` 6(a)（ER p.27）：ER is finer than row 6 (rows are not split there)。“A wide range of response was seen gaining the full range of marks. Two…”

### 无对应行（0）

（无）

### ER 重复标签（2）

- `9618_s24_22` 1(b)（ER p.17）：ER prints this label twice; second block not attached。“Few full mark answers; many candidates gained one of the two marks ava…”
- `9618_s25_42` 3(d)(ii)（ER p.46）：ER prints this label twice; second block not attached。“Candidates were often able to generate the correct outputs for the pro…”

## 抽查记录

随机抽 20 条（seed 27；P1 7 条、P2 7 条、P3 6 条，覆盖 s21–w25 各考季）。逐条把 ER 原 PDF 的对应页渲染成图，对照页上的题号与评论原文，核对题号、页码与摘录。结论：20/20 题号、页码、原文一致。

| # | 卷 | 标签 | ER 页 | 结论 |
|--:|:--|:--|--:|:--|
| 1 | 9618_s23_12 | 4(b) | 5 | 一致 |
| 2 | 9618_s25_13 | 1(c)(ii) | 10 | 一致 |
| 3 | 9618_w25_13 | 1(c) | 12 | 一致 |
| 4 | 9618_s24_11 | 8(b)(ii) | 4 | 一致 |
| 5 | 9618_s22_12 | 1(c) | 4 | 一致 |
| 6 | 9618_w24_12 | 8(a) | 7 | 一致 |
| 7 | 9618_s21_11 | 4(d) | 3 | 一致 |
| 8 | 9618_s23_22 | 8(c) | 23 | 一致 |
| 9 | 9618_s25_21 | 2(b)(ii) | 14 | 一致 |
| 10 | 9618_w24_23 | 5(b) | 27 | 一致 |
| 11 | 9618_s21_21 | 6(b) | 14 | 一致 |
| 12 | 9618_s24_23 | 2(b) | 25 | 一致 |
| 13 | 9618_s22_23 | 3(a) | 22 | 一致 |
| 14 | 9618_w23_22 | 8(a) | 20 | 一致 |
| 15 | 9618_s24_31 | 4(a) | 30 | 一致 |
| 16 | 9618_w23_33 | 8(c) | 32 | 一致 |
| 17 | 9618_s22_32 | 2(b) | 30 | 一致 |
| 18 | 9618_w22_33 | 5(a) | 40 | 一致 |
| 19 | 9618_s25_31 | 3(a) | 31 | 一致 |
| 20 | 9618_s21_33 | 1(d)(ii) | 34 | 一致 |

## 解析自检（extract_er.py 打印的异常）

- 每份 ER 的 `Question N` 标题按 N 递增接受，没有跳号；P1–P3 逐行匹配结果见上表。
- 标签序列自检（`(b)` 后只能接更大的字母，罗马数字只能递增）拒绝了 3 处并按文本保留或另存：`9618_s22_23` Q9 行首的 “(a).”（句末引用，保留为文本）；`9618_s24_22` Q1 与 `9618_s25_42` Q3 的重复标签（见下）。
- `9618_s21_31`、`9618_s21_41` 的 ER 只有「考生人数太少，不出报告」一句，只存 `_general`。

## 需要总控决定

1. `9618_w23_er.pdf` prints the heading **Paper 9618/33** twice (PDF pp. 25 and 31). The first block sits between 23 and 32, i.e. in the 31 slot, and its text is word-for-word identical to the real 33 block; QP/MS 31 and 33 also carry identical questions and mark schemes. Treated as 31 (`HEADING_FIXUPS` in `extract_er.py`, entries carry `er_header: "9618/33"`). Please confirm, or drop the fix-up and 31 loses its ER.
2. `9618_s24_er.pdf`, Paper 22, Question 1 has the label **(b)** twice (PDF p. 17). The second block ("Few full mark answers; many candidates gained one of the two marks available ... store them in an array/record/file") matches the two-mark part 1(c) (documenting variable choices), so it is almost certainly a typo for (c). Not attached (flagged `duplicate_label`); `9618_s24_22:1(c)` therefore has no `er`. Say if it should be attached to 1(c).
3. `9618_s25_er.pdf`, Paper 42, Question 3 has **(d)(ii)** twice (PDF p. 46); P4 rows do not exist yet, so nothing is lost now, but the second block (probably (d)(iii)) is flagged `duplicate_label`.
4. Where the ER comments on a finer label than the row (rows not split there): `9618_s23_22` ER 6(a) vs row 6, `9618_w24_23` ER 6(a) vs row 6, `9618_w24_22` ER 1(b)(i) vs row 1(b). Not attached (no guessing). In all three the ER gives a single sub-label, so attaching it to the row would be unambiguous: say if a rule "row has no children and the ER has exactly one finer label for it -> attach" is wanted.
5. The task rule drops a question-level or part-level comment from rows that have their own, more specific comment (listed below as `superseded`). Their content (e.g. w25_21 Q5 "All parts of Question 5 required candidates to analyse a block of code") stays in `corpus/er/*.jsonl` only; say if the skill should also see it.
6. Several ER blocks comment on two sub-parts at once, e.g. "(ii)(iii)" in `9618_s24_42` Q1 (P4). Stored once per label with `shared_with`; none occur in P1–P3.
7. `apply_p2.py` (T28) rebuilds each row line with `", "` separators and appends its owned fields last; `apply_er.py` only inserts `,"er":"..."` in compact style and replaces/removes only that field, so both can be re-run in any order. codex-1 must keep `er` out of the fields it rewrites (the `run_all.py` downstream list already includes it).
