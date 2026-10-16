PREDICTED = ["8", "Comter", "pu", "COMPUTER", "rtpo", "2", "p", "16!"]


def run_trace() -> None:
    word = "Computer"
    print(len(word))
    print(word[:3] + word[-3:])
    print(word[3:5])
    print(word.upper())
    result = ""
    for index in range(len(word), 0, -2):
        result = result + word[index - 1]
    print(result)
    print(ord("C") - ord("A"))
    print(chr(ord(word[1:2]) + 1))
    print(str(len(word) * 2) + "!")


if __name__ == "__main__":
    run_trace()
