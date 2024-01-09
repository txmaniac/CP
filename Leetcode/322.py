from typing import List
# SOLUTION 1
# TOP-DOWN APPROACH USING MEMOIZATION
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        INF = 10 ** 20
        cache = {}
        def recursion(amount):
            # base cases
            if amount < 0:
                return INF
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            res = INF
            for c in coins:
                res = min(res, 1 + recursion(amount - c))

            cache[amount] = res
            return cache[amount]
        res = recursion(amount)
        return res if res != INF else -1
    
# SOLUTION 2
# BOTTOM-DOWN APPROACH    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10 ** 9
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], dp[x - c] + 1)

        return dp[-1] if dp[-1] != INF else -1