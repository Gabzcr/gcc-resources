from maze import *
from random import random


def init_marked(size):
    marked = []
    for i in range(size):
        line = [False for j in range(size)]
        marked.append(line)
    return marked


def already_in_frontier(frontier, i, j):
    for index in range(len(frontier)):
        if frontier[index][0] == i and frontier[index][1] == j:
            return True
    return False


def mark_cell(marked, frontier, i, j, size):
    marked[i][j] = True
    if i-1 >= 0 and not marked[i-1][j] and not already_in_frontier(frontier, i-1, j):
        frontier.append((i-1, j))
    if i+1 < size and not marked[i+1][j] and not already_in_frontier(frontier, i+1, j):
        frontier.append((i+1, j))
    if j-1 >= 0 and not marked[i][j-1] and not already_in_frontier(frontier, i, j-1):
        frontier.append((i, j-1))
    if j+1 < size and not marked[j+1][j] and not already_in_frontier(frontier, i, j+1):
        frontier.append((i, j+1))


def find_neighbours(marked, i, j, size):
    neighbours = []
    if i-1 >= 0 and marked[i-1, j]:
        neighbours.append(Direction.NORTH)
    if i+1 < size and marked[i+1, j]:
        neighbours.append(Direction.SOUTH)
    if j-1 >= 0 and marked[i, j-1]:
        neighbours.append(Direction.WEST)
    if j+1 < size and marked[i, j+1]:
        neighbours.append(Direction.EAST)

    if len(neighbours) == 0:
        return Direction.NULLDIR
    rand_index = random.randrange(len(neighbours))
    return neighbours[rand_index]


def generate_prim_maze(size, start, end):
    res_maze = Maze(size, start, end)
    marked = init_marked(size)
    frontier = []

    i = random.randrange(size)
    j = random.randrange(size)
    mark_cell(marked, frontier, i, j, size)

    while len(frontier) != 0:
        choose_cell = random.randrange(len(frontier))
        index = frontier[choose_cell]
        frontier.pop(index)
        carve_dir = find_neighbours(marked, index[0], index[1], size)
        res_maze.carve_path(carve_dir)
        mark_cell(marked, frontier, index[0], index[1])

    return res_maze