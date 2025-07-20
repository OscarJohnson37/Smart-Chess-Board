import chess

board = chess.Board()
print(board)

print(board.legal_moves)

# Choose the square of the piece you're interested in (e.g. E2)
square = chess.H8

print(square)

# Iterate over all legal moves on the board
legal_moves_for_piece = [move for move in board.legal_moves if move.from_square == square]

print("Legal moves for piece on E2:")
for move in legal_moves_for_piece:
    print(move.uci())

board.push_san("f3")
board.push_san("b8c6")
board.push_san("g4")

print(board.is_checkmate())
print(board.is_check())
print(board.is_stalemate())

print(board)

# Set up a position where black can castle queenside
board = chess.Board("r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1")

print(board)

move = chess.Move.from_uci("e8c8")  # Queenside castling for black
if move in board.legal_moves:
    board.push(move)


print(board)