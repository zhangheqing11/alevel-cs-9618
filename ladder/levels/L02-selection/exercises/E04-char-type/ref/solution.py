def char_type(ch:str)->str:
    if ch>="A" and ch<="Z": return "upper"
    if ch>="a" and ch<="z": return "lower"
    if ch>="0" and ch<="9": return "digit"
    if ch==" ": return "space"
    return "other"
