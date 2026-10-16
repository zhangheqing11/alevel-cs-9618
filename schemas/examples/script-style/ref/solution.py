best_name, best_score = "", -1
with open("scores.txt", encoding="utf-8") as file:
    for line in file:
        name, score = line.strip().split(",")
        if int(score) > best_score:
            best_name, best_score = name, int(score)
print(f"Top: {best_name} {best_score}")
