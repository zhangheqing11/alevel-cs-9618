# 9618_s24_22:4 MP4: logic-ops
def IsRA():
    a=int(input('Input length of the first side: '))
    b=int(input('Input length of the second side: '))
    c=int(input('Input length of the third side: '))
    if a*a==b*b+c*c:
        print('It is right-angled')
    else:
        print('Not right-angled')
