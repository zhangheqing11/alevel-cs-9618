# 9618 官方分数线表（s21–w25）

数据来自只读 `sources/pastpapers/9618_<季><yy>_gt.pdf` 共 10 份官方原件。页码均按 PDF 从 1 起计；只统计这十季，未补 s26 或未来分数线。

## 文件与字段

三张 CSV 均为 UTF-8 BOM（`utf-8-sig`），首行为字段名，无额外索引列。

| 文件 | 行数（不含表头） | 内容 |
|:--|--:|:--|
| `components.csv` | 120 | 每季固定 11–13、21–23、31–33、41–43 各一行；118 行有原文数值，2 行仅作缺失占位 |
| `options.csv` | 156 | 原件全部 option；不补原件未列出的 option |
| `extra_components.csv` | 8 | 原件另列的 50、60，字段与 component 主表相同，避免丢掉特殊资料 |

| 字段 | 含义 |
|:--|:--|
| `session` | `s` = June，`w` = November |
| `year` | 四位年份，例如 `2025` |
| `component` | 原件的两位 component 编号，按字符串读入 |
| `max_raw` | 该 component 的原始满分；原件有值的行均为 75 |
| `option` | 原件的报考组合代码，保留数字开头或三字符代码，如 `2W`、`BYJ`、`P1` |
| `components` | 原印组合按顺序以分号连接，如 `12;22;32;42`；保留 50、60、80、87–89、95–99 等原印编号 |
| `max_weighted` | option 加权满分；2022–2025 直接抄表，2021 的处理见下文 |
| `A*` / `A` / `B` / `C` / `D` / `E` | 达到该等级所需的最低分；component 为原始分，option 为总分 |

component 没有 A*。原印 `–`（U+2013）照录，不转为 0 或空白；含义为该 option 没有该等级。空字段表示原件未提供数值，不表示 0，也不能用于估分。

## 学生四卷的 option 与估分

全 A Level 同一考季直接考四卷时，按实际 component 组合选 option，不能仅凭地区推定 variant。

| 四卷 component | option | 满分 |
|:--|:--|--:|
| 11、21、31、41 | AX | 300 |
| 12、22、32、42 | AY | 300 |
| 13、23、33、43 | AZ | 300 |

依据：各季分数线 PDF 的 option 表；例如 `9618_s25_gt.pdf` p.1。w21 原件只列 AX、AY，没有 AZ，不能套用别季 AZ。学生若考 12/22/32/42，完整四卷练习应查相应季 AY。实际报考 variant 与 option 尚未提供，最终以考试中心报名组合为准。历史分数线用于估分，不代表 2027 的实际等级线。

2027–2029 考纲 `sources/official/9618_syllabus_2027-2029.pdf` p.11（Assessment overview）列明 P1、P2、P3、P4 各 **75 marks**，各占 A Level **25%**。分数线 PDF 列四卷 option 满分 **300**（如 s25 p.1；s21 p.1 的正文也写明 A Level 300、AS Level 150）。据此换算：

`weighted_i = raw_i / 75 × 25% × 300 = raw_i`

因此直接四卷估分用 `total = P1 + P2 + P3 + P4`，每卷系数 1，总满分 300；这是由上述官方满分与权重推导的换算。完整 P1/P2 的 AS 组合 SX/SY/SZ 为 150 分。先查 option 总分线由 A* 向 E 比较，不能用“几张卷达到 component A”替代总等级，也不能把单卷 A 分数线相加推算 A*。

含 87、88、89、95–99、80 的组合以及额外的 50、60，其编号含义、历史成绩结转与具体加权细则在这十份 PDF 中未说明，**不确定**；本任务照录原表，不将它们当成本季四张新卷。2021w 的 J 后缀、2022s/w 的附加字母按原文指 A2-only options；不等同于完整四卷。

## 2021 的满分列与缺失情况

2021s/w 的 option 表本身没有 `Maximum mark after weighting` 列。正文给出 A Level 300、AS Level 150，所以完整 A Level 选项填 300，SX/SY/SZ 填 150（s21 p.1；w21 p.1，SY/SZ 行在 p.2）。w21 的 BQJ、BRJ、BYJ 虽明确为 A2-only，但正文未给这类的满分，故 `max_weighted` 留空，标记为**不确定**；不借用 2022 的 150 回填。这三行的等级分数仍全部照录，包括 A* = 114。

w21 p.1 的 component 表只印 10 行，没有 33、43；主表保留两个编号占位，`max_raw,A,B,C,D,E` 全空。PDF 未说明缺行原因，不据此断言未开考，也不复制 31/41 的数值。

## 每季行数与特殊行

“已印 component”包括补充编号；主表每季固定 12 行。下表的特殊 option 列只排除 AX/AY/AZ、SX/SY/SZ，其余全部列出，组合和分数见 CSV。

| 季 | PDF 页数 | 已印 component | option | 特殊 component | 其他 option |
|:--|--:|--:|--:|:--|:--|
| s21 | 1 | 12 | 6 | 无 | 无 |
| w21 | 2 | 10 | 11 | 缺 33、43 | BQ、BQJ、BR、BRJ、BY、BYJ |
| s22 | 2 | 14 | 22 | 50、60 | BX、BXJ、BY、BYJ、BZ、BZJ、CS、CT、CTN、CU、CUN、CY、CYN、P1、P2、P3 |
| w22 | 2 | 13 | 23 | 50 | AW、BP、BPJ、BQ、BQJ、BR、BRJ、BX、BY、CX、CXN、CY、CYN、CZ、CZN、P1、SW |
| s23 | 2 | 14 | 15 | 50、60 | BX、BY、BZ、CT、CU、CY、P1、P3、WF |
| w23 | 2 | 13 | 17 | 50 | BQ、BR、BY、BZ、CX、CY、CZ、P1、SW、W1、WA |
| s24 | 2 | 12 | 12 | 无 | BX、BY、BZ、CT、CU、CY |
| w24 | 2 | 12 | 18 | 无 | 2W、3W、BP、BQ、BR、BY、BZ、CX、CY、CZ、W1、WS |
| s25 | 2 | 14 | 15 | 50、60 | BX、BY、BZ、CS、CT、CU、CX、CY、P2 |
| w25 | 2 | 12 | 17 | 无 | 2W、BQ、BR、BX、BY、BZ、CX、CY、CZ、WC、WS |

附加 component 的数值全部在各 PDF p.1，详见 `extra_components.csv`。s22 的 P1/P2/P3、s23 的 P1/P3、w22/w23 的 P1、s25 的 P2 都是 **option 名称**，不等于通常说的 Paper 1/2/3。w24 p.1 的 2W、3W 即使组合和数值相同也保留两行；w22 AW 原印 `12;21;31;42`（p.1）、w23 WA 原印 `12;21;32;42`（p.2），不“纠正”为同 variant 组合。

s25 component 23 的 A = 62、AZ 的 A* = 240，以及 w25 component 33 的 D = 32（31/32 的 D = 31）均为原印数据，照录。未发现需转写的格内脚注符号；相关正文说明已在本页记录。未列出的 option 保持缺行，不造零值或补跨季数据。

## 重建与验证

依赖系统 Poppler 的 `pdftotext`；测试另用现有 Python 环境的 PyMuPDF、pytest，独立核对 PDF 文字。

```sh
export PATH="$HOME/.venvs/alevel-cs/bin:$PATH"
python3 pipeline/thresholds/extract_gt.py
python3 -m pytest pipeline/thresholds
make check
make check-scope TASK=T40
```

`ALEVEL_CS_SOURCES` 或 `--sources` 可指定 **sources 根目录**，默认 `/Users/zhangheqing/Desktop/alevel cs/sources`；`--output` 可指定输出目录。抽取只重建三张 CSV，手工核查文档不会覆盖。测试需要十份本地原件，不会联网下载或跳过缺失资料。测试全表逐值核对，另固定随机种子每份抽 3 格，并校验行数、满分、BOM 和重建字节一致性；人工原页抽查见 `check_report.md`。
