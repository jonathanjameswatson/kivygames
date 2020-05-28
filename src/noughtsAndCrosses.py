from game import Game
import numpy as np

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

        self.game()

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
            if np.diagonal(cells, i).all():
                return True
        return False

    def turn(self):
        while True:
            position = self.getInput('Position', tuple)
            if self.isEmpty(position):
                break
            self.sendOutput('Error', 'That space is already full.')

        self.place(self.player, position)
        if self.hasPlayerWon(self.player):
            self.sendOutput('End', f'Player {self.player} wins.')
            return True
        if np.count_nonzero(self.grid) == 9:
            self.sendOutput('End', f'It\'s a draw!')
            return True
        self.player = abs(self.player - 3)

        return False

    def game(self):
        while True:
            turn = self.turn()
            if (turn):
                break

NoughtsAndCrosses(2, 0)