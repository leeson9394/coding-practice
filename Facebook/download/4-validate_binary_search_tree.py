# 98. https://leetcode.com/problems/validate-binary-search-tree/
# explanation: https://blog.csdn.net/fuxuemingzhu/article/details/70209865

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root: TreeNode):
        stack = []
        previous = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= previous:
                return False
            previous = root.val
            root = root.right
        return True

# solution 2 DFS
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.dfs(root, float('-inf'), float('inf'))
        return res
        
    def dfs(self, node, min, max):
        if not node: 
            return True
        if node.val >= max or node.val <= min:
            return False
        return self.dfs(node.left, min, node.val) and self.dfs(node.right, node.val, max)


