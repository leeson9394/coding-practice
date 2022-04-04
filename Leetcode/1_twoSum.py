# 1. Two Sum
# https://leetcode.com/problems/two-sum/

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

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i in range(0, len(nums)):
            num_to_index[nums[i]] = i
            if target - nums[i] in num_to_index:
                return [num_to_index[target - nums[i]], i]


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
nums=[2,4,3]
target=6
print(a.twoSum(nums,target))
