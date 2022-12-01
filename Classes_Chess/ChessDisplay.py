from ChessBoard import *
from Util import *

input_player_msg = "$ "

spaces_size_for_distance_between_letters = "   "
board_end = "- - - - - - - - - - - - - - - - -";

amt_of = "{1}"
letter = r"[A-H]" + amt_of
number = "[1-" + str(BOARD_SIZE) + "]" + amt_of
middle = "\s?-?"
pattern_of_moving = re.compile(letter + number + middle + letter + number, re.IGNORECASE)
pattern_of_place_to_move = re.compile(letter + number, re.IGNORECASE)

translate_pieces_from_letters_to_names = {'r':"black_rook",
    'n':"black_knight", 'b':"black_bishop", 'q':"black_queen", 
    'k':"black_king", 'p':"black_pawn", 'P':"white_pawn", 
    "N":"white_knight",'B':"white_bishop", "K":"white_king", 
    'Q':"white_queen", 'R':"white_rook", " ":" ", "x":"x"}
#flips the dictionary, creates a second dictionary
translate_pieces_from_names_to_letters = {}
for key in translate_pieces_from_letters_to_names:
    translate_pieces_from_names_to_letters[translate_pieces_from_letters_to_names[key]] = key


class ChessTextDisplay:
#   CONSTRUCTOR    
#------------------------------------------------------------------
    def __init__(self, chess_board):
        if Util.is_right_type(chess_board, ChessBoard):
            self.chess_board = chess_board
#   METHODS
#------------------------------------------------------------------
    def request_player_input(self):
        global pattern_of_moving, input_player_msg, middle
        input_of_player = input(input_player_msg)
        size_of_input = 0
        x_loc = []
        y_loc = []
        if pattern_of_moving.match(input_of_player):
            #try:
            # debugger
            if True:
                for char in input_of_player:
                    if (re.compile("[a-zA-Z0-9]").match(char)):
                        char = char.upper()
                        if char in location_x_dictionary:
                            x_loc.append(location_x_dictionary[char])
                        else:
                            y_loc.append(8 - ((int(char))))
                        # need to change this to checking what it is, and if it can move there
                if change_piece_from_boolean[self.chess_board.is_white_turn] == self.chess_board.board[y_loc[0]][x_loc[0]].piece_color:
                    
                    self.chess_board.move_piece((x_loc[0], y_loc[0]), (x_loc[1], y_loc[1]))
                else:
                    print("It is not " + self.chess_board.board[y_loc[0]][x_loc[0]].piece_color.value +"'s turn!")
            #except:
                #self.call_invalid_message()
        elif pattern_of_place_to_move.match(input_of_player):
            x_loc_num = 0
            y_loc_num = 0
            for char in input_of_player:
                char = char.upper()
                if char in location_x_dictionary:
                    x_loc_num = location_x_dictionary[char]
                else:
                    y_loc_num = Variables.BOARD_SIZE.value - ((int(char)))
            display = self.display_board_with_tuple((x_loc_num, y_loc_num))
            if not display is None:
                print(display)
            self.request_player_input()

        else:
            self.call_invalid_message()
#------------------------------------------------------------------
    # displays board. is a wrapper for the 
    # return_board_display class method         
    def get_display_board(self):
        return self.return_board_display(self.chess_board.board)

#------------------------------------------------------------------        
        
    # displays the board, but with locations 
    # that the provided location can move to
    # Params are self and location
    def display_board_with_tuple(self, tuple_of_loc):
        x_loc, y_loc = tuple_of_loc
        board = []
        
        for i, row in enumerate(self.chess_board.board):
            new_row = []
            for j, loc in enumerate(row):
                new_row.append(str(loc))
            board.append(new_row)
        locations = self.chess_board.board[y_loc][x_loc].get_moves(self.chess_board, tuple_of_loc)
        locations = self.chess_board.remove_friendly_fire(locations, tuple_of_loc)
        for loc in locations:
            x_location =  loc[0]
            y_location = loc[1]
            board[y_location][x_location] = "x"
        return self.return_board_display(board)
        
 #------------------------------------------------------------------
        
    def return_board_display(self, board):
        msg = ""
        msg = msg + board_end
        row_num = BOARD_SIZE + 1
        for row in board:
            row_num -= 1
            string_row = "|"
            is_first = True
            for location in row:
                if is_first:
                    is_first = False
                    string_row = string_row + " " + translate_pieces_from_names_to_letters[str(location)]
                else:
                    string_row = string_row + " | " + translate_pieces_from_names_to_letters[str(location)] + ""
            string_row = string_row + " | " + str(row_num)
            msg = msg + "\n" + string_row
            if (board[index_max] != row):
                msg = msg + "\n" + board_end
        msg = msg + "\n" + board_end
        return (msg + "\n" + "  " + "a" + spaces_size_for_distance_between_letters + "b" 
        + spaces_size_for_distance_between_letters + "c" + spaces_size_for_distance_between_letters 
        + "d" + spaces_size_for_distance_between_letters +  "e" + spaces_size_for_distance_between_letters 
        + "f" + spaces_size_for_distance_between_letters +   "g" + spaces_size_for_distance_between_letters 
        + "h")
    
#------------------------------------------------------------------

    def call_invalid_message(self):
        print(invalid_message_error)
        self.request_player_input()
#------------------------------------------------------------------