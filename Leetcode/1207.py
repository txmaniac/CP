from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = list(Counter(arr).values())
        return len(counts) == len(set(counts))