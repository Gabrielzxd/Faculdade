def DecimalStringForBinary(decimal: str) -> int:
    def VerifyString(i: int) -> bool:
        if i < 0:
            return False
        if i == 0:
            return decimal[i] == '-' or ('0' <= decimal[i] <= '9')
        return VerifyString(i - 1) and '0' <= decimal[i] <= '9'
    def StringForInteger(i: int) -> int:
        if(i == 0):
            if(decimal[i] == '-'):
                return 0
            else:
                return ord(decimal[i]) - ord('0')
        else:
            return StringForInteger(i-1)*10 + ord(decimal[i]) - ord('0')
    def DecimalToBinary(decimal: int) -> int:
        if(decimal == 0 or decimal == 1):
            return decimal
        else:
            return (DecimalToBinary(decimal // 2))*10 + decimal % 2
    if(not(VerifyString(len(decimal) - 1))):
        return -999999
    else:
        num = StringForInteger(len(decimal) - 1)
        if(decimal[0] == '-'):
            return - DecimalToBinary(num)
        else:
            return DecimalToBinary(num)
        
Test = "-14"
print(DecimalStringForBinary(Test))

    