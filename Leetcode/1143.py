class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        cache = {}
        def recursion(i, j):
            if i == m - 1 and j == n - 1:
                return int(text1[i] == text2[j])
            
            if (i, j) in cache:
                return cache[(i,j)]

            if i < m and j < n:
                if text1[i] == text2[j]:
                    cache[(i,j)] = 1 + recursion(i + 1, j + 1)
                else:
                    cache[(i,j)] = max(recursion(i + 1, j), recursion(i, j + 1))
                return cache[(i,j)]
            return 0

        res = recursion(0, 0)
        return res