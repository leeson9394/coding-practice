#1. Two Sum
#https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        kv={}
        for i in range(0, len(nums)):
            if target - nums[i] in kv:
                return [kv[target - nums[i]], i]
            kv[nums[i]]=i


# class Solution:
#     def __init__(self):
#         self.kv={}

#     def ListToHash(self, nums):
#         for element in range(0, len(nums)):
#             self.kv[nums[element]] = element
#         return self.kv

#     def twoSum(self, nums, target):
#         for element in range(0, len(nums)):
#             if target - nums[element] in self.kv.keys():
#                 print ([element, self.kv[target - nums[element]]])
#             self.kv[nums[element]] = element
#             self.ListToHash(nums)

a=Solution()
nums=[15,7,11,2,3,5,4]
target=9
a.twoSum(nums,target)
