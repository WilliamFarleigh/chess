from ChessPiece import *

class Knight(ChessPiece):
    def __init__(self, piece_color):
        super().__init__(Piece.KNIGHT, piece_color)
    def get_moves(chess_board, start_spot):
        index_min = chess_board.index_min
        index_max = chess_board.index_max
        BOARD_SIZE = chess_board.BOARD_SIZE
        valid_moves = []
        # All knight moves can be represented with (+/- 1, +/- 2) and (+/- 2, +/- 1) relative to the start spot
        # (+/-1, +/-2)
        # Decreasing in x by 1, decreasing in y by 2
        x_val = start_spot[0] - 1
        y_val = start_spot[1] - 2
        if x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
        # Increasing in x by 1, decreasing in y by 2
        x_val = start_spot[0] + 1
        y_val = start_spot[1] - 2
        if x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
        # Decreasing in x by 1, increasing in y by 2
        x_val = start_spot[0] - 1
        y_val = start_spot[1] + 2
        if x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
        # Increasing in x by 1, increasing in y by 2
        x_val = start_spot[0] + 1
        y_val = start_spot[1] + 2
        if x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
        
        # (+/-2, +/-1)
        # Decreasing in x by 2, decreasing in y by 1
        x_val = start_spot[0] - 2
        y_val = start_spot[1] - 1
        if x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
        # Increasing in x by 2, decreasing in y by 1
        x_val = start_spot[0] + 2
        y_val = start_spot[1] - 1
        if x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
        # Decreasing in x by 2, increasing in y by 1
        x_val = start_spot[0] - 2
        y_val = start_spot[1] + 1
        if x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
        # Increasing in x by 2, increasing in y by 1
        x_val = start_spot[0] + 2
        y_val = start_spot[1] + 1
        if x_val >= index_min and x_val <= index_max and y_val >= index_min and y_val <= index_max:
            valid_moves.append((x_val, y_val))
        return valid_moves
Knight.get_moves = staticmethod(Knight.get_moves)