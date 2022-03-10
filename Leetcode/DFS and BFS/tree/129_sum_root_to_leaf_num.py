# 129. https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        num = 0
        res = [0]
        self.dfs(root, num, res)
        return res[0]
    
    def dfs(self, node, num, res):
        num = num * 10 + node.val
        if node.left == None and node.right == None:
            res[0] += num
            return 
        if node.left:
            self.dfs(node.left, num, res)
        if node.right:
            self.dfs(node.right, num, res)

root = TreeNode(1)