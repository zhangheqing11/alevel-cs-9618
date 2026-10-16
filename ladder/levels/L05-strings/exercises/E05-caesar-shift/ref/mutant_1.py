# M1: intentional fault from spec.md.
def caesar_shift(text: str, shift: int) -> str:
    result = ""
    for ch in text:
        if "A" <= ch <= "Z":
            result = result + chr(ord(ch) + shift)
        elif "a" <= ch <= "z":
            result = result + chr(ord(ch) + shift)
        else:
            result = result + ch
    return result
