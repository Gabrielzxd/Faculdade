def OctalBase(decimal: int) -> int:
    if(decimal < 8):
        return decimal
    else:
        return  OctalBase(decimal // 8)*10 + decimal % 8

NumTeste = 142
print(OctalBase(142))