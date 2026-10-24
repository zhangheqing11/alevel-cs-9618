from testkit import run_script

def base(name,sound,size,intelligence):
    return f"The animal's name is {name}, it makes a {sound}, its size is {size} and its intelligence level is {intelligence}"

def test_3a_animal_constructor_description(sol):
    """9618_s25_42:3(a)(i) MP4; 3(a)(ii) MP2-MP3: all fields concatenated and returned."""
    assert sol.Animal("Teddy","Bark",4,6).Description() == base("Teddy","Bark",4,6)
    assert sol.Animal("Pip","Squeak",1,3).Description() == base("Pip","Squeak",1,3)

def test_3b_parrot_inherits_updates_and_overrides(sol):
    """9618_s25_42:3(b)(i) MP1-MP4; 3(b)(ii) MP1-MP2: parent values, additive words, child string."""
    assert issubclass(sol.Parrot,sol.Animal)
    p=sol.Parrot("Chewie","Squawk",1,10,30,29)
    assert p.Description()==base("Chewie","Squawk",1,10)+". It has a wingspan of 30cm and can say 29 words."
    p.ChangeNumberWords(2);p.ChangeNumberWords(-1)
    assert p.Description()==base("Chewie","Squawk",1,10)+". It has a wingspan of 30cm and can say 30 words."

def test_3c_wolf_inherits_adds_signed_territory(sol):
    """9618_s25_42:3(c)(i) MP1-MP4; 3(c)(ii) MP1-MP2: additive change and QP's returned format."""
    assert issubclass(sol.Wolf,sol.Animal)
    w=sol.Wolf("Nighteyes","Howl",8,7,100)
    assert w.Description()==base("Nighteyes","Howl",8,7)+". Its territory is 100 square miles."
    w.SetTerritorySize(-20);w.SetTerritorySize(5)
    assert w.Description()==base("Nighteyes","Howl",8,7)+". Its territory is 85 square miles."

def test_3d_iii_screenshot_all_updated_descriptions(candidate_path):
    """9618_s25_42:3(d)(i) MP1-MP2; 3(d)(ii) MP1-MP3; 3(d)(iii) MP1-MP2."""
    result=run_script(candidate_path)
    assert result.returncode==0,result.stderr
    expected=[base("Chewie","Squawk",1,10)+". It has a wingspan of 30cm and can say 31 words.",base("Nighteyes","Howl",8,7)+". Its territory is 80 square miles.",base("Copper","Neigh",10,6)]
    assert all(message in result.stdout for message in expected)
