# 11. https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            res = max(res, min(height[left], height[right])*(right - left) )
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
max_area = s.maxArea(height)
print(max_area)