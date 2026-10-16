# Compares scores as strings: "9" > "10"
best_name, best_score = "", ""
with open("scores.txt", encoding="utf-8") as file:
    for line in file:
        name, score = line.strip().split(",")
        if score > best_score:
            best_name, best_score = name, score
print(f"Top: {best_name} {best_score}")
