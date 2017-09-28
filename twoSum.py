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
        for i in xrange(0,len(nums)):
            if target - nums[i] in kv:
                return [kv[target - nums[i]], i]
            kv[nums[i]]=i
            print kv


a=Solution()
nums=[15,7,11,2,3,6]
target=9
print a.twoSum(nums,target)

# class Solution():
#     def __init__(self):
#         self.kv={}
#
#     def ListToHash(self, nums):
#         for element in xrange(len(nums)):
#             self.kv[nums[element]] = element
#         return self.kv
#
#     def twoSum(self, nums, target):
#         for element in xrange(len(nums)):
#             if target - nums[element] in self.kv.keys():
#                 return [element, self.kv[target - nums[element]]]
#             # self.kv[nums[element]] = element
#             self.ListToHash(nums)


