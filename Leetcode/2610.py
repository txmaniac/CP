from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        # basically we need to find the count of each var and then decide on the ith occurence it belongs to ith row

        counts = Counter(nums)

        n_rows = max(counts.values())

        matrix = [[] for _ in range(n_rows)]

        for key in counts:
            for i in range(counts[key]):
                matrix[i].append(key)

        return matrix