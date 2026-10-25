# T53 · 把 `docs/guide/` 纳入构建，并修引文正则（M1）

## 目标

1. T50b 写了跨卷概念主线 `docs/guide/concept-threads.md`，现在只有 Markdown，学生要在仓库里直接读。让构建器把 `docs/guide/*.md` 生成成和手册同样式的 `output/guide/*.md` 与 `.html`（行号渲染成题号与原卷链接），`build.py all` / `make build` 一并生成。
2. 顺带修 T50 留下的 M1：`build/markdown.py` 的引文正则 `「(.*?)」\s*⟦…⟧`（带 `re.S`）遇到不带行号的「…」时，会一直匹配到后面某个「…」⟦行 id⟧，把中间的正文吞进“引文”。手册目前靠“不写不带 ⟦⟧ 的「」”绕开，修好后这条写作限制可以取消。

## 产出

- `build/build.py`：新命令 `guide`；`all` 包含它。
- `build/markdown.py`：引文正则只匹配不含「」的一段（如 `「([^「」]*)」\s*⟦([^⟧\s]+)⟧`），`QUOTE_REF` 与 `render_citations` 的 `combined` 两处一致。
- `build/tests/`：guide 构建测试（夹具）与正则回归测试。
- `build/README.md`：补 `guide` 命令。

细节见交接文档 `tasks/handoff/T53-guide-build.md`。

## 允许写的路径

`build/**`、`tasks/progress/T53.md`。不改 `docs/guide/` 的内容、`tools/`、`Makefile`（`make build` 已经调用 `build.py all`）。

## 完成标准

- `~/.venvs/alevel-cs/bin/python -m pytest build/tests -q` 全过；`python3 build/build.py all` 生成 `output/guide/concept-threads.md` 与 `.html`。
- 修正则前后各跑一次 `build.py all`，对比 `output/p1–p4`、`output/ladder` 的 `.md`：差异只出现在原来被吞文本的地方（若没有差异也照实写）；PR 贴出对比结果。
- `make check`、`make check-scope TASK=T53` 全绿。
