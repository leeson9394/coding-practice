# Leetcode 1492. https://leetcode.com/problems/the-kth-factor-of-n/

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        stack =[]
        for i in range(1, n+1):
            if n % i == 0:
                stack.append(i)
        return stack[k-1] if k <= len(stack) else -1

sol = Solution()
res = sol.kthFactor(12, 3)
print(res)