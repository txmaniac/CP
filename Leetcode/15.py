from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        n = len(nums)
        map = defaultdict(lambda: -1)
        def twoSum(i):
            target = -nums[i]
            for j in range(i+1, n):
                complement = target - nums[j]
                if map[complement] == i:
                    res.add(tuple(sorted([nums[i], nums[j], target - nums[j]])))
                map[nums[j]] = i

        visited = set()
        for i in range(n - 2):
            if nums[i] not in visited:
                twoSum(i)
                visited.add(nums[i])

        return res