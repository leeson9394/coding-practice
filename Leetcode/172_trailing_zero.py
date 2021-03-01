# Leetcode 172

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # res = 1
        # for i in range(1,n+1):
        #     res = res * i
        # return res 
        res = 0
        i = 5
        while n >= i:
            res = res + n // i
            i = i * 5
        return res

sol = Solution()
res = sol.trailingZeroes(30)
print(res)
