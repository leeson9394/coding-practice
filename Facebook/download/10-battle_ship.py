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