import numpy as np

cimport numpy as np
cimport cython

cpdef bint hasPlayerWon(np.ndarray[np.uint8_t, ndim=2] grid, int player):
    cdef np.ndarray[np.uint8_t, ndim=2, cast=True] cells
    cells = grid == np.full((3, 3), player)
    cdef int i
    for i in range(2):
        if cells.all(axis=i).any():
            return True
    if cells.diagonal().all() or np.fliplr(cells).diagonal().all():
        return True
    return False

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef (int, (int, int)) minimax(int player, int originalPlayer, bint isMin, np.ndarray[np.uint8_t, ndim=2] grid):
        cdef int bestScore
        bestScore = -2 if isMin else 2
        cdef int bestPosX = -1, bestPosY = -1
        cdef int x, y
        cdef int score
        for x in range(3):
            for y in range(3):
                if grid[x, y] != 0:
                    continue
                grid[x, y] = player
                if hasPlayerWon(grid, player):
                    score = 1 if originalPlayer == player else -1
                else:
                    score = minimax(3 - player, originalPlayer, not isMin, grid)[0]
                grid[x, y] = 0
                if isMin:
                    if score > bestScore:
                        bestScore = score
                        bestPosX = x
                        bestPosY = y
                        if bestScore == 1:
                            break
                else:
                    if score < bestScore:
                        bestScore = score
                        bestPosX = x
                        bestPosY = y
                        if bestScore == -1:
                            break
        if bestPosX == -1:
            bestScore = 0
        return (bestScore, (bestPosX, bestPosY))