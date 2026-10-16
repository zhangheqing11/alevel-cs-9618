def winner(board: list[list[str]]) -> str:
    lines = []
    for index in range(3):
        lines.append([board[index][column] for column in range(3)])
        lines.append([board[row][index] for row in range(3)])
    lines.append([board[index][index] for index in range(3)])
    lines.append([board[index][2 - index] for index in range(3)])
    for line in lines:
        if line[0] != " " and line[0] == line[1] == line[2]:
            return line[0]
    return ""
