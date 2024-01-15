from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        # count number of inward edges
        # 0/1 are the candidates

        edges = defaultdict(int)

        for (x,y) in matches:
            edges[y] += 1
            edges[x] = max(0, edges[x])

        zero_loss, one_loss = [], []
        for key in sorted(edges.keys()):
            if edges[key] == 1:
                one_loss.append(key)

            if edges[key] == 0:
                zero_loss.append(key)

        return [zero_loss, one_loss]