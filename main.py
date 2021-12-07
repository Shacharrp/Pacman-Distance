import numpy as np
import json
from collections import deque


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Node:
    def __init__(self, pt: Point, dist: int):
        self.dist = dist  # Distance from the source
        self.pt = pt  # Coordinates of the cell


# To get the neighbours of a cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]


def isValid(row: int, col: int, max_row, max_col):
    return (row >= 0) and (row < max_row) and (col >= 0) and (col < max_col)


# Function to find the shortest path using BFS
# Saving the cells already visited and using queue

def BFS(mat, src: Point, dest: Point, max_row, max_col):
    # List to keep track of visited nodes
    visited = [[False for i in range(max_col)] for j in range(max_row)]
    visited[src.x][src.y] = True

    q = deque()
    s = Node(src, 0)
    q.append(s)

    # Run the BFS
    while q:
        curr = q.popleft()
        # Reached destination so we finish
        pt = curr.pt
        if pt.x == 20 and pt.y == 25:
            return curr.dist

        # Otherwise enqueue his neighbours
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
            if (isValid(row, col, max_row, max_col) and
                    mat[row][col] == 0 and
                    not visited[row][col]):
                visited[row][col] = True
                neighbourCell = Node(Point(row, col),
                                     curr.dist + 1)
                q.append(neighbourCell)

    return -1


def calculate_distance():
    board = json.load(open('board1.npy_array.json'))
    board = np.asarray(board)
    mat = board.tolist()
    pacman_location = [np.where(board == 3)[0][0], np.where(board == 3)[1][0]]
    pacman_location = Point(pacman_location[0], pacman_location[1])
    ghosts = np.argwhere(np.array(board) == 2).tolist()
    for ghost in ghosts:
        ghost = Point(ghost[0], ghost[1])
        distance = BFS(board, pacman_location, ghost, np.shape(mat)[0], np.shape(mat)[1])
        print(distance)


calculate_distance()
