def LowerString(s: str) -> str:
    def Transform(i: int) -> str:
        if i < 0:
            return ""
        elif 'A' <= s[i] <= 'Z':
            return Transform(i - 1) + chr(ord(s[i]) - ord('A') + ord('a'))
        else:
            return Transform(i - 1) + s[i]
    
    return Transform(len(s) - 1)

example = LowerString("AHKZllk08@am7H")
print(example)
