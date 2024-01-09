class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def recursion(n):
            if n == 1 or n == 2:
                return n

            if n in cache:
                return cache[n]

            cache[n] = recursion(n - 1) + recursion(n - 2)
            return cache[n]
        return recursion(n)