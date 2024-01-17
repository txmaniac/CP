from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        
        for n in nums:
            if (n-1) not in numSet:
                # start of the sequence
                l = 1
                while (n + l) in numSet:
                    l += 1

                maxLen = max(l, maxLen)

        return maxLen