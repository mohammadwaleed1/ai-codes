from queue import PriorityQueue

# 0 = free path, 1 = wall
maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 0]
]

start = (0, 0)   # top left
goal  = (4, 4)   # bottom right


# manhattan distance
def manhattan(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1-x2) + abs(y1-y2)


# get valid neighbors (up, down, left, right)
def get_neighbors(maze, node):
    row, col  = node
    neighbors = []
    rows      = len(maze)
    cols      = len(maze[0])

    # up, down, left, right
    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        # check bounds and not a wall
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if maze[new_row][new_col] == 0:
                neighbors.append((new_row, new_col))

    return neighbors


def gbfs(maze, start, goal):

    visited   = set()
    came_from = {start: None}
    pq        = PriorityQueue()

    # start with real heuristic
    h = manhattan(start, goal)
    pq.put((h, start))

    while not pq.empty():
        cost, node = pq.get()

        if node in visited:
            continue
        visited.add(node)

        print(f"Visiting: {node}  h={cost}")

        # goal found
        if node == goal:

            # reconstruct path
            path = []
            n    = goal
            while n is not None:
                path.append(n)
                n = came_from[n]
            path.reverse()

            print(f"\nPath Found : {path}")
            print(f"Steps      : {len(path)-1}")
            print()
            print("Solved Maze:")
            return

        # explore neighbors
        for neighbor in get_neighbors(maze, node):
            if neighbor not in visited:
                h = manhattan(neighbor, goal)
                came_from[neighbor] = node
                pq.put((h, neighbor))
                print(f"  Added: {neighbor}  h={h}")

    print("No path found!")


gbfs(maze, start, goal)
