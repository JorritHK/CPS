# %%

from grid.coord import Coord
from grid.search import bfs, create_node


start = Coord(0, 0)
goal = Coord(2, 3)

grid = [
    [
        create_node([1, 1, 0, -1]),
        create_node([-1, -1, -1, -1]),
        create_node([1, 0, 1, 0]),
        create_node([1, 1, 0, 0]),
    ],
    [
        create_node([0, 0, 0, 1]),
        create_node([1, 0, 1, -1]),
        create_node([1, 0, 1, 0]),
        create_node([0, 1, 0, 0]),
    ],
    [
        create_node([0, 1, 0, 1]),
        create_node([-1, -1, -1, -1]),
        create_node([-1, -1, -1, -1]),
        create_node([0, 1, 0, 0]),
    ],
    [
        create_node([0, 1, 1, 1]),
        create_node([-1, -1, -1, -1]),
        create_node([0, 0, 0, 1]),
        create_node([0, 1, 1, 0]),
    ],
]

path = bfs(grid, start, goal)
print(path)

# %%
