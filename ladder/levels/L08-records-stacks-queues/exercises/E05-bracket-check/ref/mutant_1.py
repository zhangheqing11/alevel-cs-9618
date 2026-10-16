# M1: intentional fault from spec.md.
def balanced(text: str) -> bool:
    opening_count = sum(text.count(ch) for ch in "([{")
    closing_count = sum(text.count(ch) for ch in ")]}")
    return opening_count == closing_count
