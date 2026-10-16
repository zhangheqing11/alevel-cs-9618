# M3: intentional fault from spec.md.
def balanced(text: str) -> bool:
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}
    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            opening = stack.pop()
            if opening != matching[ch]:
                return False
    return len(stack) == 0
