"""
A GUI chess board that can be interacted with, and pieces moved around on.
"""

import tkinter as tk
from typing import Iterable

from chessington.engine.board import Board, BOARD_SIZE
from chessington.engine.data import Square
from chessington.ui.colours import Colour
from chessington.ui.images import ImageRepository

WINDOW_SIZE = 60

images = ImageRepository()


def get_square_colour(square: Square):
    """Determine the background colour of a square (checkerboard pattern)"""
    return Colour.BLACK_SQUARE if square.row % 2 == square.col % 2 else Colour.WHITE_SQUARE


def update_square(window: tk.Tk, board: Board, square: Square, colour: Colour = None):
    """Re-draw the Square, optionally setting a non-standard background colour"""
    piece = board.get_piece(square)
    colour = colour or get_square_colour(square)
    image = images.get_image(piece, colour)

    frame = window.nametowidget(square_id(square))
    btn = frame.nametowidget('button')
    btn.configure(image=image)
    btn.image = image


def update_pieces_and_colours(window: tk.Tk, board: Board):
    """Refresh the GUI to reflect the board state"""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            update_square(window, board, Square(row, col))


def highlight_squares(window: tk.Tk, board: Board, from_square: Square, to_squares: Iterable[Square]):
    """Set background colours on active movement squares"""
    if from_square is not None:
        update_square(window, board, from_square, Colour.FROM_SQUARE)
    for square in to_squares:
        update_square(window, board, square, Colour.TO_SQUARE)


def square_id(square: Square):
    """Generate a tkinter-suitable name for a square"""
    return f'square@{square.row}{square.col}'


def play_game():
    """Launch Chessington!"""
    window = tk.Tk()
    window.title('Chessington')
    window.resizable(False, False)
    board = Board.at_starting_position()

    from_square = None
    to_squares = []

    def generate_click_handler(clicked_square: Square):
        def handle_click():
            nonlocal window, board, from_square, to_squares
            clicked_piece = board.get_piece(clicked_square)

            # If making an allowed move, then make it
            if from_square is not None and clicked_square in to_squares:
                board.get_piece(from_square).move_to(board, clicked_square)
                from_square, to_squares = None, []

            # If clicking on a piece whose turn it is, get its allowed moves
            elif clicked_piece is not None and clicked_piece.player == board.current_player:
                from_square = clicked_square
                to_squares = clicked_piece.get_available_moves(board)

            # Otherwise reset everthing to default
            else:
                from_square, to_squares = None, []

            update_pieces_and_colours(window, board)
            highlight_squares(window, board, from_square, to_squares)

        return handle_click

    # Create the board
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            square = Square(row, col)
            frame = tk.Frame(window, width=WINDOW_SIZE, height=WINDOW_SIZE, name=square_id(square))
            frame.grid_propagate(False)         # disables resizing of frame
            frame.columnconfigure(0, weight=1)  # enables button to fill frame
            frame.rowconfigure(0, weight=1)     # any positive number is OK

            # The board has (0, 0) in the bottom left.
            # TKinter Grid has (0, 0) in the top left.
            # Map between these:
            gui_row = BOARD_SIZE - square.row - 1
            frame.grid(row=gui_row, column=square.col)

            btn = tk.Button(frame, command=generate_click_handler(square), name='button')
            btn.grid(sticky='wens')

    update_pieces_and_colours(window, board)
    window.mainloop()

