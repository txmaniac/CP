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

# Optimal solution O(nlogn)

from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        sorted_list = []
        
        # idea is to find the sequence in nums wherein every num we visit sequentially is placed at the end of the sorted_list
        # In case if the index is not at the end of the sorted_list
        # it means that we have a subsequence with lower values
        # so we replace the values at the indexes
        # NOTE: Here we don't remove any added values to list
        # so if new values come in, then only max value is affected

        for num in nums:
            index = bisect_left(sorted_list, num)

            if index == len(sorted_list):
                sorted_list.append(num)

            else:
                sorted_list[index] = num

        return len(sorted_list)