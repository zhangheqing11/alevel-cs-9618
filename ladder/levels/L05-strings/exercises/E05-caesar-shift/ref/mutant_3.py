# M3: intentional fault from spec.md.
def caesar_shift(text: str, shift: int) -> str:
    result = ""
    for ch in text:
        if "A" <= ch <= "Z":
            result = result + chr(ord(ch) + shift)r((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            result = result + chr(ord(ch) + shift)r((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        else:
            result = result + chr(ord(ch) + shift)
    return result
