PREDICTED: list[float] = [1.50, 3.00, 4.20, 5.40, 10.80, 13.20]


def postage(weight: int, express: bool) -> float:
    if weight <= 100:
        cost = 1.50
    elif weight <= 500:
        cost = 3.00
    else:
        cost = 3.00 + ((weight - 500) // 250 + 1) * 1.20
    if express:
        cost = cost * 2
    return cost


# CASE OF Weight
#    0 TO 100 : Cost ← 1.50
#    101 TO 500 : Cost ← 3.00
#    OTHERWISE : Cost ← 3.00 + ((Weight - 500) DIV 250 + 1) * 1.20
# ENDCASE
# Express tests another variable and stays in a separate IF.
