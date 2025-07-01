def inverterNumero(num):
    def A(num, resultado):
        if(num == 0):
            return resultado
        else:
            return A(num // 10, resultado * 10 + num % 10)
        
    return inverterNumero(num, 0)