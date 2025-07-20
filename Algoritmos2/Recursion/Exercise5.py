FLAG = -1

def NumberTimesNumberInOuther(a, b: int) -> int:
    def Digit_Count(a, b: int) -> int:
        if(a == 0):
            return 0
        if(a % 10 == b):
            return 1 + Digit_Count(a // 10, b)
        return Digit_Count(a // 10, b)
    if(a < 0 or b < 0):
        return FLAG
    if(b > 9):
        return FLAG
    if(a == 0 and b == 0):
        return 1
    return Digit_Count(a,b)
    
a = 130
b = 0
print(NumberTimesNumberInOuther(a, b))
