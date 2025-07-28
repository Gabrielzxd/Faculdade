def HexadecimalStringToDecimalString(hexa: str) -> str:
    def IsHexadecimal(i: int) -> bool:
        if(i == 0):
            return hexa[i] == '-' or ('0' <= hexa[i] <= '9') or ('A' <= hexa[i] <= 'F')
        return IsHexadecimal(i - 1) and ('0' <= hexa[i] <= '9' or 'A' <= hexa[i] <= 'F')
    def TransformerToInteger(i: int) -> int:
        if(i == 0):
            if(hexa[i] == '-'):
                return 0
            else:
                if('A' <= hexa[i] <= 'F'):
                    return ord(hexa[i]) - ord('A') + 10
                else:
                    return ord(hexa[i]) - ord('0')
        else:
            if('A' <= hexa[i] <= 'F'):
                return TransformerToInteger(i - 1)*16 + ord(hexa[i]) - ord('A') + 10
            else:
                return TransformerToInteger(i - 1)*16 + ord(hexa[i]) - ord('0')
    def TransformerIntegerToString(number: int) -> str:
        if(number == 0):
            return ""
        else:
            if(number < 9):
                return chr(number + ord('0'))
            else:
                return TransformerIntegerToString(number // 10) + chr(number % 10 + ord('0'))
    if(len(hexa) == 0 or not(IsHexadecimal(len(hexa) - 1))):
        return ""
    if(len(hexa) == 1 or hexa[0] == '-'):
        return ""
    num = TransformerToInteger(len(hexa) - 1)
    if(hexa[0] == '-'):
        return '-' + TransformerIntegerToString(num)
    else:
        return TransformerIntegerToString(num)  


HexaTest = "-1A1"
print(HexadecimalStringToDecimalString(HexaTest))