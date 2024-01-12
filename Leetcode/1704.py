class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]
        vowels = 'aAeEiIoOuU'

        cA, cB = 0, 0

        for x,y in zip(a,b):
            if x in vowels:
                cA += 1
            if y in vowels:
                cB += 1

        return cA == cB