from pathlib import Path
import pytest
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('data,lines',[('',[]),('Hello Kevin',['Hello Kevin']),('first\nlast line  \n',['first','last line  '])])
def test_message_fields_and_final_terminator(candidate_path,exercise_dir,tmp_path,monkeypatch,data,lines):
    """9618_w23_21:8(a) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('message.txt').write_text(data)
    module.MyID='101'
    sent=[]
    monkeypatch.setattr(module,'Transmit',lambda message,port:sent.append((message,port)))
    handles=watch_open(monkeypatch)
    module.SendFile('message.txt','232',2)
    assert sent==[(chr(2)+'232101'+s+chr(3),2) for s in lines+['****']]
    assert Path('message.txt').read_text()==data
    assert handles and all(h.closed for h in handles)
