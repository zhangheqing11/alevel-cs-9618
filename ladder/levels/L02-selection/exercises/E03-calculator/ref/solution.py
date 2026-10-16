def calculator():
    n1=int(input("First: ")); op=input("Operator: "); n2=int(input("Second: "))
    if op=="+": print(f"Result: {n1+n2}")
    elif op=="-": print(f"Result: {n1-n2}")
    elif op=="*": print(f"Result: {n1*n2}")
    elif op=="/": print("Error: division by zero" if n2==0 else f"Result: {n1/n2}")
    elif op=="%": print("Error: division by zero" if n2==0 else f"Result: {n1%n2}")
    else: print("Error: unknown operator")
if __name__=="__main__": calculator()
