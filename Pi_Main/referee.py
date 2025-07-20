import bitmap_utils
import numpy as np
import chess

def check_starting_position(bitmap):
    if np.array_equal(bitmap, bitmap_utils.gamestart_bitmap):
        print("Gamestart Boardstate")
        return True
    
def is_legal_move(move, board):
    if move in board.legal_moves:
        return True
    return False