# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:

# -1 if the board is not yet finished AND no one has won yet (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

def is_solved(board):
    # To check for wins, we will go through the each row, column and diagonal and find
    # the product of the numbers in the cells. 
    # A product of 1 means all 1s, a product of 8 means all 2s, otherwise it's a mixture
    row_products = [1] * 3
    col_products = [1] * 3
    diag_products = [1] * 2
    for i in range(3):
        diag_products[0] *= board[i][i]
        diag_products[1] *= board[i][2 - i]
        for j in range(3):
            row_products[i] *= board[i][j]
            col_products[i] *= board[j][i]
    
    products = row_products + col_products + diag_products
    
    # If 1 is in products then we have 1 * 1 * 1 all in a row -> 1 wins
    if 1 in products:
        return 1
    # If 8 is in products then we have 2 * 2 * 2 all in a row -> 2 wins
    if 8 in products:
        return 2
    
    # If code gets to here, no one has run so:
    # If 0 is in products then there is still a 0 on the board so the game hasn't finished
    if 0 in products:
        return -1
    
    # Otherwise a draw
    return 0
    
    
    