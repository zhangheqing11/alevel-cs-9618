# 整卷模考批改包

D1 保留 `9618_s26_*` 的 12 份卷用于考前限时模考；**做完后才打开批改包**。本工具从 `corpus/rows/` 与 inventory 读取本卷数据，不读取题型卡正文，不复制 QP 题干。给分只用当前小问自己的 MS；ER 明确标为“仅供易错参考，不是给分依据”。

## 考前与考后

在仓库根目录运行（使用共享环境，无需安装新依赖）：

```sh
~/.venvs/alevel-cs/bin/python pipeline/mock/make_mock.py 9618_s26_22
```

生成 `output/mock/9618_s26_22/{marking.md,marking.html,score.csv}`，不提交生成物。`--out DIR` 改输出父目录，仍会创建 `<卷 id>/` 子目录。脚本不覆盖任何已有的 `score.csv`；要重新生成请用新的 `--out`，先保管原来的批改记录。

1. 考前只准备原卷 QP、P2 插页或 P4 源文件及证据文档，按 QP 封面计时；勿提前查看本包。
2. 完成后打开 `marking.html` 或 `marking.md`，逐小问核对本题 MS 原文。图、表、代码排版需查看对应 QP / MS 原页。页码均按 PDF 从 1 起算。现有抽取标记会原样提示；没有标记也不保证图形已转成文本。
3. 有得分点时可在打印的表格勾选；**勾选不是自动给分**。遵守 MS 的 Max、分组上限、替代答案等规则，不能机械累加。未拆得分点的小问直接按 MS 批。
4. 在 `score.csv` 的 `marks_awarded` 填整数；未得分填 `0`，未批的留空。程序拒绝未批完的表，并校验每行分值、缺行、重复行、小问及 `ms_max` 上限。
5. 可用 `lost_skills` 记录技能失分，格式例如 `loop-to-eof=2;file-close=1`。标签必须来自仓库技能词表，数值必须为正整数；同一行不能重复标签，归因总数不能超过该行失分。一个失分只归入一个主要技能，不能把同一分分给多个标签。拿不准的留空，余数列为“未归因”。**不会根据 markpoints 自动猜哪一点丢分**。`note` 可填失分原因或待教师确认的问题。
6. 汇总后把已填 `score.csv` 和摘要交给学习会话；由学习会话按既有规则记录 `ledger/`，本工具不自动写学习记录。

```sh
~/.venvs/alevel-cs/bin/python pipeline/mock/score_mock.py output/mock/9618_s26_22/score.csv
# 需要手册卡链接时先构建（脚本仅生成链接，不展示卡片答案）：
make build
```

材料路径读 `ALEVEL_CS_SOURCES`，默认 `/Users/zhangheqing/Desktop/alevel cs/sources`。时长使用官方 `sources/official/9618_syllabus_2027-2029.pdf` p.11：P1 / P3 90 分钟、P2 120 分钟、P4 150 分钟；已与 s26 四类 QP 封面核对。总分与 `corpus/inventory.csv` 核对。材料目录没有本地副本时路径仍会列出，需在持有原始资料的电脑上打开。

## 分数线接口与统计口径

读取 T40 约定的两张 UTF-8 BOM CSV：

| 文件 | 字段 |
| :-- | :-- |
| `corpus/thresholds/components.csv` | `session,year,component,max_raw,A,B,C,D,E` |
| `corpus/thresholds/options.csv` | `session,year,option,components,max_weighted,A*,A,B,C,D,E` |

T40 未合并时输出“等级占位：待 T40 …”，原始分、失分统计仍可用。合并后无需改 CSV 接口；rebase 后自动读取。`--thresholds DIR` 可指定同格式表。测试中的数值是人工构造的边界测试数据，**不是官方分数线**。

- 单卷从表中**最新一季**精确匹配 component（如 `22`，不借 `21` / `23`），估 A–E；低于 E 为 U；刚好等于分数线即达到该等级。缺少匹配不回退更早季或换 variant。
- 四卷同时传入时，必须 P1–P4 各一份，与最新季 option 的 `components` 分号串精确匹配；匹配不唯一可用 `--option AY` 明确选择。**不硬编码 AX / AY / AZ 与 variant 的对应关系**。
- 仅支持直接四卷的满分 300 option，每卷原始满分须 75。官方 2027–2029 考纲 p.11 中四卷均为 75 分、各占 A Level 的 25%，因此在此路线下加权总分等于四卷原始分之和。其他加权满分、AS 路线、跨季 carry-forward 均输出占位，不能猜换算。
- 历史线估计不是本次正式等级。摘要显示参考考季、component / option、CSV 及原始 GT 文件名；s26 目前没有 GT，默认使用 T40 最新表。
- 失分按主题型 `primary` 只计一次，副题型不重复累计；技能按手填数字累计、余数计入“未归因”。无标签小问计入“未标注”。两类统计各自与实际失分合计一致。

```sh
~/.venvs/alevel-cs/bin/python pipeline/mock/score_mock.py \
  output/mock/9618_s26_12/score.csv output/mock/9618_s26_22/score.csv \
  output/mock/9618_s26_32/score.csv output/mock/9618_s26_42/score.csv
```

## 校验与限制

```sh
make check
make check-scope TASK=T41
# 环境中的 python3 需含 pytest；使用共享环境即可：
PATH="$HOME/.venvs/alevel-cs/bin:$PATH" python3 -m pytest pipeline/mock
```

测试覆盖 s26 与普通卷的小问数、75 分合计、完整 MS 原文、得分点表、ER 提示、全部 12 卷、材料、已有分数保护、非法填写、失分守恒及单卷 / 四卷等级边界。测试不需要读取 PDF，也不会修改 `sources/`。

已知限制：P4 题型标签和得分点随后续任务入库才显示；s26 行没有 ER 摘录时明确提示“无摘录”。语料本身的抽取问题需回原页；本工具保留原文，不裁定 MS 笔误，不生成新的给分规则。2021 Specimen 尚无 inventory / rows，当前不支持；正常 2021 扩展真题可用。

需要总控决定：是否添加 `make mock PAPER=<卷 id>` 目标（调用 `$(PY) pipeline/mock/make_mock.py $(PAPER)`），以及把 `pipeline/mock` 测试纳入 `make check`；本任务不改 Makefile / tools。
