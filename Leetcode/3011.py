from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        n = len(nums)
        temp = sorted(nums).copy()
        count = 1
        while count:
            count = 0
            for i in range(1,n):
                if nums[i-1] > nums[i] and bin(nums[i-1]).count("1") == bin(nums[i]).count("1"):
                    count += 1
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
                    
        return nums == temp