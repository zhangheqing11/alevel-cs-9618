# M4: intentional fault from spec.md.
def InputName() -> str:
    while True:
        Name = input("Name: ")
        if len(Name) == 3 and all("A" <= Ch <= "Z" for Ch in Name):
            return Name
        print("Invalid name")


def InputScore() -> int:
    while True:
        Text = input("Score: ")
        try:
            Score = int(Text)
        except ValueError:
            print("Invalid score")
            continue
        if 0 <= Score < 1000:
            return Score
        print("Invalid score")
