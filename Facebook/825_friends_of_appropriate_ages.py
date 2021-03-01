# leetcode 825. Friends Of Appropriate Ages

import collections

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ## too slow in leetcode to submit
        # friend_count = 0
        # ages = sorted(ages, reverse= True)
        # for i in range(0, len(ages)):
        #     for j in range(i+1, len(ages)):
        #         if ages[j] <= 0.5 * ages[i] + 7:
        #             continue
        #         if ages[j] > ages[i]:
        #             continue
        #         if ages[j] > 100 and ages[i] < 100:
        #             continue
        #         if ages[j] == ages[i]:
        #             friend_count += 1
        #             print(ages[i], ages[j])
        #         friend_count += 1
        #         print(ages[i], ages[j])
                    
        # return friend_count
        
        # person A and B must fit in 0.5 * age[A] + 7 < age[B] <= age[A] to be friends
        res = 0
        count = collections.Counter(ages)
        print(count)
        ages = sorted(count.keys())
        for age_A in ages:
            for age_B in range(int(0.5 * age_A) + 7 + 1, age_A + 1):
                res += count[age_A] * (count[age_B] - int(age_A == age_B)) 
        return res

ages = [16,16,20,30,100,110,120]
sol = Solution()
res = sol.numFriendRequests(ages)
print(res)