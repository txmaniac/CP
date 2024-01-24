class Solution:
    def minimumPushes(self, word: str) -> int:
        # pigeon hole
        cost = 0
        for i, ch in enumerate(word):
            if i < 8:
                cost += 1    
            elif 8 <= i < 16:
                cost += 2
            elif 16 <= i < 24:
                cost += 3
            else:
                cost += 4
                
        return cost