class Solution(object):
    def backspaceCompare(self, s, t):
        newS = []
        newT = []
        for char in s:
            if char == '#':
                if newS:
                    newS.pop()
            else:
                newS.append(char)
        for char in t:
            if char == '#':
                if newT:
                    newT.pop()
            else:
                newT.append(char)
        return newS == newT