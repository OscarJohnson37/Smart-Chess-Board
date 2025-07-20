import chess
import chess.engine
import numpy as np

STOCKFISH_PATH = "/opt/homebrew/bin/stockfish"  # Change to your Stockfish binary path

board = chess.Board()

skillLevel = 20

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

# Set skill level (0 to 20, where 20 is max strength)
engine.configure({"Skill Level": skillLevel})

board.push_san("e2e4")

result = engine.play(board, chess.engine.Limit(time=0.1))

board.push(result.move)

print("Best move at skill level", skillLevel, ":", result.move)
print(board.fen())

def fen_to_bitmap(fen: str) -> np.ndarray:
    board = chess.Board(fen)
    bitmap = np.zeros((8, 8), dtype=int)

    for square in chess.SQUARES:
        if board.piece_at(square):
            row = 7 - (square // 8)
            col = square % 8
            bitmap[row][col] = 1

    return bitmap

bitmap = fen_to_bitmap(board.fen())

print(bitmap)

engine.quit()