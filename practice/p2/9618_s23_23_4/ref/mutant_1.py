# 9618_s23_23:4 MP3: boundary-values
def MakeString(Count, AChar):
    if Count<0:
        return 'ERROR'
    MyString=''
    for Index in range(Count):
        MyString+=AChar
    return MyString
