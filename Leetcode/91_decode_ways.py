# 91. https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, data:str) -> int:
        return self.helper(data, len(data))

    def helper(self, data:str, k:int) -> int:
        s = len(data) - k ## start pointer in each recursive layer

        if k == 0: ## base case: numDecodings("") = 1
            return 1
        if data[s] == "0": ## base case: numDecodings("0123") = 0
            return 0

        result = self.helper(data, k - 1)
        if k >= 2 and int(data[s:s+2]) <=26: 
            result += self.helper(data, k - 2)
        return result

## Dynamics Programming - memoization

class Solution:
    def numDecodings(self, data:str) -> int:
        memo = [None] * (len(data) + 1)
        return self.helper(data, len(data), memo)

    def helper(self, data:str, k:int, memo:list) -> int:
        s = len(data) - k

        if k == 0:
            return 1
        if data[s] == "0":
            return 0
        if memo[k] != None:
            return memo[k]

        result = self.helper(data, k - 1, memo)
        if k >= 2 and int(data[s:s+2]) <=26: 
            result += self.helper(data, k - 2, memo)
        memo[k] = result
        return result

## Dynamics Programming solution
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if s=="" or s[0]=='0': return 0
        dp=[1,1]
        for i in range(2,len(s)+1):
            if 10 <=int(s[i-2:i]) <=26 and s[i-1]!='0':
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                dp.append(dp[i-2])
            elif s[i-1]!='0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]