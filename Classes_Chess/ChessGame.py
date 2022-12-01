from ChessBoard import *
from ChessDisplay import *
# builds the board 
# can build any type of 8x8 board with any amount of pieces
row_0 = ["black_rook", "black_knight", "black_bishop", "black_king", "black_queen", "black_bishop", "black_knight", "black_rook"]
row_1 = ["black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn"]
row_2 = [" ", " ", " ", " ", " ", " ", " ", " "]
row_3 = [" ", " ", " ", " ", " ", " ", " ", " "]
row_4 = [" ", " ", " ", " ", " ", " ", " ", " "]
row_5 = [" ", " ", " ", " ", " ", " ", " ", " "]
row_6 = ["white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn"]
row_7 = ["white_rook", "white_knight", "white_bishop", "white_king", "white_queen", "white_bishop", "white_knight", "white_rook"]

board = [row_0, row_1, row_2, row_3, row_4, row_5, row_6, row_7]

#tester
'''
CURRENTLY WORKING PIECES
ROOK (w out castling), PAWN (w out en pessant), BISHOP, KNIGHT, QUEEN
'''
chess_board = ChessBoard(board);
chess_display = ChessTextDisplay(chess_board);
while True:
    print(chess_display.get_display_board())
    chess_display.request_player_input()