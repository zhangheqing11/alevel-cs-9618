# T01 · 下载、清单与配对（总控）

- 官网公开文件 → `sources/official/`：2027–2029 考纲、考纲更新说明、伪代码指南。
- PapaCambridge → `sources/pastpapers/`：2021–2026s、四卷全部 variant 的 `qp`、`ms`、`in`（P2 插页）、`sf`（P4 源文件）、`er`、`gt`。先试 2 个文件，学生批准后全量。
- 脚本 `pipeline/download/`（可重跑、跳过已有文件、记录失败）。
- 产出 `corpus/inventory.csv`（`schemas/corpus-format.md`）、`corpus/download_report.md`（缺失清单、重复 variant、文件大小）。
- 完成后通知 codex-1 开始 T12。
