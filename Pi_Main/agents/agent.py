import utils.bitmap_utils as butils

class Agent:
    def __init__(self, engine, bitmap_container):
        self.engine = engine
        self.bitmap_container = bitmap_container

        self.current_bitmap = None
        self.previous_bitmap = None

        self.start_bitmap = None
        self.action_bitmap = None
        self.target_bitmap = None
        self.final_bitmap = None

        self.current_stage = 0

    def get_current_bitmap(self):
        self.current_bitmap = self.bitmap_container.current_bitmap

    def start_turn(self):
        self.get_current_bitmap()
        self.current_stage = 0
        self.start_bitmap = self.current_bitmap()

    def update_bitmaps(self):
        self.previous_bitmap = self.current_bitmap
        self.current_bitmap = self.bitmap_container.current_bitmap

    def report_updates(self):

        match(self.current_stage):
            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass

