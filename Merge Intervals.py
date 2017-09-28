# 56. Merge Intervals
#https://leetcode.com/problems/merge-intervals/discuss/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = [intervals[0]]

        for element in intervals:
            if res[-1][0] <= element[0] <= res[-1][1]:
                res[-1][1] = max(element[1], res[-1][1])
            else:
                res.append(element)
        return res


arr = [[1,3],[2,6],[8,10],[15,18]]
a=Solution()
print a.merge(arr)