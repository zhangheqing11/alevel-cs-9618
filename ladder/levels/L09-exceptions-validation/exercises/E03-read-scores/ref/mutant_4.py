# M4: intentional fault from spec.md.
ScoreArray = [-1] * 20   # INTEGER, 20 elements, each initialised to -1
NumberScores = 0         # INTEGER


def ReadScores(FileName: str) -> int:
    global NumberScores
    NumberScores = 0
    try:
        with open(FileName, encoding="utf-8") as Source:
            for RawLine in Source:
                Line = RawLine.strip()
                try:
                    Score = int(Line)
                except ValueError:
                    print(f"Skipped: {Line}")
                    continue
                ScoreArray[NumberScores] = Score
                NumberScores = NumberScores + 1
    except FileNotFoundError:
        print("File not found")
    return NumberScores
