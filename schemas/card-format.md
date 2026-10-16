# 手写内容格式：题型卡、概念表、阶梯对照卡

构建器（T13）读取这些 markdown，填入自动生成的块，产出 `output/` 下的 md/html/json。校验器（`make check`）检查引文与题号。

## 1. 文件布局

```
papers/p<N>/
  taxonomy.json          # 章节与题型清单（schema: taxonomy.schema.json）
  skill_tags.json        # 仅 P2/P4：得分点技能标签词表
  front.md               # 卷首：使用指南、考情总览、通用得分规则（可含 auto 块）
  cards/<章节码>.md       # 一章一个文件：章首 + 该章全部题型卡 + 易混辨析
  core/<章节码>.md        # 核心概念表（P1/P3 必需；P2/P4 写「伪代码 ↔ Python 对照与模板」）
  back.md                # 书末：跨章入口、解释题得分链、勘误等
ladder/
  design.md              # 阶梯总设计
  levels/L<nn>-<slug>/card.md   # 每级对照卡
```

## 2. 章文件 `cards/<章节码>.md`

```markdown
## DB　Databases {#ch-DB}

<!-- auto:chapter-stats -->

### 核心思想
……

### 题型树
<!-- auto:type-tree -->

### P1-DB-03　范式化与第三范式　{#P1-DB-03}

<!-- auto:stats P1-DB-03 -->

**考法**　……
**识别信号**　……
**解题思路**
1. ……
**得分表述**（引自对应 MS）
- 「a table is in 3NF if it is in 2NF and contains no non-key dependencies」⟦9618_s24_12:8(b)(i)⟧
**易错与失分**　……（可引 ER：⟦9618_s24_12:8(b)(i)⟧ 的 `er` 字段）

#### 代表题精讲　⟦9618_s24_12:8(b)(i)⟧
……逐步解答，每步对应 MS 分点……

**下一道变式**　⟦9618_w23_11:7(c)⟧

<!-- auto:drills P1-DB-03 -->

### 本章易混辨析
| 容易混 | 区别 | 判断信号 |
```

- 题型卡标题必须是 `### <题型码>　<中文名>　{#<题型码>}`（全角空格分隔），题型码必须在 `taxonomy.json` 里。**星级不手写**，由构建器按统计算出填入。
- `<!-- auto:… -->` 块由构建器填：`chapter-stats`、`type-tree`、`stats <码>`（考情：小问数、分值、出现卷数、设问分布、★）、`drills <码>`（2022–26 刷题清单，新卷在前；2021 扩展单列）。手写内容不要写这些数据。

## 3. 引文与题号语法（机器校验）

- **题号引用**：`⟦<行 id>⟧`，如 `⟦9618_s24_22:3(b)(ii)⟧`。校验：该行必须存在于 `corpus/rows/`。
- **MS 原文引用**：`「<MS 原文片段>」⟦<行 id>⟧`。校验：片段（忽略大小写、合并空白、忽略首尾标点）必须是该行 `ms_text` 的子串。**意译不要用「」**，用普通文字并附题号即可。
- 一张卡里「得分表述」的每一条都必须是 MS 原文引用。
- 伪代码与 Python 用围栏代码块，语言标注 `pseudocode` 或 `python`。

## 4. 核心概念表 `core/<章节码>.md`（P1/P3）

每个术语一行，三层：

| 术语 | 英文得分句（MS 原文，带引用） | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Primary key | 「a field / attribute that uniquely identifies each record」⟦9618_…⟧ | 唯一标识表中每条记录的字段 | 像学号：每人一个、不重复 | P1-DB-01 |

## 5. 阶梯对照卡 `ladder/levels/L<nn>-<slug>/card.md`

必需小节：`## 本级目标`、`## 伪代码 ↔ Python 对照`（两列或成对代码块，伪代码严格按 2027–29 伪代码指南）、`## 常见坑`、`## 延伸阅读`（CS50P / Think Python 3e 的具体讲次或章节链接，注明 CC BY-NC-SA）、`## 练习`（列出本级 `exercises/E<nn>-<slug>/`）。
