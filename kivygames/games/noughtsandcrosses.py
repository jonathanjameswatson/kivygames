import asyncio
import numpy as np

from kivygames.games import Game


class CellOccupiedError(Exception):
    pass


class NoughtsAndCrosses(Game):
    minPlayers = 1
    maxPlayers = 2
    hasAI = True

    gridShape = (3, 3)

    def __init__(self, nPlayers, nAI):
        Game.__init__(self, nPlayers, nAI)

        self.grid = np.zeros(self.gridShape, dtype='u1')
        self.player = 1

    def isEmpty(self, position):
        return self.grid[position] == 0

    def place(self, player, position):
        if not self.isEmpty(position):
            raise CellOccupiedError

        self.grid[position] = player

    def hasPlayerWon(self, player):
        cells = self.grid == np.full(self.gridShape, player)
        for i in (0, 1):
            if cells.all(axis=i).any():
                return True
        if cells.diagonal().all() or np.fliplr(cells).diagonal().all():
            return True
        return False

    async def turn(self):
        await self.sendOutput('Player', self.player)
        while True:
            position = await self.getInput('Position', tuple)
            if self.isEmpty(position):
                break
            await self.sendOutput('Error', 'That space is already full.')

        self.place(self.player, position)
        await self.sendOutput('Grid', self.grid.flatten().tolist())
        if self.hasPlayerWon(self.player):
            await self.sendOutput('End', f'Player {self.player} wins.')
            return True
        if np.count_nonzero(self.grid) == 9:
            await self.sendOutput('End', f'It\'s a draw!')
            return True
        self.player = abs(self.player - 3)

        return False

    async def game(self):
        while True:
            ended = await self.turn()
            if (ended):
                break
        await self.end()
