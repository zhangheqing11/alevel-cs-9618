# alevel-cs-9618

CIE AS & A Level Computer Science 9618 个人学习系统（P1–P4，2027 年 5–6 月考）。

- 方案：`docs/PLAN.md`
- 协作规则（所有 agent 必读）：`AGENTS.md`
- 任务看板：`tasks/BOARD.md`；Codex 启动提示词：`tasks/PROMPTS.md`
- 常用命令：`make setup`（首次）· `make check` · `make build` · `make try EX=<练习目录>`

原始资料（真题 PDF、教材）在本地 `sources/`，不入库。

首次在另一台电脑使用时，可先运行 `python3 tools/check_sources.py` 检查本地官方资料是否齐全。脚本读取 `ALEVEL_CS_SOURCES`；未设置时仍使用默认路径 `/Users/zhangheqing/Desktop/alevel cs/sources`。也可以用 `python3 tools/check_sources.py --sources /path/to/sources` 做一次性检查。它只读目录和文件名，不下载或修改资料。
