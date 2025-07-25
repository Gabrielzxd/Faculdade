def MenorString(v, t):
    if t == 1:
        return v[0] 
    menor = MenorString(v, t - 1)
    if v[t - 1] < menor:
        return v[t - 1]
    else:
        return menor
lista = ["b", "aa", "d", "a"]
print(MenorString(lista, len(lista)))