# 825. https://leetcode.com/problems/friends-of-appropriate-ages/

import collections

class Solution(object):
    # # soluton 1
    # def numFriendRequests(self, ages):
    #     """
    #     :type ages: List[int]
    #     :rtype: int
    #     """
    #     count = collections.Counter(ages)
    #     ages = sorted(count.keys())
    #     print(ages)
    #     N = len(ages)
    #     res = 0
    #     for A in ages:
    #         for B in range(int(0.5 * A) + 7 + 1, A + 1): # friend age requirement 0.5 * A + 7 < B <= A.
    #             res += count[A] * (count[B] - int(A == B))
    #     return res

    # # solution 2
    def numFriendRequests(self, ages):
        cnt = collections.Counter(ages)
        ans = 0
        for ageA in ages:
            cnt[ageA] -= 1 # take out A iteself 
            left, right = int(0.5 * ageA) + 7, ageA
            for ageB in range(left + 1, right + 1):
                ans += cnt[ageB]
            cnt[ageA] += 1 # put A back
        return ans

    # solution 3
    # def numFriendRequests(self, ages):
    #     ages_count = [0] * 121
    #     for age in ages:
    #         ages_count[age] += 1
    #     result = 0
    #     # print(ages_count)
    #     for age in ages:
    #         lower_bound = 0.5 * age + 7
    #         upper_bound = age + 1 if age >= 100 else min(age + 1, 101)
    #         result += sum(ages_count[int(lower_bound+1): upper_bound])
    #         print(int(lower_bound+1), upper_bound)
    #         if ages_count[age] > 0 and int(lower_bound+1) <= age < upper_bound:
    #             result -= 1
    #     return result

ages = [108,115,5,24,82] 
s = Solution()
res = s.numFriendRequests(ages)
print(res)

# if __name__ == '__main__':
#     print(numFriendRequests([108,115,5,24,82]))


