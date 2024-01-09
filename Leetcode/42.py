from typing import List

# IDEA OF THE SOLUTION:

# To find if there are holes at a certain index, we need to find the "max of the left side so far" and "the right side so far" of the index,
# Since, these will be the place where water logging can be possible, if leftMax and rightMax are greater than the current index's height

# Water logging happens as follows min(L, R) - height[i]

# min(L,R) because we can water log to a height exactly equal to the min

# min(L,R) - height[i] because we need to count the water logged blocks at that index which is pretty straight forward

class Solution:
    def trap(self, height: List[int]) -> int:

        l,r = 0, len(height) - 1

        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res