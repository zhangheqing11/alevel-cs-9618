def calculator() -> None:
    num1 = int(input("First integer: "))
    operator = input("Operator: ")
    num2 = int(input("Second integer: "))
    if operator == "+":
        print(f"Result: {num1 + num2}")
    elif operator == "-":
        print(f"Result: {num1 - num2}")
    elif operator == "*":
        print(f"Result: {num1 * num2}")
    elif operator == "/":
        if num2 == 0:
            print("Error: division by zero")
        else:
            print(f"Result: {num1 / num2}")
    elif operator == "%":
        if num2 == 0:
            print("Error: division by zero")
        else:
            print(f"Result: {num1 % num2}")
    else:
        print("Error: unknown operator")


if __name__ == "__main__":
    calculator()
