from ChessPiece import *
from variables import *
from Pieces.BoardSpace import *

class Rook(HasMovedPiece):
    def __init__(self, piece_color):
        super().__init__(Piece.ROOK, piece_color)
    def get_moves(chess_board, start_spot):
        board = chess_board.board
        index_min = chess_board.index_min
        index_max = chess_board.index_max
        BOARD_SIZE = chess_board.BOARD_SIZE
        valid_moves = []
        # Offset the spot by the direction moves are being checked to not have start move as a valid move
        # Decreasing in x values (going left) [West]
        x_val, y_val = start_spot
        x_val -= 1
        while x_val >= index_min and x_val <= index_max:
            valid_moves.append((x_val, y_val))
            if type(board[y_val][x_val]) != BoardSpace:
                break
            x_val -= 1
        # Increasing in x values (going right) [East]
        x_val, y_val = start_spot
        x_val += 1
        while x_val >= index_min and x_val <= index_max:
            valid_moves.append((x_val, y_val))
            if type(board[y_val][x_val]) != BoardSpace:
                break
            x_val += 1
        # Decreasing in y values (going up) [North]
        x_val, y_val = start_spot
        y_val -= 1
        while y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
            if type(board[y_val][x_val]) != BoardSpace:
                break
            y_val -= 1
        # Increasing in y values (going down) [South]
        x_val, y_val = start_spot
        y_val += 1
        while y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
            if type(board[y_val][x_val]) != BoardSpace:
                break
            y_val += 1
        return valid_moves
Rook.get_moves = staticmethod(Rook.get_moves)