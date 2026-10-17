def test_declaration_size_zero_to_max_and_false(sol):
    """9618_w25_22:4(a) MP3,4; behaviour (syntax and declarations checked manually)."""
    sol.main()
    assert isinstance(sol.CheckTotal,list)
    assert len(sol.CheckTotal)==36
    assert all(value is False for value in sol.CheckTotal)
