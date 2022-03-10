# 102. https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque
import queue
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Solution 1: use double-end queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        if not root: 
            return res
        while q:
            level = []
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            print(level)
            res.append(level)
        return res

# Solution 2: use list as queue
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = []
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                cur = q.pop(0)
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)
        return res


