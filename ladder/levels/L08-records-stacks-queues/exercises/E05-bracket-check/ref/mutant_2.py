# M2: intentional fault from spec.md.
def balanced(text: str) -> bool:
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}
    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack:
                return False
            opening = stack.pop()
            if opening != matching[ch]:
                return False
    return True
