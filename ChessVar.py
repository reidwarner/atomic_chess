# Author: Reid Singleton
# GitHub username: reidwarner
# Date: 5/27/2024
# Description: A program for playing atomic chess.

import pygame, os
SQUARE_LEN = 100

class ChessVar:
    """
    A class that represents a game of atomic chess.
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
        A method that returns a string for the current status of the game -
        whether the game is unfinished or if a player has won the game.
        :return: string that represents an unfinished game or if a player has won
        """
        return self._game_state

    def get_player_turn(self):
        """
        A method that returns a string for which color's turn it is.
        :return: string that contains current turn's color
        """
        return self._player_turn

    def make_move(self, move_from, move_to):
        """
        A method for moving a chess piece.
        :param move_from: string that represents where the piece the player wants to move is in algebraic notation
        :param move_to: string that represents where the piece is to be moved in algebraic notation
        :return: True if move is successful, False if not successful
        """
        # If game has already been won, return False
        if self._game_state != 'UNFINISHED':
            return False

        # Get the piece object at the move_from square and check the inputs are valid
        square_start = self.translate_square(move_from)
        if square_start[0] is False:
            return False
        square_end = self.translate_square(move_to)
        if square_start[1] is False:
            return False

        piece = self._board[square_start[0]][square_start[1]]

        # If a piece is not at start square, return False
        if not piece:
            return False

        # Check if piece to be moved violates a player's turn
        if piece.get_color() != self._player_turn:
            return False

        # Get list of valid moves for the piece
        valid_moves = piece.get_valid_moves(self._board)

        # If the move_to square is in the list, make the move and return True
        if square_end in valid_moves:

            # If a piece is being captured, detonate explosion and remove affected pieces
            captured_piece = self._board[square_end[0]][square_end[1]]
            if captured_piece:
                captured_piece.capture_piece()
                self._board[square_end[0]][square_end[1]] = piece
                self._board[square_start[0]][square_start[1]] = None
                self.explosion(self._board, square_end)

            # Move the piece
            if not captured_piece:
                self._board[square_end[0]][square_end[1]] = piece
                self._board[square_start[0]][square_start[1]] = None
                piece.set_position((square_end[0], square_end[1]))

            # Check if pawn to set has moved
            if piece.get_piece_type() == 'PAWN' and not piece.get_pawn_move_status():
                piece.set_pawn_move_status()

            # Change Player Turn
            if self._player_turn == 'WHITE':
                self._player_turn = 'BLACK'
            else:
                self._player_turn = 'WHITE'

            return True
        else:
            return False

    def initialize_board(self):
        """
        Sets up the board for a new game.
        :return: Nothing
        """
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
            x_coord, y_coord = piece.get_position()
            self._board[x_coord][y_coord] = piece

    def print_board(self):
        """
        A class that prints the current board when called on a ChessVar object. Prints the board
        in an ASCII art styling.
        :return: Nothing
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
        :param square: a string in algebraic notation
        :return: a tuple of integers
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

    def explosion(self, board, square):
        """
        A method that represents an explosion when a chess piece attacks an opponent's piece. Updates the
        game board data member if the explosion removes chess pieces.
        :param board: list of lists representing the chess board
        :param square: tuple of integers representing a board position
        :return: Nothing
        """
        blast_radius = [(0, 0), (1, 0), (1, 1), (0, 1), (-1, 0), (-1, 1), (-1, -1), (0, -1), (1, -1)]

        # Check if a pawn suicide
        if board[square[0]][square[1]].get_piece_type() == 'PAWN':
            board[square[0]][square[1]] = None

        for position in blast_radius:
            blast_x = square[1] + position[1]
            blast_y = square[0] + position[0]

            if blast_x < 0 or blast_x > 7:
                continue
            if blast_y < 0 or blast_y > 7:
                continue

            affected_piece = board[blast_y][blast_x]
            if affected_piece and affected_piece.get_piece_type() != 'PAWN':
                affected_piece.capture_piece()
                if affected_piece.get_piece_type() == 'KING':
                    winner = self.get_player_turn()
                    self._game_state = f'{winner}_WON'
                board[blast_y][blast_x] = None

    def display_board(self):
        """
        """
        # Display the board background
        color_brown = (92, 64, 51)
        pygame.draw.rect(screen, color_brown, pygame.Rect(0, 0, 900, 900))

        # Initializing Color
        color_light = (234, 221, 202)
        color_dark = (150, 105, 25)

        # Drawing Rectangle
        red_index_left = 50
        red_index_top = 50
        for index_i in range(0, 7, 2):
            for index_j in range(0, 8, 2):
                pygame.draw.rect(screen, color_light, pygame.Rect(red_index_left + (index_j * SQUARE_LEN),
                                                                  red_index_top + (index_i * SQUARE_LEN), SQUARE_LEN,
                                                                  SQUARE_LEN))
                pygame.draw.rect(screen, color_dark, pygame.Rect(red_index_left + ((index_j + 1) * SQUARE_LEN),
                                                                 red_index_top + (index_i * SQUARE_LEN), SQUARE_LEN,
                                                                 SQUARE_LEN))
            for index_j in range(0, 8, 2):
                pygame.draw.rect(screen, color_dark, pygame.Rect(red_index_left + (index_j * SQUARE_LEN),
                                                                 (index_i * SQUARE_LEN) + SQUARE_LEN + red_index_top,
                                                                 SQUARE_LEN, SQUARE_LEN))
                pygame.draw.rect(screen, color_light, pygame.Rect(red_index_left + ((index_j + 1) * SQUARE_LEN),
                                                                  (index_i * SQUARE_LEN) + SQUARE_LEN + red_index_top,
                                                                  SQUARE_LEN, SQUARE_LEN))
        # Display current pieces
        for row in self._board:
            for piece in row:
                if piece:
                    color = piece.get_color()
                    position =piece.get_position()
                    piece_type = piece.get_piece_type()
                    filename = f'{color}_{piece_type}.png'
                    image = pygame.image.load(os.path.join('img', filename)).convert_alpha()
                    img_x = position[1] * SQUARE_LEN + (SQUARE_LEN / 2) + 5
                    img_y = position[0] * SQUARE_LEN + (SQUARE_LEN / 2) + 5
                    screen.blit(image, (img_x, img_y))

                    pygame.display.flip()


class ChessPiece:
    """
    A class that represents the different types of chess pieces. Each piece type inherits from this class.
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
        :param square: Tuple of integers that represents a position on the chess board
        :return: Nothing
        """
        self._position = square

    def capture_piece(self):
        """
        Changes a pieces captured status to captured.
        :return: Nothing
        """
        self._captured = True

    def get_piece_type(self):
        """Returns the type of piece a piece object is."""
        return self._piece_type

    def is_move_valid(self, board, new_x_coord, new_y_coord, color):
        """
        A method that checks if a potential move is in bounds on the chess board and if a move
        would result in landing on a friendly chess piece.
        :param board: list of lists that represents a chess board
        :param new_x_coord: an integer representing one dimension of chess board position
        :param new_y_coord: an integer representing one dimension of chess board position
        :param color: string that represents the player's color
        :return: True if move is valid, False if not valid
        """
        if (new_x_coord < 0 or new_x_coord > 7) or (0 > new_y_coord or new_y_coord > 7):
            return False
        if board[new_y_coord][new_x_coord] and board[new_y_coord][new_x_coord].get_color() == color:
            return False
        else:
            return True


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
        Creates a list of all the valid, possible moves for a King.
        :param board: list of lists that represents a chess board
        :return: list of tuples that represent coordinates on the chess board
        """
        x_coord = self._position[1]
        y_coord = self._position[0]
        valid_moves = []

        for move in self._king_moves:
            new_x_coord = x_coord + move[1]
            new_y_coord = y_coord + move[0]
            is_valid = self.is_move_valid(board, new_x_coord, new_y_coord, self._color)
            if is_valid and not board[new_y_coord][new_x_coord]:
                valid_moves.append((new_y_coord, new_x_coord))
        return valid_moves


class Queen(ChessPiece):
    """
    A class that represents a Queen chess piece. Inherits from
    the ChessPiece class. Can move any amount of squares diagonally, vertically
    or horizontally.
    """
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self._piece_type = 'QUEEN'
        self._queen_moves = []

    def generate_queen_moves(self, board):
        """
        Creates a list of all the valid, possible moves for a Queen and saves them to a data member for the Queen
        object.
        :param board: list of lists that represents a chess board
        :return: Nothing
        """
        x_coord = self._position[1]
        y_coord = self._position[0]

        self._queen_moves = []

        # Checks if spaces above piece are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord, y_coord - index, self.get_color()):
                self._queen_moves.append((y_coord - index, x_coord))
                if board[y_coord - index][x_coord]:
                    break
            else:
                break

        # Checks if spaces below piece are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord, y_coord + index, self.get_color()):
                self._queen_moves.append((y_coord + index, x_coord))
                if board[y_coord + index][x_coord]:
                    break
            else:
                break

        # Checks if spaces left of the piece are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord - index, y_coord, self.get_color()):
                self._queen_moves.append((y_coord, x_coord - index))
                if board[y_coord][x_coord - index]:
                    break
            else:
                break

        # Check if spaces right of the piece are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord + index, y_coord, self.get_color()):
                self._queen_moves.append((y_coord, x_coord + index))
                if board[y_coord][x_coord + index]:
                    break
            else:
                break

        # Check if spaces right/below are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord + index, y_coord + index, self.get_color()):
                self._queen_moves.append((y_coord + index, x_coord + index))
                if board[y_coord + index][x_coord + index]:
                    break
            else:
                break

        # Checks if spaces left/above are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord - index, y_coord - index, self.get_color()):
                self._queen_moves.append((y_coord - index, x_coord - index))
                if board[y_coord - index][x_coord - index]:
                    break
            else:
                break

        # Check if spaces right/above are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord + index, y_coord - index, self.get_color()):
                self._queen_moves.append((y_coord - index, x_coord + index))
                if board[y_coord - index][x_coord + index]:
                    break
            else:
                break

        # Checks if spaces left/below are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord - index, y_coord + index, self.get_color()):
                self._queen_moves.append((y_coord + index, x_coord - index))
                if board[y_coord + index][x_coord - index]:
                    break
            else:
                break

    def get_valid_moves(self, board):
        """
        Creates a list of all the valid, possible moves for a Queen.
        :param board: list of lists that represents a chess board
        :return: list of tuples that represent coordinates on the chess board
        """
        self.generate_queen_moves(board)
        valid_moves = self._queen_moves
        return valid_moves


class Rook(ChessPiece):
    """
    A class that represents a Rook chess piece. Inherits from
    the ChessPiece class. Can move any amount of squares vertically
    or horizontally.
    """
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self._piece_type = 'ROOK'
        self._rook_moves = []

    def generate_rook_moves(self, board):
        """
        Creates a list of all the valid, possible moves for a Rook and saves them to a data member for the Rook
        object.
        :param board: list of lists that represents a chess board
        :return: Nothing
        """
        x_coord = self._position[1]
        y_coord = self._position[0]

        self._rook_moves = []

        # Checks if spaces above piece are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord, y_coord - index, self.get_color()):
                self._rook_moves.append((y_coord - index, x_coord))
                if board[y_coord - index][x_coord]:
                    break
            else:
                break

        # Checks if spaces below piece are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord, y_coord + index, self.get_color()):
                self._rook_moves.append((y_coord + index, x_coord))
                if board[y_coord + index][x_coord]:
                    break
            else:
                break

        # Checks if spaces left of the piece are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord - index, y_coord, self.get_color()):
                self._rook_moves.append((y_coord, x_coord - index))
                if board[y_coord][x_coord - index]:
                    break
            else:
                break

        # Check if spaces right of the piece are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord + index, y_coord, self.get_color()):
                self._rook_moves.append((y_coord, x_coord + index))
                if board[y_coord][x_coord + index]:
                    break
            else:
                break

    def get_valid_moves(self, board):
        """
        Creates a list of all the valid, possible moves for a Rook.
        :param board: list of lists that represents a chess board
        :return: list of tuples that represent coordinates on the chess board
        """
        self.generate_rook_moves(board)
        valid_moves = self._rook_moves
        return valid_moves


class Bishop(ChessPiece):
    """
    A class that represents a Bishop chess piece. Inherits from
    the ChessPiece class. Can move any amount of squares diagonally.
    """
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self._piece_type = 'BISHOP'
        self._bishop_moves = []

    def generate_bishop_moves(self, board):
        """
        Creates a list of all the valid, possible moves for a bishop and saves them to a data member for the bishop
        object.
        :param board: list of lists that represents a chess board
        :return: Nothing
        """
        x_coord = self._position[1]
        y_coord = self._position[0]

        self._bishop_moves = []

        # Check if spaces right/below are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord + index, y_coord + index, self.get_color()):
                self._bishop_moves.append((y_coord + index, x_coord + index))
                if board[y_coord + index][x_coord + index]:
                    break
            else:
                break

        # Checks if spaces left/above are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord - index, y_coord - index, self.get_color()):
                self._bishop_moves.append((y_coord - index, x_coord - index))
                if board[y_coord - index][x_coord - index]:
                    break
            else:
                break

        # Check if spaces right/above are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord + index, y_coord - index, self.get_color()):
                self._bishop_moves.append((y_coord - index, x_coord + index))
                if board[y_coord - index][x_coord + index]:
                    break
            else:
                break

        # Checks if spaces left/below are valid moves
        for index in range(1, 8):
            if self.is_move_valid(board, x_coord - index, y_coord + index, self.get_color()):
                self._bishop_moves.append((y_coord + index, x_coord - index))
                if board[y_coord + index][x_coord - index]:
                    break
            else:
                break

    def get_valid_moves(self, board):
        """
        Creates a list of all the valid, possible moves for a bishop.
        :param board: list of lists that represents a chess board
        :return: list of tuples that represent coordinates on the chess board
        """
        self.generate_bishop_moves(board)
        valid_moves = self._bishop_moves
        return valid_moves


class Knight(ChessPiece):
    """
    A class that represents a Knight chess piece. Inherits from
    the ChessPiece class. Moves in an ‘L-shape,’ two squares in a
    straight direction, and then one square perpendicular to that.
    """
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self._piece_type = 'KNIGHT'
        self._knight_moves = [(-2, -1), (2, -1), (-1, -2), (1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1)]

    def get_valid_moves(self, board):
        """
        Creates a list of all the valid, possible moves for a Knight and saves them to a data member for the Knight
        object.
        :param board: list of lists that represents a chess board
        :return: List of tuples of coordinates of possible knight moves
        """
        x_coord = self._position[1]
        y_coord = self._position[0]
        valid_moves = []

        for move in self._knight_moves:
            new_x_coord = x_coord + move[1]
            new_y_coord = y_coord + move[0]
            is_valid = self.is_move_valid(board, new_x_coord, new_y_coord, self._color)
            if is_valid:
                valid_moves.append((new_y_coord, new_x_coord))
        return valid_moves


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

    def get_pawn_move_status(self):
        """
        A method that returns True if a pawn has already been moved or False if the pawn
        object has yet to move.
        """
        return self._has_moved

    def set_pawn_move_status(self):
        """
        If called, sets the pawn move status to True.
        """
        self._has_moved = True

    def get_valid_moves(self, board):
        """
        Creates a list of all the valid, possible moves for a Pawn.
        :param board: list of lists that represents a chess board
        :return: list of tuples that represent coordinates on the chess board
        """
        x_coord, y_coord = self._position[1], self._position[0]
        valid_moves = []

        if self._color == 'WHITE':
            if self.is_move_valid(board, x_coord, y_coord - 2, self.get_color()):
                if not self._has_moved and not board[y_coord - 2][x_coord]:
                    valid_moves.append((y_coord - 2, x_coord))
            if self.is_move_valid(board, x_coord, y_coord - 1, self.get_color()):
                if not board[y_coord - 1][x_coord]:
                    valid_moves.append((y_coord - 1, x_coord))
            if self.is_move_valid(board, x_coord - 1, y_coord - 1, self.get_color()):
                if board[y_coord - 1][x_coord - 1] and board[y_coord - 1][x_coord - 1].get_color() != 'WHITE':
                    valid_moves.append((y_coord - 1, x_coord - 1))
            if self.is_move_valid(board, x_coord + 1, y_coord - 1, self.get_color()):
                if board[y_coord - 1][x_coord + 1] and board[y_coord - 1][x_coord + 1].get_color() != 'WHITE':
                    valid_moves.append((y_coord - 1, x_coord + 1))
        else:
            if self.is_move_valid(board, x_coord, y_coord + 2, self.get_color()):
                if not self._has_moved and not board[y_coord + 2][x_coord]:
                    valid_moves.append((y_coord + 2, x_coord))
            if self.is_move_valid(board, x_coord, y_coord + 1, self.get_color()):
                if not board[y_coord + 1][x_coord]:
                    valid_moves.append((y_coord + 1, x_coord))
            if self.is_move_valid(board, x_coord + 1, y_coord + 1, self.get_color()):
                if board[y_coord + 1][x_coord - 1] and board[y_coord + 1][x_coord - 1].get_color() != 'BLACK':
                    valid_moves.append((y_coord + 1, x_coord - 1))
            if self.is_move_valid(board, x_coord + 1, y_coord + 1, self.get_color()):
                if board[y_coord + 1][x_coord + 1] and board[y_coord + 1][x_coord + 1].get_color() != 'BLACK':
                    valid_moves.append((y_coord + 1, x_coord + 1))
        return valid_moves



# initializing imported module
pygame.init()
# displaying a window of height
screen = pygame.display.set_mode((900, 900))

# Function for converting coords to algebraic notaion
def position_to_algebraic(pos):
    """"""
    letter_dict = {0: 'a',
                   1: 'b',
                   2: 'c',
                   3: 'd',
                   4: 'e',
                   5: 'f',
                   6: 'g',
                   7: 'h',
                   }
    y, x = pos[0], pos[1]
    x = int(10 - ((x + (SQUARE_LEN / 2)) // SQUARE_LEN) - 1)
    y = ((y + (SQUARE_LEN / 2)) // SQUARE_LEN) - 1

    return f'{letter_dict[y]}{str(x)}'


game = ChessVar()
game.display_board()

running = True
x_cord_from, y_cord_from, x_cord_to, y_cord_to = 0, 0, 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            alg_from_square = position_to_algebraic(event.dict['pos'])
        if event.type == pygame.MOUSEBUTTONUP:
            alg_to_square = position_to_algebraic(event.dict['pos'])
            game.make_move(alg_from_square, alg_to_square)
            game.display_board()
        if event.type == pygame.QUIT:
            running = False

