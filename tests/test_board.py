from chessington.engine.board import Board
from chessington.engine.data import Player, Square

def test_new_board_has_white_pieces_at_bottom():

    # Arrange
    board = Board.at_starting_position()

    # Act
    piece = board.get_piece(Square.at(0, 0))

    # Assert
    assert piece.player == Player.WHITE

def test_new_board_has_black_pieces_at_top():

    # Arrange
    board = Board.at_starting_position()

    # Act
    piece = board.get_piece(Square.at(7, 0))

    # Assert
    assert piece.player == Player.BLACK

def test_pieces_can_be_moved_on_the_board():

    # Arrange
    board = Board.at_starting_position()
    from_square = Square.at(1, 0)
    piece = board.get_piece(from_square)

    # Act
    to_square = Square.at(3, 0)
    board.move_piece(from_square, to_square)

    assert board.get_piece(from_square) is None
    assert board.get_piece(to_square) is piece