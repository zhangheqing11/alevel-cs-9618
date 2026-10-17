def MakeString(Count, AChar):
    if Count<1:
        return 'ERROR'
    MyString=''
    for Index in range(Count):
        MyString+=AChar
    return MyString
