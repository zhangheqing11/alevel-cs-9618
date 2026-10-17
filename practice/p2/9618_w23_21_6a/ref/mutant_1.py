# 9618_w23_21:6(a) MP3: boundary-values
MyString = ''  # Global STRING, maximum buffered length 255.

def MyOutput(NewString,EOL):
    global MyString
    if len(MyString)+len(NewString)>=255:
        print(MyString)
        MyString=NewString
    else:
        MyString+=NewString
        if EOL:
            print(MyString)
            MyString=''
