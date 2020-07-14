"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        if (self.player == Player.WHITE):
            return self.move_by_side(board, 1, 1)
        else:
            return self.move_by_side(board, -1, 6)

    def move_by_side(self, board, move, startRow):
            available_moves = []
            square = board.find_piece(self)
            if (square.row != 0 and square.row != 7):
                forward = Square.at(square.row + move, square.col)
                if (board.get_piece(forward) == None):
                    available_moves.append(forward)

                    twoForward = Square.at(square.row + (move * 2), square.col)
                    if(square.row == startRow and board.get_piece(twoForward) == None):
                        available_moves.append(twoForward)

                if square.col >= 1 and square.col <= 7:
                    leftAttack = Square.at(square.row + move, square.col - 1)
                    leftTarget = board.get_piece(leftAttack)
                    if (leftTarget != None):
                        if (leftTarget.player != self.player):
                            available_moves.append(leftAttack)

                if square.col >= 0 and square.col <= 6:
                    rightAttack = Square.at(square.row + move, square.col + 1)
                    rightTarget = board.get_piece(rightAttack)
                    if (rightTarget != None):
                        if (rightTarget.player != self.player):
                            available_moves.append(rightAttack)
                    
            return available_moves

class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []