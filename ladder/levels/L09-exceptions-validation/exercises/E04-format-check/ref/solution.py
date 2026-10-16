def ValidCode(Code: str) -> bool:
    if len(Code) != 5:
        return False
    for Ch in Code[:2]:
        if not "A" <= Ch <= "Z":
            return False
    for Ch in Code[2:5]:
        if not "0" <= Ch <= "9":
            return False
    return True
