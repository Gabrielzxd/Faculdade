def OctalStringForDecimal(octal: str) -> int:
    def IsOctal(octal: str) -> bool:
        def Position(i: int) -> bool: #Talvez não precise dessa função
            if(i == 0):
                return '0' <= octal[i] <= '7'
            return Position(i-1) and ('0' <= octal[i] <= '7')
        return Position(len(octal) - 1)
    def Position(i: int) -> int:
        if(i == 0):
            return ord(octal[i]) - ord('0')
        return Position(i - 1)*8 +  ord(octal[i]) - ord('0')
    if(not(IsOctal(octal))):
        return -999999
    else:
        Position(len(octal) - 1)

NumTest = "145"
print(OctalStringForDecimal(NumTest))