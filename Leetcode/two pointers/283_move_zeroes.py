# 283. https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = 0
        for j in range(N):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1