from enum import Enum
from Util import *
from variables import Variables
class PieceColor(Enum):
    BLACK = "black"
    WHITE = "white"
    NONE = "none"

class Piece(Enum):
    KING = "king"
    QUEEN = "queen"
    BISHOP = "bishop"
    ROOK = "rook"
    KNIGHT = "knight"
    PAWN = "pawn"
    NONE =  "none"

'''

ALL CLASSES DEFINED BELOW THIS MESSAGE ARE ABSTRACT CLASSES, 
DO NOT USE THEM DIRECTLY TO MAKE A OBJECT PLS AND TY

IF YOU DO YOU ARE FREAKING CRAZY

idk how to make abstract classes in python ¯\_(ツ)_/¯

'''

class ChessPiece:
    def __init__(self, piece, piece_color):
        if Util.is_right_type(piece, Piece) and Util.is_right_type(piece_color, PieceColor):
            self.piece = piece
            self.piece_color = piece_color
    def __str__(self):
        return f"{self.piece_color.value}_{self.piece.value}"
    def get_moves(chess_board, start_spot):
        return []
    def get_valid_take_moves(self, chess_board, start_spot, piece_color):
        if self.piece_color == piece_color:
            return []
        valid_moves = self.get_moves(chess_board, start_spot)
        return valid_moves
    def tell_if_at_last_line(self, chess_board, spot):
        pass
    def tell_moved(self):
        pass
    def get_has_moved(self):
        return True

class HasMovedPiece(ChessPiece):
    def __init__(self, piece, piece_color):
        super().__init__(piece, piece_color)
        self.has_moved = False
    def get_tell_moved():
        return self.has_moved
    def tell_moved(self):
        self.has_moved = True
# GETTERS
    def get_color(self):
        return self.piece_color
        
    def get_piece(self):
        return self.piece
        
    def get_has_moved(self):
        return self.has_moved
        
ChessPiece.get_moves = staticmethod(ChessPiece.get_moves)