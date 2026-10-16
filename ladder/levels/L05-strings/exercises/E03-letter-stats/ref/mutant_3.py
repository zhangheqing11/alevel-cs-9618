# M3: intentional fault from spec.md.
def letter_stats(text: str) -> tuple[int, int, int]:
    vowels = 0
    consonants = 0
    others = 0
    for index in range(1, len(text)):
        ch = text[index - 1]
        upper = ch.upper()
        if upper in "AEIOU":
            vowels = vowels + 1
        elif "A" <= upper <= "Z":
            consonants = consonants + 1
        else:
            others = others + 1
    return vowels, consonants, others
