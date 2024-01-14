from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxVal = max(counts.values())
        
        total = 0
        for c in counts.values():
            if maxVal == c:
                total += c
        return total