# leetcode 226

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.swap(root)
        return root
    def swap(self, node):
        if not node:
            return
        node.left, node.right = self.swap(node.right), self.swap(node.left)
        return node