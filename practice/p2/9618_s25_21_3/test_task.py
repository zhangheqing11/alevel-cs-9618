import random,pytest
from testkit import output_lines

@pytest.mark.parametrize('seed',[1,5,23])
def test_guess_feedback_and_termination(sol,monkeypatch,capsys,seed):
    """9618_s25_21:3 MP1,2,3,4,5,6,7,8,9 (behaviour; syntax/declarations checked manually)."""
    random.seed(seed)
    order=[]
    for n in range(1,51):
        order.extend([101-n,n])
    used=[]
    answers=iter(order)
    def get_guess(prompt=''):
        n=next(answers)
        used.append(n)
        return str(n)
    monkeypatch.setattr('builtins.input',get_guess)
    sol.main()
    lines=output_lines(capsys.readouterr().out)
    assert len(lines)==len(used)
    target=used[-1]
    assert any(w in lines[-1].lower() for w in ('correct','success','found','right'))
    for guess,line in zip(used[:-1],lines[:-1]):
        words=('high','large','big') if guess>target else ('low','small')
        assert any(w in line.lower() for w in words)


def test_same_seed_has_same_hidden_number_for_different_guess_orders(sol,monkeypatch,capsys):
    """9618_s25_21:3 MP5, MP7–MP9: the secret is independent of the guesses."""
    targets=[]
    for order in (range(1,101),range(100,0,-1)):
        random.seed(5)
        used=[]
        answers=iter(order)
        def get_guess(prompt=''):
            value=next(answers)
            used.append(value)
            return str(value)
        monkeypatch.setattr('builtins.input',get_guess)
        sol.main()
        capsys.readouterr()
        targets.append(used[-1])
    assert targets[0]==targets[1]
