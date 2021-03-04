# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_arr = sorted(intervals, key = lambda x: x[0]) # sort intervals
        res = [sorted_arr[0]] # put first interval into res

        for i in range(1, len(sorted_arr)):     # parse intervals from second interval
            if res[-1][1] >= sorted_arr[i][0]:  
                start = min(res[-1][0],sorted_arr[i][0])
                end = max(res[-1][1],sorted_arr[i][1])
                res[-1][0] = start
                res[-1][1] = end
            else:
                res.append(sorted_arr[i])
        return res

arr = [[2,6],[1,3],[8,10],[15,18]]
# arr = [[1,4],[0,2],[3,5]]

solu=Solution()
res = solu.merge(arr)
print(res)

# Answer from online
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """
#         N = len(intervals)
#         if not N: return []
#         intervals.sort(key = lambda x : x.start)
#         res = []
#         start = intervals[0].start
#         end = intervals[0].end
#         for it in intervals:
#             if it.start <= end:
#                 end = max(end, it.end)
#             else:
#                 cur = Interval(start, end)
#                 res.append(cur)
#                 start = it.start
#                 end = it.end
#         res.append(Interval(start, end))
#         return res


# arr = [[1,3],[2,6],[8,10],[15,18]]
# solu=Solution()
# intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
# print([[e.start, e.end] for e in solu.merge(intervals)])