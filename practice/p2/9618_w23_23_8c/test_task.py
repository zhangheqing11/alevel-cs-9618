from testkit import feed_input,output_lines

def test_received_bye_needs_no_reply(sol,monkeypatch,capsys):
    """9618_w23_23:8(c) MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    monkeypatch.setattr(sol,'GetData',lambda:'Bye')
    sent=[]
    monkeypatch.setattr(sol,'Transmit',lambda *args:sent.append(args))
    feed_input(monkeypatch)
    sol.Chat('454',2)
    assert output_lines(capsys.readouterr().out)==['Bye']
    assert sent==[]

def test_multiple_exchanges_and_sent_bye(sol,monkeypatch,capsys):
    """9618_w23_23:8(c) MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    received=iter(['Hello Jack','Again'])
    monkeypatch.setattr(sol,'GetData',lambda:next(received))
    sol.MyID='202'
    sent=[]
    monkeypatch.setattr(sol,'Transmit',lambda message,port:sent.append((message,port)))
    feed_input(monkeypatch,'Hello back','Bye')
    sol.Chat('454',3)
    assert output_lines(capsys.readouterr().out)==['Hello Jack','Again']
    assert sent==[(chr(2)+'454202Hello back'+chr(3),3),(chr(2)+'454202Bye'+chr(3),3)]
