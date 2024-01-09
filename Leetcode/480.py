from bisect import bisect, bisect_right
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        n = len(nums)

        window = []
        res = []
        med_index = k // 2

        for i in range(n):
            if len(window) < k:
                index = bisect_right(window, nums[i])
                window.insert(index, nums[i])

            else:
                # find median
                if k % 2:
                    median = float(window[k // 2])
                else:
                    median = (window[k // 2] + window[k // 2 - 1]) / 2

                res.append(median)
                # remove left and add right using bisect
                left = nums[i - k]
                right = nums[i]

                index = bisect(window, left)
                window.pop(index-1)

                index = bisect_right(window, right)
                window.insert(index, right)

        if k % 2:
            median = float(window[k // 2])
        else:
            median = (window[k // 2] + window[k // 2 - 1]) / 2

        res.append(median)
        return res