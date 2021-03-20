# leetcode 112
# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            if sum == root.val:
                return True
            else:
                return False
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
sol = Solution()
res = sol.hasPathSum(root, targetSum)
print(res)