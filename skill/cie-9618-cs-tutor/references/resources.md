# 资料地图：仓库产物、原始资料、降级办法

> SKILL.md 的附录。每样资料「是什么、在哪、怎么用、边界」。给分只认该题自己的 MS（SKILL.md §7.1）。

## 1. 仓库里的学习资料

| 资料 | 位置 | 用法 |
|:--|:--|:--|
| 题型手册（教学主线） | 构建版 `output/p<N>/P<N>题型手册.md`（`.html` 给学生看）；手写源 `papers/p<N>/front.md`、`cards/<章节码>.md`、`back.md` | 章：考情、核心思想、题型树、易混辨析。型：考情与 ★、考法、识别信号、解题思路、（写代码类）模板与得分点地图、得分表述（MS 原文 + 题号）、易错与失分、代表题精讲、对应练习 / 阶梯、下一道变式、刷题清单。**用 `rows.py card <题型码>` 按型取**，不整章读入（每卷 5000–7000 行） |
| 概念表 / 对照表 | `output/p1/P1核心概念.md`、`output/p3/P3核心概念.md`；`output/p2/P2伪代码与Python对照.md`、`output/p4/P4伪代码与Python对照.md`；源 `papers/p<N>/core/<章节码>.md` | 术语三层定义（英文得分句带题号 / 中文 / 直观）；P2 / P4 是伪代码 ↔ Python 模板。`rows.py card P3-BL --core` 取一章 |
| 前言与通用得分规则 | `papers/p<N>/front.md`（构建版在手册开头） | 每卷的使用指南、记号、通用得分规则（每条附 MS 例）；P4 前言有章 ↔ 阶梯表 |
| 题型索引 | `output/p<N>/index.json` | 每型的统计、★、代表题、下一道变式、刷题清单（行 id、页码、文件名、是否保留）、`exercise_paths`（对应练习文件夹） |
| 小问行 | `corpus/rows/p<N>/<卷>.jsonl`（字段见 `schemas/row.schema.json`） | `stem` / `stem_ctx`、`marks`、`qp_page` / `ms_page`、本小问 MS 原文 `ms_text`、`has_figure`、`flags`、`types`（`primary` 与 `cross`）、`markpoints`（P2 / P3 写代码小问 ≥ 4 分、P4 ≥ 2 分：`n`、`text`、`marks`、`skills`）、`ms_max`、`er`（考官报告本题摘录）、`equivalent_of`、`extension` |
| 考官报告全文摘录 | `corpus/er/<季>.jsonl`（每条 `paper`、`label`、`page`、`text`） | 行级摘录已挂在行的 `er`；每卷的 Key messages / General comments 是 `label: "_general"` 的条目，冲刺与模考报告时用；**不是给分依据** |
| 题型体系、技能词表 | `papers/p<N>/taxonomy.json`；`papers/p2/skill_tags.json`（P3、P4 各有 `extends` P2 的扩展词表） | 题型码、识别信号；「失分技能」只能用词表里的标签 |
| 真题练习 | `practice/p2/<卷>_<小问>/`（126 道）、`practice/p4/<卷>_q<题号>/`（54 道整题） | `make try EX=<练习目录> [K=<测试名>]`；`meta.json` 的 `source.rows` 列出覆盖的行；`task.md` 的核对清单与对照表作答后再看 |
| Python 阶梯 | `ladder/design.md`、`ladder/levels/L<nn>-<slug>/card.md` 与 `exercises/E<nn>-<slug>/`；构建版 `output/ladder/` | 见 ladder.md |
| 模考批改包 | `pipeline/mock/make_mock.py`、`score_mock.py`（说明 `pipeline/mock/README.md`）；生成物在 `output/mock/<卷>/` | 见 mock-exam.md |
| 分数线 | `corpus/thresholds/components.csv`（每卷各 component 的 A–E）、`options.csv`（报考组合总分线，含 A*）、`extra_components.csv`；说明 `corpus/thresholds/README.md` | 估分；四卷同 variant 的 option：AX / AY / AZ |
| 决策 | `docs/DECISIONS.md` | 已定的批改与教学口径（SKILL.md §7.2 摘要） |
| 记录表 | `ledger/P1.csv`…`P4.csv`、`ledger/ladder.csv`（格式 `schemas/ledger-format.md`） | **学习进度的唯一权威**；空表由 `skill/cie-9618-cs-tutor/scripts/init_ledger.py <P1-P4>` 生成，已有的不覆盖 |
| 交接与勘误 | `handoff/` | 最新交接文档；`handoff/勘误.md` |
| 学生作答 | `attempts/<练习同路径>/`（`solution.py`、`answer.pseudo` / `answer.steps.md`、P4 的数据文件副本）；`attempts/mock/<卷>/` | 由 `make try` 创建；**里面的代码只由学生写** |

## 2. 老师提供的原始资料（只读）

根目录 `/Users/zhangheqing/Desktop/alevel cs/sources`（脚本也认环境变量 `ALEVEL_CS_SOURCES`；会话里这个变量通常没设，命令里直接写绝对路径）。不得编辑、改名、移动、删除；`teach_cambridge_raw/`、`teach_cambridge_sf/` 是导出包原样，不直接引用。`rows.py files <卷>` 直接列出一份卷的全部文件。

| 资料 | 路径（相对 sources/） | 用来做什么 | 边界 |
|:--|:--|:--|:--|
| 真题 QP / MS / P2 插页 | `pastpapers/9618_<季><yy>_<qp\|ms\|in>_<卷号>.pdf` | 原卷页（图、表、代码排版、行号）；MS 原文；插页函数表 | **给分只认该题自己的 MS**；P2 内置函数以当卷插页为准 |
| 考官报告 / 分数线 | `pastpapers/9618_<季><yy>_er.pdf`、`…_gt.pdf`（每季一份） | 易错（按 `Paper 9618/<卷号>` → `Question n`）；分数线原件 | ER 不作给分依据；分数线已抽成 `corpus/thresholds/` |
| P4 源文件 | `pastpapers/9618_<季><yy>_sf_<卷号>/`（数据 `.txt` + `evidence.doc(x)`；有的多套一层目录） | 练习的 `files/` 已逐字节复制；模考时复制到 `attempts/mock/<卷>/` | 复制使用，不改原件 |
| 2027–29 考纲 | `official/9618_syllabus_2027-2029.pdf`（更新说明 `official/9618_syllabus_update_2027-2029.pdf`） | 判断考不考；p.11 各卷时长与分值 | 范围以它为准 |
| 2027–29 伪代码指南 | `official/9618_pseudocode_guide_2027-2029.pdf` | 伪代码写法的**唯一权威**（节号与页码见 programming.md §6） | P2 内置函数以当卷插页为准 |
| 教材 Langfield & Duddell 2e | `textbooks/Langfield_Duddell_Coursebook_2e_2019.pdf` | 概念讲解与直觉、三语代码示例；章节对照见 syllabus-map.md，PDF 页 = 印刷页 + 6 | 不作给分依据；不整段复制；伪代码与指南不一致处以指南为准 |
| ZNotes AS 理论笔记 | `textbooks/ZNotes_AS_Theory_2026.pdf` | 仅作核对（P1 概念有没有漏、说法对不对） | 不当讲解主参考，不复制 |
| Example Candidate Responses（2021） | `official/support/9618_Example_Candidate_Responses_Paper_<n>_for_examination_from_2021.pdf` | 真实考生 high / middle / low 答卷 + 考官逐点点评；覆盖 s21 13 / 22 / 32 / 42 | 讲「怎样拿满分、差在哪」；不作给分依据 |
| Example Responses（2024） | `…_Paper_<n>_for_examination_from_2024.pdf` | 考官撰写的整卷范答 + 常见错误点评；覆盖 s24 13 / 22 / 32 / 42 | 同上 |
| Specimen Paper Answers P1–P3 | `official/support/9618_Specimen_Paper_Answers_Paper_<n>_for_examination_from_2021.pdf` | 2021 样卷范答 + 点评 | 同上 |
| 2021 样卷 | `official/specimen/9618_y21_sp_<qp\|ms\|in>_<n>.pdf`；P4 题卷与证据文档在 `9618_y21_sp_qp_4/`、源文件在 `9618_y21_sp_sf_4/`，MS 是 `9618_y21_sp_ms_4.pdf` | 冲刺整卷；按样卷自己的 MS 批改 | 不进 `corpus/rows`，不计统计，没有批改包 |
| Learner Guide | `official/support/9618_Learner_Guide_for_examination_from_2021.pdf` | 学生自查清单（红黄绿）、各卷答题建议 | — |
| Scheme of Work | `official/support/9618_Scheme_of_Work_for_examination_from_2021.pdf` | 官方教学顺序、课时与个别常见误区 | 不覆盖本系统已定的学习顺序 |
| 旧版指南与 2026 考纲 | `official/support/` 下 2023–25、2026 版 | 只在核对新旧差异时用 | 不用于示范写法 |

读 PDF：`pdftotext -layout -f <页> -l <页> "<文件>" -`；看图用 `rows.py render`（PyMuPDF）。没有行数据的 PDF（2021 样卷、范答册）渲染原页：`pdftoppm -r 110 -png -f <页> -l <页> "<文件>" work/tmp/figures/<名>`（生成 `<名>-<页>.png`）。

## 3. 资料缺失时怎么降级

- **某卷手册还没构建**（`output/p<N>/` 缺失）：`make build`。**手册还没合并**（`papers/p<N>/` 不存在）：告诉学生该卷未就绪，先学已就绪的卷或阶梯；学生坚持时，按考纲节 + 教材 + `rows.py find --grep` 找到的真题讲，批改照样只认该题 MS，没有题型码就不写记录表，进度写进交接文档。
- **某卷没有行数据**（例如 2021 样卷）：直接读 PDF（`pdftotext -layout` + 原页渲染），照样精确配对 MS。
- **记录表缺失**（`ledger.py summary` 显示 not created）：只有总控能建表；可以运行 `python3 skill/cie-9618-cs-tutor/scripts/init_ledger.py P<N>` 生成未学表（它不覆盖已有的表），并在交接文档里告诉总控。
- **编程题型没有练习文件夹**：先换一道有文件夹的变式（`index.json` 的 `exercise_paths`、`rows.py ex`）。整型都没有时照常教和批改：P2 伪代码按 MS；Python 写在 `attempts/practice/p<N>/<行 id 去掉冒号括号>/solution.py`，由你用题目样例数据手动运行核对；**不能标「已掌握」**，记学习中，解释证据写「无 pytest，待练习建成后补测」，交接文档待办列出补测（D3）。
- **`sources/` 不在本机**（云端会话）：只能用仓库里的行数据与练习；涉及图、表、排版的题明确说「需要在本机看原页」，不凭抽取文本断言。
