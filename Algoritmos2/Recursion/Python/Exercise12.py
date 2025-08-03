def OctalStringForDecimal(octal: str) -> int:
    def IsOctal(i: int) -> bool:
        if(i == 0):
            return octal[i] == '-' or ('0' <= octal[i] <= '7')
        return IsOctal(i - 1) and ('0' <= octal[i] <= '7')
    def Pos(i: int) -> int:
        if(i == 0):
            if(octal[i] == '-'):
                return 0
            else:
                return ord(octal[i]) - ord('0')
        return Pos(i - 1)*8 +  ord(octal[i]) - ord('0')
    if(len(octal) == 0 or not(IsOctal(len(octal) - 1))):
        return -999999
    if len(octal) == 1 and octal[0] == '-':
        return -999999
    if(octal[0] == '-'):
        return -Pos(len(octal) - 1)
    else:
        return Pos(len(octal) - 1)

NumTest = "-"
print(OctalStringForDecimal(NumTest))