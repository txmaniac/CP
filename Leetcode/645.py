from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums)    
        temp = -1
        for key in counts:
            if counts[key] > 1:
                temp = key
                break
                
        for i in range(1, n+1):
            if i not in counts:
                return [temp, i]