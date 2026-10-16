# T13 · 手册构建器 md → md/html/json（执行工位 codex-2）

## 目标

写 `make build` 背后的构建器：把设计工位手写的题型卡、概念表、阶梯卡，与语料统计合成为学生阅读的手册（md + 单文件 html）和机器索引（json），输出到 `output/`（gitignore）。真实内容还没写出来，所以你要**自带夹具数据**开发和测试。

## 输入

- 规范：`schemas/card-format.md`（**auto 块、题型卡标题、⟦行 id⟧ 与「MS 引文」⟦行 id⟧ 语法**）、`schemas/row.schema.json`、`schemas/taxonomy.schema.json`、`schemas/corpus-format.md`。
- 参考实现（物理版，只读，可移植思路与样式）：`/Users/zhangheqing/Desktop/a2 physics/work/p4-v2-build/`——`gen_handbook.py`、`build_html.py`、`page.css`、`page.js`、`data/mkstats.py`（星级算法）。

## 功能需求

1. 入口 `build/build.py`，子命令 `all`、`p1`、`p2`、`p3`、`p4`、`ladder`。缺输入的部分跳过并提示，不报错退出。
2. **统计**（`build/stats.py`）：每个题型基于核验语料（`extension: false`，`equivalent_of` 为空的行）计算主归属小问数、分值、跨章出现数、出现卷数、出现考季数、设问分布（`command_word` 归类）、2021 扩展题数。星级沿用物理算法、**按卷内分别计算**：`score = marks + 3 × sessions`，前 1/4 → ★★★，前 2/3 → ★★，其余 ★。
3. **auto 块填充**：`chapter-stats`、`type-tree`（题型码、名称、★、小问数/分值）、`stats <码>`（一行考情）、`drills <码>`（2022–26 刷题清单按新卷在前，题号形如 `s24/22 Q3 (b)(i),(b)(ii)`；2021 扩展单列）。
4. **引用渲染**：`⟦9618_s24_22:3(b)(ii)⟧` → 短格式 `s24/22 Q3(b)(ii)`；html 里加 `title` 显示 QP/MS 文件名与页码。`「…」⟦…⟧` 保留引文、渲染为英文得分句样式。
5. **组装顺序**：`papers/p<N>/front.md` → 按 `taxonomy.json` 的章节顺序拼 `cards/<章>.md` → `back.md`；概念表单独成书：`core/<章>.md` 依章序。输出：
   - `output/p<N>/P<N>题型手册.md` 与 `.html`
   - `output/p<N>/P<N>核心概念.md` 与 `.html`（P2/P4 名为 `P<N>伪代码与Python对照`）
   - `output/p<N>/index.json`：每个题型的统计、★、代表题（解析 `#### 代表题精讲　⟦…⟧`）、下一道变式、刷题清单（行 id、`qp_page`、`ms_page`、QP/MS 文件名）、对应练习文件夹路径（扫描 `practice/` 的 `meta.json`）。
   - `output/ladder/Python阶梯.md`、`.html`、`index.json`（design + 各级卡 + 练习清单）。
6. **HTML**：单文件自包含（内联 CSS/JS），左侧目录可折叠、页内搜索、锚点跳转（`{#P1-DB-03}`）、代码高亮（Python 用 pygments；`pseudocode` 自写简单词法：大写关键字、`←`、注释 `//`）、表格样式、打印友好。中文字体栈：`"PingFang SC", "Noto Sans CJK SC", sans-serif`。不需要掌握按钮。
7. md → html 转换用 `markdown` 包（已在 requirements）或 pandoc（已装）；选一个并在 `build/README.md` 说明。

## 测试

- `build/tests/fixtures/`：一套迷你语料（2 份卷、十几行）、迷你 taxonomy、2 张章文件（含全部 auto 块与引用语法）、迷你阶梯。
- `build/tests/test_build.py`（pytest）：统计数值、星级分档、auto 块全部被替换、引用渲染、输出文件存在、index.json 字段完整、缺输入时不崩溃。构建器须支持 `--root` 指向夹具目录、`--out` 指向临时目录。

## 允许写的路径

`build/**`、`tasks/progress/T13.md`。（`make build` 已在 Makefile 里调用 `build/build.py all`。）

## 完成标准

- `~/.venvs/alevel-cs/bin/python -m pytest build/tests -q` 全绿。
- 在真实仓库上 `make build` 不报错（此时大部分输入缺失，应优雅跳过）。
- `make check`、`make check-scope TASK=T13` 全绿。
- PR 附一张用夹具生成的 html 截图或说明如何打开。

## 工作方式

```bash
cd ~/Desktop/"alevel cs" && git fetch origin
git worktree add ~/Desktop/alevel-cs-wt/T13 -b task/T13-builder origin/main
cd ~/Desktop/alevel-cs-wt/T13 && codex
```

进度写 `tasks/progress/T13.md`；交付：rebase → 检查 → `git push -u origin HEAD` → `gh pr create --base main`。不要合并。完成后转 T14（若总控已通知 T10 批 1 合并）。
