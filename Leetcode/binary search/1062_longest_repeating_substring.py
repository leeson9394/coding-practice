# 1062. https://leetcode.com/problems/longest-duplicate-substring/

import re
res = [m.start() for m in re.finditer('test', 'test test test test')]
print(res)

# class Solution:
#     def longestDupSubstring(self, s: str) -> str:
        