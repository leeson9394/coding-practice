# leetcode 78
# Given an integer array nums of unique elements, return all possible subsets 
# https://leetcode.com/problems/subsets/
# Example: 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path =[]
        index = 0
        self.dfs(nums, index, res, path)
        return res
    
    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])
            # print(path)
        
nums = [1, 2, 3]
sol = Solution()
res = sol.subsets(nums)
print(res)