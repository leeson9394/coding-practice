# leetcode 15. 3Sum
# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        res = []

        for i in range(len(nums)):
            target = 0 - nums[i]
            num_to_index = {} # reset dict when target changed
            for j in range(i + 1, len(nums)):
                if target - nums[j] in num_to_index:
                    res_candidate = ([ nums[i], target - nums[j], nums[j] ])
                    if res_candidate not in res: # remove duplidate result
                        res.append(res_candidate)

                num_to_index[nums[j]] = j
        
        return res



sol=Solution()
nums=[-1, 0, 1, 2, -1, -4]
target=0
res=sol.threeSum(nums)
print(res)



