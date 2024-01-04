from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)

        if 1 in counts.values():
            return -1

        total = 0
        for count in counts.values():
            total += count // 3
            if count % 3:
                total += 1

        return total