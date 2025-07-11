def NumberCallsFibonacci(num: int) -> int:
    if(num == 0 or num == 1):
        return 1
    else:
        return NumberCallsFibonacci(num - 1) + NumberCallsFibonacci(num - 2) + 1
    
teste = NumberCallsFibonacci(5)
print(teste)
