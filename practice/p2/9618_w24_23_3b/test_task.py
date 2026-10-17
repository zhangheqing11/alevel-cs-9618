def test_all_pointers_and_unchanged_data(sol):
    """9618_w24_23:3(b) MP1,2,3,4; behaviour (syntax and declarations checked manually)."""
    for i in range(1,201):
        sol.List[i].Data='node'+str(i)
        sol.List[i].Pointer=88
    sol.HeadPointer=17
    sol.main()
    assert [sol.List[i].Pointer for i in range(1,201)]==list(range(2,201))+[0]
    assert [sol.List[i].Data for i in range(1,201)]==['node'+str(i) for i in range(1,201)]
    assert sol.HeadPointer==17
