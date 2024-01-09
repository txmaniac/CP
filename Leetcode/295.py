from bisect import bisect_right
from heapq import heappush, heappushpop

# SOLUTION 1
# Insert O(logn) using bisect and list insert O(1)
class MedianFinder:
    def __init__(self):
        self.med_index = 0
        self.nums = []

    def addNum(self, num: int) -> None:
        # inserting at O(logn)
        index = bisect_right(self.nums, num)
        self.nums.insert(index, num)
        if len(self.nums) % 2 == 0:
            self.med_index += 1

    def findMedian(self) -> float:
        if len(self.nums) % 2 == 0:
            return (
                self.nums[self.med_index] + self.nums[self.med_index - 1]
            ) / 2

        return self.nums[self.med_index]

# SOLUTION 2
# Insert O(logn) using max and min heap
class MedianFinder:
    def __init__(self):
        # left for max heap
        self.leftHeap = []
        # right for min heap
        self.rightHeap = []

    def addNum(self, num: int) -> None:
        
        if len(self.leftHeap) == len(self.rightHeap):
            heappush(self.leftHeap, -heappushpop(self.rightHeap, num))
        else:
            heappush(self.rightHeap, -heappushpop(self.leftHeap, -num))

    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        else:
            return (-self.leftHeap[0])