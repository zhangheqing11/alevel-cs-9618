# M2: intentional fault from spec.md.
def trim_spaces(text: str) -> str:
    leading = 0
    while leading < len(text) and text[leading] == " ":
        leading = leading + 1
    text = text[leading:]
    return text.replace(" ", "")
