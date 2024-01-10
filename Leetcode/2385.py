# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import defaultdict, deque

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # IDEA - convert tree to graph (redundant and unoptimized)
        # Perform BFS on the graph (TC: O(E+V))
        graph = defaultdict(list)
        def dfs(root):
            if root:
                if root.left:
                    graph[root.val].append(root.left.val)
                    graph[root.left.val].append(root.val)
                
                if root.right:
                    graph[root.val].append(root.right.val)
                    graph[root.right.val].append(root.val)

                dfs(root.left)
                dfs(root.right)

        dfs(root)
        queue = deque([(start, 0)])
        visited = set()
        while queue:
            node, time = queue.popleft()

            if node not in visited:
                visited.add(node)
                for nbr in graph[node]:
                    if nbr not in visited:
                        queue.append((nbr, time + 1))

        return time