import pytest

@pytest.mark.parametrize('message,success,expected_stack',[('123data',True,1),('999data',True,2),('123X',False,1),('999X',False,2),('123',True,None)])
def test_stack_routing_and_error(sol,monkeypatch,capsys,message,success,expected_stack):
    """9618_w23_22:8(b) MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    sol.MyID='123'
    calls=[]
    def stack(msg,num):
        calls.append((msg,num))
        return success
    monkeypatch.setattr(sol,'StackMsg',stack)
    sol.ProcessMsg(message)
    assert calls==([] if expected_stack is None else [(message,expected_stack)])
    output=capsys.readouterr().out
    assert bool(output.strip()) is (expected_stack is not None and not success)
