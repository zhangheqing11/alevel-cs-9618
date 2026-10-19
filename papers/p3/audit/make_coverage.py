#!/usr/bin/env python3
"""Write papers/p3/audit/T36-coverage.json: per card, the representative / variation rows, the QP / MS pages read
(text of every page named by the row, from the PDF), the pages also looked at as renders, the finding ids, plus the
SHA-256 of every audited input so that `check_handbook.py --validate` refuses a stale audit.

  ~/.venvs/alevel-cs/bin/python papers/p3/audit/make_coverage.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_handbook as h  # noqa: E402

# Pages looked at as rendered images during the manual review (paper, kind, page), by card.
RENDERED = {
    'P3-DR-09': [('9618_w24_31', 'ms', 4)],
    'P3-DR-10': [('9618_w24_31', 'ms', 4)],
    'P3-DR-11': [('9618_s25_33', 'ms', 7)],
    'P3-HV-01': [('9618_w22_31', 'ms', 11)],
    'P3-HV-02': [('9618_s23_32', 'ms', 9)],
    'P3-BL-01': [('9618_s24_31', 'qp', 6), ('9618_s24_31', 'ms', 9), ('9618_w25_31', 'qp', 6), ('9618_w23_32', 'qp', 6)],
    'P3-BL-02': [('9618_s22_32', 'qp', 9), ('9618_s22_32', 'ms', 7), ('9618_s21_31', 'qp', 9), ('9618_s21_31', 'ms', 8)],
    'P3-BL-03': [('9618_w22_32', 'qp', 7), ('9618_w22_32', 'ms', 10), ('9618_w22_32', 'ms', 11)],
    'P3-BL-04': [('9618_w24_31', 'qp', 6), ('9618_w24_31', 'ms', 8), ('9618_s23_32', 'qp', 10), ('9618_s23_32', 'ms', 9)],
    'P3-BL-05': [('9618_s23_31', 'qp', 8), ('9618_s23_31', 'ms', 6), ('9618_w24_32', 'qp', 6), ('9618_w24_32', 'qp', 7)],
    'P3-BL-06': [('9618_w24_31', 'qp', 7), ('9618_w24_31', 'ms', 9), ('9618_w24_31', 'ms', 10), ('9618_w25_31', 'qp', 7), ('9618_w25_31', 'ms', 11)],
    'P3-BL-07': [('9618_w22_32', 'qp', 7), ('9618_w22_32', 'ms', 12), ('9618_w23_31', 'qp', 7), ('9618_w23_31', 'ms', 5),
                 ('9618_s23_31', 'ms', 7), ('9618_w24_31', 'ms', 10)],
    'P3-SY-06': [('9618_w22_31', 'ms', 7)],
    'P3-SY-07': [('9618_s23_31', 'qp', 6), ('9618_s23_31', 'qp', 7), ('9618_s23_31', 'ms', 5)],
    'P3-SY-08': [('9618_s25_31', 'qp', 8), ('9618_s25_31', 'qp', 9), ('9618_s25_31', 'ms', 12)],
    'P3-SY-09': [('9618_s23_31', 'qp', 6), ('9618_s23_31', 'qp', 7), ('9618_s23_31', 'ms', 6)],
    'P3-SY-11': [('9618_s24_31', 'qp', 5), ('9618_s24_31', 'ms', 7)],
    'P3-SY-12': [('9618_w25_32', 'qp', 8), ('9618_w25_32', 'ms', 14), ('9618_s24_31', 'ms', 8)],
    'P3-AI-03': [('9618_w23_32', 'qp', 7), ('9618_w23_32', 'ms', 6), ('9618_w25_33', 'qp', 7)],
    'P3-AI-04': [('9618_s23_32', 'qp', 12), ('9618_s23_32', 'ms', 11), ('9618_w21_31', 'qp', 12), ('9618_w21_31', 'ms', 9)],
    'P3-AI-05': [('9618_s23_31', 'ms', 3)],
    'P3-CT-02': [('9618_s24_31', 'qp', 10), ('9618_s24_31', 'ms', 12)],
    'P3-CT-09': [('9618_w24_31', 'qp', 12), ('9618_w24_31', 'qp', 13), ('9618_w24_31', 'ms', 15),
                 ('9618_w24_31', 'ms', 16), ('9618_w24_31', 'ms', 17)],
    'P3-CT-12': [('9618_s23_31', 'qp', 12), ('9618_s23_31', 'ms', 10)],
    'P3-FP-05': [('9618_s25_31', 'qp', 12)],
}
# Extra page text read beyond the row's own pages (context, continuation pages).
EXTRA_TEXT = {
    'P3-SC-01': [('9618_w22_31', 'qp', 6)],
    'P3-FP-03': [('9618_w25_32', 'qp', 11)],
    'P3-CT-02': [('9618_s24_31', 'ms', 13)],
    'P3-FP-06': [('9618_w22_31', 'qp', 10)],
}


def main():
    findings = [json.loads(l) for l in (h.AUDIT / 'T36-findings.jsonl').read_text().splitlines() if l.strip()]
    out = []
    for c in h.cards():
        rep = h.ROWS[c['representative']]
        var = h.ROWS.get(c['variation'])
        fids = [f'F{i + 1:02d}' for i, f in enumerate(findings) if f['card'] == c['card']]
        rendered = RENDERED.get(c['card'], [])
        out.append({
            'card': c['card'], 'representative': c['representative'], 'variation': c['variation'],
            'qp_pages': h.pages_of(rep, 'qp'), 'ms_pages': h.pages_of(rep, 'ms'),
            'variation_pages': {'qp': h.pages_of(var, 'qp'), 'ms': h.pages_of(var, 'ms')} if var else None,
            'rendered': [f'{p} {k.upper()} p.{n}' for p, k, n in rendered],
            'extra_text': [f'{p} {k.upper()} p.{n}' for p, k, n in EXTRA_TEXT.get(c['card'], [])],
            'method': 'text+render' if rendered else 'text',
            'findings': fids,
        })
    data = {'audit': 'T36', 'base': 'a9bb0d8', 'cards': out, 'source_sha256': h.input_hashes()}
    (h.AUDIT / 'T36-coverage.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(len(out), 'cards;', sum(1 for c in out if c['rendered']), 'with renders;', len(findings), 'findings')


if __name__ == '__main__':
    main()
