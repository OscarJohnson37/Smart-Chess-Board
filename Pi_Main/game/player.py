import agents

class Player:
    def __init__(self, colour, playerType='human'):
        self.colour = colour # colour is 'black' or 'white'
        self.playerType = playerType

        if playerType == 'human':
            self.agent = agents.Human()
        elif playerType == 'bot':
            self.agent = agents.Bot()


        