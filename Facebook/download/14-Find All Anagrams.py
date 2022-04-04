# 438. https://leetcode.com/problems/find-all-anagrams-in-a-string/

# def findAnagrams(s, p):
#     p_dict = {}
#     for c in p:
#         if c in p_dict:
#             p_dict[c] += 1
#         else:
#             p_dict[c] = 1

#     if len(s) < len(p):
#         return []
#     s_dict = {}
#     for c in s[:len(p)]:
#         if c in s_dict:
#             s_dict[c] += 1
#         else:
#             s_dict[c] = 1

#     result = []
#     if s_dict == p_dict:
#         result.append(0)
#     for i in range(len(p), len(s)):
#         if s_dict[s[i-len(p)]] == 1:
#             s_dict.pop(s[i-len(p)])
#         else:
#             s_dict[s[i-len(p)]] -= 1
#         if s[i] in s_dict:
#             s_dict[s[i]] += 1
#         else:
#             s_dict[s[i]] = 1
#         if s_dict == p_dict:
#             result.append(i - len(p) + 1)
#     return result


# if __name__ == '__main__':
#     print(findAnagrams("abab", "ab"))

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        answer = []
        s_length, p_length = len(s), len(p)
        if s_length < p_length:
            return answer
        p_counter = Counter(p) # dict counter of p string 
        s_counter = Counter(s[:p_length-1]) # dict counter of s string of beginning to len(p) - 1 
        index = 0
        for index in range(0, s_length - (p_length - 1)): # sliding window start index from beginning to s_length - (p_length - 1)
                s_counter[s[index + (p_length - 1)]] += 1 # add new element to the s count
                if s_counter == p_counter:
                    answer.append(index) # add the start index to the answer
                s_counter[s[index]] -= 1 # remove current index count
                if s_counter[s[index]] == 0: # if count drop to 0, then delete it from dict
                    del s_counter[s[index]] 
        return answer
