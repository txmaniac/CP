from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def recursion(i):
            if i >= n - 1:
                return nums[n - 1] if i == n - 1 else 0

            if i in cache:
                return cache[i]
            # choose i, #choose i + 1
            cache[i] = max(nums[i] + recursion(i + 2), nums[i + 1] + recursion(i + 3))
            return cache[i]

        return recursion(0)