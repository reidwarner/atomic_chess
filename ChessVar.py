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
        A method that takes two move parameters - starting square and ending square.
        The method determines if the move is valid. It will return False if not valid.
        If valid, the method makes the requested move, adjust any captured pieces, update the
        game state, update whose turn it is and return True.
        """
        # Check/get the object in the move_from square
        start_square = self.translate_square(move_from)
        end_square = self.translate_square(move_to)

        # Check there is a valid end square in bounds
        if 0 > end_square[0] > 7 or 0 > end_square[1] > 7:
            return False

        piece_object = self._board[start_square[0]][start_square[1]]
        if not piece_object:
            print("Invalid move.")
            return False

        # Check if the requested move is valid for each piece type
        if not piece_object.is_move_valid(end_square):
            return False

        # Check if move results in illegal jump

        # Update the board
        self._board[start_square[0]][start_square[1]] = None
        self._board[end_square[0]][end_square[1]] = piece_object
        return True



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

        col = ord(square[0]) - ord('a')
        row = row_dict[square[1]]
        return row, col

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

    def is_move_valid(self, move):
        """
        Takes in the desired square to move to as a parameter.
        Returns true if the move is valid. Returns false if not valid.
        """
        current_position = self.get_position()

        if current_position == move:
            return False
        elif -2 < current_position[0] - move[0] > 2:
            return False
        elif -2 < current_position[1] - move[1] > 2:
            return False
        elif current_position[0] - move[0] != 0 and current_position[1] - move[1] != 0:
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

    def is_move_valid(self, move):
        """
        Takes in the desired square to move to as a parameter.
        Returns true if the move is valid. Returns false if not valid.
        """
        current_position = self.get_position()

        if current_position == move:
            return False
        elif current_position[1] != move[1]:
            return False
        elif move[0] < 0 or move[0] > 7:
            return False
        elif move[1] < 0 or move[1] > 7:
            return False
        elif move[0] == current_position[0]:
            return False
        elif self.get_color() == 'WHITE':
            if not self._has_moved and current_position[0] - move[0] > 2:
                return False
            elif self._has_moved and current_position[0] - move[0] > 1:
                return False
            else:
                return True
        elif self.get_color() == 'BLACK':
            if not self._has_moved and (move[0] - current_position[0]) < -2:
                return False
            elif self._has_moved and (move[0] - current_position[0]) < -1:
                return False
            else:
                return True

myboard = ChessVar()
myboard.print_board()
myboard.make_move('a2', 'a4')
myboard.print_board()
myboard.make_move('a7', 'a5')
myboard.print_board()
myboard.make_move('b1', 'c3')
myboard.print_board()
