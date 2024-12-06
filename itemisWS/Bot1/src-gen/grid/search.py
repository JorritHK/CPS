# %%
# Directions: North (0), East (1), South (2), West (3)
from collections import deque
from grid.coord import Coord, Orientation
from grid.Grid import Node
from typing import List

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # North, East, South, West
direction_names: List[str] = ["NORTH", "EAST", "SOUTH", "WEST"]


def bfs(grid: List[List[Node]], start: Coord, goal: Coord):
    rows, cols = len(grid), len(grid[0])

    visited: set[Coord] = set()  # To track visited nodes
    queue: deque[tuple[Coord, List[Orientation]]] = deque(
        [(start, [])]
    )  # (current_position, path_taken)

    visited.add(start)

    while queue:
        cur, path = queue.popleft()
        # If the goal is reached, return the path]
        x = cur.x
        y = cur.y

        if cur == goal:
            print("Found it")
            return path

        # Explore neighbors (North, East, South, West)
        for i, (dx, dy) in enumerate(directions):
            neighbor = Coord(x + dx, y + dy)

            # Check if new position is within bounds
            if (
                0 <= neighbor.y < rows
                and 0 <= neighbor.x < cols
                and neighbor not in visited
            ):
                print(
                    "Neighbor wall: ",
                    node_has_wall(grid[neighbor.y][neighbor.x], (i + 2) % 4),
                )
                # Check if the move is possible (no wall in the way)
                if not node_has_wall(
                    grid[x][y], i
                ):  # Check current node for wall in direction `i`
                    # Check if there's no wall on the neighboring node in the opposite direction
                    if not node_has_wall(
                        grid[neighbor.y][neighbor.x], (i + 2) % 4
                    ):  # (i+2)%4 to check the opposite direction
                        # print(f"Add to queue: {neighbor}")
                        # print(f"Direction: {direction_names[i]}")
                        visited.add(Coord(neighbor.x, neighbor.y))
                        queue.append(
                            (
                                neighbor,
                                path + [Orientation[direction_names[i]]],
                            )
                        )
        print("Current queue after iteration: ", queue)


def create_node(walls):
    n = Node(0, 0)
    n.walls = walls
    return n


def node_has_wall(node, direction):
    return node.walls[direction] == 1


if __name__ == "__main__":

    start = Coord(0, 0)
    goal = Coord(1, 0)

    print("Start: ", start, "\tGoal: ", goal)
    grid = [[create_node([1, 0, 1, 1]), create_node([1, 1, 0, 0])]]

    # Find the shortest path
    path = bfs(grid, start, goal)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found")
