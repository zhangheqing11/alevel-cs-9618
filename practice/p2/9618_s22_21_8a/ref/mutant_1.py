# 9618_s22_21:8(a) MP5: random-numbers
import random
# STRING array, 500 rows x 2 columns; Python indices = pseudocode indices - 1.
Secret = [["", ""] for _ in range(500)]

def RandomChar():
    ThisRange = random.randrange(3)
    if ThisRange == 0:
        return chr(random.randrange(97,124))
    if ThisRange == 1:
        return chr(random.randrange(65,91))
    return str(random.randrange(10))
