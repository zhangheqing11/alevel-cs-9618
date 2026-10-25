# 交接 · T53 指南进构建 + 引文正则

任务卡：`tasks/T53-guide-build.md`。纯工程任务，改 `build/` 一个包。

## 1. 先读

- `build/README.md`、`build/build.py`（`build_ladder` 是最接近的范本：无 taxonomy 的文档也走 `_processed(...)`，`empty_taxonomy = {"chapters": [], "types": []}`，同时出 `.md` 与 `.html`）、`build/markdown.py`（`QUOTE_REF` 第 18 行、`render_citations` 里的 `combined` 第 91 行）、`build/html.py` 的 `render_html(source, title, kind)`。
- `build/tests/test_build.py` 与 `build/tests/fixtures/`：现有测试怎样用 `--root` 指向夹具、`--out` 指向临时目录。
- `docs/guide/concept-threads.md`：真实输入（标题是一级标题「跨卷概念主线」，文中有 ⟦行 id⟧ 与题型码，没有「」）。

## 2. 执行方案

1. 建 worktree（交接 README §1，新分支 `task/T53-guide-build`）；先跑一次 `python3 build/build.py all --out work/tmp/before` 留作对比基线。
2. **正则（M1）**：
   1. 先写回归测试：输入 `示例标「非 MS 原文」。……「A buffer allows temporary storage of the data」⟦<夹具里存在的行 id>⟧` 这种“前面一个不带行号的「」、后面一个带行号的引文”，断言渲染后前一个「」原样保留、只有后一个被当作引文。现在的正则下它应当失败（真实例子：`skill/cie-9618-cs-tutor/references/few-shots.md` 开头说明段的「非 MS 原文」会和示例 6 的引文连成一段）。
   2. 把 `QUOTE_REF` 与 `combined` 改成不跨越「」的写法（`「([^「」]*)」`），保持其余行为不变；测试转绿。
3. **guide 命令**：
   1. `build_guide(root, out)`：`docs/guide/` 不存在或没有 `.md` 时打印 skip 并返回 False（同 `build_ladder`）；否则每个 `docs/guide/*.md`（排序）各生成 `out/guide/<stem>.md` 与 `<stem>.html`，HTML 标题取文中第一个 `# ` 标题（去掉 `{#…}`），`kind="guide"`；引文与行号照 ladder 的方式渲染（`citation_metadata(rows, load_inventory(root), source_root=…)`）。打印 `built output/guide/<stem>.md`。
   2. `main()` 的 `choices` 加 `guide`；`all` 在 `build_ladder` 之后调用 `build_guide`。
   3. 测试：夹具里放一份带一个 ⟦行 id⟧ 的小 guide，断言两个文件生成、行号被渲染成短题号、HTML 标题正确；无 `docs/guide/` 的夹具 `all` 仍成功。
4. `build/README.md` 加 `guide` 用法一行。
5. 对比：`python3 build/build.py all --out work/tmp/after`，`diff -r work/tmp/before work/tmp/after`（只看 `.md`，HTML 太长可只统计）；把差异逐条贴进 PR，说明每处是不是原来被吞的文本。
6. 交付：rebase → `pytest build/tests -q` → `python3 build/build.py all` → `make check` → `make check-scope TASK=T53` → push → `gh pr create --base main --title "T53: build docs/guide and fix quote regex"`。

## 3. 坑

- `build/` 里的 `html.py`、`markdown.py` 与标准库 / 第三方包同名；直接 `python3 build/build.py` 跑没问题（文件开头处理了 `sys.path`），测试照现有测试的导入方式写。
- `output/` 是生成物（gitignore），不要提交；对比用的 `work/tmp/` 也不提交。
- 只改 `build/`。`tools/check.py` 的 `QUOTE_REF` 已经是 `「([^」]+)」`，且已把 `docs/guide` 纳入扫描（总控 2026-10-25 改），不用动。
