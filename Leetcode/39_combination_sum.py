# leetcode 39

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        index=0
        self.dfs(candidates, target, index, res, [])
        return res

    def dfs(self, nums, target, index, res, path):
        if target == 0:
            res.append(path)
            return
        if nums[index] > target:
            return
        for i in range(index,len(nums)):
            # print(nums[i])
            self.dfs(nums, target-nums[i], i, res, path + [nums[i]])

target = 8
candidates = [2,3,5]
sol = Solution()
res = sol.combinationSum(candidates,target)
print(res)