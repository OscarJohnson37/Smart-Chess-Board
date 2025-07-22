import chess

STOCKFISH_PATH = "/opt/homebrew/bin/stockfish"

class Game:
    def __init__(self, player1, player2):
        
        self.players = {
            player1.colour: player1, # colour is 'black' or 'white'
            player2.colour: player2
        }

        self.to_move = 'white'
        self.board = chess.Board()

        self.update_current_player()


    def change_turns(self):
        self.to_move = 'black' if self.to_move == 'white' else 'white'

        self.update_current_player()


    def start_game(self):
        self.to_move = 'white'
        self.board = chess.Board()

        self.update_current_player()
        


    def update_current_player(self):
        self.current_player = self.players[self.to_move]


    def apply_move(self, move):
        move = chess.Move.from_uci(move)
        self.board.push(move)

    def is_legal_move(self, move):
        move = chess.Move.from_uci(move)
        if move in self.board.legal_moves:
            return True
        return False