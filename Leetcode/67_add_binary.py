# 67. https://leetcode.com/problems/add-binary/

#       1 0 1 0
# +   1 0 1 1 1
# = 1 0 0 0 0 1


class Solution(object):
    def addBinary(self, a, b):
        res = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry != 0:
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0
            sum = digitA + digitB + carry
            carry = 1 if sum >= 2 else 0
            sum = sum - 2 if sum >= 2 else sum
            res += str(sum)
            i -= 1
            j -= 1
        return res[::-1]

s1 = Solution()
a = "11"
b = "1"
print(s1.addBinary(a, b))