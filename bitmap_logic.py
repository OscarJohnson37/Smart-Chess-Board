import numpy as np

import chess

import chess.engine

import bitmap_utils

board = chess.Board()

STOCKFISH_PATH = "/opt/homebrew/bin/stockfish"

skillLevel = 20

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

# Set skill level (0 to 20, where 20 is max strength)
engine.configure({"Skill Level": skillLevel})

def index_to_chess_coord(row, col):
    # Map row 0->8, row 7->1 (ranks count from bottom)
    rank = 8 - row
    
    # Map col 0->'a', col 1->'b', ..., col 7->'h'
    file = chr(ord('a') + col)
    
    return f"{file}{rank}"

gamestart_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

gamestart_bitmap = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]])

previous_bitmap = gamestart_bitmap.copy()

current_bitmap = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]])

diff_indices = np.where(current_bitmap != previous_bitmap)

piece_start = None


if diff_indices[0].size == 0:
    print("No differences")
else:
    row = int(diff_indices[0][0])
    col = int(diff_indices[1][0])
    piece_start = index_to_chess_coord(row, col)
    print(piece_start)

previous_bitmap = current_bitmap.copy()

current_bitmap = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]])

diff_indices = np.where(current_bitmap != previous_bitmap)

piece_final = None

if diff_indices[0].size == 0:
    print("No differences")
else:
    row = int(diff_indices[0][0])
    col = int(diff_indices[1][0])
    piece_final = index_to_chess_coord(row, col)
    print(piece_final)

move = chess.Move.from_uci(piece_start + piece_final)

if move in board.legal_moves:
    board.push(move)
    print("Move played:", move.uci())
else:
    print("illegal_move")

print(current_bitmap)


result = engine.play(board, chess.engine.Limit(time=0.1))


board.push(result.move)

expected_bitmap = bitmap_utils.fen_to_bitmap(board.fen())

print("stockfish moves to" , result.move)

print(expected_bitmap)

previous_bitmap = current_bitmap.copy()

current_bitmap = expected_bitmap

if np.array_equal(current_bitmap, expected_bitmap):

    previous_bitmap = current_bitmap.copy()

current_bitmap = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1]])
    

diff_indices = np.where(current_bitmap != previous_bitmap)


if diff_indices[0].size == 0:
    print("No differences")
else:
    row = int(diff_indices[0][0])
    col = int(diff_indices[1][0])
    piece_start = index_to_chess_coord(row, col)
    print(piece_start)

previous_bitmap = current_bitmap.copy()

current_bitmap = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1]])

diff_indices = np.where(current_bitmap != previous_bitmap)


if diff_indices[0].size == 0:
    print("No differences")
else:
    row = int(diff_indices[0][0])
    col = int(diff_indices[1][0])
    piece_final = index_to_chess_coord(row, col)
    print(piece_final)

move = chess.Move.from_uci(piece_start + piece_final)

if move in board.legal_moves:
    board.push(move)
    print("Move played:", move.uci())
else:
    print("illegal move")

print(current_bitmap)

result = engine.play(board, chess.engine.Limit(time=0.1))


board.push(result.move)

expected_bitmap = bitmap_utils.fen_to_bitmap(board.fen())

print("stockfish moves to" , result.move)

print(expected_bitmap)

print(board)