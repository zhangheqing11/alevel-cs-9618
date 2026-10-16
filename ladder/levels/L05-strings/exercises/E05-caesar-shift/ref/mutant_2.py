# M2: intentional fault from spec.md.
def caesar_shift(text: str, shift: int) -> str:
    result = ""
    for ch in text:
        if "A" <= ch <= "Z":
            result = result + chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            result = result + chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        else:
            result = result + ch
    return result
