from testkit import run_script

def base(name,sound,size,intelligence):
    return f"The animal's name is {name}, it makes a {sound}, its size is {size} and its intelligence level is {intelligence}"

def test_3a_animal_constructor_description(sol):
    """9618_s25_42:3(a)(i) MP4; 3(a)(ii) MP2-MP3: all fields concatenated and returned."""
    assert sol.Animal("Teddy","Bark",4,6).Description() == base("Teddy","Bark",4,6)
    assert sol.Animal("Pip","Squeak",1,3).Description() == base("Pip","Squeak",1,3)

def test_3b_parrot_inherits_updates_and_overrides(sol,monkeypatch):
    """9618_s25_42:3(b)(i) MP1-MP4; 3(b)(ii) MP1-MP2: parent values, additive words, child string."""
    assert issubclass(sol.Parrot,sol.Animal)
    constructor_calls = []
    original_constructor = sol.Animal.__init__
    def constructor_spy(self,*args,**kwargs):
        constructor_calls.append(args if args else tuple(kwargs.values()))
        original_constructor(self,*args,**kwargs)
    monkeypatch.setattr(sol.Animal,"__init__",constructor_spy)
    p=sol.Parrot("Chewie","Squawk",1,10,30,29)
    assert constructor_calls == [("Chewie","Squawk",1,10)]
    assert p.Description()==base("Chewie","Squawk",1,10)+". It has a wingspan of 30cm and can say 29 words."
    p.ChangeNumberWords(2);p.ChangeNumberWords(-1)
    assert p.Description()==base("Chewie","Squawk",1,10)+". It has a wingspan of 30cm and can say 30 words."

def test_3c_wolf_inherits_adds_signed_territory(sol,monkeypatch):
    """9618_s25_42:3(c)(i) MP1-MP4; 3(c)(ii) MP1-MP2: additive change and QP's returned format."""
    assert issubclass(sol.Wolf,sol.Animal)
    constructor_calls = []
    original_constructor = sol.Animal.__init__
    def constructor_spy(self,*args,**kwargs):
        constructor_calls.append(args if args else tuple(kwargs.values()))
        original_constructor(self,*args,**kwargs)
    monkeypatch.setattr(sol.Animal,"__init__",constructor_spy)
    w=sol.Wolf("Nighteyes","Howl",8,7,100)
    assert constructor_calls == [("Nighteyes","Howl",8,7)]
    assert w.Description()==base("Nighteyes","Howl",8,7)+". Its territory is 100 square miles."
    w.SetTerritorySize(-20);w.SetTerritorySize(5)
    assert w.Description()==base("Nighteyes","Howl",8,7)+". Its territory is 85 square miles."

def test_3d_iii_screenshot_all_updated_descriptions(candidate_path):
    """9618_s25_42:3(d)(i) MP1-MP2; 3(d)(ii) MP1-MP3; 3(d)(iii) MP1-MP2."""
    result=run_script(candidate_path)
    assert result.returncode==0,result.stderr
    expected=[base("Chewie","Squawk",1,10)+". It has a wingspan of 30cm and can say 31 words.",base("Nighteyes","Howl",8,7)+". Its territory is 80 square miles.",base("Copper","Neigh",10,6)]
    assert all(message in " ".join(result.stdout.split()) for message in expected)


def test_3di_3dii_main_call_chain(candidate_path, exercise_dir):
    """9618_s25_42:3(d)(i) MS p.43; 9618_s25_42:3(d)(ii) MS p.44; 9618_s25_42:3(b)(i) MS p.37; 9618_s25_42:3(c)(i) MS p.40: 3(b)(i) MP2; 3(c)(i) MP2; 3(d)(i) MP1–MP2; 3(d)(ii) MP1–MP3; observe required calls, parameters and returned output (D46)."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin='', files_dir=exercise_dir / "files")
    assert r.error is None, r.error

    assert [list(c.args.values()) for c in r.called("SetTerritorySize")] == [[-20]]
    assert [list(c.args.values()) for c in r.called("ChangeNumberWords")] == [[2]]
    descriptions = r.called("Description")
    assert {"Chewie","Nighteyes","Copper"} <= {n for n in ["Chewie","Nighteyes","Copper"] if any(n in str(c.result) and " ".join(c.result.split()) in " ".join(r.stdout.split()) for c in descriptions)}
    assert len(r.called("Animal.__init__")) == 3
    assert [list(c.args.values()) for c in r.called("Parrot.__init__")] == [["Chewie","Squawk",1,10,30,29]]
    assert [list(c.args.values()) for c in r.called("Wolf.__init__")] == [["Nighteyes","Howl",8,7,100]]
