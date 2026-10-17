# 9618_w25_22:4(c) MP1: input-validation.
# Provided filled ARRAY[0:35] OF BOOLEAN (part b is already completed).
# Python indices equal the QP indices.
CheckTotal = [False] * 36
for EasyQ in range(0,16,3):
    for HardQ in range(0,21,5):
        CheckTotal[EasyQ + HardQ] = True


def ValidateScore(TotalScore):
    if TotalScore > 35:
        return False
    return CheckTotal[TotalScore]
