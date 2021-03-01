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

# sort 1 bubble
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         for i in range(0, len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[j] > nums[i] : 
#                     nums[j], nums[i] = nums[i], nums[j]

#         return nums[k-1] if k <= len(nums) else -1

# sort 2 insert sort
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         n = len(nums)
#         if n <= 1:
#             return nums[0]
#         for i in range (1, n):
#             target = nums[i]
#             while i > 0 and target > nums[i-1]:
#                 nums[i] = nums[i-1]
#                 i = i-1
#             nums[i] = target
#         return nums[k-1] if k <= len(nums) else -1




sol = Solution()
res = sol.findKthLargest([3,2,1,5,6,4], 2)
print(res)
