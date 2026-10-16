# M3: intentional fault described in spec.md.
def char_type(ch: str) -> str:
    if ch >= "A" and ch <= "Z":
        return "upper"
    if ch >= "a" and ch <= "z":
        return "lower"
    if ch >= "1" and ch <= "9":
        return "digit"
    if ch == " ":
        return "space"
    return "other"
