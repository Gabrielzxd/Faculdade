def HexadecimalBase(decimal: int) -> str:
    def Transform(decimal: int) -> str:
        if(decimal == 0):
            return ""
        if(decimal < 0):
            return "-" + Transform(-decimal)
        if(decimal % 16 >= 10):
            return Transform(decimal // 16) + chr(decimal % 16 - 10 + ord('A'))
        else:
            return Transform(decimal // 16) + chr(decimal % 16 + ord('0'))
    if decimal == 0:
        return "0"
    else:
        return Transform(decimal)

NumTest = 16
print(HexadecimalBase(NumTest))