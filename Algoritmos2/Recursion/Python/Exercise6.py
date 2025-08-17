def MinString(names: list[str], length: int) -> str:
    def Aux(n: int, min: str) -> str:
        if n < 0:
            return min
        if names[n] < min:
            min = names[n]
        return Aux(n - 1, min)

    if length < 1:
        return ""
    return Aux(length - 1, names[length - 1])


names = ["João", "Maria", "Eduardo", "Antonio", "Julia"]
print(MinString(names, 5))