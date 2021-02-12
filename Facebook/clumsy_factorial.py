# Leetcode 1006

class Solution:
    def clumsy(self, N):
        res, d = 0, 0
        stack = list()
        for i in range(N, 0, -1):
            if stack:
                if d % 4 == 0:
                    val = stack.pop()
                    stack.append(val*i)
                    print(stack)
                elif d % 4 == 1:
                    val = stack.pop()
                    stack.append(val//i)
                    print(stack)
                elif d % 4 == 2:
                    stack.append(i)
                    print(stack)
                elif d % 4 == 3:
                    stack.append(i)
                    print(stack)
                d += 1
            else:
                stack.append(i)
                
        if stack:
            res = stack[0]
            for i, val in enumerate(stack[1:]):
                if i & 1 == 0:
                    res += val
                else:
                    res -= val
        
        return res

N = 10
sol = Solution()
answer = sol.clumsy(N)
print(answer)
