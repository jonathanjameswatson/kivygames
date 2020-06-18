cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef bint hasPlayerWon(np.ndarray[np.uint8_t, ndim=2] grid, int player):
    cdef int i, j, count1, count2
    for i in range(3):
        count1 = 0
        count2 = 0
        for j in range(3):
            if grid[i, j] == player:
                count1 += 1
            if grid[j, i] == player:
                count2 += 1
        if count1 == 3 or count2 == 3:
            return True
    count1 = 0
    count2 = 0
    for i in range(3):
        if grid[i, i] == player:
            count1 += 1
        if grid[i, 2 - i] == player:
            count2 += 1
    if count1 == 3 or count2 == 3:
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