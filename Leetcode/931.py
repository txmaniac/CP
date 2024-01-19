from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        INF = 10 ** 20

        cache = {}
        def minPathSum(i,j):
            if i == m:
                return 0
            
            if (i, j) in cache:
                return cache[(i,j)]

            if 0 <= j < n:
                # choose three possibilities
                cache[(i,j)] = matrix[i][j] + min(
                    minPathSum(i + 1, j - 1), 
                    minPathSum(i + 1, j),
                    minPathSum(i + 1, j + 1)
                )
                return cache[(i,j)]
            
            return INF

        res = INF
        for j in range(n):
            res = min(res, minPathSum(0, j))

        return res