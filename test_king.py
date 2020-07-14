from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import King
from chessington.engine.pieces import Pawn

class TestKings:

    @staticmethod
    def test_white_king_can_move_up_one_square():

        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        square = Square.at(4, 4)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 3) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(5, 5) in moves

    
    @staticmethod
    def test_black_king_can_move_up_one_square():

        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 3) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(5, 5) in moves

    @staticmethod
    def test_king_cannot_move_off_the_top_of_board():

        # Arrange 
        board = Board.empty()
        king = King(Player.BLACK)
        square = Square.at(7,4)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(6, 3) in moves
        assert Square.at(6, 4) in moves
        assert Square.at(6, 5) in moves
        assert Square.at(7, 3) in moves
        assert Square.at(7, 5) in moves
        assert Square.at(8, 3) not in moves
        assert Square.at(8, 4) not in moves
        assert Square.at(8, 5) not in moves

    @staticmethod
    def test_king_cannot_move_off_the_bottom_of_board():

        # Arrange 
        board = Board.empty()
        king = King(Player.BLACK)
        square = Square.at(0,4)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 5) in moves
        assert Square.at(0, 3) in moves
        assert Square.at(0, 5) in moves
        assert Square.at(-1, 3) not in moves
        assert Square.at(-1, 4) not in moves
        assert Square.at(-1, 5) not in moves

    @staticmethod
    def test_king_cannot_move_off_the_left_of_board():

        # Arrange 
        board = Board.empty()
        king = King(Player.BLACK)
        square = Square.at(4,0)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 1) in moves
        assert Square.at(4, 1) in moves
        assert Square.at(5, 1) in moves
        assert Square.at(3, 0) in moves
        assert Square.at(5, 0) in moves
        assert Square.at(3, -1) not in moves
        assert Square.at(4, -1) not in moves
        assert Square.at(5, -1) not in moves

    @staticmethod
    def test_king_cannot_move_off_the_right_of_board():

        # Arrange 
        board = Board.empty()
        king = King(Player.BLACK)
        square = Square.at(4,7)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 6) in moves
        assert Square.at(4, 6) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(3, 7) in moves
        assert Square.at(5, 7) in moves
        assert Square.at(3, 8) not in moves
        assert Square.at(4, 8) not in moves
        assert Square.at(5, 8) not in moves
    
    @staticmethod
    def test_king_cannot_move_into_friendly_pieces():

        # Arrange 
        board = Board.empty()
        king = King(Player.WHITE)
        square = Square.at(4,4)

        pawn1 = Pawn(Player.WHITE)
        pawn2 = Pawn(Player.WHITE)
        pawn3 = Pawn(Player.WHITE)
        pawn4 = Pawn(Player.WHITE)
        pawn5 = Pawn(Player.WHITE)
        pawn6 = Pawn(Player.WHITE)
        pawn7 = Pawn(Player.WHITE)
        pawn8 = Pawn(Player.WHITE)

        square1 = Square.at(3, 3)
        square2 = Square.at(3, 4)
        square3 = Square.at(3, 5)
        square4 = Square.at(4, 3)
        square5 = Square.at(4, 5)
        square6 = Square.at(5, 3)
        square7 = Square.at(5, 4)
        square8 = Square.at(5, 5)

        board.set_piece(square, king)
        board.set_piece(square1, pawn1)
        board.set_piece(square2, pawn2)
        board.set_piece(square3, pawn3)
        board.set_piece(square4, pawn4)
        board.set_piece(square5, pawn5)
        board.set_piece(square6, pawn6)
        board.set_piece(square7, pawn7)
        board.set_piece(square8, pawn8)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 3) not in moves
        assert Square.at(3, 4) not in moves
        assert Square.at(3, 5) not in moves
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 5) not in moves
        assert Square.at(5, 3) not in moves
        assert Square.at(5, 4) not in moves
        assert Square.at(5, 5) not in moves 


    @staticmethod
    def test_king_can_take_enemy_pieces():

        # Arrange 
        board = Board.empty()
        king = King(Player.WHITE)
        square = Square.at(4,4)

        pawn1 = Pawn(Player.BLACK)
        pawn2 = Pawn(Player.BLACK)
        pawn3 = Pawn(Player.BLACK)
        pawn4 = Pawn(Player.BLACK)
        pawn5 = Pawn(Player.BLACK)
        pawn6 = Pawn(Player.BLACK)
        pawn7 = Pawn(Player.BLACK)
        pawn8 = Pawn(Player.BLACK)

        square1 = Square.at(3, 3)
        square2 = Square.at(3, 4)
        square3 = Square.at(3, 5)
        square4 = Square.at(4, 3)
        square5 = Square.at(4, 5)
        square6 = Square.at(5, 3)
        square7 = Square.at(5, 4)
        square8 = Square.at(5, 5)

        board.set_piece(square, king)
        board.set_piece(square1, pawn1)
        board.set_piece(square2, pawn2)
        board.set_piece(square3, pawn3)
        board.set_piece(square4, pawn4)
        board.set_piece(square5, pawn5)
        board.set_piece(square6, pawn6)
        board.set_piece(square7, pawn7)
        board.set_piece(square8, pawn8)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 3) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(5, 5) in moves 