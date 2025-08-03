def WriteSums(num: int) -> int:
    def sums(num: int) -> int:
        if(num == 0):
            print(0)
            return 0
        else:
            s = sums(num - 1) + num
            print(", ", s)
            return sums(num - 1)

    if(num >= 0):
        print("{")
        s = sums(num)
        print("}")
    return s