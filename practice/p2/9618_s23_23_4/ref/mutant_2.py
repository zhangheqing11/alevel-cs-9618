# 9618_s23_23:4 MP4: loop-bounds
def MakeString(Count, AChar):
    if Count<1:
        return 'ERROR'
    MyString=''
    for Index in range(Count-1):
        MyString+=AChar
    return MyString
