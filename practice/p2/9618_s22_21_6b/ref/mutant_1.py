# 9618_s22_21:6(b) MP2: nested-if
MySwitch = 0
ThisChar = ''

MySwitch = 0
ThisChar = ''

def main():
    global ThisChar
    if MySwitch == 1:
        ThisChar = 'a'
    elif MySwitch == 2:
        ThisChar = 'a'
    elif MySwitch == 3:
        ThisChar = '7'
    else:
        ThisChar = '*'
