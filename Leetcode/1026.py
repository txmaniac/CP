# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        maxval = -1
        def recursion(root):
            if not root:
                return []
            # leaf
            if not root.left and not root.right:
                return [root.val]

            nonlocal maxval
            left = recursion(root.left)
            right = recursion(root.right)

            # CONSTANT TIME ONLY SINCE ONLY 4 values are being iterated
            for val in left + right:
                maxval = max(maxval, abs(root.val - val))

            return [min(left + right + [root.val]), max(left + right + [root.val])]

        recursion(root)
        return maxval