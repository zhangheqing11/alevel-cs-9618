# T01 · 资料导入、清单与配对（总控）✅

- 老师提供的 Teach Cambridge 官方导出（`references_temp/` 中的 zip）原样解压到 `sources/teach_cambridge_raw/`，P4 源文件 zip 解到 `sources/teach_cambridge_sf/`。
- `pipeline/download/import_teacher.py`：复制并规范命名到 `sources/pastpapers/`、`sources/official/support/`、`sources/official/specimen/`（只复制，不改原件）。
- `pipeline/download/make_inventory.py` → `corpus/inventory.csv`：130 份卷（核验 108：s22–s25、w22–w25、s26；扩展 22：2021），全部 QP/MS 配对、总分 75、无重复。
- `pipeline/download/fetch.py`（PapaCambridge）保留，仅用于补 3 月卷（m22–m26，每季 variant 2）——需学生同意。
- 官网下载：2027–29 考纲、更新说明、伪代码指南 → `sources/official/`。
- 教材 → `sources/textbooks/`。
