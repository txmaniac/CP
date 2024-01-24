from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution using hashmap to store counts of the node values
# NOTE: We just have to identify if the current node chain till child node is a PERMUTATION of a palindrome

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # to capture counts for the respective paths
        hashMap = defaultdict(int)

        def dfs(root):
            if not root:
                return 0
            # leaf check
            if not root.left and not root.right:
                count = 0
                hashMap[root.val] += 1
                for val in hashMap.values():
                    count += val % 2
                hashMap[root.val] -= 1
                return int(count <= 1)

            # add values to map
            hashMap[root.val] += 1
            left = dfs(root.left)
            right = dfs(root.right)
            hashMap[root.val] -= 1

            return left + right

        return dfs(root)
    
# Solution using the XOR property to check if the node chain is a PERMUTATION of palindrome

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # to capture counts for the respective paths
        def dfs(root, path):
            if not root:
                return 0
            # path is essentially setting the root.val'th bit using XOR
            # if a string is palidrome either path would be zero or be a power of 2

            path ^= (1 << root.val)
            # leaf check
            if not root.left and not root.right:
                # at leaf node, if the node chain is palindrome, either path == 0 or is equal to a power of 2
                # so if we perform path & (path - 1) (bitwise AND), we get 0
                # EX: if path == 4 -> 100 & 011 == 000 (0)
                # EX: if path == 5 -> 101 & 100 == 100 (4)
                return int(path & (path - 1) == 0)
                
            # add values to map
            left = dfs(root.left, path)
            right = dfs(root.right, path)
            
            return left + right

        return dfs(root, 0)