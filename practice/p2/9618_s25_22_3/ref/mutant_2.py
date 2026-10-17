# 9618_s25_22:3 MP7: logic-ops
import random

def main():
    FirstNumber=random.randint(-10,10)
    print(FirstNumber)
    SecondNumber=random.randint(-10,10)
    while SecondNumber==FirstNumber:
        SecondNumber=random.randint(-10,10)
    print(SecondNumber)
    if FirstNumber<0 or SecondNumber<0:
        print(random.randint(30,35))
