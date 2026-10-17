# P3 标注真源与复现

T31 的完整判定与原页复核已经记录；`blind/` 是首次读取 pilot 之前提交的快照，其 SHA256 在 `blind/manifest.json`。`report_p3.py` 校验散列后比较原始盲标与 pilot，技能集合分歧另记 `pilot_review.json`。

- `manual_types.json`：617 个独立行按原顺序的题型判定；`manual_notes.json`：边界说明及局部修订。
- `compile_tags.py`：展开独立判定与 241 个 equivalent_of / D35 继承行，重建 `p3_tags.jsonl`。
- `split_spec.json`：A 类 MS 清单的切分与技能、B 类 QP 留空行到本题 MS 的原文映射。
- `compile_markpoints.py`：重建 `p3_markpoints.jsonl`，复制重复行对应内容；`split_exemptions.jsonl` 逐项说明图/表豁免。
- `render_review.py`：通过 `rows.py render` 生成独立行 QP/MS 拼图；图片在 `/tmp/t31-render`。`render_manifest_*.json` 与 `review_log.json` 记录已核对页，重新渲染会把对应 manifest 状态重设为待核对。
- `apply_p3.py`：只替换 `types`、`tag_confidence`、`tag_note`、`markpoints`、`ms_max`；其余字段的原始 JSON 片段保留。`audit_merge.py` 对照基线逐字段核验字节。

在任务 worktree 根目录执行（共用环境，无新增依赖）：

```sh
~/.venvs/alevel-cs/bin/python pipeline/tag/p3/compile_tags.py
~/.venvs/alevel-cs/bin/python pipeline/tag/p3/compile_markpoints.py
~/.venvs/alevel-cs/bin/python pipeline/tag/p3/check_p3.py
~/.venvs/alevel-cs/bin/python pipeline/tag/p3/report_p3.py
~/.venvs/alevel-cs/bin/python pipeline/tag/p3/apply_p3.py
~/.venvs/alevel-cs/bin/python pipeline/tag/p3/audit_merge.py --base origin/main
~/.venvs/alevel-cs/bin/python -m pytest pipeline/tag/p3 -q
make check
make check-scope TASK=T31
~/.venvs/alevel-cs/bin/python pipeline/tag/p3/apply_p3.py --check
~/.venvs/alevel-cs/bin/python pipeline/tag/p2/apply_p2.py --check
~/.venvs/alevel-cs/bin/python pipeline/er/apply_er.py --check
```

测试覆盖非任务字段/转义的保留、替换过期标注、重复 ID 拒绝、完整覆盖、原文子串、技能词表、分值上限与豁免约束。临时让 apply 删除 `er` 的故障注入使两个保留测试失败；恢复代码后七项测试全过。

报告中的三个「需要总控决定」均为指南边界建议；当前数据采用明确记录的判定，可供设计工位复核。主题型和切分的盲标一致率均为 100%，未在对照后改写它们。
