from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        items = freq.most_common()
        cost = 0
        
        for i, (x, c) in enumerate(items):
            if i < 8:
                cost += c
            elif 8 <= i < 16:
                cost += c * 2
            elif 16 <= i < 24:
                cost += c * 3
            else:
                cost += c * 4
            
        return cost