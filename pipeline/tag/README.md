# P1 标签维护

`p1_tags.jsonl` 是当前标签真源；`p1_tags.blind.jsonl` 与 `blind_manifest.json`
保存首次全量盲标，不随裁决更新。设计工位维护只读输入
`papers/p1/adjudication.csv`，列为 `id,primary,cross,reason`，副题型以分号分隔，
没有副题型时留空。

T22 批 B/C 或后续批次追加裁决后，在仓库根目录依次运行：

```sh
~/.venvs/alevel-cs/bin/python pipeline/tag/apply_adjudication.py
~/.venvs/alevel-cs/bin/python pipeline/tag/apply_tags.py
~/.venvs/alevel-cs/bin/python pipeline/tag/build_report.py
~/.venvs/alevel-cs/bin/python pipeline/tag/apply_adjudication.py --check
~/.venvs/alevel-cs/bin/python pipeline/tag/apply_tags.py --check
~/.venvs/alevel-cs/bin/python -m pytest pipeline/tag/test_apply_tags.py pipeline/tag/test_adjudication.py -q
make check
make check-scope TASK=T24
```

回写脚本读取每次运行时 CSV 的全部行，无需手工维护行号或规则清单。
`reason` 必须以类似 `裁决规则 B1（名称）：解释` 的格式开头；脚本提取规则编号，
将备注写为 `adjudicated: B1`，置信度统一改为 `high`。
同一 `equivalent_of` 链上的标签一并更新。重复行号、未知题型、无规则编号、
等价行相互冲突等情况会在写标签真源之前拒绝。重复运行没有改动。

最后合并仅修改 corpus 的三个标签字段。报告分别显示封存盲标一致率与裁决后结果；
`pilot_review.jsonl` 保留第一次复核，`pilot_comparison.json` 追加展示当前裁决，
不会通过改写盲标来提高历史一致率。
