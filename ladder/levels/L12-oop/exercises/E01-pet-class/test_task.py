def test_constructor_and_getters(sol):
    """B1, B8: constructor stores supplied name/age; getters return str/int."""
    pet = sol.Pet("Kitty", 3)
    assert pet.GetName() == "Kitty"
    assert type(pet.GetName()) is str
    assert pet.GetAge() == 3
    assert type(pet.GetAge()) is int


def test_set_age(sol):
    """B2-B4, B8: accept inclusive age range, reject out-of-range without changing state; bool return."""
    pet = sol.Pet("Kitty", 3)
    assert pet.SetAge(10) is True
    assert pet.GetAge() == 10
    for age in [51, -1]:
        assert pet.SetAge(age) is False
        assert pet.GetAge() == 10
    for age in [0, 50]:
        assert pet.SetAge(age) is True
        assert pet.GetAge() == age


def test_birthday(sol):
    """B5: Birthday changes the object's own age on each call."""
    pet = sol.Pet("Rex", 4)
    pet.Birthday()
    pet.Birthday()
    assert pet.GetAge() == 6


def test_independent_objects(sol):
    """B6: updating the first object's age leaves the second object's age unchanged."""
    first, second = sol.Pet("A", 1), sol.Pet("B", 2)
    assert first.SetAge(9) is True
    assert second.GetAge() == 2


def test_private_attributes(sol):
    """B7: exactly the specified name-mangled private attributes; no public Name/Age."""
    pet = sol.Pet("Kitty", 3)
    assert set(vars(pet)) == {"_Pet__Name", "_Pet__Age"}
    assert not hasattr(pet, "Name")
    assert not hasattr(pet, "Age")
