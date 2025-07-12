def OctalBase(decimal: int) -> int:
    def Transformer(decimal: int) -> int:
        if(decimal < 8):
            return decimal
        else:
            return  Transformer(decimal // 8)*10 + decimal % 8
    if(decimal > 0):
        return Transformer(decimal)
    else:
        return -Transformer(-decimal)

NumTeste = -142
print(OctalBase(NumTeste))