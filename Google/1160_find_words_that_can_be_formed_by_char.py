# 1160. https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # solution two
        res = 0
        for word in words:
            n = len(word)
            cnt = 0
            for i in word:
                # word  in the character i  the number of <= chars  in the character i  the number of 
                if word.count(i) <= chars.count(i):
                    cnt += 1
                else:
                    break
            # word  can be caused by chars  spell out 
            if cnt == n:
                res += cnt
        return res