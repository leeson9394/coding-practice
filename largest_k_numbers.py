# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/#/description
# Given [3,2,1,5,6,4] and k = 2, return 5.


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=sorted(nums)
        return nums[len(nums)-k]

a=Solution()
print a.findKthLargest([3,2,1,5,6,4], 2)