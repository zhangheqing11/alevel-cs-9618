# 语料格式：清单与小问行

## `corpus/inventory.csv`（T01 产出）

一行一份卷（`9618_<季><yy>_<卷号>`）。列：

| 列 | 说明 |
|:--|:--|
| `paper` | `9618_s24_22` |
| `component` | 1–4 |
| `session`, `year`, `variant` | `s`, 2024, 2 |
| `corpus` | `verified`（2022–2026s）或 `extension`（2021） |
| `qp`, `ms`, `in` | 相对 `sources/pastpapers/` 的文件名；没有则空 |
| `sf` | P4 源文件**目录名**（`9618_s24_sf_41`）；非 P4 为空 |
| `er`, `gt` | 该考季考官报告、分数线文件名（同季各卷共用） |
| `total_marks` | 整卷总分（QP 封面标注；9618 各卷为 75） |
| `qp_sha256`, `ms_sha256` | 校验和，用于去重与变更检测 |
| `duplicate_of` | 若本卷 QP 与另一卷逐页相同，填那份卷号 |
| `status` | `ok` / `missing-ms` / `missing-qp` / `missing-sf` / `note:<文字>` |

## `corpus/rows/p<N>/<卷>.jsonl`（T12 产出）

每行一个最细小问，字段见 `row.schema.json`。规则：

1. **最细一级**：凡印有独立分值 `[n]` 的部分都是一行。`3(b)` 下有 `(i)(ii)` 时只出 `3(b)(i)`、`3(b)(ii)`，不出 `3(b)`。整题只有一个分值时题号可以只是 `5`。
2. **分值守恒**：同一卷所有行 `marks` 之和必须等于 `inventory.csv` 的 `total_marks`。`make check` 会验证。
3. **题干**：`stem` 只放本小问自己的文字；理解本小问必需的公共情景放进 `stem_ctx`（可截取，保留关键数据与标识符名）。代码清单、表格尽量保留排版。
4. **MS**：`ms_text` 只放本小问那一格的 MS 原文；P4 的 MS 常并列 Java/VB/Python 三种示例，**全部保留**（得分点与语言无关，Python 示例供出测试）。
5. **页码**：`qp_page`、`ms_page` 为对应 PDF 的 1 起页码。
6. **重复 variant**：若某小问与更早一份卷逐字相同，填 `equivalent_of`，仍保留本行（分值守恒要用）。
7. **不确定就标记**：拆分边界拿不准 → `split-uncertain`；MS 对不上 → `ms-misaligned`；依赖图表 → `has_figure: true` 并加 `figure`。不要为了凑分值而硬拆。
8. 2021 年的卷 `extension: true`。
9. `types`、`tag_confidence`、`markpoints`、`er` 在后续任务添加；T12 不写这些字段。
