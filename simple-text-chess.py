"""
Important note about tuples:
Tuples represent the indicies of spaces on the board with one caveat: the format
for the tuples is (x, y), while the format for the board is board[y][x].

Eg: (2, 6) and board[6][2]; represent the same space
"""
# The number of spaces one side of the board is (only supports squares)
# Eg: A chess board is 8x8, so BOARD_SIZE = 8 for a typical board
# TODO: make it so I can make the board bigger by increasing board size; by creating
# 'row_n' variables and making them have BOARD_SIZE number of items.
BOARD_SIZE = 8

# The maximum and minimum indices that correspond to the spaces 
index_min = 0
index_max = BOARD_SIZE - 1

# The captured pieces (overwritten by pieces moving onto the space they're on)
captured_pieces = []

# A list of all the valid moves. Goes on a turn by turn basis. Gets cleared
# after every move
valid_moves = []

row_0 = ["r", "n", "b", "q", "k", "b", "n", "r"]
row_1 = ["p", "p", "p", "p", "p", "p", "p", "p"]
row_2 = [" ", " ", " ", " ", " ", " ", " ", " "]
row_3 = [" ", " ", " ", " ", " ", " ", " ", " "]
row_4 = [" ", " ", " ", " ", " ", " ", " ", " "]
row_5 = [" ", " ", " ", " ", " ", " ", " ", " "]
row_6 = ["P", "P", "P", "P", "P", "P", "P", "P"]
row_7 = ["R", "N", "B", "Q", "K", "B", "N", "R"]

board = [row_0, row_1, row_2, row_3, row_4, row_5, row_6, row_7]

# This function prints out the board, with a new line between each row. 
# White pieces are represented using captial letters. Black is with lowercase. 
# The board can easily be flipped to show black's pieces at the bottom using the 
# reverse method on 'board'.
def display_board():
    print("- - - - - - - - - - - - - - - - - - - -")
    for row in board:
        print(str(row))
        if (board[index_max] != row):
            print("")
    print("- - - - - - - - - - - - - - - - - - - -")

# This function takes two tuples representing the x and y coordinates of the start
# and end spots. It moves a piece from whatever the piece is right now (parameter 1)
# to another space (parameter 2). If there is a piece on the ending spot (parameter 2),
# then the piece will 'capture' it by overwriting it. It is added to a list to keep
# track of captured pieces
def move_piece(start_spot, end_spot):
    if board[start_spot[1]][start_spot[0]] == " ":
        print("Error: No piece to move")
        return
    # Checks if the end spot has a piece on it, is so, adds the piece to a 'captured' list
    if board[end_spot[1]][end_spot[0]] != " ":
        captured_pieces.append(board[end_spot[1]][end_spot[0]])
    # Copies the piece from start spot to end spot
    board[end_spot[1]][end_spot[0]] = board[start_spot[1]][start_spot[0]]
    # Makes the start spot have no piece in it
    board[start_spot[1]][start_spot[0]] = " "

# This function gets all valid rook moves, with a tuple representing the rooks' location as input
# It puts them in the valid moves list
def get_rook_moves(start_spot):
    # Offset the spot by the direction moves are being checked to not have start move as a valid move
    # Decreasing in x values (going left)
    x_val = start_spot[0] - 1
    y_val = start_spot[1]
    while x_val >= index_min and x_val <= index_max:
        valid_moves.append((x_val, y_val))
        if board[y_val][x_val] != " ":
            break
        x_val -= 1
    # Increasing in x values (going right)
    x_val = start_spot[0] + 1
    while x_val >= index_min and x_val <= index_max:
        valid_moves.append((x_val, y_val))
        if board[y_val][x_val] != " ":
            break
        x_val += 1
    # Decreasing in y values (going up)
    # Need to reset x_val back to its default value
    x_val = start_spot[0]
    y_val = start_spot[1] - 1
    while y_val >= 0 and y_val <= 7:
        valid_moves.append((x_val, y_val))
        if board[y_val][x_val] != " ":
            break
        y_val -= 1
    # Increasing in y values (going down)
    y_val = start_spot[1] + 1
    while y_val >= 0 and y_val <= 7:
        valid_moves.append((x_val, y_val))
        if board[y_val][x_val] != " ":
            break
        y_val += 1

