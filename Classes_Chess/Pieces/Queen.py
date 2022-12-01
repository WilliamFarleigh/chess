from ChessPiece import *
from Pieces.BoardSpace import *
from Pieces.Rook import *
from Pieces.Bishop import *
class Queen(ChessPiece):
    def __init__(self, piece_color):
        super().__init__(Piece.QUEEN, piece_color)
    def get_moves(chess_board, start_spot):
        valid_moves_rook = Rook.get_moves(chess_board, start_spot)
        valid_moves_bishop = Bishop.get_moves(chess_board, start_spot)
        valid_moves = []
        for i in valid_moves_rook:
            valid_moves.append(i)
        for i in valid_moves_bishop:
            valid_moves.append(i)
        return valid_moves
Queen.get_moves = staticmethod(Queen.get_moves)