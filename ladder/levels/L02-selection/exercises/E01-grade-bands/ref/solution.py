def grade(mark:int)->str:
    if 80<=mark<=100:return "A"
    if 70<=mark<=79:return "B"
    if 60<=mark<=69:return "C"
    if 50<=mark<=59:return "D"
    if 40<=mark<=49:return "E"
    if 0<=mark<=39:return "U"
    return "Invalid"
