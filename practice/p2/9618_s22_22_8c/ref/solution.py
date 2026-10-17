import random

# Provided modules; comparisons are case-sensitive.
def Exists(Text, Character):
    for Item in Text:
        if Item == Character:
            return True
    return False


def RandomChar():
    return random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


def GeneratePassword():
    Password = ""
    for Group in range(3):
        if Group > 0:
            Password += "-"
        for Count in range(4):
            Character = RandomChar()
            while Exists(Password, Character):
                Character = RandomChar()
            Password += Character
    return Password
