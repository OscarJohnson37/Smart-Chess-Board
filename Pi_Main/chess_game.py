import numpy as np
from copy import deepcopy
import bitmap_utils
import chess
import referee
import chess.engine
STOCKFISH_PATH = "/opt/homebrew/bin/stockfish"

class Game:
    def __init__(self, initial_bitmap=None, starting_to_move='white', starting_turn='player'):
        """
        Initialise the Game with a starting bitmap and player.
        """
        self.bitmap_history = []

        if initial_bitmap is not None:
            self.current_bitmap = np.array(initial_bitmap, dtype=int)
        else:
            self.current_bitmap = bitmap_utils.gamestart_bitmap

        self.to_move = starting_to_move  # 'white' or 'black'
        self.turn = starting_turn # 'player' or 'cpu'
        self.stage = 0
        self.action_square = None
        self.destination_square = None
        self.completed_move = None
        self.bitmap_history.append(deepcopy(self.current_bitmap))
        self.required_bitmap = None

        self.board = chess.Board()

        self.cpu_skill_level = 20
        self.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

        self.engine.configure({"Skill Level": self.cpu_skill_level})

    def update_bitmap(self, new_bitmap):
        """
        Update the bitmap and store the previous state.
        """
        self.bitmap_history.append(deepcopy(self.current_bitmap))
        self.current_bitmap = np.array(new_bitmap, dtype=int)
        diff_indicies = bitmap_utils.find_diff_indices(self.current_bitmap, self.bitmap_history[-1])
        diff_coords = bitmap_utils.indices_to_coords(diff_indicies)

        print(self.stage)

        print(self.current_bitmap)

        if self.turn == 'player':
            match(self.stage):
                case 0:
                    """
                    player stage 0 is where the cpu has just made a move, and the player pick up a piece to move it
                    """
                    if len(diff_coords) == 1:
                        if self.current_bitmap[diff_indicies[0][0]][diff_indicies[1][0]] == 0:
                            self.action_square = diff_coords[0]
                            self.stage = 1
                            print(self.action_square)
                case 1:
                    """
                    player stage 1 is where the player had picked up a piece and will either place it somewhere else, or
                    pick up the piece it wishes to capture
                    """
                    if len(diff_coords) == 1:
                        if self.current_bitmap[diff_indicies[0][0]][diff_indicies[1][0]] == 1:
                            self.destination_square = diff_coords[0]
                            self.stage = 3
                            print(self.destination_square)

                            self.completed_move = chess.Move.from_uci(self.action_square + self.destination_square)
                            print("Move played:", self.completed_move.uci())
                            if referee.is_legal_move(self.completed_move, self.board):
                                self.board.push(self.completed_move)
                                print("Move played:", self.completed_move.uci())
                                self.turn = 'cpu'
                                print(self.board)


                                result = self.engine.play(self.board, chess.engine.Limit(time=0.1))
                                self.board.push(result.move)

                                print("stockfish moves to" , result.move)
                                print(self.board)

                                self.turn = 'player'
                                self.stage = 0

                        else:
                            self.stage = 2
                case 2:
                    if len(diff_coords) == 1:
                        if self.current_bitmap[diff_indicies[0][0]][diff_indicies[1][0]] == 1:
                            self.destination_square = diff_coords[0]
                            self.stage = 3
                            print(self.destination_square)

                            self.completed_move = chess.Move.from_uci(self.action_square + self.destination_square)
                            print("Move played:", self.completed_move.uci())
                            if referee.is_legal_move(self.completed_move, self.board):
                                self.board.push(self.completed_move)
                                print("Move played:", self.completed_move.uci())
                                self.turn = 'cpu'
                                print(self.board)


                                result = self.engine.play(self.board, chess.engine.Limit(time=0.1))
                                self.board.push(result.move)

                                print("stockfish moves to" , result.move)
                                print(self.board)

                                self.turn = 'player'
                                self.stage = 0

                case 3:
                    pass
                    


    def switch_to_move(self):
        """
        Switch to the other colour to move.
        """
        self.to_move = 'black' if self.to_move == 'white' else 'white'


    def undo_move(self):
        """
        Revert to the previous bitmap state, if available.
        """
        if len(self.bitmap_history) > 0:
            self.current_bitmap = self.bitmap_history.pop()
            self.switch_to_move()
        else:
            print("No previous bitmap state to revert to.")

    def print_bitmap(self):
        """
        Print the current bitmap in a readable format.
        """
        print(np.flip(self.current_bitmap, axis=0))  # show from white's perspective

    def get_current_state(self):
        """
        Return a dict of current game state.
        """
        return {
            'bitmap': deepcopy(self.current_bitmap),
            'to move': self.to_move,
            'history_length': len(self.bitmap_history)
        }