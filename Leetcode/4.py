from typing import List

# SOLUTION 1
# MERGING TWO LISTS TC: O(M + N)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1 = 0
        ptr2 = 0

        res = []
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] < nums2[ptr2]:
                res.append(nums1[ptr1])
                ptr1 += 1
            else:
                res.append(nums2[ptr2])
                ptr2 += 1

        if ptr1 == len(nums1):
            res += nums2[ptr2:]

        else:
            res += nums1[ptr1:]

        print(res)

        mid = len(res) // 2
        if len(res) % 2 == 0:
            return (res[mid] + res[mid - 1]) / 2

        else:
            return float(res[mid])