import chess
import chess.engine

STOCKFISH_PATH = "/opt/homebrew/bin/stockfish"


class Engine:
    def __init__(self, board, skill_level=20):
        """
        :param board: A reference to the current game board (e.g. python-chess Board, custom object, etc.)
        """
        self.board = board
        self.skill_level = skill_level
        self.highest_level = 20
        self.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
        self.engine.configure({"Skill Level": self.skill_level})

    def propose_move(self, skill_level=20):
        """
        Generate a move given the current board and a skill level.
        Skill level could adjust search depth, randomness, etc.
        
        :param skill_level: An int from 1 (easy) to 10 (hard)
        :return: Move in string format like 'e2e4'
        """
        self.set_skill_level(skill_level)

        result = self.engine.play(self.board, chess.engine.Limit(time=0.1))

        return result
    
    def set_skill_level(self, skill_level):
        self.engine.configure({"Skill Level": self.skill_level})

    def propose_best_move(self):
        return self.propose_move(self.highest_level)
