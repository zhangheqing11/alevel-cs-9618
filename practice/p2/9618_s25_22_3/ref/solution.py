import random

def main():
    FirstNumber=random.randint(-10,10)
    print(FirstNumber)
    SecondNumber=random.randint(-10,10)
    while SecondNumber==FirstNumber:
        SecondNumber=random.randint(-10,10)
    print(SecondNumber)
    if FirstNumber<0 and SecondNumber<0:
        print(random.randint(30,35))
