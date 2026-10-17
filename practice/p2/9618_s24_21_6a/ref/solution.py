def IsRA(x1,y1,x2,y2,x3,y3):
    Len1=(x1-x2)**2+(y1-y2)**2
    Len2=(x1-x3)**2+(y1-y3)**2
    Len3=(x2-x3)**2+(y2-y3)**2
    return Len1==Len2+Len3 or Len2==Len1+Len3 or Len3==Len1+Len2
