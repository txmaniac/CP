from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        coords = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    coords.append((i, j))

        for x, y in coords:
            for i in range(n):
                matrix[x][i] = 0

            for i in range(m):
                matrix[i][y] = 0