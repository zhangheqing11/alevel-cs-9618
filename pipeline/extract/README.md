# T12 PDF 抽取

从独立 worktree 根目录运行（先按根目录说明准备共用环境）：

```sh
~/.venvs/alevel-cs/bin/python pipeline/extract/run_all.py --component 1
~/.venvs/alevel-cs/bin/python -m pytest pipeline/extract/test_extract.py -q
make check
make check-scope TASK=T12
```

`--component 2/3/4` 分别重建后续批次；`--all` 重建全部。后续批次仍须各自完成抽查后分 PR 交付。源目录由 `ALEVEL_CS_SOURCES` 指定，默认主 checkout 的 sources；读取前核对 inventory 的 QP/MS SHA-256。源文件不写入。缓存由 `ALEVEL_CS_EXTRACT_CACHE` 指定，默认 `/tmp/alevel-cs-extract`，不入库；缓存版本变化时自动重建。

QP 使用旋转后的可视坐标识别题号、右侧分值框及父级情景。MS 根据表头定位 Question/Answer/Marks 列，重复题号与无表头续页合并，保留语言示例。题号顺序、唯一性或总分不符时停止，避免静默写入错配结果。少数 MS 文本层缺括号的题号统一规范化；答案文字不改写。

`overrides.json` 按行 id 保存有证据的字段覆盖，格式为 `{"id": {"reason": "原页与修正理由", "fields": {...}}}`。当前无需逐行手工覆盖。不要直接修改生成的 JSONL。

每卷以卷号为固定随机种子抽 5 行。人工对照源 PDF 文字层的题号、起句、关键数据、分值、页码和同题 MS；图表与代码另看渲染原页。所见、结果与行内容 SHA-256 记录在 `audit_p<N>.json`。这些记录必须由实际复核后填写；重跑解析器不会自动认证。行内容变化会在报告显示“待核验”。抽查范围不等于全量逐字校勘。

文字层不含图形连线、填色、逻辑取反横线和部分箭头，相关题标 figure；完整图意须回 QP/MS 原页。MS 仅保存 Answer 单元格原文，额外 Guidance 列不混入答案。报告列出每卷全部 flags、分值差异与有效抽查记录。
