#15. 3Sum
#https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result=[]
        # print nums
        for i in xrange(0,len(nums)):
            target= 0 - nums[i]
            kv = {}
            for j in xrange(i+1,len(nums)):
                if  target - nums[j] in kv:
                    tmp_result=([nums[i], target - nums[j], nums[j]])
                    if tmp_result not in result:
                        result.append(tmp_result)
                kv[nums[j]] = j
            # print kv
        return result



a=Solution()
nums=[-1, 0, 1, 2, -1, -4]
target=0
print a.threeSum(nums)



