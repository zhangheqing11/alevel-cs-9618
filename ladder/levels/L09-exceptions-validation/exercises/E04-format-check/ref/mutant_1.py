# M1: intentional fault from spec.md.
def ValidCode(Code: str) -> bool:
    if len(Code) != 5:
        return False
    for Ch in Code[:2]:
        if not "A" <= Ch <= "Z":
            return False
    try:
        float(Code[2:])
    except ValueError:
        return False
    return True
