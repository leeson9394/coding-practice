import random


class Solution:
    """
    DFS approach

    For each empty square, we count the mines in adjacent neighbors
        - If there is no mine, do the dfs for its empty neighnors
        - If there are mines, change to num of mines

    Stop the dfs when we are out of bound, or have found a mine
    """

    def updateBoard(self, board, click):
        m = len(board)
        n = len(board[0])

        MOVES = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}

        def inBound(r, c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r, c):
            if not inBound(r, c) or board[r][c] == 'M':
                return

            mines = 0

            for move in MOVES:
                new_r = r + move[0]
                new_c = c + move[1]
                if inBound(new_r, new_c):
                    if board[new_r][new_c] == 'M':
                        mines += 1

            if mines == 0:
                if board[r][c] == 'E':
                    board[r][c] = 'B'
                for move in MOVES:
                    new_r = r + move[0]
                    new_c = c + move[1]
                    if inBound(new_r, new_c) and board[new_r][new_c] == 'E':
                        dfs(new_r, new_c)
            else:
                if board[r][c] == 'E':
                    board[r][c] = str(mines)

        row, col = click[0], click[1]

        if board[row][col] == 'M':
            board[row][col] = 'X'
            dfs(0, 0)
        else:
            dfs(row, col)

        return board


def generate(m, n, p):
    board = []
    for i in range(m):
        new = []
        for j in range(n):
            new.append('E')
        board.append(new)
    # return board
    array = list(range(n*m))
    positions = random.sample(array, p)
    for pos in positions:
        board[pos // 3][pos % 3] = 'M'
    return board


if __name__ == '__main__':
    print(generate(2, 3, 1))
