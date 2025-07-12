def DecimalStringForBinary(decimal: str) -> int:
    def position(i: int) -> int:
        if(not('0' <= decimal[i]) <= '9'):
            return
        else:
            return