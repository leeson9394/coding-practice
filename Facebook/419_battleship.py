# leetcode 419. Battleships in a Board
# https://leetcode.com/problems/battleships-in-a-board/

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row = len(board)
        col = len(board[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    if (i>=1 and board[i-1][j] == 'X') or (j>=1 and board[i][j-1] == 'X'):
                        continue
                    count += 1
        return count

board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

sol = Solution()
res = sol.countBattleships(board)
print(res)

# follow up: not only count the ship, also output ship coordinates
import collections

class Solution:
    def countBattleships(self, board) -> int:
        
        if not board or len(board) == 0 or len(board[0]) == 0:
            return 0
        
        cnt = 0
        self.ships = collections.defaultdict(list)
            
        for row in range(len(board)):
            for cell in range(len(board[0])):
                
                if board[row][cell] == 'X': 
                    cnt += 1
                    self.dfs(row,cell,cnt,board)
        
        print("Count ships: {}, coords: {}".format(cnt,list(self.ships.values())))
        return cnt

    def dfs(self,i,j,cnt,board):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '.':
            return
        
        self.ships[cnt].append((i,j))         
        board[i][j] = '.'
        self.dfs(i+1,j,cnt,board)
        self.dfs(i-1,j,cnt,board)
        self.dfs(i,j-1,cnt,board)
        self.dfs(i,j+1,cnt,board)
