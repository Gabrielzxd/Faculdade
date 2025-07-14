def HexadecimalBase(decimal: int) -> str:
    if(decimal == 0):
        return ""
    if(decimal < 0):
        return "-" + HexadecimalBase(-decimal)
    if(decimal % 16 >= 10):
        return HexadecimalBase(decimal // 16) + chr(decimal % 16 - 10 + ord('A'))
    else:
        return HexadecimalBase(decimal // 16) + chr(decimal % 16 + ord('0'))

NumTest = 145
print(HexadecimalBase(NumTest))