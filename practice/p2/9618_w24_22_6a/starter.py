import random
# Provided QP arrays; Python indices = QP - 1. Remaining sample slots unused.
Filling=['Cheese','Onion','Salmon','Anchovies','Peanut Butter']+['']*30
Bread=['White','Brown','Pitta']+['']*7
# RAND is the insert's random function, supplied for deterministic tests.
def RAND(Limit):
    return random.random()*Limit

def Special():
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
