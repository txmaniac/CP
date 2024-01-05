from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # it's optimal to assume that every elem in the list as the ending elem and 
        # try to find the length of longest increasing subseq using dp
        #
        # The idea is to find the length of the longest increasing subseq ending i
        # which can be used to compute the problem for index i + 1
        n = len(nums)
        lengths = [1] * n
        INF = 10 ** 9
        for i in range(1, n):
            temp = -INF
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = max(temp, lengths[j])

            if temp > -INF:
                lengths[i] = 1 + temp

        return max(lengths)