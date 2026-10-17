# 9618_s25_21:3 MP9: output-format
import random

def main():
    GeneratedValue=random.randint(1,100)
    while True:
        Guess=int(input('Enter a guess between 1 and 100: '))
        if Guess>GeneratedValue:
            print('Guess was too high')
        elif Guess<GeneratedValue:
            print('Guess was too high')
        else:
            print('Number guessed correctly')
            return
