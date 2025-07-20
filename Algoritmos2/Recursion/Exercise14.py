def MaxValue(flag: float) -> float:
    num = float(input())
    if(num == flag):
        return num
    max = MaxValue(flag)
    if(num > max or num == flag):
        return num
    return max