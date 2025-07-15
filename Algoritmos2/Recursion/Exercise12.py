def OctalStringForDecimal(octal: str) -> int:
    def IsOctal(i: int) -> bool:
        if(i == 0):
            if(octal[i] == '-'):
                return True
            else:
                return '0' <= octal[i] <= '7'
        return IsOctal(i - 1) and ('0' <= octal[i] <= '7')
    def Pos(i: int) -> int:
        if(i == 0):
            if(octal[i] == '-'):
                return 0
            else:
                return ord(octal[i]) - ord('0')
        return Pos(i - 1)*8 +  ord(octal[i]) - ord('0')
    if(not(IsOctal(octal))):
        return -999999
    if(octal[0] == '-'):
        return -Pos(len(octal) - 1)
    else:
        return Pos(len(octal) - 1)

NumTest = "-145"
print(OctalStringForDecimal(NumTest))