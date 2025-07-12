def HexadecimalBase(decimal: int) -> str:
    def Transformer(decimal: int) -> str:
        if(decimal == 0):
            return ""
        else:
            if(decimal % 16 >= 10):
                return Transformer(decimal // 16) + chr(decimal % 16 - 10 + ord('A'))
            else:
                return Transformer(decimal // 16) + chr(decimal % 16 + ord('0'))
    
    if(decimal > 0):
        return Transformer(decimal)
    else:
        return '-' + Transformer(-decimal)

NumTest = -145
print(HexadecimalBase(NumTest))