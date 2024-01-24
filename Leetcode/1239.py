from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:

        n = len(arr)
        cache = {}
        def recursion(i, curr_str):
            if i == n:
                return len(curr_str)

            if (i, curr_str) in cache:
                return cache[(i, curr_str)]

            deselect = recursion(i + 1, curr_str)

            # condition to even select the string to merge 
            flag = 0
            temp = set(curr_str)
            for ch in arr[i]:
                if ch in temp:
                    flag = 1
                    break
                else:
                    temp.add(ch)

            select = 0
            # ideal merge condition
            if not flag:
                select = recursion(i + 1, curr_str + arr[i])

            cache[(i, curr_str)] = max(select, deselect)
            return cache[(i, curr_str)]

        return recursion(0, "")