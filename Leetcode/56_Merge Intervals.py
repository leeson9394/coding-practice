# 56. Merge Intervals
#https://leetcode.com/problems/merge-intervals/discuss/

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

class Solution(object):

    def merge(self, intervals):
        sorted_arr = sorted(intervals)
        res = []
        for i in range(0, len(sorted_arr)):
            if sorted_arr[i][1] > sorted_arr[i+1][0]:
                start = min(sorted_arr[i][0],sorted_arr[i+1][0])
                end = max(sorted_arr[i][1],sorted_arr[i+1][1])
                sorted_arr.pop(i)
                sorted_arr.pop(i+1)
                sorted_arr.insert(i,[start,end])
            res.append(sorted_arr[i])
        return res
                
    
        



arr = [[1,3],[2,5],[8,10],[15,18]]
solu=Solution()
print(solu.merge(arr))

# a=[2,8]
# b=[2,6]

# start = min((a[0],b[0]))
# end = max(a[1],b[1])
# print([start, end])
