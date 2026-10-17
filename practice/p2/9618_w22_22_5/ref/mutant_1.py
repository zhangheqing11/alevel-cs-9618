# 9618_w22_22:5 MP3: logic-ops
A = False
B = False
C = False
# Provided procedures; tests observe their calls.
def Sub1():
    print('Sub1')
def Sub2():
    print('Sub2')
def Sub3():
    print('Sub3')
def Sub4():
    print('Sub4')

def main():
    if A and B and C:
        Sub1()
    if A and B and not C:
        Sub2()
    if not A and not B and not C:
        Sub3()
    if not A and C:
        Sub4()
