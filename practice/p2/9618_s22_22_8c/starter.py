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
    """Implement the algorithm described in task.md."""
    raise NotImplementedError
