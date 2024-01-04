from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # find max per sliding window range using segment tree
        # LEARN SEGMENT TREE IMPLEMENTATION
        # n == 16
        # k = 4 -> log2(n)

        # total number of nodes = 2 ^ (k + 1) - 1
        # 2 * 2 ^ (log2(n)) - 1
        # 2 * n - 1
        # O(n)
        
        pass