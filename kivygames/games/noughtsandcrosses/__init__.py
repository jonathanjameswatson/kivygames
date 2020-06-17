import asyncio
import numpy as np

from kivygames.games import Game

import kivygames.games.noughtsandcrosses.c as c


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

    async def turn(self):
        await self.sendOutput('Player', self.player)
        while True:
            position = await self.getInput('Position', tuple, self.player)
            if self.isEmpty(position):
                break
            await self.sendOutput('Error', 'That space is already full.')

        self.grid[position] = self.player
        await self.sendOutput('Grid', self.grid)
        if c.hasPlayerWon(self.grid, self.player):
            await self.sendOutput('End', f'Player {self.player} wins.')
            return True
        if np.count_nonzero(self.grid) == 9:
            await self.sendOutput('End', f'It\'s a draw!')
            return True
        self.player = 3 - self.player

        return False

    def getAIInput(self, name):
        if name == 'Position':
            return c.minimax(self.player, self.player, True, self.grid)[1]

    def minMax(self, player, isMin=True):
        bestScore = -2 if isMin else 2
        bestIndex = None
        for index, cell in np.ndenumerate(self.grid):
            if not self.isEmpty(index):
                continue
            self.grid[index] = player
            if self.hasPlayerWon(player):
                score = 1 if self.player == player else -1
            else:
                score = self.minMax(3 - player, not isMin)[0]
            self.grid[index] = 0
            if isMin:
                if score > bestScore:
                    bestScore = score
                    bestIndex = index
                    if bestScore == 1:
                        break
            else:
                if score < bestScore:
                    bestScore = score
                    bestIndex = index
                    if bestScore == -1:
                        break
        if bestIndex == None:
            bestScore = 0
        return (bestScore, bestIndex)

    async def game(self):
        while True:
            ended = await self.turn()
            if (ended):
                break
        await self.end()
