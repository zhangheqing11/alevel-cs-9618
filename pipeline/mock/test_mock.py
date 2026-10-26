"""Regression tests for marking kits and student score validation."""
import csv
import html
from pathlib import Path

import pytest

from pipeline.mock.make_mock import ROOT, generate, load_paper
from pipeline.mock.score_mock import estimate_component, estimate_option, score_sheet, summarize


def fill_score(path, awarded=None, skills=None):
    with path.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row['marks_awarded'] = str(row['marks_available'] if awarded is None else awarded)
        if skills:
            row['lost_skills'] = skills
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return rows


@pytest.mark.parametrize('paper', ['9618_s26_22', '9618_s25_22'])
def test_complete_marking_kit(paper, tmp_path):
    info, rows = load_paper(paper)
    folder = generate(paper, tmp_path)
    md = (folder / 'marking.md').read_text()
    page = (folder / 'marking.html').read_text()
    with (folder / 'score.csv').open(encoding='utf-8-sig', newline='') as f:
        scores = list(csv.DictReader(f))
    assert len(scores) == len(rows)
    assert sum(int(x['marks_available']) for x in scores) == int(info['total_marks']) == 75
    assert all(x['marks_awarded'] == '' for x in scores)
    assert (folder / 'score.csv').read_bytes().startswith(b'\xef\xbb\xbf')
    for row in rows:
        assert row['ms_text'] in md
        assert html.escape(row['ms_text']) in page
        assert f"## {row['q']} · {row['marks']} 分" in md
        assert row['stem'] not in md
        for mp in row.get('markpoints', []):
            assert f"| MP{mp['n']} |" in md
            assert html.escape(mp['text']) in page
            assert '; '.join(mp['skills']) in page
        if row.get('ms_max'):
            assert f"MS 上限：{row['ms_max']}" in md
        if row.get('er'):
            assert row['er'] in md
            assert '仅供易错参考，不是给分依据' in md
        if row['has_figure']:
            assert f"对照 QP p.{row['qp_page']}" in md
    assert f"#P2-" in md
    assert '120 分钟' in md
    assert '9618_s26_in_22.pdf' in md if 's26' in paper else '9618_s25_in_22.pdf' in md


def test_all_s26_papers_and_materials(tmp_path):
    papers = sorted((ROOT / 'corpus/rows').glob('p*/9618_s26_*.jsonl'))
    assert len(papers) == 12
    for path in papers:
        info, rows = load_paper(path.stem)
        folder = generate(path.stem, tmp_path)
        md = (folder / 'marking.md').read_text()
        if path.stem.endswith(('41', '42', '43')):
            assert info['sf']
            assert info['qp'] in md
            assert info['ms'] in md
            assert info['sf'] in md
            assert '考试时长：150 分钟' in md
            for row in rows:
                primary = row.get('types', {}).get('primary')
                assert primary, f"{row['id']} has no primary type"
                assert f'主题型：[{primary}](' in md
        assert len(list(folder.iterdir())) == 3


def test_regeneration_cannot_erase_marks(tmp_path):
    folder = generate('9618_s26_22', tmp_path)
    fill_score(folder / 'score.csv')
    before = (folder / 'score.csv').read_bytes()
    with pytest.raises(FileExistsError):
        generate('9618_s26_22', tmp_path)
    assert (folder / 'score.csv').read_bytes() == before


def test_complete_score_and_missing_threshold_placeholder(tmp_path):
    folder = generate('9618_s26_22', tmp_path)
    fill_score(folder / 'score.csv')
    result = score_sheet(folder / 'score.csv')
    assert result['awarded'] == result['available'] == 75
    assert sum(result['types'].values()) == 0
    assert '75/75' in summarize([result], tmp_path / 'absent')
    assert 'T40' in summarize([result], tmp_path / 'absent')


@pytest.mark.parametrize('failure', ['blank', 'negative', 'fraction', 'too-high', 'nan', 'missing', 'duplicate', 'tamper', 'unknown-skill', 'over-attribute'])
def test_invalid_score_is_rejected(failure, tmp_path):
    folder = generate('9618_s26_22', tmp_path)
    path = folder / 'score.csv'
    rows = fill_score(path)
    if failure in ('blank', 'negative', 'fraction', 'too-high', 'nan'):
        rows[0]['marks_awarded'] = {'blank': '', 'negative': '-1', 'fraction': '0.5', 'too-high': '99', 'nan': 'NaN'}[failure]
    elif failure == 'missing':
        rows.pop()
    elif failure == 'duplicate':
        rows.append(rows[0])
    elif failure == 'tamper':
        rows[0]['marks_available'] = '99'
    elif failure == 'unknown-skill':
        rows[0]['lost_skills'] = 'invented-skill=1'
    else:
        rows[0]['lost_skills'] = 'trace-dry-run=1'
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(ValueError):
        score_sheet(path)


def test_loss_stats_are_explicit_and_conserve_marks(tmp_path):
    folder = generate('9618_s26_22', tmp_path)
    path = folder / 'score.csv'
    fill_score(path, awarded=0)
    with path.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    rows[0]['lost_skills'] = 'declare-variables=1'
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    result = score_sheet(path)
    assert sum(result['types'].values()) == 75
    assert sum(result['skills'].values()) == 75
    assert result['skills']['declare-variables'] == 1
    assert result['skills']['未归因'] == 74


def threshold_tables(folder):
    folder.mkdir()
    for filename, fields, rows in [
        ('components.csv', ['session', 'year', 'component', 'max_raw', 'A', 'B', 'C', 'D', 'E'], [
            ['s', 2025, 22, 75, 50, 40, 30, 20, 10],
            ['w', 2025, 22, 75, 55, 45, 35, 25, 15],
        ]),
        ('options.csv', ['session', 'year', 'option', 'components', 'max_weighted', 'A*', 'A', 'B', 'C', 'D', 'E'], [
            ['w', 2025, 'AY', '12;22;32;42', 300, 250, 220, 190, 160, 130, 100],
        ]),
    ]:
        with (folder / filename).open('w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            writer.writerows(rows)
    return folder


def test_grade_boundaries_use_latest_season_and_exact_component(tmp_path):
    tables = threshold_tables(tmp_path / 'thresholds')
    for score, expected in [(55, 'A'), (54, 'B'), (45, 'B'), (15, 'E'), (14, 'U')]:
        result = estimate_component('22', score, 75, tables)
        assert result['grade'] == expected
        assert result['season'] == 'w2025'
    assert estimate_component('21', 75, 75, tables)['grade'] is None


def test_option_requires_exact_four_components_and_supports_astar(tmp_path):
    tables = threshold_tables(tmp_path / 'thresholds')
    results = [{'paper': f'9618_s26_{c}', 'available': 75, 'awarded': score}
               for c, score in [('12', 75), ('22', 75), ('32', 75), ('42', 25)]]
    assert estimate_option(results, tables)['grade'] == 'A*'
    results[-1]['awarded'] = 24
    assert estimate_option(results, tables)['grade'] == 'A'
    assert estimate_option(results[:3], tables)['grade'] is None
    results[-1]['paper'] = '9618_s26_41'
    assert estimate_option(results, tables)['grade'] is None


def test_option_does_not_guess_weighting(tmp_path):
    tables = threshold_tables(tmp_path / 'thresholds')
    p = tables / 'options.csv'
    p.write_text(p.read_text(encoding='utf-8-sig').replace(',300,', ',400,'), encoding='utf-8-sig')
    results = [{'paper': f'9618_s26_{c}', 'available': 75, 'awarded': 75}
               for c in ['12', '22', '32', '42']]
    assert estimate_option(results, tables)['grade'] is None


def test_unsafe_paper_id_rejected():
    with pytest.raises(ValueError):
        load_paper('../not-a-paper')


def test_sources_are_read_only_even_with_custom_out(tmp_path):
    sources = tmp_path / 'sources'
    with pytest.raises(ValueError, match='sources'):
        generate('9618_s26_22', sources / 'generated', sources=sources)
    assert not sources.exists()


def test_mismatched_ms_pair_and_marks_total_rejected(tmp_path):
    import json
    import shutil
    (tmp_path / 'corpus/rows/p2').mkdir(parents=True)
    inventory = tmp_path / 'corpus/inventory.csv'
    shutil.copy(ROOT / 'corpus/inventory.csv', inventory)
    path = tmp_path / 'corpus/rows/p2/9618_s26_22.jsonl'
    _, rows = load_paper('9618_s26_22')
    path.write_text('\n'.join(json.dumps(r) for r in rows))
    text = inventory.read_text(encoding='utf-8-sig')
    inventory.write_text(text.replace('9618_s26_ms_22.pdf', '9618_s26_ms_21.pdf'), encoding='utf-8-sig')
    with pytest.raises(ValueError, match='配对'):
        load_paper('9618_s26_22', tmp_path)
    inventory.write_text(text, encoding='utf-8-sig')
    rows[0]['marks'] += 1
    path.write_text('\n'.join(json.dumps(r) for r in rows))
    with pytest.raises(ValueError, match='分值合计'):
        load_paper('9618_s26_22', tmp_path)


def test_html_and_markdown_quote_ms_as_data(tmp_path):
    import json
    import shutil
    (tmp_path / 'corpus/rows/p2').mkdir(parents=True)
    shutil.copy(ROOT / 'corpus/inventory.csv', tmp_path / 'corpus/inventory.csv')
    _, rows = load_paper('9618_s26_22')
    payload = '<script>alert(1)</script>\n```\n# plain MS text'
    rows[0]['ms_text'] = payload
    path = tmp_path / 'corpus/rows/p2/9618_s26_22.jsonl'
    path.write_text('\n'.join(json.dumps(r) for r in rows))
    folder = generate('9618_s26_22', tmp_path / 'output/mock', root=tmp_path)
    page = (folder / 'marking.html').read_text()
    assert '<script>' not in page
    assert html.escape(payload) in page
    assert '````text\n' + payload + '\n````' in (folder / 'marking.md').read_text()


def test_cli_rejects_incomplete_sheet_and_reports_filled_sheet(tmp_path):
    import subprocess
    import sys
    folder = generate('9618_s26_22', tmp_path)
    command = [sys.executable, str(ROOT / 'pipeline/mock/score_mock.py'), str(folder / 'score.csv'), '--thresholds', str(tmp_path / 'absent')]
    bad = subprocess.run(command, capture_output=True, text=True)
    assert bad.returncode == 2
    assert '空白不能视为 0' in bad.stderr
    fill_score(folder / 'score.csv')
    good = subprocess.run(command, capture_output=True, text=True)
    assert good.returncode == 0
    assert '75/75' in good.stdout and 'T40' in good.stdout


def test_card_link_encodes_spaces_for_custom_output(tmp_path):
    from pipeline.mock.make_mock import card_link
    row = {'component': 2, 'types': {'primary': 'P2-DT-01'}}
    md, page = card_link(row, tmp_path / 'kits/9618_s26_22', tmp_path / 'repo with spaces')
    assert 'repo%20with%20spaces' in md
    assert 'repo%20with%20spaces' in page
