from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search in the row first till target > num[i]
        # in this case, we know that target isn't in the row so we need to switch the row and search

        m, n = len(matrix), len(matrix[0])

        # start search from any corner of first row
        i = 0
        j = n - 1

        while i < m and j >= 0:
            # Check in the ith row
            while j > 0 and target < matrix[i][j]:
                j -= 1
            
            if target == matrix[i][j]:
                return True
            
            # shift row
            i += 1
        return False