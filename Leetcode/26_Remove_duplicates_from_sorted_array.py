class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        nums_set = set(nums)
        for item in nums_set:
            res.append(item)
        return len(res), res

arr = [1,1,1,2,3,4,4,4,5]
sol = Solution()
res = sol.removeDuplicates(arr)
print(res)