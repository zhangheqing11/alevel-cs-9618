def Trim(Name):
    if len(Name)<=16:
        return Name
    while len(Name)>13:
        while Name[-1]!=' ':
            Name=Name[:-1]
        Name=Name[:-1]
    return Name+'...'
