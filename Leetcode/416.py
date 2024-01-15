from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # since we only need to choose either of the partition
        # we compute for this/that scenario
        n = len(nums)
        total = sum(nums)
        cache = {}
        def recursion(i, total):
            if i == n:
                return total == 0

            if (i,total) in cache:
                return cache[(i, total)]
                
            cache[(i, total)] = recursion(i + 1, total - nums[i]) or recursion(i + 1, total)
            return cache[(i, total)]

        if(total%2): return False 

        return recursion(0, total // 2)