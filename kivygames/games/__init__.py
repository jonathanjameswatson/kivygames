class IO:
    def __init__(self, *message):
        self.message = message

    def __await__(self):
        response = yield self.message
        return response


class Game:
    minPlayers = 0
    maxPlayers = 0
    hasAI = False

    def __init__(self):
        self.players = None
        self.started = False
        self.generator = self.game()

    async def game(self):
        pass

    def getAIInput(self, name, player):
        pass

    async def getInput(self, name, dataType, player):
        if self.players[player - 1]:
            return self.getAIInput(name)
        response = await IO(True, name, dataType, player)
        return response

    async def sendOutput(self, name, output):
        await IO(False, name, output)

    async def end(self):
        await IO(StopIteration)

    def send(self, message):
        tempMessage = message
        if not self.started:
            self.started = True
            self.players = message
            tempMessage = None
        return self.generator.send(tempMessage)
