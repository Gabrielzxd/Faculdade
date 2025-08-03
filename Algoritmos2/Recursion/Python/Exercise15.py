def LastCharString(s, c: str) -> int:
    def position(i: int) -> int:
        if(i - 1 == 0):
            return 0
        else:
            if(s[i] == c[0]):
                return i
            else:
                return position(i-1)
    return position(len(s) - 1)

StringTest = "afdsfa"
print(LastCharString(StringTest, "a"))