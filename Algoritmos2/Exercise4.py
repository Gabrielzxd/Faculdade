FLAG = 0

def MDC(a, b: int) -> int:
    if(a <= 0 or b <= 0):
        return FLAG
    else:
        if (b > a):
            return FLAG
        else:
            if(a == b):
                return a
            else:
                return MDC(b, a % b)