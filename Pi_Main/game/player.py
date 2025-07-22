import agents

class Player:
    def __init__(self, colour, engine, playerType='human'):
        self.colour = colour # colour is 'black' or 'white'
        self.playerType = playerType

        if playerType == 'human':
            self.agent = agents.Human(engine, bitmap_container, 20)
        elif playerType == 'bot':
            self.agent = agents.Bot(engine, bitmap_container, 5)


        