class Solution:
    # @return an integer
    def romanToInt(self, s):
        numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        sum=0
        s=s[::-1] # Reverse string
        print s
        last=None
        for x in s:
            if last and numerals[x]<last:
                sum-=2*numerals[x]
            sum+=numerals[x]
            last=numerals[x]
        return sum
a=Solution()
print a.romanToInt("MC")

# def romantoint(str):
#     roman_dict={"L":50,"X":10,"V":5,"I":1}
#     sum=0
#     str=str[::-1]
#     last=None
#     for i in str:
#         if roman_dict[i] < last:
#             sum-=2*roman_dict[i]
#         sum+=roman_dict[i]
#         last=roman_dict[i]
#     return sum
#
# print romantoint("IV")