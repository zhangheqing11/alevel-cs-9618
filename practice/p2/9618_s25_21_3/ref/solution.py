import random

def main():
    GeneratedValue=random.randint(1,100)
    while True:
        Guess=int(input('Enter a guess between 1 and 100: '))
        if Guess>GeneratedValue:
            print('Guess was too high')
        elif Guess<GeneratedValue:
            print('Guess was too low')
        else:
            print('Number guessed correctly')
            return
