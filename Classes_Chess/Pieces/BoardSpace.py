from ChessPiece import *

class BoardSpace(ChessPiece):
    def __init__(self):
        super().__init__(Piece.NONE, PieceColor.NONE)
    def __str__(self):
        return " "