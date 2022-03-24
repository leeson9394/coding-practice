# 682. https://leetcode.com/problems/baseball-game/

from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        total_sum = 0
        for point in ops:
            if point == "C":
                res.pop(-1)
            elif point == "D":
                last_point = res[-1]
                res.append(last_point * 2)
            elif point == "+":
                last_point = res[-1] + res[-2]
                res.append(last_point)
            else:
                res.append(int(point))
        
        for item in res:
            total_sum = total_sum + item

        return total_sum

s = Solution()
arr = ["5","-2","4","C","D","9","+","+"]
res = s.calPoints(arr)
print(res)