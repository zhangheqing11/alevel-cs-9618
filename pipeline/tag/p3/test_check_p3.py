"""Exercise annotation guardrails before any corpus mutation."""
from copy import deepcopy
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_p3 import validate

ROW = {'id': 'x', 'component': 3, 'marks': 4, 'ms_text': 'TYPE A ENDTYPE', 'equivalent_of': None}
TAG = {'id': 'x', 'primary': 'P3-DR-03', 'cross': [], 'confidence': 'high', 'note': ''}
POINT = {'id': 'x', 'ms_max': None, 'markpoints': [{'n': 1, 'text': 'TYPE A ENDTYPE', 'marks': 4, 'skills': ['record-type']}]}

def check(tags=None, points=None, exemptions=None):
    validate({'x': ROW}, {'x': TAG} if tags is None else tags,
             {'x': POINT} if points is None else points, {},
             {'P3-DR-03'}, {'record-type'}, {} if exemptions is None else exemptions)

def test_require_every_row_and_every_required_split():
    with pytest.raises(ValueError, match='coverage'):
        check(tags={})
    with pytest.raises(ValueError, match='split'):
        check(points={})

def test_reject_nonverbatim_points_and_invalid_skills():
    points = {'x': deepcopy(POINT)}
    points['x']['markpoints'][0]['text'] = 'invented'
    with pytest.raises(ValueError, match='verbatim'):
        check(points=points)
    points['x']['markpoints'][0]['text'] = 'TYPE A ENDTYPE'
    points['x']['markpoints'][0]['skills'] = ['invented']
    with pytest.raises(ValueError, match='skills'):
        check(points=points)

def test_require_cap_when_points_exceed_marks():
    points = {'x': deepcopy(POINT)}
    points['x']['markpoints'][0]['marks'] = 5
    with pytest.raises(ValueError, match='total'):
        check(points=points)
    points['x']['ms_max'] = 4
    check(points=points)

def test_prohibit_exempting_always_split_type():
    with pytest.raises(ValueError, match='exemption'):
        check(points={}, exemptions={'x': {'id': 'x', 'reason': 'not code'}})
