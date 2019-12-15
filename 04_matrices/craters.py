#!/usr/bin/env python3

"""
    Inits a matrix of size lines x cols with all slots set at value
"""
def init(lines, cols, value):

    visitedMap = []

    for i in range(lines):

        L = []

        for j in range(cols):
            L.append(value)

        visitedMap.append(L)

    return visitedMap

"""
    Creates a matrix from a txt file
"""
def loadMap(filename):

    M = []
    f = open(filename)
    lines = f.readlines()
    f.close()

    for l in lines:
        M.append(l)

    return M;

"""
    Visits the whole crater
"""
def replaceCrater(M, visitedMap, i, j):

    visitedMap[i][j] = True

    if M[i + 1][j] == '#' and visitedMap[i + 1][j] == False:
        replaceCratere(M, visitedMap, i + 1, j)
    if M[i - 1][j] == '#' and visitedMap[i - 1][j] == False:
        replaceCratere(M, visitedMap, i - 1, j)
    if M[i][j + 1] == '#' and visitedMap[i][j + 1] == False:
        replaceCratere(M, visitedMap, i, j + 1)
    if M[i][j - 1] == '#' and visitedMap[i][j - 1] == False:
        replaceCratere(M, visitedMap, i, j - 1)

    if M[i + 1][j + 1] == '#' and visitedMap[i + 1][j + 1] == False:
        replaceCratere(M, visitedMap, i + 1, j + 1)
    if M[i - 1][j + 1] == '#' and visitedMap[i + 1][j + 1] == False:
        replaceCratere(M, visitedMap, i - 1, j + 1)
    if M[i - 1][j - 1] == '#' and visitedMap[i + 1][j - 1] == False:
        replaceCratere(M, visitedMap, i - 1, j - 1)
    if M[i + 1][j - 1] == '#' and visitedMap[i + 1][j - 1] == False:
        replaceCratere(M, visitedMap, i + 1, j - 1)

"""
    Counts the number of craters on the map
"""
def craters(M):

    nbCrateres = 0

    n = len(M)
    m = len(M[0])

    visitedMap = init(n, m, False)

    for i in range(n):

        for j in range(m):

            if M[i][j] == '#' and visitedMap[i][j] == False:
                visitedMap[i][j] = True
                replaceCrater(M, visitedMap, i, j)
                nbCraters += 1

    return nbCrateres

"""
    Displays the number of craters of the loaded map
"""
if __name__ == "__main__":

    marsMap = loadMap("mars1.map")
    nbCrateres = craters(marsMap)
    print(nbCraters)