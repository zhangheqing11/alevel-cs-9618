# 9618_w23_21:8(d) MP4: field-extract
MyID = '101'  # Global STRING; demonstration computer ID, not used by GetField.

def GetField(Msg,FieldNo):
    if FieldNo==1:
        RetString=Msg[1:4]
    elif FieldNo==2:
        RetString=Msg[4:7]
    elif FieldNo==3:
        RetString=Msg[7:]
    else:
        RetString=''
    return RetString
