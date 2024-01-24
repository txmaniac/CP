from collections import deque
# Iterative Solution using BFS
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)

        queue = deque([(0, 0, 0)])
        cache = set()
        count = 0

        while queue:
            i, j, count = queue.popleft()
            
            if (i, j) in cache:
                continue

            while i < m and j < n and word1[i] == word2[j]:
                i += 1
                j += 1
            
            if i == m and j == n:
                return count

            # insertion
            if (i, j+1) not in cache:
                queue.append((i, j+1, count + 1))
            # deletion
            if (i+1,j) not in cache:
                queue.append((i+1, j, count + 1))
            # modification
            if (i+1, j+1) not in cache:
                queue.append((i+1, j+1, count + 1))

            cache.add((i,j))

# Recursive Solution
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)

        if m == 0:
            return n
        if n == 0:
            return m
            
        cache = {}
        def recursion(i,j):
            if (i, j) in cache:
                return cache[(i,j)]

            if i == m or j == n:
                return (m - i) + (n - j) 

            # insert at first 
            l = 1 + recursion(i, j + 1)
            # modify the current index
            mid = int(word1[i] != word2[j]) + recursion(i + 1, j + 1)
            # delete at i'th index
            r = 1 + recursion(i + 1, j)

            cache[(i,j)] = min(l, mid, r)
            return cache[(i, j)]

        return recursion(0, 0)