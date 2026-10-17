# 9618_s25_22:3 MP4: input-validation
import random

def main():
    FirstNumber=random.randint(-10,10)
    print(FirstNumber)
    SecondNumber=random.randint(-10,10)
    while False:
        SecondNumber=random.randint(-10,10)
    print(SecondNumber)
    if FirstNumber<0 and SecondNumber<0:
        print(random.randint(30,35))
