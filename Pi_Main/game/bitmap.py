class BitmapContainer:
    def __init__(self, initial_state):
        self.current = initial_state
        self.history = [initial_state]

    def update(self, new_state):
        self.history.append(new_state)
        self.current = new_state

    def get_current(self):
        return self.current

    def get_history(self):
        return self.history

    def reset_history(self):
        self.history = [self.current]
