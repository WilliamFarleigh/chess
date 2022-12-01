from ChessPiece import *
from Pieces.BoardSpace import *
class Bishop(ChessPiece):
    def __init__(self, piece_color):
        super().__init__(Piece.BISHOP, piece_color)
    def get_moves(chess_board, start_spot):
        board = chess_board.board
        index_min = chess_board.index_min
        index_max = chess_board.index_max
        BOARD_SIZE = chess_board.BOARD_SIZE
        valid_moves = []
        # Offset the spot by the direction moves are being checked to not count start spot as a valid move
        # Decreasing in x and y values (going top left) [North West]
        x_val = start_spot[0] - 1
        y_val = start_spot[1] - 1
        while x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
            if type(board[y_val][x_val]) != BoardSpace:
                break
            x_val -= 1
            y_val -= 1
    
        # Increasing in x values, decreasing in y values (going top right) [North East]
        x_val = start_spot[0] + 1
        y_val = start_spot[1] - 1
        while x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
            if type(board[y_val][x_val]) != BoardSpace:
                break
            x_val += 1
            y_val -= 1
        
        # Decreasing in x values, increasing in y values (going bottom left) [South West]
        x_val = start_spot[0] - 1
        y_val = start_spot[1] + 1
        while x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
            if type(board[y_val][x_val]) != BoardSpace:
                break
            x_val -= 1
            y_val += 1
        
        # Increasing in x and y values (going bottom right) [South East]
        x_val = start_spot[0] + 1
        y_val = start_spot[1] + 1
        while x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
            if type(board[y_val][x_val]) != BoardSpace:
                break
            x_val += 1
            y_val += 1
        return valid_moves
Bishop.get_moves = staticmethod(Bishop.get_moves)





#