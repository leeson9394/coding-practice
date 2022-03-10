# 104. https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution1:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # left_max = self.maxDepth(root.left)
        # right_max = self.maxDepth(root.right)
        
        # return 1 + max(left_max, right_max)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = self.dfs(root)
        return res

    def dfs(self, node):
        if not node:
            return 0
        left_max = self.dfs(node.left)
        right_max = self.dfs(node.right)
        depth = 1 + max(left_max, right_max)
        return depth

# BFS
class Solution2:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root:
            return depth
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1
        return depth

