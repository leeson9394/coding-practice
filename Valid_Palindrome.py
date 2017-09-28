# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/?tab=Description

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valids = []
        for character in s:
            if character.isalpha() or character.isdigit():
                valids.append(character)
        word=''.join(valids)
        print word
        # for i in xrange(len(word)/2):
        #     if word[i] != word[-1*(i+1)]:
        #         return False
        # return True
        start=0
        end=len(word)-1
        while start < end:
            if word[start].lower() != word[end].lower():
                return False
            start+=1
            end-=1
        return True
a=Solution()
print a.isPalindrome("A man, a plan, a canal: Panama")