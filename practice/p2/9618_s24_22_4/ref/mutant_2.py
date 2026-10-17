# 9618_s24_22:4 MP5: output-format
def IsRA():
    a=int(input('Input length of the first side: '))
    b=int(input('Input length of the second side: '))
    c=int(input('Input length of the third side: '))
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print('It is right-angled')
    else:
        print('It is right-angled')
