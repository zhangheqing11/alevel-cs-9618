# 9618_s25_21:7(b)(i) MP9: file-append
def AddNewCustomers(NumToAdd):
    with open('Loyalty.txt',encoding='utf-8') as Source:
        for Line in Source:
            LastLine=Line
    CustomerID=int(LastLine[:6])
    with open('Loyalty.txt','a',encoding='utf-8') as Target:
        if NumToAdd>0 and not LastLine.endswith('\n'):
            Target.write('\n')
        for Count in range(NumToAdd):
            CustomerID+=1
            print(CustomerID)
            Target.write(str(CustomerID)+',1\n')
