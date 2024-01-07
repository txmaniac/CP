from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        dp = [defaultdict(int) for _ in range(n)]
        # NOTES
        # The idea is to find the subsequence ending at i
        # with a length of atleast 3
        # The recurrence relation is as follows
        # dp[i][diff] = dp[i][diff] + 1 + dp[j][diff]
        # 2,4,6,8,10
        # if i == 2, j == 1, diff = 2
        # dp[2][2] = 0 + 1 + dp[1][2] ( which is 1 because (2,4) is a subsequence)
        # if dp[i][diff] == 0, then the length of subsequence is 0 else length of subsequence is atleast 2
        # I DON'T COMPLETELY UNDERSTAND THIS PART

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                total += dp[j][diff] # (we add the count of subsequence of length 2 only after we find another entry which can make the length atleast)
        return total