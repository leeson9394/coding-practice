# Leetcode 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/#/description

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0
        
        N = len(nums)
        cur, prev = 0, 0
        res = float("-inf")
        for i in range(N):
            if prev > 0:
                cur = nums[i] + prev
            else:
                cur = nums[i] 
            prev = cur
            res = max(res, cur)
        return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
res = sol.maxSubArray(nums)
print(res)