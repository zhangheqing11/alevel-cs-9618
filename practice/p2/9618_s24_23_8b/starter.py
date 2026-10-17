# Provided Header module; sample capacity (QP only requires sufficient rows).
# QP gives no total capacity; 11 illustrative STRING rows hold its two examples.
# Python indices = pseudocode indices - 1; Header does not access ModInfo.
ModInfo = [["", "", ""] for _ in range(11)]
ModInfo[9] = ["27", "P", "MyProc(Z : CHAR)"]
ModInfo[10] = ["35", "F", "MyFun(Y : CHAR) RETURNS BOOLEAN"]

def Header(Line):
    if len(Line)>=13:
        if Line[:9].upper()=='FUNCTION ':
            return 'F'+Line[9:]
        if Line[:10].upper()=='PROCEDURE ':
            return 'P'+Line[10:]
    return ''

ModInfo=[['','',''] for _ in range(100)]

def FindModules(FileName):
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
