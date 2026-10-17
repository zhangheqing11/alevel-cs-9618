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
