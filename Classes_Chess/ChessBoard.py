import re

# local, util

from Util import *

#variables import
from variables import *

# chessPiece import

from ChessPiece import *

# all the pieces imported here

from Pieces.BoardSpace import *
from Pieces.Knight import *
from Pieces.King import *
from Pieces.Pawn import *
from Pieces.Bishop import *
from Pieces.Queen import *
from Pieces.Rook import *

'''
modifiable variables
'''


invalid_message_error = "Invalid input, please enter another move (eg: b1c3)" 

'''
unmodifiable variables
'''

BOARD_SIZE = Variables.BOARD_SIZE.value
# The maximum and minimum indices that correspond to the spaces 
index_min = Variables.index_min.value
index_max = Variables.index_max.value



location_x_dictionary = {"A":0, "B":1, 
"C":2, "D":3, "E":4, "F":5, "G":6,"H":7}

change_piece_from_boolean = {True:PieceColor.WHITE, False:PieceColor.BLACK}


class ChessBoard:
#    CONSTRUCTOR

#---------------------------------------------------------------------
    def __init__(self, board):
        if Util.is_right_type(board, list):
            #fields
            self.board = []
            self.is_white_turn = True
            self.captured_pieces = []
            self.BOARD_SIZE = BOARD_SIZE
            self.index_min = index_min
            self.index_max = index_max
            for row in board:
                new_row = []
                for piece_name in row:
                    new_row.append(generate_new_piece_using_string(piece_name))
                self.board.append(new_row)
#METHODS
#---------------------------------------------------------------------            

    # removes friendly fire from a list of valid_moves 
    #(the list), and generates from the location
    def remove_friendly_fire(self, valid_moves, loc):
        piece = self.board[loc[1]][loc[0]]
        new_valid_moves = []
        for move in valid_moves:
            if move[0] <= Variables.index_max.value and move[0] >= Variables.index_min.value and piece.piece_color != self.board[move[1]][move[0]].piece_color:
                new_valid_moves.append(move)
        return new_valid_moves

#---------------------------------------------------------------------    

    # This function takes two tuples representing the x and y coordinates of the start
    # and end spots. It moves a piece from whatever the piece is right now (parameter 1)
    # to another space (parameter 2). If there is a piece on the ending spot (parameter 2),
    # then the piece will 'capture' it by overwriting it. It is added to a list to keep
    # track of captured pieces
    def move_piece(self, start_spot, end_spot):
        global translate_pieces
        # This is to detect checks it is very ineffient
        if self.detect_if_in_check(self.get_piece(start_spot)):
            return
        if type(self.board[start_spot[1]][start_spot[0]]) == BoardSpace:
            print("Error: No piece to move")
            self.request_player_input()
            return
        #gets all of the possible moves for this piece
        moves_list = self.board[start_spot[1]][start_spot[0]].get_moves(self, start_spot)
        moves_list = self.remove_friendly_fire(moves_list, start_spot)
        if not end_spot in moves_list:
            print(str(self.board[start_spot[1]][start_spot[0]]) + " cannot move there.")
            return
        # Checks if the end spot has a piece on it, is so, adds the piece to a 'captured' list
        if self.board[end_spot[1]][end_spot[0]] != " ":
            self.captured_pieces.append(self.board[end_spot[1]][end_spot[0]])
        # Copies the piece from start spot to end spot
        self.board[end_spot[1]][end_spot[0]] = self.board[start_spot[1]][start_spot[0]]
        # Makes the start spot have no piece in it
        self.board[start_spot[1]][start_spot[0]] = BoardSpace()
        self.board[end_spot[1]][end_spot[0]].has_moved = True
        self.board[end_spot[1]][end_spot[0]].tell_if_at_last_line(self, end_spot)
        self.is_white_turn = not self.is_white_turn 
        self.detect_if_in_check(self.get_piece(start_spot))
#-------------------------------------------------------------------
    def detect_if_in_check(self, piece):
        needed_color = PieceColor.NONE
        if self.is_white_turn == True:
            needed_color = PieceColor.WHITE
        else:
            needed_color = PieceColor.BLACK 
        is_in_check = False
        for y, row in enumerate(self.board):
            for x, needed_piece in enumerate(row):
                if type(needed_piece) == King and needed_piece.get_color() == needed_color:
                    is_in_check = needed_piece.is_in_check(self, (x, y))
        if is_in_check and type(piece) != King:
            print("You are currently in check!")
            return True
        return False
#-------------------------------------------------------------------
    # GETTERS to make it easier
    def get_piece(self, location):
        return self.board[location[1]][location[0]]
    
    def get_is_white_turn(self):
        return self.is_white_turn
    
    def get_captured_pieces(self):
        return self.captured_pieces;
#---------------------------------------------------------------------
#END OF CLASS

#im lazy so made bad version
def generate_new_piece_using_string(piece_as_string):
    if Util.is_right_type(piece_as_string, str):
        if (piece_as_string == " " or piece_as_string == ""):
            return BoardSpace()
        color_and_piece = piece_as_string.split("_")
        color = color_and_piece[0]
        piece = color_and_piece[1]
        color_enum = PieceColor.NONE
        if color == "black":
            color_enum = PieceColor.BLACK
        elif color == "white":
            color_enum = PieceColor.WHITE
        else:
            return BoardSpace()
        if (piece == "king"):
            return King(color_enum)
        if (piece == "knight"):
            return Knight(color_enum)
        if (piece == "pawn"):
            return Pawn(color_enum)
        if (piece == "queen"):
            return Queen(color_enum)
        if (piece == "bishop"):
            return Bishop(color_enum)
        if (piece == "rook"):
            return Rook(color_enum)
        else:
            return BoardSpace()