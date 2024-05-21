# Author: Reid Singleton
# GitHub username: reidwarner
# Date: 5/20/2024
# Description: A program for playing atomic chess.

class ChessVar:
    """
    A class that allows two users to play Atomic Chess.
    """

    def __init__(self):
        self._game_state = 'UNFINISHED'
        self._player_turn = 'WHITE'
        self._pieces = []
        self._board = [
                       [None, None, None, None, None, None, None, None],                # Chess board notation row 8
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],              # Chess board notation row 1
                     ]

        self.initialize_board()

    def get_game_state(self):
        """
        Method that returns the current status of the game.
        """
        return self._game_state

    def make_move(self, move_from, move_to):
        """
        """
        # Get the piece object at the move_from square and check the inputs are valid
        square_start = self.translate_square(move_from)
        if not square_start[0]:
            print(square_start)
            return False
        square_end = self.translate_square(move_to)
        if not square_end[0]:
            return False
        piece = self._board[square_start[0]][square_start[1]]

        # Check if piece to be moved violates a player's turn
        if piece.get_color() != self._player_turn:
            return False

        # Get list of valid moves for the piece
        valid_moves = piece.get_valid_moves(self._board)

        # If the move_to square is in the list, make the move and return True
        if square_end in valid_moves:
            if self._board[square_end[0]][square_end[1]]:
                self._board[square_end[0]][square_end[1]].capture_piece()
            self._board[square_start[0]][square_start[1]] = None
            self._board[square_end[0]][square_end[1]] = piece
            return True
        else:
            return False



    def initialize_board(self):
        """Sets up the board for a new game."""

        # Initialize white pieces
        white_king = self._pieces.append(King('WHITE', self.translate_square('e1')))
        white_queen = self._pieces.append(Queen("WHITE", self.translate_square('d1')))
        white_rook_1 = self._pieces.append(Rook('WHITE', self.translate_square('a1')))
        white_rook_2 = self._pieces.append(Rook('WHITE', self.translate_square('h1')))
        white_knight_1 = self._pieces.append(Knight("WHITE", self.translate_square('b1')))
        white_knight_2 = self._pieces.append(Knight("WHITE", self.translate_square('g1')))
        white_bishop_1 = self._pieces.append(Bishop("WHITE", self.translate_square('c1')))
        white_bishop_2 = self._pieces.append(Bishop("WHITE", self.translate_square('f1')))
        white_pawn_1 = self._pieces.append(Pawn("WHITE", self.translate_square('a2')))
        white_pawn_2 = self._pieces.append(Pawn("WHITE", self.translate_square('b2')))
        white_pawn_3 = self._pieces.append(Pawn("WHITE", self.translate_square('c2')))
        white_pawn_4 = self._pieces.append(Pawn("WHITE", self.translate_square('d2')))
        white_pawn_5 = self._pieces.append(Pawn("WHITE", self.translate_square('e2')))
        white_pawn_6 = self._pieces.append(Pawn("WHITE", self.translate_square('f2')))
        white_pawn_7 = self._pieces.append(Pawn("WHITE", self.translate_square('g2')))
        white_pawn_8 = self._pieces.append(Pawn("WHITE", self.translate_square('h2')))

        # Initialize black pieces
        black_king = self._pieces.append(King('BLACK', self.translate_square('e8')))
        black_queen = self._pieces.append(Queen("BLACK", self.translate_square('d8')))
        black_rook_1 = self._pieces.append(Rook('BLACK', self.translate_square('a8')))
        black_rook_2 = self._pieces.append(Rook('BLACK', self.translate_square('h8')))
        black_knight_1 = self._pieces.append(Knight("BLACK", self.translate_square('b8')))
        black_knight_2 = self._pieces.append(Knight("BLACK", self.translate_square('g8')))
        black_bishop_1 = self._pieces.append(Bishop("BLACK", self.translate_square('c8')))
        black_bishop_2 = self._pieces.append(Bishop("BLACK", self.translate_square('f8')))
        black_pawn_1 = self._pieces.append(Pawn("BLACK", self.translate_square('a7')))
        black_pawn_2 = self._pieces.append(Pawn("BLACK", self.translate_square('b7')))
        black_pawn_3 = self._pieces.append(Pawn("BLACK", self.translate_square('c7')))
        black_pawn_4 = self._pieces.append(Pawn("BLACK", self.translate_square('d7')))
        black_pawn_5 = self._pieces.append(Pawn("BLACK", self.translate_square('e7')))
        black_pawn_6 = self._pieces.append(Pawn("BLACK", self.translate_square('f7')))
        black_pawn_7 = self._pieces.append(Pawn("BLACK", self.translate_square('g7')))
        black_pawn_8 = self._pieces.append(Pawn("BLACK", self.translate_square('h7')))

        # Add to board
        for piece in self._pieces:
            position = piece.get_position()
            self._board[position[0]][position[1]] = piece

    def print_board(self):
        """
        A class that prints the current board when called on a
        ChessVar object.
        """
        print('-------------------------------------------------------------------------------------------------')
        for row in self._board:
            print('|           |           |           |           |           |           |           |           |')
            for square in row:
                print('|', end='')
                if not square:
                    print('           ', end='')
                else:
                    color = square.get_color()
                    if len(square.get_piece_type()) == 4:
                        print('  ' + color[0] + ' ' + square.get_piece_type() + '   ', end='')
                    elif len(square.get_piece_type()) == 5:
                        print('  ' + color[0] + ' ' + square.get_piece_type() + '  ', end='')
                    else:
                        print('  ' + color[0] + ' ' + square.get_piece_type() + ' ', end='')
            print('|')
            print('|           |           |           |           |           |           |           |           |')
            print('-------------------------------------------------------------------------------------------------')

    def translate_square(self, square):
        """
        Takes in a square as a parameter in chess board algebraic notation. Returns
        a tuple of the square's address for use in a 2D python array.
        """
        row_dict = {'1': 7,
                    '2': 6,
                    '3': 5,
                    '4': 4,
                    '5': 3,
                    '6': 2,
                    '7': 1,
                    '8': 0
                    }

        col_dict = {'a': 0,
                    'b': 1,
                    'c': 2,
                    'd': 3,
                    'e': 4,
                    'f': 5,
                    'g': 6,
                    'h': 7,
                    }
        if square[0] not in col_dict or square[1] not in row_dict:
            return False, False
        else:
            return row_dict[square[1]], col_dict[square[0]]

    def is_square_open(self, square):
        """
        Takes in a square coordinates and returns True if the square is open
        or False if there is a piece on the square.
        """
        if self._board[square[0]][square[1]] == '':
            return True
        else:
            return False


class ChessPiece:
    """
    A class that represents the different types of chess pieces.
    """
    def __init__(self, color, position):
        self._color = color
        self._position = position
        self._captured = False
        self._piece_type = ''

    def get_color(self):
        """Returns the piece color."""
        return self._color

    def get_position(self):
        """Returns the piece position"""
        return self._position

    def set_position(self, square):
        """
        Takes in a square as a parameter and sets that piece's position
        to the new coordinates.
        """
        pass

    def capture_piece(self):
        """
        Changes a pieces captured status to captured.
        """
        self._captured = True
        return True

    def get_piece_type(self):
        """Returns the type of piece a piece object is."""
        return self._piece_type

class King(ChessPiece):
    """
    A class that represents a king chess piece. Inherits from
    the ChessPiece class. Can move one square in any direction.
    """
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self._piece_type = 'KING'
        self._king_moves = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 0), (-1, 1)]

    def get_valid_moves(self, board):
        """
        Takes the current board layout as input.
        Returns a list of all possible moves for the king on the board.
        """
        x_coord = self._position[1]
        y_coord = self._position[0]
        valid_moves = []

        for move in self._king_moves:
            new_x_coord = x_coord + move[1]
            new_y_coord = y_coord + move[0]
            is_valid = self.is_move_valid(board, new_x_coord, new_y_coord, self._color)
            if is_valid:
                valid_moves.append((new_y_coord, new_x_coord))
        print(valid_moves)
        return valid_moves

    def is_move_valid(self, board, new_x_coord, new_y_coord, color):
        """
        """
        if (new_x_coord < 0 or new_x_coord > 7) or (0 > new_y_coord or new_y_coord > 7):
            return False
        if board[new_y_coord][new_x_coord] and board[new_y_coord][new_x_coord].get_color() == color:
            return False
        else:
            return True




class Queen(ChessPiece):
    """
    A class that represents a Queen chess piece. Inherits from
    the ChessPiece class. Can move any amount of squares diagonally, vertically
    or horizontally.
    """
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self._piece_type = 'QUEEN'

    def is_move_valid(self, move):
        """
        Takes in the desired square to move to as a parameter.
        Returns true if the move is valid. Returns false if not valid.
        """
        current_position = self.get_position()

        if current_position == move:
            return False
        elif move[0] < 0 or move[0] > 7:
            return False
        elif move[1] < 0 or move[1] > 7:
            return False
        else:
            return True


class Rook(ChessPiece):
    """
    A class that represents a Rook chess piece. Inherits from
    the ChessPiece class. Can move any amount of squares vertically
    or horizontally.
    """
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self._piece_type = 'ROOK'

    def is_move_valid(self, move):
        """
        Takes in the desired square to move to as a parameter.
        Returns true if the move is valid. Returns false if not valid.
        """
        current_position = self.get_position()

        if current_position == move:
            return False
        elif move[0] < 0 or move[0] > 7:
            return False
        elif move[1] < 0 or move[1] > 7:
            return False
        elif current_position[0] - move[0] != 0 and current_position[1] - move[1] != 0:
            return False
        else:
            return True


class Bishop(ChessPiece):
    """
    A class that represents a Bishop chess piece. Inherits from
    the ChessPiece class. Can move any amount of squares diagonally.
    """
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self._piece_type = 'BISHOP'

    def is_move_valid(self, move):
        """
        Takes in the desired square to move to as a parameter.
        Returns true if the move is valid. Returns false if not valid.
        """
        current_position = self.get_position()
        slope = (move[1] - current_position[1]) / (current_position[0]  - current_position[0])

        if current_position == move:
            return False
        elif move[0] < 0 or move[0] > 7:
            return False
        elif move[1] < 0 or move[1] > 7:
            return False
        elif current_position[0] - move[0] == 0 or current_position[1] - move[1] == 0:
            return False
        elif slope != 1 or slope != -1:
            return False
        else:
            return True


class Knight(ChessPiece):
    """
    A class that represents a Knight chess piece. Inherits from
    the ChessPiece class. Moves in an ‘L-shape,’ two squares in a
    straight direction, and then one square perpendicular to that.
    """
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self._piece_type = 'KNIGHT'

    def is_move_valid(self, move):
        """
        Takes in the desired square to move to as a parameter.
        Returns true if the move is valid. Returns false if not valid.
        """
        current_position = self.get_position()

        if current_position == move:
            return False
        elif move[0] < 0 or move[0] > 7:
            return False
        elif move[1] < 0 or move[1] > 7:
            return False
        elif move[0] - current_position[0] == 2 or move[0] - current_position[0] == -2:
            if move[1] - current_position[1] != 1 or move[1] - current_position[1] != -1:
                return False
        elif move[1] - current_position[1] == 2 or move[1] - current_position[1] == -2:
            if move[0] - current_position[0] != 1 or move[0] - current_position[0] != -1:
                return False
        else:
            return True


class Pawn(ChessPiece):
    """
    A class that represents a Pawn chess piece. Inherits from
    the ChessPiece class. Moves one square forward, but on its first move,
    it can move two squares forward. It captures diagonally one square forward.
    """
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self._has_moved = False
        self._piece_type = 'PAWN'

    def get_valid_moves(self, board):
        """
        Takes the current board layout as input.
        Returns a list of all possible moves for the pawn on the board.
        """
        x_coord = self._position[1]
        y_coord = self._position[0]
        valid_moves = []
        if self._color == 'WHITE':
            if not self._has_moved and not board[y_coord - 2][x_coord]:
                valid_moves.append((y_coord - 2, x_coord))
            if not board[y_coord - 1][x_coord]:
                valid_moves.append((y_coord - 1, x_coord))
        else:
            if not self._has_moved and not board[y_coord + 2][x_coord]:
                valid_moves.append((y_coord + 2, x_coord))
            if not board[y_coord + 1][x_coord]:
                valid_moves.append((y_coord + 1, x_coord))
        return valid_moves

myboard = ChessVar()
myboard.print_board()
myboard.make_move('d2', 'd4')
myboard.make_move('e1', 'd2')
myboard.print_board()

