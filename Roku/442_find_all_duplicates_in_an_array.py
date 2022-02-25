# Leetocde #442 Find All Duplicates in an Array
class Solution(object):
    def findDuplicates(self, arr):
        # left = 0
        # right = len(arr) - 1
        # arr.sort() 
        # res = []
        # for i in range(len(arr)-1):
        #     if arr[i] == arr[i+1]:
        #         res.append(arr[i])
        # return res
        kv = {}
        res = []
        for item in arr:
            if item in kv:
                res.append(item)
            kv[item] = "exists"
        return res
# time complexity O(n), space complexity O(n)

array = [4,3,2,7,8,2,3,1]
s = Solution()
result = s.findDuplicates(array)
print(result)


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            nums[abs(num) - 1] *= - 1
        return ans
# time complexity O(n), space complexity O(1)