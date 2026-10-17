from practice.p2._test_support import no_shortcuts

def test_first_free_and_encryption(sol,candidate_path,monkeypatch):
    """9618_s22_23:9(b) MP1,2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.Secret[0]=['old','encrypted:old']
    monkeypatch.setattr(sol,'Encrypt',lambda text:'new-cipher-'+text)
    assert sol.AddPassword('new','FxAf-3hzV-Aq49') is True
    assert sol.Secret[1]==['new','new-cipher-FxAf-3hzV-Aq49']
    assert sol.Secret[0]==['old','encrypted:old']

def test_existing_domain_is_unchanged(sol):
    """9618_s22_23:9(b) MP1,2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    sol.Secret[499]=['existing','encrypted:old']
    before=[row[:] for row in sol.Secret]
    assert sol.AddPassword('existing','new') is False
    assert sol.Secret==before

def test_only_last_free_and_full(sol):
    """9618_s22_23:9(b) MP1,2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    sol.Secret=[['site'+str(i),'encrypted:p'] for i in range(500)]
    sol.Secret[499]=['','']
    assert sol.AddPassword('new','FxAf-3hzV-Aq49') is True
    assert sol.Secret[499]==['new','encrypted:FxAf-3hzV-Aq49']
    before=[row[:] for row in sol.Secret]
    assert sol.AddPassword('more','FxAf-3hzV-Aq49') is False
    assert sol.Secret==before
