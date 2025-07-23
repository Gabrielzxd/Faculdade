def MDC(a, b: int) -> int:
    if a <= 0 or b <= 0:
        return -1
    if b > a:
        aux = b
        b = a
        a = b
    if a % b == 0:
        return b
    return MDC(b, a % b)

print(MDC(4, 12))
