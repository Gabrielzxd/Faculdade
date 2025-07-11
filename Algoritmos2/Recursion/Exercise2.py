def InverseNum(num: int) -> int:
    def aux(num, result: int) -> int:
        if(num == 0):
            return result
        else:
            return aux(num // 10, result * 10 + num % 10)
        
    if(num < 0):
        return - aux(- num, 0)
    else:
        return aux(num, 0)
    
NumTest = - 12345
NumTest = InverseNum(NumTest)
print(NumTest)
