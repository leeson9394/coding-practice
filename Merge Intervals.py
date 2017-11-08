# 56. Merge Intervals
#https://leetcode.com/problems/merge-intervals/discuss/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for element in intervals:
            if len(res) == 0 or res[-1].end < element.start:
                res.append(element)
            else:
                res[-1].end = max(res[-1].end, element.end)
        return res


arr = [[1,3],[2,6],[8,10],[15,18]]
a=Solution()
print a.merge(arr)
