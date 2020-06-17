import os
from typing import Optional

from PIL import Image, ImageTk

from chessington.engine.data import Player
from chessington.engine.pieces import Pawn, Knight, Bishop, King, Queen, Rook, Piece
from chessington.ui.colours import Colour

IMAGES_BASE_DIRECTORY = 'images'


class ImageRepository:
    """
    Tkinter can't handle a non-rectangular overlay on a coloured background. This is
    troublesome when programming a chess board.

    This class works around the limitation by providing pre-processed piece images
    with all possible backgrounds.
    """

    PIECES_WITH_IMAGES = [Pawn, Knight, Bishop, King, Queen, Rook]

    def __init__(self):
        self._images = {}
        self._load_from_disk()

    def _load_from_disk(self):
        """Load all possible images into memory to optimise performance"""
        mapping = {}

        def piece_on_all_backgrounds(piece: Optional[Piece]):
            return {colour: get_image_with_background(piece, colour) for colour in Colour}

        for piece in self.PIECES_WITH_IMAGES:
            mapping[piece] = {}
            mapping[piece][Player.WHITE] = piece_on_all_backgrounds(piece(Player.WHITE))
            mapping[piece][Player.BLACK] = piece_on_all_backgrounds(piece(Player.BLACK))

        mapping['empty'] = piece_on_all_backgrounds(None)
        self._images = mapping

    def get_image(self, piece: Piece, background_colour: Colour) -> ImageTk:
        """Get a GUI-ready image of a piece on the specified background colour"""
        if piece:
            image = self._images[piece.__class__][piece.player][background_colour]
        else:
            image = self._images['empty'][background_colour]
        return ImageTk.PhotoImage(image.convert('RGB'))


def get_filename_for_piece(piece: Piece) -> str:
    """Find the correct PNG file for a piece"""
    if piece is None:
        return os.path.join(IMAGES_BASE_DIRECTORY, 'blank.png')
    image_name = piece.__class__.__name__.lower() + piece.player._name_.lower()[0] + '.png'
    return os.path.join(IMAGES_BASE_DIRECTORY, image_name)


def get_image_for_piece(piece: Piece) -> Image:
    """Load a piece image from disk"""
    file = get_filename_for_piece(piece)
    return Image.open(file)


def get_image_with_background(piece: Piece, background_colour: Colour) -> Image:
    """Load a piece image from disk and add background colour.

    You can't make tkinter elements transparent, and they are all rectangular.
    This function pre-processes piece PNGs to give appropriate background colours.
    """
    image = get_image_for_piece(piece)
    new_image = Image.new("RGBA", image.size, background_colour.value)
    try:
        # This will error on an empty image
        new_image.paste(image, (0, 0), image)
    except:
        pass
    return new_image
