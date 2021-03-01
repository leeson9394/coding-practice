# leetcode 125. Valid Palindrome
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Filter the string and put character into list
        valid = []
        for char in s:
            if char.isalpha() or char.isdigit():
                valid.append(char.lower())

        left = 0
        right = len(valid) - 1

        while left < right:
            if valid[left] != valid[right]:
                return False
            left += 1
            right -= 1
        return True
        
        # traverse with for loop
        # for i in xrange(len(valid)/2):
        #     if valid[i] != valid[-1*(i+1)]:
        #         return False
        # return True

string = "A man, a plan, a canal: Panama"
solution = Solution()
result = solution.isPalindrome(string)
print(bool(result))