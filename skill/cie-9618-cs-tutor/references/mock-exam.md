# 整卷模考、考前冲刺与估分

> 在 SKILL.md 的共用协议之下使用。给分只认每题自己的 MS；批改包与估分工具的真源说明在 `pipeline/mock/README.md` 与 `corpus/thresholds/README.md`，命令以它们为准。

## 1. 卷与时间安排

| 资源 | 内容 | 用法 |
|:--|:--|:--|
| `9618_s26_*`（12 份：11–13、21–23、31–33、41–43） | D1 保留，平时专项、复测、变式都跳过 | 4–5 月限时整卷模考；有批改包 |
| 2021 样卷 `sources/official/specimen/9618_y21_sp_<qp\|ms\|in>_<n>.pdf`；P4 题卷与证据文档在 `9618_y21_sp_qp_4/`、源文件在 `9618_y21_sp_sf_4/` | 不在 `corpus/rows`，没有批改包 | 冲刺整卷，按样卷自己的 MS 手工批；P1–P3 有 Specimen Paper Answers 可对照 |
| 用得最少的往年卷 | 在记录表「独立题目」「复测结果」里出现最少的卷（`rows.py find --paper <卷>` 列出该卷各行与题型） | s26 用完后的补充整卷；`make_mock.py` 也能给普通卷（含 2021）生成批改包 |

时长（2027–29 考纲 p.11，批改包里也会写）：P1、P3 90 分钟；P2 120 分钟；P4 150 分钟；每卷 75 分。

建议节奏（学生可改）：4 月第 1–2 周做一套 variant 1（11 / 21 / 31 / 41）当诊断，之后两周按失分回炉；4 月底 – 5 月初做 variant 2（12 / 22 / 32 / 42）；考前两到三周做 variant 3。一天最多一卷，P4 单独排一个整块时间。

## 2. 考前准备（学生做题前）

1. 确认卷别与时长：`python3 skill/cie-9618-cs-tutor/scripts/rows.py files 9618_s26_22` 列出 QP、MS、插页、源文件的路径——**只告诉学生 QP（与插页、源文件）的路径**，不打开 MS，也先不生成批改包（README：做完后才打开批改包）。
2. 作答方式：
   - **P1 / P2 / P3**：考试是纸笔。优先打印 QP 手写、做完拍照发来（HEIC 用 SKILL.md §9 的 `sips` 转换）；也可以在 `attempts/mock/<卷>/answers.md` 里打字（伪代码写进代码块）。P2 带当卷插页（`9618_s26_in_2x.pdf`）。
   - **P4**：你把该卷源文件目录里的 `.txt` 复制到 `attempts/mock/<卷>/`（只复制数据文件，不改原件；有的卷多套一层目录，所以用 find）：

     ```bash
     mkdir -p attempts/mock/9618_s26_42 && find "/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/9618_s26_sf_42" -name "*.txt" -exec cp {} attempts/mock/9618_s26_42/ \;
     ```

     学生在那里按题目要求的文件名写程序（如 `Question1_J26.py`），并按证据文档的格子顺序维护 `attempts/mock/<卷>/evidence.md`：每个代码格贴代码，每个截图格贴运行输出。
3. 学生自己计时，记下开始、结束时间；超时部分用另一种颜色或标「超时」，批改时分开算。

## 3. 生成批改包

学生交卷后：

```bash
python3 pipeline/mock/make_mock.py 9618_s26_22
```

生成 `output/mock/9618_s26_22/marking.html`、`marking.md`、`score.csv`。每个小问一节：主题型（链接到手册）、本题 MS 原页页码、**本题 MS 原文**、拆好的得分点勾选表、考官报告摘录（s26 一般「无摘录」）。脚本不覆盖已有的 `score.csv`；要重新生成就用 `--out <别的目录>`，原来的批改记录先保管好。

## 4. 自批、复核与估分

1. **学生自批**：打开批改包（`open output/mock/9618_s26_22/marking.html`），逐小问对 MS 打分；图、表、代码排版回原页。在 `score.csv` 填 `marks_awarded`（未得分填 0，空着表示未批）；`lost_skills` 可填 `loop-to-eof=2;file-close=1`（标签取技能词表，数值为正整数，一分只归一个技能，拿不准留空）；`note` 写失分原因或疑问。
2. **你复核**（逐卷，一条回复一卷）：
   - 每个丢分小问：对照该题 MS 确认丢的是哪一点，给出可得分的写法，归错误类别；
   - 全部写代码小问（P2 伪代码、P3 伪代码、P4 程序）逐点重批：P2 / P3 按 programming.md §6 的伪代码规则；P4 由你按 QP 测试数据运行学生程序（p4-practical.md §5 的 `run_script`，`files_dir` 指向 `attempts/mock/<卷>/`），并按 MS 核对每个证据格；
   - 再抽查至少 3 个学生给了分的非代码小问（自批往往偏松）；
   - 发现评分不一致，和学生说明理由后改正 `score.csv`。
3. **汇总与估分**：

   ```bash
   python3 pipeline/mock/score_mock.py output/mock/9618_s26_22/score.csv
   ```

   输出原始分、按主题型失分、按技能失分，以及「参考等级」：单卷取分数线表里**最新一季、同一 component**（如 22）的 A–E。四卷都做完、且是同一组 variant（如 12 / 22 / 32 / 42）时，四份一起传，按最新一季的 option 估 A Level 总等级（满分 300，四卷原始分直接相加）：

   ```bash
   python3 pipeline/mock/score_mock.py output/mock/9618_s26_12/score.csv output/mock/9618_s26_22/score.csv \
     output/mock/9618_s26_32/score.csv output/mock/9618_s26_42/score.csv
   ```

   option 对应（`corpus/thresholds/README.md`）：11/21/31/41 → AX，12/22/32/42 → AY，13/23/33/43 → AZ。学生实际报考的 variant 还不知道；历史分数线只用于估计，**不是 2027 的等级线**，向学生说清楚。
4. **存档**：`output/` 不进 git。把复核后的 `score.csv` 复制到 `attempts/mock/<卷>/score.csv`，把 `score_mock.py` 的摘要贴进 `attempts/mock/<卷>/summary.md`，随学习记录提交。

## 5. 回炉：把失分落到题型

1. 按 `score_mock.py` 的「按主题型失分」逐型处理（SKILL.md §10.4）：在该型「复测结果」写 `<行 id> x/y（模考）`；已掌握的型因非笔误丢了 MS 得分点 → 改回学习中、写缺口、复测日期排在一周内；学习中的型补一个新的复测日期；还是未学的型只追加「首学前已做」（SKILL.md §10.2）；笔误只记不改状态。
2. 「按技能失分」里累计两分以上的技能：`rows.py find --skill <标签>` 找非 s26 的同技能小问做针对练习，并回到对应阶梯卡。
3. 给学生一份模考报告（写进交接文档）：原始分与参考等级；失分最多的 5 个题型（各附下一道刷题）；失分技能排行；写不出的定义句与解释链；时间分配（哪题超时）。
4. 往年同卷号的考官报告总评（`corpus/er/<季>.jsonl` 里该卷 `label` 为 `_general` 的条目：Key messages / General comments）可以作为「这类卷常见失分」的补充读物，展示为「考官报告指出 …」，不作给分依据；s26 本身没有考官报告。
5. 做完一卷后可以展示该卷号对应的范答（ECR 2021 覆盖 s21 13 / 22 / 32 / 42，Example Responses 2024 覆盖 s24 13 / 22 / 32 / 42）作为「怎样写更稳」的示范。

## 6. 冲刺期的混合题组

整卷之间穿插：

- **混合题组**：8–12 个小问，跨章混排、**不报题型**（`rows.py` 输出里的题型码不转给学生），优先 ★★★ 与学习中的型，题取非 s26、没做过的；包含定义 / 解释句默写（概念表英文列、手册书末的解释链）。
- **编程限时**：P2 写代码题按分值 × 1.5 分钟、P4 小问按分值 × 2 分钟计时，用练习文件夹（p4-practical.md §3 第 5 步的整题）。
- 每组之后报告：按题型列得分；要回炉的题型各附下一道刷题；写不出的英文句。

## 7. 记录与交接

- 记录表只记题型层面的证据（§5 第 1 条）；整卷分数、参考等级、时间分配写在交接文档「进度总览」下的「模考」表：卷 · 日期 · 用时 · 原始分 · 参考等级（分数线来源）· 失分最多的题型。
- 模考做完、复核完、记录写完之后，按 SKILL.md §12 提交 `ledger handoff attempts`。
