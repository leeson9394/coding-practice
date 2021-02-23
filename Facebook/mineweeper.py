# generate x in length, y in width mineweeper, with n mines.

import random 

def generate_mineweeper(x, y, n):
    row = x
    col = y
    board = [ [0 for i in range(row)] for j in range(col) ]

    for i in range(n):              # put n mines in random place
        bomb_x = random.randrange(row)
        bomb_y = random.randrange(col)
        board[bomb_x][bomb_y] = "X"

    return board

mine_board = generate_mineweeper(10,10,5)
print(mine_board)

# followup: calculate the number of adjacent mines and put it on the board

# def adjacent_mine_calculator(board):