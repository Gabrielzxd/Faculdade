FLAG = -1

def NumberTimesNumberInOuther(a, b: int) -> int:
    def Digit_Count(a, b: int) -> int:
        if(a == 0):
            return 0
        if(a % 10 == b):
            return 1 + Digit_Count(a // 10, b)
        return Digit_Count(a // 10, b)
    if(a <= 0 or b <= 0 or b > 9):
        return FLAG
    return Digit_Count(a,b)
    
a = 12
b = 4
print(NumberTimesNumberInOuther(a, b))
