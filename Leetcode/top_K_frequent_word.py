# # Leetcode 692
import collections

# solution 1 from me, not working on alphabet orders.
class Solution(object):
    def topKFrequent(self,words,k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hashmap = {}
        for item in words:
            if item in hashmap:
                hashmap[item] += 1
            else:
                hashmap[item] = 1
        
        print("before sort:", hashmap.items())
        res = sorted( hashmap.items(), key = lambda x: (-x[1], x[0]) )
        print("after sort:", res)
        res = [tup[0] for tup in res]
        return res[:k]

# solution 2 from online

# class Solution(object):
#     def topKFrequent(self, words, k):
#         """
#         :type words: List[str]
#         :type k: int
#         :rtype: List[str]
#         """
#         count = collections.Counter(words)
#         res = sorted(count.items(), key = lambda x: (-x[1], x[0]))
#         res = [tup[0] for tup in res]
#         return res[:k]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

sol = Solution()
res = sol.topKFrequent(words, k)
print(res)
