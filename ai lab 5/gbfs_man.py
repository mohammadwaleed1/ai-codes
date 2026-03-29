from queue import PriorityQueue

# coordinates for each node (x, y)
coordinates = {
    'S': (0, 0),
    'A': (1, 2),
    'B': (2, 1),
    'C': (1, 1),
    'D': (2, 3),
    'E': (3, 2),
    'F': (4, 1),
    'G': (4, 2),
    'H': (2, 0),
    'I': (3, 0),   # ← goal
    'J': (3, 1)
}

# graph — only stores connections, NO heuristic values
graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],
    'B': ['F', 'G'],
    'C': ['H'],
    'H': ['I', 'J'],
    'D': [], 'E': [], 'F': [],
    'G': [], 'I': [], 'J': []
}


# manhattan distance function
def manhattan(node, goal):
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return abs(x1 - x2) + abs(y1 - y2)


def gbfs(graph, start, goal):
    visited   = set()
    came_from = {start: None}
    pq        = PriorityQueue()

    # heuristic of start node
    h = manhattan(start, goal)
    pq.put((h, start))

    print(f"Start: {start}  h={h}")

    while not pq.empty():
        cost, node = pq.get()

        if node in visited:
            continue
        visited.add(node)

        print(f"Visiting: {node}  h={cost}")

        # goal check
        if node == goal:
            path = []
            n = goal
            while n is not None:
                path.append(n)
                n = came_from[n]
            path.reverse()
            print(f"\nPath Found : {' → '.join(path)}")
            return

        # explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                h = manhattan(neighbor, goal)   # ← calculate heuristic
                came_from[neighbor] = node
                pq.put((h, neighbor))
                print(f"  Added: {neighbor}  h={h}")

    print("Goal not reachable!")


gbfs(graph, 'S', 'I')

import math

# # manhattan
# def manhattan(node, goal):
#     x1, y1 = coordinates[node]
#     x2, y2 = coordinates[goal]
#     return abs(x1-x2) + abs(y1-y2)

# # euclidean
# def euclidean(node, goal):
#     x1, y1 = coordinates[node]
#     x2, y2 = coordinates[goal]
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)