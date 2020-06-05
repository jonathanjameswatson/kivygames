class Game:
    minPlayers = 0
    maxPlayers = 0
    hasAI = False

    def __init__(self, nPlayers, nAI):
        self.nPlayers = nPlayers
        self.nAI = nAI

    def getInput(self, name, type):
        return eval(input(f'Give a value for {name} as type {type.__name__}: '))

    def sendOutput(self, name, output):
        print(f'{name}: {output}')
