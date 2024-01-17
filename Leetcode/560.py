from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hash = defaultdict(int)
        hash[0] = 1 # used to store count of occurence of sums
        currSum = 0
        res = 0
        for num in nums:
            currSum += num
            diff = currSum - k
            res += hash[diff]
            hash[currSum] += 1
        
        return res