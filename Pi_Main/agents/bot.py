import utils.bitmap_utils as butils
from copy import deepcopy
import numpy as np


class Bot:
    def __init__(self, engine, bitmap_container, ai_difficulty=5):
        self.engine = engine
        self.bitmap_container = bitmap_container
        self.ai_difficulty = ai_difficulty

        self.current_bitmap = None

        self.start_bitmap = None            # Bitmap at the beginning of the turn
        self.action_bitmap = None           # Bitmap when the action piece has been picked up
        self.target_bitmap = None           # Bitmap when the target piece has been picked up
        self.final_bitmap = None            # Bitmap when the action piece is placed at the destination square
        self.proposed_move_coords = None    # Coordinates describing the move proposed by the ai, such as e1e2
        self.proposed_move_indicies = None  # Indicies of the coordinates e.g. e1e2 = [7, 6],[4, 4] which are the 

        self.current_stage = 0

    def get_current_bitmap(self):
        self.current_bitmap = deepcopy(self.bitmap_container.current_bitmap)

    def clear_bitmaps(self):
        for i in range(0, len(self.bitmaps)):
            self.bitmaps[i] = None

    def start_turn(self):
        self.current_stage = 0

        self.get_current_bitmap()

        self.start_bitmap = deepcopy(self.current_bitmap)

        self.proposed_move_coords = self.get_ai_move()

        self.proposed_move_indicies = butils.coords_to_indices(self.proposed_move_coords)

        x_start = self.proposed_move_indicies[0][0]
        y_start = self.proposed_move_indicies[1][0]

        self.action_bitmap = deepcopy(self.start_bitmap)
        self.action_bitmap[x_start][y_start] = 0

    def get_ai_move(self):
        return self.engine.propose_move(skill_level=self.ai_difficulty)


    def update(self):

        self.get_current_bitmap()

        match(self.current_stage):
            case 0:

                if np.array_equal(self.current_bitmap, self.action_bitmap):
                    print("Picked up piece at", self.proposed_move_coords)

                    x_target = self.proposed_move_indicies[0][1]
                    y_target = self.proposed_move_indicies[1][1]

                    if self.current_bitmap[x_target][y_target] == 1:
                        self.target_bitmap = deepcopy(self.action_bitmap)
                        self.target_bitmap[x_target][y_target] = 0

                        self.current_stage = 1  # piece needs to be taken
                    else:
                        self.final_bitmap = deepcopy(self.action_bitmap)
                        self.final_bitmap[x_target][y_target] = 0
                        self.current_stage = 2  # piece is being placed in an open sqaure

            case 1:

                if np.array_equal(self.current_bitmap, self.target_bitmap):
                    print("Picked up piece at", self.proposed_move_coords)

                    x_target = self.proposed_move_indicies[0][1]
                    y_target = self.proposed_move_indicies[1][1]

                    if self.current_bitmap[x_target][y_target] == 0:
                        self.final_bitmap = deepcopy(self.target_bitmap)
                        self.final_bitmap[x_target][y_target] = 1

                        self.current_stage = 2 # piece is being placed in an open sqaure
            case 2:
                if np.array_equal(self.current_bitmap, self.final_bitmap):
                    print("Move has been made to", self.proposed_move_coords)

                    self.current_stage = 3 # piece has been placed and the move is complete
            case 3:
                pass