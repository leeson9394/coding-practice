# 529. https://leetcode.com/problems/minesweeper/

from typing import List
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        (row, col) = click 
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                n = sum([board[row + r][col + c] == 'M' for r, c in directions if 0 <= row + r < len(board) and 0 <= col +c < len(board[0])])
                board[row][col] = str(n if n else 'B')
                if not n:
                    for r, c in directions:
                        self.updateBoard(board, [row + r, col + c])
        return board

# class Solution(object):

#     def updateBoard(self, board, click):
#         x = click[0]
#         y = click[1]
#         if board[x][y] == 'M':
#             board[x][y] = 'X'
#         else:
#             self.dfs(board, x, y)
#         return board

#     def dfs(self, board, x, y):
#         m = len(board)
#         n = len(board[0])
#         dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

#         if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != "E":
#             return
        
#         num = self.num_of_bombs(board, x, y) # check num of bomb adjacent to the (x,y)

#         # 1. no adjacent mine
#         if num == 0:
#             board[x][y] == "B"
#             for dir in dirs:
#                 new_x = dir[0] + x
#                 new_y = dir[1] + y
#                 self.dfs(board, new_x, new_y)
#         # 2. Find at least one mine
#         else:
#             board[x][y] = str(num + 0)

#     def num_of_bombs(self, board, x, y):
#         num = 0
#         m = len(board)
#         n = len(board[0])
#         dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

#         for dir in dirs:
#             new_x = dir[0] + x
#             new_y = dir[1] + y
#             if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
#                 continue
#             if board[new_x][new_y] == "M" or board[new_x][new_y] == "X": # found hidden bomb or marked bomb
#                 num += 1
#         return num



board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3, 0]
s = Solution()
res = s.updateBoard(board, click)
print(res)