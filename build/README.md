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

## 设问分布（T13b）

设问分布按 `command_word` 的开头命令短语归为以下八类；忽略大小写、合并空白，
命令词后的冒号等标点也可识别。不从题干或 MS 猜补缺失的命令词。

| JSON 键 | 手册显示 | 命令词 |
|:--|:--|:--|
| state | 陈述/识别/列举 | State、Identify、Give、Name、Define、List、Label |
| describe | 描述 | Describe、Outline |
| explain | 解释/论证 | Explain、Justify、Why、Suggest |
| complete | 补全/绘制 | Complete、Draw、Fill、Trace、Dry run、Tick、Circle、Match、Copy |
| write | 编写（代码/表达式/SQL） | Write、Code、Program、Implement、Construct |
| calculate | 计算/转换 | Calculate、Convert、Show、Work out、Determine、Find |
| compare | 比较/评价 | Compare、Evaluate、Discuss、Distinguish、Difference、Contrast |
| other | 其他 | 缺失或未识别的命令词 |

Show 包含二进制运算/移位的结果展示。Write 不论要求代码、表达式还是 SQL 都归编写。
只统计核验语料的主题型行，扩展行、等价行与仅副归属行均不增加该题型的设问计数。
JSON 仍使用英文键，Markdown 与 HTML 使用中文类名并按上表顺序展示。
旧的独立 define/identify/suggest 键已分别并入 state/state/explain，Evaluate、Discuss
并入 compare；重新构建即可更新索引。

回归测试：`~/.venvs/alevel-cs/bin/python -m pytest build/tests -q`。
