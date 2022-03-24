from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        left_max = 0
        right = len(height) - 1
        right_max = 0
        result = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                result += left_max - height[left]
                left += 1
            else:
                result += right_max - height[right]
                right -= 1
        return result

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
res = s.trap(arr)
print(res)