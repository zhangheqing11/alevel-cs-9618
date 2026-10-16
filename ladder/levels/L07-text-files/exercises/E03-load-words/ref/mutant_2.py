# M2: intentional fault from spec.md.
def load_words(file_name: str) -> list[str]:
    words = []
    with open(file_name, encoding="utf-8") as source:
        for line in source:
            word = line.rstrip("\n")
            words.append(word)
    return words


def longest_word(file_name: str) -> str:
    longest = ""
    for word in load_words(file_name):
        if len(word) > len(longest):
            longest = word
    return longest
