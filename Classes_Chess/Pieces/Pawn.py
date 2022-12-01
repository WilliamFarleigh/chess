from ChessPiece import *
from variables import *

from Pieces.BoardSpace import *
from Pieces.Queen import *
from Pieces.Rook import *
from Pieces.Knight import *
from Pieces.Bishop import *

BOARD_SIZE = Variables.BOARD_SIZE.value
index_min = Variables.index_min.value
index_max = Variables.index_max.value


input_to_piece = {"queen":Queen, "rook":Rook, "bishop":Bishop, "knight":Knight}
class Pawn(HasMovedPiece):
    def __init__(self, piece_color):
        super().__init__(Piece.PAWN, piece_color)

#changes to any piece
    def tell_if_at_last_line(self, chess_board, spot):
        x_val, y_val = spot
        if y_val == 7 or y_val == 0:
            while(True):
                piece = input("What piece would you like? ")
                if piece.lower() in input_to_piece:
                    chess_board.board[y_val][x_val] = input_to_piece[piece.lower()](self.piece_color)
                    return
                print("That is not a valid piece. eg: queen")
    def get_valid_take_moves(self, chess_board, start_spot, piece_color):
        if self.piece_color == piece_color:
            return []
        movement = self.__get_piece_movement_based_on_color(chess_board.get_piece(start_spot))
        valid_moves = self.__get_attackable_spaces_two(chess_board, start_spot[0], start_spot[1], [], movement)
        return valid_moves
    #gets moves            
    def get_moves(chess_board, start_spot):
        x_val, y_val = start_spot
        board = chess_board.board
        piece = chess_board.board[y_val][x_val]
        valid_moves = []
        movement = piece.__get_piece_movement_based_on_color(piece)
        y_val += movement
        valid_moves = piece.__get_attackable_spaces_one(chess_board, x_val, y_val, valid_moves, movement)
        valid_moves = piece.__get_forward_two_spots(piece, valid_moves, chess_board, x_val, y_val, movement)
        return valid_moves
    def __get_piece_movement_based_on_color(self, piece):         
        if piece.piece_color == PieceColor.WHITE:
            return -1 
        else:
            return 1
        return 0
            
    def __get_forward_two_spots(self, piece, valid_moves, chess_board, x_val, y_val, movement):
        if type(chess_board.get_piece((x_val, y_val))) == BoardSpace:
            if y_val >= chess_board.index_min and y_val <= chess_board.index_max:
                valid_moves.append((x_val, y_val))
                if not piece.has_moved:
                    if type(chess_board.get_piece((x_val, y_val + 1*movement))) == BoardSpace:
                        valid_moves.append((x_val, y_val + 1*movement))
        return valid_moves
    
    def __get_attackable_spaces_one(self, chess_board, x_val, y_val, valid_moves, movement):
            y_val += movement
            # Checking if a pawn can capture (diagonally from start spot)
            x_val += 1
            if type(x_val >= chess_board.index_min and  x_val <= chess_board.index_max and chess_board.board[y_val][x_val]) != BoardSpace:
                valid_moves.append((x_val, y_val))
                    
            # Because went 1 to the side from start spot, so to go 1 from the other side (relative to start spot), subtract 2
            x_val -= 2
            if type(x_val >= chess_board.index_min and  x_val <= chess_board.index_max and chess_board.board[y_val][x_val]) != BoardSpace:
                valid_moves.append((x_val, y_val))
            return valid_moves 

    def __get_attackable_spaces_two(self, chess_board, x_val, y_val, valid_moves, movement):
            y_val += movement
            # Checking if a pawn can capture (diagonally from start spot)
            x_val += 1
            if (x_val >= chess_board.index_min and x_val <= chess_board.index_max):
                valid_moves.append((x_val, y_val))
                    
            # Because went 1 to the side from start spot, so to go 1 from the other side (relative to start spot), subtract 2
            x_val -= 2
            if (x_val >= chess_board.index_min and x_val <= chess_board.index_max):
                valid_moves.append((x_val, y_val))
            return valid_moves 
            
Pawn.get_moves = staticmethod(Pawn.get_moves)