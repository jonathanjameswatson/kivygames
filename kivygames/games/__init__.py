import asyncio


class IO:
    def __init__(self, message):
        self.message = message

    def __await__(self):
        response = yield self.message
        return response


class Game:
    minPlayers = 0
    maxPlayers = 0
    hasAI = False

    def __init__(self, nPlayers, nAI):
        self.nPlayers = nPlayers
        self.nAI = nAI

        self.generator = self.game()

    async def game(self):
        pass

    async def getInput(self, name, dataType):
        response = await IO((True, name, dataType))
        return response

    async def sendOutput(self, name, output):
        await IO((False, name, output))

    async def end(self):
        await IO(StopIteration)

    def send(self, message):
        return self.generator.send(message)
