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

    def isEmpty(self, position, grid):
        return grid[position] == 0

    def hasPlayerWon(self, player, grid):
        cells = grid == np.full(self.gridShape, player)
        for i in (0, 1):
            if cells.all(axis=i).any():
                return True
        if cells.diagonal().all() or np.fliplr(cells).diagonal().all():
            return True
        return False

    async def turn(self):
        await self.sendOutput('Player', self.player)
        while True:
            position = await self.getInput('Position', tuple, self.player)
            if self.isEmpty(position, self.grid):
                break
            await self.sendOutput('Error', 'That space is already full.')

        self.grid[position] = self.player
        await self.sendOutput('Grid', self.grid)
        if self.hasPlayerWon(self.player, self.grid):
            await self.sendOutput('End', f'Player {self.player} wins.')
            return True
        if np.count_nonzero(self.grid) == 9:
            await self.sendOutput('End', f'It\'s a draw!')
            return True
        self.player = abs(self.player - 3)

        return False

    def getAIInput(self, name):
        if name == 'Position':
            return self.minMax(self.player, self.grid)[1]

    def minMax(self, player, grid, isMin=True):
        bestScore = 0
        bestIndex = None
        for index, cell in np.ndenumerate(grid):
            if not self.isEmpty(index, grid):
                continue
            score = 0
            newGrid = grid.copy()
            newGrid[index] = player
            if self.hasPlayerWon(player, newGrid):
                score = abs(self.player - player) * 2 - 1
            else:
                score = self.minMax(abs(player - 3), newGrid, not isMin)[0]
            if score == bestScore or isMin == (score < bestScore):
                bestScore = score
                bestIndex = index
                if (isMin and bestScore == 1) or (not isMin and bestScore == -1):
                    break
        if bestIndex == None:
            for index, cell in np.ndenumerate(grid):
                if self.isEmpty(index, grid):
                    bestIndex = index
                    break
        return (bestScore, bestIndex)

    async def game(self):
        while True:
            ended = await self.turn()
            if (ended):
                break
        await self.end()
