# 1062. https://leetcode.com/problems/longest-duplicate-substring/

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        while l < r:
            mid = l + (r - l + 1) / 2
            if self.helper(s, mid, l):
                l = mid
            else:
                r = mid - 1
        return l
    
    def helper(self, s, mid, l):
        seen = set()
        for i in range(len(s)):
            j = i + l - 1
            sub = s[i, j + 1]
            if seen.contains(sub):
                return True
            seen.add(sub)
        return False