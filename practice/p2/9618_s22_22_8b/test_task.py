from testkit import output_lines
from practice.p2._test_support import no_shortcuts

def test_first_group_all_matches_including_last(sol,candidate_path,monkeypatch,capsys):
    """9618_s22_22:8(b) MP1,2,3,4,5,6,7,8,9; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    entries=[(0,'ThisWebsite.com','A1'),(100,'other.net','B1'),(200,'other2.net','B2'),(300,'website27.net','A2'),(499,'websiteZ99.org','A3')]
    for i,name,cipher in entries:
        sol.Secret[i]=[name,cipher]
    def decrypt(cipher):
        assert cipher!=''
        return cipher[0]
    monkeypatch.setattr(sol,'Decrypt',decrypt)
    sol.SearchDuplicates()
    assert output_lines(capsys.readouterr().out)==['Password for ThisWebsite.com also used for website27.net','Password for ThisWebsite.com also used for websiteZ99.org']

def test_no_duplicates(sol,monkeypatch,capsys):
    """9618_s22_22:8(b) MP1,2,3,4,5,6,7,8,9; behaviour (syntax and declarations checked manually)."""
    sol.Secret[499]=['last','unique']
    monkeypatch.setattr(sol,'Decrypt',lambda value:value)
    sol.SearchDuplicates()
    assert output_lines(capsys.readouterr().out)==['No duplicate passwords found']
