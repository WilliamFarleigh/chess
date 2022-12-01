from enum import Enum
class Variables(Enum):
    # The number of spaces one side of the board is (only supports squares)
    # Eg: A chess board is 8x8, so BOARD_SIZE = 8 for a typical board
    BOARD_SIZE = 8
    # The maximum and minimum indices that correspond to the spaces 
    index_min = 0
    index_max = BOARD_SIZE - 1