"""Guard D33 byte preservation and safe annotation replacement."""
import importlib.util,json
from pathlib import Path
import pytest

SPEC=importlib.util.spec_from_file_location('apply_p3',Path(__file__).with_name('apply_p3.py'))
apply=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(apply)
TAG={'id':'x','primary':'P3-CT-02','cross':[],'confidence':'high','note':'指南 §3'}

def test_preserve_unowned_json_bytes_and_escaped_er():
 line=r'{"id": "x", "stem": "a, } \" b", "er": "\u4e2d\nline", "flags": [ "figure" ], "types": {"primary":"old","cross":[]}, "ms_max": 8, "markpoints": []}'
 result=apply.annotated_line(line,{'x':TAG},{})
 assert r'"er": "\u4e2d\nline"' in result
 assert '"flags": [ "figure" ]' in result
 assert r'"stem": "a, } \" b"' in result
 assert set(json.loads(result))=={'id','stem','er','flags','types','tag_confidence','tag_note'}
 assert apply.annotated_line(result,{'x':TAG},{})==result

def test_replace_stale_points_and_add_cap():
 line=json.dumps({'id':'x','er':'original','markpoints':[{'old':True}],'ms_max':99})
 points={'x':{'id':'x','ms_max':4,'markpoints':[{'n':1,'text':'source','marks':5,'skills':['binary-search']}]}}
 result=json.loads(apply.annotated_line(line,{'x':TAG},points))
 assert result['markpoints']==points['x']['markpoints'] and result['ms_max']==4 and result['er']=='original'

def test_duplicate_annotation_ids_fail():
 with pytest.raises(ValueError,match='duplicate'):apply.index_records([TAG,TAG])
