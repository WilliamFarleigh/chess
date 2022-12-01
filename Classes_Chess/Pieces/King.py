from ChessPiece import *
from Pieces.BoardSpace import *
# pieces
from Pieces.Knight import *
from Pieces.Pawn import *
from Pieces.Bishop import *
from Pieces.Queen import *
from Pieces.Rook import *


class King(HasMovedPiece):
    def __init__(self, piece_color):
        super().__init__(Piece.KING, piece_color)
    def get_moves(chess_board, start_spot):
        list_of_king_moves = generate_king_moves(chess_board, start_spot)
        return list_of_king_moves
    def is_in_check(self, chess_board, start_spot):
        if not (start_spot in generate_king_moves(chess_board, start_spot)):
            return True
        return False
        
def generate_king_moves(chess_board, start_spot):
    check_spaces = []
    piece = chess_board.get_piece(start_spot)
    # Generate a 3x3 of moves centered on king
    for i in range(3):
        for j in range(3):
            x_val = i+start_spot[0]-1
            y_val = j+start_spot[1]-1
            if x_val >= chess_board.index_min and x_val <= chess_board.index_max and y_val >= chess_board.index_min and y_val <= chess_board.index_max:
                check_spaces.append((x_val, y_val))
    # Castling
    if start_spot[0] == 3 and not piece.get_has_moved():  
        if  not chess_board.get_piece((start_spot[0] - 3, start_spot[1])).get_has_moved() and type(chess_board.get_piece((start_spot[0] - 2, start_spot[1]))) == BoardSpace:
            # x-val is start_spot - 2 
            check_spaces.append((start_spot[0] - 2, y_val-1)) # need to add a value after y_val to show that there is castling
        if  not chess_board.get_piece((start_spot[0] + 4, start_spot[1])).get_has_moved() and type(chess_board.get_piece((start_spot[0] + 2, start_spot[1]))) == BoardSpace:
            # x-val is start_spot + 3 
            check_spaces.append((start_spot[0] + 2, y_val-1)) # need to add a value after y_val to show that there is castling
    
    for y, row in enumerate(chess_board.board):
        for x, row_piece in enumerate(row):
            # if its not a king, or null go on
            if type(row_piece) != King and type(row_piece) != BoardSpace:
                piece_valid_moves = row_piece.get_valid_take_moves(chess_board, (x, y), piece.piece_color)
                for move in piece_valid_moves:
                    if move in check_spaces:
                        check_spaces.remove(move)
    # also need check detection--check if start spot is still a "valid move", if so remove and you know king isnt in check
    # if start spot isnt there anymore then king is in check; do whatever code
            
    return check_spaces
    
King.get_moves = staticmethod(King.get_moves)