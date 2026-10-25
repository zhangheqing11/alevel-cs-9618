# Codex 启动提示词

在 worktree 里打开 codex 后，整段粘贴对应提示词。worktree 命令见各任务卡「工作方式」。

## codex-2 · T13（现在可开）

```
你是执行工位 codex-2，负责任务 T13（手册构建器）。
先读 AGENTS.md，再读 tasks/T13-builder.md；若 tasks/progress/T13.md 存在，从它记录的下一步继续。
只改任务卡允许的路径（tasks/scope.json 的 T13）。共享文件需要改动时，不要绕过，在 PR 描述写「需要总控决定：…」。
完成标准见任务卡。交付：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T13 → git push -u origin HEAD → gh pr create --base main。不要合并 PR。
中途停下或上下文将满时，把已完成/进行中/下一步/坑写进 tasks/progress/T13.md 并提交。
```

## codex-1 · T12（现在可开：语料已就绪）

```
你是执行工位 codex-1，负责任务 T12（抽文本、拆最细小问）。
先读 AGENTS.md，再读 tasks/T12-extract-rows.md 与 schemas/corpus-format.md；若 tasks/progress/T12.md 存在，从它记录的下一步继续。
PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/（只读）。按 P1 → P2 → P3 → P4 分批，每批一个 PR。
只改 tasks/scope.json 里 T12 允许的路径。交付：rebase origin/main → make check → make check-scope TASK=T12 → push → gh pr create --base main。不要合并 PR。
停下前更新 tasks/progress/T12.md 并提交。
```

## codex-2 · T14（总控通知 T10 批 1 合并后）

```
你是执行工位 codex-2，负责任务 T14（阶梯练习实现 + 伪代码审计）。
先读 AGENTS.md，再读 tasks/T14-ladder-exercises.md、schemas/exercise-format.md 和 schemas/examples/；若 tasks/progress/T14.md 存在，从它记录的下一步继续。
需求只来自 ladder/levels/*/exercises/*/spec.md，不要改 spec.md 或 card.md。伪代码指南在 /Users/zhangheqing/Desktop/alevel cs/sources/official/。
只改 tasks/scope.json 里 T14 允许的路径。交付：rebase origin/main → make check-all → make check-scope TASK=T14 → push → gh pr create --base main。不要合并 PR。
停下前更新 tasks/progress/T14.md 并提交。
```

## codex-1 · T24（现在：手上那卷 T12 开出 PR 后就转这个）

```
你是执行工位 codex-1，负责任务 T24（P1 全量打标签）。它优先于 T12 剩余的 P3/P4。
先读 AGENTS.md、docs/DECISIONS.md，再读 tasks/T24-p1-tagging.md、papers/p1/taxonomy.json、papers/p1/tagging-guide.md（唯一打标签规则）。若 tasks/progress/T24.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T24-p1-tagging。先盲标全部 979 行，再与 papers/p1/pilot_tags.csv 比对一致率。标签真源放 pipeline/tag/p1_tags.jsonl，用脚本合并进 corpus/rows/p1/。
只改 tasks/scope.json 里 T24 允许的路径。交付：rebase origin/main → make check → make check-scope TASK=T24 → push → gh pr create --base main。不要合并 PR。停下前更新 tasks/progress/T24.md 并提交。
```

## codex-2 · T14 批 3（现在可开：T10 批 3 已合并）

```
继续 T14：实现 T10 批 3（L09–L12）的练习与伪代码审计，同批 1、批 2 的做法。先读 docs/DECISIONS.md（D10–D13、D18）。从最新 origin/main 开分支 task/T14-ladder-batch3。交付：rebase → make check-all → make check-scope TASK=T14 → push → gh pr create --base main --title "T14 batch 3: L09–L12"。不要合并 PR。
```

## codex-1 · T12 补 equivalent_of（D21，可在 T24 之后或手头那卷之后做）

```
T12 后续：按 docs/DECISIONS.md D21，用 pipeline/extract/overrides.json 给 9618_s21_23、9618_w21_23 中与同季 _21 卷逐题相同、但还没标 equivalent_of 的 37 行补上 equivalent_of（指向 _21 卷对应行），重跑抽取确认其余字段不变。从最新 origin/main 开分支 task/T12-p2-equivalents。交付：make check → make check-scope TASK=T12 → push → gh pr create --base main。不要合并。
```

## codex-2 · T28（现在可开：P2 全量打标签 + 拆得分点）

```
你是执行工位 codex-2，负责任务 T28（P2 全量打标签 + 拆得分点）。它与 codex-1 的 T24（P1）并行，不要碰 P1 的文件。
先读 AGENTS.md、docs/DECISIONS.md，再读 tasks/T28-p2-tagging.md、papers/p2/taxonomy.json、papers/p2/skill_tags.json、papers/p2/tagging-guide.md（唯一规则，§8 是得分点拆分）。若 tasks/progress/T28.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T28-p2-tagging。先盲标全部 721 行并拆得分点，再与 papers/p2/pilot_tags.csv、pilot_markpoints.jsonl 比对。真源放 pipeline/tag/p2/，用脚本合并进 corpus/rows/p2/。
只改 tasks/scope.json 里 T28 允许的路径。交付：rebase origin/main → make check → make check-scope TASK=T28 → push → gh pr create --base main。不要合并 PR。停下前更新 tasks/progress/T28.md 并提交。
```

## codex-1 · T24b 回写裁决 + T13b 命令词归类（T22 批 A 合并后可做）

```
两个小任务，各开一个分支、各一个 PR，不要合并：
1) T24b（分支 task/T24b-apply-adjudication）：把 papers/p1/adjudication.csv（设计工位的裁决，id,primary,cross,reason）回写进 pipeline/tag/p1_tags.jsonl（cross 用分号分隔；confidence 改 high；note 写 "adjudicated: " + reason 的规则编号），再用 apply_tags.py 套进 corpus/rows/p1/。以后 T22 批 B/C 追加的 adjudication 行也照此回写（可重复运行）。scope 用 T24。
2) T13b（分支 task/T13b-command-words）：build/stats.py 的设问分布把 Convert/Give/Identify/Complete/Write/Draw/Calculate/Show 等都归成了 other。按 9618 常见命令词整理成有限几类（state/identify/give、describe、explain/justify、complete/draw、write（代码/表达式/SQL）、calculate/convert、compare/evaluate、other），md 里用中文类名显示；补测试。scope 用 T13。
交付：make check → make check-scope TASK=T24（或 T13）→ push → gh pr create --base main。
```

## codex-1 · T12c 私用区字符归一（D26，等 T28 合并后再做）

```
T12c（分支 task/T12c-pua-normalise）：按 docs/DECISIONS.md D26 的对照表，在 pipeline/extract 的文本归一步骤里把私用区字符改写成真实符号，作用于全部卷的 stem、stem_ctx、ms_text；重跑抽取，确认除这些字符外其余字段逐字不变（写一个对比脚本，报告每卷改了多少处）。表外若还有 U+E000–U+F8FF 字符，列进报告，不要猜。然后用 pipeline/tag/apply_tags.py（P1）与 pipeline/tag/p2/apply_p2.py（P2，T28 的产物）重新套上标签，并把 markpoints 的 text 按同一张表改写。scope 用 T12 + T24 + T28 的路径（如被 check-scope 拦下，写进 PR「需要总控决定」）。交付：make check-all → push → gh pr create --base main。不要合并。
```

## codex-2 · T25 批 1（现在可开：P2 练习文件夹）

```
你是执行工位 codex-2，负责任务 T25（P2 真题练习文件夹）。先做批 1（主题型 P2-PG-*）。
先读 AGENTS.md、docs/DECISIONS.md（D1、D2、D10、D24、D25、D26），再读 tasks/T25-p2-practice.md、schemas/exercise-format.md、schemas/examples/，并参考已合并的阶梯练习写法（ladder/levels/*/exercises/*）。若 tasks/progress/T25.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T25-p2-practice-b1。题干与示例一律对照 QP 原页转写（PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/）。
只改 tasks/scope.json 里 T25 允许的路径。交付：rebase origin/main → make check-all → make check-scope TASK=T25 → push → gh pr create --base main --title "T25 batch 1: P2 practice (PG)"。不要合并 PR。停下前更新 tasks/progress/T25.md 并提交。
```

## codex-1 · T12 P3/P4 抽取（T12c 之后）

```
继续 T12：抽取 P3 与 P4 的最细小问，P3 先、P4 后，各一个 PR，做法与 P1/P2 相同（tasks/T12-extract-rows.md、schemas/corpus-format.md，分值守恒、每卷抽查 5 行、报告写进 corpus/extract_report.md）。抽取文本按 D26 的私用区对照表归一（T12c 的归一步骤直接复用）。P4 注意：MS 并列 Java/VB/Python 三种范例，全部保留在 ms_text；题目引用的源文件在 sources/pastpapers/9618_<季><yy>_sf_<卷号>/。从最新 origin/main 开分支 task/T12-extract-p3（之后 task/T12-extract-p4）。交付：make check → make check-scope TASK=T12 → push → gh pr create --base main。不要合并 PR。
```

## codex-1 · rebase #22 + D29 新字符，然后 T12d 标签回填（#21、#23 已合并）

```
两件事，按顺序做，不要合并 PR：
1) PR #22（分支 task/T12-extract-p3）：#21 已合并进 main，你的分支与 main 在 corpus/extract_report.md、pipeline/extract/run_all.py、tasks/progress/T12.md 冲突。git fetch origin && git rebase origin/main，以 main 上 T12c 的归一代码为准解决冲突（不要保留两份实现）。再按 docs/DECISIONS.md D29 把 U+F0F0→「⇨」、U+F0A5→「∞」加进 pipeline/extract 的归一对照表（tools/check.py 已加），补一条回归测试，重跑 P3，确认 P3 已无表外私用区字符、P1/P2 rows 无变化，更新报告。make check-all → make check-scope TASK=T12 → git push --force-with-lease（只推你自己的分支）→ 在 PR #22 留言说明已 rebase。
2) T12d（从最新 origin/main 开分支 task/T12d-backfill-skills）：按 D30 在 pipeline/tag/p2/p2_markpoints.jsonl 回填两个新技能标签（已在 papers/p2/skill_tags.json v1.1）：9618_w21_22:6(d) MP6、9618_w23_21:6(a) MP5 → assign-value；9618_s22_22:4(a) MP5、MP6 → shift-values；都替换掉暂用的 initialise-variables。用 pipeline/tag/p2/apply_p2.py 重新套进 corpus/rows/p2/，重出 corpus/tag_report_p2.md。另外用关键词（assign、shuffle、shift、move up/down、rotate 等）扫一遍全部 P2 得分点，把疑似也该用这两个标签的列进 PR「需要总控决定」，不要自己改。make check-all → make check-scope TASK=T12 → push → gh pr create --base main --title "T12d: backfill D30 skill tags"。
之后 P4 抽取照旧从最新 main 单独开分支、单独 PR。
```

## codex-2 · T25 批 2（#24 已合并：DT 题型 + 两处修正）

```
你是执行工位 codex-2，继续任务 T25（P2 真题练习文件夹），做批 2（主题型 P2-DT-*：一维/二维数组、记录数组、冒泡排序、读写文本文件、栈/队列/链表的数组实现）。批 1 已合并为 PR #24，写法、目录结构与人工核对清单照批 1 原样沿用。
先读 AGENTS.md、docs/DECISIONS.md（D1、D2、D10、D11、D24、D25、D26、D29、D30，以及新的 D31）、tasks/T25-p2-practice.md、tasks/progress/T25.md（从记录的下一步继续）、schemas/exercise-format.md；阶梯 L06–L08、L10 的练习是数组、文件、记录、栈队列、链表的现成写法参考。
从最新 origin/main 开分支 task/T25-p2-practice-b2。题干、数组/记录定义、文件格式与示例一律对照 QP 原页转写（PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/）。

本批要点：
- 选题口径同批 1：有 markpoints、2022–25、非 extension、主题型 P2-DT-*，一行一个练习，不跳过符合条件的行；清单写进 practice/p2/batch2_manifest.json 与 README-batch2.md。
- 全局数组按 D24/D10：Python 里用题目给定上下界的真实 list（1 起下标用占位元素或在 task.md 写明换算），题目给的全局数组、记录类型、常量放进 starter.py 的 provided 部分；不得用内置 sort、index、in 代替题目要求的查找/排序算法（测试要能抓到）。
- 读文件题：按 QP 描述的格式在 files/ 下做样例数据文件（D11：逐字、注明最后一行是否换行），用 run_script 或 candidate_path 在临时目录运行；写文件题检查生成文件的内容；空文件、只有一行等边界要测。
- 栈/队列/链表题：指针变量、空闲表、满/空判断按 QP 的全局变量定义；测试检查调用后的数组与指针状态。
- D31：QP 与 MS 范例在边界上不一致时，测试按 QP、人工清单按 MS 得分点，并在「Python 接口」写明；QP 未定义的边界不要测，或先在 task.md 写明约定。

顺手修批 1 的两处（同一个 PR，单独一个提交 "T25: fix batch 1 over-specified tests"）：
1. practice/p2/9618_s25_23_7ai：删掉把 2024-03 与 2025-03 当作同月的那个测试用例（QP 未定义是否要求同年，D31），保留同月 / 不同月两类；若 mutant 因此不再被抓到，换一个用例或改 mutant。
2. practice/p2/9618_w24_23_2a：「Python 接口」写明“循环结束后只 print 一行，内容只有总和这个数，不带说明文字”（与测试一致）；并检查批 1 其他用 output_lines 的练习是否都写清了确切输出格式，没写清的一并补上。

只改 tasks/scope.json 里 T25 允许的路径。交付：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T25 → push → gh pr create --base main --title "T25 batch 2: P2 practice (DT)"。PR 描述同批 1：数量、选题口径、对照原页情况、接口约定、「需要总控决定」。不要合并 PR。停下前更新 tasks/progress/T25.md 并提交。
```

## codex-1 · T12e P3 重复行补 equivalent_of（D35；排在 T12d 之后、P4 之前）

```
T12e（从最新 origin/main 开分支 task/T12e-p3-equivalents，scope 用 T12）：按 docs/DECISIONS.md D35，给 P3 里 119 行与同季 _31 卷同题号逐字相同的行补 equivalent_of（指向 _31 的行 id），做法同 D21：写进 pipeline/extract/overrides.json，再用 run_all.py 重出 rows，不要手改 jsonl。
1) 先用脚本列出候选：P3 中 paper 不是 _31、equivalent_of 为空、且 stem、stem_ctx、ms_text 压缩空白后与同季 _31 同 q 行完全相同的行（总控复核为 119 行：s21_32 14、s21_33 14、w21_32 15、s22_33 9、s23_33 15、s24_33 12、w22_33 14、w23_33 10、w24_33 16）。
2) 对每个 has_figure 行，渲染两卷对应 QP 页（qp_page）的题目区域比对图形是否相同（像素哈希或逐页目视；结果写进报告）；图形不同或拿不准的行不补，列进报告「需要总控决定」。
3) 重跑后确认：只有这些行的 equivalent_of 变化，其余字段逐字节不变；types、markpoints、er 等下游字段原样保留（run_all.py 已把它们列为下游字段，务必验证）；P1/P2 rows 无变化。
4) 报告写进 corpus/extract_report.md 的新小节（每卷补了几行、跳过几行及原因）。
交付：make check-all → make check-scope TASK=T12 → push → gh pr create --base main --title "T12e: link duplicated P3 rows (equivalent_of)"。不要合并。
提醒：T27 已合并，rows 现在有 er 字段；你改 pipeline/extract、pipeline/tag 时必须保留 er（D33）。之后的 P4 抽取同样从最新 main 单独开分支、单独 PR。
```

## codex（任一工位）· T31 P3 全量打标签 + 拆得分点（T30 已合并；T12e 合并前也可开工）

```
你是执行工位，负责任务 T31：按 papers/p3/tagging-guide.md 给 P3 全部 858 行打题型标签，并按指南 §8 拆写代码小问的得分点。这是跨模型盲标：P3 的题型体系与试标由 Claude 设计，你要独立标出结果，再与试标比一致率。
先读 AGENTS.md、docs/DECISIONS.md（D2、D8、D21、D33、D34、D35）、tasks/T31-p3-tagging.md（任务卡：做法、产出、完成标准都在里面，严格照做）、papers/p3/taxonomy.json、papers/p3/tagging-guide.md、papers/p3/skill_tags.json（extends P2 词表）、schemas/row.schema.json；做法照抄 P2 的 T28（pipeline/tag/p2/ 是现成范本）。若 tasks/progress/T31.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T31-p3-tagging。先盲标全部 858 行（不先看 papers/p3/pilot_*），盲标快照存 pipeline/tag/p3/blind/；再对照 pilot 复核分歧。看图题回到原页（rows.py render，PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/，只读）。
D35：与同季 _31 卷逐字相同的 119 行（T12e 正在补 equivalent_of）和已有 equivalent_of 的行，照抄 _31 卷对应行的标签与得分点。行里已有 T27 的 er 字段，apply 必须逐字保留（D33）。
只改 tasks/scope.json 里 T31 允许的路径；P2 的 apply_p2.py 不要改（需要泛化就写进「需要总控决定」）。交付：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T31 → apply_p3.py --check 与 pipeline/er/apply_er.py --check 都 0 改动 → push → gh pr create --base main --title "T31: tag P3 rows + split markpoints"。不要合并 PR。停下前更新 tasks/progress/T31.md 并提交。
```

## codex-2 · T25 批 3（#30 已合并：AD-05 / AD-06，P2 练习收尾）

```
你是执行工位 codex-2，继续任务 T25（P2 真题练习文件夹），做批 3 = 最后一批（主题型 P2-AD-05 流程图 → 伪代码、P2-AD-06 用文字步骤描述算法）。批 1（#24）、批 2（#30）已合并，写法、目录结构、人工核对清单、D31 口径照原样沿用。
先读 AGENTS.md、docs/DECISIONS.md（D1、D2、D10、D24、D25、D26、D31、D37，以及新的 D38）、tasks/T25-p2-practice.md、tasks/progress/T25.md（从记录的下一步继续）、schemas/exercise-format.md（新加了 answer.steps.md）。
从最新 origin/main 开分支 task/T25-p2-practice-b3。题干、流程图、数组/文件定义一律对照 QP 原页转写（PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/）；流程图题在 task.md 用文字或 ASCII 框图转写，并写「讲解时请对照原卷 QP p.N」，必要时像批 1 那样用原页裁切图（assets/）。

本批要点：
- 选题口径同前两批：有 markpoints、2022–25、非 extension、主题型 P2-AD-05 / P2-AD-06（当前主线约 20 行：AD-06 18、AD-05 2），一行一个练习，不跳过符合条件的行；清单写进 practice/p2/batch3_manifest.json 与 README-batch3.md。
- D38：AD-06 练习 meta.pseudocode=false，作答模板 answer.steps.md（编号空步骤，提示“英文一句一步、不写伪代码语句、说清循环与位置 in the loop / after the loop”），人工清单逐点照该题 MS；同时写同一算法的 Python（starter.py / test_task.py / ref / ≥2 mutant 照常）。AD-05 照常用 answer.pseudo。
- 原题算法无法有意义地自动测（例如只问“说明怎样用某数组”的 2 分题）时不硬造测试，列进 PR「需要总控决定」，其余照常做。
- 批 3 完成后在 README 里汇总 T25 三批总数（练习数、覆盖卷数、分值），并在 tasks/progress/T25.md 标明 T25 完成。

只改 tasks/scope.json 里 T25 允许的路径。交付：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T25 → push → gh pr create --base main --title "T25 batch 3: P2 practice (AD)"。PR 描述同前两批：数量、选题口径、对照原页情况、接口约定、「需要总控决定」。不要合并 PR。停下前更新 tasks/progress/T25.md 并提交。
```

## codex-1 · T26a 审计 P1 题型手册（跨模型交叉审计；新开 Codex 会话）

```
你是执行工位 codex-1，负责任务 T26a：逐张审计 P1 题型手册（88 张卡，章：IR、CM、HW、LG、PF、SS、SP、EO、DB），只出报告，不改卡片。手册由 Claude 设计工位写成，你是另一家模型的交叉审计。
先读 AGENTS.md（尤其 §5 证据规则）、docs/DECISIONS.md（D1、D2、D15、D25、D26、D29–D32、D37）、tasks/T26-card-audit.md（任务卡：7 个审计项、产出格式、完成标准，严格照做）、schemas/card-format.md、papers/p1/tagging-guide.md。若 tasks/progress/T26a.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T26a-p1-audit。审计范围：papers/p1/front.md、papers/p1/cards/*.md、papers/p1/core/*.md、papers/p1/back.md；先 make build 看 output/p1/ 的成品。每张卡的代表题必须对照该题 QP 与 MS 原页（PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/，只读；用 rows.py render 或 pymupdf / pdftotext），报告里列出每张卡核对的页码。make check 已保证引文逐字存在，你查的是意义：引文是否支持那句说法、满分作答是否真满分、MP 对齐、选题规则、手写计数、原卷页码、概念句.
可以先写脚本做机械检查（选题规则、计数重算、页码引用），放在 papers/p1/audit/，再逐张人工核对。产出：papers/p1/audit/T26-findings.jsonl（一条问题一行，字段与 kind / severity 取值见任务卡）、papers/p1/audit/T26-report.md。
只改 tasks/scope.json 里 T26a 允许的路径（papers/p1/audit/**）与 tasks/progress/T26a.md；不要改卡片、概念表、corpus、practice。交付：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T26a → push → gh pr create --base main --title "T26a: audit P1 handbook"。PR 描述：审计卡数、问题数（按 severity）、最严重的 5 条、「需要总控决定」。不要合并 PR。停下前更新 tasks/progress/T26a.md 并提交。
```

## codex-2 · T26b 审计 P2 题型手册（跨模型交叉审计；新开 Codex 会话）

```
你是执行工位 codex-2，负责任务 T26b：逐张审计 P2 题型手册（46 张卡，章：AD、DT、PG、SD），只出报告，不改卡片。手册由 Claude 设计工位写成，你是另一家模型的交叉审计。
先读 AGENTS.md（尤其 §5 证据规则）、docs/DECISIONS.md（D1、D2、D15、D25、D26、D29–D32、D37）、tasks/T26-card-audit.md（任务卡：7 个审计项、产出格式、完成标准，严格照做）、schemas/card-format.md、papers/p2/tagging-guide.md。若 tasks/progress/T26b.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T26b-p2-audit。审计范围：papers/p2/front.md、papers/p2/cards/*.md、papers/p2/core/*.md、papers/p2/back.md；先 make build 看 output/p2/ 的成品。每张卡的代表题必须对照该题 QP 与 MS 原页（PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/，只读；用 rows.py render 或 pymupdf / pdftotext），报告里列出每张卡核对的页码。make check 已保证引文逐字存在，你查的是意义：引文是否支持那句说法、满分作答是否真满分、MP 对齐、选题规则、手写计数、原卷页码、概念句、伪代码是否合 2027–29 指南（sources/official/9618_pseudocode_guide_2027-2029.pdf）、Python 片段能否运行.
可以先写脚本做机械检查（选题规则、计数重算、页码引用、伪代码 lint、Python 片段运行），放在 papers/p2/audit/，再逐张人工核对。产出：papers/p2/audit/T26-findings.jsonl（一条问题一行，字段与 kind / severity 取值见任务卡）、papers/p2/audit/T26-report.md。
只改 tasks/scope.json 里 T26b 允许的路径（papers/p2/audit/**）与 tasks/progress/T26b.md；不要改卡片、概念表、corpus、practice。交付：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T26b → push → gh pr create --base main --title "T26b: audit P2 handbook"。PR 描述：审计卡数、问题数（按 severity）、最严重的 5 条、「需要总控决定」。不要合并 PR。停下前更新 tasks/progress/T26b.md 并提交。
```

## codex-1 · T26c 按审计修正 P1 手册（新开 Codex 会话）

```
你是执行工位 codex-1，负责任务 T26c：按 docs/DECISIONS.md D40 修正 P1 题型手册里 T26a 审计找出的 13 条问题（F01–F13 = papers/p1/audit/T26-findings.jsonl 的行序；证据见 papers/p1/audit/T26-report.md）。审计也是你做的，这次把它们改掉。
先读 AGENTS.md（§5 证据规则）、docs/DECISIONS.md（D1、D15、D37、D40）、tasks/T26-fixes.md（任务卡：改法要求、产出、完成标准）、schemas/card-format.md。D40 的四条裁决优先于 findings 里的 suggestion，其中 P1 相关：F12 跟踪表注明 MS 省略 205、211；F04/F05 词条改名为 No partial dependencies（2NF 条件）/ No non-key / transitive dependencies（3NF 条件），英文列保留 MS 原句。
从最新 origin/main 开分支 task/T26c-p1-fixes。只改有问题的地方及审计点名的同类重复表述；满分作答类（F02 EO-05）动笔前重读该题 QP/MS 原页（PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/，只读），重写后与 MS 逐点对齐；F01 示意图改完 make build 后在 output/p1/*.html 里确认。「…」⟦行 id⟧ 只放 MS 原文，新写的非 MS 句子不加「」。
产出 papers/p1/audit/T26-fixes.md（F 编号 → 文件与行 → 改动摘要；error 附改后原文片段），重跑 papers/p1/audit/check_handbook.py 并记录结果。只改 tasks/scope.json 里 T26c 允许的路径与 tasks/progress/T26c.md。交付：git fetch origin && git rebase origin/main → make check → make build → make check-scope TASK=T26c → push → gh pr create --base main --title "T26c: fix P1 handbook per audit"。不要合并 PR。停下前更新 tasks/progress/T26c.md 并提交。
```

## codex-2 · T26d 按审计修正 P2 手册 + P3 指南措辞（新开 Codex 会话）

```
你是执行工位 codex-2，负责任务 T26d：按 docs/DECISIONS.md D40 修正 P2 题型手册里 T26b 审计找出的 13 条问题（F01–F13 = papers/p2/audit/T26-findings.jsonl 的行序；证据见 papers/p2/audit/T26-report.md），并按 D39 同步 P3 指南措辞。审计是你做的，这次把它们改掉。
先读 AGENTS.md（§5 证据规则）、docs/DECISIONS.md（D1、D2、D25、D37、D39、D40）、tasks/T26-fixes.md（任务卡：改法要求、产出、完成标准）、schemas/card-format.md。D40 的裁决优先于 findings 里的 suggestion，其中 P2 相关：F10（SD-03）BOOLEAN 返回值按该题 MS 画实心圆、删去“空心实心都行”。
从最新 origin/main 开分支 task/T26d-p2-fixes。只改有问题的地方及审计点名的同类重复表述（如 F02 的 core/SD.md:115、F09 的 core/DT.md 旧状态说明）；动笔前重读相关 QP/MS 原页（PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/，只读）；伪代码保持 2027–29 指南写法。「…」⟦行 id⟧ 只放 MS 原文，新写的非 MS 句子不加「」。
D39 的 P3 部分：papers/p3/tagging-guide.md §7 加“同票时主题型取题干 / MS 中先出现的那项、其余进 cross、标 low”的判例规则（例 9618_s21_31:3(a)）；§8.2 B 写明“MS 只给填空答案片段时，按 QP 留空行逐行对应拆分，text 取 MS 片段”（例 9618_s22_32:8(a)）；papers/p3/taxonomy.json 的 P3-DR-02 summary 与 DR-04 分界统一（给记录字段赋值含赋枚举值归 DR-04）。只改措辞，不动 rows。
产出 papers/p2/audit/T26-fixes.md（F 编号 → 文件与行 → 改动摘要；error 附改后原文片段；末尾列 D39 三处改动），重跑 papers/p2/audit/check_handbook.py 与 run_python.py 并记录结果。只改 tasks/scope.json 里 T26d 允许的路径与 tasks/progress/T26d.md。交付：git fetch origin && git rebase origin/main → make check → make build → make check-scope TASK=T26d → push → gh pr create --base main --title "T26d: fix P2 handbook per audit"。不要合并 PR。停下前更新 tasks/progress/T26d.md 并提交。
```

## codex-1 · T40 分数线表（新开 Codex 会话）

```
你是执行工位 codex-1，负责任务 T40：把 10 份官方分数线 PDF（sources/pastpapers/9618_<季><yy>_gt.pdf，s21–w25）抽成机器可读表，供冲刺阶段按分数线估分。
先读 AGENTS.md、tasks/T40-grade-thresholds.md（任务卡：产出、规则、完成标准，严格照做）。PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/（只读，不提交）。
从最新 origin/main 开分支 task/T40-grade-thresholds。产出 pipeline/thresholds/extract_gt.py 与 test_gt.py，corpus/thresholds/components.csv、options.csv（utf-8-sig）、README.md（字段、学生四卷对应的 option、加权方式——以 PDF 或考纲原文为准，查不到写“不确定”）、check_report.md（人工抽查 20 格带页码）。数值照 PDF 原样，异常照录。
只改 tasks/scope.json 里 T40 允许的路径与 tasks/progress/T40.md。交付：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T40 → python3 -m pytest pipeline/thresholds → push → gh pr create --base main --title "T40: grade threshold tables"。不要合并 PR。停下前更新 tasks/progress/T40.md 并提交。
```

## codex-2 · T41 整卷模考批改包（新开 Codex 会话）

```
你是执行工位 codex-2，负责任务 T41：写整卷模考批改包生成器。D1 把 2026 年 6 月的 12 份卷留作考前限时模考；学生做完一份后要能照着批改包自己批改、汇总原始分、按分数线估等级。
先读 AGENTS.md（§5：给分只认该题自己的 MS，ER 只作易错）、docs/DECISIONS.md（D1、D33）、tasks/T41-mock-kit.md（任务卡：产出、规则、完成标准，严格照做）、schemas/row.schema.json、corpus/inventory.csv。分数线表 corpus/thresholds/ 由 codex-1 的 T40 同时在做；它合并前估分部分用占位并在 PR 注明，合并后 rebase 接上。
从最新 origin/main 开分支 task/T41-mock-kit。产出 pipeline/mock/make_mock.py（生成 output/mock/<卷 id>/ 的 marking.md、marking.html、score.csv；output/ 不入库）、score_mock.py（汇总、按题型/技能统计失分、估等级、输出可贴进学习记录的摘要）、test_mock.py、README.md。不复制题干（学生看原卷），不显示代表题答案；ER 摘录明确标“仅供易错参考，不是给分依据”。需要 make mock 目标时写进「需要总控决定」，不要改 Makefile。
只改 tasks/scope.json 里 T41 允许的路径与 tasks/progress/T41.md。交付：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T41 → python3 -m pytest pipeline/mock → push → gh pr create --base main --title "T41: mock exam marking kit"。PR 里贴一份 marking.md 开头片段与 12 份 s26 卷的生成清单。不要合并 PR。停下前更新 tasks/progress/T41.md 并提交。
```

## codex-1 · T12f P4 重复行补 equivalent_of + 回写 P3 裁决（新开 Codex 会话）

```
你是执行工位 codex-1，负责任务 T12f：①按 docs/DECISIONS.md D42 ③，给 P4 里 162 行与同季 _41 卷逐字相同的行补 equivalent_of；②按 D41 ⑤ 给 9618_s24_33:10(b) 补 equivalent_of（指向 9618_s24_31:10(b)）；③按 D41 ④ 把 papers/p3/adjudication.csv 的 5 行裁决回写进 pipeline/tag/p3/p3_tags.jsonl。
先读 AGENTS.md、docs/DECISIONS.md（D21、D33、D35、D41、D42）、tasks/T12f-p4-equivalents.md（任务卡：分布表、做法、产出、完成标准，严格照做）。做法照 T12e（#31）：pipeline/extract/p3_equivalents.py 的 scan → 人工审阅清单 → apply → verify，泛化到 P4 时不要改变 P3 的行为。若 tasks/progress/T12f.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T12f-p4-equivalents。每个候选行渲染两卷 QP 原页比对图形（PDF 与 P4 源文件目录在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/，只读），结论写进 pipeline/extract/p4_equivalents_review.json；图形或源文件不同、拿不准的行不补，列进「需要总控决定」。只写 overrides.json，再用 run_all.py 重出 rows，不要手改 jsonl；P3 那 5 行改 p3_tags.jsonl 后跑 apply_p3.py。
用脚本证明只有该变的字段变了：types、markpoints、ms_max、er 等下游字段原样保留（D33），P1/P2 rows 无变化。报告写进 corpus/extract_report.md 的新小节「T12f」。
只改 tasks/scope.json 里 T12f 允许的路径与 tasks/progress/T12f.md。交付：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T12f → apply_p2.py / apply_p3.py / pipeline/er/apply_er.py 的 --check 都 0 改动 → push → gh pr create --base main --title "T12f: link duplicated P4 rows + write back P3 adjudication"。不要合并 PR。停下前更新 tasks/progress/T12f.md 并提交。
```

## codex-2 · T34 P4 全量打标签 + 拆得分点（新开 Codex 会话；可与 T12f 同时开）

```
你是执行工位 codex-2，负责任务 T34：按 papers/p4/tagging-guide.md 给 P4 全部 744 行打题型标签，并按指南 §8 拆得分点。这是跨模型盲标：P4 的题型体系与试标由 Claude（T33）设计，你要独立标出结果，再与试标比一致率。
先读 AGENTS.md、docs/DECISIONS.md（D2、D8、D21、D26、D29、D33、D35、D42）、tasks/T34-p4-tagging.md（任务卡：做法、产出、完成标准都在里面，严格照做）、papers/p4/taxonomy.json、papers/p4/tagging-guide.md、papers/p4/skill_tags.json（extends P2 词表）、schemas/row.schema.json；做法照抄 P3 的 T31（pipeline/tag/p3/ 是现成范本）。若 tasks/progress/T34.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T34-p4-tagging。先盲标全部 744 行（不先看 papers/p4/pilot_*），盲标快照存 pipeline/tag/p4/blind/；再对照 pilot 复核分歧。看图题、截图格回到原页（rows.py render，PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/，只读）。
D42：拆分门槛 ≥ 2 分；只从 MS 开头的语言无关清单切，Java / VB.NET / Python / 伪代码范例不拆；与同季 _41 逐字相同的 162 行（codex-1 的 T12f 正在补 equivalent_of）和已有 equivalent_of 的行，照抄 _41 对应行的标签与得分点。行里已有 er 字段，apply 必须逐字保留（D33）。
T12f 合并后 rebase 时若 corpus/rows/p4/*.jsonl 冲突：取 origin/main 的版本，重跑 apply_p4.py，再重跑全部检查。
只改 tasks/scope.json 里 T34 允许的路径；P2 / P3 的 apply 脚本不要改（需要泛化就写进「需要总控决定」）。交付：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T34 → apply_p4.py --check、pipeline/tag/p3/apply_p3.py --check、pipeline/er/apply_er.py --check 都 0 改动 → push → gh pr create --base main --title "T34: tag P4 rows + split markpoints"。不要合并 PR。停下前更新 tasks/progress/T34.md 并提交。
```

## codex（任一工位）· T36 审计 P3 题型手册（跨模型交叉审计；新开 Codex 会话，可与 T12f / T34 同时开）

```
你是执行工位，负责任务 T36：逐张审计 P3 题型手册（79 张卡，章：DR、CI、HV、BL、SY、SC、AI、CT、FP），只出报告，不改卡片。手册由 Claude 设计工位写成，你是另一家模型的交叉审计。
先读 AGENTS.md（尤其 §5 证据规则）、docs/DECISIONS.md（D1、D2、D10、D25、D26、D29、D33–D35、D37、D39、D40、D41）、tasks/T36-p3-audit.md（任务卡：T26 的 7 项 + P3 特有 5 项、产出格式、完成标准，严格照做）、tasks/T26-card-audit.md（审计项与 findings 字段）、schemas/card-format.md、papers/p3/tagging-guide.md。若 tasks/progress/T36.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T36-p3-audit。审计范围：papers/p3/front.md、cards/*.md、core/*.md、back.md；先 make build 看 output/p3/ 的成品。每张卡的代表题必须对照该题 QP 与 MS 原页（PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/，只读；用 rows.py render 或 pymupdf / pdftotext）。ms_text 会丢布尔表达式的横线、浮点数的上标和图的连线：卡里凡涉及这些的地方，一律看原页渲染图核对，BL 表达式再用真值表验算；Dijkstra、A*、RPN、追踪表按 QP 的图 / 数据重算。D41 已定的例外（变式替代、w24/31 7(d)(ii) 笔误、范围类型）不算问题。
可以先写脚本做机械检查（选题规则、计数重算、页码引用、伪代码 lint、Python 片段运行、真值表），放在 papers/p3/audit/（T26 的 papers/p1/audit/、papers/p2/audit/ 脚本可复制改用），再逐张人工核对。产出：papers/p3/audit/T36-findings.jsonl、papers/p3/audit/T36-report.md（引用行号写纯文本行 id，不用 ⟦⟧；引 MS 用 “”，不用「」）。
只改 tasks/scope.json 里 T36 允许的路径（papers/p3/audit/**）与 tasks/progress/T36.md；不要改卡片、概念表、corpus、practice。交付：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T36 → push → gh pr create --base main --title "T36: audit P3 handbook"。PR 描述：审计卡数、问题数（按 severity）、最严重的 5 条、「需要总控决定」。不要合并 PR。停下前更新 tasks/progress/T36.md 并提交。
```

## 2026-10-24 起：Codex 交接模式（每个任务新开一个 Codex 会话；交接文档在 tasks/handoff/）

### codex · T35a 续做（P4 练习批 1 前半，剩 3 题）

```
你是执行工位，负责 T35a（P4 真题练习，批 1 前半 · s 季，续做）。先读 AGENTS.md、docs/DECISIONS.md（D1、D3、D10、D11、D13、D24、D31、D37 ②、D42、D43）、tasks/T35-p4-practice.md（任务卡：本子批的大题清单在分批表里）、papers/p4/practice-notes.md、schemas/exercise-format.md 末节、tasks/handoff/README.md（通用约定）与 **tasks/handoff/T35-practice.md（交接文档：每道大题的 11 步执行方案、占比口径、已知的坑——严格照做）**。
续做已推的分支 task/T35a-p4-practice（照交接 README §1 建 worktree，不要重开分支）：已完成并提交 6 题（见 tasks/progress/T35a.md 与 practice/p4/manifest-T35a.json），它们就是范本。剩下 9618_s24_42_q3、9618_s25_41_q2、9618_s25_43_q2 三题，然后写 practice/p4/README-T35a.md，全部 9 题都在 manifest 里。
只写 tasks/scope.json 里 T35a 允许的路径与 tasks/progress/T35a.md；共享文件不改。每完成一个单元就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T35a → push → gh pr create --base main --title "T35a: P4 practice (PR/AR/FL/SR/RC, s sessions)"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

### codex · T35b 续做（P4 练习批 1 后半，补验第 8 题）

```
你是执行工位，负责 T35b（P4 真题练习，批 1 后半 · w 季，续做）。先读 AGENTS.md、docs/DECISIONS.md（D1、D3、D10、D11、D13、D24、D31、D37 ②、D42、D43）、tasks/T35-p4-practice.md（任务卡：本子批的大题清单在分批表里）、papers/p4/practice-notes.md、schemas/exercise-format.md 末节、tasks/handoff/README.md（通用约定）与 **tasks/handoff/T35-practice.md（交接文档：每道大题的 11 步执行方案、占比口径、已知的坑——严格照做）**。
续做已推的分支 task/T35b-p4-practice（照交接 README §1 建 worktree，不要重开分支）：前 7 题已完成；第 8 题 practice/p4/9618_w25_43_q3 是上一个工位中断前的 WIP 提交（a0e7778，未验证；总控检查时缺 task.md）——逐项检查（task.md 转写与证据对照表、files sha256、测试、参考解、≥2 mutant），按执行方案第 10 步验证，缺的补齐，再写 practice/p4/manifest-T35b.json（8 题）与 README-T35b.md。
只写 tasks/scope.json 里 T35b 允许的路径与 tasks/progress/T35b.md；共享文件不改。每完成一个单元就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T35b → push → gh pr create --base main --title "T35b: P4 practice (PR/AR/FL/SR/RC, w sessions)"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

### codex · T35c 新开（P4 练习批 2 前半 · SQ/LT（10 题））

```
你是执行工位，负责 T35c（P4 真题练习，批 2 前半 · SQ/LT（10 题））。先读 AGENTS.md、docs/DECISIONS.md（D1、D3、D10、D11、D13、D24、D31、D37 ②、D42、D43）、tasks/T35-p4-practice.md（任务卡：本子批的大题清单在分批表里）、papers/p4/practice-notes.md、schemas/exercise-format.md 末节、tasks/handoff/README.md（通用约定）与 **tasks/handoff/T35-practice.md（交接文档：每道大题的 11 步执行方案、占比口径、已知的坑——严格照做）**。
新任务：从最新 origin/main 开分支 task/T35c-p4-practice（照交接 README §1）。大题清单见任务卡分批表的 T35c 行。先读 T35a / T35b 已完成的 2–3 道练习作范本（分支 origin/task/T35a-p4-practice、origin/task/T35b-p4-practice，可用 git show 或另建只读 worktree 查看），再逐题按执行方案做。
只写 tasks/scope.json 里 T35c 允许的路径与 tasks/progress/T35c.md；共享文件不改。每完成一个单元就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T35c → push → gh pr create --base main --title "T35c: P4 practice (SQ/LT, s sessions + w22_41)"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

### codex · T35d 新开（P4 练习批 2 后半 · SQ/LT（9 题））

```
你是执行工位，负责 T35d（P4 真题练习，批 2 后半 · SQ/LT（9 题））。先读 AGENTS.md、docs/DECISIONS.md（D1、D3、D10、D11、D13、D24、D31、D37 ②、D42、D43）、tasks/T35-p4-practice.md（任务卡：本子批的大题清单在分批表里）、papers/p4/practice-notes.md、schemas/exercise-format.md 末节、tasks/handoff/README.md（通用约定）与 **tasks/handoff/T35-practice.md（交接文档：每道大题的 11 步执行方案、占比口径、已知的坑——严格照做）**。
新任务：从最新 origin/main 开分支 task/T35d-p4-practice（照交接 README §1）。大题清单见任务卡分批表的 T35d 行。先读 T35a / T35b 已完成的 2–3 道练习作范本（分支 origin/task/T35a-p4-practice、origin/task/T35b-p4-practice，可用 git show 或另建只读 worktree 查看），再逐题按执行方案做。
只写 tasks/scope.json 里 T35d 允许的路径与 tasks/progress/T35d.md；共享文件不改。每完成一个单元就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T35d → push → gh pr create --base main --title "T35d: P4 practice (SQ/LT, w sessions)"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

### codex · T35e 新开（P4 练习批 3 前半 · OP（9 题））

```
你是执行工位，负责 T35e（P4 真题练习，批 3 前半 · OP（9 题））。先读 AGENTS.md、docs/DECISIONS.md（D1、D3、D10、D11、D13、D24、D31、D37 ②、D42、D43）、tasks/T35-p4-practice.md（任务卡：本子批的大题清单在分批表里）、papers/p4/practice-notes.md、schemas/exercise-format.md 末节、tasks/handoff/README.md（通用约定）与 **tasks/handoff/T35-practice.md（交接文档：每道大题的 11 步执行方案、占比口径、已知的坑——严格照做）**。
新任务：从最新 origin/main 开分支 task/T35e-p4-practice（照交接 README §1）。大题清单见任务卡分批表的 T35e 行。先读 T35a / T35b 已完成的 2–3 道练习作范本（分支 origin/task/T35a-p4-practice、origin/task/T35b-p4-practice，可用 git show 或另建只读 worktree 查看），再逐题按执行方案做。
只写 tasks/scope.json 里 T35e 允许的路径与 tasks/progress/T35e.md；共享文件不改。每完成一个单元就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T35e → push → gh pr create --base main --title "T35e: P4 practice (OP, s sessions)"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

### codex · T35f 新开（P4 练习批 3 后半 · OP（9 题））

```
你是执行工位，负责 T35f（P4 真题练习，批 3 后半 · OP（9 题））。先读 AGENTS.md、docs/DECISIONS.md（D1、D3、D10、D11、D13、D24、D31、D37 ②、D42、D43）、tasks/T35-p4-practice.md（任务卡：本子批的大题清单在分批表里）、papers/p4/practice-notes.md、schemas/exercise-format.md 末节、tasks/handoff/README.md（通用约定）与 **tasks/handoff/T35-practice.md（交接文档：每道大题的 11 步执行方案、占比口径、已知的坑——严格照做）**。
新任务：从最新 origin/main 开分支 task/T35f-p4-practice（照交接 README §1）。大题清单见任务卡分批表的 T35f 行。先读 T35a / T35b 已完成的 2–3 道练习作范本（分支 origin/task/T35a-p4-practice、origin/task/T35b-p4-practice，可用 git show 或另建只读 worktree 查看），再逐题按执行方案做。
只写 tasks/scope.json 里 T35f 允许的路径与 tasks/progress/T35f.md；共享文件不改。每完成一个单元就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T35f → push → gh pr create --base main --title "T35f: P4 practice (OP, w sessions)"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

### codex · T37A 续做（P4 卡：FL / SR / RC + front）

```
你是执行工位，续做 T37A（P4 题型卡，设计类产物）。先读 AGENTS.md（§5 证据规则）、docs/DECISIONS.md（D1、D2、D10、D13、D24、D25、D31、D33、D37、D40–D44）、**tasks/T37-p4-cards.md（任务卡：卡片结构、Python 模板 / 得分点地图 / 对应练习三项、选题规则、六条审计教训——全文照做）**、schemas/card-format.md、papers/p4/taxonomy.json、papers/p4/tagging-guide.md、papers/p4/skill_tags.json、corpus/tag_report_p4.md、tasks/handoff/README.md 与 **tasks/handoff/T37-cards.md（交接文档：现状、工具、每张卡的执行方案）**。
续做已推的分支 task/T37A-p4-cards（照交接 README §1 建 worktree）：PR、AR 两章已完成，是你的质量标杆，先通读。剩下 FL、SR、RC 三章（cards + core，进度日志里已预选代表题与变式，核对原页后再用）与 papers/p4/front.md。每张卡的完整作答都要写成可运行的整题 Python，在官方源文件 / QP 测试数据上跑过，输出与 MS 一致；工具见交接文档（~/Desktop/alevel-cs-wt/handoff/t37b-scripts/ 复制到 work/tmp/）。
只写 tasks/scope.json 里 T37A 允许的路径与 tasks/progress/T37A.md；共享文件不改。每完成一个单元就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check → python3 build/build.py p4 → make check-scope TASK=T37A → push → gh pr create --base main --title "T37 batch A: P4 front + PR/AR/FL/SR/RC cards"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

### codex · T37B 续做（P4 卡：OP / MP + back）

```
你是执行工位，续做 T37B（P4 题型卡，设计类产物）。先读 AGENTS.md（§5 证据规则）、docs/DECISIONS.md（D1、D2、D10、D13、D24、D25、D31、D33、D37、D40–D44）、**tasks/T37-p4-cards.md（任务卡：卡片结构、Python 模板 / 得分点地图 / 对应练习三项、选题规则、六条审计教训——全文照做）**、schemas/card-format.md、papers/p4/taxonomy.json、papers/p4/tagging-guide.md、papers/p4/skill_tags.json、corpus/tag_report_p4.md、tasks/handoff/README.md 与 **tasks/handoff/T37-cards.md（交接文档：现状、工具、每张卡的执行方案）**。
续做已推的分支 task/T37B-p4-cards（照交接 README §1 建 worktree）：SQ、LT 两章已完成，是你的质量标杆，先通读。剩下 OP（7 型）、MP（3 型，含截图证据格的讲法）两章（cards + core）与 papers/p4/back.md。每张卡的完整作答都要写成可运行的整题 Python，在官方源文件 / QP 测试数据上跑过，输出与 MS 一致；上一个工位的脚本与已跑程序在 ~/Desktop/alevel-cs-wt/handoff/t37b-scripts/（复制到 work/tmp/t37b/）。
只写 tasks/scope.json 里 T37B 允许的路径与 tasks/progress/T37B.md；共享文件不改。每完成一个单元就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check → python3 build/build.py p4 → make check-scope TASK=T37B → push → gh pr create --base main --title "T37 batch B: P4 SQ/LT/OP/MP cards + back"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

### codex · T38 审计 P4 题型手册（新开 Codex 会话）

```
你是执行工位，负责 T38：逐张审计 P4 题型手册（36 张卡）并抽查 6 道 P4 真题练习，只出报告，不改卡片与练习。先读 AGENTS.md（§5 证据规则）、docs/DECISIONS.md（D1、D2、D10、D31、D37、D40–D45）、tasks/T38-p4-audit.md（任务卡：范围、10 项审计项、产出格式）、tasks/handoff/README.md 与 **tasks/handoff/T38-audit.md（交接文档：执行方案）**，再通读 papers/p2/audit/T26-report.md、papers/p3/audit/T36-report.md 学前例的格式与口径。
从最新 origin/main 开分支 task/T38-p4-audit。每张卡的代表题都要渲染 QP 与 MS 原页核对；每个完整作答的 Python 都要在官方源文件 / QP 测试数据上实际运行（PDF 与源文件在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/，只读）。报告与 jsonl 用纯文本行 id，不用 ⟦⟧ 与「」。
只写 tasks/scope.json 里 T38 允许的路径与 tasks/progress/T38.md；共享文件不改。每完成一个单元就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T38 → push → gh pr create --base main --title "T38: audit P4 handbook"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

### ~~codex · T39 教学 skill 更新到全四卷~~（作废：学生指定改由 Claude Opus 子智能体做，不要发给 Codex）

```
你是执行工位，负责 T39：把教学 skill skill/cie-9618-cs-tutor/ 更新到能教全四卷（P3、P4 手册与 P4 上机练习）、能带整卷模考（批改包 + 分数线估分），并生成 ledger/P3.csv、ledger/P4.csv。skill 是给 Claude 学习会话看的说明书，保持原口吻，不改教学协议本身。先读 AGENTS.md、docs/DECISIONS.md（D1、D2、D31、D32、D33、D37、D38、D44、D45）、tasks/T39-skill-update.md（任务卡：现状、9 项改动、完成标准）、tasks/handoff/README.md 与 **tasks/handoff/T39-skill.md（交接文档：执行方案）**；改之前先读 pipeline/mock/README.md、corpus/thresholds/README.md、papers/p4/practice-notes.md、schemas/exercise-format.md、schemas/ledger-format.md、tools/try.py，命令以它们为准。
从最新 origin/main 开分支 task/T39-skill-update。skill 里写到的每条命令都要实际跑一次（模考包用一份 s26 卷、score_mock 用假数据、make try 用一道 P4 练习的参考解加 K=），生成物放 output/ 或 work/tmp/，不入库；ledger/P1.csv、P2.csv、ladder.csv 是学生的真实记录，不要改。
只写 tasks/scope.json 里 T39 允许的路径与 tasks/progress/T39.md；共享文件不改。每完成一个单元就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T39 → push → gh pr create --base main --title "T39: update tutor skill for P3/P4, mocks and thresholds"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

## T38 修正（#57 合并后发出；T38b、T38c1、T38c2、T38c3 四个会话可并行）

### codex · T38b 改 P4 卡 + OP 换题（新开 Codex 会话）

```
你是执行工位，负责 T38b：按 D46 修正 P4 题型卡 F01–F04，并把 OP-02、OP-03、OP-07 的代表题换成审计建议的三道。前提：#57（T38 审计报告）已合并进 main。先读 AGENTS.md（§5 证据规则）、docs/DECISIONS.md（D10、D13、D31、D37、D40–D46）、tasks/T38-fixes.md（任务卡）、tasks/handoff/README.md 与 **tasks/handoff/T38-fixes.md（交接文档：执行方案）**、papers/p4/audit/T38-report.md 与 T38-findings.jsonl（F01–F09 = jsonl 行序）。
另读 tasks/T37-p4-cards.md（卡片标准）、tasks/handoff/T37-cards.md（写卡执行方案与工具）、papers/p4/cards/OP.md 全章。从最新 origin/main 开分支 task/T38b-p4-card-fixes。新代表题要对照 QP / MS 原页（/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/，只读），完整作答是可运行的整题 Python，在官方源文件 / QP 数据上跑过、输出与 MS 一致。
只写 tasks/scope.json 里 T38b 允许的路径与 tasks/progress/T38b.md；共享文件（tools/、schemas/ 等）不改。每完成一个单元就提交并更新进度日志。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check → python3 build/build.py p4 → make check-scope TASK=T38b → push → gh pr create --base main --title "T38b: fix P4 handbook per audit (incl. OP rep swaps)"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡要求的内容与「需要总控决定」。
```

### codex · T38c1 排查 P4 练习（T35a + T35b 的 17 道；新开 Codex 会话）

```
你是执行工位，负责 T38c1：按 D46 排查并修正 T35a + T35b 的 17 道 P4 真题练习（练习目录清单见 tasks/scope.json 的 T38c1）。前提：#57（T38 审计报告）已合并进 main。先读 AGENTS.md（§5 证据规则）、docs/DECISIONS.md（D10、D13、D31、D37、D40–D46）、tasks/T38-fixes.md（任务卡）、tasks/handoff/README.md 与 **tasks/handoff/T38-fixes.md（交接文档：执行方案）**、papers/p4/audit/T38-report.md 与 T38-findings.jsonl（F01–F09 = jsonl 行序）。
另读 schemas/exercise-format.md 末节 P4 规则（第 6、7 条是 D46 新加的）、papers/p4/practice-notes.md、tools/testkit.py 的 run_script_traced。审计已发现的本组问题：F05 9618_s24_42_q3——先修它们，再逐题排查其余练习的同类问题（调用链漏测、过严断言），每道含主程序的练习加 ref/mutant_hollow_main.py，并用 1–2 个等价正确改写自测。从最新 origin/main 开分支 task/T38c1-p4-practice。
只写 tasks/scope.json 里 T38c1 允许的路径与 tasks/progress/T38c1.md；共享文件（tools/、schemas/ 等）不改。每完成一个单元就提交并更新进度日志。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T38c1 → push → gh pr create --base main --title "T38c1: harden P4 practice tests (call chains, over-strict output)"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡要求的内容与「需要总控决定」。
```

### codex · T38c2 排查 P4 练习（T35c + T35d 的 19 道；新开 Codex 会话）

```
你是执行工位，负责 T38c2：按 D46 排查并修正 T35c + T35d 的 19 道 P4 真题练习（练习目录清单见 tasks/scope.json 的 T38c2）。前提：#57（T38 审计报告）已合并进 main。先读 AGENTS.md（§5 证据规则）、docs/DECISIONS.md（D10、D13、D31、D37、D40–D46）、tasks/T38-fixes.md（任务卡）、tasks/handoff/README.md 与 **tasks/handoff/T38-fixes.md（交接文档：执行方案）**、papers/p4/audit/T38-report.md 与 T38-findings.jsonl（F01–F09 = jsonl 行序）。
另读 schemas/exercise-format.md 末节 P4 规则（第 6、7 条是 D46 新加的）、papers/p4/practice-notes.md、tools/testkit.py 的 run_script_traced。审计已发现的本组问题：F06 9618_s25_42_q1、F07 9618_w24_41_q3——先修它们，再逐题排查其余练习的同类问题（调用链漏测、过严断言），每道含主程序的练习加 ref/mutant_hollow_main.py，并用 1–2 个等价正确改写自测。从最新 origin/main 开分支 task/T38c2-p4-practice。
只写 tasks/scope.json 里 T38c2 允许的路径与 tasks/progress/T38c2.md；共享文件（tools/、schemas/ 等）不改。每完成一个单元就提交并更新进度日志。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T38c2 → push → gh pr create --base main --title "T38c2: harden P4 practice tests (call chains, over-strict output)"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡要求的内容与「需要总控决定」。
```

### codex · T38c3 排查 P4 练习（T35e + T35f 的 18 道；新开 Codex 会话）

```
你是执行工位，负责 T38c3：按 D46 排查并修正 T35e + T35f 的 18 道 P4 真题练习（练习目录清单见 tasks/scope.json 的 T38c3）。前提：#57（T38 审计报告）已合并进 main。先读 AGENTS.md（§5 证据规则）、docs/DECISIONS.md（D10、D13、D31、D37、D40–D46）、tasks/T38-fixes.md（任务卡）、tasks/handoff/README.md 与 **tasks/handoff/T38-fixes.md（交接文档：执行方案）**、papers/p4/audit/T38-report.md 与 T38-findings.jsonl（F01–F09 = jsonl 行序）。
另读 schemas/exercise-format.md 末节 P4 规则（第 6、7 条是 D46 新加的）、papers/p4/practice-notes.md、tools/testkit.py 的 run_script_traced。审计已发现的本组问题：F08 9618_s24_41_q2、F09 9618_w25_42_q1——先修它们，再逐题排查其余练习的同类问题（调用链漏测、过严断言），每道含主程序的练习加 ref/mutant_hollow_main.py，并用 1–2 个等价正确改写自测。从最新 origin/main 开分支 task/T38c3-p4-practice。
只写 tasks/scope.json 里 T38c3 允许的路径与 tasks/progress/T38c3.md；共享文件（tools/、schemas/ 等）不改。每完成一个单元就提交并更新进度日志。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check-all → make check-scope TASK=T38c3 → push → gh pr create --base main --title "T38c3: harden P4 practice tests (call chains, over-strict output)"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡要求的内容与「需要总控决定」。
```

## T50b 之后（2026-10-25；T51、T52、T53 三个会话互不依赖，可并行）

### codex · T51 开场检索题库（新开 Codex 会话）

```
你是执行工位，负责 T51：为教学 skill 建一个按题型码组织、答案带 MS 证据的开场检索题库（★★★ 每型 2 道、★★☆ 每型 1 道，共 169 个题型），并写抽题脚本 retrieval.py。先读 AGENTS.md（§5 证据规则）、docs/DECISIONS.md（D1、D2、D10、D40、D47）、tasks/T51-retrieval-bank.md（任务卡）、tasks/handoff/README.md 与 **tasks/handoff/T51-retrieval.md（交接文档：题库格式、脚本规格、逐章执行方案、坑——严格照做）**，再读 skill/cie-9618-cs-tutor/references/few-shots.md 的「六种探针」「把错误转成下一道题」两节与示例 6–8。
从最新 origin/main 开分支 task/T51-retrieval-bank。先写脚本与 README、用 P1 IR 两三个题型试通格式，再按 P1 → P2 → P3 → P4 逐章写题；每道题只测一环、30 秒英文答完；MS 原句逐字写成「…」⟦行 id⟧，只引该题型卡或该章概念表已出现的行，不用 s26 行；代码答案标「非 MS 原文」。ledger/ 下的真实记录表不要改，实测用 work/tmp/ 里的副本。
只写 tasks/scope.json 里 T51 允许的路径与 tasks/progress/T51.md；SKILL.md 与其他共享文件不改。每完成一章就提交并更新进度日志（随时可能被中断）。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → python3 skill/cie-9618-cs-tutor/scripts/retrieval.py check → make check → make check-scope TASK=T51 → push → gh pr create --base main --title "T51: opening retrieval bank and picker"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容与「需要总控决定」。
```

### codex · T52 P3 DR、P4 LT 心智模型（新开 Codex 会话）

```
你是执行工位，负责 T52：在 papers/p3/cards/DR.md 与 papers/p4/cards/LT.md 的「核心思想」末尾各加一段「心智模型」，把整章讲成一两幅能推出题型的图，结尾告诉学生看到题先定位到图的哪里。先读 AGENTS.md、docs/DECISIONS.md（D2、D10、D24）、tasks/T52-chapter-models.md（任务卡）、tasks/handoff/README.md 与 **tasks/handoff/T52-models.md（交接文档：范本、写作方向、执行方案、坑）**；范本是 papers/p1/cards/HW.md 第 15 行等 T50b 新加的四段心智模型，衔接读 docs/guide/concept-threads.md。
从最新 origin/main 开分支 task/T52-chapter-models。只加新段，不动原有段落、题型卡、引文与选题；新段不写「」；每个模型句落到本章题型码上；下标与空指针约定写“以本题题干为准”。
只写 tasks/scope.json 里 T52 允许的路径与 tasks/progress/T52.md；共享文件不改。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → make check → python3 build/build.py p3 → python3 build/build.py p4 → make check-scope TASK=T52 → push → gh pr create --base main --title "T52: mental models for P3 DR and P4 LT"。不要合并 PR，不要推 main。
PR 描述贴出两段新文字全文、每幅图能推出哪些题型，以及「需要总控决定」。
```

### codex · T53 指南进构建 + 引文正则（新开 Codex 会话）

```
你是执行工位，负责 T53：让构建器把 docs/guide/*.md 生成成和手册同样式的 output/guide/*.md 与 .html（build.py 新命令 guide，all 包含它），并修 build/markdown.py 引文正则跨越「」吞文本的问题（T50 M1）。先读 AGENTS.md、tasks/T53-guide-build.md（任务卡）、tasks/handoff/README.md 与 **tasks/handoff/T53-guide-build.md（交接文档：执行方案、测试要求、坑）**，再读 build/README.md、build/build.py（build_ladder 是范本）、build/markdown.py、build/tests/。
从最新 origin/main 开分支 task/T53-guide-build。先用 --out work/tmp/before 留一份构建基线；正则先写失败的回归测试再修；guide 构建加夹具测试；最后 --out work/tmp/after 再构建，diff 两份 .md 输出，逐处说明差异。output/ 与 work/tmp/ 不提交。
只写 tasks/scope.json 里 T53 允许的路径（build/**）与 tasks/progress/T53.md；tools/、Makefile、docs/ 不改。交付照 tasks/handoff/README.md §6–7：git fetch origin && git rebase origin/main → ~/.venvs/alevel-cs/bin/python -m pytest build/tests -q → python3 build/build.py all → make check → make check-scope TASK=T53 → push → gh pr create --base main --title "T53: build docs/guide and fix quote regex"。不要合并 PR，不要推 main。
最后在 PR 描述里写全任务卡「完成标准」要求的内容（含构建前后对比）与「需要总控决定」。
```
