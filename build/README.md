# T13 手册构建器

`build/build.py` 读取 `papers/`、`corpus/`、`practice/` 和 `ladder/`，写入被
`.gitignore` 忽略的 `output/`。入口支持：

```bash
~/.venvs/alevel-cs/bin/python build/build.py all
~/.venvs/alevel-cs/bin/python build/build.py p2
~/.venvs/alevel-cs/bin/python build/build.py ladder
```

可以用 `--root` 指向测试夹具，用 `--out` 指向临时输出目录。缺少 taxonomy、卡片
或语料时，构建器会提示并跳过对应部分，仍以成功状态退出，方便总控逐步填入真实内容。

Markdown 转 HTML 使用 requirements 中的 Python `markdown` 包，并启用 `extra`、表格、
属性和围栏代码扩展。Python 代码块通过 Pygments 内联高亮；`pseudocode` 代码块使用
构建器内置的轻量关键字词法标记器。CSS 与 JavaScript 直接嵌入每个 HTML 文件，因此
生成的页面可离线打开、搜索、折叠目录并打印。
