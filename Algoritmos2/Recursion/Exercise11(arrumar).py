def BinaryForDecimal(binary: int) -> int:
    def IsBinary(binary: int) -> bool:
        if(binary == 0):
            return True
        return IsBinary(binary // 10) and (0 <= binary % 10 <= 1)
    
    if(not(IsBinary(binary))):
        return -999999
    if(binary == 0 or binary == 1):
        return binary
    return BinaryForDecimal(binary // 10) * 2 + binary % 10

NumTest = 101
print(BinaryForDecimal(NumTest))