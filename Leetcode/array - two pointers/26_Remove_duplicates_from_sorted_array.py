# 26. https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        # use while loop
        # while j < len(nums):
        #     if i == 0 or nums[j] != nums[i-1] : # parsing arr with j cursor, found new element than left element of i cursor
        #         nums[i] = nums[j] 
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1
        # return i

        # use for loop
        for j in range(len(nums)):
            if i == 0 or nums[j] != nums[i-1] :
                nums[i] = nums[j]
                i += 1
        return i

arr = [1,1,1,2,3,4,4,4,5]
sol = Solution()
res = sol.removeDuplicates(arr)
print(res)

