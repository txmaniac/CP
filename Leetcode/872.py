# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return []

            if root.left == None and root.right == None:
                return [root.val]

            left = dfs(root.left)
            right = dfs(root.right)

            return left + right

        return dfs(root1) == dfs(root2)