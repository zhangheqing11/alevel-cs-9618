# M1: intentional fault from spec.md.
def winner(board: list[list[str]]) -> str:
    lines = []
    for index in range(3):
        lines.append([board[index][column] for column in range(3)])
    for line in lines:
        if line[0] != " " and line[0] == line[1] == line[2]:
            return line[0]
    return ""
