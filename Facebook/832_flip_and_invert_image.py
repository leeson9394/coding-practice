# Leetcode 832

# 1 1 0         0 1 1           1 0 0
# 1 0 1    ->   1 0 1   ->      0 1 0
# 0 0 0         0 0 0           1 1 1

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        A = self.horizontal_flip(A, row, col)
        A = self.invert_image(A, row, col)
        return A


    def horizontal_flip(self, A, row, col):
        for i in range(0, row):
            # A[i] = A[i][::-1]
            A[i].reverse()
        print(A)
        return A
    
    def invert_image(self, A, row, col):
        for i in range(0, row):
            for j in range(0, col):
                A[i][j] ^= 1
        return A

# class Solution(object):
#     def flipAndInvertImage(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         row = len(A)
#         col = len(A[0])
#         for i in range(0, row):
#             A[i] = A[i][::-1]
#         print(A)

#         for i in range(0, row):
#             for j in range(0, col):
#                 if A[i][j] == 1:
#                     A[i][j] = 0
#                 else:
#                     A[i][j] = 1
#         print(A)
#         return A

A = [[1,1,0],[1,0,1],[0,0,0]]
sol = Solution()
sol.flipAndInvertImage(A)