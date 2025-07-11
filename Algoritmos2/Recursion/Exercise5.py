FLAG = -1

def NumberTimesNumberInOuther(a, b: int) -> int:
    if(a < 0 or b < 0):
        return FLAG
    else:
        if(b // 10 != 0):
            return FLAG
        else:
            if(a == 0):
                return 0
            else:
                if(a % 10 == b):
                    return 1 + NumberTimesNumberInOuther(a // 10, b)
                else:
                    return NumberTimesNumberInOuther(a // 10, b)

a = 123452
b = 2
print(NumberTimesNumberInOuther(a, b))
