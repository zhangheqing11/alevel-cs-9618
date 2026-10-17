# Provided filled ARRAY[0:35] OF BOOLEAN (part b is already completed).
# Python indices equal the QP indices.
CheckTotal = [False] * 36
for EasyQ in range(0,16,3):
    for HardQ in range(0,21,5):
        CheckTotal[EasyQ + HardQ] = True


def ValidateScore(TotalScore):
    """Implement the algorithm described in task.md."""
    raise NotImplementedError
