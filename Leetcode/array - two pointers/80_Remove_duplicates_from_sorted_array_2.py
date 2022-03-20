# 80. https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        for j in range(len(nums)):
            if i == 0 or nums[j] != nums[i-2]:
                nums[i]= nums[j]
                i += 1
        return i
            
