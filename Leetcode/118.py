from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]

        res = [[1],[1,1]]
        for i in range(2, numRows):
            temp = []
            for j in range(1, len(res[-1])):
                temp.append(res[-1][j] + res[-1][j - 1])
            
            temp = [1] + temp + [1]
            res.append(temp)

        return res