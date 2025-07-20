import numpy as np
import chess


def fen_to_bitmap(fen: str) -> np.ndarray:
    """
    Converts FEN Notation into 8x8 bitmap    
    """
    board = chess.Board(fen)
    bitmap = np.zeros((8, 8), dtype=int)

    for square in chess.SQUARES:
        if board.piece_at(square):
            row = 7 - (square // 8)
            col = square % 8
            bitmap[row][col] = 1

    return bitmap


def find_diff_indices(bitmap1: np.ndarray, bitmap2: np.ndarray):
    """
    Returns tuple of arrays of indices where bitmaps differ
    """
    return np.where(bitmap1 != bitmap2)

def bitmaps_equal(bitmap1: np.ndarray, bitmap2: np.ndarray) -> bool:
    """
    Return True if bitmaps are exactly equal
    """
    return np.array_equal(bitmap1, bitmap2)

def indices_to_coords(diff_indices):
    """
    Convert np.where output into list of chess coords like ['e4', 'd5']
    """
    rows, cols = diff_indices
    coords = []
    for r, c in zip(rows, cols):
        rank = 8 - r
        file = chr(ord('a') + c)
        coords.append(f"{file}{rank}")
    return coords

def find_dif_coords(bitmap1: np.ndarray, bitmap2: np.ndarray):
    indicies = find_diff_indices(bitmap1, bitmap2)
    return indices_to_coords(indicies)

# def coords to indicies(coords):


