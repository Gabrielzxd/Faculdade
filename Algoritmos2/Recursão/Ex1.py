def stringMinuscula(s):
    def transformar(i):
        if i >= len(s):
            return ""
        else:
            if 'A' <= s[i] <= 'Z':
                return chr(ord(s[i]) - ord('A') + ord('a')) + transformar(i + 1)
            else:
                return s[i] + transformar(i + 1)
    
    return transformar(0)

def main():
    s = "GaBBr!@a0ieMM_"
    print("Minuscula: ", stringMinuscula(s))

if __name__ == "__main__":
    main()