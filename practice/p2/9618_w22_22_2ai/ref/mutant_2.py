# 9618_w22_22:2(a)(i) MP3: relational-ops.


def main():
    with open("Support_List.txt", "a", encoding="utf-8") as Target:
        for Count in range(35):
            Name = input("Name: ")
            Mark = float(input("Mark: "))
            if Mark <= 20:
                Target.write(Name + "\n")
